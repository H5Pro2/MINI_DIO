from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "122_STRESS_GEGENPOL_DIAGNOSE.md"


DEFAULT_WORLDS = [
    ("welt_2023_stress_01", "debug/research_chain_2023_stress_01", "data/kontrolliert_2023_real_test4_1000_5m_SOLUSDT.csv"),
    ("welt_2024_bridge3_01", "debug/research_chain_2024_bridge3_01", "data/kontrolliert_2024_bridge_test3_1000_5m_SOLUSDT.csv"),
    ("welt_2025_core_01", "debug/research_chain_2025_core_01", "data/kontrolliert_2025_core_test1_1000_5m_SOLUSDT.csv"),
    ("welt_2025_late_shift_01", "debug/research_chain_2025_late_shift_01", "data/kontrolliert_2025_late_shift_test_1000_5m_SOLUSDT.csv"),
]


def _path(path_text: str) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(row: dict, key: str) -> float:
    try:
        return float(row.get(key) or 0.0)
    except Exception:
        return 0.0


def _read_world(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _read_episodes(debug_root: Path) -> list[dict]:
    path = debug_root / "dio_mini_lauf_2" / "episodes.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _world_segment_metrics(world_rows: list[dict], start: int, end: int) -> dict[str, float]:
    rows = world_rows[start:end]
    closes = [float(row["close"]) for row in rows]
    highs = [float(row["high"]) for row in rows]
    lows = [float(row["low"]) for row in rows]
    returns = [
        abs((closes[index] - closes[index - 1]) / closes[index - 1])
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
    ranges = [(high - low) / close for high, low, close in zip(highs, lows, closes) if close]
    drift = ((closes[-1] - closes[0]) / closes[0]) if len(closes) >= 2 and closes[0] else 0.0
    direction_changes = sum(
        1
        for index in range(2, len(closes))
        if (closes[index] - closes[index - 1]) * (closes[index - 1] - closes[index - 2]) < 0
    )
    return {
        "avg_abs_return": sum(returns) / max(1, len(returns)),
        "max_abs_return": max(returns) if returns else 0.0,
        "avg_range": sum(ranges) / max(1, len(ranges)),
        "drift": drift,
        "direction_changes": float(direction_changes),
    }


def _episode_segment_metrics(episodes: list[dict], start: int, end: int) -> dict:
    rows = episodes[start:end]
    class_counts = Counter(row.get("passive_mcm_effect_class", "-") for row in rows)
    strained = class_counts.get("gespannt", 0) + class_counts.get("kippend", 0)
    carried_unrest = class_counts.get("tragend_unruhig", 0)
    stable = class_counts.get("stabil", 0)
    total = max(1, len(rows))

    def avg(key: str) -> float:
        return sum(_float(row, key) for row in rows) / total

    return {
        "class_counts": dict(class_counts),
        "stress_ratio": strained / total,
        "carried_unrest_ratio": carried_unrest / total,
        "stable_ratio": stable / total,
        "mcm_rekopplung": avg("mcm_rekopplung_quality"),
        "mcm_carry": avg("mcm_carry_quality"),
        "mcm_strain": avg("mcm_strain_quality"),
        "mcm_sensory": avg("mcm_sensory_coupling"),
        "visual_gap": avg("mcm_visual_field_gap"),
        "hearing_gap": avg("mcm_hearing_field_gap"),
        "sehen_flow": avg("sehen_form_flow"),
        "sehen_change": avg("sehen_form_change"),
        "hoeren_tone": avg("hoeren_energy_tone"),
        "hoeren_shift": avg("hoeren_energy_shift"),
        "fuehlen_coherence": avg("fuehlen_mcm_coherence"),
        "fuehlen_tension": avg("fuehlen_mcm_tension"),
        "fuehlen_asymmetry": avg("fuehlen_mcm_asymmetry"),
        "episode_memory_count": sum(1 for row in rows if row.get("episode_memory_symbol", "-") not in ("", "-")),
    }


def analyze_world(name: str, debug_root: Path, data_path: Path, segments: int) -> dict:
    world_rows = _read_world(data_path)
    episodes = _read_episodes(debug_root)
    segment_size = max(1, min(len(world_rows), len(episodes)) // segments)
    segment_rows = []
    for index in range(segments):
        start = index * segment_size
        end = min(start + segment_size, min(len(world_rows), len(episodes)))
        if index == segments - 1:
            end = min(len(world_rows), len(episodes))
        world = _world_segment_metrics(world_rows, start, end)
        episode = _episode_segment_metrics(episodes, start, end)
        segment_rows.append(
            {
                "segment": index + 1,
                "start": start,
                "end": end,
                "world": world,
                "episode": episode,
                "stress_score": (
                    episode["stress_ratio"] * 0.42
                    + episode["carried_unrest_ratio"] * 0.18
                    + world["avg_abs_return"] * 40.0
                    + world["avg_range"] * 22.0
                    + episode["mcm_strain"] * 0.24
                    + episode["episode_memory_count"] / max(1, (end - start)) * 0.12
                    - episode["mcm_rekopplung"] * 0.14
                ),
            }
        )
    top_segments = sorted(segment_rows, key=lambda row: row["stress_score"], reverse=True)[:3]
    return {
        "name": name,
        "debug_root": str(debug_root.relative_to(ROOT)),
        "data_path": str(data_path.relative_to(ROOT)),
        "segments": segment_rows,
        "top_segments": top_segments,
    }


def write_markdown(results: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Stress-Gegenpol-Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose untersucht, welche Rohwelt- und Innenfeldmerkmale den Stress-Gegenpol begleiten.",
        "Sie ist passiv: Sie erzeugt keine Handlung, kein Gate und keine Regel.",
        "",
        "Hierarchie der Prüfung:",
        "",
        "1. Grundfrage: Warum kippt eine Welt in stärkere innere Verarbeitungslast?",
        "2. Unterprüfung: Welche Abschnitte tragen erhöhte Spannung, Kippnähe und Episodenmemory?",
        "3. Folgeschritt: Prüfen, ob diese Merkmale bei neuen Stresswelten wiederkehren.",
        "",
        "## Ergebnisübersicht",
        "",
    ]

    for result in results:
        lines.extend(
            [
                f"### {result['name']}",
                "",
                f"- Datenwelt: `{result['data_path']}`",
                f"- Debug: `{result['debug_root']}`",
                "",
                "Top-Stressabschnitte:",
                "",
            ]
        )
        for segment in result["top_segments"]:
            world = segment["world"]
            episode = segment["episode"]
            lines.extend(
                [
                    f"- Abschnitt `{segment['segment']}` (`{segment['start']}`-`{segment['end']}`): "
                    f"stress_score `{segment['stress_score']:.4f}`, "
                    f"stress_ratio `{episode['stress_ratio']:.3f}`, "
                    f"tragend_unruhig `{episode['carried_unrest_ratio']:.3f}`, "
                    f"Rekopplung `{episode['mcm_rekopplung']:.3f}`, "
                    f"avg_abs_return `{world['avg_abs_return']:.4f}`, "
                    f"avg_range `{world['avg_range']:.4f}`, "
                    f"Episodenmemory `{episode['episode_memory_count']}`",
                ]
            )
        lines.append("")

    lines.extend(["## Abschnittsdetails", ""])
    for result in results:
        lines.extend([f"### {result['name']}", ""])
        lines.extend(
            [
                "| Abschnitt | Stress | Tragend unruhig | Stabil | Rekopplung | Tragqualität | Roh-Bewegung | Range | Drift | Memory |",
                "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for segment in result["segments"]:
            world = segment["world"]
            episode = segment["episode"]
            lines.append(
                f"| {segment['segment']} | "
                f"{episode['stress_ratio']:.3f} | "
                f"{episode['carried_unrest_ratio']:.3f} | "
                f"{episode['stable_ratio']:.3f} | "
                f"{episode['mcm_rekopplung']:.3f} | "
                f"{episode['mcm_carry']:.3f} | "
                f"{world['avg_abs_return']:.4f} | "
                f"{world['avg_range']:.4f} | "
                f"{world['drift']:.3f} | "
                f"{episode['episode_memory_count']} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Befund",
            "",
            "Der Stress-Gegenpol entsteht in den bisherigen Läufen nicht durch ein einzelnes Merkmal.",
            "Er zeigt eine Kopplung aus höherer Rohweltbewegung, größerer Range, erhöhter Kipp-/Spannungswirkung, niedrigerer Rekopplung und mehr Episodenmemory.",
            "",
            "Fachlich gelesen heißt das: MINI_DIO reagiert nicht nur auf Bewegung, sondern auf eine Belastungskombination aus Weltunruhe und Innenfeld-Rekopplungsverlust.",
            "",
            "Die Diagnose bleibt passiv. Sie beschreibt, welche Abschnitte Last tragen; sie entscheidet nicht, was MINI_DIO tun soll.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte eine neue Stresswelt gegen diese Abschnittsmerkmale geprüft werden. Entscheidend ist, ob der Stress-Gegenpol wieder aus derselben Kombination entsteht oder ob ein anderer Belastungstyp sichtbar wird.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analysiere den passiven Stress-Gegenpol abschnittsweise.")
    parser.add_argument("--world", action="append", nargs=3, metavar=("NAME", "DEBUG_ROOT", "DATA_CSV"))
    parser.add_argument("--segments", type=int, default=10)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    worlds = args.world or DEFAULT_WORLDS
    results = [analyze_world(name, _path(debug_root), _path(data_csv), args.segments) for name, debug_root, data_csv in worlds]
    out_path = _path(args.out)
    write_markdown(results, out_path)
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
