"""Active action-memory compatibility layer.

This module preserves the older symbol/family action statistics used by the
current mini runtime. It is intentionally separated from passive MCM meaning,
episode and field-memory stores so active compatibility does not define the
target memory architecture.
"""

from __future__ import annotations


ACTION_NAMES = ("WAIT", "LONG", "SHORT")


def _clip(value: float, lo: float = -1.0, hi: float = 1.0) -> float:
    try:
        value = float(value)
    except Exception:
        value = 0.0
    if value != value:
        value = 0.0
    return max(lo, min(hi, value))


def _vector_distance(left: list[float], right: list[float]) -> float:
    if not left or not right:
        return 1.0
    size = min(len(left), len(right))
    if size <= 0:
        return 1.0
    total = 0.0
    for i in range(size):
        total += abs(float(left[i]) - float(right[i]))
    return total / size


def _update_vector(record: dict, vector: list[float], count: int) -> None:
    if not vector:
        return
    previous = record.get("vector")
    if not isinstance(previous, list) or len(previous) != len(vector):
        record["vector"] = [_clip(value) for value in vector]
        return
    weight_old = max(1, int(count) - 1)
    weight_new = 1
    denom = weight_old + weight_new
    record["vector"] = [
        _clip(((float(previous[i]) * weight_old) + (_clip(vector[i]) * weight_new)) / denom)
        for i in range(len(vector))
    ]


def _default_action_map() -> dict:
    return {
        action: {
            "count": 0,
            "reward_sum": 0.0,
            "trust": 0.0,
            "caution": 0.0,
            "last_reward": 0.0,
            "timing_improvement_sum": 0.0,
            "last_timing_improvement": 0.0,
        }
        for action in ACTION_NAMES
    }


def _default_observation_map() -> dict:
    return {
        action: {
            "count": 0,
            "recognition_sum": 0.0,
            "reward_sum": 0.0,
            "last_recognition": 0.0,
            "last_reward": 0.0,
        }
        for action in ACTION_NAMES
    }


def _ensure_action_defaults(record: dict) -> dict:
    actions = record.setdefault("actions", {})
    defaults = _default_action_map()
    for action in ACTION_NAMES:
        state = actions.setdefault(action, {})
        for key, value in defaults[action].items():
            state.setdefault(key, value)
    return actions


def _ensure_observations(record: dict) -> dict:
    observations = record.setdefault("observations", {})
    for action in ACTION_NAMES:
        observations.setdefault(
            action,
            {
                "count": 0,
                "recognition_sum": 0.0,
                "reward_sum": 0.0,
                "last_recognition": 0.0,
                "last_reward": 0.0,
            },
        )
    return observations


def _action_signal(record: dict, action: str) -> float:
    state = dict(dict(record.get("actions", {}) or {}).get(action, {}) or {})
    trust = float(state.get("trust", 0.0) or 0.0)
    caution = float(state.get("caution", 0.0) or 0.0)
    count = int(state.get("count", 0) or 0)
    familiarity = min(1.0, count / 6.0)
    return (trust - caution) * familiarity


def _observation_signal(record: dict, action: str) -> float:
    observations = _ensure_observations(record)
    state = dict(observations.get(action, {}) or {})
    count = int(state.get("count", 0) or 0)
    if count <= 0:
        return 0.0
    recognition_avg = float(state.get("recognition_sum", 0.0) or 0.0) / max(1, count)
    reward_avg = float(state.get("reward_sum", 0.0) or 0.0) / max(1, count)
    familiarity = min(1.0, count / 8.0)
    return _clip(recognition_avg * reward_avg * familiarity, -1.0, 1.0)


def _associative_signal(records: list[dict], action: str, vector: list[float]) -> float:
    if not vector:
        return 0.0
    has_signal = False
    for record in records:
        if _action_signal(record, action) != 0.0:
            has_signal = True
            break
    if not has_signal:
        return 0.0
    weighted = 0.0
    weight_sum = 0.0
    for record in records:
        record_vector = record.get("vector")
        if not isinstance(record_vector, list):
            continue
        distance = _vector_distance(vector, record_vector)
        weight = 1.0 / (1.0 + (distance * distance * 12.0))
        signal = _action_signal(record, action)
        weighted += signal * weight
        weight_sum += weight
    if weight_sum <= 0.0:
        return 0.0
    return _clip(weighted / weight_sum, -1.0, 1.0)


def episode_record_rank(item: dict) -> tuple:
    actions = dict(item.get("actions", {}) or {})
    observations = dict(item.get("observations", {}) or {})
    action_count = sum(int(dict(actions.get(action, {}) or {}).get("count", 0) or 0) for action in ACTION_NAMES)
    observation_count = sum(int(dict(observations.get(action, {}) or {}).get("count", 0) or 0) for action in ACTION_NAMES)
    action_reward = sum(abs(float(dict(actions.get(action, {}) or {}).get("reward_sum", 0.0) or 0.0)) for action in ACTION_NAMES)
    observation_reward = sum(
        abs(float(dict(observations.get(action, {}) or {}).get("reward_sum", 0.0) or 0.0)) for action in ACTION_NAMES
    )
    return (
        int(item.get("count", 0) or 0),
        action_count + observation_count,
        action_reward + observation_reward,
    )


def compact_record(record: dict) -> dict:
    compact = dict(record)
    compact.pop("vector", None)
    return compact


def family_record(data: dict, family: str) -> dict:
    family = str(family or "-") or "-"
    families = data.setdefault("families", {})
    record = families.get(family)
    if not isinstance(record, dict):
        record = {
            "family": family,
            "count": 0,
            "actions": _default_action_map(),
            "observations": _default_observation_map(),
        }
        families[family] = record
    _ensure_observations(record)
    _ensure_action_defaults(record)
    return record


def symbol_record(data: dict, symbol: str) -> dict:
    symbols = data.setdefault("symbols", {})
    record = symbols.get(symbol)
    if not isinstance(record, dict):
        record = {
            "symbol": symbol,
            "count": 0,
            "actions": _default_action_map(),
            "observations": _default_observation_map(),
            "syntax_family": symbol[:8],
        }
        symbols[symbol] = record
    _ensure_observations(record)
    _ensure_action_defaults(record)
    return record


def action_diagnostics(data: dict, symbol: str, action: str, vector: list[float] | None = None) -> dict:
    record = symbol_record(data, symbol)
    action_state = record.get("actions", {}).get(action, {})
    trust = float(action_state.get("trust", 0.0) or 0.0)
    caution = float(action_state.get("caution", 0.0) or 0.0)
    count = int(action_state.get("count", 0) or 0)
    familiarity = min(1.0, count / 8.0)
    family = str(record.get("syntax_family", symbol[:8]) or symbol[:8])
    family_state = family_record(data, family).get("actions", {}).get(action, {})
    family_trust = float(family_state.get("trust", 0.0) or 0.0)
    family_caution = float(family_state.get("caution", 0.0) or 0.0)
    family_count = int(family_state.get("count", 0) or 0)
    family_familiarity = min(1.0, family_count / 6.0)
    symbol_bias = (trust - caution) * (0.25 + familiarity * 0.45)
    family_bias = (family_trust - family_caution) * (0.20 + family_familiarity * 0.55)
    symbol_observation = _observation_signal(record, action)
    family_observation = _observation_signal(family_record(data, family), action)
    observation_signal = (symbol_observation * 0.35) + (family_observation * 0.65)
    family_records = list(data.get("families", {}).values())
    associative_raw = _associative_signal(family_records, action, vector or [])
    associative_bias = associative_raw * 0.16
    observation_bias = observation_signal * 0.08
    readiness = _clip(
        ((trust - caution) * min(1.0, count / 5.0) * 0.52)
        + ((family_trust - family_caution) * min(1.0, family_count / 5.0) * 0.41)
        + (associative_raw * 0.07),
        -1.0,
        1.0,
    )
    observation_readiness = observation_signal * 0.11
    readiness = _clip(
        readiness + observation_readiness,
        -1.0,
        1.0,
    )
    return {
        "symbol": symbol,
        "family": family,
        "action": action,
        "symbol_count": count,
        "family_count": family_count,
        "symbol_trust": trust,
        "symbol_caution": caution,
        "family_trust": family_trust,
        "family_caution": family_caution,
        "symbol_bias": symbol_bias,
        "family_bias": family_bias,
        "symbol_observation": symbol_observation,
        "family_observation": family_observation,
        "observation_signal": observation_signal,
        "observation_bias": observation_bias,
        "observation_readiness": observation_readiness,
        "associative_raw": associative_raw,
        "associative_bias": associative_bias,
        "action_bias": symbol_bias + family_bias + associative_bias + observation_bias,
        "readiness": readiness,
    }


def action_bias(data: dict, symbol: str, action: str, vector: list[float] | None = None) -> float:
    return float(action_diagnostics(data, symbol, action, vector=vector).get("action_bias", 0.0) or 0.0)


def action_readiness(data: dict, symbol: str, action: str, vector: list[float] | None = None) -> float:
    return float(action_diagnostics(data, symbol, action, vector=vector).get("readiness", 0.0) or 0.0)


def learn(
    data: dict,
    symbol: str,
    action: str,
    reward: float,
    *,
    shadow: bool = False,
    vector: list[float] | None = None,
    timing_improvement: float = 0.0,
) -> None:
    action = str(action or "WAIT").upper()
    if action not in ACTION_NAMES:
        action = "WAIT"
    record = symbol_record(data, symbol)
    record["count"] = int(record.get("count", 0) or 0) + (0 if shadow else 1)
    _update_vector(record, vector or [], int(record.get("count", 1) or 1))
    family = str(record.get("syntax_family", symbol[:8]) or symbol[:8])
    family_data = family_record(data, family)
    family_data["count"] = int(family_data.get("count", 0) or 0) + (0 if shadow else 1)
    _update_vector(family_data, vector or [], int(family_data.get("count", 1) or 1))
    actions = record.setdefault("actions", {})
    action_state = actions.setdefault(
        action,
        {
            "count": 0,
            "reward_sum": 0.0,
            "trust": 0.0,
            "caution": 0.0,
            "last_reward": 0.0,
            "timing_improvement_sum": 0.0,
            "last_timing_improvement": 0.0,
        },
    )
    family_actions = family_data.setdefault("actions", {})
    family_action_state = family_actions.setdefault(
        action,
        {
            "count": 0,
            "reward_sum": 0.0,
            "trust": 0.0,
            "caution": 0.0,
            "last_reward": 0.0,
            "timing_improvement_sum": 0.0,
            "last_timing_improvement": 0.0,
        },
    )
    alpha = 0.10 if shadow else 0.18
    family_alpha = 0.08 if shadow else 0.14
    reward = _clip(reward, -2.0, 2.0)
    timing_improvement = _clip(timing_improvement, 0.0, 1.0)
    action_state["count"] = int(action_state.get("count", 0) or 0) + 1
    action_state["reward_sum"] = float(action_state.get("reward_sum", 0.0) or 0.0) + reward
    action_state["last_reward"] = reward
    action_state["timing_improvement_sum"] = (
        float(action_state.get("timing_improvement_sum", 0.0) or 0.0) + timing_improvement
    )
    action_state["last_timing_improvement"] = timing_improvement
    family_action_state["count"] = int(family_action_state.get("count", 0) or 0) + 1
    family_action_state["reward_sum"] = float(family_action_state.get("reward_sum", 0.0) or 0.0) + reward
    family_action_state["last_reward"] = reward
    family_action_state["timing_improvement_sum"] = (
        float(family_action_state.get("timing_improvement_sum", 0.0) or 0.0) + timing_improvement
    )
    family_action_state["last_timing_improvement"] = timing_improvement
    positive = max(0.0, reward)
    negative = max(0.0, -reward)
    action_state["trust"] = _clip(
        (float(action_state.get("trust", 0.0) or 0.0) * (1.0 - alpha)) + (positive * alpha),
        0.0,
        1.0,
    )
    action_state["caution"] = _clip(
        (float(action_state.get("caution", 0.0) or 0.0) * (1.0 - alpha)) + (negative * alpha),
        0.0,
        1.0,
    )
    family_action_state["trust"] = _clip(
        (float(family_action_state.get("trust", 0.0) or 0.0) * (1.0 - family_alpha)) + (positive * family_alpha),
        0.0,
        1.0,
    )
    family_action_state["caution"] = _clip(
        (float(family_action_state.get("caution", 0.0) or 0.0) * (1.0 - family_alpha)) + (negative * family_alpha),
        0.0,
        1.0,
    )


def learn_observation(
    data: dict,
    symbol: str,
    action: str,
    reward: float,
    recognition: float,
    *,
    vector: list[float] | None = None,
) -> None:
    action = str(action or "WAIT").upper()
    if action not in ACTION_NAMES:
        action = "WAIT"
    recognition = _clip(recognition, 0.0, 1.0)
    reward = _clip(reward, -2.0, 2.0)
    if recognition <= 0.0:
        return
    record = symbol_record(data, symbol)
    family = str(record.get("syntax_family", symbol[:8]) or symbol[:8])
    family_data = family_record(data, family)
    _update_vector(record, vector or [], int(record.get("count", 0) or 0) + 1)
    _update_vector(family_data, vector or [], int(family_data.get("count", 0) or 0) + 1)
    for target in (record, family_data):
        observations = _ensure_observations(target)
        state = observations[action]
        state["count"] = int(state.get("count", 0) or 0) + 1
        state["recognition_sum"] = float(state.get("recognition_sum", 0.0) or 0.0) + recognition
        state["reward_sum"] = float(state.get("reward_sum", 0.0) or 0.0) + reward
        state["last_recognition"] = recognition
        state["last_reward"] = reward
