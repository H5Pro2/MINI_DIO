from __future__ import annotations

import argparse
import csv
import statistics
from pathlib import Path


FIELDS = [
    "hoeren_energy_tone",
    "mcm_rekopplung_quality",
    "mcm_strain_quality",
    "mcm_carry_quality",
    "rezeptor_field_intake_pressure",
    "perception_auditory_loudness",
    "perception_auditory_listen_tendency",
    "perception_auditory_softening_tendency",
    "perception_adapted_field_intake_pressure",
    "mcm_feldwirkung_mcm_tension",
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


def _iter_episode_files(world_dirs: list[Path]) -> list[Path]:
    files: list[Path] = []
    for world_dir in world_dirs:
        if world_dir.is_file() and world_dir.name == "episodes.csv":
            files.append(world_dir)
        elif world_dir.is_dir():
            files.extend(sorted(world_dir.glob("**/episodes.csv")))
    return files


def _summarize_run(path: Path) -> list[dict[str, object]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return []

    tones = [_float(row, "hoeren_energy_tone") for row in rows]
    q33 = _quantile(tones, 0.33)
    q66 = _quantile(tones, 0.66)
    world_baseline = {field: _mean([_float(row, field) for row in rows]) for field in FIELDS}

    buckets: dict[str, list[dict[str, str]]] = {"tonal_low": [], "tonal_mid": [], "tonal_high": []}
    for row in rows:
        buckets[_band(_float(row, "hoeren_energy_tone"), q33, q66)].append(row)

    world = path.parent.parent.name
    run = path.parent.name
    out: list[dict[str, object]] = []
    for band_name, band_rows in buckets.items():
        entry: dict[str, object] = {
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
            "world": world,
            "run": run,
            "tonal_band": band_name,
            "count": len(band_rows),
            "ratio": len(band_rows) / len(rows),
        }
        for field in FIELDS:
            avg = _mean([_float(row, field) for row in band_rows])
            entry[f"avg_{field}"] = avg
            entry[f"delta_{field}_vs_world"] = avg - world_baseline[field]
        entry["rekopplung_minus_strain"] = (
            float(entry["avg_mcm_rekopplung_quality"]) - float(entry["avg_mcm_strain_quality"])
        )
        out.append(entry)
    return out


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, object]]] = {}
    for row in rows:
        groups.setdefault((str(row["world"]), str(row["tonal_band"])), []).append(row)

    out: list[dict[str, object]] = []
    for (world, band), group_rows in sorted(groups.items()):
        entry: dict[str, object] = {
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
            "world": world,
            "tonal_band": band,
            "runs": len(group_rows),
            "avg_count": _mean([float(row["count"]) for row in group_rows]),
            "avg_ratio": _mean([float(row["ratio"]) for row in group_rows]),
        }
        for key in rows[0].keys():
            if key.startswith("avg_") or key.startswith("delta_") or key == "rekopplung_minus_strain":
                entry[key] = _mean([float(row[key]) for row in group_rows])
        out.append(entry)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Passive Gegenprobe: tonale Energie gegen MCM-Feldrollen lesen."
    )
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    episode_files = _iter_episode_files([Path(item) for item in args.world_dir])
    run_rows: list[dict[str, object]] = []
    for episode_file in episode_files:
        run_rows.extend(_summarize_run(episode_file))

    aggregate_rows = _aggregate(run_rows) if run_rows else []
    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    if aggregate_rows:
        with out_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(aggregate_rows[0].keys()))
            writer.writeheader()
            writer.writerows(aggregate_rows)

    high = [row for row in aggregate_rows if row["tonal_band"] == "tonal_high"]
    low = [row for row in aggregate_rows if row["tonal_band"] == "tonal_low"]
    high_balance = _mean([float(row["rekopplung_minus_strain"]) for row in high])
    low_balance = _mean([float(row["rekopplung_minus_strain"]) for row in low])
    high_strain_delta = _mean([float(row["delta_mcm_strain_quality_vs_world"]) for row in high])
    low_strain_delta = _mean([float(row["delta_mcm_strain_quality_vs_world"]) for row in low])
    high_rekopplung_delta = _mean([float(row["delta_mcm_rekopplung_quality_vs_world"]) for row in high])
    low_rekopplung_delta = _mean([float(row["delta_mcm_rekopplung_quality_vs_world"]) for row in low])

    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(
        "\n".join(
            [
                "# 1062 - Tonale Energie gegen Feldrollen",
                "",
                "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
                "",
                "## Frage",
                "",
                "Ist `tonale_energie` nur in der Rohwelt-Ruecklesung auffaellig, oder zeigt sie auch gegen vorhandene Sinnes- und Feldrollen eine eigene Qualitaet?",
                "",
                "## Methode",
                "",
                "- Episoden werden je Lauf in weltrelative Tonenergie-Baender geteilt: `tonal_low`, `tonal_mid`, `tonal_high`.",
                "- Danach werden Rekopplung, Strain, Carry, Feldaufnahme, Lautheit, Hinhoeren und Daempfung gegen die jeweilige Weltbasis gelesen.",
                "- Die Baender sind relativ zur jeweiligen Welt und daher kein globaler Schwellenwert.",
                "",
                "## Befund",
                "",
                f"- Ausgewertete Episoden-Dateien: {len(episode_files)}.",
                f"- Ausgewertete Welt/Band-Profile: {len(aggregate_rows)}.",
                f"- `tonal_high` Rekopplung-minus-Strain: {high_balance:.6f}.",
                f"- `tonal_low` Rekopplung-minus-Strain: {low_balance:.6f}.",
                f"- `tonal_high` Strain-Delta zur Weltbasis: {high_strain_delta:.6f}.",
                f"- `tonal_low` Strain-Delta zur Weltbasis: {low_strain_delta:.6f}.",
                f"- `tonal_high` Rekopplungs-Delta zur Weltbasis: {high_rekopplung_delta:.6f}.",
                f"- `tonal_low` Rekopplungs-Delta zur Weltbasis: {low_rekopplung_delta:.6f}.",
                "",
                "## Lesart",
                "",
                "Die Rohenergie des Hoerens ist nicht identisch mit geordnetem Hinhoeren. Hohe tonale Energie kann als Rohbelastung oder Fragmentierungsnaehe erscheinen, waehrend `hoeren_hin` in den Sinnesachsen eine geordnete Rezeptorhaltung beschreibt.",
                "",
                "Damit trennt sich die Mechanik sauberer:",
                "",
                "- Tonenergie = ankommende akustisch-energetische Weltspannung.",
                "- Hinhoeren = rezeptorische Haltung des Organismus gegenueber dieser Spannung.",
                "- Rekopplung = Feld kann die Spannung wieder einordnen.",
                "- Fragmentierung = Feld verliert zeitweise Bindung oder muss neu organisieren.",
                "",
                "## Schluss",
                "",
                "Die tonale Achse ist relevant, aber nicht direkt als Handlung oder Richtung zu lesen. Fuer MINI_DIO bedeutet das: Hoeren braucht weiterhin rezeptorische Regulation. Nicht lauter Ton ist wichtig, sondern ob das Feld den Ton tragen, daempfen oder neu ordnen kann.",
                "",
                "## Wie es weitergeht",
                "",
                "Als naechstes sollte geprueft werden, ob `tonal_high` vor allem an bestimmten Topologie-Rollen liegt: Zentrum, Bruecke, Rand oder offene Pole.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"wrote {out_csv}")
    print(f"wrote {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
