from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.sensory_intake_memory import SensoryIntakeMemory


INPUT_DEFAULT = ROOT / "docs" / "befunde" / "408_SINNESAUFNAHME_WIEDERERKENNUNG.csv"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "409_PASSIVE_SINNESAUFNAHME_MEMORY.csv"
JSON_DEFAULT = ROOT / "docs" / "befunde" / "409_PASSIVE_SINNESAUFNAHME_MEMORY.json"
MD_DEFAULT = ROOT / "docs" / "befunde" / "409_PASSIVE_SINNESAUFNAHME_MEMORY.md"


def _quality_counts(rows: list[dict[str, object]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        counter[str(row.get("intake_memory_quality") or "-")] += 1
    return counter


def _write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    title_number = path.name.split("_", 1)[0] if "_" in path.name and path.name[:3].isdigit() else "409"
    quality_counter = _quality_counts(rows)
    top_rows = rows[:18]
    quiet_rows = [row for row in rows if row["intake_memory_quality"] == "reproduced_quiet_intake"]
    contact_rows = [row for row in rows if row["intake_memory_quality"] == "contact_loaded_intake"]
    lines = [
        f"# {title_number} - Passive Sinnesaufnahme Memory",
        "",
        "## Fragestellung",
        "",
        "Kann MINI_DIO wiederkehrende Aufnahmequalitaet als passive Memory-Spur speichern, ohne daraus Handlung, Gate oder Strategie zu machen?",
        "",
        "Die Memory speichert nur diese passive Kopplung:",
        "",
        "```text",
        "Aufnahmeachse + Innenfeldzustand + MCM-Preview",
        "  -> Wiederkehr",
        "  -> Tragart der Aufnahme",
        "  -> Kontaktlast / Strain / Rekopplung",
        "```",
        "",
        "## Kurzbefund",
        "",
        f"- Memory-Eintraege: {len(rows)}.",
        f"- Reproduzierte ruhige Aufnahmen: {len(quiet_rows)}.",
        f"- Kontaktlastige Aufnahmen: {len(contact_rows)}.",
        "",
        "## Qualitaetsprofil",
        "",
        "| Qualitaet | Count |",
        "|---|---:|",
    ]
    for quality, count in quality_counter.most_common():
        lines.append(f"| {quality} | {count} |")
    lines.extend(
        [
            "",
            "## Staerkste Memory-Spuren",
            "",
            "| Achse | Innenfeld | Preview | Memory-Qualitaet | Welten | Count | Balance | Strain | Feldinput |",
            "|---|---|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in top_rows:
        lines.append(
            f"| {row['axis']} | {row['inner_effect_state']} | {row['mcm_preview_symbol']} | "
            f"{row['intake_memory_quality']} | {int(row['max_world_count'])} | "
            f"{int(row['total_events'])} | {float(row['avg_recoupling_balance']):.4f} | "
            f"{float(row['avg_strain_quality']):.4f} | {float(row['avg_field_intake_pressure']):.4f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die passive Sinnesaufnahme-Memory verdichtet die vorherige Wiedererkennungsstufe: MINI_DIO speichert hier keine Rohdaten und keine Entscheidung, sondern wiederkehrende Aufnahmequalitaet.",
            "",
            "`hoeren_hin` und `sehen_fokus` bilden die staerksten ruhigen Spuren, wenn sie mit `inner_effect_stable` und einer wiederkehrenden MCM-Preview zusammenfallen. `feldinput` bleibt lesbar, traegt aber mehr Kontaktlast.",
            "",
            "Damit entsteht eine kleine passive Erfahrungsform:",
            "",
            "```text",
            "So wurde Welt aufgenommen.",
            "So lag das Innenfeld.",
            "Diese MCM-Feldfamilie trat dabei wieder auf.",
            "Diese Aufnahme war eher ruhig, tragend, offen, kontaktlastig oder belastet.",
            "```",
            "",
            "Wichtig: Diese Memory ist nicht die rezeptorisch-regulatorische Steuerung selbst. Sie speichert nur, welche Aufnahmequalitaeten sich wiederholt gezeigt haben. Wie MINI_DIO spaeter mit Fokus, Abstand, lauter/leiser, scharf/unscharf oder Druck/Entspannung umgeht, bleibt eine getrennte Faehigkeitsschicht.",
            "",
            "## Mechanische Grenze",
            "",
            "- keine Handlung",
            "- kein Entry",
            "- kein Gate",
            "- keine Strategie",
            "- keine globale Daempfung des MCM-Feldes",
            "",
            "Die Memory ist eine passive Landkarte der Sinnesaufnahme vor dem Feld.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese Intake-Memory bei einer neuen Welt dieselben ruhigen und kontaktlastigen Aufnahmefamilien wiedererkennt oder ob neue Aufnahmequalitaeten entstehen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=INPUT_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--json-out", type=Path, default=JSON_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    memory = SensoryIntakeMemory.from_csv_paths([args.input])
    rows = memory.to_rows()
    memory.write_csv(args.csv_out)
    memory.write_json(args.json_out)
    _write_markdown(args.md_out, rows)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.json_out}")
    print(f"wrote {args.md_out}")
    print(f"records={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
