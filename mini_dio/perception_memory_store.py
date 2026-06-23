"""Passive perception-memory helpers for MINI_DIO.

This module stores temporal family traces: recurrence, afterimage, distance and
passive trust/caution support. It is perception/priming memory, not semantic
meaning and not action logic.
"""

from __future__ import annotations


def temporal_family_rank(item: dict) -> tuple:
    return (
        float(item.get("max_temporal_trust_support", 0.0) or 0.0),
        float(item.get("max_afterimage", 0.0) or 0.0),
        int(item.get("seen_count", 0) or 0),
        -float(item.get("max_temporal_caution_support", 0.0) or 0.0),
    )


def compact_temporal_families(data: dict, max_items: int) -> dict:
    """Keep passive temporal family traces compact."""

    limit = max(1, int(max_items))
    families = data.setdefault("temporal_families", {})
    if not isinstance(families, dict):
        data["temporal_families"] = {}
        return {"before": 0, "after": 0, "removed": 0}
    before = len(families)
    if before <= limit:
        return {"before": before, "after": before, "removed": 0}
    sorted_items = sorted(families.items(), key=lambda item: temporal_family_rank(dict(item[1] or {})), reverse=True)
    kept = dict(sorted_items[:limit])
    data["temporal_families"] = kept
    after = len(kept)
    return {"before": before, "after": after, "removed": before - after}


def store_temporal_family(data: dict, family: str, temporal_state: dict, max_items: int) -> None:
    """Store passive time-depth for a DIO-owned family."""

    family = str(family or "").strip()
    if not family:
        return
    traces = data.setdefault("temporal_families", {})
    current = dict(traces.get(family, {}) or {})
    seen_count = int(current.get("seen_count", 0) or 0) + 1
    trust_support = float(temporal_state.get("mini_temporal_trust_support", 0.0) or 0.0)
    caution_support = float(temporal_state.get("mini_temporal_caution_support", 0.0) or 0.0)
    afterimage = float(temporal_state.get("mini_afterimage", 0.0) or 0.0)
    current.update(
        {
            "family": family,
            "passive_only": 1,
            "seen_count": seen_count,
            "last_temporal_state": str(temporal_state.get("mini_temporal_state", "") or ""),
            "last_family_age": int(temporal_state.get("mini_family_age", 0) or 0),
            "last_ticks_since_seen": int(temporal_state.get("mini_ticks_since_family_seen", -1) or -1),
            "last_recurrence_strength": float(temporal_state.get("mini_recurrence_strength", 0.0) or 0.0),
            "last_afterimage": afterimage,
            "last_time_distance": float(temporal_state.get("mini_time_distance", 0.0) or 0.0),
            "last_temporal_form_distance": float(temporal_state.get("mini_temporal_form_distance", 0.0) or 0.0),
            "last_temporal_trust_support": trust_support,
            "last_temporal_caution_support": caution_support,
            "max_afterimage": max(float(current.get("max_afterimage", 0.0) or 0.0), afterimage),
            "max_temporal_trust_support": max(
                float(current.get("max_temporal_trust_support", 0.0) or 0.0),
                trust_support,
            ),
            "max_temporal_caution_support": max(
                float(current.get("max_temporal_caution_support", 0.0) or 0.0),
                caution_support,
            ),
        }
    )
    traces[family] = current
    compact_temporal_families(data, max_items)


__all__ = [
    "compact_temporal_families",
    "store_temporal_family",
    "temporal_family_rank",
]
