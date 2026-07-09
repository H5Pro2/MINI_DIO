from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
INPUT = befunde_root(ROOT) / "1382_FELDFUNKTIONSKARTE_ROHWELT_RUECKLESUNG.csv"
OUT_CSV = befunde_root(ROOT) / "1385_BRUECKE_ZENTRUM_MISCHROLLE_UNTERFORMEN.csv"
OUT_MD = befunde_root(ROOT) / "1385_BRUECKE_ZENTRUM_MISCHROLLE_UNTERFORMEN.md"

TARGET_ROLE = "mischrolle_brueckennaehe_zentrumsnaehe"
TARGET_RAW_FORM = "gemischte_rohwelt"

EPISODE_KEYS = [
    "sehen_form_flow",
    "sehen_form_stability",
    "sehen_form_change",
    "hoeren_energy_tone",
    "hoeren_energy_shift",
    "rezeptor_visual_form_salience",
    "rezeptor_visual_memory_recall",
    "rezeptor_auditory_stimulation",
    "rezeptor_direct_contact_pressure",
    "rezeptor_field_intake_pressure",
    "perception_focus_strength",
    "perception_distance_need",
    "perception_auditory_loudness",
    "perception_auditory_softening",
    "perception_visual_sharpness",
    "perception_visual_blur",
    "perception_felt_pressure",
    "perception_felt_relaxation",
    "perception_adapted_field_intake_pressure",
    "perception_regulation_damping",
    "mcm_feldwirkung_mcm_coherence",
    "mcm_feldwirkung_mcm_tension",
    "mcm_feldwirkung_mcm_asymmetry",
    "fuehlen_mcm_coherence",
    "fuehlen_mcm_tension",
    "fuehlen_mcm_asymmetry",
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


def _episode_window_cache(paths: set[Path]) -> dict[Path, list[dict[str, str]]]:
    return {path: _read_csv(path) for path in paths}


def _episode_rows(cache: dict[Path, list[dict[str, str]]], path: Path, start: int, end: int) -> list[dict[str, str]]:
    rows = cache.get(path, [])
    return [row for row in rows if start <= int(_float(row, "tick")) <= end]


def _build_window_rows() -> list[dict[str, str]]:
    role_rows = [
        row
        for row in _read_csv(INPUT)
        if row.get("passive_role_near") == TARGET_ROLE and row.get("raw_form") == TARGET_RAW_FORM
    ]
    paths = {ROOT / row["source"] for row in role_rows}
    cache = _episode_window_cache(paths)

    out: list[dict[str, str]] = []
    for row in role_rows:
        source_path = ROOT / row["source"]
        start = int(_float(row, "start_tick"))
        end = int(_float(row, "end_tick"))
        episodes = _episode_rows(cache, source_path, start, end)
        merged = {
            "world": row.get("world", "-"),
            "source": row.get("source", "-"),
            "start_tick": str(start),
            "end_tick": str(end),
            "preview": row.get("preview", "-"),
            "family": row.get("family", "-"),
            "preview_carry_next": row.get("preview_carry_next", "0"),
            "drift_pct": row.get("drift_pct", "0"),
            "abs_drift_pct": row.get("abs_drift_pct", "0"),
            "avg_abs_return_pct": row.get("avg_abs_return_pct", "0"),
            "avg_range_pct": row.get("avg_range_pct", "0"),
            "max_range_pct": row.get("max_range_pct", "0"),
            "direction_change_ratio": row.get("direction_change_ratio", "0"),
            "direction_persistence": row.get("direction_persistence", "0"),
        }
        for key in EPISODE_KEYS:
            merged[key] = f"{_avg(episodes, key):.6f}"
        out.append(merged)
    return out


def build_report() -> None:
    rows = _build_window_rows()
    if not rows:
        raise RuntimeError("no mixed role rows")

    q = {
        key: _quantiles([_float(row, key) for row in rows])
        for key in [
            "hoeren_energy_tone",
            "hoeren_energy_shift",
            "sehen_form_stability",
            "sehen_form_change",
            "avg_range_pct",
            "direction_change_ratio",
            "direction_persistence",
            "perception_adapted_field_intake_pressure",
            "mcm_feldwirkung_mcm_tension",
        ]
    }

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

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    signatures = Counter(row["mischlinien_signature"] for row in rows)
    tones = Counter(row["tonale_unterform"] for row in rows)
    visuals = Counter(row["visuelle_unterform"] for row in rows)
    motions = Counter(row["bewegungs_unterform"] for row in rows)
    contacts = Counter(row["feldkontakt_unterform"] for row in rows)
    worlds = Counter(row["world"] for row in rows)
    family_by_signature: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        family_by_signature[row["mischlinien_signature"]][row["family"]] += 1

    top_signature_lines = []
    for signature, count in signatures.most_common(8):
        fams = ", ".join(f"{k}:{v}" for k, v in family_by_signature[signature].most_common(4))
        top_signature_lines.append(f"- `{signature}`: `{count}` Fenster; Familien: `{fams}`")

    lines = [
        "# 1385 - Bruecke/Zentrum-Mischrolle: Unterformen",
        "",
        "## Zweck",
        "",
        "Diese Diagnose zerlegt die staerkste Mischrolle aus `1383` und `1384` feiner.",
        "",
        "Geprueft wird, welche Ton-, Sicht-, Bewegungs- und Feldkontakt-Unterformen innerhalb der Kopplung vorkommen.",
        "Die Einteilung erfolgt relativ innerhalb der isolierten Mischrollenfenster, nicht ueber feste globale Regeln.",
        "",
        "Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.",
        "",
        "## Befund",
        "",
        f"- Fenster: `{len(rows)}`",
        f"- Welten: `{', '.join(f'{k}:{v}' for k, v in worlds.most_common())}`",
        f"- Tonale Unterformen: `{', '.join(f'{k}:{v}' for k, v in tones.most_common())}`",
        f"- Visuelle Unterformen: `{', '.join(f'{k}:{v}' for k, v in visuals.most_common())}`",
        f"- Bewegungs-Unterformen: `{', '.join(f'{k}:{v}' for k, v in motions.most_common())}`",
        f"- Feldkontakt-Unterformen: `{', '.join(f'{k}:{v}' for k, v in contacts.most_common())}`",
        "",
        "## Dominante Signaturen",
        "",
        *top_signature_lines,
        "",
        "## Lesung",
        "",
        "Die Mischrolle zerfaellt nicht in eine einzelne starre Rohform.",
        "Sie bleibt eine Kopplungslinie, zeigt aber mehrere Unterformen.",
        "",
        "Wichtig ist dabei: Die Unterformen entstehen nicht als neue Handlungsklassen.",
        "Sie beschreiben, wie MINI_DIO innerhalb derselben Feldrolle unterschiedlich sieht, hoert und Feldkontakt aufnimmt.",
        "",
        "Das stuetzt die Deutung als dynamische Feldfunktion: eine Rolle kann stabil sein, ohne immer dieselbe Oberflaeche zu haben.",
        "",
        "## Grenze",
        "",
        "Die Unterformen sind relative Lesarten innerhalb dieser Probe.",
        "Sie muessen spaeter gegen andere Welten und frische Memories geprueft werden, bevor sie als stabile Teilrollen gelten.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
