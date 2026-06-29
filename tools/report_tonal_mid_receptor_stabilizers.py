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


def _summarize_run(path: Path, tonal_band_name: str, target_role: str) -> list[dict[str, object]]:
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

    band_rows = [
        row
        for row in rows
        if _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"]) == tonal_band_name
    ]
    if not band_rows:
        return []

    target = [row for row in band_rows if _role(row, qs) == target_role]
    other = [row for row in band_rows if _role(row, qs) != target_role]
    out: list[dict[str, object]] = []
    for receptor_label, column in RECEPTOR_METRICS:
        center_avg = _mean([_float(row, column) for row in target])
        other_avg = _mean([_float(row, column) for row in other])
        out.append(
            {
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
                "world": path.parent.parent.name,
                "run": path.parent.name,
                "tonal_band": tonal_band_name,
                "target_role": target_role,
                "receptor_axis": receptor_label,
                "source_column": column,
                "band_count": len(band_rows),
                "target_count": len(target),
                "other_count": len(other),
                "target_avg": center_avg,
                "other_avg": other_avg,
                "target_minus_other": center_avg - other_avg,
                "target_rekopplung_avg": _mean([_float(row, "mcm_rekopplung_quality") for row in target]),
                "other_rekopplung_avg": _mean([_float(row, "mcm_rekopplung_quality") for row in other]),
                "target_strain_avg": _mean([_float(row, "mcm_strain_quality") for row in target]),
                "other_strain_avg": _mean([_float(row, "mcm_strain_quality") for row in other]),
            }
        )
    return out


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[str(row["receptor_axis"])].append(row)

    out: list[dict[str, object]] = []
    for receptor_axis, group in sorted(groups.items()):
        source_column = str(group[0]["source_column"])
        delta = _mean([float(row["target_minus_other"]) for row in group])
        abs_delta = abs(delta)
        if abs_delta >= 0.045:
            strength = "stark"
        elif abs_delta >= 0.020:
            strength = "mittel"
        elif abs_delta >= 0.008:
            strength = "schwach"
        else:
            strength = "kaum_trennend"
        direction = "hoeher_im_zentrum" if delta > 0 else "niedriger_im_zentrum" if delta < 0 else "gleich"
        out.append(
            {
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
                "receptor_axis": receptor_axis,
                "source_column": source_column,
                "tonal_band": str(group[0]["tonal_band"]),
                "target_role": str(group[0]["target_role"]),
                "run_profiles": len(group),
                "avg_band_count": _mean([float(row["band_count"]) for row in group]),
                "avg_target_count": _mean([float(row["target_count"]) for row in group]),
                "avg_other_count": _mean([float(row["other_count"]) for row in group]),
                "target_avg": _mean([float(row["target_avg"]) for row in group]),
                "other_avg": _mean([float(row["other_avg"]) for row in group]),
                "target_minus_other": delta,
                "direction": direction,
                "separation_strength": strength,
                "target_rekopplung_avg": _mean([float(row["target_rekopplung_avg"]) for row in group]),
                "other_rekopplung_avg": _mean([float(row["other_rekopplung_avg"]) for row in group]),
                "target_strain_avg": _mean([float(row["target_strain_avg"]) for row in group]),
                "other_strain_avg": _mean([float(row["other_strain_avg"]) for row in group]),
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Passive Pruefung: Welche Rezeptorhaltung stabilisiert tonal_mid?"
    )
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--tonal-band", default="tonal_mid")
    parser.add_argument("--target-role", default="zentrum_rekoppelnd")
    parser.add_argument("--report-id", default="1067")
    parser.add_argument("--report-title", default="Rezeptorhaltung von tonal_mid")
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    episode_files = _iter_episode_files([Path(item) for item in args.world_dir])
    run_rows: list[dict[str, object]] = []
    for episode_file in episode_files:
        run_rows.extend(_summarize_run(episode_file, args.tonal_band, args.target_role))

    aggregate_rows = _aggregate(run_rows)
    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    if aggregate_rows:
        with out_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(aggregate_rows[0].keys()))
            writer.writeheader()
            writer.writerows(aggregate_rows)

    strongest = sorted(aggregate_rows, key=lambda row: abs(float(row["target_minus_other"])), reverse=True)
    strongest_lines = [
        f"- `{row['receptor_axis']}`: {float(row['target_minus_other']):.6f} "
        f"({row['direction']}, {row['separation_strength']})."
        for row in strongest[:6]
    ]
    positive = [row for row in strongest if float(row["target_minus_other"]) > 0][:4]
    negative = [row for row in strongest if float(row["target_minus_other"]) < 0][:4]

    Path(args.out_md).write_text(
        "\n".join(
            [
                f"# {args.report_id} - {args.report_title}",
                "",
                "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
                "",
                "## Frage",
                "",
                f"Welche Rezeptorhaltung unterscheidet innerhalb von `{args.tonal_band}` die Zielrolle `{args.target_role}` von den uebrigen Episoden?",
                "",
                "## Methode",
                "",
                "- Je Lauf wird Tonenergie weltrelativ in `tonal_low`, `tonal_mid`, `tonal_high` geteilt.",
                f"- Nur `{args.tonal_band}` wird betrachtet.",
                f"- Innerhalb von `{args.tonal_band}` wird `{args.target_role}` gegen die uebrigen Episoden gelesen.",
                "- Die Rollen werden relativ aus Rekopplung, Strain, Carry, Spannung und Feldklasse abgeleitet.",
                "- Es werden keine globalen Grenzwerte gesetzt.",
                "",
                "## Staerkste Trennachsen",
                "",
                *strongest_lines,
                "",
                "## Hoeher in der Zielrolle",
                "",
                *[
                    f"- `{row['receptor_axis']}` ({float(row['target_minus_other']):.6f})."
                    for row in positive
                ],
                "",
                "## Niedriger in der Zielrolle",
                "",
                *[
                    f"- `{row['receptor_axis']}` ({float(row['target_minus_other']):.6f})."
                    for row in negative
                ],
                "",
                "## Lesart",
                "",
                f"Die Rolle `{args.target_role}` innerhalb von `{args.tonal_band}` entsteht nicht durch Tonenergie allein. Sie wird durch eine Rezeptorhaltung mitgetragen, die bestimmte Aufnahmequalitaeten erhoeht und andere reduziert. Entscheidend ist damit Ton plus Aufnahmehaltung plus Feldantwort.",
                "",
                "## Wie es weitergeht",
                "",
                "Als naechstes sollte aus dieser Gegenlesung eine kurze Synthese gebildet werden: welche Rezeptorhaltung stabilisiert Verarbeitung, und welche Haltung begleitet Kippnaehe?",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
