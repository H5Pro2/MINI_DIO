from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.market_melody import MelodyConfig
from mini_dio.market_melody import build_market_melody
from mini_dio.market_melody import read_candles
from mini_dio.market_melody import write_melody_csv

DATA_DEFAULT = ROOT / "data" / "kontrolliert_2023_negative_stress_10k_5m_SOLUSDT.csv"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "832_MARKTMELODIE_TONFOLGE.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "832_MARKTMELODIE_TONFOLGE.md"


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _write_markdown(path: Path, csv_path: Path, data_path: Path, frames: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    report_id = path.stem.split("_", 1)[0]
    role_counts = Counter(frame.tone_role for frame in frames)
    phrase_counts = Counter(frame.phrase_symbol for frame in frames)
    speech_counts = Counter(frame.speech_token for frame in frames)
    note_counts = Counter(f"{frame.note}{frame.octave}" for frame in frames)
    avg_pitch = _mean([frame.pitch_hz for frame in frames])
    avg_amplitude = _mean([frame.amplitude for frame in frames])
    avg_roughness = _mean([frame.roughness for frame in frames])
    avg_relative_energy = _mean([frame.relative_energy for frame in frames])

    lines = [
        f"# {report_id} - Marktmelodie Tonfolge",
        "",
        "## Zweck",
        "",
        "Diese Diagnose uebersetzt eine Aussenwelt passiv in eine tonale Spur.",
        "Sie ist keine Handlung, kein Gate und keine direkte MCM-Feldkopplung.",
        "",
        "Hierarchie:",
        "",
        "1. Chartdaten werden als Weltbewegung gelesen.",
        "2. Weltbewegung wird in Tonhoehe, Lautstaerke, Rauigkeit und Klangrolle uebersetzt.",
        "3. Wiederkehrende Tonrollen werden zu Melodiephrasen und DIO-Klangtokens verdichtet.",
        "4. Erst spaeter kann geprueft werden, ob bestimmte Klangphrasen mit MCM-Feldlagen koppeln.",
        "",
        "## Quelle",
        "",
        f"- Daten: `{data_path}`",
        f"- CSV: `{csv_path}`",
        f"- Frames: `{len(frames)}`",
        "",
        "## Globale Klangwerte",
        "",
        "| Wert | Ergebnis |",
        "|---|---:|",
        f"| durchschnittliche Tonhoehe Hz | {_fmt(avg_pitch, 2)} |",
        f"| durchschnittliche Lautstaerke | {_fmt(avg_amplitude)} |",
        f"| durchschnittliche Rauigkeit | {_fmt(avg_roughness)} |",
        f"| durchschnittliche relative Energie | {_fmt(avg_relative_energy)} |",
        f"| eindeutige Melodiephrasen | {len(phrase_counts)} |",
        f"| eindeutige Klangtokens | {len(speech_counts)} |",
        "",
        "## Klangrollen",
        "",
        "| Rolle | Anzahl | Anteil |",
        "|---|---:|---:|",
    ]
    total = max(1, len(frames))
    for role, count in role_counts.most_common():
        lines.append(f"| {role} | {count} | {_fmt(count / total)} |")
    lines.extend(["", "## Dominante Noten", "", "| Note | Anzahl |", "|---|---:|"])
    for note, count in note_counts.most_common(12):
        lines.append(f"| {note} | {count} |")
    lines.extend(["", "## Dominante Melodiephrasen", "", "| Phrase | Anzahl |", "|---|---:|"])
    for phrase, count in phrase_counts.most_common(12):
        lines.append(f"| `{phrase}` | {count} |")
    lines.extend(["", "## Dominante DIO-Klangtokens", "", "| Token | Anzahl |", "|---|---:|"])
    for token, count in speech_counts.most_common(12):
        lines.append(f"| `{token}` | {count} |")
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Marktmelodie ist eine rezeptorische Vorstufe des Hoerens.",
            "Sie macht aus Rohdaten keine Sprache im menschlichen Sinn, sondern eine wiederkehrende Klangfolge.",
            "Aus dieser Klangfolge koennen spaeter eigene DIO-Tokens und semantische Klangfamilien entstehen.",
            "",
            "Wichtig: Der Chart spricht nicht. MINI_DIO erhaelt eine tonale Weltspur, aus der sich bei Wiederkehr eigene Klangbedeutung bilden kann.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Tonfolge gegen MCM-Feldlagen gelegt werden. Dann sehen wir, ob bestimmte Melodiephrasen wiederkehrend mit stabiler Mitte, Randspannung oder offener Bruecke koppeln.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Erstellt eine passive Marktmelodie aus einer Welt-CSV.")
    parser.add_argument("--data", type=Path, default=DATA_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    parser.add_argument("--min-hz", type=float, default=110.0)
    parser.add_argument("--max-hz", type=float, default=1760.0)
    parser.add_argument("--phrase-size", type=int, default=4)
    args = parser.parse_args()

    data_path = args.data if args.data.is_absolute() else ROOT / args.data
    csv_path = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    md_path = args.md_out if args.md_out.is_absolute() else ROOT / args.md_out
    config = MelodyConfig(min_hz=args.min_hz, max_hz=args.max_hz, phrase_size=args.phrase_size)
    frames = build_market_melody(read_candles(data_path), config=config)
    write_melody_csv(csv_path, frames)
    _write_markdown(md_path, csv_path, data_path, frames)
    print(f"data={data_path}")
    print(f"frames={len(frames)}")
    print(f"wrote {csv_path}")
    print(f"wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
