from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.market_audio import WavRenderConfig
from mini_dio.market_audio import render_melody_csv_to_wav


MELODY_DEFAULT = ROOT / "docs" / "befunde" / "834_MARKTMELODIE_STRESS2024_TONFOLGE.csv"
WAV_DEFAULT = ROOT / "docs" / "audio" / "836_MARKTMELODIE_STRESS2024.wav"
MD_DEFAULT = ROOT / "docs" / "befunde" / "836_MARKTMELODIE_STRESS2024_WAV_DEBUG.md"


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def _fmt(value: float, digits: int = 3) -> str:
    return f"{value:.{digits}f}"


def _write_markdown(path: Path, melody_path: Path, wav_path: Path, stats: dict[str, float | int | str]) -> None:
    rows = _read_rows(melody_path)
    role_counts = Counter(str(row.get("tone_role") or "-") for row in rows)
    token_counts = Counter(str(row.get("speech_token") or "-") for row in rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 836 - Marktmelodie WAV Debug",
        "",
        "## Zweck",
        "",
        "Dieser Bericht erzeugt eine hoerbare WAV-Datei aus der passiven Marktmelodie.",
        "Die WAV-Datei ist ein Debug-Artefakt fuer menschliches Anhoeren, keine Handlung, kein Gate und keine direkte MCM-Feldwirkung.",
        "",
        "Kette:",
        "",
        "1. Welt wurde bereits in eine Marktmelodie uebersetzt.",
        "2. Die Melodie wird als Mono-WAV gerendert.",
        "3. Tonhoehe, Lautstaerke, Rauigkeit und Klangrolle werden hoerbar gemacht.",
        "",
        "## Quelle",
        "",
        f"- Melodie-CSV: `{melody_path}`",
        f"- WAV: `{wav_path}`",
        "",
        "## Audio-Daten",
        "",
        "| Wert | Ergebnis |",
        "|---|---:|",
        f"| Frames | {stats['frames']} |",
        f"| Sample Rate | {stats['sample_rate']} Hz |",
        f"| Sekunden pro Frame | {_fmt(float(stats['seconds_per_frame']), 4)} |",
        f"| Dauer | {_fmt(float(stats['duration_seconds']), 2)} s |",
        f"| Peak | {_fmt(float(stats['peak']), 4)} |",
        "",
        "## Klangrollen",
        "",
        "| Rolle | Anzahl |",
        "|---|---:|",
    ]
    for role, count in role_counts.most_common():
        lines.append(f"| {role} | {count} |")
    lines.extend(["", "## Dominante Klangtokens", "", "| Token | Anzahl |", "|---|---:|"])
    for token, count in token_counts.most_common(12):
        lines.append(f"| `{token}` | {count} |")
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die WAV-Ausgabe macht die energetische Weltspur auditiv pruefbar.",
            "Sie ersetzt nicht die CSV-Diagnose, sondern hilft zu hoeren, ob die Welt eher ruhig, bruechig, gespannt oder tragend wirkt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine zweite Welt als WAV gerendert werden. Dann kann geprueft werden, ob sich unterschiedliche Welten auch akustisch klar unterscheiden.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Rendert eine MINI_DIO-Marktmelodie als WAV-Debug.")
    parser.add_argument("--melody", type=Path, default=MELODY_DEFAULT)
    parser.add_argument("--wav-out", type=Path, default=WAV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    parser.add_argument("--sample-rate", type=int, default=22050)
    parser.add_argument("--seconds-per-frame", type=float, default=0.025)
    parser.add_argument("--volume", type=float, default=0.45)
    parser.add_argument("--max-frames", type=int, default=0)
    args = parser.parse_args()

    melody_path = args.melody if args.melody.is_absolute() else ROOT / args.melody
    wav_path = args.wav_out if args.wav_out.is_absolute() else ROOT / args.wav_out
    md_path = args.md_out if args.md_out.is_absolute() else ROOT / args.md_out
    config = WavRenderConfig(
        sample_rate=args.sample_rate,
        seconds_per_frame=args.seconds_per_frame,
        master_volume=args.volume,
    )
    max_frames = args.max_frames if args.max_frames > 0 else None
    stats = render_melody_csv_to_wav(melody_path, wav_path, config=config, max_frames=max_frames)
    _write_markdown(md_path, melody_path, wav_path, stats)
    print(f"melody={melody_path}")
    print(f"wav={wav_path}")
    print(f"frames={stats['frames']}")
    print(f"duration_seconds={stats['duration_seconds']:.2f}")
    print(f"wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
