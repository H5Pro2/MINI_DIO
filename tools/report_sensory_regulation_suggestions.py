from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.sensory_regulation_suggestion import (  # noqa: E402
    build_suggestions,
    read_intake_memory,
    suggestion_counts,
    write_csv,
)


INPUT_DEFAULT = ROOT / "docs" / "befunde" / "409_PASSIVE_SINNESAUFNAHME_MEMORY.csv"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "459_PASSIVE_REGULATIONSVORSCHLAG_BASIS.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "459_PASSIVE_REGULATIONSVORSCHLAG_BASIS.md"


DISPLAY_NAMES = {
    "focus_pull": "Fokus halten / vertiefen",
    "distance_pull": "Abstand bilden",
    "softening_pull": "leiser / weicher aufnehmen",
    "sharpening_pull": "Sehen schaerfen",
    "contact_relief_pull": "Druck / Feldkontakt entlasten",
    "stable_listening_pull": "ruhig hinhoeren",
}


def _title(path: Path) -> str:
    stem = path.stem
    if "_" in stem:
        number, rest = stem.split("_", 1)
        if number.isdigit():
            return f"# {number} - {rest.replace('_', ' ').title()}"
    return f"# {stem.replace('_', ' ').title()}"


def _fmt(value: object) -> str:
    try:
        return f"{float(value):.4f}"
    except Exception:
        return "0.0000"


def _write_markdown(path: Path, rows: list[dict[str, object]], input_path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    suggestion_counter, family_counter = suggestion_counts(rows)
    top_rows = sorted(
        rows,
        key=lambda row: (
            -int(row.get("total_events") or 0),
            str(row.get("dominant_suggestion") or "-"),
            str(row.get("intake_key") or "-"),
        ),
    )[:24]
    lines = [
        _title(path),
        "",
        "## Fragestellung",
        "",
        "Welche Wahrnehmungsfaehigkeit liegt aus der passiven Sinnesaufnahme-Memory nahe, ohne daraus Handlung, Gate oder Strategie zu machen?",
        "",
        "Gelesen wird:",
        "",
        f"- Input: `{input_path.name}`",
        "",
        "Wichtig: Diese Schicht ist kein aktiver Regler. Sie ist eine passive Regulationsvorschlagsschicht vor dem MCM-Feld.",
        "",
        "## Kurzbefund",
        "",
        f"- Ausgewertete Intake-Spuren: {len(rows)}.",
        "",
        "## Vorschlagsfamilien",
        "",
        "| Familie | Count |",
        "|---|---:|",
    ]
    for family, count in family_counter.most_common():
        lines.append(f"| {family} | {count} |")
    lines.extend(
        [
            "",
            "## Dominante Vorschlaege",
            "",
            "| Vorschlag | Count |",
            "|---|---:|",
        ]
    )
    for suggestion, count in suggestion_counter.most_common():
        lines.append(f"| {DISPLAY_NAMES.get(suggestion, suggestion)} | {count} |")
    lines.extend(
        [
            "",
            "## Staerkste Spuren",
            "",
            "| Achse | Innenfeld | Qualitaet | Ereignisse | Dominanter Vorschlag | Fokus | Abstand | Weicher | Schaerfer | Kontaktentlastung | Hinhoeren |",
            "|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in top_rows:
        suggestion = str(row.get("dominant_suggestion") or "-")
        lines.append(
            f"| {row.get('axis')} | {row.get('inner_effect_state')} | {row.get('intake_memory_quality')} | "
            f"{int(row.get('total_events') or 0)} | {DISPLAY_NAMES.get(suggestion, suggestion)} | "
            f"{_fmt(row.get('focus_pull'))} | {_fmt(row.get('distance_pull'))} | "
            f"{_fmt(row.get('softening_pull'))} | {_fmt(row.get('sharpening_pull'))} | "
            f"{_fmt(row.get('contact_relief_pull'))} | {_fmt(row.get('stable_listening_pull'))} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Schicht beschreibt keine Entscheidung. Sie liest nur, welche Wahrnehmungsfaehigkeit aus der bisherigen Aufnahmequalitaet naheliegt.",
            "",
            "Damit bleibt die Trennung erhalten:",
            "",
            "```text",
            "Sinneskontakt -> passive Aufnahmequalitaet -> Regulationsvorschlag -> noch keine Handlung",
            "```",
            "",
            "Die Vorschlaege sind kontinuierliche Zugrichtungen. Sie sind keine Schwellen, keine Sperren und keine Anweisungen.",
            "",
            "## Mechanische Grenze",
            "",
            "- keine Handlung",
            "- kein Entry",
            "- kein Gate",
            "- keine Strategie",
            "- keine direkte Veraenderung des MCM-Feldes",
            "",
            "Die Schicht bereitet nur vor, wie MINI_DIO spaeter lernen koennte, seine Wahrnehmung zu dosieren: Fokus oder Abstand, lauter oder leiser, schaerfer oder unschaerfer, mehr Kontakt oder Entlastung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese passive Vorschlagsschicht ueber mehrere Welten verglichen werden. Stabil wiederkehrende Vorschlaege koennen spaeter als lernbare Wahrnehmungsfaehigkeiten betrachtet werden, ohne das MCM-Feld direkt zu regeln.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=INPUT_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    rows = build_suggestions(read_intake_memory(args.input))
    write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows, args.input)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    print(f"records={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
