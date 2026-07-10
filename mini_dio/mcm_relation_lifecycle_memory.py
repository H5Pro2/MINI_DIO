"""Passive lifecycle traces between equally aged MCM relations."""

from __future__ import annotations

import base64
import hashlib
import math
import struct
import zlib

from mini_dio.mcm_neighborhood_event_memory import (
    passive_mcm_neighborhood_event_relations,
)


PASSIVE_RELATION_LIFECYCLE_BOUNDARY = {
    "passive_only": 1,
    "relation_event_derived_only": 1,
    "stored_in_runtime_document": 1,
    "read_by_mini_dio": 0,
    "influences_field": 0,
    "influences_action": 0,
    "deletes_memory": 0,
    "dampens_memory": 0,
    "stores_components": 0,
    "uses_fixed_members": 0,
    "uses_distance_threshold": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}
LIFECYCLE_FORMAT = "compressed_relation_neighbor_observation_chunks_v1"
OBSERVATION_STRUCT = struct.Struct(">III")
BREADTH_FIELDS = ("world_pair_count", "world_count")


def _safe_int(value: object) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def _edge_symbol(left: str, right: str) -> str:
    first, second = sorted((str(left), str(right)))
    digest = hashlib.sha256(f"{first}|{second}".encode("utf-8")).hexdigest()
    return f"dio_mcm_relation_edge_{digest[:16]}"


def _layer(data: dict) -> dict:
    layer = data.setdefault("passive_mcm_relation_lifecycle_memory", {})
    if not isinstance(layer, dict):
        layer = {}
        data["passive_mcm_relation_lifecycle_memory"] = layer
    if not isinstance(layer.get("symbols"), list):
        layer["symbols"] = []
    if not isinstance(layer.get("observation_chunks"), list):
        layer["observation_chunks"] = []
    layer.update(PASSIVE_RELATION_LIFECYCLE_BOUNDARY)
    layer["format"] = LIFECYCLE_FORMAT
    return layer


def _numeric_observations(layer: dict) -> list[list[int]]:
    values = []
    finalization = 0
    for raw_chunk in list(layer.get("observation_chunks", []) or []):
        chunk = dict(raw_chunk or {})
        finalization += _safe_int(chunk.get("finalization_delta"))
        count = _safe_int(chunk.get("observation_count"))
        try:
            compressed = base64.b64decode(str(chunk.get("payload", "") or ""))
            payload = zlib.decompress(compressed)
        except Exception as exc:
            raise ValueError("invalid passive MCM relation lifecycle chunk") from exc
        if len(payload) != count * OBSERVATION_STRUCT.size:
            raise ValueError("invalid passive MCM relation lifecycle chunk size")
        for offset in range(0, len(payload), OBSERVATION_STRUCT.size):
            relation_age, left_index, right_index = OBSERVATION_STRUCT.unpack_from(
                payload, offset
            )
            values.append(
                [finalization, relation_age, left_index, right_index]
            )
    return values


def _breadth_vector(events: list[dict]) -> list[float]:
    values = []
    for left, right in zip(events, events[1:]):
        values.extend(
            float(_safe_int(right[field]) - _safe_int(left[field]))
            for field in BREADTH_FIELDS
        )
    return values


def _rank_values(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda index: values[index])
    ranks = [0.0] * len(values)
    index = 0
    while index < len(order):
        end = index + 1
        while end < len(order) and values[order[end]] == values[order[index]]:
            end += 1
        average_rank = (index + end - 1) / 2.0
        for offset in range(index, end):
            ranks[order[offset]] = average_rank
        index = end
    return ranks


def _rank_vectors(vectors: dict[str, list[float]]) -> dict[str, list[float]]:
    keys = sorted(vectors)
    if not keys:
        return {}
    dimensions = len(vectors[keys[0]])
    ranked_by_position = {
        position: _rank_values([vectors[key][position] for key in keys])
        for position in range(dimensions)
    }
    return {
        key: [ranked_by_position[position][index] for position in range(dimensions)]
        for index, key in enumerate(keys)
    }


def _distance(left: list[float], right: list[float]) -> float:
    return math.sqrt(
        sum((left[index] - right[index]) ** 2 for index in range(len(left)))
        / max(1, len(left))
    )


def _mutual_nearest_edges(
    vectors: dict[str, list[float]],
) -> set[tuple[str, str]]:
    keys = sorted(vectors)
    nearest: dict[str, set[str]] = {}
    for left in keys:
        distances = {
            right: _distance(vectors[left], vectors[right])
            for right in keys
            if right != left
        }
        if not distances:
            continue
        minimum = min(distances.values())
        nearest[left] = {
            right
            for right, value in distances.items()
            if abs(value - minimum) <= 1e-12
        }
    return {
        tuple(sorted((left, right)))
        for left, neighbors in nearest.items()
        for right in neighbors
        if left in nearest.get(right, set())
    }


def _append_edge_observation(
    pair: tuple[str, str],
    *,
    relation_age: int,
    observations: list[tuple[int, int, int]],
    symbols: list[str],
    symbol_indexes: dict[str, int],
) -> None:
    for relation in pair:
        if relation not in symbol_indexes:
            symbol_indexes[relation] = len(symbols)
            symbols.append(relation)
    observations.append(
        (
        _safe_int(relation_age),
        symbol_indexes[pair[0]],
        symbol_indexes[pair[1]],
        )
    )


def _append_observation_chunk(
    layer: dict,
    *,
    finalization_index: int,
    observations: list[tuple[int, int, int]],
) -> None:
    if not observations:
        return
    payload = b"".join(OBSERVATION_STRUCT.pack(*item) for item in observations)
    previous_finalization = _safe_int(layer.get("last_chunk_finalization"))
    layer["observation_chunks"].append(
        {
            "finalization_delta": _safe_int(finalization_index)
            - previous_finalization,
            "observation_count": len(observations),
            "payload": base64.b64encode(zlib.compress(payload, level=9)).decode(
                "ascii"
            ),
        }
    )
    layer["last_chunk_finalization"] = _safe_int(finalization_index)
    layer["observation_count"] = _safe_int(layer.get("observation_count")) + len(
        observations
    )


def observe_passive_mcm_relation_lifecycle(
    data: dict,
    *,
    finalization_index: int,
    changed_relations: set[str],
) -> dict:
    """Observe mutual breadth neighbors without selecting fixed members."""

    layer = _layer(data)
    if _safe_int(layer.get("last_finalization")) == _safe_int(finalization_index):
        return {
            **PASSIVE_RELATION_LIFECYCLE_BOUNDARY,
            "format": LIFECYCLE_FORMAT,
            "last_finalization": _safe_int(finalization_index),
            "observations": _safe_int(layer.get("observation_count")),
        }
    relations = passive_mcm_neighborhood_event_relations(data)
    changed = {str(symbol) for symbol in changed_relations if str(symbol)}
    if _safe_int(layer.get("started_at_finalization")) == 0:
        current_events = sum(
            _safe_int(relation.get("event_count")) for relation in relations.values()
        )
        current_changed_events = sum(symbol in relations for symbol in changed)
        layer["started_at_finalization"] = _safe_int(finalization_index)
        layer["source_events_before_start"] = max(
            0, current_events - current_changed_events
        )
        layer["source_relations_at_start"] = len(relations)

    complete = {
        symbol: relation
        for symbol, relation in relations.items()
        if _safe_int(relation.get("unobserved_prior_events")) == 0
    }
    changed_ages = {
        _safe_int(complete[symbol].get("event_count"))
        for symbol in changed
        if symbol in complete and _safe_int(complete[symbol].get("event_count")) >= 2
    }
    symbol_indexes = {
        str(symbol): index for index, symbol in enumerate(layer["symbols"])
    }
    observations: list[tuple[int, int, int]] = []
    for age in sorted(changed_ages):
        raw_vectors = {
            symbol: _breadth_vector(list(relation.get("events", []) or []))
            for symbol, relation in complete.items()
            if _safe_int(relation.get("event_count")) == age
        }
        if len(raw_vectors) < 2:
            continue
        ranked = _rank_vectors(raw_vectors)
        for pair in _mutual_nearest_edges(ranked):
            if not changed.intersection(pair):
                continue
            _append_edge_observation(
                pair,
                relation_age=age,
                observations=observations,
                symbols=layer["symbols"],
                symbol_indexes=symbol_indexes,
            )
    _append_observation_chunk(
        layer,
        finalization_index=finalization_index,
        observations=observations,
    )
    layer["observation_calls"] = _safe_int(layer.get("observation_calls")) + 1
    layer["last_finalization"] = _safe_int(finalization_index)
    return {
        **PASSIVE_RELATION_LIFECYCLE_BOUNDARY,
        "format": LIFECYCLE_FORMAT,
        "last_finalization": _safe_int(finalization_index),
        "observations": _safe_int(layer.get("observation_count")),
    }


def passive_mcm_relation_lifecycle_edges(data: dict) -> dict[str, dict]:
    layer = _layer(data)
    symbols = [str(symbol) for symbol in layer["symbols"]]
    grouped: dict[tuple[str, str], list[dict[str, int]]] = {}
    for values in _numeric_observations(layer):
        left_index = values[2]
        right_index = values[3]
        if not (0 <= left_index < len(symbols) and 0 <= right_index < len(symbols)):
            raise ValueError("invalid passive MCM relation lifecycle symbol index")
        pair = tuple(sorted((symbols[left_index], symbols[right_index])))
        observations = grouped.setdefault(pair, [])
        observations.append(
            {
                "finalization_index": values[0],
                "relation_age": values[1],
                "observation_index": len(observations) + 1,
            }
        )
    out = {}
    for pair, observations in grouped.items():
        symbol = _edge_symbol(*pair)
        out["|".join(pair)] = {
            **PASSIVE_RELATION_LIFECYCLE_BOUNDARY,
            "edge_symbol": symbol,
            "left_relation": pair[0],
            "right_relation": pair[1],
            "observation_count": len(observations),
            "observations": observations,
        }
    return out


def passive_mcm_relation_lifecycle_profile(data: dict) -> dict:
    layer = _layer(data)
    source_relations = passive_mcm_neighborhood_event_relations(data)
    edges = passive_mcm_relation_lifecycle_edges(data)
    relations = set()
    partners: dict[str, set[str]] = {}
    observations = 0
    recurring_edges = 0
    later_age_edges = 0
    maximum_age = 0
    for edge in edges.values():
        left = str(edge["left_relation"])
        right = str(edge["right_relation"])
        relations.update((left, right))
        partners.setdefault(left, set()).add(right)
        partners.setdefault(right, set()).add(left)
        history = list(edge["observations"])
        observations += len(history)
        recurring_edges += int(len(history) >= 2)
        ages = [_safe_int(item.get("relation_age")) for item in history]
        maximum_age = max(maximum_age, *ages, 0)
        later_age_edges += int(bool(ages) and max(ages) > min(ages))
    incomplete = sum(
        _safe_int(relation.get("unobserved_prior_events")) > 0
        for relation in source_relations.values()
    )
    return {
        **PASSIVE_RELATION_LIFECYCLE_BOUNDARY,
        "format": LIFECYCLE_FORMAT,
        "started_at_finalization": _safe_int(layer.get("started_at_finalization")),
        "last_finalization": _safe_int(layer.get("last_finalization")),
        "observation_calls": _safe_int(layer.get("observation_calls")),
        "source_events_before_start": _safe_int(
            layer.get("source_events_before_start")
        ),
        "source_relations_at_start": _safe_int(
            layer.get("source_relations_at_start")
        ),
        "source_relations": len(source_relations),
        "incomplete_source_relations_ignored": incomplete,
        "relations": len(relations),
        "edges": len(edges),
        "observations": observations,
        "recurring_edges": recurring_edges,
        "edges_reappearing_at_later_age": later_age_edges,
        "relations_with_multiple_partners": sum(
            len(neighbors) >= 2 for neighbors in partners.values()
        ),
        "maximum_relation_age": maximum_age,
    }


def top_passive_mcm_relation_lifecycle_edges(
    data: dict, limit: int = 8
) -> list[dict]:
    records = list(passive_mcm_relation_lifecycle_edges(data).values())
    records.sort(
        key=lambda record: (
            _safe_int(record.get("observation_count")),
            _safe_int(list(record.get("observations", []) or [{}])[-1].get("relation_age")),
            str(record.get("edge_symbol", "")),
        ),
        reverse=True,
    )
    return records[: max(1, int(limit))]


__all__ = [
    "BREADTH_FIELDS",
    "LIFECYCLE_FORMAT",
    "OBSERVATION_FIELDS",
    "PASSIVE_RELATION_LIFECYCLE_BOUNDARY",
    "observe_passive_mcm_relation_lifecycle",
    "passive_mcm_relation_lifecycle_edges",
    "passive_mcm_relation_lifecycle_profile",
    "top_passive_mcm_relation_lifecycle_edges",
]
