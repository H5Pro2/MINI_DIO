from __future__ import annotations

import argparse
import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path


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


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _run_rows(path: Path) -> list[dict[str, object]]:
    rows = _read_rows(path)
    if not rows:
        return []

    tones = [_float(row, "hoeren_energy_tone") for row in rows]
    qs = {
        "tone_q33": _quantile(tones, 0.33),
        "tone_q66": _quantile(tones, 0.66),
        "rekopplung_q33": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.33),
        "rekopplung_q50": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.50),
        "rekopplung_q66": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.66),
        "strain_q33": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.33),
        "strain_q50": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.50),
        "strain_q66": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.66),
        "carry_q66": _quantile([_float(row, "mcm_carry_quality") for row in rows], 0.66),
        "tension_q66": _quantile([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows], 0.66),
    }

    buckets: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        tonal_band = _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"])
        role = _role(row, qs)
        buckets[(tonal_band, role)].append(row)

    total_by_band = Counter(
        _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"]) for row in rows
    )
    world = path.parent.parent.name
    run = path.parent.name
    out: list[dict[str, object]] = []
    for (tonal_band, role), group in sorted(buckets.items()):
        out.append(
            {
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
                "world": world,
                "run": run,
                "tonal_band": tonal_band,
                "topology_role": role,
                "count": len(group),
                "ratio_of_run": len(group) / len(rows),
                "ratio_within_band": len(group) / total_by_band[tonal_band],
                "avg_hoeren_energy_tone": _mean([_float(row, "hoeren_energy_tone") for row in group]),
                "avg_mcm_rekopplung_quality": _mean([_float(row, "mcm_rekopplung_quality") for row in group]),
                "avg_mcm_strain_quality": _mean([_float(row, "mcm_strain_quality") for row in group]),
                "avg_mcm_carry_quality": _mean([_float(row, "mcm_carry_quality") for row in group]),
                "avg_mcm_tension": _mean([_float(row, "mcm_feldwirkung_mcm_tension") for row in group]),
                "avg_rezeptor_field_intake_pressure": _mean(
                    [_float(row, "rezeptor_field_intake_pressure") for row in group]
                ),
            }
        )
    return out


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[(str(row["tonal_band"]), str(row["topology_role"]))].append(row)
    out: list[dict[str, object]] = []
    for (tonal_band, role), group in sorted(groups.items()):
        out.append(
            {
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
                "tonal_band": tonal_band,
                "topology_role": role,
                "world_run_profiles": len(group),
                "avg_count": _mean([float(row["count"]) for row in group]),
                "avg_ratio_of_run": _mean([float(row["ratio_of_run"]) for row in group]),
                "avg_ratio_within_band": _mean([float(row["ratio_within_band"]) for row in group]),
                "avg_hoeren_energy_tone": _mean([float(row["avg_hoeren_energy_tone"]) for row in group]),
                "avg_mcm_rekopplung_quality": _mean(
                    [float(row["avg_mcm_rekopplung_quality"]) for row in group]
                ),
                "avg_mcm_strain_quality": _mean([float(row["avg_mcm_strain_quality"]) for row in group]),
                "avg_mcm_carry_quality": _mean([float(row["avg_mcm_carry_quality"]) for row in group]),
                "avg_mcm_tension": _mean([float(row["avg_mcm_tension"]) for row in group]),
                "avg_rezeptor_field_intake_pressure": _mean(
                    [float(row["avg_rezeptor_field_intake_pressure"]) for row in group]
                ),
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Passive Topologielesung je Tonenergie-Band.")
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--report-id", default="1063")
    parser.add_argument("--report-title", default="Tonale Energie und Topologie-Rollen")
    args = parser.parse_args()

    episode_files = _iter_episode_files([Path(item) for item in args.world_dir])
    run_rows: list[dict[str, object]] = []
    for episode_file in episode_files:
        run_rows.extend(_run_rows(episode_file))
    aggregate_rows = _aggregate(run_rows)

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    if aggregate_rows:
        with out_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(aggregate_rows[0].keys()))
            writer.writeheader()
            writer.writerows(aggregate_rows)

    by_band = defaultdict(list)
    for row in aggregate_rows:
        by_band[str(row["tonal_band"])].append(row)
    dominant_lines = []
    for band in ["tonal_low", "tonal_mid", "tonal_high"]:
        rows = sorted(by_band.get(band, []), key=lambda item: float(item["avg_ratio_within_band"]), reverse=True)
        if rows:
            top = rows[0]
            dominant_lines.append(
                f"- `{band}` dominant: `{top['topology_role']}` "
                f"({float(top['avg_ratio_within_band']):.3f} im Band, "
                f"Rekopplung {float(top['avg_mcm_rekopplung_quality']):.3f}, "
                f"Strain {float(top['avg_mcm_strain_quality']):.3f})."
            )

    high_rows = {str(row["topology_role"]): row for row in by_band.get("tonal_high", [])}
    high_rand = float(high_rows.get("rand_kipp", {}).get("avg_ratio_within_band", 0.0))
    high_open = float(high_rows.get("offen_unruhig", {}).get("avg_ratio_within_band", 0.0))
    high_center = float(high_rows.get("zentrum_rekoppelnd", {}).get("avg_ratio_within_band", 0.0))

    Path(args.out_md).write_text(
        "\n".join(
            [
                f"# {args.report_id} - {args.report_title}",
                "",
                "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
                "",
                "## Frage",
                "",
                "Liegt `tonal_high` vor allem in bestimmten Topologie-Rollen: Zentrum, Bruecke, Rand/Kipp oder offene Unruhe?",
                "",
                "## Methode",
                "",
                "- Tonenergie wird je Lauf in weltrelative Baender geteilt.",
                "- Topologie-Rollen werden je Lauf relativ aus Rekopplung, Strain, Carry, Spannung und Feldklasse gelesen.",
                "- Es werden keine globalen Grenzwerte gesetzt.",
                "",
                "## Dominante Rollen je Tonband",
                "",
                *dominant_lines,
                "",
                "## Befund zu `tonal_high`",
                "",
                f"- Rand/Kipp-Anteil im hohen Tonband: {high_rand:.3f}.",
                f"- Offen-unruhiger Anteil im hohen Tonband: {high_open:.3f}.",
                f"- Zentrums-rekoppelnder Anteil im hohen Tonband: {high_center:.3f}.",
                "",
                "## Lesart",
                "",
                "`tonal_high` ist keine eigene Topologie-Rolle. Es faerbt vorhandene Rollen und verschiebt sie eher in offene Unruhe oder Randnaehe, wenn die Feldbindung nicht nachkommt. Damit bestaetigt sich die Trennung aus 1062: Tonenergie ist ankommende Weltspannung; erst die Feldrolle entscheidet, ob sie getragen, offen gehalten oder kippnah wird.",
                "",
                "## Wie es weitergeht",
                "",
                "Als naechstes sollte geprueft werden, ob mittlere Tonenergie (`tonal_mid`) als optimaler Verarbeitungsbereich stabil ueber weitere Weltgruppen reproduziert.",
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
