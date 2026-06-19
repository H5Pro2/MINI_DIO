from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from report_auditory_regulation import DEFAULT_SUMMARIES
from report_auditory_regulation import _fmt
from report_auditory_regulation import _row as auditory_row
from report_recoupling_quality import _resolve


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "226_AUDITIVE_FELDKOPPLUNG_DIAGNOSE.md"


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _row(name: str, path_text: str, group: str) -> dict:
    row = auditory_row(name, path_text, group)
    active_listen = row["hinhoeren_ratio"] + row["genauer_ratio"] + row["alarm_ratio"]
    filter_release = row["rauschen_ratio"] + row["abklingen_ratio"] + row["hintergrund_ratio"]
    field_binding = _clamp(
        (row["field_strain"] * 0.42)
        + (row["memory_load"] * 0.34)
        + (max(0.0, 0.64 - row["rekopplung"]) * 0.24)
    )
    auditory_load = _clamp(
        (row["avg_focus"] * 0.28)
        + (row["avg_alarm"] * 0.24)
        + (row["avg_aftertone"] * 0.18)
        + (row["alarm_ratio"] * 0.16)
        + (row["genauer_ratio"] * 0.14)
    )
    auditory_relief = _clamp(
        (row["rauschen_ratio"] * 0.30)
        + (row["abklingen_ratio"] * 0.24)
        + (row["hintergrund_ratio"] * 0.18)
        + (row["beruhigung_ratio"] * 0.16)
        + (max(0.0, row["rekopplung"] - 0.60) * 1.8 * 0.12)
    )
    coupling_gap = _clamp(field_binding - auditory_relief)
    auditory_field_fit = _clamp(1.0 - abs(auditory_load - field_binding))

    if field_binding > 0.20 and auditory_relief > 0.26:
        coupling_role = "filtert_aber_feld_bindet"
    elif field_binding > 0.20 and auditory_load >= auditory_relief:
        coupling_role = "hoerlast_feldnah"
    elif field_binding <= 0.12 and auditory_relief >= 0.26:
        coupling_role = "hoerfilter_entlastend"
    elif auditory_load > 0.28 and row["rekopplung"] >= 0.61:
        coupling_role = "aktiv_rekoppelnd"
    else:
        coupling_role = "offene_hoerkopplung"

    return {
        **row,
        "active_listen": active_listen,
        "filter_release": filter_release,
        "field_binding": field_binding,
        "auditory_load": auditory_load,
        "auditory_relief": auditory_relief,
        "coupling_gap": coupling_gap,
        "auditory_field_fit": auditory_field_fit,
        "coupling_role": coupling_role,
    }


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"]))

    role_counts: dict[str, int] = {}
    for row in rows:
        role_counts[row["coupling_role"]] = role_counts.get(row["coupling_role"], 0) + 1

    lines = [
        "# Auditive Feldkopplung - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt auditive Hoerzustande gegen MCM-Feldlast, Memorylast und Rekopplung.",
        "Sie prueft, ob Hoeren nur Oberflaechenlabel ist oder eine lesbare Feldkopplung besitzt.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Koppeln Hoerzustande messbar an MCM-Feldwirkung?",
        "2. Unterpruefung: aktive Hoeranteile, Filter-/Abklinganteile, Feldbindung und Rekopplung vergleichen.",
        "3. Folgeschritt: Bestimmen, ob Rauschenfiltern und Reizabklingen wirklich entlasten oder ob das Feld trotzdem bindet.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | Gruppe | Rolle | auditive Kopplung | aktiv hoeren | Filter/Abklingen | Hoerlast | Hoerentlastung | Feldbindung | Kopplungsluecke | Fit | Rekopplung |",
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
                    _fmt(row["active_listen"], 4),
                    _fmt(row["filter_release"], 4),
                    _fmt(row["auditory_load"], 4),
                    _fmt(row["auditory_relief"], 4),
                    _fmt(row["field_binding"], 4),
                    _fmt(row["coupling_gap"], 4),
                    _fmt(row["auditory_field_fit"], 4),
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
            "- `hoerfilter_entlastend`: Filter-/Abklinganteile sind hoch und Feldbindung bleibt niedrig.",
            "- `filtert_aber_feld_bindet`: Hoerfilter ist vorhanden, aber Feld/Memory binden trotzdem.",
            "- `hoerlast_feldnah`: auditive Last und Feldbindung liegen nah beieinander.",
            "- `aktiv_rekoppelnd`: aktives Hoeren bleibt mit guter Rekopplung verbunden.",
            "- `offene_hoerkopplung`: Hoerzustand ist noch nicht eindeutig interpretierbar.",
            "",
            "## Vorlaeufiger Befund",
            "",
            "Diese Diagnose trennt Hoeren von Feldwirkung.",
            "Rauschenfiltern oder Reizabklingen ist nur dann entlastend, wenn die Feldbindung niedrig bleibt.",
            "Wenn Feldlast und Memorylast hoch bleiben, ist auditive Filterung allein nicht ausreichend.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Dort wird bewertet, ob SOL 5m eine entlastende Hoerkopplung zeigt und warum Stress/1h trotz Filterung binden kann.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Koppelt auditive Hoerzustaende gegen MCM-Feldwirkung.")
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    rows = [_row(name, path_text, group) for name, path_text, group in specs]
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
