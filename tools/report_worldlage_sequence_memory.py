from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.worldlage_classifier import classify_worldlage
from mini_dio.worldlage_sequence_memory import WorldlageSequenceMemory
from tools.report_receptor_preference_ab_test import (
    DEFAULT_WORLDS,
    _add_tick,
    _apply_preference,
    _effect,
    _empty_summary,
    _finish_summary,
    _load_preferences,
    _signature,
)
from mini_dio.mini_world import build_senses_world_relative, build_sensory_profile, load_candles


def _parse_world(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("world must be LABEL=PATH")
    label, path = value.split("=", 1)
    return label, path


def _block_row(world: str, mode: str, ticks: list[tuple[dict, dict]]) -> dict[str, object]:
    summary = _empty_summary(world, mode)
    for senses, effect in ticks:
        _add_tick(summary, senses, effect)
    return _finish_summary(summary)


def _world_blocks(label: str, path: Path, preferences: dict[str, dict[str, str]], *, limit: int, window: int, block_size: int) -> list[dict[str, object]]:
    candles = load_candles(path)
    if limit > 0:
        candles = candles[:limit]
    profile = build_sensory_profile(candles, window=window)
    blocks: list[dict[str, object]] = []
    base_ticks: list[tuple[dict, dict]] = []
    adapted_ticks: list[tuple[dict, dict]] = []

    def flush(block_index: int) -> None:
        if not base_ticks:
            return
        base = _block_row(label, "A_BASE", base_ticks)
        adapted = _block_row(label, "B_PREF", adapted_ticks)
        base["block_index"] = block_index
        adapted["block_index"] = block_index
        base["worldlage"] = classify_worldlage(base)
        adapted["worldlage"] = classify_worldlage(adapted)
        blocks.append({"base": base, "adapted": adapted})
        base_ticks.clear()
        adapted_ticks.clear()

    block_index = 0
    for index in range(len(candles)):
        base_senses = build_senses_world_relative(candles, index, window=window, profile=profile)
        base_effect = _effect(base_senses)
        pref = preferences.get(_signature(base_senses, base_effect))
        adapted_senses = _apply_preference(base_senses, pref) if pref else base_senses
        base_ticks.append((base_senses, base_effect))
        adapted_ticks.append((adapted_senses, _effect(adapted_senses)))
        if len(base_ticks) >= block_size:
            flush(block_index)
            block_index += 1
    flush(block_index)
    return blocks


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(sequence_rows: list[dict[str, object]], detail_rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    role_counts = Counter(str(row["base_sequence"]) for row in detail_rows)
    lines = [
        "# Weltlagen-Folgememory",
        "",
        "Passive Blockfolgen der gemessenen Weltlage.",
        "",
        "Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:",
        "",
        "```text",
        "vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung",
        "```",
        "",
        "## Verdichtete Folgen",
        "",
        "| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |",
        "|---|---:|---|---|---:|---:|---:|---:|",
    ]
    for row in sequence_rows:
        lines.append(
            "| {worldlage_sequence} | {occurrences} | {dominant_outcome} | {outcome_counts} | {avg_delta_zentrum:.4f} | {avg_delta_rand:.4f} | {avg_delta_rekopplung:.4f} | {avg_delta_strain:.4f} |".format(
                **row
            )
        )

    lines.extend(["", "## Haeufigste Rohfolgen", ""])
    for sequence, count in role_counts.most_common(12):
        lines.append(f"- `{sequence}`: `{count}`")

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.",
            "",
            "Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.",
            "",
            "Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", type=_parse_world)
    parser.add_argument("--preference-memory", default="docs/befunde/1279_SINNESAUFNAHME_TOPOLOGIE_REPRO_MEMORY.csv")
    parser.add_argument("--limit", type=int, default=2000)
    parser.add_argument("--window", type=int, default=5)
    parser.add_argument("--block-size", type=int, default=100)
    parser.add_argument("--out", default="docs/befunde/1302_WELTLAGEN_FOLGEMEMORY.md")
    parser.add_argument("--csv-out", default="docs/befunde/1302_WELTLAGEN_FOLGEMEMORY.csv")
    parser.add_argument("--detail-out", default="docs/befunde/1302_WELTLAGEN_FOLGEMEMORY_DETAILS.csv")
    args = parser.parse_args()

    preferences = _load_preferences(Path(args.preference_memory))
    worlds = dict(args.world or DEFAULT_WORLDS.items())
    memory = WorldlageSequenceMemory()
    details: list[dict[str, object]] = []
    for label, world_path in worlds.items():
        blocks = _world_blocks(label, Path(world_path), preferences, limit=args.limit, window=args.window, block_size=max(5, args.block_size))
        for index in range(1, len(blocks)):
            previous = blocks[index - 1]
            current = blocks[index]
            previous_lage = str(previous["base"]["worldlage"])
            current_lage = str(current["base"]["worldlage"])
            memory.observe(previous_lage=previous_lage, current_lage=current_lage, base=current["base"], adapted=current["adapted"])
            details.append(
                {
                    "world": label,
                    "block_index": current["base"]["block_index"],
                    "base_sequence": f"{previous_lage}->{current_lage}",
                    "adapted_lage": current["adapted"]["worldlage"],
                    "base_zentrum": current["base"]["zentrum_ratio"],
                    "base_rand": current["base"]["rand_ratio"],
                    "base_rekopplung": current["base"]["avg_rekopplung"],
                    "base_strain": current["base"]["avg_strain"],
                    "adapted_zentrum": current["adapted"]["zentrum_ratio"],
                    "adapted_rand": current["adapted"]["rand_ratio"],
                    "adapted_rekopplung": current["adapted"]["avg_rekopplung"],
                    "adapted_strain": current["adapted"]["avg_strain"],
                }
            )
    rows = memory.rows()
    _write_csv(rows, Path(args.csv_out))
    _write_csv(details, Path(args.detail_out))
    _write_markdown(rows, details, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.detail_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
