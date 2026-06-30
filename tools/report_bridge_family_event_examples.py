from __future__ import annotations

import argparse
import csv
from pathlib import Path

from report_bridge_family_rawworld_windows import (
    PATTERNS,
    _band,
    _field_label,
    _float,
    _iter_episode_files,
    _quantile,
    _role,
    _tone_label,
    _visual_label,
    _world_group,
)


def _matches(row: dict[str, str], pattern: str, qs: dict[str, float]) -> bool:
    spec = PATTERNS[pattern]
    band = _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"])
    role = _role(row, qs)
    return band == spec["tonal_band"] and role == spec["target_role"]


def _summarize_file(path: Path, family: str, window: int) -> list[dict[str, object]]:
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
    out: list[dict[str, object]] = []
    for idx, row in enumerate(rows):
        if (row.get("symbol_family") or "").strip() != family:
            continue
        for pattern in PATTERNS:
            if not _matches(row, pattern, qs):
                continue
            before = rows[max(0, idx - window) : idx] or [row]
            before_tension = sum(_float(item, "mcm_feldwirkung_mcm_tension") for item in before) / len(before)
            before_rekopplung = sum(_float(item, "mcm_rekopplung_quality") for item in before) / len(before)
            before_strain = sum(_float(item, "mcm_strain_quality") for item in before) / len(before)
            out.append(
                {
                    "passive_only": 1,
                    "read_by_mini_dio": 0,
                    "influences_action": 0,
                    "is_gate": 0,
                    "is_motoric": 0,
                    "is_entry_signal": 0,
                    "is_direction_signal": 0,
                    "world_group": _world_group(path),
                    "world": path.parent.parent.name,
                    "run": path.parent.name,
                    "family": family,
                    "pattern": pattern,
                    "tick": int(_float(row, "tick")),
                    "timestamp_ms": row.get("timestamp_ms", ""),
                    "visual": _visual_label(row),
                    "tone": _tone_label(row),
                    "field": _field_label(row),
                    "before_tension": before_tension,
                    "target_tension": _float(row, "mcm_feldwirkung_mcm_tension"),
                    "delta_tension": _float(row, "mcm_feldwirkung_mcm_tension") - before_tension,
                    "before_rekopplung": before_rekopplung,
                    "target_rekopplung": _float(row, "mcm_rekopplung_quality"),
                    "delta_rekopplung": _float(row, "mcm_rekopplung_quality") - before_rekopplung,
                    "before_strain": before_strain,
                    "target_strain": _float(row, "mcm_strain_quality"),
                    "delta_strain": _float(row, "mcm_strain_quality") - before_strain,
                    "visual_sharpness": _float(row, "perception_visual_sharpness"),
                    "visual_distance": _float(row, "perception_visual_distance_tendency"),
                    "auditory_loudness": _float(row, "perception_auditory_loudness"),
                    "auditory_listen": _float(row, "perception_auditory_listen_tendency"),
                    "raw_field_intake": _float(row, "perception_raw_field_intake_pressure"),
                    "adapted_field_intake": _float(row, "perception_adapted_field_intake_pressure"),
                }
            )
    return out


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _report_title(path: Path, fallback: str) -> str:
    stem = path.stem
    if "_" not in stem:
        return fallback
    prefix, rest = stem.split("_", 1)
    if not prefix.isdigit():
        return fallback
    return f"{prefix} - {rest.replace('_', ' ').title()}"


def _write_md(rows: list[dict[str, object]], path: Path, family: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        lines = [
            f"# {_report_title(path, f'Einzelereignisse Brueckenfamilie {family}')}",
            "",
            "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
            "",
            "## Befund",
            "",
            f"Fuer die Familie `{family}` wurden in den geprueften Weltverzeichnissen keine passenden Ereignisse gefunden.",
            "",
            "## Lesart",
            "",
            "Das widerlegt die Familie nicht. Es zeigt nur, dass sie in dieser Weltgruppe nicht als passende Brueckenlesart auftritt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Familie gegen eine andere Weltgruppe oder mit einer breiteren Rohwelt-Lupe geprueft werden.",
        ]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return
    representative = sorted(
        rows,
        key=lambda row: (
            str(row["pattern"]),
            -abs(float(row["delta_tension"])) - abs(float(row["delta_rekopplung"])),
        ),
    )[:30]
    lines = [
        f"# {_report_title(path, f'Einzelereignisse Brueckenfamilie {family}')}",
        "",
        "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
        "",
        "## Frage",
        "",
        f"Wie sieht die reale Rueckkopplung der Brueckenfamilie `{family}` in einzelnen Rohweltfenstern aus?",
        "",
        "## Repraesentative Ereignisse",
        "",
        "| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |",
        "|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in representative:
        lines.append(
            "| {world_group} | {world} | {pattern} | {tick} | {visual} | {tone} | {field} | {delta_tension:.4f} | {delta_rekopplung:.4f} | {delta_strain:.4f} | {target_tension:.4f} | {target_rekopplung:.4f} | {target_strain:.4f} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.",
            "",
            "Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:",
            "",
            "```text",
            "innere Familie allein reicht nicht;",
            "Realitaetsrueckkopplung entscheidet die aktuelle Lesart.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--family", required=True)
    parser.add_argument("--window", type=int, default=8)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    rows: list[dict[str, object]] = []
    for episode_file in _iter_episode_files([Path(item) for item in args.world_dir]):
        rows.extend(_summarize_file(episode_file, args.family, args.window))
    _write_csv(rows, Path(args.out_csv))
    _write_md(rows, Path(args.out_md), args.family)
    print(f"events={len(rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
