"""Report real MCM episode roles that sleep does not activate.

Passive diagnostic only. This checks whether sleep-role activation is selective
by comparing real source roles with sleep-active roles.
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


def _role_score(item: dict) -> float:
    carry = _float(item.get("avg_mcm_carry_quality"))
    strain = _float(item.get("avg_mcm_strain_quality"))
    rekopplung = _float(item.get("avg_mcm_rekopplung_quality"))
    coupling = _float(item.get("avg_sensory_coupling"))
    seen = _float(item.get("seen_count"))
    duration = _float(item.get("duration"))
    return (
        rekopplung * 0.34
        + carry * 0.24
        + coupling * 0.16
        + min(duration, 240.0) / 240.0 * 0.16
        + min(seen, 8.0) / 8.0 * 0.10
        - strain * 0.18
    )


def _sleep_activity(ticks: list[dict]) -> Counter[str]:
    active: Counter[str] = Counter()
    for row in ticks:
        for role in str(row.get("active_roles", "") or "").split("|"):
            role = role.strip()
            if role:
                active[role] += 1
    return active


def analyze_selection_gap(sleep_dir: Path, source_memory: Path) -> tuple[dict, list[dict]]:
    sleep_dir = Path(sleep_dir)
    ticks = _load_ticks(sleep_dir / "sleep_field_environment_ticks.csv")
    sleep_summary = _load_json(sleep_dir / "sleep_field_environment_summary.json")
    active = _sleep_activity(ticks)
    episodes = _episode_index(_load_json(source_memory))
    rows: list[dict] = []
    state_counts: Counter[str] = Counter()
    quality_counts: Counter[str] = Counter()
    inactive_quality_counts: Counter[str] = Counter()
    active_quality_counts: Counter[str] = Counter()
    total_ticks = max(1, len(ticks))
    for role, item in sorted(episodes.items(), key=lambda pair: _role_score(pair[1]), reverse=True):
        quality = _quality(item)
        is_active = role in active
        if is_active:
            selection_state = "sleep_activated"
            active_quality_counts[quality] += 1
        else:
            selection_state = "real_role_not_sleep_active"
            inactive_quality_counts[quality] += 1
        state_counts[selection_state] += 1
        quality_counts[quality] += 1
        rows.append(
            {
                "role": role,
                "selection_state": selection_state,
                "source_quality": quality,
                "source_score": f"{_role_score(item):.6f}",
                "sleep_ticks": active.get(role, 0),
                "sleep_presence_ratio": f"{active.get(role, 0) / total_ticks:.6f}",
                "source_carry": f"{_float(item.get('avg_mcm_carry_quality')):.6f}",
                "source_strain": f"{_float(item.get('avg_mcm_strain_quality')):.6f}",
                "source_rekopplung": f"{_float(item.get('avg_mcm_rekopplung_quality')):.6f}",
                "source_seen_count": int(_float(item.get("seen_count"))),
                "source_duration": int(_float(item.get("duration"))),
            }
        )
    summary = {
        "sleep_dir": str(sleep_dir),
        "source_memory": str(source_memory),
        "sleep_top_symbol": sleep_summary.get("sleep_top_symbol", "-"),
        "source_role_count": len(episodes),
        "sleep_active_role_count": len(active),
        "state_counts": dict(state_counts),
        "quality_counts": dict(quality_counts),
        "active_quality_counts": dict(active_quality_counts),
        "inactive_quality_counts": dict(inactive_quality_counts),
    }
    return summary, rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Report real roles not selected by sleep.")
    parser.add_argument("--sleep-dir", required=True)
    parser.add_argument("--source-memory-json", required=True)
    parser.add_argument("--out-dir", default="debug/sleep_role_selection_gap")
    args = parser.parse_args()

    root = Path.cwd()
    sleep_dir = Path(args.sleep_dir)
    if not sleep_dir.is_absolute():
        sleep_dir = root / sleep_dir
    source_memory = Path(args.source_memory_json)
    if not source_memory.is_absolute():
        source_memory = root / source_memory
    summary, rows = analyze_selection_gap(sleep_dir, source_memory)
    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "sleep_role_selection_gap_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    if rows:
        with (out_dir / "sleep_role_selection_gap.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
