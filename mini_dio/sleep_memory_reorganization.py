"""Passive sleep-memory reorganization for MINI_DIO.

Sleep reorganization is intentionally narrow: it marks which stored MCM-field
episode roles were touched in an offline field milieu. It does not create world
symbols, directions, entries, gates, or motoric signals.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations
from pathlib import Path


PASSIVE_SLEEP_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
    "writes_runtime_memory": 0,
}


def _split_pipe(value: str) -> list[str]:
    return [part for part in str(value or "").split("|") if part]


def _safe_float(value: object) -> float:
    try:
        result = float(value)
    except Exception:
        result = 0.0
    if result != result:
        return 0.0
    return result


def _safe_int(value: object) -> int:
    try:
        return int(float(value))
    except Exception:
        return 0


def _clip01(value: object) -> float:
    return max(0.0, min(1.0, _safe_float(value)))


def _pressure(value: object, scale: float = 1.0) -> float:
    amount = max(0.0, _safe_float(value))
    return amount / (amount + max(0.000001, scale))


def _mean(*values: object) -> float:
    clean = [_clip01(value) for value in values]
    return sum(clean) / max(1, len(clean))


def _dominant_label(scores: dict[str, float], default: str) -> str:
    clean = {key: _clip01(value) for key, value in scores.items()}
    if not clean:
        return default
    return max(clean, key=clean.get)


def build_sleep_reorganization_memory(memory: dict, sleep_summary: dict, sleep_rows: list[dict]) -> dict:
    """Build a passive sleep reorganization artifact from sleep ticks."""

    role_counter: Counter[str] = Counter()
    role_resonance_sum: Counter[str] = Counter()
    role_states: dict[str, Counter[str]] = {}
    pair_counter: Counter[tuple[str, str]] = Counter()
    pair_resonance_sum: Counter[tuple[str, str]] = Counter()
    pair_states: dict[tuple[str, str], Counter[str]] = {}
    for row in sleep_rows or []:
        roles = _split_pipe(str(row.get("active_roles", "") or ""))
        resonances = [_safe_float(item) for item in _split_pipe(str(row.get("active_role_resonance", "") or ""))]
        state = str(row.get("sleep_state", "") or "-")
        for index, role in enumerate(roles):
            role_counter[role] += 1
            role_resonance_sum[role] += resonances[index] if index < len(resonances) else 0.0
            role_states.setdefault(role, Counter())[state] += 1
        indexed_resonance = {
            role: resonances[index] if index < len(resonances) else 0.0
            for index, role in enumerate(roles)
        }
        for left, right in combinations(sorted(set(roles)), 2):
            pair = (left, right)
            pair_counter[pair] += 1
            pair_resonance_sum[pair] += (indexed_resonance.get(left, 0.0) + indexed_resonance.get(right, 0.0)) / 2.0
            pair_states.setdefault(pair, Counter())[state] += 1

    field_episodes = dict(memory.get("mcm_field_episode_memory", {}) or {})
    touched_roles = []
    for role, count in role_counter.most_common():
        source = dict(field_episodes.get(role, {}) or {})
        avg_resonance = float(role_resonance_sum[role]) / max(1, int(count))
        touched_roles.append(
            {
                "role": role,
                "touch_count": int(count),
                "touch_ratio": round(int(count) / max(1, _safe_int(sleep_summary.get("ticks", 0))), 6),
                "avg_sleep_resonance": round(avg_resonance, 6),
                "sleep_states": dict(sorted(role_states.get(role, Counter()).items())),
                "source_episode_state": str(source.get("episode_state", "") or ""),
                "source_transition": str(source.get("transition", "") or ""),
                "source_seen_count": _safe_int(source.get("seen_count", 0)),
                "source_rekopplung": round(_safe_float(source.get("avg_mcm_rekopplung_quality", 0.0)), 6),
                "source_carry": round(_safe_float(source.get("avg_mcm_carry_quality", 0.0)), 6),
                "source_strain": round(_safe_float(source.get("avg_mcm_strain_quality", 0.0)), 6),
                **PASSIVE_SLEEP_FLAGS,
            }
        )

    combination_traces = []
    for pair, count in pair_counter.most_common():
        avg_pair_resonance = float(pair_resonance_sum[pair]) / max(1, int(count))
        left, right = pair
        left_source = dict(field_episodes.get(left, {}) or {})
        right_source = dict(field_episodes.get(right, {}) or {})
        same_source_state = str(left_source.get("episode_state", "") or "") == str(
            right_source.get("episode_state", "") or ""
        )
        same_transition = str(left_source.get("transition", "") or "") == str(right_source.get("transition", "") or "")
        if same_transition and same_source_state:
            combination_state = "sleep_same_role_family_combination"
        elif same_source_state:
            combination_state = "sleep_same_state_combination"
        else:
            combination_state = "sleep_cross_state_combination"
        combination_traces.append(
            {
                "roles": [left, right],
                "pair_key": f"{left}|{right}",
                "co_touch_count": int(count),
                "co_touch_ratio": round(int(count) / max(1, _safe_int(sleep_summary.get("ticks", 0))), 6),
                "avg_pair_sleep_resonance": round(avg_pair_resonance, 6),
                "combination_state": combination_state,
                "sleep_states": dict(sorted(pair_states.get(pair, Counter()).items())),
                "left_source_episode_state": str(left_source.get("episode_state", "") or ""),
                "right_source_episode_state": str(right_source.get("episode_state", "") or ""),
                "left_source_transition": str(left_source.get("transition", "") or ""),
                "right_source_transition": str(right_source.get("transition", "") or ""),
                **PASSIVE_SLEEP_FLAGS,
            }
        )

    role_set_count = _safe_int(sleep_summary.get("active_role_set_count", 0))
    touched_count = len(touched_roles)
    touch_pressure = _pressure(touched_count, 1.0)
    role_set_pressure = _pressure(role_set_count, 1.0)
    focus_pressure = _mean(touch_pressure, 1.0 - role_set_pressure)
    broad_pressure = _mean(touch_pressure, role_set_pressure)
    reorganization_state = _dominant_label(
        {
            "sleep_no_touch": 1.0 - touch_pressure,
            "sleep_single_rekopplung_trace": _mean(touch_pressure, 1.0 - role_set_pressure),
            "sleep_focused_role_touch": focus_pressure,
            "sleep_broad_role_touch": broad_pressure,
        },
        default="sleep_no_touch",
    )

    return {
        "version": 1,
        "kind": "passive_sleep_reorganization_memory",
        "reorganization_state": reorganization_state,
        "sleep_symbol": str(sleep_summary.get("sleep_top_symbol", "") or ""),
        "sleep_unique_symbols": _safe_int(sleep_summary.get("sleep_unique_symbols", 0)),
        "sleep_ticks": _safe_int(sleep_summary.get("ticks", 0)),
        "sleep_state_counts": dict(sleep_summary.get("state_counts", {}) or {}),
        "avg_afterimage_abs": round(_safe_float(sleep_summary.get("avg_afterimage_abs", 0.0)), 6),
        "avg_signature_abs": round(_safe_float(sleep_summary.get("avg_signature_abs", 0.0)), 6),
        "active_role_set_count": role_set_count,
        "touched_role_count": touched_count,
        "touched_roles": touched_roles[:24],
        "combination_trace_count": len(combination_traces),
        "combination_traces": combination_traces[:32],
        "interpretation_boundary": (
            "Passive Sleep-Reorganisation markiert beruehrte bestehende Rollen. "
            "Kombinationsspuren beschreiben nur gemeinsame Offline-Beruehrung. "
            "Sie erzeugt keine neue Weltbedeutung und steuert keine Handlung."
        ),
        **PASSIVE_SLEEP_FLAGS,
    }


def apply_sleep_reorganization_to_memory_file(
    memory_path: Path,
    sleep_summary: dict,
    sleep_rows: list[dict],
) -> dict:
    """Write passive sleep reorganization into an existing memory file."""

    memory_path = Path(memory_path)
    memory = json.loads(memory_path.read_text(encoding="utf-8"))
    sleep_memory = build_sleep_reorganization_memory(memory, sleep_summary, sleep_rows)
    history = memory.setdefault("passive_sleep_reorganization_history", [])
    if not isinstance(history, list):
        history = []
    history.append(sleep_memory)
    memory["passive_sleep_reorganization_history"] = history[-16:]
    memory["passive_sleep_reorganization_memory"] = sleep_memory
    temp_path = memory_path.with_suffix(memory_path.suffix + ".tmp")
    temp_path.write_text(json.dumps(memory, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    temp_path.replace(memory_path)
    return sleep_memory


__all__ = [
    "apply_sleep_reorganization_to_memory_file",
    "build_sleep_reorganization_memory",
]
