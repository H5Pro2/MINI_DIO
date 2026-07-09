from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
INPUT = befunde_root(ROOT) / "1382_FELDFUNKTIONSKARTE_ROHWELT_RUECKLESUNG.csv"
OUT_CSV = befunde_root(ROOT) / "1386_BRUECKE_ZENTRUM_UNTERFORMEN_WIEDERKEHR.csv"
OUT_MD = befunde_root(ROOT) / "1386_BRUECKE_ZENTRUM_UNTERFORMEN_WIEDERKEHR.md"

TARGET_ROLE = "mischrolle_brueckennaehe_zentrumsnaehe"
TARGET_RAW_FORM = "gemischte_rohwelt"

EPISODE_KEYS = [
    "sehen_form_stability",
    "sehen_form_change",
    "hoeren_energy_tone",
    "hoeren_energy_shift",
    "perception_adapted_field_intake_pressure",
    "mcm_feldwirkung_mcm_tension",
]


def _float(row: dict[str, str], key: str) -> float:
    try:
        out = float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if out != out else out


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _avg(rows: list[dict[str, str]], key: str) -> float:
    return mean(_float(row, key) for row in rows) if rows else 0.0


def _quantiles(values: list[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    values = sorted(values)
    lo = values[int((len(values) - 1) * 0.33)]
    hi = values[int((len(values) - 1) * 0.66)]
    return lo, hi


def _tier(value: float, lo: float, hi: float, low: str, mid: str, high: str) -> str:
    if value <= lo:
        return low
    if value >= hi:
        return high
    return mid


def _episode_cache(paths: set[Path]) -> dict[Path, list[dict[str, str]]]:
    return {path: _read_csv(path) for path in paths}


def _episode_rows(cache: dict[Path, list[dict[str, str]]], path: Path, start: int, end: int) -> list[dict[str, str]]:
    rows = cache.get(path, [])
    return [row for row in rows if start <= int(_float(row, "tick")) <= end]


def _window_feature_rows(role_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    paths = {ROOT / row["source"] for row in role_rows}
    cache = _episode_cache(paths)
    out: list[dict[str, str]] = []
    for row in role_rows:
        source_path = ROOT / row["source"]
        start = int(_float(row, "start_tick"))
        end = int(_float(row, "end_tick"))
        episodes = _episode_rows(cache, source_path, start, end)
        merged = dict(row)
        for key in EPISODE_KEYS:
            merged[key] = f"{_avg(episodes, key):.6f}"
        out.append(merged)
    return out


def _attach_signature(rows: list[dict[str, str]], q: dict[str, tuple[float, float]]) -> None:
    for row in rows:
        tone_lo, tone_hi = q["hoeren_energy_tone"]
        shift_lo, shift_hi = q["hoeren_energy_shift"]
        range_lo, range_hi = q["avg_range_pct"]
        change_lo, change_hi = q["direction_change_ratio"]
        persistence_lo, persistence_hi = q["direction_persistence"]
        intake_lo, intake_hi = q["perception_adapted_field_intake_pressure"]
        tension_lo, tension_hi = q["mcm_feldwirkung_mcm_tension"]

        tone = _tier(_float(row, "hoeren_energy_tone"), tone_lo, tone_hi, "leise", "mittlerer_ton", "laut")
        shift = _tier(_float(row, "hoeren_energy_shift"), shift_lo, shift_hi, "ruhiger_ton", "bewegter_ton", "starker_tonwechsel")
        range_state = _tier(_float(row, "avg_range_pct"), range_lo, range_hi, "enge_range", "mittlere_range", "weite_range")
        change_state = _tier(_float(row, "direction_change_ratio"), change_lo, change_hi, "wenig_wechsel", "mittlerer_wechsel", "viel_wechsel")
        persistence = _tier(_float(row, "direction_persistence"), persistence_lo, persistence_hi, "geringe_persistenz", "mittlere_persistenz", "hohe_persistenz")
        intake = _tier(_float(row, "perception_adapted_field_intake_pressure"), intake_lo, intake_hi, "gedaempfte_aufnahme", "mittlere_aufnahme", "starke_aufnahme")
        tension = _tier(_float(row, "mcm_feldwirkung_mcm_tension"), tension_lo, tension_hi, "geringe_feldspannung", "mittlere_feldspannung", "hohe_feldspannung")

        stability = _float(row, "sehen_form_stability")
        visual_change = _float(row, "sehen_form_change")
        if stability > visual_change:
            visual = "stabile_form"
        elif visual_change > stability:
            visual = "bewegte_form"
        else:
            visual = "balancierte_form"

        row["tonale_unterform"] = f"{tone}+{shift}"
        row["visuelle_unterform"] = visual
        row["bewegungs_unterform"] = f"{range_state}+{change_state}+{persistence}"
        row["feldkontakt_unterform"] = f"{intake}+{tension}"
        row["mischlinien_signature"] = "|".join(
            [
                row["tonale_unterform"],
                row["visuelle_unterform"],
                row["bewegungs_unterform"],
                row["feldkontakt_unterform"],
            ]
        )


def _top(counter: Counter[str], n: int = 6) -> str:
    return ", ".join(f"{name}:{count}" for name, count in counter.most_common(n)) or "-"


def build_report() -> None:
    source_rows = _read_csv(INPUT)
    feature_rows = _window_feature_rows(source_rows)
    target_rows = [
        row
        for row in feature_rows
        if row.get("passive_role_near") == TARGET_ROLE and row.get("raw_form") == TARGET_RAW_FORM
    ]
    if not target_rows:
        raise RuntimeError("no target rows for recurrence reference")

    quantile_keys = [
        "hoeren_energy_tone",
        "hoeren_energy_shift",
        "avg_range_pct",
        "direction_change_ratio",
        "direction_persistence",
        "perception_adapted_field_intake_pressure",
        "mcm_feldwirkung_mcm_tension",
    ]
    q = {key: _quantiles([_float(row, key) for row in target_rows]) for key in quantile_keys}
    _attach_signature(feature_rows, q)

    target_signatures = Counter(row["mischlinien_signature"] for row in target_rows)
    strong_target_signatures = {sig for sig, count in target_signatures.items() if count >= 2}
    all_target_signatures = set(target_signatures)

    for row in feature_rows:
        is_target = row.get("passive_role_near") == TARGET_ROLE and row.get("raw_form") == TARGET_RAW_FORM
        row["is_reference_target"] = "1" if is_target else "0"
        row["signature_seen_in_reference"] = "1" if row["mischlinien_signature"] in all_target_signatures else "0"
        row["signature_strong_in_reference"] = "1" if row["mischlinien_signature"] in strong_target_signatures else "0"

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(feature_rows[0].keys()))
        writer.writeheader()
        writer.writerows(feature_rows)

    outside_rows = [row for row in feature_rows if row["is_reference_target"] == "0"]
    outside_seen = [row for row in outside_rows if row["signature_seen_in_reference"] == "1"]
    outside_strong = [row for row in outside_rows if row["signature_strong_in_reference"] == "1"]

    by_role_seen = Counter(row.get("passive_role_near", "-") for row in outside_seen)
    by_role_strong = Counter(row.get("passive_role_near", "-") for row in outside_strong)
    by_world_seen = Counter(row.get("world", "-") for row in outside_seen)
    by_signature_seen = Counter(row.get("mischlinien_signature", "-") for row in outside_seen)
    role_signature: dict[str, Counter[str]] = defaultdict(Counter)
    for row in outside_seen:
        role_signature[row.get("passive_role_near", "-")][row["mischlinien_signature"]] += 1

    role_lines = []
    for role, counter in sorted(role_signature.items()):
        role_lines.append(f"- `{role}`: {_top(counter, 4)}")

    lines = [
        "# 1386 - Bruecke/Zentrum-Unterformen: Wiederkehr",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob die Unterformen aus `1385` nur in der isolierten Mischrolle vorkommen oder auch in anderen Rollenfenstern wieder auftauchen.",
        "",
        "Die Referenz bleibt die Mischrolle:",
        "",
        "```text",
        "mischrolle_brueckennaehe_zentrumsnaehe + gemischte_rohwelt",
        "```",
        "",
        "Die Einteilung wird aus der Referenz gelernt und anschliessend passiv auf alle Rollenfenster aus `1382` angewendet.",
        "",
        "## Befund",
        "",
        f"- Referenzfenster: `{len(target_rows)}`",
        f"- Referenzsignaturen gesamt: `{len(all_target_signatures)}`",
        f"- Referenzsignaturen mit mindestens 2 Treffern: `{len(strong_target_signatures)}`",
        f"- gepruefte Fenster ausserhalb der Referenz: `{len(outside_rows)}`",
        f"- Wiederkehr irgendeiner Referenzsignatur ausserhalb: `{len(outside_seen)}`",
        f"- Wiederkehr starker Referenzsignaturen ausserhalb: `{len(outside_strong)}`",
        f"- Rollen bei Wiederkehr: `{_top(by_role_seen, 8)}`",
        f"- Rollen bei starker Wiederkehr: `{_top(by_role_strong, 8)}`",
        f"- Welten bei Wiederkehr: `{_top(by_world_seen, 8)}`",
        "",
        "## Wiederkehr nach Rollen",
        "",
        *role_lines,
        "",
        "## Dominante wiederkehrende Signaturen",
        "",
        *[f"- `{sig}`: `{count}`" for sig, count in by_signature_seen.most_common(8)],
        "",
        "## Lesung",
        "",
        "Wenn Referenzsignaturen ausserhalb der Mischrolle wieder auftauchen, ist die Unterform nicht nur an eine einzelne Rollenbezeichnung gebunden.",
        "Wenn starke Referenzsignaturen ausserhalb kaum auftauchen, bleibt die Mischrolle dagegen spezifischer.",
        "",
        "Der Befund trennt damit Oberflaechenwiederkehr von Rollenwiederkehr.",
        "Das ist wichtig, weil MINI_DIO dadurch nicht nur Namen, sondern Feldfunktionsnaehen lesen kann.",
        "",
        "## Grenze",
        "",
        "Die Signaturen sind aus einer Referenzprobe abgeleitet.",
        "Sie sind kein abgeschlossenes Lexikon, sondern eine passive Vergleichsschicht.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
