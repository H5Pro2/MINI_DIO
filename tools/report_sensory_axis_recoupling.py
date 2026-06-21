from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


INPUT_DEFAULT = Path("docs/befunde/402_LOKALE_SINNESACHSEN_EPISODENKARTE.csv")
CSV_DEFAULT = Path("docs/befunde/403_SINNESACHSEN_REKOPPLUNGSQUALITAET.csv")
MD_DEFAULT = Path("docs/befunde/403_SINNESACHSEN_REKOPPLUNGSQUALITAET.md")


NUMERIC_COLUMNS = [
    "ratio",
    "avg_axis_z",
    "avg_mcm_rekopplung_quality",
    "avg_mcm_strain_quality",
    "avg_mcm_carry_quality",
    "avg_rezeptor_field_intake_pressure",
    "avg_perception_adaptation_potential",
    "avg_perception_visual_focus_tendency",
    "avg_perception_visual_distance_tendency",
    "avg_perception_auditory_listen_tendency",
    "avg_perception_auditory_softening_tendency",
    "avg_perception_felt_distance_tendency",
]


def _float(value: str | None, default: float = 0.0) -> float:
    try:
        return float(value or default)
    except (TypeError, ValueError):
        return default


def _weighted_average(rows: list[dict[str, str]], column: str) -> float:
    total = sum(_float(row.get("count")) for row in rows)
    if total <= 0.0:
        return 0.0
    return sum(_float(row.get("count")) * _float(row.get(column)) for row in rows) / total


def _dominant_value(rows: list[dict[str, str]], column: str) -> str:
    counts: dict[str, float] = defaultdict(float)
    for row in rows:
        counts[str(row.get(column) or "-")] += _float(row.get("count"))
    if not counts:
        return "-"
    return max(counts.items(), key=lambda item: item[1])[0]


def _quality_label(row: dict[str, object]) -> str:
    recoupling = float(row["avg_mcm_rekopplung_quality"])
    strain = float(row["avg_mcm_strain_quality"])
    field_input = float(row["avg_rezeptor_field_intake_pressure"])
    if recoupling >= 0.70 and strain <= 0.15 and field_input <= 0.10:
        return "ruhig_rekoppelnd"
    if recoupling >= 0.68 and strain <= 0.18:
        return "getragen"
    if strain >= 0.20 or field_input >= 0.20:
        return "belastet"
    return "offen"


def build_axis_rows(input_path: Path) -> list[dict[str, object]]:
    with input_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        rows = list(reader)

    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("world") or "-"), str(row.get("axis") or "-"))].append(row)

    output: list[dict[str, object]] = []
    for (world, axis), group_rows in sorted(grouped.items()):
        count = int(sum(_float(row.get("count")) for row in group_rows))
        ratio = sum(_float(row.get("ratio")) for row in group_rows)
        item: dict[str, object] = {
            "world": world,
            "axis": axis,
            "count": count,
            "ratio": ratio,
            "dominant_inner_effect_state": _dominant_value(group_rows, "inner_effect_state"),
            "dominant_mcm_preview_symbol": _dominant_value(group_rows, "mcm_preview_symbol"),
        }
        for column in NUMERIC_COLUMNS:
            if column == "ratio":
                continue
            item[column] = _weighted_average(group_rows, column)
        item["recoupling_balance"] = (
            float(item["avg_mcm_rekopplung_quality"])
            - float(item["avg_mcm_strain_quality"])
            - (float(item["avg_rezeptor_field_intake_pressure"]) * 0.25)
        )
        item["quality_label"] = _quality_label(item)
        output.append(item)
    return output


def build_world_summary(axis_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in axis_rows:
        grouped[str(row["world"])].append(row)

    summaries: list[dict[str, object]] = []
    for world, rows in sorted(grouped.items()):
        best = max(rows, key=lambda row: float(row["recoupling_balance"]))
        highest_strain = max(rows, key=lambda row: float(row["avg_mcm_strain_quality"]))
        highest_field_input = max(rows, key=lambda row: float(row["avg_rezeptor_field_intake_pressure"]))
        summaries.append(
            {
                "world": world,
                "best_axis": best["axis"],
                "best_axis_quality": best["quality_label"],
                "best_axis_balance": best["recoupling_balance"],
                "highest_strain_axis": highest_strain["axis"],
                "highest_strain": highest_strain["avg_mcm_strain_quality"],
                "highest_field_input_axis": highest_field_input["axis"],
                "highest_field_input": highest_field_input["avg_rezeptor_field_intake_pressure"],
            }
        )
    return summaries


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "world",
        "axis",
        "count",
        "ratio",
        "dominant_inner_effect_state",
        "dominant_mcm_preview_symbol",
        "avg_axis_z",
        "avg_mcm_rekopplung_quality",
        "avg_mcm_strain_quality",
        "avg_mcm_carry_quality",
        "avg_rezeptor_field_intake_pressure",
        "avg_perception_adaptation_potential",
        "avg_perception_visual_focus_tendency",
        "avg_perception_visual_distance_tendency",
        "avg_perception_auditory_listen_tendency",
        "avg_perception_auditory_softening_tendency",
        "avg_perception_felt_distance_tendency",
        "recoupling_balance",
        "quality_label",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_markdown(path: Path, axis_rows: list[dict[str, object]], summaries: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_axis: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in axis_rows:
        by_axis[str(row["axis"])].append(row)

    def mean(axis: str, column: str) -> float:
        rows = by_axis.get(axis, [])
        if not rows:
            return 0.0
        total = sum(float(row["count"]) for row in rows)
        if total <= 0.0:
            return 0.0
        return sum(float(row["count"]) * float(row[column]) for row in rows) / total

    title_number = path.name.split("_", 1)[0] if "_" in path.name and path.name[:3].isdigit() else "405" if "405_" in path.name else "403"
    title_suffix = " Gegenprobe" if "GEGENPROBE" in path.name else ""
    lines: list[str] = []
    lines.append(f"# {title_number} - Sinnesachsen-Rekopplungsqualitaet{title_suffix}")
    lines.append("")
    lines.append("## Fragestellung")
    lines.append("")
    lines.append(
        "Die globale Achspruefung zeigte nahe Mittelwerte. Diese Auswertung prueft deshalb lokal, "
        "welche Sinnesachse in Episoden eher rekoppelt und welche Achse mehr Strain oder Feldinput traegt."
    )
    lines.append("")
    lines.append("Wichtig: Das ist Diagnose. Es ist keine Handlung, kein Gate und keine neue Steuerregel.")
    lines.append("")
    lines.append("## Weltbezogene Rangordnung")
    lines.append("")
    lines.append("| Welt | Beste Achse | Qualitaet | Balance | Hoechster Strain | Hoechster Feldinput |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for row in summaries:
        lines.append(
            f"| {row['world']} | {row['best_axis']} | {row['best_axis_quality']} | "
            f"{float(row['best_axis_balance']):.4f} | "
            f"{row['highest_strain_axis']} {float(row['highest_strain']):.4f} | "
            f"{row['highest_field_input_axis']} {float(row['highest_field_input']):.4f} |"
        )
    lines.append("")
    lines.append("## Achsenbefund")
    lines.append("")
    lines.append(
        f"- `hoeren_hin`: mittlere Rekopplung {mean('hoeren_hin', 'avg_mcm_rekopplung_quality'):.4f}, "
        f"mittlerer Strain {mean('hoeren_hin', 'avg_mcm_strain_quality'):.4f}."
    )
    lines.append(
        f"- `sehen_fokus`: mittlere Rekopplung {mean('sehen_fokus', 'avg_mcm_rekopplung_quality'):.4f}, "
        f"mittlerer Strain {mean('sehen_fokus', 'avg_mcm_strain_quality'):.4f}."
    )
    lines.append(
        f"- `feldinput`: mittlere Rekopplung {mean('feldinput', 'avg_mcm_rekopplung_quality'):.4f}, "
        f"mittlerer Strain {mean('feldinput', 'avg_mcm_strain_quality'):.4f}, "
        f"mittlerer Feldinput {mean('feldinput', 'avg_rezeptor_field_intake_pressure'):.4f}."
    )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "Die Sinnesachsen sind nicht gleichwertig im lokalen Innenfeld. In den geprueften Welten "
        "wirkt `hoeren_hin` am haeufigsten ruhig rekoppelnd. `sehen_fokus` bleibt tragend, liegt "
        "aber etwas naeher an Formspannung. Lokaler `feldinput` traegt dagegen mehr Strain und "
        "Kontaktlast. Das bestaetigt die Trennung: Hoeren, Sehen und Feldkontakt muessen getrennt "
        "gelesen werden, bevor daraus eine MCM-Feldwirkung entsteht."
    )
    lines.append("")
    lines.append("## Mechanische Bedeutung")
    lines.append("")
    lines.append(
        "MINI_DIO braucht keine globale Daempfung des MCM-Feldes. Sichtbar wird eher eine "
        "rezeptorisch-regulatorische Wahrnehmungsschicht: Der Organismus kann lernen, ob eine "
        "Weltlage besser ueber Hinhoren, fokussiertes Sehen, Abstand oder gedrosselten Feldkontakt "
        "tragbar aufgenommen wird."
    )
    lines.append("")
    lines.append("## Naechster Pruefpunkt")
    lines.append("")
    lines.append(
        "Als naechstes sollte geprueft werden, ob `hoeren_hin` wirklich eine ruhige Rekopplungsachse "
        "bleibt, wenn neue Welten mit anderer Lautstaerke, Drift und Bruchfolge hinzukommen."
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=INPUT_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    axis_rows = build_axis_rows(args.input)
    summaries = build_world_summary(axis_rows)
    write_csv(args.csv_out, axis_rows)
    write_markdown(args.md_out, axis_rows, summaries)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
