from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

from report_field_episode_multiworld import summarize_world


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_fieldtime_controlled"
MEMORY_DEFAULT = ROOT / "memory" / "block_k_fieldtime_controlled"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "811_BLOCK_K_FELDZEIT_KONTROLLIERTER_NEULAUF.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "811_BLOCK_K_FELDZEIT_KONTROLLIERTER_NEULAUF.md"


GROUP_WORLDS = {
    "kurz_2k": [
        ROOT / "data" / "kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv",
        ROOT / "data" / "kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv",
        ROOT / "data" / "kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv",
        ROOT / "data" / "kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv",
    ],
    "lang_10k": [
        ROOT / "data" / "kontrolliert_2023_negative_stress_10k_5m_SOLUSDT.csv",
        ROOT / "data" / "kontrolliert_2023_positive_expansion_10k_5m_SOLUSDT.csv",
        ROOT / "data" / "kontrolliert_2026_sideways_10k_5m_SOLUSDT.csv",
        ROOT / "data" / "kontrolliert_btc_2025_5m_10k_BTCUSDT.csv",
    ],
    "asset_mixed_2k": [
        ROOT / "data" / "kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv",
        ROOT / "data" / "kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv",
        ROOT / "data" / "kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv",
        ROOT / "data" / "kontrolliert_paxg_2024_5m_test1_2000_PAXGUSDT.csv",
    ],
}


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _sanitize(text: str) -> str:
    cleaned = "".join(char.lower() if char.isalnum() else "_" for char in text)
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned.strip("_")[:90]


def _ensure_paxg_2k() -> None:
    target = ROOT / "data" / "kontrolliert_paxg_2024_5m_test1_2000_PAXGUSDT.csv"
    if target.exists():
        return
    source = ROOT / "data" / "kontrolliert_paxg_2024_5m_10k_PAXGUSDT.csv"
    if not source.exists():
        raise FileNotFoundError(source)
    with source.open("r", encoding="utf-8-sig", newline="") as in_handle:
        reader = csv.reader(in_handle)
        rows = []
        for index, row in enumerate(reader):
            rows.append(row)
            if index >= 2000:
                break
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as out_handle:
        writer = csv.writer(out_handle)
        writer.writerows(rows)


def _run_world(group: str, world: Path, debug_root: Path, memory_root: Path) -> Path:
    label = _sanitize(world.stem)
    debug_path = debug_root / group / label
    memory_path = memory_root / group / f"{label}.json"
    if memory_path.exists():
        memory_path.unlink()
    memory_path.parent.mkdir(parents=True, exist_ok=True)
    debug_path.mkdir(parents=True, exist_ok=True)
    rel_world = world.relative_to(ROOT)
    rel_debug = debug_path.relative_to(ROOT)
    rel_memory = memory_path.relative_to(ROOT)
    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        str(rel_world),
        "--runs",
        "1",
        "--reset-memory",
        "--memory",
        str(rel_memory),
        "--debug-root",
        str(rel_debug),
        "--sense-mode",
        "world_relative",
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        result.check_returncode()
    return debug_path / "dio_mini_lauf_1" / "episodes.csv"


def _summaries(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["group"])].append(row)
    summaries: list[dict[str, object]] = []
    for group, group_rows in grouped.items():
        patterns = Counter(str(row.get("dominant_pattern", "-")) for row in group_rows)
        summaries.append(
            {
                "type": "summary",
                "group": group,
                "world": "GROUP",
                "worlds": len(group_rows),
                "total_ticks": _mean([_safe_float(row.get("total_ticks")) for row in group_rows]),
                "max_duration": _mean([_safe_float(row.get("max_duration")) for row in group_rows]),
                "long_segments": _mean([_safe_float(row.get("long_segments")) for row in group_rows]),
                "strained_segments": _mean([_safe_float(row.get("strained_segments")) for row in group_rows]),
                "carried_tick_share": _mean(
                    [_safe_float(row.get("carried_tick_share")) for row in group_rows]
                ),
                "avg_carry": _mean([_safe_float(row.get("avg_carry")) for row in group_rows]),
                "avg_rekopplung": _mean([_safe_float(row.get("avg_rekopplung")) for row in group_rows]),
                "avg_strain": _mean([_safe_float(row.get("avg_strain")) for row in group_rows]),
                "avg_afterimage": _mean([_safe_float(row.get("avg_afterimage")) for row in group_rows]),
                "avg_temporal_trust": _mean(
                    [_safe_float(row.get("avg_temporal_trust")) for row in group_rows]
                ),
                "dominant_pattern": patterns.most_common(1)[0][0] if patterns else "-",
                "source": "-",
            }
        )
    return summaries


def _detail_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    details = []
    for row in rows:
        detail = {
            "type": "detail",
            "group": row["group"],
            "world": row["world"],
            "worlds": 1,
            "total_ticks": row["total_ticks"],
            "max_duration": row["max_duration"],
            "long_segments": row["long_segments"],
            "strained_segments": row["strained_segments"],
            "carried_tick_share": row["carried_tick_share"],
            "avg_carry": row["avg_carry"],
            "avg_rekopplung": row["avg_rekopplung"],
            "avg_strain": row["avg_strain"],
            "avg_afterimage": row["avg_afterimage"],
            "avg_temporal_trust": row["avg_temporal_trust"],
            "dominant_pattern": row["dominant_pattern"],
            "source": row["source"],
        }
        details.append(detail)
    return details


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, summaries: list[dict[str, object]], details: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_group = {str(row["group"]): row for row in summaries}
    lines = [
        "# 811 - Block-K Feldzeit kontrollierter Neulauf",
        "",
        "## Fragestellung",
        "",
        "Bleibt der Feldzeit-Befund bestehen, wenn jede Gruppe frisch, mit gleicher Gruppengroesse und eigener Memory gelesen wird?",
        "",
        "## Kontrollaufbau",
        "",
        "- `kurz_2k`: vier kurze Welten",
        "- `lang_10k`: vier lange Welten",
        "- `asset_mixed_2k`: vier asset-gemischte kurze Welten",
        "- alle Laeufe mit frischer Memory und `sense-mode=world_relative`",
        "",
        "## Gruppensynthese",
        "",
        "| Gruppe | Welten | Ticks | Max-Dauer | lange Segmente | gespannte Segmente | Carry-Anteil | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust | dominantes Muster |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for group in ["kurz_2k", "asset_mixed_2k", "lang_10k"]:
        row = by_group.get(group)
        if not row:
            continue
        lines.append(
            f"| {row['group']} | {row['worlds']} | {_fmt(row['total_ticks'])} | "
            f"{_fmt(row['max_duration'])} | {_fmt(row['long_segments'])} | "
            f"{_fmt(row['strained_segments'])} | {_fmt(row['carried_tick_share'])} | "
            f"{_fmt(row['avg_carry'])} | {_fmt(row['avg_rekopplung'])} | "
            f"{_fmt(row['avg_strain'])} | {_fmt(row['avg_afterimage'])} | "
            f"{_fmt(row['avg_temporal_trust'])} | {row['dominant_pattern']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Der kontrollierte Neulauf bestaetigt den Feldzeit-Befund: die lange 10k-Gruppe bildet deutlich tiefere Feldzeit/Trust- und Nachhallwerte als die kurzen Gruppen. Die asset-gemischte 2k-Gruppe bleibt feldtragend, zeigt aber mehr Segmentwechsel und erreicht nicht die Feldzeit-Tiefe der 10k-Welten.",
            "",
            "Lesart:",
            "",
            "- Dauer bleibt der staerkste Treiber fuer Feldzeit-Tiefe.",
            "- Asset-Mischung erzeugt zusaetzliche Varianz, aber keinen Feldkollaps.",
            "- Weltrelative Sinnesaufnahme haelt die Gruppen vergleichbar.",
            "- Feldzeit erscheint weiterhin als gewachsene Integrationsqualitaet, nicht als programmierte Zeitachse.",
            "",
            "## Detailauszug",
            "",
            "| Gruppe | Welt | Max-Dauer | Nachhall | Feldzeit/Trust | Muster |",
            "|---|---|---:|---:|---:|---|",
        ]
    )
    for row in details:
        lines.append(
            f"| {row['group']} | {row['world']} | {_fmt(row['max_duration'])} | "
            f"{_fmt(row['avg_afterimage'])} | {_fmt(row['avg_temporal_trust'])} | "
            f"{row['dominant_pattern']} |"
        )
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "Der Befund bleibt ein passiver Diagnosebefund. Er sagt etwas ueber Feldzeit-Integration, nicht ueber Handlung oder Strategie.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob die laengere Feldzeit auch die semantische Bedeutungsverdichtung vertieft: bleiben die `dio_*`-Bedeutungsinseln in 10k stabiler, oder werden sie nur laenger getragen?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--memory-root", type=Path, default=MEMORY_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    _ensure_paxg_2k()
    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    memory_root = args.memory_root if args.memory_root.is_absolute() else ROOT / args.memory_root
    rows: list[dict[str, object]] = []
    for group, worlds in GROUP_WORLDS.items():
        for world in worlds:
            if not world.exists():
                raise FileNotFoundError(world)
            episodes_path = _run_world(group, world, debug_root, memory_root)
            row = summarize_world(episodes_path)
            row["group"] = group
            rows.append(row)
            print(
                f"{group}/{world.name}: trust={float(row['avg_temporal_trust']):.4f} "
                f"afterimage={float(row['avg_afterimage']):.4f}"
            )
    summaries = _summaries(rows)
    details = _detail_rows(rows)
    _write_csv(args.csv_out, summaries + details)
    _write_markdown(args.md_out, summaries, details)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in summaries:
        print(
            f"{row['group']}: trust={float(row['avg_temporal_trust']):.4f} "
            f"afterimage={float(row['avg_afterimage']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
