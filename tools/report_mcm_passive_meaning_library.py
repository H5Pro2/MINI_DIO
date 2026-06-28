from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if not text.strip():
        return []
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;")
    except csv.Error:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _meaning_name(visual_form: str) -> str:
    mapping = {
        "fallende_rueckbindung": "dio_meaning_fallende_rueckbindung",
        "ruhige_gerichtete_rekopplung": "dio_meaning_ruhige_rekopplung",
        "weite_aufwaerts_expansion": "dio_meaning_weite_expansion",
        "schmale_offene_transition": "dio_meaning_schmale_transition",
    }
    return mapping.get(visual_form, f"dio_meaning_{visual_form}")


def _core_description(visual_form: str) -> str:
    mapping = {
        "fallende_rueckbindung": "Fallende Weltform, die nicht nur als Bruch erscheint, sondern rekoppelnd im MCM-Feld gehalten wird.",
        "ruhige_gerichtete_rekopplung": "Gerichtete Bewegung mit Rueckbindung; weniger expansive Breite, staerker ruhige Kopplungsqualitaet.",
        "weite_aufwaerts_expansion": "Weite positive Weltform mit Fortsetzungscharakter und groesserer Range.",
        "schmale_offene_transition": "Schmales Uebergangsfenster mit geringer Verlaufstiefe und offener Kontaktlage.",
    }
    return mapping.get(visual_form, "Passive Bedeutungsform ohne feste Handlungsableitung.")


def _open_boundary(visual_form: str) -> str:
    mapping = {
        "fallende_rueckbindung": "Nicht jede negative Bewegung ist Rueckbindung; Bruch und reine Last muessen getrennt bleiben.",
        "ruhige_gerichtete_rekopplung": "Kann mit Volatilitaetszonen ueberlappen; Bedeutung bleibt Rueckbindung, nicht Richtungsvorgabe.",
        "weite_aufwaerts_expansion": "Nicht jede Expansion ist tragend; Feldqualitaet schwankt zwischen Druck, Rekopplung und mittlerer Spannung.",
        "schmale_offene_transition": "Schmale Offenheit ist Anwesenheit, aber keine tiefe Bestaetigung; kann lokal bleiben.",
    }
    return mapping.get(visual_form, "Bedeutung bleibt offen und muss ueber weitere Welten beobachtet werden.")


def _build(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    library: list[dict[str, object]] = []
    for row in rows:
        if row.get("stability_class") != "robuste_bedeutungsform":
            continue
        visual_form = row.get("visual_form", "-")
        library.append(
            {
                "meaning_name": _meaning_name(visual_form),
                "visual_form": visual_form,
                "stability_class": row.get("stability_class", "-"),
                "core_description": _core_description(visual_form),
                "typical_worlds": row.get("worlds", "-"),
                "typical_typologies": row.get("typologies", "-"),
                "typical_field_qualities": row.get("field_qualities", "-"),
                "recurrence_count": row.get("recurrence_count", "0"),
                "world_variety": row.get("world_variety", "0"),
                "typology_variety": row.get("typology_variety", "0"),
                "field_quality_variety": row.get("field_quality_variety", "0"),
                "avg_return_pct": row.get("avg_return_pct", "0"),
                "avg_range_pct": row.get("avg_range_pct", "0"),
                "avg_pressure_abs": row.get("avg_pressure_abs", "0"),
                "avg_rekopplung_abs": row.get("avg_rekopplung_abs", "0"),
                "open_boundary": _open_boundary(visual_form),
                "library_status": "passive_bedeutungsgrundlage",
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )
    return library


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1027 - Passive Bedeutungsbibliothek",
        "",
        "Aus den robusten visuellen Bedeutungsformen aus 1026 abgeleitete passive Bedeutungsbibliothek.",
        "",
        "Diese Bibliothek ist kein Strategiebaustein. Sie beschreibt wiederkehrende Bild-/Feldformen,",
        "die Mini-DIO als Bedeutungsgrundlage weiter untersuchen kann.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Bedeutungsbibliothek",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine Richtungsvorgabe",
        "- keine starre Bedeutungsfixierung",
        "",
        "## Bibliothek",
        "",
        "| Name | Weltform | Wiederkehr | Weltstreuung | Feldqualitaeten | Return % | Range % | Druck | Rekopplung |",
        "|---|---|---:|---:|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['meaning_name']}` | `{row['visual_form']}` | {row['recurrence_count']} | "
            f"{row['world_variety']} | `{row['typical_field_qualities']}` | {row['avg_return_pct']} | "
            f"{row['avg_range_pct']} | {row['avg_pressure_abs']} | {row['avg_rekopplung_abs']} |"
        )

    lines.extend(["", "## Bedeutungsprofile", ""])
    for row in rows:
        lines.extend(
            [
                f"### `{row['meaning_name']}`",
                "",
                f"- Weltform: `{row['visual_form']}`",
                f"- Status: `{row['library_status']}`",
                f"- Kernlesung: {row['core_description']}",
                f"- Typische Welten: `{row['typical_worlds']}`",
                f"- Typische Typologien: `{row['typical_typologies']}`",
                f"- Typische Feldqualitaeten: `{row['typical_field_qualities']}`",
                f"- Offene Grenze: {row['open_boundary']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Die Bibliothek enthaelt aktuell vier robuste passive Bedeutungsformen.",
            "Sie bildet keine Entscheidung, sondern eine geordnete Grundlage fuer spaetere Innenfeld-Lesung.",
            "",
            "## Schluss",
            "",
            "Mini-DIO kann aus wiederkehrenden Welt-/Feldformen eine kleine Bedeutungsbibliothek aufbauen.",
            "Das ist ein Schritt von reiner Beobachtung zu strukturierter Bedeutungsverdichtung, ohne Handlung zu erzwingen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob neue Welten diese Bibliothek erweitern, bestaetigen oder einzelne Bedeutungen wieder oeffnen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stability", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    rows = _build(_read_rows(args.stability))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"library_entries={len(rows)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
