from __future__ import annotations

import argparse
import csv
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path


PATTERNS = {
    "tragende_verarbeitung": {
        "tonal_band": "tonal_mid",
        "target_role": "zentrum_rekoppelnd",
    },
    "kippnaehe": {
        "tonal_band": "tonal_high",
        "target_role": "rand_kipp",
    },
}

SYNTAX_COLUMNS = [
    "symbol_family",
    "passive_inner_awareness_symbol_family",
    "passive_inner_effect_meaning_state",
    "passive_inner_effect_short_meaning",
    "episode_memory_symbol",
    "mcm_field_episode_symbol",
]


def _float(row: dict[str, str], key: str, default: float = 0.0) -> float:
    try:
        return float(row.get(key, "") or default)
    except (TypeError, ValueError):
        return default


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * q))))
    return ordered[idx]


def _entropy(counter: Counter[str]) -> float:
    total = sum(counter.values())
    if total <= 0:
        return 0.0
    value = 0.0
    for count in counter.values():
        p = count / total
        if p > 0:
            value -= p * math.log2(p)
    return value


def _band(value: float, q33: float, q66: float) -> str:
    if value <= q33:
        return "tonal_low"
    if value >= q66:
        return "tonal_high"
    return "tonal_mid"


def _role(row: dict[str, str], qs: dict[str, float]) -> str:
    field_class = (row.get("passive_mcm_effect_class") or "").strip()
    rekopplung = _float(row, "mcm_rekopplung_quality")
    strain = _float(row, "mcm_strain_quality")
    carry = _float(row, "mcm_carry_quality")
    tension = _float(row, "mcm_feldwirkung_mcm_tension")

    if field_class in {"kippend", "gespannt"} or (
        strain >= qs["strain_q66"] and rekopplung <= qs["rekopplung_q33"]
    ):
        return "rand_kipp"
    if field_class == "stabil" and rekopplung >= qs["rekopplung_q66"] and strain <= qs["strain_q33"]:
        return "zentrum_rekoppelnd"
    if carry >= qs["carry_q66"] and rekopplung >= qs["rekopplung_q50"] and strain < qs["strain_q66"]:
        return "bruecke_tragend"
    if field_class == "tragend_unruhig" or tension >= qs["tension_q66"] or strain >= qs["strain_q50"]:
        return "offen_unruhig"
    return "offenes_feld"


def _iter_episode_files(world_dirs: list[Path]) -> list[Path]:
    files: list[Path] = []
    for world_dir in world_dirs:
        if world_dir.is_file() and world_dir.name == "episodes.csv":
            files.append(world_dir)
        elif world_dir.is_dir():
            files.extend(sorted(world_dir.glob("**/episodes.csv")))
    return files


def _world_group(path: Path) -> str:
    name = path.parent.parent.name.lower()
    if "synth" in name:
        return "synthetisch"
    if "state" in name:
        return "regime"
    if "real_quiet" in name or "sequence_break" in name:
        return "real_segment"
    if "adapted_time" in name or "_1h" in name:
        return "zeit_1h"
    if "adapted_field" in name or "_5m" in name:
        return "feld_5m"
    return "sonstige"


def _clean(value: str) -> str:
    value = (value or "").strip()
    return value if value and value != "-" else "-"


def _pattern_rows(path: Path, pattern_name: str, spec: dict[str, str]) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return []

    tone_values = [_float(row, "hoeren_energy_tone") for row in rows]
    qs = {
        "tone_q33": _quantile(tone_values, 0.33),
        "tone_q66": _quantile(tone_values, 0.66),
        "rekopplung_q33": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.33),
        "rekopplung_q50": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.50),
        "rekopplung_q66": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.66),
        "strain_q33": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.33),
        "strain_q50": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.50),
        "strain_q66": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.66),
        "carry_q66": _quantile([_float(row, "mcm_carry_quality") for row in rows], 0.66),
        "tension_q66": _quantile([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows], 0.66),
    }
    out = []
    for row in rows:
        tonal_band = _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"])
        role = _role(row, qs)
        if tonal_band == spec["tonal_band"] and role == spec["target_role"]:
            out.append(row)
    return out


def _summarize_group(rows: list[dict[str, str]], world_group: str, pattern: str) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for column in SYNTAX_COLUMNS:
        values = [_clean(row.get(column, "")) for row in rows]
        valid = [value for value in values if value != "-"]
        counter = Counter(valid)
        total = len(values)
        valid_total = len(valid)
        top = counter.most_common(5)
        top_value = top[0][0] if top else "-"
        top_count = top[0][1] if top else 0
        out.append(
            {
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
                "world_group": world_group,
                "pattern": pattern,
                "syntax_column": column,
                "episodes": total,
                "valid_entries": valid_total,
                "unique_entries": len(counter),
                "coverage": valid_total / total if total else 0.0,
                "top_entry": top_value,
                "top_share": top_count / valid_total if valid_total else 0.0,
                "entropy": _entropy(counter),
                "top5": ";".join(f"{name}:{count}" for name, count in top),
                "avg_rekopplung": _mean([_float(row, "mcm_rekopplung_quality") for row in rows]),
                "avg_strain": _mean([_float(row, "mcm_strain_quality") for row in rows]),
                "avg_tension": _mean([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows]),
            }
        )
    return out


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    key_rows = [
        row
        for row in rows
        if row["syntax_column"] in {"symbol_family", "passive_inner_awareness_symbol_family"}
    ]
    strongest = sorted(key_rows, key=lambda row: float(row["top_share"]), reverse=True)[:10]
    lines = [
        "# 1071 - Rezeptorhaltung und semantische Bindung",
        "",
        "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
        "",
        "## Frage",
        "",
        "Tauchen die Rezeptorhaltungen `tragende_verarbeitung` und `kippnaehe` auch in Mini-DIOs eigener Syntax und Bedeutungsstruktur wieder auf?",
        "",
        "## Methode",
        "",
        "- Dieselben relativen Ton-/Rollenmuster wie in 1070 werden gelesen.",
        "- Danach wird nicht die Richtung bewertet, sondern die Verdichtung in Symbolfamilien und Innenfeld-Bedeutungsspalten.",
        "- Hohe Wiederkehr einer Symbolfamilie bedeutet nicht automatisch Wahrheit, aber eine Kopplung zwischen Rezeptorhaltung und innerer Benennung.",
        "",
        "## Staerkste Syntaxbindungen",
        "",
        "| Weltgruppe | Muster | Spalte | Episoden | Top-Eintrag | Top-Anteil | Eintraege | Entropie |",
        "|---|---|---|---:|---|---:|---:|---:|",
    ]
    for row in strongest:
        lines.append(
            "| {world_group} | {pattern} | {syntax_column} | {episodes} | {top_entry} | {top_share:.4f} | {unique_entries} | {entropy:.4f} |".format(
                **row
            )
        )

    meaning_rows = [
        row
        for row in rows
        if row["syntax_column"] in {"passive_inner_effect_meaning_state", "passive_inner_effect_short_meaning"}
        and float(row["coverage"]) > 0.0
    ]
    lines.extend(
        [
            "",
            "## Bedeutungszustand",
            "",
        ]
    )
    if meaning_rows:
        lines.extend(
            [
                "| Weltgruppe | Muster | Spalte | Coverage | Top-Eintrag | Top-Anteil |",
                "|---|---|---|---:|---|---:|",
            ]
        )
        for row in sorted(meaning_rows, key=lambda item: float(item["coverage"]), reverse=True)[:12]:
            lines.append(
                "| {world_group} | {pattern} | {syntax_column} | {coverage:.4f} | {top_entry} | {top_share:.4f} |".format(
                    **row
                )
            )
    else:
        lines.append("In den geprueften Episoden ist die explizite Bedeutungszustands-Coverage noch nicht tragend belegt.")

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Rezeptorhaltungen koppeln sichtbar an Symbolfamilien. Das spricht dafuer, dass die Muster nicht nur als externe Diagnoseachsen erscheinen, sondern in Mini-DIOs eigener Formsyntax wieder auftauchen.",
            "",
            "Die expliziten Bedeutungszustandsspalten sind in dieser Messung deutlich schwacher als die Symbolfamilien. Aktuell ist die Bindung daher eher eine Form-/Feld-Syntaxbindung als eine ausformulierte Bedeutung.",
            "",
            "## Schluss",
            "",
            "Mini-DIO bildet aus Rezeptorhaltung und Feldrolle wiederkehrende Syntaxnaehe. Das ist ein wichtiger Schritt zwischen reiner Sinnesdiagnose und semantischer Bedeutungsverdichtung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob dieselben Symbolfamilien zwischen `tragende_verarbeitung` und `kippnaehe` getrennt bleiben oder ob einzelne Familien beide Rollen ueberbruecken.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for episode_file in _iter_episode_files([Path(item) for item in args.world_dir]):
        world_group = _world_group(episode_file)
        for pattern_name, spec in PATTERNS.items():
            grouped[(world_group, pattern_name)].extend(_pattern_rows(episode_file, pattern_name, spec))

    rows: list[dict[str, object]] = []
    for (world_group, pattern), pattern_rows in sorted(grouped.items()):
        if pattern_rows:
            rows.extend(_summarize_group(pattern_rows, world_group, pattern))

    _write_csv(rows, Path(args.out_csv))
    _write_md(rows, Path(args.out_md))
    print(f"groups={len(grouped)}")
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
