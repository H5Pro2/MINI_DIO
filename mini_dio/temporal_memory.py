"""Passive temporal perception for Mini-DIO.

The layer tracks family recurrence, distance and afterimage. It is deliberately
passive: it does not choose actions and it does not change action scores.
"""

from __future__ import annotations


def _clip(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    try:
        value = float(value)
    except Exception:
        value = 0.0
    if value != value:
        value = 0.0
    return max(lo, min(hi, value))


def _signed_clip(value: float) -> float:
    return max(-1.0, min(1.0, float(value or 0.0)))


def _vector_distance(left: list[float], right: list[float]) -> float:
    if not left or not right:
        return 1.0
    size = min(len(left), len(right))
    if size <= 0:
        return 1.0
    return _clip(sum(abs(_signed_clip(left[i]) - _signed_clip(right[i])) for i in range(size)) / size)


def _pressure(value: float, scale: float = 1.0) -> float:
    amount = max(0.0, float(value or 0.0))
    return amount / (amount + max(0.000001, scale))


def _mean(*values: float) -> float:
    clean = [_clip(float(value or 0.0)) for value in values]
    return sum(clean) / max(1, len(clean))


def _dominant_label(scores: dict[str, float], default: str) -> str:
    clean = {key: _clip(value) for key, value in scores.items()}
    if not clean:
        return default
    return max(clean, key=clean.get)


class MiniTemporalTracker:
    """In-run temporal trace for DIO-owned symbol families."""

    def __init__(self, *, afterimage_decay: float = 0.86):
        self.afterimage_decay = _clip(afterimage_decay, 0.0, 0.99)
        self.families: dict[str, dict] = {}

    def step(self, family: str, tick: int, vector: list[float]) -> dict:
        family = str(family or "-") or "-"
        tick = int(tick)
        previous = dict(self.families.get(family, {}) or {})
        seen_before = int(previous.get("seen_count", 0) or 0)
        first_seen_tick = int(previous.get("first_seen_tick", tick) or tick)
        previous_seen_tick = int(previous.get("last_seen_tick", tick) or tick)
        ticks_since_seen = tick - previous_seen_tick if seen_before > 0 else -1
        family_age = max(0, tick - first_seen_tick)
        previous_vector = list(previous.get("vector", []) or [])
        form_distance = _vector_distance(vector, previous_vector) if seen_before > 0 else 1.0
        elapsed_ticks = max(0, ticks_since_seen)
        temporal_distance = _pressure(elapsed_ticks, 12.0) if seen_before > 0 else 1.0
        recurrence_strength = _clip(seen_before / (seen_before + 5.0)) if seen_before > 0 else 0.0
        first_pressure = 1.0 if seen_before <= 0 else 0.0
        immediate_pressure = _pressure(1.0, 1.0 + elapsed_ticks) if seen_before > 0 else 0.0
        near_pressure = _mean(_pressure(8.0, 1.0 + elapsed_ticks), recurrence_strength) if seen_before > 0 else 0.0
        far_pressure = _mean(temporal_distance, recurrence_strength, 1.0 - immediate_pressure) if seen_before > 0 else 0.0
        contact_state = _dominant_label(
            {
                "temporal_first_contact": first_pressure,
                "temporal_immediate_afterimage": immediate_pressure,
                "temporal_near_return": near_pressure,
                "temporal_far_return": far_pressure,
            },
            default="temporal_first_contact",
        )
        contact_pressure = _clip(
            {
                "temporal_first_contact": 0.0,
                "temporal_immediate_afterimage": immediate_pressure,
                "temporal_near_return": near_pressure,
                "temporal_far_return": far_pressure,
            }.get(contact_state, 0.0)
        )
        previous_afterimage = float(previous.get("afterimage", 0.0) or 0.0)
        afterimage = _clip((previous_afterimage * self.afterimage_decay) + (contact_pressure * (1.0 - self.afterimage_decay)))
        temporal_fit = _clip((1.0 - form_distance) * 0.58 + afterimage * 0.24 + recurrence_strength * 0.18)
        temporal_caution = _clip(form_distance * 0.42 + temporal_distance * 0.18 + max(0.0, 0.30 - temporal_fit) * 0.40)

        self.families[family] = {
            "family": family,
            "first_seen_tick": first_seen_tick,
            "last_seen_tick": tick,
            "seen_count": seen_before + 1,
            "family_age": family_age,
            "ticks_since_seen": ticks_since_seen,
            "afterimage": afterimage,
            "vector": list(vector or []),
        }
        return {
            "mini_temporal_identity": family,
            "mini_temporal_state": contact_state,
            "mini_family_age": family_age,
            "mini_ticks_since_family_seen": ticks_since_seen,
            "mini_recurrence_strength": recurrence_strength,
            "mini_afterimage": afterimage,
            "mini_time_distance": temporal_distance,
            "mini_temporal_form_distance": form_distance,
            "mini_temporal_trust_support": temporal_fit,
            "mini_temporal_caution_support": temporal_caution,
            "passive_only": 1,
        }


__all__ = ["MiniTemporalTracker"]
