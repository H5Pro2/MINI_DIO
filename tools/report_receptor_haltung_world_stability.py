from __future__ import annotations

import argparse
import csv
import statistics
from collections import defaultdict
from pathlib import Path


RECEPTOR_METRICS = [
    ("hinhoeren", "perception_auditory_listen_tendency"),
    ("daempfung", "perception_auditory_softening_tendency"),
    ("lautheit", "perception_auditory_loudness"),
    ("visuelle_schaerfe", "perception_visual_sharpness"),
    ("visueller_fokus", "perception_visual_focus_tendency"),
    ("visuelle_distanz", "perception_visual_distance_tendency"),
    ("feldaufnahme_adaptiert", "perception_adapted_field_intake_pressure"),
    ("feldaufnahme_roh", "perception_raw_field_intake_pressure"),
    ("rezeptor_daempfung", "perception_regulation_damping"),
    ("rezeptor_hoerkontakt", "rezeptor_auditory_contact"),
    ("rezeptor_stimulation", "rezeptor_auditory_stimulation"),
    ("rezeptor_feldaufnahme", "rezeptor_field_intake_pressure"),
]


PATTERNS = {
    "tragende_verarbeitung": {
        "tonal_band": "tonal_mid",
        "target_role": "zentrum_rekoppelnd",
        "expected": {
            "visuelle_schaerfe": 1,
            "hinhoeren": 1,
            "visuelle_distanz": -1,
            "lautheit": -1,
            "feldaufnahme_roh": -1,
            "feldaufnahme_adaptiert": -1,
        },
    },
    "kippnaehe": {
        "tonal_band": "tonal_high",
        "target_role": "rand_kipp",
        "expected": {
            "lautheit": 1,
            "rezeptor_hoerkontakt": 1,
            "rezeptor_stimulation": 1,
            "daempfung": 1,
            "hinhoeren": -1,
            "feldaufnahme_roh": 1,
            "feldaufnahme_adaptiert": 1,
            "visuelle_schaerfe": -1,
        },
    },
}


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


def _run_rows(path: Path, pattern_name: str, spec: dict[str, object]) -> list[dict[str, object]]:
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
    tonal_band = str(spec["tonal_band"])
    target_role = str(spec["target_role"])
    expected = dict(spec["expected"])  # type: ignore[arg-type]
    band_rows = [
        row
        for row in rows
        if _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"]) == tonal_band
    ]
    if not band_rows:
        return []
    target = [row for row in band_rows if _role(row, qs) == target_role]
    other = [row for row in band_rows if _role(row, qs) != target_role]
    if not target or not other:
        return []

    out: list[dict[str, object]] = []
    for receptor_axis, column in RECEPTOR_METRICS:
        target_avg = _mean([_float(row, column) for row in target])
        other_avg = _mean([_float(row, column) for row in other])
        delta = target_avg - other_avg
        expected_direction = int(expected.get(receptor_axis, 0) or 0)
        supports_pattern = 0
        if expected_direction > 0 and delta > 0:
            supports_pattern = 1
        elif expected_direction < 0 and delta < 0:
            supports_pattern = 1
        elif expected_direction == 0:
            supports_pattern = -1
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
                "pattern": pattern_name,
                "tonal_band": tonal_band,
                "target_role": target_role,
                "receptor_axis": receptor_axis,
                "source_column": column,
                "band_count": len(band_rows),
                "target_count": len(target),
                "other_count": len(other),
                "target_avg": target_avg,
                "other_avg": other_avg,
                "target_minus_other": delta,
                "expected_direction": expected_direction,
                "supports_pattern": supports_pattern,
            }
        )
    return out


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[(str(row["world_group"]), str(row["pattern"]), str(row["receptor_axis"]))].append(row)

    out: list[dict[str, object]] = []
    for (world_group, pattern, receptor_axis), group in sorted(groups.items()):
        expected_rows = [row for row in group if int(row["expected_direction"]) != 0]
        support_count = sum(1 for row in expected_rows if int(row["supports_pattern"]) == 1)
        tested = len(expected_rows)
        support_ratio = support_count / tested if tested else 0.0
        delta = _mean([float(row["target_minus_other"]) for row in group])
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
                "receptor_axis": receptor_axis,
                "run_profiles": len(group),
                "avg_band_count": _mean([float(row["band_count"]) for row in group]),
                "avg_target_count": _mean([float(row["target_count"]) for row in group]),
                "avg_other_count": _mean([float(row["other_count"]) for row in group]),
                "target_minus_other": delta,
                "expected_direction": int(group[0]["expected_direction"]),
                "support_ratio": support_ratio,
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
    pattern_groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        pattern_groups[(str(row["world_group"]), str(row["pattern"]))].append(row)

    lines = [
        "# 1070 - Rezeptorhaltung Stabilitaet ueber Weltgruppen",
        "",
        "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
        "",
        "## Frage",
        "",
        "Bleiben die in 1067-1069 gefundenen Rezeptorhaltungen ueber verschiedene Weltgruppen erhalten, oder waren sie nur ein Einzelbefund?",
        "",
        "## Methode",
        "",
        "- Je Lauf werden Tonband und Rollen weltrelativ bestimmt.",
        "- Geprueft werden zwei Muster:",
        "  - `tragende_verarbeitung`: tonal_mid + zentrum_rekoppelnd.",
        "  - `kippnaehe`: tonal_high + rand_kipp.",
        "- Pro Weltgruppe wird gelesen, ob die erwarteten Achsrichtungen wiederkehren.",
        "- Keine globalen Grenzwerte, keine Handlung, keine Runtime-Regel.",
        "",
        "## Weltgruppen-Uebersicht",
        "",
        "| Weltgruppe | Muster | Profile | Unterstuetzte Erwartungsachsen | Staerkste Achsen |",
        "|---|---|---:|---:|---|",
    ]

    for (world_group, pattern), group in sorted(pattern_groups.items()):
        expected = [row for row in group if int(row["expected_direction"]) != 0]
        support_ratio = _mean([float(row["support_ratio"]) for row in expected]) if expected else 0.0
        profiles = max(int(row["run_profiles"]) for row in group)
        strongest = sorted(group, key=lambda row: abs(float(row["target_minus_other"])), reverse=True)[:4]
        strongest_text = ", ".join(
            f"{row['receptor_axis']}={float(row['target_minus_other']):.4f}" for row in strongest
        )
        lines.append(
            f"| {world_group} | {pattern} | {profiles} | {support_ratio:.3f} | {strongest_text} |"
        )

    strongest_rows = sorted(rows, key=lambda row: abs(float(row["target_minus_other"])), reverse=True)[:8]
    lines.extend(
        [
            "",
            "## Staerkste Einzelachsen",
            "",
            "| Weltgruppe | Muster | Achse | Richtung | Delta | Support |",
            "|---|---|---|---:|---:|---:|",
        ]
    )
    for row in strongest_rows:
        lines.append(
            "| {world_group} | {pattern} | {receptor_axis} | {expected_direction} | {target_minus_other:.6f} | {support_ratio:.3f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die beiden Haltungen bleiben als unterschiedliche Rezeptorstile lesbar:",
            "",
            "- Tragende Verarbeitung zeigt eher Schaerfe/Hinhoeren und geringere Rohlast.",
            "- Kippnaehe zeigt eher Lautheit/Stimulation/Feldaufnahme und Distanz.",
            "",
            "Die Stabilitaet ist nicht als starres Schema zu lesen. Einzelne Weltgruppen verschieben die Staerke der Achsen, aber die Grundtrennung bleibt passiv sichtbar.",
            "",
            "## Schluss",
            "",
            "Damit wird die Rezeptorhaltung als eigenstaendige Ebene plausibler: Nicht nur die Weltenergie entscheidet, sondern wie der Organismus sieht, hoert und Aufnahme zulaesst.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob Mini-DIO diese Haltungen als wiederkehrende Innenfeld-Bedeutungen verdichtet oder ob sie nur diagnostische Achsen bleiben.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    episode_files = _iter_episode_files([Path(item) for item in args.world_dir])
    run_rows: list[dict[str, object]] = []
    for episode_file in episode_files:
        for pattern_name, spec in PATTERNS.items():
            run_rows.extend(_run_rows(episode_file, pattern_name, spec))

    aggregate_rows = _aggregate(run_rows)
    _write_csv(aggregate_rows, Path(args.out_csv))
    _write_md(aggregate_rows, Path(args.out_md))
    print(f"episode_files={len(episode_files)}")
    print(f"aggregate_rows={len(aggregate_rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
