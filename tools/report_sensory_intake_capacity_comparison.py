from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


INPUT_DEFAULT = Path("docs/befunde/404_SINNESACHSEN_EPISODENKARTE_GEGENPROBE.csv")
CSV_DEFAULT = Path("docs/befunde/407_SINNESAUFNAHME_FAEHIGKEITSVERGLEICH.csv")
MD_DEFAULT = Path("docs/befunde/407_SINNESAUFNAHME_FAEHIGKEITSVERGLEICH.md")

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


AXIS_READING = {
    "hoeren_hin": "ruhige_akustische_rekopplung",
    "sehen_fokus": "visuelle_formtragfaehigkeit",
    "sehen_abstand": "visueller_abstand",
    "hoeren_leise": "akustische_daempfungsnaehe",
    "fuehlen_abstand": "kontaktabstand_unruhe",
    "feldinput": "direkter_feldkontakt_last",
    "ausgeglichen": "ausgeglichene_aufnahme",
}


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


def _inner_ratio(rows: list[dict[str, str]], marker: str) -> float:
    total = sum(_float(row.get("count")) for row in rows)
    if total <= 0.0:
        return 0.0
    count = sum(_float(row.get("count")) for row in rows if marker in str(row.get("inner_effect_state") or ""))
    return count / total


def _recoupling_balance(item: dict[str, object]) -> float:
    return (
        float(item["avg_mcm_rekopplung_quality"])
        - float(item["avg_mcm_strain_quality"])
        - (float(item["avg_rezeptor_field_intake_pressure"]) * 0.25)
    )


def _capacity_label(item: dict[str, object]) -> str:
    axis = str(item["axis"])
    balance = float(item["recoupling_balance"])
    strain = float(item["avg_mcm_strain_quality"])
    field_input = float(item["avg_rezeptor_field_intake_pressure"])
    stable = float(item["stable_ratio"])
    if axis == "feldinput" and (strain >= 0.20 or field_input >= 0.20):
        return "kontaktlastig"
    if stable >= 0.95 and balance >= 0.54 and strain <= 0.15:
        return "ruhig_tragend"
    if balance >= 0.48 and strain <= 0.18:
        return "tragend"
    if strain >= 0.20 or field_input >= 0.20:
        return "belastet"
    return "offen"


def _axis_aggregate(world: str, axis: str, rows: list[dict[str, str]]) -> dict[str, object]:
    item: dict[str, object] = {
        "world": world,
        "axis": axis,
        "count": int(sum(_float(row.get("count")) for row in rows)),
        "ratio": sum(_float(row.get("ratio")) for row in rows),
        "dominant_inner_effect_state": _dominant_value(rows, "inner_effect_state"),
        "dominant_mcm_preview_symbol": _dominant_value(rows, "mcm_preview_symbol"),
        "stable_ratio": _inner_ratio(rows, "stable"),
        "unrest_ratio": _inner_ratio(rows, "unrest"),
    }
    for column in NUMERIC_COLUMNS:
        if column in {"count", "ratio"}:
            continue
        item[column] = _weighted_average(rows, column)
    item["recoupling_balance"] = _recoupling_balance(item)
    item["axis_reading"] = AXIS_READING.get(axis, "offene_aufnahme")
    item["capacity_label"] = _capacity_label(item)
    return item


def build_rows(input_path: Path) -> list[dict[str, object]]:
    raw_rows = _read_rows(input_path)
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in raw_rows:
        grouped[(str(row.get("world") or "-"), str(row.get("axis") or "-"))].append(row)

    by_world: dict[str, list[dict[str, object]]] = defaultdict(list)
    for (world, axis), rows in grouped.items():
        by_world[world].append(_axis_aggregate(world, axis, rows))

    output: list[dict[str, object]] = []
    for world, rows in sorted(by_world.items()):
        ranked = sorted(rows, key=lambda row: float(row["recoupling_balance"]), reverse=True)
        for index, row in enumerate(ranked, start=1):
            row = dict(row)
            row["rank"] = index
            output.append(row)
    return output


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "world",
        "rank",
        "axis",
        "axis_reading",
        "capacity_label",
        "count",
        "ratio",
        "recoupling_balance",
        "avg_mcm_rekopplung_quality",
        "avg_mcm_strain_quality",
        "avg_mcm_carry_quality",
        "avg_rezeptor_field_intake_pressure",
        "stable_ratio",
        "unrest_ratio",
        "dominant_inner_effect_state",
        "dominant_mcm_preview_symbol",
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


def _axis_mean(rows: list[dict[str, object]], axis: str, column: str) -> float:
    axis_rows = [row for row in rows if row["axis"] == axis]
    total = sum(float(row["count"]) for row in axis_rows)
    if total <= 0.0:
        return 0.0
    return sum(float(row["count"]) * float(row[column]) for row in axis_rows) / total


def write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    worlds = sorted({str(row["world"]) for row in rows})
    top_rows = [row for row in rows if int(row["rank"]) <= 3]
    lines = [
        "# 407 - Sinnesaufnahme Faehigkeitsvergleich",
        "",
        "## Fragestellung",
        "",
        "Nach `hoeren_hin` wird dieselbe passive Lesart auf alle lokalen Aufnahmeachsen gelegt. Geprueft wird, welche Achse ruhig rekoppelt, welche visuell tragend wirkt und welche mehr Kontaktlast in das Feld bringt.",
        "",
        "Wichtig: Das ist Diagnose der Aufnahmequalitaet. Es ist keine Handlung, kein Gate und keine Steuerregel.",
        "",
        "## Achsenmittel",
        "",
        "| Achse | Balance | Rekopplung | Strain | Feldinput | Stable | Lesart |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for axis in ["hoeren_hin", "sehen_fokus", "sehen_abstand", "hoeren_leise", "ausgeglichen", "feldinput", "fuehlen_abstand"]:
        axis_rows = [row for row in rows if row["axis"] == axis]
        if not axis_rows:
            continue
        lines.append(
            f"| {axis} | {_axis_mean(rows, axis, 'recoupling_balance'):.4f} | "
            f"{_axis_mean(rows, axis, 'avg_mcm_rekopplung_quality'):.4f} | "
            f"{_axis_mean(rows, axis, 'avg_mcm_strain_quality'):.4f} | "
            f"{_axis_mean(rows, axis, 'avg_rezeptor_field_intake_pressure'):.4f} | "
            f"{_axis_mean(rows, axis, 'stable_ratio'):.4f} | {AXIS_READING.get(axis, '-')} |"
        )
    lines.extend(
        [
            "",
            "## Top-3 je Welt",
            "",
            "| Welt | Rang | Achse | Qualitaet | Balance | Strain | Feldinput | Stable |",
            "|---|---:|---|---|---:|---:|---:|---:|",
        ]
    )
    for world in worlds:
        for row in [item for item in top_rows if item["world"] == world]:
            lines.append(
                f"| {world} | {int(row['rank'])} | {row['axis']} | {row['capacity_label']} | "
                f"{float(row['recoupling_balance']):.4f} | "
                f"{float(row['avg_mcm_strain_quality']):.4f} | "
                f"{float(row['avg_rezeptor_field_intake_pressure']):.4f} | "
                f"{float(row['stable_ratio']):.4f} |"
            )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "`hoeren_hin` bleibt die klarste ruhige Rekopplungsfaehigkeit. `sehen_fokus` bleibt ebenfalls tragend, aber naeher an Formspannung. `feldinput` ist nicht falsch; er ist der direkte Kontaktlast-Traeger. Dadurch wird sichtbar: Aufnahmequalitaet ist nicht ein globaler Wert, sondern eine lokale Auswahl der Wahrnehmungsart.",
            "",
            "Fachlich bedeutet das: MINI_DIO braucht keine Regel wie 'immer hinhoren'. Der Organismus braucht die Faehigkeit, die Art der Aufnahme zu unterscheiden: akustisch ruhig rekoppeln, visuell Form halten oder Feldkontakt als Druck wahrnehmen.",
            "",
            "## Mechanische Grenze",
            "",
            "Diese Schicht bleibt vor dem MCM-Feld:",
            "",
            "```text",
            "Sehen / Hoeren / Feldkontakt",
            "  -> rezeptorische Aufnahmequalitaet",
            "  -> MCM-Feldwirkung",
            "```",
            "",
            "Das Feld wird nicht umgebaut. Es liest, was die Aufnahmeart mit ihm macht.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob MINI_DIO diese Aufnahmequalitaeten episodisch wiedererkennt: gleiche Weltlage, gleiche Aufnahmeart, aehnliche Feldwirkung. Das waere der Uebergang von Diagnose zu passiver Lernspur.",
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
