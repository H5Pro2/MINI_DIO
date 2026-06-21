from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path


INPUT_DEFAULT = Path("docs/befunde/404_SINNESACHSEN_EPISODENKARTE_GEGENPROBE.csv")
CSV_DEFAULT = Path("docs/befunde/408_SINNESAUFNAHME_WIEDERERKENNUNG.csv")
MD_DEFAULT = Path("docs/befunde/408_SINNESAUFNAHME_WIEDERERKENNUNG.md")

SUMMARY_COLUMNS = [
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
        result = float(value or default)
    except (TypeError, ValueError):
        return default
    if result != result:
        return default
    return result


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def _report_title(path: Path) -> str:
    stem = path.stem
    if "_" in stem:
        number, rest = stem.split("_", 1)
        if number.isdigit():
            return f"# {number} - {rest.replace('_', ' ').title()}"
    return f"# {stem.replace('_', ' ').title()}"


def _weighted_average(rows: list[dict[str, str]], column: str) -> float:
    total = sum(_float(row.get("count")) for row in rows)
    if total <= 0.0:
        return 0.0
    return sum(_float(row.get("count")) * _float(row.get(column)) for row in rows) / total


def _weighted_stdev(rows: list[dict[str, str]], column: str, mean: float) -> float:
    total = sum(_float(row.get("count")) for row in rows)
    if total <= 0.0:
        return 0.0
    variance = sum(_float(row.get("count")) * ((_float(row.get(column)) - mean) ** 2) for row in rows) / total
    return math.sqrt(max(0.0, variance))


def _recoupling_balance(item: dict[str, object]) -> float:
    return (
        float(item["avg_mcm_rekopplung_quality"])
        - float(item["avg_mcm_strain_quality"])
        - (float(item["avg_rezeptor_field_intake_pressure"]) * 0.25)
    )


def _signature_label(item: dict[str, object]) -> str:
    world_count = int(item["world_count"])
    balance = float(item["recoupling_balance"])
    strain = float(item["avg_mcm_strain_quality"])
    field_input = float(item["avg_rezeptor_field_intake_pressure"])
    balance_stdev = float(item["stdev_recoupling_balance"])
    if world_count >= 4 and balance >= 0.52 and strain <= 0.16 and balance_stdev <= 0.025:
        return "reproduzierte_ruhige_aufnahme"
    if world_count >= 3 and balance >= 0.48 and strain <= 0.18:
        return "wiederkehrend_tragend"
    if world_count >= 3 and (strain >= 0.20 or field_input >= 0.20):
        return "wiederkehrend_kontaktlastig"
    if world_count >= 2:
        return "wiederkehrend_offen"
    return "einzelspur"


def build_rows(input_path: Path) -> list[dict[str, object]]:
    raw_rows = _read_rows(input_path)
    world_total: dict[str, float] = defaultdict(float)
    for row in raw_rows:
        world_total[str(row.get("world") or "-")] += _float(row.get("count"))

    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in raw_rows:
        inner_effect = row.get("inner_effect_state") or row.get("dominant_inner_effect_state") or "-"
        preview = row.get("mcm_preview_symbol") or row.get("dominant_mcm_preview_symbol") or "-"
        key = (
            str(row.get("axis") or "-"),
            str(inner_effect),
            str(preview),
        )
        grouped[key].append(row)

    output: list[dict[str, object]] = []
    for (axis, inner_effect, preview), rows in grouped.items():
        worlds = sorted({str(row.get("world") or "-") for row in rows})
        total_count = int(sum(_float(row.get("count")) for row in rows))
        total_ratio = sum(_float(row.get("count")) / max(1.0, world_total[str(row.get("world") or "-")]) for row in rows)
        item: dict[str, object] = {
            "axis": axis,
            "inner_effect_state": inner_effect,
            "mcm_preview_symbol": preview,
            "world_count": len(worlds),
            "worlds": ",".join(worlds),
            "total_count": total_count,
            "world_relative_ratio_sum": total_ratio,
        }
        for column in SUMMARY_COLUMNS:
            item[column] = _weighted_average(rows, column)
        balances = []
        for row in rows:
            balance = (
                _float(row.get("avg_mcm_rekopplung_quality"))
                - _float(row.get("avg_mcm_strain_quality"))
                - (_float(row.get("avg_rezeptor_field_intake_pressure")) * 0.25)
            )
            expanded = max(1, int(_float(row.get("count"))))
            balances.extend([balance] * expanded)
        item["recoupling_balance"] = _recoupling_balance(item)
        mean_balance = float(item["recoupling_balance"])
        item["stdev_recoupling_balance"] = math.sqrt(sum((value - mean_balance) ** 2 for value in balances) / len(balances)) if balances else 0.0
        item["signature_label"] = _signature_label(item)
        output.append(item)

    output.sort(
        key=lambda row: (
            -int(row["world_count"]),
            -float(row["total_count"]),
            str(row["axis"]),
            str(row["inner_effect_state"]),
            str(row["mcm_preview_symbol"]),
        )
    )
    return output


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "axis",
        "inner_effect_state",
        "mcm_preview_symbol",
        "signature_label",
        "world_count",
        "worlds",
        "total_count",
        "world_relative_ratio_sum",
        "recoupling_balance",
        "stdev_recoupling_balance",
        "avg_mcm_rekopplung_quality",
        "avg_mcm_strain_quality",
        "avg_mcm_carry_quality",
        "avg_rezeptor_field_intake_pressure",
        "avg_axis_z",
        "avg_perception_adaptation_potential",
        "avg_perception_visual_focus_tendency",
        "avg_perception_visual_distance_tendency",
        "avg_perception_auditory_listen_tendency",
        "avg_perception_auditory_softening_tendency",
        "avg_perception_felt_distance_tendency",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    stable_rows = [row for row in rows if row["signature_label"] == "reproduzierte_ruhige_aufnahme"]
    recurring_rows = [row for row in rows if int(row["world_count"]) >= 3]
    lines = [
        _report_title(path),
        "",
        "## Fragestellung",
        "",
        "Kann MINI_DIO Aufnahmequalitaeten wiedererkennen, ohne daraus Handlung oder Regel zu machen?",
        "",
        "Geprueft wird die kleinste passive Signatur:",
        "",
        "```text",
        "Aufnahmeachse + Innenfeldzustand + MCM-Preview",
        "```",
        "",
        "Wenn diese Signatur ueber mehrere Welten mit aehnlicher Feldwirkung wiederkehrt, ist sie eine passive Lernspur.",
        "",
        "## Kurzbefund",
        "",
        f"- Wiederkehrende Signaturen mit mindestens drei Welten: {len(recurring_rows)}.",
        f"- Reproduzierte ruhige Aufnahmen: {len(stable_rows)}.",
        "",
        "## Staerkste Wiedererkennungen",
        "",
        "| Achse | Innenfeld | Preview | Label | Welten | Count | Balance | Streuung | Strain | Feldinput |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows[:18]:
        lines.append(
            f"| {row['axis']} | {row['inner_effect_state']} | {row['mcm_preview_symbol']} | "
            f"{row['signature_label']} | {int(row['world_count'])} | {int(row['total_count'])} | "
            f"{float(row['recoupling_balance']):.4f} | {float(row['stdev_recoupling_balance']):.4f} | "
            f"{float(row['avg_mcm_strain_quality']):.4f} | {float(row['avg_rezeptor_field_intake_pressure']):.4f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die staerksten Wiedererkennungen liegen nicht in beliebigen Rohwerten, sondern in wiederkehrenden Kombinationen aus Aufnahmeachse, Innenfeldzustand und MCM-Preview. Damit wird Aufnahmequalitaet als passive Spur lesbar.",
            "",
            "`hoeren_hin + inner_effect_stable` bildet die ruhigste wiederkehrende Spur. `sehen_fokus + inner_effect_stable` liegt nahe daran und traegt Form stabiler. `feldinput` erscheint ebenfalls wiederkehrend, aber mit mehr Strain und Kontaktlast.",
            "",
            "Das ist der wichtige Schnitt: MINI_DIO lernt hier nicht 'was zu tun ist'. MINI_DIO sammelt, welche Art von Weltaufnahme welche MCM-Feldwirkung wiederholt erzeugt.",
            "",
            "## Mechanische Bedeutung",
            "",
            "Diese Ebene ist der Uebergang von Diagnose zu passiver Lernspur:",
            "",
            "```text",
            "gleiche/aehnliche Weltlage",
            "  -> gleiche Aufnahmeart",
            "  -> aehnliche MCM-Feldwirkung",
            "  -> wiedererkennbare Innenfeldspur",
            "```",
            "",
            "Sie bleibt vor Handlung, vor Gate und vor Strategie.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Wiedererkennung in eine kleine passive Intake-Memory ueberfuehrt werden: nicht zur Steuerung, sondern um zu speichern, welche Aufnahmeart in welcher Innenfeldlage wiederholt getragen oder belastet war.",
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
