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


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _visual_form(row: dict[str, str]) -> tuple[str, str]:
    reading = row.get("reading", "")
    chart_zone = row.get("chart_zone", "")
    movement = row.get("dominant_movement", "")
    ret = _float(row, "return_pct")
    rng = _float(row, "range_pct")
    before = _float(row, "before_return_pct")
    after = _float(row, "after_return_pct")

    if reading == "bull_expansion":
        return (
            "weite_aufwaerts_expansion",
            "Sichtbar als groesseres Aufwaertsfeld mit tragender Fortsetzung; die Achse liegt in einer expansiven Weltform.",
        )
    if reading == "last_rebound_rekopplung":
        return (
            "erholung_nach_vorlast",
            "Sichtbar als grosser Ruecklauf nach vorheriger negativer Last; die Achse wirkt als Rekopplung nach Belastung.",
        )
    if reading == "falling_rekopplung":
        return (
            "fallende_rueckbindung",
            "Sichtbar als fallende Bewegung, die nicht nur bricht, sondern rekoppelnd im Feld gehalten wird.",
        )
    if reading == "falling_bruch":
        return (
            "fallender_strukturbruch",
            "Sichtbar als negative Bewegung mit Bruchzone; die Achse wird als Umordnung unter Last gelesen.",
        )
    if reading == "quiet_rekopplung":
        return (
            "ruhige_gerichtete_rekopplung",
            "Sichtbar als gerichteter Verlauf mit Rueckbindung, weniger als expansive Breite.",
        )
    if reading == "bull_open_bruch_risk":
        return (
            "offenes_bullfenster_mit_bruch",
            "Sichtbar als offenes Richtungsfenster, das in der Ruecklesung nicht getragen bleibt.",
        )
    if reading == "open_transition":
        return (
            "schmale_offene_transition",
            "Sichtbar als schmales offenes Fenster; die Achse zeigt Anwesenheit, aber geringe Verlaufstiefe.",
        )
    if reading == "mixed_axis_state":
        return (
            "gemischte_achsenbewegung",
            "Sichtbar als positive Bewegung mit Bruchlesung; die Achse ist nicht eindeutig einseitig.",
        )

    if "rekopplung" in movement:
        return ("rekopplungsfenster", "Sichtbar als Rueckbindungsfenster.")
    if ret > 0 and rng > 30:
        return ("weite_positive_bewegung", "Sichtbar als weite positive Bewegung.")
    if ret < 0 and rng > 20:
        return ("weite_negative_bewegung", "Sichtbar als weite negative Bewegung.")
    if "offen" in chart_zone or before * after < 0:
        return ("offene_transition", "Sichtbar als Uebergangsfenster.")
    return ("nicht_eindeutig", "Keine eindeutige visuelle Kurzlesung.")


def _field_quality(row: dict[str, str]) -> str:
    pressure = _float(row, "pressure_abs")
    rekopplung = _float(row, "rekopplung_abs")
    rng = _float(row, "range_pct")

    if pressure >= 0.09 and rng >= 80:
        return "hochlastige_weite_rekopplung"
    if pressure >= 0.07 and rng >= 35:
        return "druckgetragene_weite"
    if rekopplung >= 0.023:
        return "starke_rekopplungsbindung"
    if pressure <= 0.055 and "rekopplung" in row.get("dominant_movement", ""):
        return "ruhige_rekopplung"
    if rng <= 8:
        return "schmale_offene_lage"
    return "mittlere_feldspannung"


def _build(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row in rows:
        form, note = _visual_form(row)
        result.append(
            {
                "reading": row.get("reading", "-"),
                "visual_form": form,
                "field_quality": _field_quality(row),
                "world": row.get("world", "-"),
                "pair": row.get("pair", "-"),
                "mode": row.get("mode", "-"),
                "phase_hint": row.get("phase_hint", "-"),
                "chart_zone": row.get("chart_zone", "-"),
                "dominant_movement": row.get("dominant_movement", "-"),
                "return_pct": _float(row, "return_pct"),
                "range_pct": _float(row, "range_pct"),
                "before_return_pct": _float(row, "before_return_pct"),
                "after_return_pct": _float(row, "after_return_pct"),
                "pressure_abs": _float(row, "pressure_abs"),
                "rekopplung_abs": _float(row, "rekopplung_abs"),
                "image_path": row.get("image_path", "-"),
                "visual_note": note,
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )
    return result


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1024 - Visuelle Typologie der Achse 183drjy<->1t5bcxp",
        "",
        "Passive Ableitung aus den Chartbildern von 1023.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive visuelle Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine Richtungsvorgabe",
        "",
        "## Typologie",
        "",
        "| Lesart | Sichtbare Weltform | Feldqualitaet | Welt | Bewegung | Return % | Range % | Druck | Rekopplung |",
        "|---|---|---|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['reading']}` | `{row['visual_form']}` | `{row['field_quality']}` | "
            f"`{row['world']}` | `{row['dominant_movement']}` | {row['return_pct']} | "
            f"{row['range_pct']} | {row['pressure_abs']} | {row['rekopplung_abs']} |"
        )

    lines.extend(["", "## Einzelbilder", ""])
    for row in rows:
        lines.extend(
            [
                f"### `{row['reading']}` -> `{row['visual_form']}`",
                "",
                f"- Feldqualitaet: `{row['field_quality']}`",
                f"- Kurzlesung: {row['visual_note']}",
                f"- Welt: `{row['world']}`",
                f"- Paar: `{row['pair']}`",
                f"- Modus: `{row['mode']}`",
                f"- Phase: `{row['phase_hint']}`",
                "",
                f"![{row['reading']} {row['world']}]({Path(str(row['image_path'])).as_posix()})",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Die sichtbaren Weltformen sind nicht austauschbar, obwohl dieselbe Achse beteiligt ist.",
            "Die Achse `183drjy<->1t5bcxp` traegt mindestens vier robuste Bild-/Feldtypen:",
            "",
            "- weite Aufwaerts-Expansion",
            "- fallende Rueckbindung",
            "- fallender Strukturbruch",
            "- Erholung nach vorheriger Last",
            "",
            "Dazu kommen schmalere oder gemischte Uebergangsformen.",
            "",
            "## Schluss",
            "",
            "Die MCM-Achse wirkt wie ein visueller und feldbezogener Kanal.",
            "Ihre Bedeutung entsteht nicht aus einer einzelnen Richtung, sondern aus der Kopplung von sichtbarer Weltform, Druck, Rekopplung und Vorlast.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese visuellen Typen in spaeteren Welten wiederkehren oder ob sie nur aus dieser isolierten Achsenfamilie stammen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chart-windows", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    rows = _build(_read_rows(args.chart_windows))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"typology_rows={len(rows)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
