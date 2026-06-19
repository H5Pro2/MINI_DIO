from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from report_auditory_field_coupling import _row as auditory_row
from report_auditory_regulation import DEFAULT_SUMMARIES
from report_auditory_regulation import _fmt
from report_recoupling_quality import _resolve
from report_visual_field_coupling import _row as visual_row


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "232_MULTISENSORISCHE_KOPPLUNG_DIAGNOSE.md"


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _row(name: str, path_text: str, group: str) -> dict:
    auditory = auditory_row(name, path_text, group)
    visual = visual_row(name, path_text, group)

    hearing_load = auditory["auditory_load"]
    seeing_load = visual["visual_load"]
    hearing_relief = auditory["auditory_relief"]
    seeing_relief = visual["visual_relief"]
    field_binding = (auditory["field_binding"] + visual["field_binding"]) * 0.5
    recoupling = (auditory["rekopplung"] + visual["rekopplung"]) * 0.5
    memory_load = (auditory["memory_load"] + visual["memory_load"]) * 0.5
    field_strain = (auditory["field_strain"] + visual["field_strain"]) * 0.5

    sensory_load = _clamp((hearing_load * 0.50) + (seeing_load * 0.50))
    sensory_relief = _clamp((hearing_relief * 0.50) + (seeing_relief * 0.50))
    sensory_balance = _clamp(0.5 + ((sensory_relief - sensory_load) * 0.5))
    field_pressure = _clamp((field_binding * 0.42) + (memory_load * 0.28) + (field_strain * 0.20) + (max(0.0, 0.64 - recoupling) * 0.10))
    multisensory_fit = _clamp(1.0 - abs(sensory_load - field_pressure))
    sensory_conflict = _clamp(abs(hearing_load - seeing_load) + abs(hearing_relief - seeing_relief) * 0.5)
    harmonic_support = _clamp((sensory_balance * 0.34) + (multisensory_fit * 0.30) + (recoupling * 0.22) + (max(0.0, 0.22 - field_pressure) * 0.14))
    overload_pressure = _clamp((field_pressure * 0.38) + (sensory_load * 0.28) + (sensory_conflict * 0.20) + (memory_load * 0.14))

    if harmonic_support >= 0.66 and overload_pressure < 0.30:
        coupling_role = "multisensorisch_tragend"
    elif overload_pressure >= 0.34 and sensory_conflict >= 0.16:
        coupling_role = "sinnesachsen_konflikt"
    elif overload_pressure >= 0.32:
        coupling_role = "multisensorisch_belastet"
    elif multisensory_fit >= 0.90 and recoupling >= 0.60:
        coupling_role = "rekoppelnde_sinnesnaehe"
    else:
        coupling_role = "offene_multisensorik"

    return {
        "name": name,
        "group": group,
        "auditory_role": auditory["coupling_role"],
        "visual_role": visual["coupling_role"],
        "field_role": auditory["role"],
        "hearing_load": hearing_load,
        "seeing_load": seeing_load,
        "hearing_relief": hearing_relief,
        "seeing_relief": seeing_relief,
        "sensory_load": sensory_load,
        "sensory_relief": sensory_relief,
        "field_pressure": field_pressure,
        "recoupling": recoupling,
        "sensory_conflict": sensory_conflict,
        "multisensory_fit": multisensory_fit,
        "harmonic_support": harmonic_support,
        "overload_pressure": overload_pressure,
        "coupling_role": coupling_role,
    }


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"]))

    role_counts: dict[str, int] = {}
    for row in rows:
        role_counts[row["coupling_role"]] = role_counts.get(row["coupling_role"], 0) + 1

    lines = [
        "# Multisensorische Kopplung - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt Hoeren, Sehen und MCM-Feldwirkung zusammen.",
        "Sie prueft, ob eine Weltlage erst durch gemeinsame Sinneskopplung tragend oder belastend wird.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Bilden Hoeren, Sehen und MCM-Feld zusammen eine lesbare Innenlage?",
        "2. Unterpruefung: Hoerlast, Sehlast, Sinnesentlastung, Felddruck, Rekopplung und Sinneskonflikt vergleichen.",
        "3. Folgeschritt: Pruefen, ob harmonische Welten an gemeinsamer Rekopplung und niedriger Ueberlast liegen.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | Gruppe | multisensorische Rolle | Hoeren | Sehen | Feld | Hoerlast | Sehlast | Sinneslast | Sinnesentlastung | Felddruck | Konflikt | Fit | Harmonie | Ueberlast | Rekopplung |",
        "|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["group"],
                    row["coupling_role"],
                    row["auditory_role"],
                    row["visual_role"],
                    row["field_role"],
                    _fmt(row["hearing_load"], 4),
                    _fmt(row["seeing_load"], 4),
                    _fmt(row["sensory_load"], 4),
                    _fmt(row["sensory_relief"], 4),
                    _fmt(row["field_pressure"], 4),
                    _fmt(row["sensory_conflict"], 4),
                    _fmt(row["multisensory_fit"], 4),
                    _fmt(row["harmonic_support"], 4),
                    _fmt(row["overload_pressure"], 4),
                    _fmt(row["recoupling"], 6),
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
            "- `multisensorisch_tragend`: Sinneslast bleibt niedrig, Rekopplung ist tragend, Felddruck bleibt gering.",
            "- `rekoppelnde_sinnesnaehe`: Hoeren, Sehen und Feld liegen nah beieinander, ohne starke Ueberlast.",
            "- `multisensorisch_belastet`: Sinneslast und Felddruck steigen gemeinsam.",
            "- `sinnesachsen_konflikt`: Hoeren und Sehen laufen auseinander und belasten die Feldnaehe.",
            "- `offene_multisensorik`: gemeinsame Sinneslage ist noch nicht eindeutig interpretierbar.",
            "",
            "## Vorlaeufiger Befund",
            "",
            "Diese Diagnose ist die erste Zusammenfuehrung der drei passiven Wahrnehmungsachsen.",
            "Sie ersetzt keine Einzelachse.",
        "Sie prueft nur, ob Hoeren, Sehen und MCM-Feldwirkung zusammen eine stabilere Innenlage beschreiben als jede Achse allein.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Danach kann entschieden werden, ob die multisensorische Kopplung als Standarddiagnose fuer weitere Welten genutzt wird.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Koppelt Hoeren, Sehen und MCM-Feldwirkung passiv.")
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    rows = [_row(name, path_text, group) for name, path_text, group in specs]
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
