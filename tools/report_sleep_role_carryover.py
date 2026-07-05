"""Report how phasic sleep roles carry into real memory contexts.

Passive diagnostic only. The tool reads sleep-environment tick CSVs and memory
JSON files, then classifies whether sleep-active MCM episode roles are source
only, reappear in follow memories, or carry rekoppling quality there.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _load_json(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _load_ticks(path: Path) -> list[dict]:
    with Path(path).open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(value: object) -> float:
    try:
        value = float(value or 0.0)
    except Exception:
        value = 0.0
    if value != value:
        return 0.0
    return value


def _episode_index(memory_data: dict) -> dict[str, dict]:
    episodes = dict(memory_data.get("mcm_field_episode_memory", {}) or {})
    return {
        str(item.get("mcm_field_episode_symbol", key) or key): dict(item)
        for key, item in episodes.items()
        if isinstance(item, dict)
    }


def _quality(item: dict) -> str:
    carry = _float(item.get("avg_mcm_carry_quality"))
    strain = _float(item.get("avg_mcm_strain_quality"))
    rekopplung = _float(item.get("avg_mcm_rekopplung_quality"))
    if rekopplung >= 0.58 and strain <= 0.42:
        return "rekopplung_tragend"
    if carry >= 0.52 and strain <= 0.50:
        return "tragend_offen"
    if strain >= 0.58:
        return "belastet"
    return "offen_ungeklart"


def _sleep_role_activity(ticks: list[dict]) -> dict[str, dict]:
    seen: Counter[str] = Counter()
    resonance_sum: defaultdict[str, float] = defaultdict(float)
    for row in ticks:
        roles = [item for item in str(row.get("active_roles", "") or "").split("|") if item]
        resonance = [
            _float(item)
            for item in str(row.get("active_role_resonance", "") or "").split("|")
            if item != ""
        ]
        for index, role in enumerate(roles):
            seen[role] += 1
            resonance_sum[role] += resonance[index] if index < len(resonance) else 0.0
    result: dict[str, dict] = {}
    total_ticks = max(1, len(ticks))
    for role, count in seen.items():
        result[role] = {
            "sleep_ticks": count,
            "sleep_presence_ratio": count / total_ticks,
            "avg_sleep_resonance": resonance_sum[role] / max(1, count),
        }
    return result


def analyze_role_carryover(sleep_dir: Path, source_memory: Path, follow_memories: list[Path]) -> tuple[dict, list[dict]]:
    sleep_dir = Path(sleep_dir)
    ticks = _load_ticks(sleep_dir / "sleep_field_environment_ticks.csv")
    sleep_summary = _load_json(sleep_dir / "sleep_field_environment_summary.json")
    activity = _sleep_role_activity(ticks)
    source_episodes = _episode_index(_load_json(source_memory))
    follow_indices = [(path, _episode_index(_load_json(path))) for path in follow_memories]
    rows: list[dict] = []
    state_counts: Counter[str] = Counter()
    for role, sleep_values in sorted(activity.items(), key=lambda item: item[1]["sleep_ticks"], reverse=True):
        source_item = source_episodes.get(role, {})
        follow_hits = []
        quality_counts: Counter[str] = Counter()
        carry_values: list[float] = []
        strain_values: list[float] = []
        rekopplung_values: list[float] = []
        for path, episodes in follow_indices:
            if role not in episodes:
                continue
            item = episodes[role]
            follow_hits.append(path.name)
            quality = _quality(item)
            quality_counts[quality] += 1
            carry_values.append(_float(item.get("avg_mcm_carry_quality")))
            strain_values.append(_float(item.get("avg_mcm_strain_quality")))
            rekopplung_values.append(_float(item.get("avg_mcm_rekopplung_quality")))
        if follow_hits and quality_counts.get("rekopplung_tragend", 0) >= max(1, len(follow_hits) // 2):
            carryover_state = "cross_memory_rekopplung"
        elif follow_hits:
            carryover_state = "cross_memory_present"
        elif role in source_episodes:
            carryover_state = "source_only"
        else:
            carryover_state = "sleep_only"
        state_counts[carryover_state] += 1
        rows.append(
            {
                "role": role,
                "carryover_state": carryover_state,
                "sleep_ticks": sleep_values["sleep_ticks"],
                "sleep_presence_ratio": f"{sleep_values['sleep_presence_ratio']:.6f}",
                "avg_sleep_resonance": f"{sleep_values['avg_sleep_resonance']:.6f}",
                "source_quality": _quality(source_item) if source_item else "-",
                "source_carry": f"{_float(source_item.get('avg_mcm_carry_quality')):.6f}" if source_item else "0.000000",
                "source_strain": f"{_float(source_item.get('avg_mcm_strain_quality')):.6f}" if source_item else "0.000000",
                "source_rekopplung": f"{_float(source_item.get('avg_mcm_rekopplung_quality')):.6f}" if source_item else "0.000000",
                "follow_hit_count": len(follow_hits),
                "follow_quality_counts": json.dumps(dict(quality_counts), ensure_ascii=False, sort_keys=True),
                "avg_follow_carry": f"{(sum(carry_values) / max(1, len(carry_values))):.6f}",
                "avg_follow_strain": f"{(sum(strain_values) / max(1, len(strain_values))):.6f}",
                "avg_follow_rekopplung": f"{(sum(rekopplung_values) / max(1, len(rekopplung_values))):.6f}",
                "follow_memories": "|".join(follow_hits[:8]),
            }
        )
    summary = {
        "sleep_dir": str(sleep_dir),
        "source_memory": str(source_memory),
        "follow_memory_count": len(follow_memories),
        "sleep_top_symbol": sleep_summary.get("sleep_top_symbol", "-"),
        "sleep_active_role_count": len(activity),
        "carryover_state_counts": dict(state_counts),
        "top_roles": [row["role"] for row in rows[:8]],
    }
    return summary, rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Report sleep-role carryover into follow memories.")
    parser.add_argument("--sleep-dir", required=True)
    parser.add_argument("--source-memory-json", required=True)
    parser.add_argument("--follow-memory-json", action="append", required=True)
    parser.add_argument("--out-dir", default="debug/sleep_role_carryover")
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
    summary, rows = analyze_role_carryover(sleep_dir, source_memory, follow_memories)
    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "sleep_role_carryover_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    if rows:
        with (out_dir / "sleep_role_carryover.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
