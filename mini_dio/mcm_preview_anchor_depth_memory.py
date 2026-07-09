"""Passive depth memory for MCM preview anchors.

This layer keeps a read-only trace of preview symbols that reappear across
worlds. It is not action logic. It only preserves whether a preview anchor
starts gaining semantic depth through world breadth, profile proximity,
afterimage, recurrence and recoupling.
"""

from __future__ import annotations


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _clip(value: object, lo: float = 0.0, hi: float = 1.0) -> float:
    try:
        result = float(value)
    except Exception:
        return lo
    if result != result:
        return lo
    return max(lo, min(hi, result))


def _avg(previous: float, count: int, value: float) -> float:
    count = max(0, int(count or 0))
    return _clip(((previous * count) + value) / (count + 1))


def _trim_mapping(mapping: dict, max_items: int) -> dict:
    if len(mapping) <= max_items:
        return mapping
    ranked = sorted(
        mapping.items(),
        key=lambda item: (
            float(item[1].get("depth_score", 0.0) or 0.0),
            int(item[1].get("count", 0) or 0),
        ),
        reverse=True,
    )
    return dict(ranked[:max(1, int(max_items))])


def _depth_state(depth_score: float, world_count: int, profile: float, afterimage: float, recurrence: float) -> str:
    if world_count >= 3 and depth_score >= 0.50 and profile >= 0.28:
        return "multiworld_depth_seed"
    if world_count >= 2 and depth_score >= 0.42:
        return "recurring_depth_seed"
    if profile >= 0.24 and (afterimage >= 0.08 or recurrence >= 0.16):
        return "local_depth_seed"
    return "surface_anchor"


def store_passive_mcm_preview_anchor_depth(
    data: dict,
    payload: dict,
    *,
    max_items: int = 512,
) -> dict:
    """Store one passive preview-anchor depth observation and return the item."""

    symbol = str((payload or {}).get("preview_symbol", "") or "").strip()
    if not symbol or symbol == "-":
        return {}

    memory = data.setdefault("passive_mcm_preview_anchor_depth_memory", {})
    if not isinstance(memory, dict):
        memory = {}
    item = dict(memory.get(symbol, {}) or {})
    count = int(item.get("count", 0) or 0)

    world = str(payload.get("world", "") or "-")
    effect = str(payload.get("effect", "") or "-")
    family = str(payload.get("symbol_family", "") or "-")
    worlds = dict(item.get("worlds", {}) or {})
    effects = dict(item.get("effects", {}) or {})
    families = dict(item.get("families", {}) or {})
    worlds[world] = int(worlds.get(world, 0) or 0) + 1
    effects[effect] = int(effects.get(effect, 0) or 0) + 1
    families[family] = int(families.get(family, 0) or 0) + 1

    profile_proximity = _clip(payload.get("profile_proximity", 0.0))
    afterimage = _clip(payload.get("afterimage", 0.0))
    recurrence = _clip(payload.get("recurrence", 0.0))
    rekopplung = _clip(payload.get("rekopplung", 0.0))
    strain = _clip(payload.get("strain", 0.0))
    sensory_coupling = _clip(payload.get("sensory_coupling", 0.0))
    avg_profile = _avg(float(item.get("avg_profile_proximity", 0.0) or 0.0), count, profile_proximity)
    avg_afterimage = _avg(float(item.get("avg_afterimage", 0.0) or 0.0), count, afterimage)
    avg_recurrence = _avg(float(item.get("avg_recurrence", 0.0) or 0.0), count, recurrence)
    avg_rekopplung = _avg(float(item.get("avg_rekopplung", 0.0) or 0.0), count, rekopplung)
    avg_strain = _avg(float(item.get("avg_strain", 0.0) or 0.0), count, strain)
    avg_sensory = _avg(float(item.get("avg_sensory_coupling", 0.0) or 0.0), count, sensory_coupling)
    world_count = len([key for key in worlds if key and key != "-"])
    world_breadth = _clip(world_count / 4.0)
    depth_score = _clip(
        (world_breadth * 0.20)
        + (avg_profile * 0.24)
        + (avg_afterimage * 0.16)
        + (avg_recurrence * 0.18)
        + (avg_rekopplung * 0.14)
        + ((1.0 - avg_strain) * 0.05)
        + (avg_sensory * 0.03)
    )
    state = _depth_state(depth_score, world_count, avg_profile, avg_afterimage, avg_recurrence)

    item = {
        **PASSIVE_FLAGS,
        "preview_symbol": symbol,
        "count": count + 1,
        "world_count": world_count,
        "worlds": worlds,
        "effects": effects,
        "families": families,
        "last_world": world,
        "last_effect": effect,
        "last_family": family,
        "last_tick": int(payload.get("tick", 0) or 0),
        "avg_profile_proximity": round(avg_profile, 6),
        "avg_afterimage": round(avg_afterimage, 6),
        "avg_recurrence": round(avg_recurrence, 6),
        "avg_rekopplung": round(avg_rekopplung, 6),
        "avg_strain": round(avg_strain, 6),
        "avg_sensory_coupling": round(avg_sensory, 6),
        "depth_score": round(depth_score, 6),
        "depth_state": state,
    }
    memory[symbol] = item
    data["passive_mcm_preview_anchor_depth_memory"] = _trim_mapping(memory, max_items)
    return item


def top_preview_anchor_depth(data: dict, limit: int = 12) -> list[dict]:
    memory = dict((data or {}).get("passive_mcm_preview_anchor_depth_memory", {}) or {})
    items = [dict(item or {}) for item in memory.values()]
    items.sort(
        key=lambda item: (
            float(item.get("depth_score", 0.0) or 0.0),
            int(item.get("world_count", 0) or 0),
            int(item.get("count", 0) or 0),
        ),
        reverse=True,
    )
    return items[: max(1, int(limit))]


__all__ = [
    "store_passive_mcm_preview_anchor_depth",
    "top_preview_anchor_depth",
]
