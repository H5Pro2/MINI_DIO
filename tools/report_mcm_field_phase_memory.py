from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_field_phase_memory import MCMFieldPhaseMemory


DEFAULT_INPUTS = [
    befunde_root(ROOT) / "1225_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_TRANSITIONS.csv",
    befunde_root(ROOT) / "1227_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_1H_TRANSITIONS.csv",
    befunde_root(ROOT) / "1229_SYNTHETISCHE_SINNESACHSEN_STRESS_FELDPHASEN_TRANSITIONS.csv",
]
DEFAULT_OUT = befunde_root(ROOT) / "1242_MCM_FELDPHASEN_MEMORY.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, memory: MCMFieldPhaseMemory, inputs: list[Path]) -> None:
    rows = memory.to_rows()
    top_rows = rows[:24]
    profile = memory.quality_profile()
    lines: list[str] = [
        "# MCM-Feldphasen-Memory",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Zweck",
        "",
        "Diese Datei verdichtet vorhandene Feldphasen-Uebergaenge in eine passive Feldphasen-Memory.",
        "",
        "Sie ist:",
        "",
        "- keine Handlungsschicht,",
        "- kein Gate,",
        "- keine Strategie,",
        "- kein Richtungssignal.",
        "",
        "Sie speichert nur, welche Feldrollenfolgen wiederkehren.",
        "",
        "## Eingaben",
        "",
    ]
    for input_path in inputs:
        lines.append(f"- `{input_path.relative_to(ROOT)}`")

    lines.extend(
        [
            "",
            "## Profil",
            "",
            f"- Phasenfamilien: `{profile['records']}`",
            f"- Qualitaeten: `{profile['phase_memory_quality']}`",
            f"- Wirkungen: `{profile['dominant_effect']}`",
            "",
            "## Staerkste Phasenfamilien",
            "",
            "| Phase | Anzahl | Welten | Wirkung | Qualitaet | Rekopplung danach | Strain danach | Notiz |",
            "|---|---:|---:|---|---|---:|---:|---|",
        ]
    )
    for row in top_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["phase_key"]),
                    str(row["seen_count"]),
                    str(row["world_count"]),
                    str(row["dominant_effect"]),
                    str(row["phase_memory_quality"]),
                    _fmt(row["avg_rekopplung_delta_to_next"]),
                    _fmt(row["avg_strain_delta_to_next"]),
                    str(row["phase_note"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "MINI_DIO kann Feldphasen nicht nur als Einzelrollen lesen, sondern als wiederkehrende Bewegungsfolgen verdichten.",
            "",
            "Besonders wichtig ist die Trennung:",
            "",
            "```text",
            "Feldrolle = momentane Innenfeldlage",
            "Feldphase = Bewegung dieser Lage ueber Vorher/Jetzt/Nachher",
            "```",
            "",
            "Damit entsteht mehr Tiefe, ohne Handlung zu erzeugen.",
            "",
            "## Grenze",
            "",
            "Diese Memory darf nicht direkt in Handlung, Richtung oder Bewertung uebersetzt werden.",
            "Sie beschreibt passive Phasenerfahrung.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verdichtet Feldphasen-Transitionen in eine passive MCM-Feldphasen-Memory."
    )
    parser.add_argument("--input", action="append", default=[], help="Transition-CSV. Kann mehrfach angegeben werden.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    args = parser.parse_args()

    inputs = [_resolve(path) for path in (args.input or [])]
    if not inputs:
        inputs = [path for path in DEFAULT_INPUTS if path.exists()]
    missing = [path for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("Fehlende Eingaben: " + ", ".join(str(path) for path in missing))

    out_path = _resolve(args.out)
    memory = MCMFieldPhaseMemory.from_transition_csv_paths(inputs)
    memory.write_csv(out_path.with_suffix(".csv"))
    memory.write_json(out_path.with_suffix(".json"))
    _write_markdown(out_path, memory, inputs)

    print(f"inputs={len(inputs)} records={len(memory.records)} out={out_path}")
    for row in memory.to_rows()[:12]:
        print(
            f"{row['phase_key']} | {row['phase_memory_quality']} | "
            f"{row['dominant_effect']} | seen={row['seen_count']}"
        )


if __name__ == "__main__":
    main()
