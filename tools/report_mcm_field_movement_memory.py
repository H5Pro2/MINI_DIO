from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_field_movement_memory import MCMFieldMovementMemory

DEFAULT_INPUTS = [
    ROOT / "docs" / "befunde" / "386_JAHRES_ZEITAUFLOESUNGS_MATRIX_GERICHTETE_FELDBEWEGUNG.csv",
    ROOT / "docs" / "befunde" / "391_KAS_ASSET_GEGENPROBE_PASSIVE_REGULATIONSQUALITAET_reproduktion.csv",
]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "394_MCM_FELDBEWEGUNGS_MEMORY_SUMMARY.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, memory: MCMFieldMovementMemory, inputs: list[Path]) -> None:
    rows = memory.to_rows()
    carried = [row for row in rows if row["field_memory_quality"] == "recurrently_carried"]
    fragmented = [row for row in rows if row["field_memory_quality"] == "recurrently_fragmented"]
    young = [row for row in rows if row["field_memory_quality"] == "young"]
    open_rows = [row for row in rows if row["field_memory_quality"] == "open_drifting"]
    reconnecting = [row for row in rows if row["field_memory_quality"] == "recurrently_reconnecting"]
    opening_strain = [row for row in rows if row["field_memory_quality"] == "recurrently_opening_strain"]
    lines: list[str] = [
        "# MCM-Feldbewegungs-Memory Summary",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Zweck",
        "",
        "Dieser Report verdichtet vorhandene passive Befunde in eine erste MCM-Feldbewegungs-Memory.",
        "Er ist keine Handlungsschicht, kein Gate und keine Strategie.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche gerichteten MCM-Feldbewegungen tragen wiederkehrende Feldwirkung?",
        "2. Unterpruefung: Welche Bewegungen wirken wiederkehrend getragen, rekoppelnd, oeffnend, fragmentiert oder offen driftend?",
        "3. Folgeschritt: Diese passive Erinnerung kann spaeter als Innenfeld-Leseschicht dienen, ohne Handlung zu erzwingen.",
        "",
        "## Eingaben",
        "",
    ]
    for input_path in inputs:
        lines.append(f"- `{input_path.relative_to(ROOT)}`")

    lines.extend(
        [
            "",
            "Quellenhinweis:",
            "",
            "Dieser Report kann mehrere Ableitungen derselben Grundbefunde enthalten.",
            "Er liest deshalb die wiederkehrende Richtung als Verdichtungsbefund, nicht als unabhaengige statistische Beweiszahl.",
        ]
    )

    lines.extend(
        [
            "",
            "## Passive Verdichtung",
            "",
            "| Bewegung | Beobachtungen | Ereignisse | dominante Tragart | Bewegungswirkung | Feldmemory-Qualitaet | Reifungsnotiz | Druck | Rekopplung | Strain | Lautheit | Drift |",
            "|---|---:|---:|---|---|---|---|---:|---:|---:|---:|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["movement_key"]),
                    str(row["seen_count"]),
                    str(row["total_events"]),
                    str(row["dominant_tragart"]),
                    str(row.get("dominant_movement_effect", "-")),
                    str(row["field_memory_quality"]),
                    str(row["maturity_note"]),
                    _fmt(row.get("avg_pressure_delta", 0.0)),
                    _fmt(row.get("avg_rekopplung_delta", 0.0)),
                    _fmt(row.get("avg_strain_delta", 0.0)),
                    _fmt(row.get("avg_loudness_delta", 0.0)),
                    str(row["dominant_drift_label"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die bisherige Verdichtung bleibt passiv:",
            "",
        ]
    )
    if reconnecting:
        for row in reconnecting:
            lines.append(
                f"- `{row['movement_key']}` wird als wiederkehrend rekoppelnde/entlastende Feldbewegung gelesen."
            )
    if opening_strain:
        for row in opening_strain:
            lines.append(
                f"- `{row['movement_key']}` wird als wiederkehrend oeffnende, lautere und strain-naehere Feldbewegung gelesen."
            )
    if carried:
        for row in carried:
            lines.append(
                f"- `{row['movement_key']}` wird als wiederkehrend getragen gelesen."
            )
    if fragmented:
        for row in fragmented:
            lines.append(
                f"- `{row['movement_key']}` wird als wiederkehrend fragmentiert gelesen."
            )
    if open_rows:
        for row in open_rows:
            lines.append(
                f"- `{row['movement_key']}` wird als offen driftend gelesen."
            )
    if young:
        for row in young:
            lines.append(
                f"- `{row['movement_key']}` bleibt jung: beobachtet, aber noch nicht gereift."
            )
    if not rows:
        lines.append("- Keine verwertbaren Bewegungen gefunden.")

    lines.extend(
        [
            "",
            "Wichtig: Diese Qualitaeten sind keine Regeln. Sie beschreiben gewachsene Innenfeldspuren.",
            "",
            "## Export",
            "",
            f"- CSV: `{path.with_suffix('.csv').relative_to(ROOT)}`",
            f"- JSON: `{path.with_suffix('.json').relative_to(ROOT)}`",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes kann diese MCM-Feldbewegungs-Memory gegen weitere Welten laufen, um zu pruefen, ob neue Bewegungen jung bleiben, driften oder wiederkehrend tragen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verdichtet passive Feldbewegungsbefunde in eine MCM-Feldbewegungs-Memory-Zusammenfassung."
    )
    parser.add_argument(
        "--input",
        action="append",
        default=[],
        help="CSV-Eingabe. Kann mehrfach angegeben werden.",
    )
    parser.add_argument(
        "--out",
        default=str(DEFAULT_OUT),
        help="Markdown-Ausgabe.",
    )
    args = parser.parse_args()

    inputs = [_resolve(path) for path in (args.input or [])]
    if not inputs:
        inputs = [path for path in DEFAULT_INPUTS if path.exists()]

    missing = [path for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("Fehlende Eingaben: " + ", ".join(str(path) for path in missing))

    out_path = _resolve(args.out)
    memory = MCMFieldMovementMemory.from_csv_paths(inputs)
    memory.write_csv(out_path.with_suffix(".csv"))
    memory.write_json(out_path.with_suffix(".json"))
    _write_markdown(out_path, memory, inputs)

    print(f"inputs={len(inputs)} records={len(memory.records)} out={out_path}")
    for row in memory.to_rows():
        print(
            f"{row['movement_key']} | {row['field_memory_quality']} | "
            f"{row['dominant_tragart']} | events={row['total_events']}"
        )


if __name__ == "__main__":
    main()
