"""Passive neighborhoods grown from recurring inner MCM episode proximity."""

from __future__ import annotations

import math

from mini_dio.dio_syntax import make_mcm_field_episode_symbol


PASSIVE_NEIGHBOR_BOUNDARY = {
    "passive_only": 1,
    "stored_in_runtime_document": 1,
    "read_by_mini_dio": 0,
    "influences_field": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}

CORE_FIELDS = (
    "avg_mcm_carry_quality",
    "avg_mcm_strain_quality",
    "avg_mcm_rekopplung_quality",
    "avg_mcm_adaptive_rekopplung_quality",
)
FULL_FIELDS = CORE_FIELDS + (
    "avg_sensory_coupling",
    "avg_visual_field_gap",
    "avg_hearing_field_gap",
)
FULL_DURATION_FIELDS = ("avg_duration",) + FULL_FIELDS
PROFILE_SCOPES = (
    ("field_core_raw", CORE_FIELDS, False),
    ("field_full_raw", FULL_FIELDS, False),
    ("field_full_plus_duration_standardized", FULL_DURATION_FIELDS, True),
)
def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if not math.isfinite(result) else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def _safe_mask(value: object) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def _mean_update(previous: object, value: object, count: int) -> float:
    current = _safe_float(value)
    if count <= 1:
        return current
    return ((_safe_float(previous) * (count - 1)) + current) / count


def _base36(value: int) -> str:
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    if not value:
        return "0"
    parts = []
    while value:
        value, remainder = divmod(value, 36)
        parts.append(alphabet[remainder])
    return "".join(reversed(parts))


def _hash_symbol(prefix: str, values: tuple[str, ...], offset: int) -> str:
    hash_value = 2166136261
    for value in values:
        for char in value:
            hash_value ^= ord(char) + offset
            hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"{prefix}{_base36(hash_value).rjust(7, '0')}"


def _world_run_symbol(world: str, run_index: int) -> str:
    return _hash_symbol(
        "dio_mcm_world_",
        (str(world or "unlabeled"), str(_safe_int(run_index))),
        79,
    )


def _neighbor_symbol(left: str, right: str) -> str:
    first, second = sorted((str(left), str(right)))
    return _hash_symbol("dio_mcm_neighbor_", (first, second), 83)


def _run_bit(run_index: int) -> int:
    return 1 << max(0, _safe_int(run_index) - 1)


def _layer(data: dict) -> dict:
    layer = data.setdefault("passive_mcm_neighborhood_memory", {})
    if not isinstance(layer, dict):
        layer = {}
        data["passive_mcm_neighborhood_memory"] = layer
    if not isinstance(layer.get("world_profiles"), dict):
        layer["world_profiles"] = {}
    if not isinstance(layer.get("neighborhoods"), dict):
        layer["neighborhoods"] = {}
    layer.update(PASSIVE_NEIGHBOR_BOUNDARY)
    return layer


def observe_passive_mcm_neighborhood_episode(
    data: dict,
    payload: dict,
    *,
    world: str = "",
    run_index: int = 0,
) -> dict:
    """Accumulate one completed inner episode into its world-run profile."""

    if not isinstance(payload, dict) or not payload:
        return {"world_run_symbol": "", "node_symbol": ""}
    layer = _layer(data)
    world_run_symbol = _world_run_symbol(world, run_index)
    world_profiles = layer["world_profiles"]
    world_profile = dict(world_profiles.get(world_run_symbol, {}) or {})
    nodes = dict(world_profile.get("nodes", {}) or {})
    node_symbol = make_mcm_field_episode_symbol(payload)
    node = dict(nodes.get(node_symbol, {}) or {})
    seen_count = _safe_int(node.get("seen_count")) + 1
    node.update(
        {
            **PASSIVE_NEIGHBOR_BOUNDARY,
            "node_symbol": node_symbol,
            "episode_state": str(payload.get("episode_state", "") or ""),
            "seen_count": seen_count,
        }
    )
    node["avg_duration"] = _mean_update(node.get("avg_duration"), payload.get("duration"), seen_count)
    for field in FULL_FIELDS:
        node[field] = _mean_update(node.get(field), payload.get(field), seen_count)
    nodes[node_symbol] = node
    world_profile.update(
        {
            **PASSIVE_NEIGHBOR_BOUNDARY,
            "world_run_symbol": world_run_symbol,
            "world_label": str(world or "unlabeled"),
            "run_index": _safe_int(run_index),
            "finalized": 0,
            "episode_observations": _safe_int(world_profile.get("episode_observations")) + 1,
            "node_count": len(nodes),
            "nodes": nodes,
        }
    )
    world_profiles[world_run_symbol] = world_profile
    layer["episode_observations"] = _safe_int(layer.get("episode_observations")) + 1
    return {"world_run_symbol": world_run_symbol, "node_symbol": node_symbol}


def _raw_profile(record: dict, fields: tuple[str, ...]) -> list[float]:
    values = [_safe_float(record.get(field)) for field in fields]
    if "avg_duration" in fields:
        index = fields.index("avg_duration")
        values[index] = math.log1p(max(0.0, values[index]))
    return values


def _scaler(vectors: list[list[float]]) -> tuple[list[float], list[float]]:
    dimensions = len(vectors[0])
    means = [sum(vector[index] for vector in vectors) / len(vectors) for index in range(dimensions)]
    deviations = []
    for index in range(dimensions):
        variance = sum((vector[index] - means[index]) ** 2 for vector in vectors) / len(vectors)
        deviations.append(math.sqrt(variance) or 1.0)
    return means, deviations


def _scope_profiles(
    world_profiles: list[dict], fields: tuple[str, ...], standardize: bool
) -> dict[str, dict[str, list[float]]]:
    raw: dict[str, dict[str, list[float]]] = {}
    for world in world_profiles:
        nodes = dict(world.get("nodes", {}) or {})
        raw[str(world["world_run_symbol"])] = {
            symbol: _raw_profile(dict(nodes[symbol] or {}), fields)
            for symbol in sorted(nodes)
        }
    vectors = [vector for world in raw.values() for vector in world.values()]
    if standardize:
        means, deviations = _scaler(vectors)
    else:
        means = [0.0] * len(fields)
        deviations = [1.0] * len(fields)
    return {
        world: {
            symbol: [
                (value - means[index]) / deviations[index]
                for index, value in enumerate(vector)
            ]
            for symbol, vector in profiles.items()
        }
        for world, profiles in raw.items()
    }


def _distance(left: list[float], right: list[float]) -> float:
    return math.sqrt(
        sum((left[index] - right[index]) ** 2 for index in range(len(left))) / len(left)
    )


def _nearest(
    source: dict[str, list[float]], target: dict[str, list[float]]
) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for source_symbol, source_vector in source.items():
        distances = {
            target_symbol: _distance(source_vector, target_vector)
            for target_symbol, target_vector in target.items()
            if target_symbol != source_symbol
        }
        if not distances:
            continue
        minimum = min(distances.values())
        out[source_symbol] = {
            symbol for symbol, value in distances.items() if abs(value - minimum) <= 1e-12
        }
    return out


def _mutual_links(
    left: dict[str, list[float]], right: dict[str, list[float]]
) -> dict[tuple[str, str], float]:
    left_nearest = _nearest(left, right)
    right_nearest = _nearest(right, left)
    links: dict[tuple[str, str], float] = {}
    for left_symbol, right_symbols in left_nearest.items():
        for right_symbol in right_symbols:
            if left_symbol in right_nearest.get(right_symbol, set()):
                pair = tuple(sorted((left_symbol, right_symbol)))
                links[pair] = _distance(left[left_symbol], right[right_symbol])
    return links


def _grow_neighborhoods(layer: dict, world_profile: dict, *, run_index: int) -> None:
    prior_worlds = [
        dict(record or {})
        for symbol, record in sorted(dict(layer.get("world_profiles", {}) or {}).items())
        if symbol != str(world_profile["world_run_symbol"])
        and _safe_int(dict(record or {}).get("finalized")) == 1
    ]
    current: dict[tuple[str, str], dict] = {}
    for prior in prior_worlds:
        pair_worlds = [prior, world_profile]
        left_world = str(prior["world_run_symbol"])
        right_world = str(world_profile["world_run_symbol"])
        world_pair = "|".join(sorted((left_world, right_world)))
        for scope, fields, standardize in PROFILE_SCOPES:
            profiles = _scope_profiles(pair_worlds, fields, standardize)
            for pair, distance in _mutual_links(
                profiles[left_world], profiles[right_world]
            ).items():
                item = current.setdefault(
                    pair,
                    {
                        "scope_support": {},
                        "scope_distance_sum": {},
                        "world_pairs": set(),
                        "world_run_mask": 0,
                        "world_labels": set(),
                    },
                )
                item["scope_support"][scope] = _safe_int(
                    item["scope_support"].get(scope)
                ) + 1
                item["scope_distance_sum"][scope] = _safe_float(
                    item["scope_distance_sum"].get(scope)
                ) + distance
                item["world_pairs"].add(world_pair)
                item["world_run_mask"] |= _run_bit(prior.get("run_index", 0))
                item["world_run_mask"] |= _run_bit(world_profile.get("run_index", 0))
                item["world_labels"].update(
                    (
                        str(prior.get("world_label", "") or ""),
                        str(world_profile.get("world_label", "") or ""),
                    )
                )

    neighborhoods = dict(layer.get("neighborhoods", {}) or {})
    finalization_index = _safe_int(layer.get("finalization_count")) + 1
    for pair, evidence in current.items():
        symbol = _neighbor_symbol(*pair)
        record = dict(neighborhoods.get(symbol, {}) or {})
        scope_support = dict(record.get("current_scope_support", {}) or {})
        avg_distance = dict(record.get("current_avg_distance", {}) or {})
        for scope, increment in dict(evidence["scope_support"]).items():
            previous_count = _safe_int(scope_support.get(scope))
            increment = _safe_int(increment)
            next_count = previous_count + increment
            distance_sum = _safe_float(evidence["scope_distance_sum"].get(scope))
            avg_distance[scope] = (
                (_safe_float(avg_distance.get(scope)) * previous_count) + distance_sum
            ) / max(1, next_count)
            scope_support[scope] = next_count
        legacy_world_count = _safe_int(record.get("legacy_world_count"))
        support_world_mask = _safe_mask(record.get("support_world_mask"))
        if "support_world_runs" in record:
            unresolved = 0
            world_profiles = dict(layer.get("world_profiles", {}) or {})
            for world_run_symbol in set(record.pop("support_world_runs", []) or []):
                profile = dict(world_profiles.get(world_run_symbol, {}) or {})
                if profile:
                    support_world_mask |= _run_bit(profile.get("run_index", 0))
                else:
                    unresolved += 1
            legacy_world_count = max(legacy_world_count, unresolved)
        support_world_mask |= _safe_mask(evidence["world_run_mask"])
        world_examples = set(record.get("world_examples", []) or [])
        world_examples.update(label for label in evidence["world_labels"] if label)
        world_pair_count = _safe_int(record.get("current_world_pair_count")) + len(
            evidence["world_pairs"]
        )
        record.update(
            {
                **PASSIVE_NEIGHBOR_BOUNDARY,
                "neighborhood_symbol": symbol,
                "left_node": pair[0],
                "right_node": pair[1],
                "active": 1,
                "current_scope_count": sum(1 for count in scope_support.values() if _safe_int(count) > 0),
                "current_scope_support": scope_support,
                "current_avg_distance": avg_distance,
                "current_world_pair_count": world_pair_count,
                "current_world_count": legacy_world_count + support_world_mask.bit_count(),
                "support_world_mask": support_world_mask,
                "legacy_world_count": legacy_world_count,
                "world_examples": sorted(world_examples)[:12],
                "first_run": _safe_int(record.get("first_run")) or _safe_int(run_index),
                "last_run": _safe_int(run_index),
                "growth_seen_count": _safe_int(record.get("growth_seen_count")) + 1,
                "peak_world_pair_count": world_pair_count,
                "last_finalization": finalization_index,
            }
        )
        neighborhoods[symbol] = record

    layer["neighborhoods"] = neighborhoods
    layer["finalization_count"] = finalization_index
    layer["finalized_world_profiles"] = len(prior_worlds) + 1
    layer["active_neighborhoods"] = len(neighborhoods)
    layer["historical_neighborhoods"] = len(neighborhoods)


def finalize_passive_mcm_neighborhood_world(
    data: dict,
    *,
    world: str = "",
    run_index: int = 0,
) -> dict:
    """Finalize one world-run profile and reorganize current neighborhoods."""

    layer = _layer(data)
    world_run_symbol = _world_run_symbol(world, run_index)
    world_profile = dict(layer["world_profiles"].get(world_run_symbol, {}) or {})
    if not world_profile:
        return passive_mcm_neighborhood_profile(data)
    if _safe_int(world_profile.get("finalized")) == 1:
        return passive_mcm_neighborhood_profile(data)
    _grow_neighborhoods(layer, world_profile, run_index=run_index)
    world_profile["finalized"] = 1
    layer["world_profiles"][world_run_symbol] = world_profile
    return passive_mcm_neighborhood_profile(data)


def passive_mcm_neighborhood_profile(data: dict) -> dict:
    layer = _layer(data)
    neighborhoods = dict(layer.get("neighborhoods", {}) or {})
    active = [record for record in neighborhoods.values() if _safe_int(record.get("active")) == 1]
    return {
        **PASSIVE_NEIGHBOR_BOUNDARY,
        "world_profiles": len(dict(layer.get("world_profiles", {}) or {})),
        "finalized_world_profiles": _safe_int(layer.get("finalized_world_profiles")),
        "episode_observations": _safe_int(layer.get("episode_observations")),
        "active_neighborhoods": len(active),
        "historical_neighborhoods": len(neighborhoods),
        "active_three_scope_neighborhoods": sum(
            1 for record in active if _safe_int(record.get("current_scope_count")) == len(PROFILE_SCOPES)
        ),
        "active_world_pair_observations": sum(
            _safe_int(record.get("current_world_pair_count")) for record in active
        ),
        "finalization_count": _safe_int(layer.get("finalization_count")),
    }


def top_passive_mcm_neighborhoods(data: dict, limit: int = 8) -> list[dict]:
    records = [
        dict(record or {})
        for record in dict(_layer(data).get("neighborhoods", {}) or {}).values()
        if _safe_int(dict(record or {}).get("active")) == 1
    ]
    records.sort(
        key=lambda record: (
            _safe_int(record.get("current_world_pair_count")),
            _safe_int(record.get("current_scope_count")),
            _safe_int(record.get("current_world_count")),
            _safe_int(record.get("growth_seen_count")),
            str(record.get("neighborhood_symbol", "")),
        ),
        reverse=True,
    )
    return records[: max(1, int(limit))]


__all__ = [
    "PASSIVE_NEIGHBOR_BOUNDARY",
    "PROFILE_SCOPES",
    "finalize_passive_mcm_neighborhood_world",
    "observe_passive_mcm_neighborhood_episode",
    "passive_mcm_neighborhood_profile",
    "top_passive_mcm_neighborhoods",
]
