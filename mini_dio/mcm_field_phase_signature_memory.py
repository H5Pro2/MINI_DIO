"""Passive memory for recurring MCM field-phase qualities.

This layer stores how a preview anchor carries a field-quality vector across
world contact. It is not action logic. It preserves whether a field phase stays
similar, drifts, changes carrier role, or binds to real/null/synthetic worlds.
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

VECTOR_KEYS = (
    "carry",
    "strain",
    "rekopplung",
    "sensory",
    "visual_gap",
    "hearing_gap",
    "coherence",
    "tension",
    "asymmetry",
)


def _clip(value: object, lo: float = 0.0, hi: float = 1.0) -> float:
    try:
        result = float(value)
    except Exception:
        return lo
    if result != result:
        return lo
    return max(lo, min(hi, result))


def _signed_clip(value: object) -> float:
    try:
        result = float(value)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return max(-1.0, min(1.0, result))


def _avg(previous: float, count: int, value: float, *, lo: float = 0.0, hi: float = 1.0) -> float:
    count = max(0, int(count or 0))
    result = ((previous * count) + value) / (count + 1)
    return max(lo, min(hi, result))


def _pressure(value: object, scale: float = 1.0) -> float:
    amount = max(0.0, float(value or 0.0))
    return amount / (amount + max(0.000001, scale))


def _vector_from_payload(payload: dict) -> dict[str, float]:
    return {
        "carry": _clip(payload.get("carry", 0.0)),
        "strain": _clip(payload.get("strain", 0.0)),
        "rekopplung": _clip(payload.get("rekopplung", 0.0)),
        "sensory": _clip(payload.get("sensory_coupling", 0.0)),
        "visual_gap": _clip(payload.get("visual_gap", 0.0)),
        "hearing_gap": _clip(payload.get("hearing_gap", 0.0)),
        "coherence": _clip(payload.get("coherence", 0.0)),
        "tension": _clip(payload.get("tension", 0.0)),
        "asymmetry": _signed_clip(payload.get("asymmetry", 0.0)),
    }


def _vector_distance(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    distances = []
    for key in VECTOR_KEYS:
        distances.append(abs(float(a.get(key, 0.0) or 0.0) - float(b.get(key, 0.0) or 0.0)))
    return _clip(sum(distances) / max(1, len(distances)))


def _counter_add(counter: dict, key: object) -> dict:
    clean = str(key or "-").strip() or "-"
    counter[clean] = int(counter.get(clean, 0) or 0) + 1
    return counter


def _dominant(counter: dict) -> str:
    if not counter:
        return "-"
    return max(counter, key=lambda key: int(counter.get(key, 0) or 0))


def _trim_mapping(mapping: dict, max_items: int) -> dict:
    if len(mapping) <= max_items:
        return mapping
    ranked = sorted(
        mapping.items(),
        key=lambda item: (
            float(item[1].get("phase_quality_depth", 0.0) or 0.0),
            int(item[1].get("count", 0) or 0),
            int(item[1].get("world_count", 0) or 0),
        ),
        reverse=True,
    )
    return dict(ranked[: max(1, int(max_items))])


def _phase_quality_state(*, count: int, world_count: int, avg_drift: float, positive_score: float) -> str:
    recurrence = _pressure(count, 8.0)
    breadth = _pressure(world_count, 3.0)
    stability = _clip(1.0 - avg_drift)
    scores = {
        "young_field_phase": _clip(1.0 - recurrence),
        "stable_crossworld_field_phase": _clip((recurrence * 0.34) + (breadth * 0.34) + (stability * 0.32)),
        "drifting_field_phase": _clip((recurrence * 0.34) + (breadth * 0.18) + (avg_drift * 0.48)),
        "positive_recoupling_field_phase": _clip((positive_score * 0.52) + (recurrence * 0.24) + (stability * 0.24)),
    }
    return max(scores, key=scores.get)


def _positive_phase_score(vector: dict[str, float]) -> float:
    """Read affinity to a calm recoupling phase without turning it into a rule."""

    return _clip(
        (vector["rekopplung"] * 0.24)
        + (vector["carry"] * 0.16)
        + (vector["sensory"] * 0.16)
        + ((1.0 - vector["strain"]) * 0.16)
        + ((1.0 - vector["tension"]) * 0.12)
        + ((1.0 - vector["hearing_gap"]) * 0.08)
        + (vector["coherence"] * 0.08)
    )


def store_passive_mcm_field_phase_signature(
    data: dict,
    payload: dict,
    *,
    max_items: int = 512,
) -> dict:
    """Store one passive field-phase signature observation."""

    symbol = str((payload or {}).get("preview_symbol", "") or "").strip()
    if not symbol or symbol == "-":
        return {}

    memory = data.setdefault("passive_mcm_field_phase_signature_memory", {})
    if not isinstance(memory, dict):
        memory = {}
    item = dict(memory.get(symbol, {}) or {})
    count = int(item.get("count", 0) or 0)

    vector = _vector_from_payload(payload)
    previous_vector = dict(item.get("avg_vector", {}) or {})
    drift = _vector_distance(previous_vector, vector) if count > 0 else 0.0
    avg_vector = {}
    for key in VECTOR_KEYS:
        lo, hi = (-1.0, 1.0) if key == "asymmetry" else (0.0, 1.0)
        avg_vector[key] = round(
            _avg(float(previous_vector.get(key, 0.0) or 0.0), count, vector[key], lo=lo, hi=hi),
            6,
        )

    world = str(payload.get("world", "") or "-")
    effect = str(payload.get("effect", "") or "-")
    family = str(payload.get("symbol_family", "") or "-")
    field_function = str(payload.get("field_function_class", "") or "-")
    field_variant = str(payload.get("field_function_variant", "") or "-")
    world_binding = str(payload.get("world_binding_quality", "") or "-")
    worlds = _counter_add(dict(item.get("worlds", {}) or {}), world)
    effects = _counter_add(dict(item.get("effects", {}) or {}), effect)
    families = _counter_add(dict(item.get("families", {}) or {}), family)
    field_functions = _counter_add(dict(item.get("field_functions", {}) or {}), field_function)
    field_variants = _counter_add(dict(item.get("field_variants", {}) or {}), field_variant)
    world_bindings = _counter_add(dict(item.get("world_bindings", {}) or {}), world_binding)

    avg_drift = _avg(float(item.get("avg_phase_drift", 0.0) or 0.0), count, drift)
    max_drift = max(float(item.get("max_phase_drift", 0.0) or 0.0), drift)
    positive_score = _positive_phase_score(avg_vector)
    world_count = len([key for key in worlds if key and key != "-"])
    phase_state = _phase_quality_state(
        count=count + 1,
        world_count=world_count,
        avg_drift=avg_drift,
        positive_score=positive_score,
    )
    phase_quality_depth = _clip(
        (_pressure(count + 1, 8.0) * 0.24)
        + (_pressure(world_count, 3.0) * 0.22)
        + ((1.0 - avg_drift) * 0.20)
        + (positive_score * 0.18)
        + (_clip(float(payload.get("depth_score", 0.0) or 0.0)) * 0.16)
    )

    item = {
        **PASSIVE_FLAGS,
        "preview_symbol": symbol,
        "count": count + 1,
        "world_count": world_count,
        "worlds": worlds,
        "effects": effects,
        "families": families,
        "field_functions": field_functions,
        "field_variants": field_variants,
        "world_bindings": world_bindings,
        "dominant_field_function": _dominant(field_functions),
        "dominant_field_variant": _dominant(field_variants),
        "dominant_world_binding": _dominant(world_bindings),
        "last_world": world,
        "last_effect": effect,
        "last_family": family,
        "last_tick": int(payload.get("tick", 0) or 0),
        "avg_vector": avg_vector,
        "last_vector": {key: round(value, 6) for key, value in vector.items()},
        "last_phase_drift": round(drift, 6),
        "avg_phase_drift": round(avg_drift, 6),
        "max_phase_drift": round(max_drift, 6),
        "positive_phase_affinity": round(positive_score, 6),
        "phase_quality_depth": round(phase_quality_depth, 6),
        "phase_quality_state": phase_state,
        "caution_note": "passive_field_phase_memory_not_actionable",
    }
    memory[symbol] = item
    data["passive_mcm_field_phase_signature_memory"] = _trim_mapping(memory, max_items)
    return item


def top_passive_mcm_field_phase_signatures(data: dict, limit: int = 12) -> list[dict]:
    memory = dict((data or {}).get("passive_mcm_field_phase_signature_memory", {}) or {})
    items = [dict(item or {}) for item in memory.values()]
    items.sort(
        key=lambda item: (
            float(item.get("phase_quality_depth", 0.0) or 0.0),
            int(item.get("world_count", 0) or 0),
            int(item.get("count", 0) or 0),
        ),
        reverse=True,
    )
    return items[: max(1, int(limit))]


__all__ = [
    "store_passive_mcm_field_phase_signature",
    "top_passive_mcm_field_phase_signatures",
]
