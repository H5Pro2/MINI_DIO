"""Passive episode persistence helpers for MINI_DIO.

The functions in this module keep concrete episode traces and coarse MCM-field
episode traces. They do not choose actions and they do not read strategy state.
"""

from __future__ import annotations

from mini_dio.dio_syntax import make_episode_memory_symbol


def episode_memory_rank(item: dict) -> tuple:
    return (
        float(item.get("avg_mcm_rekopplung_quality", 0.0) or 0.0),
        float(item.get("avg_mcm_carry_quality", 0.0) or 0.0),
        int(item.get("seen_count", 0) or 0),
        -float(item.get("avg_mcm_strain_quality", 0.0) or 0.0),
        int(item.get("duration", 0) or 0),
    )


def _avg(current: dict, payload: dict, key: str, seen_count: int) -> float:
    previous = float(current.get(key, 0.0) or 0.0)
    value = float(payload.get(key, 0.0) or 0.0)
    if seen_count <= 1:
        return value
    return ((previous * (seen_count - 1)) + value) / seen_count


def compact_episode_memory(data: dict, max_items: int) -> dict:
    limit = max(1, int(max_items))
    episodes = data.setdefault("episode_memory", {})
    if not isinstance(episodes, dict):
        data["episode_memory"] = {}
        return {"before": 0, "after": 0, "removed": 0}
    before = len(episodes)
    if before <= limit:
        return {"before": before, "after": before, "removed": 0}
    sorted_items = sorted(
        episodes.items(),
        key=lambda item: episode_memory_rank(dict(item[1] or {})),
        reverse=True,
    )
    kept = dict(sorted_items[:limit])
    data["episode_memory"] = kept
    after = len(kept)
    return {"before": before, "after": after, "removed": before - after}


def store_episode_memory(data: dict, payload: dict, max_items: int) -> str:
    """Store a passive episode-memory trace."""

    if not isinstance(payload, dict):
        return ""
    episode_symbol = make_episode_memory_symbol(payload)
    episodes = data.setdefault("episode_memory", {})
    current = dict(episodes.get(episode_symbol, {}) or {})
    seen_count = int(current.get("seen_count", 0) or 0) + 1
    duration = int(payload.get("duration", current.get("duration", 0)) or 0)
    current.update(
        {
            "episode_symbol": episode_symbol,
            "episode_state": str(payload.get("episode_state", "") or ""),
            "previous_state": str(payload.get("previous_state", "") or ""),
            "next_state": str(payload.get("next_state", "") or ""),
            "transition": str(payload.get("transition", "") or ""),
            "dominant_family": str(payload.get("dominant_family", "") or ""),
            "family_count": int(payload.get("family_count", current.get("family_count", 0)) or 0),
            "seen_count": seen_count,
            "duration": duration,
            "last_start_tick": int(payload.get("start_tick", 0) or 0),
            "last_end_tick": int(payload.get("end_tick", 0) or 0),
            "avg_mcm_carry_quality": _avg(current, payload, "avg_mcm_carry_quality", seen_count),
            "avg_mcm_strain_quality": _avg(current, payload, "avg_mcm_strain_quality", seen_count),
            "avg_mcm_rekopplung_quality": _avg(current, payload, "avg_mcm_rekopplung_quality", seen_count),
            "avg_sensory_coupling": _avg(current, payload, "avg_sensory_coupling", seen_count),
            "avg_visual_field_gap": _avg(current, payload, "avg_visual_field_gap", seen_count),
            "avg_hearing_field_gap": _avg(current, payload, "avg_hearing_field_gap", seen_count),
            "passive_only": 1,
            "writes_runtime_memory": 0,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
        }
    )
    episodes[episode_symbol] = current
    compact_episode_memory(data, max_items)
    return episode_symbol


def top_episode_memory(data: dict, limit: int = 8) -> list[dict]:
    episodes = list(dict(data.get("episode_memory", {}) or {}).values())
    episodes.sort(key=episode_memory_rank, reverse=True)
    return episodes[: max(1, int(limit))]


__all__ = [
    "compact_episode_memory",
    "episode_memory_rank",
    "store_episode_memory",
    "top_episode_memory",
]
