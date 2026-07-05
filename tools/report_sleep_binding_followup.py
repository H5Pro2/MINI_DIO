"""Compare sleep-field activity with later real memory traces.

This is a passive diagnostic. It does not write runtime memory and does not
interpret sleep activity as truth. It only checks whether offline symbols or
episode roles reappear in selected real memory files.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _load_json(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _load_sleep_ticks(path: Path) -> list[dict]:
    with Path(path).open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _role_quality(item: dict) -> str:
    carry = float(item.get("avg_mcm_carry_quality", 0.0) or 0.0)
    strain = float(item.get("avg_mcm_strain_quality", 0.0) or 0.0)
    rekopplung = float(item.get("avg_mcm_rekopplung_quality", 0.0) or 0.0)
    if rekopplung >= 0.58 and strain <= 0.42:
        return "rekopplung_tragend"
    if carry >= 0.52 and strain <= 0.50:
        return "tragend_offen"
    if strain >= 0.58:
        return "belastet"
    return "offen_ungeklart"


def _episode_index(memory_data: dict) -> dict[str, dict]:
    episodes = dict(memory_data.get("mcm_field_episode_memory", {}) or {})
    return {
        str(item.get("mcm_field_episode_symbol", key) or key): dict(item)
        for key, item in episodes.items()
        if isinstance(item, dict)
    }


def _symbol_index(memory_data: dict) -> dict[str, dict]:
    symbols = dict(memory_data.get("symbols", {}) or {})
    return {str(key): dict(value) for key, value in symbols.items() if isinstance(value, dict)}


def analyze_sleep_followup(sleep_dir: Path, source_memory: Path, follow_memories: list[Path]) -> tuple[dict, list[dict]]:
    sleep_dir = Path(sleep_dir)
    summary_path = sleep_dir / "sleep_field_environment_summary.json"
    ticks_path = sleep_dir / "sleep_field_environment_ticks.csv"
    sleep_summary = _load_json(summary_path)
    sleep_ticks = _load_sleep_ticks(ticks_path)
    source_data = _load_json(source_memory)
    source_symbols = _symbol_index(source_data)
    source_episodes = _episode_index(source_data)

    sleep_symbols = Counter(str(row.get("sleep_symbol", "") or "") for row in sleep_ticks)
    active_role_counter: Counter[str] = Counter()
    for row in sleep_ticks:
        for role in str(row.get("active_roles", "") or "").split("|"):
            role = role.strip()
            if role:
                active_role_counter[role] += 1

    rows: list[dict] = []
    for follow_path in follow_memories:
        follow_data = _load_json(follow_path)
        follow_symbols = _symbol_index(follow_data)
        follow_episodes = _episode_index(follow_data)
        sleep_symbol_hits = {
            symbol: count
            for symbol, count in sleep_symbols.items()
            if symbol and symbol in follow_symbols
        }
        source_sleep_symbol_hits = {
            symbol: count
            for symbol, count in sleep_symbols.items()
            if symbol and symbol in source_symbols
        }
        role_hits = {
            role: count
            for role, count in active_role_counter.items()
            if role in follow_episodes
        }
        role_quality_counts = Counter()
        for role in role_hits:
            role_quality_counts[_role_quality(follow_episodes.get(role, {}))] += 1
        source_role_hits = {
            role: count
            for role, count in active_role_counter.items()
            if role in source_episodes
        }
        if sleep_symbol_hits:
            follow_state = "offline_symbol_reappears"
        elif role_hits:
            follow_state = "old_episode_roles_reappear"
        elif source_role_hits:
            follow_state = "source_roles_only"
        else:
            follow_state = "no_direct_reappearance"
        rows.append(
            {
                "follow_memory": str(follow_path),
                "follow_state": follow_state,
                "sleep_unique_symbols": len(sleep_symbols),
                "sleep_top_symbol": sleep_summary.get("sleep_top_symbol", "-"),
                "sleep_symbol_hits": len(sleep_symbol_hits),
                "sleep_symbol_hit_names": "|".join(sorted(sleep_symbol_hits)[:8]),
                "source_sleep_symbol_hits": len(source_sleep_symbol_hits),
                "active_role_count": len(active_role_counter),
                "follow_episode_role_hits": len(role_hits),
                "source_episode_role_hits": len(source_role_hits),
                "role_hit_names": "|".join(sorted(role_hits)[:8]),
                "role_quality_counts": json.dumps(dict(role_quality_counts), ensure_ascii=False, sort_keys=True),
            }
        )
    combined = {
        "sleep_dir": str(sleep_dir),
        "source_memory": str(source_memory),
        "follow_memory_count": len(follow_memories),
        "sleep_top_symbol": sleep_summary.get("sleep_top_symbol", "-"),
        "sleep_unique_symbols": len(sleep_symbols),
        "active_role_count": len(active_role_counter),
        "result_counts": dict(Counter(row["follow_state"] for row in rows)),
    }
    return combined, rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare sleep-field activity with later real memory traces.")
    parser.add_argument("--sleep-dir", required=True)
    parser.add_argument("--source-memory-json", required=True)
    parser.add_argument("--follow-memory-json", action="append", required=True)
    parser.add_argument("--out-dir", default="debug/sleep_binding_followup")
    args = parser.parse_args()

    root = Path.cwd()
    sleep_dir = Path(args.sleep_dir)
    if not sleep_dir.is_absolute():
        sleep_dir = root / sleep_dir
    source_memory = Path(args.source_memory_json)
    if not source_memory.is_absolute():
        source_memory = root / source_memory
    follow_memories = []
    for item in args.follow_memory_json:
        path = Path(item)
        if not path.is_absolute():
            path = root / path
        follow_memories.append(path)

    summary, rows = analyze_sleep_followup(sleep_dir, source_memory, follow_memories)
    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "sleep_binding_followup_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    if rows:
        with (out_dir / "sleep_binding_followup.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
