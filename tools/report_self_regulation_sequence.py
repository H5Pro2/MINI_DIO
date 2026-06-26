from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


INTAKE_DEFAULT = ROOT / "docs" / "befunde" / "409_PASSIVE_SINNESAUFNAHME_MEMORY.csv"
REGULATION_DEFAULT = ROOT / "docs" / "befunde" / "473_PASSIVE_REGULATIONSVORSCHLAG_FELDTRAGUNG.csv"
MOVEMENT_DEFAULT = ROOT / "docs" / "befunde" / "394_MCM_FELDBEWEGUNGS_MEMORY_SUMMARY.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "799_BLOCK_K_SELBSTREGULATION_KETTE.md"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "799_BLOCK_K_SELBSTREGULATION_KETTE.csv"


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(str(value).replace(",", "."))
    except Exception:
        return default
    if result != result:
        return default
    return result


def _safe_int(value: object, default: int = 0) -> int:
    try:
        return int(float(str(value).replace(",", ".")))
    except Exception:
        return default


def _read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8-sig")
    first = text.splitlines()[0] if text.splitlines() else ""
    delimiter = ";" if first.count(";") >= first.count(",") else ","
    reader = csv.DictReader(text.splitlines(), delimiter=delimiter)
    return [dict(row) for row in reader]


def _top_counter(rows: list[dict[str, str]], key: str, limit: int = 6) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for row in rows:
        value = str(row.get(key, "") or "-")
        counter[value] += 1
    return counter.most_common(limit)


def _sum_int(rows: list[dict[str, str]], key: str) -> int:
    return sum(_safe_int(row.get(key)) for row in rows)


def _avg(rows: list[dict[str, str]], key: str) -> float:
    values = [_safe_float(row.get(key)) for row in rows if str(row.get(key, "") or "") != ""]
    if not values:
        return 0.0
    return sum(values) / len(values)


def _stage_rows(intake_rows: list[dict[str, str]], regulation_rows: list[dict[str, str]], movement_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    recurrent_intake = [
        row
        for row in intake_rows
        if str(row.get("maturity_note", "") or "") == "multi_world_recurrent"
        or "recurrent" in str(row.get("intake_memory_quality", "") or "")
        or "reproduced" in str(row.get("intake_memory_quality", "") or "")
    ]
    named_symbols = set()
    for row in intake_rows:
        symbol = str(row.get("mcm_preview_symbol", "") or "")
        if symbol:
            named_symbols.add(symbol)
    for row in movement_rows:
        movement = str(row.get("movement_key", "") or "")
        for part in movement.split("->"):
            part = part.strip()
            if part:
                named_symbols.add(part)
    carried_regulation = [
        row
        for row in regulation_rows
        if str(row.get("passive_reading", "") or "") == "eher_getragen"
        and _safe_float(row.get("support_minus_pressure")) > 0.0
    ]
    integrated_movements = [
        row
        for row in movement_rows
        if str(row.get("field_memory_quality", "") or "").startswith("recurrently_")
    ]
    stable_movements = [
        row
        for row in movement_rows
        if str(row.get("maturity_note", "") or "") == "consistent_top_quality"
        and str(row.get("field_memory_quality", "") or "").startswith("recurrently_")
    ]
    intake_events = _sum_int(intake_rows, "total_events")
    movement_events = _sum_int(movement_rows, "total_events")
    regulation_events = _sum_int(regulation_rows, "total_events")
    return [
        {
            "stage": "wahrnehmung",
            "evidence": "Sinnesaufnahme-Memory",
            "records": len(intake_rows),
            "events": intake_events,
            "quality": f"{len(recurrent_intake)} wiederkehrende Aufnahmequalitaeten",
            "support": _avg(intake_rows, "avg_recoupling_balance"),
            "pressure": _avg(intake_rows, "avg_strain_quality"),
            "reading": "Weltkontakt wird kanalgetrennt als Aufnahmequalitaet lesbar.",
        },
        {
            "stage": "benennung",
            "evidence": "dio_*-Syntax / MCM-Preview-Symbole",
            "records": len(named_symbols),
            "events": intake_events + movement_events,
            "quality": f"{len(named_symbols)} benannte Feld-/Preview-Anker",
            "support": 0.0,
            "pressure": 0.0,
            "reading": "Wiederkehrende Feldlagen werden nicht nur als Wert, sondern als eigene Syntax getragen.",
        },
        {
            "stage": "feldwirkung",
            "evidence": "Rekopplung, Carry, Strain, Feldinput",
            "records": len(intake_rows),
            "events": intake_events,
            "quality": "MCM-Feldwirkung aus Rezeptoraufnahme",
            "support": (_avg(intake_rows, "avg_recoupling_balance") + _avg(intake_rows, "avg_carry_quality")) / 2.0,
            "pressure": (_avg(intake_rows, "avg_strain_quality") + _avg(intake_rows, "avg_field_intake_pressure")) / 2.0,
            "reading": "Aufnahme erzeugt eine innere Feldlage mit Tragung, Druck, Rekopplung und Strain.",
        },
        {
            "stage": "passive_regulation",
            "evidence": "Regulationsvorschlag-Feldtragung",
            "records": len(regulation_rows),
            "events": regulation_events,
            "quality": f"{len(carried_regulation)} getragene Vorschlagsspuren",
            "support": _avg(regulation_rows, "field_support_score"),
            "pressure": _avg(regulation_rows, "field_pressure_score"),
            "reading": "Regulation erscheint als Wahrnehmungsfaehigkeit vor dem Feld, nicht als Gate.",
        },
        {
            "stage": "integration",
            "evidence": "MCM-Feldbewegungs-Memory",
            "records": len(movement_rows),
            "events": movement_events,
            "quality": f"{len(integrated_movements)} wiederkehrende Feldbewegungen",
            "support": _avg(movement_rows, "avg_top_share"),
            "pressure": 1.0 - _avg(movement_rows, "avg_top_signature_share"),
            "reading": "Gerichtete Feldbewegungen werden als Innenfeldspur integriert.",
        },
        {
            "stage": "stabilisierung",
            "evidence": "konsistente Top-Qualitaet / Wiederkehr",
            "records": len(stable_movements),
            "events": _sum_int(stable_movements, "total_events"),
            "quality": f"{len(stable_movements)} stabilisierte Bewegungsqualitaeten",
            "support": _avg(stable_movements, "avg_top_share"),
            "pressure": 1.0 - _avg(stable_movements, "avg_top_signature_share") if stable_movements else 0.0,
            "reading": "Stabilisierung zeigt sich als gereifte, wiederkehrende Bedeutungsspanne, nicht als starre Regel.",
        },
    ]


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["stage", "evidence", "records", "events", "quality", "support", "pressure", "reading"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_markdown(
    path: Path,
    rows: list[dict[str, object]],
    intake_rows: list[dict[str, str]],
    regulation_rows: list[dict[str, str]],
    movement_rows: list[dict[str, str]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 799 - Block-K-Selbstregulationskette in MINI_DIO",
        "",
        "## Fragestellung",
        "",
        "Ist die in Block K beschriebene MCM-Folge in MINI_DIO praktisch als passive Diagnosekette sichtbar?",
        "",
        "Gepruefte Folge:",
        "",
        "```text",
        "Wahrnehmung",
        "  -> Benennung",
        "  -> Feldwirkung",
        "  -> passive Regulation",
        "  -> Integration",
        "  -> Stabilisierung",
        "```",
        "",
        "## Methode",
        "",
        "Dieser Report fuehrt vorhandene Befunde zusammen. Er erzeugt keine Handlung, kein Gate, keine Strategie und keine neue MCM-Feldsteuerung.",
        "",
        "Eingaben:",
        "",
        "- `409_PASSIVE_SINNESAUFNAHME_MEMORY.csv`",
        "- `473_PASSIVE_REGULATIONSVORSCHLAG_FELDTRAGUNG.csv`",
        "- `394_MCM_FELDBEWEGUNGS_MEMORY_SUMMARY.csv`",
        "",
        "## Kettenbefund",
        "",
        "| Stufe | Evidenz | Records | Events | Support | Druck / Streuung | Lesart |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['stage']} | {row['evidence']} | {int(row['records'])} | {int(row['events'])} | "
            f"{float(row['support']):.4f} | {float(row['pressure']):.4f} | {row['reading']} |"
        )
    lines.extend(
        [
            "",
            "## Top-Aufnahmequalitaeten",
            "",
            "| Qualitaet | Count |",
            "|---|---:|",
        ]
    )
    for quality, count in _top_counter(intake_rows, "intake_memory_quality"):
        lines.append(f"| {quality} | {count} |")
    lines.extend(
        [
            "",
            "## Top-Regulationsvorschlaege",
            "",
            "| Vorschlag | Count |",
            "|---|---:|",
        ]
    )
    for suggestion, count in _top_counter(regulation_rows, "dominant_suggestion"):
        lines.append(f"| {suggestion} | {count} |")
    lines.extend(
        [
            "",
            "## Feldbewegungsqualitaeten",
            "",
            "| Qualitaet | Count |",
            "|---|---:|",
        ]
    )
    for quality, count in _top_counter(movement_rows, "field_memory_quality"):
        lines.append(f"| {quality} | {count} |")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Block-K-Folge ist in den vorhandenen MINI_DIO-Befunden als Diagnosekette sichtbar.",
            "",
            "Hinweis zur Spalte `Druck / Streuung`: In den Wahrnehmungs- und Feldwirkungsstufen beschreibt sie eher Strain/Feldinput. In den Integrations- und Stabilisierungsstufen beschreibt sie eher Reststreuung beziehungsweise Fragmentierung der Bewegungssignatur.",
            "",
            "Wichtig ist die fachliche Grenze:",
            "",
            "```text",
            "sichtbar als passive Struktur",
            "nicht bewiesen als universelles Gesetz",
            "nicht gekoppelt an Handlung",
            "nicht als harte Regel im Feld eingebaut",
            "```",
            "",
            "Die staerkste Aussage ist daher:",
            "",
            "```text",
            "MINI_DIO bildet aus Weltkontakt eine wiedererkennbare innere Kette:",
            "Aufnahmequalitaet -> eigene Benennung -> Feldwirkung -> passive Regulationslesung -> integrierte Feldbewegung -> stabilere Bedeutungsspanne.",
            "```",
            "",
            "Das stuetzt die bisherige MCM-Richtung: Regulation entsteht hier nicht als Befehl, sondern als Ordnungsfaehigkeit eines Feldes, das Wahrnehmung, Syntax, Wiederkehr und Rekopplung verbindet.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Kette nicht nur aus vorhandenen Summaries gelesen werden. Sinnvoll ist ein frischer Mehrweltlauf, der pro Welt dieselben sechs Stufen direkt nebeneinander ausgibt.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--intake", type=Path, default=INTAKE_DEFAULT)
    parser.add_argument("--regulation", type=Path, default=REGULATION_DEFAULT)
    parser.add_argument("--movement", type=Path, default=MOVEMENT_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    intake_rows = _read_rows(args.intake)
    regulation_rows = _read_rows(args.regulation)
    movement_rows = _read_rows(args.movement)
    rows = _stage_rows(intake_rows, regulation_rows, movement_rows)
    _write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows, intake_rows, regulation_rows, movement_rows)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in rows:
        print(f"{row['stage']}: records={row['records']} events={row['events']} quality={row['quality']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
