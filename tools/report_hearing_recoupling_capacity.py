from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


INPUT_DEFAULT = Path("docs/befunde/404_SINNESACHSEN_EPISODENKARTE_GEGENPROBE.csv")
CSV_DEFAULT = Path("docs/befunde/406_HOEREN_HIN_REKOPPLUNGSFAEHIGKEIT.csv")
MD_DEFAULT = Path("docs/befunde/406_HOEREN_HIN_REKOPPLUNGSFAEHIGKEIT.md")

NUMERIC_COLUMNS = [
    "count",
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


def _float(value: object, default: float = 0.0) -> float:
    try:
        return float(value or default)
    except (TypeError, ValueError):
        return default


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


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


def _recoupling_balance(item: dict[str, object]) -> float:
    return (
        float(item["avg_mcm_rekopplung_quality"])
        - float(item["avg_mcm_strain_quality"])
        - (float(item["avg_rezeptor_field_intake_pressure"]) * 0.25)
    )


def _axis_aggregate(world: str, axis: str, rows: list[dict[str, str]]) -> dict[str, object]:
    item: dict[str, object] = {
        "world": world,
        "axis": axis,
        "count": int(sum(_float(row.get("count")) for row in rows)),
        "ratio": sum(_float(row.get("ratio")) for row in rows),
        "dominant_inner_effect_state": _dominant_value(rows, "inner_effect_state"),
        "dominant_mcm_preview_symbol": _dominant_value(rows, "mcm_preview_symbol"),
    }
    for column in NUMERIC_COLUMNS:
        if column in {"count", "ratio"}:
            continue
        item[column] = _weighted_average(rows, column)
    item["recoupling_balance"] = _recoupling_balance(item)
    return item


def _inner_effect_ratio(rows: list[dict[str, str]], marker: str) -> float:
    total = sum(_float(row.get("count")) for row in rows)
    if total <= 0.0:
        return 0.0
    count = sum(
        _float(row.get("count"))
        for row in rows
        if marker in str(row.get("inner_effect_state") or "")
    )
    return count / total


def _reading_label(hearing_rank: int, gap_to_second: float, strain_delta_vs_field: float) -> str:
    if hearing_rank == 1 and gap_to_second >= 0.010 and strain_delta_vs_field < 0.0:
        return "ruhige_hinhoerfaehigkeit"
    if hearing_rank <= 2 and strain_delta_vs_field < 0.0:
        return "tragende_hinhoernaehe"
    return "offene_hinhoerdiagnose"


def build_rows(input_path: Path) -> list[dict[str, object]]:
    raw_rows = _read_rows(input_path)
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in raw_rows:
        grouped[(str(row.get("world") or "-"), str(row.get("axis") or "-"))].append(row)

    by_world: dict[str, list[dict[str, object]]] = defaultdict(list)
    raw_by_world_axis: dict[tuple[str, str], list[dict[str, str]]] = {}
    for (world, axis), rows in grouped.items():
        aggregate = _axis_aggregate(world, axis, rows)
        by_world[world].append(aggregate)
        raw_by_world_axis[(world, axis)] = rows

    output: list[dict[str, object]] = []
    for world, axis_rows in sorted(by_world.items()):
        ranked = sorted(axis_rows, key=lambda row: float(row["recoupling_balance"]), reverse=True)
        ranks = {str(row["axis"]): index + 1 for index, row in enumerate(ranked)}
        hearing = next((row for row in axis_rows if row["axis"] == "hoeren_hin"), None)
        field = next((row for row in axis_rows if row["axis"] == "feldinput"), None)
        visual = next((row for row in axis_rows if row["axis"] == "sehen_fokus"), None)
        if hearing is None:
            continue
        second_balance = float(ranked[1]["recoupling_balance"]) if len(ranked) > 1 and ranked[0]["axis"] == "hoeren_hin" else float(ranked[0]["recoupling_balance"])
        if ranked and ranked[0]["axis"] != "hoeren_hin":
            second_balance = float(ranked[0]["recoupling_balance"])
        gap_to_second = float(hearing["recoupling_balance"]) - second_balance
        strain_delta_vs_field = float(hearing["avg_mcm_strain_quality"]) - float(field["avg_mcm_strain_quality"]) if field else 0.0
        fieldinput_delta_vs_field = float(hearing["avg_rezeptor_field_intake_pressure"]) - float(field["avg_rezeptor_field_intake_pressure"]) if field else 0.0
        balance_delta_vs_visual = float(hearing["recoupling_balance"]) - float(visual["recoupling_balance"]) if visual else 0.0
        hearing_rows = raw_by_world_axis.get((world, "hoeren_hin"), [])
        output.append(
            {
                "world": world,
                "hearing_rank": ranks.get("hoeren_hin", 0),
                "hearing_count": hearing["count"],
                "hearing_ratio": hearing["ratio"],
                "hearing_balance": hearing["recoupling_balance"],
                "gap_to_next_axis": gap_to_second,
                "balance_delta_vs_visual_focus": balance_delta_vs_visual,
                "strain_delta_vs_fieldinput_axis": strain_delta_vs_field,
                "fieldinput_delta_vs_fieldinput_axis": fieldinput_delta_vs_field,
                "hearing_rekopplung": hearing["avg_mcm_rekopplung_quality"],
                "hearing_strain": hearing["avg_mcm_strain_quality"],
                "hearing_field_input": hearing["avg_rezeptor_field_intake_pressure"],
                "hearing_stable_ratio": _inner_effect_ratio(hearing_rows, "stable"),
                "hearing_unrest_ratio": _inner_effect_ratio(hearing_rows, "unrest"),
                "dominant_hearing_preview": hearing["dominant_mcm_preview_symbol"],
                "reading_label": _reading_label(ranks.get("hoeren_hin", 99), gap_to_second, strain_delta_vs_field),
            }
        )
    return output


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "world",
        "hearing_rank",
        "hearing_count",
        "hearing_ratio",
        "hearing_balance",
        "gap_to_next_axis",
        "balance_delta_vs_visual_focus",
        "strain_delta_vs_fieldinput_axis",
        "fieldinput_delta_vs_fieldinput_axis",
        "hearing_rekopplung",
        "hearing_strain",
        "hearing_field_input",
        "hearing_stable_ratio",
        "hearing_unrest_ratio",
        "dominant_hearing_preview",
        "reading_label",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    avg_rank = sum(float(row["hearing_rank"]) for row in rows) / len(rows) if rows else 0.0
    avg_balance = sum(float(row["hearing_balance"]) for row in rows) / len(rows) if rows else 0.0
    avg_gap = sum(float(row["gap_to_next_axis"]) for row in rows) / len(rows) if rows else 0.0
    avg_stable = sum(float(row["hearing_stable_ratio"]) for row in rows) / len(rows) if rows else 0.0
    lines = [
        "# 406 - Hoeren-Hin Rekopplungsfaehigkeit",
        "",
        "## Fragestellung",
        "",
        "Die Befunde 404/405 zeigen `hoeren_hin` als ruhige lokale Rekopplungsachse. Diese Auswertung fragt deshalb nicht, ob daraus gehandelt werden soll, sondern ob `hoeren_hin` als rezeptorische Faehigkeit gelesen werden kann.",
        "",
        "Wichtig: Das bleibt passive Diagnose. Es ist keine Handlung, kein Gate und keine Regel.",
        "",
        "## Kurzbefund",
        "",
        f"- Mittlerer Rang von `hoeren_hin`: {avg_rank:.2f}.",
        f"- Mittlere Rekopplungsbalance: {avg_balance:.4f}.",
        f"- Mittlerer Abstand zur naechsten Achse: {avg_gap:.4f}.",
        f"- Mittlerer stabiler Innenfeldanteil innerhalb `hoeren_hin`: {avg_stable:.4f}.",
        "",
        "## Weltvergleich",
        "",
        "| Welt | Rang | Lesart | Balance | Gap | vs Sehen | Strain vs Feldinput | Feldinput vs Feldinput | Stable | Unrest | Preview |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['world']} | {int(row['hearing_rank'])} | {row['reading_label']} | "
            f"{float(row['hearing_balance']):.4f} | {float(row['gap_to_next_axis']):.4f} | "
            f"{float(row['balance_delta_vs_visual_focus']):.4f} | "
            f"{float(row['strain_delta_vs_fieldinput_axis']):.4f} | "
            f"{float(row['fieldinput_delta_vs_fieldinput_axis']):.4f} | "
            f"{float(row['hearing_stable_ratio']):.4f} | {float(row['hearing_unrest_ratio']):.4f} | "
            f"{row['dominant_hearing_preview']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "`hoeren_hin` wirkt in der Gegenprobe nicht wie ein zufaelliger Nebenwert. Es steht in allen geprueften Welten weit oben in der Rekopplungsbalance, traegt weniger Strain als lokaler `feldinput` und bleibt deutlich mit stabiler Innenfeldlage gekoppelt.",
            "",
            "Fachlich heisst das: Hinhoren kann als moegliche Aufnahmefaehigkeit des Organismus gelesen werden. MINI_DIO muss dadurch nicht automatisch handeln und auch nicht das Feld daempfen. Sichtbar wird nur, dass die Welt in bestimmten Lagen ueber Hoeren ruhiger aufgenommen werden kann als ueber direkten Feldinput.",
            "",
            "## Mechanische Grenze",
            "",
            "Diese Faehigkeit darf nicht als harte Steuerung umgesetzt werden. Sie gehoert vor das MCM-Feld als rezeptorisch-regulatorische Wahrnehmungsschicht:",
            "",
            "```text",
            "Weltlage -> Hoeren/Hinhoren -> Rezeptoraufnahme -> MCM-Feldwirkung",
            "```",
            "",
            "Das Feld bleibt einfach. Gelernt wird, welche Aufnahmeart welche Feldwirkung erzeugt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieselbe Faehigkeitslesung fuer `sehen_fokus` und `feldinput` gebaut werden. Danach kann MINI_DIO vergleichen: Wann hilft Hinhoren, wann hilft Sehen, und wann ist Feldkontakt zu belastend?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=INPUT_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()
    rows = build_rows(args.input)
    write_csv(args.csv_out, rows)
    write_markdown(args.md_out, rows)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
