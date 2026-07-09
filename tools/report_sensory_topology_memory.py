from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.sensory_topology_memory import SensoryTopologyMemory


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], role_index: dict[str, list[str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    strongest = max(rows, key=lambda row: float(row["carrying_quality"]))
    weakest = min(rows, key=lambda row: float(row["carrying_quality"]))
    lines = [
        "# Sinnesaufnahme Topologie Memory",
        "",
        "Passive Verdichtung von Sinnes-Signaturen zu Feldrollen.",
        "",
        "Diese Memory ist keine Handlungsschicht. Sie speichert, welche Aufnahmeform mit welcher Feldrolle und welcher Tragqualitaet zusammen auftritt.",
        "",
        "## Signaturen",
        "",
        "| Signatur | Rolle | Segmente | Dauer | Rekopplung | Strain | Rohfeld | Tragqualitaet | Hoeren | Sehen | Fuehlen |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| {sensory_signature} | {dominant_role} | {segments} | {duration} | {avg_rekopplung:.4f} | {avg_strain:.4f} | {avg_raw_field:.4f} | {carrying_quality:.4f} | {hearing_preference} | {vision_preference} | {feeling_preference} |".format(
                **row
            )
        )

    lines.extend(["", "## Rollenindex", ""])
    for role, signatures in role_index.items():
        lines.append(f"- `{role}`: " + ", ".join(f"`{item}`" for item in signatures))

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Staerkste Tragqualitaet: `{strongest['sensory_signature']}` -> `{strongest['dominant_role']}` mit `{float(strongest['carrying_quality']):.4f}`.",
            f"- Schwaechste Tragqualitaet: `{weakest['sensory_signature']}` -> `{weakest['dominant_role']}` mit `{float(weakest['carrying_quality']):.4f}`.",
            "",
            "## Bewertung",
            "",
            "Mini-DIO kann Sinnesaufnahme jetzt als passive Bedeutungsnaehe speichern: nicht als Rohdatenstrom, sondern als wiederkehrende Aufnahmeform mit Feldrolle.",
            "",
            "Zusaetzlich erzeugt die Memory jetzt eine achsenabhaengige Rezeptor-Praeferenz. Sie ist keine Handlung und kein Gate. Sie beschreibt nur, ob Mini-DIO bei aehnlicher Aufnahme eher Hoeren, Sehen oder Fuehlen hochregeln, herunterregeln oder halten sollte.",
            "",
            "Das ist die Grundlage fuer eine spaetere lernende Rezeptorschicht. Sie kann im naechsten Schritt nicht entscheiden, aber lesen: Diese Aufnahmeart fuehrt haeufig zu Zentrum, Bruecke, Offenheit oder Rand und legt eine bestimmte Sinneshaltung nahe.",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="docs/befunde/1001-2000/1001-1500/1274_SINNESAUFNAHME_TOPOLOGIE_KOPPLUNG.csv")
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1276_SINNESAUFNAHME_TOPOLOGIE_MEMORY.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1276_SINNESAUFNAHME_TOPOLOGIE_MEMORY.csv")
    args = parser.parse_args()

    memory = SensoryTopologyMemory()
    for row in _load(Path(args.input)):
        memory.observe_row(row)
    rows = memory.rows()
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, memory.role_index(), Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
