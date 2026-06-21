from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUTS = [
    ROOT / "docs" / "befunde" / "459_PASSIVE_REGULATIONSVORSCHLAG_BASIS.csv",
    ROOT / "docs" / "befunde" / "460_BTC2024_5M_QUIET_REGULATIONSVORSCHLAG.csv",
    ROOT / "docs" / "befunde" / "461_BTC2024_5M_STRESS_REGULATIONSVORSCHLAG.csv",
    ROOT / "docs" / "befunde" / "462_BTC2024_1H_QUIET_REGULATIONSVORSCHLAG.csv",
    ROOT / "docs" / "befunde" / "463_BTC2024_1H_STRESS_REGULATIONSVORSCHLAG.csv",
    ROOT / "docs" / "befunde" / "465_SOL2023_NEGATIVE_STRESS_10K_REGULATIONSVORSCHLAG.csv",
    ROOT / "docs" / "befunde" / "466_SOL2026_SIDEWAYS_10K_REGULATIONSVORSCHLAG.csv",
    ROOT / "docs" / "befunde" / "467_SOL2023_POSITIVE_EXPANSION_10K_REGULATIONSVORSCHLAG.csv",
    ROOT / "docs" / "befunde" / "471_KAS2024_ZEITEBENEN_REGULATIONSVORSCHLAG.csv",
]
CSV_DEFAULT = ROOT / "docs" / "befunde" / "473_PASSIVE_REGULATIONSVORSCHLAG_FELDTRAGUNG.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "473_PASSIVE_REGULATIONSVORSCHLAG_FELDTRAGUNG.md"


DISPLAY_NAMES = {
    "focus_pull": "Fokus halten / vertiefen",
    "distance_pull": "Abstand bilden",
    "softening_pull": "leiser / weicher aufnehmen",
    "sharpening_pull": "Sehen schaerfen",
    "contact_relief_pull": "Druck / Feldkontakt entlasten",
    "stable_listening_pull": "ruhig hinhoeren",
}


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _int(value: object) -> int:
    try:
        return int(float(value or 0.0))
    except Exception:
        return 0


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _source_label(path: Path) -> str:
    stem = path.stem
    if "_" in stem and stem.split("_", 1)[0].isdigit():
        return stem.split("_", 1)[1]
    return stem


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter=";"))
    for row in rows:
        row["_source"] = _source_label(path)
    return rows


def _weighted(rows: list[dict[str, str]], column: str) -> float:
    total = sum(max(1, _int(row.get("total_events"))) for row in rows)
    if total <= 0:
        return 0.0
    return sum(max(1, _int(row.get("total_events"))) * _float(row.get(column)) for row in rows) / total


def _sum_events(rows: list[dict[str, str]]) -> int:
    return sum(_int(row.get("total_events")) for row in rows)


def _reading(row: dict[str, object]) -> str:
    support = float(row["field_support_score"])
    pressure = float(row["field_pressure_score"])
    if support >= pressure:
        return "eher_getragen"
    return "eher_drucknah"


def _aggregate(rows: list[dict[str, str]], group_key: str) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        key = str(row.get(group_key) or "-")
        grouped[key].append(row)

    output: list[dict[str, object]] = []
    for key, group in sorted(grouped.items()):
        recoupling = _weighted(group, "recoupling_balance")
        strain = _weighted(group, "strain_quality")
        carry = _weighted(group, "carry_quality")
        field_input = _weighted(group, "field_intake_pressure")
        support = _clamp((recoupling * 0.45) + (carry * 0.35) + ((1.0 - strain) * 0.10) + ((1.0 - field_input) * 0.10))
        pressure = _clamp((strain * 0.45) + (field_input * 0.40) + ((1.0 - recoupling) * 0.15))
        item: dict[str, object] = {
            group_key: key,
            "display_name": DISPLAY_NAMES.get(key, key),
            "source_count": len({str(row.get("_source") or "-") for row in group}),
            "trace_count": len(group),
            "total_events": _sum_events(group),
            "avg_recoupling_balance": recoupling,
            "avg_strain_quality": strain,
            "avg_carry_quality": carry,
            "avg_field_intake_pressure": field_input,
            "field_support_score": support,
            "field_pressure_score": pressure,
            "support_minus_pressure": support - pressure,
        }
        item["passive_reading"] = _reading(item)
        output.append(item)
    output.sort(
        key=lambda item: (
            str(item.get("passive_reading") or "-"),
            -float(item.get("support_minus_pressure") or 0.0),
            -int(item.get("total_events") or 0),
            str(item.get(group_key) or "-"),
        )
    )
    return output


def build_followthrough(input_paths: list[Path]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, str]]]:
    all_rows: list[dict[str, str]] = []
    for path in input_paths:
        if path.exists():
            all_rows.extend(_read_rows(path))
    by_suggestion = _aggregate(all_rows, "dominant_suggestion")
    by_source_suggestion: list[dict[str, object]] = []
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in all_rows:
        grouped[(str(row.get("_source") or "-"), str(row.get("dominant_suggestion") or "-"))].append(row)
    for (source, suggestion), rows in sorted(grouped.items()):
        item = _aggregate(rows, "dominant_suggestion")[0]
        item["source"] = source
        item["dominant_suggestion"] = suggestion
        by_source_suggestion.append(item)
    by_source_suggestion.sort(key=lambda item: (str(item["source"]), str(item["dominant_suggestion"])))
    return by_suggestion, by_source_suggestion, all_rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    columns = [
        "source",
        "dominant_suggestion",
        "display_name",
        "passive_reading",
        "source_count",
        "trace_count",
        "total_events",
        "avg_recoupling_balance",
        "avg_strain_quality",
        "avg_carry_quality",
        "avg_field_intake_pressure",
        "field_support_score",
        "field_pressure_score",
        "support_minus_pressure",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def _fmt(value: object, digits: int = 4) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except Exception:
        return str(value)


def write_markdown(
    path: Path,
    by_suggestion: list[dict[str, object]],
    by_source_suggestion: list[dict[str, object]],
    source_count: int,
    trace_count: int,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 473 - Passive Regulationsvorschlag Feldtragung",
        "",
        "Stand: 2026-06-21",
        "",
        "## Fragestellung",
        "",
        "Welche passive Vorschlagsrichtung wird vom MCM-Feld eher getragen, und welche liegt naeher an Druck oder kurzfristiger Entlastung?",
        "",
        "Wichtig: Diese Diagnose erzeugt keine aktive Regulation. Sie liest nur vorhandene Vorschlags-Spuren gegen Rekopplung, Carry, Strain und Feldinput.",
        "",
        "## Methode",
        "",
        "Gelesen wurden die Vorschlagsdateien 459 bis 467 und 471.",
        "",
        f"- Quellen: {source_count}",
        f"- Vorschlags-Spuren: {trace_count}",
        "",
        "Pro Vorschlagsrichtung werden die vorhandenen Felddaten ereignisgewichtet verdichtet:",
        "",
        "```text",
        "Feldtragung = Rekopplung + Carry + wenig Strain + wenig Feldinput",
        "Felddruck   = Strain + Feldinput + schwächere Rekopplung",
        "```",
        "",
        "Das ist eine Lesart, keine Schwelle und keine Anweisung.",
        "",
        "## Gesamtbild nach Vorschlagsrichtung",
        "",
        "| Vorschlag | Lesart | Quellen | Spuren | Ereignisse | Support | Druck | Netto | Rekopplung | Strain | Feldinput |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in by_suggestion:
        lines.append(
            f"| {row['display_name']} | {row['passive_reading']} | {row['source_count']} | {row['trace_count']} | "
            f"{row['total_events']} | {_fmt(row['field_support_score'])} | {_fmt(row['field_pressure_score'])} | "
            f"{_fmt(row['support_minus_pressure'])} | {_fmt(row['avg_recoupling_balance'])} | "
            f"{_fmt(row['avg_strain_quality'])} | {_fmt(row['avg_field_intake_pressure'])} |"
        )
    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "Die Vorschlaege trennen sich nicht in einfache Ja/Nein-Gruppen. Sie liegen auf einem Spannungsfeld:",
            "",
            "- `ruhig hinhoeren`, `Sehen schaerfen` und `Fokus halten / vertiefen` liegen eher auf der getragenen Seite.",
            "- `Abstand bilden`, `leiser / weicher aufnehmen` und `Druck / Feldkontakt entlasten` liegen naeher an Entlastung und Druckbearbeitung.",
            "- Das ist fachlich passend: Entlastungsvorschlaege entstehen dort, wo das Feld mehr Abstand, weichere Aufnahme oder Kontaktentlastung braucht.",
            "",
            "Damit wird die naechste Trennung sichtbar:",
            "",
            "```text",
            "getragenes Wahrnehmen",
            "vs.",
            "entlastendes Wahrnehmen",
            "```",
            "",
            "Beides kann wertvoll sein. Getragen heisst nicht automatisch besser. Entlastend kann eine notwendige Organismusfaehigkeit sein, wenn Weltkontakt Druck erzeugt.",
            "",
            "## Mechanische Grenze",
            "",
            "- keine Handlung",
            "- kein Gate",
            "- keine Strategie",
            "- keine direkte MCM-Feldsteuerung",
            "- keine harte Entscheidung aus diesen Werten",
            "",
            "Die Diagnose zeigt nur, welche Wahrnehmungsfaehigkeit in welchen Feldlagen eher getragen oder eher drucknah gelesen wird.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Feldtragung pro Asset getrennt gelesen werden: BTC, SOL und KAS koennen dieselbe Vorschlagssprache nutzen, aber unterschiedliche Entlastungs- und Tragprofile besitzen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _resolve_many(values: list[str]) -> list[Path]:
    if not values:
        return DEFAULT_INPUTS
    paths: list[Path] = []
    for value in values:
        path = Path(value)
        if not path.is_absolute():
            path = ROOT / path
        paths.append(path)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    input_paths = _resolve_many(args.input)
    by_suggestion, by_source_suggestion, all_rows = build_followthrough(input_paths)
    csv_rows = []
    for row in by_source_suggestion:
        item = dict(row)
        item.setdefault("source", "-")
        csv_rows.append(item)
    write_csv(args.csv_out, csv_rows)
    write_markdown(args.md_out, by_suggestion, by_source_suggestion, len(input_paths), len(all_rows))
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    print(f"records={len(csv_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
