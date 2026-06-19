from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from report_auditory_regulation import DEFAULT_SUMMARIES
from report_auditory_regulation import _fmt
from report_recoupling_quality import _resolve
from report_visual_regulation import _row as visual_row


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "230_VISUELLE_FELDKOPPLUNG_DIAGNOSE.md"


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _row(name: str, path_text: str, group: str) -> dict:
    row = visual_row(name, path_text, group)
    active_seeing = row["genauer_ratio"] + row["alarm_ratio"]
    visual_filter_release = row["rauschen_ratio"] + row["hintergrund_ratio"] + row["stabil_ratio"] + row["abklingen_ratio"]

    field_binding = _clamp(
        (row["field_strain"] * 0.42)
        + (row["memory_load"] * 0.34)
        + (max(0.0, 0.64 - row["rekopplung"]) * 0.24)
    )
    visual_load = _clamp(
        (row["avg_visual_focus"] * 0.28)
        + (row["avg_visual_alarm"] * 0.24)
        + (row["avg_visual_gap"] * 0.18)
        + (row["alarm_ratio"] * 0.16)
        + (row["genauer_ratio"] * 0.14)
    )
    visual_relief = _clamp(
        (row["rauschen_ratio"] * 0.28)
        + (row["hintergrund_ratio"] * 0.22)
        + (row["stabil_ratio"] * 0.20)
        + (row["abklingen_ratio"] * 0.16)
        + (max(0.0, row["rekopplung"] - 0.60) * 1.8 * 0.14)
    )
    coupling_gap = _clamp(field_binding - visual_relief)
    visual_field_fit = _clamp(1.0 - abs(visual_load - field_binding))

    if field_binding <= 0.12 and visual_relief >= 0.26:
        coupling_role = "visuell_entlastend"
    elif field_binding > 0.20 and visual_relief > 0.26:
        coupling_role = "filtert_aber_feld_bindet"
    elif field_binding > 0.20 and visual_load >= visual_relief:
        coupling_role = "sehlast_feldnah"
    elif active_seeing > 0.18 and row["rekopplung"] >= 0.61:
        coupling_role = "aktive_form_rekoppelnd"
    else:
        coupling_role = "offene_sehkopplung"

    return {
        **row,
        "active_seeing": active_seeing,
        "visual_filter_release": visual_filter_release,
        "field_binding": field_binding,
        "visual_load": visual_load,
        "visual_relief": visual_relief,
        "coupling_gap": coupling_gap,
        "visual_field_fit": visual_field_fit,
        "coupling_role": coupling_role,
    }


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"]))

    role_counts: dict[str, int] = {}
    for row in rows:
        role_counts[row["coupling_role"]] = role_counts.get(row["coupling_role"], 0) + 1

    lines = [
        "# Visuelle Feldkopplung - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt visuelle Sehzustande gegen MCM-Feldlast, Memorylast und Rekopplung.",
        "Sie prueft, ob Sehen nur Oberflaechenform bleibt oder messbar mit dem Innenfeld gekoppelt ist.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Koppeln visuelle Formzustaende messbar an MCM-Feldwirkung?",
        "2. Unterpruefung: aktive Sehanteile, visuelle Filter-/Hintergrundanteile, Feldbindung und Rekopplung vergleichen.",
        "3. Folgeschritt: Bestimmen, wann sichtbare Form entlastet, bindet oder als offene Sehkopplung stehen bleibt.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | Gruppe | Rolle | visuelle Kopplung | aktiv sehen | Filter/Hintergrund | Sehlast | Sehentlastung | Feldbindung | Kopplungsluecke | Fit | Rekopplung |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["group"],
                    row["role"],
                    row["coupling_role"],
                    _fmt(row["active_seeing"], 4),
                    _fmt(row["visual_filter_release"], 4),
                    _fmt(row["visual_load"], 4),
                    _fmt(row["visual_relief"], 4),
                    _fmt(row["field_binding"], 4),
                    _fmt(row["coupling_gap"], 4),
                    _fmt(row["visual_field_fit"], 4),
                    _fmt(row["rekopplung"], 6),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Rollenzaehlung", ""])
    for role, count in sorted(role_counts.items()):
        lines.append(f"- `{role}`: `{count}`")

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "- `visuell_entlastend`: Form bleibt sichtbar, aber Feldbindung bleibt niedrig.",
            "- `filtert_aber_feld_bindet`: visuelle Filterung ist vorhanden, Feld/Memory binden trotzdem.",
            "- `sehlast_feldnah`: visuelle Last und Feldbindung liegen nah beieinander.",
            "- `aktive_form_rekoppelnd`: aktive Formwahrnehmung bleibt mit guter Rekopplung verbunden.",
            "- `offene_sehkopplung`: Sehzustand ist noch nicht eindeutig interpretierbar.",
            "",
            "## Vorlaeufiger Befund",
            "",
            "Diese Diagnose trennt Sehen von Feldwirkung.",
            "Eine Form kann sichtbar, stabil oder unruhig sein, ohne automatisch als Feldlast zu gelten.",
            "Feldlast entsteht erst, wenn sichtbare Form, Memorylast und Rekopplung gemeinsam binden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Danach koennen Hoeren, Sehen und Fuehlen als multisensorische Kopplung verglichen werden.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Koppelt visuelle Sehzustande gegen MCM-Feldwirkung.")
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    rows = [_row(name, path_text, group) for name, path_text, group in specs]
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
