"""Passive relation-internal event time for growing MCM neighborhoods."""

from __future__ import annotations


PASSIVE_EVENT_BOUNDARY = {
    "passive_only": 1,
    "relation_event_time_only": 1,
    "stored_in_runtime_document": 1,
    "read_by_mini_dio": 0,
    "influences_field": 0,
    "influences_action": 0,
    "deletes_memory": 0,
    "dampens_memory": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}
EVENT_FORMAT = "compact_relation_event_delta_v1"
SCOPE_FIELDS = (
    "field_core_raw",
    "field_full_raw",
    "field_full_plus_duration_standardized",
)
EVENT_FIELDS = (
    "finalization_index",
    "world_pair_count",
    "world_count",
    "growth_seen_count",
    *SCOPE_FIELDS,
)


def _safe_int(value: object) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def _store(data: dict) -> dict:
    store = data.setdefault("passive_mcm_neighborhood_event_memory", {})
    if not isinstance(store, dict):
        store = {}
        data["passive_mcm_neighborhood_event_memory"] = store
    if not isinstance(store.get("relations"), dict):
        store["relations"] = {}
    store.update(PASSIVE_EVENT_BOUNDARY)
    store["format"] = EVENT_FORMAT
    return store


def _numeric_events(record: dict) -> list[list[int]]:
    values = []
    previous = [0] * len(EVENT_FIELDS)
    for raw_delta in list(record.get("event_deltas", []) or []):
        delta = [_safe_int(value) for value in list(raw_delta or [])]
        if len(delta) != len(EVENT_FIELDS):
            raise ValueError("invalid passive MCM neighborhood event delta")
        current = [previous[index] + delta[index] for index in range(len(delta))]
        values.append(current)
        previous = current
    return values


def _event_deltas(values: list[list[int]]) -> list[list[int]]:
    deltas = []
    previous = [0] * len(EVENT_FIELDS)
    for current in values:
        if len(current) != len(EVENT_FIELDS):
            raise ValueError("invalid passive MCM neighborhood event")
        deltas.append(
            [current[index] - previous[index] for index in range(len(EVENT_FIELDS))]
        )
        previous = current
    return deltas


def observe_passive_mcm_neighborhood_growth_event(
    data: dict,
    neighborhood: dict,
    *,
    finalization_index: int,
) -> dict:
    """Append one event exactly when a neighborhood receives new evidence."""

    symbol = str(neighborhood.get("neighborhood_symbol", "") or "")
    if not symbol:
        return {"neighborhood_symbol": "", "event_count": 0}
    store = _store(data)
    relations = store["relations"]
    relation = dict(relations.get(symbol, {}) or {})
    values = _numeric_events(relation)
    if values and values[-1][0] == _safe_int(finalization_index):
        return {"neighborhood_symbol": symbol, "event_count": len(values)}
    scope_support = dict(neighborhood.get("current_scope_support", {}) or {})
    unobserved_prior_events = _safe_int(relation.get("unobserved_prior_events"))
    if not values and "unobserved_prior_events" not in relation:
        unobserved_prior_events = max(
            0, _safe_int(neighborhood.get("growth_seen_count")) - 1
        )
    values.append(
        [
            _safe_int(finalization_index),
            _safe_int(neighborhood.get("current_world_pair_count")),
            _safe_int(neighborhood.get("current_world_count")),
            _safe_int(neighborhood.get("growth_seen_count")),
            *[_safe_int(scope_support.get(scope)) for scope in SCOPE_FIELDS],
        ]
    )
    event_record = {
        "neighborhood_symbol": symbol,
        "left_node": str(neighborhood.get("left_node", "") or ""),
        "right_node": str(neighborhood.get("right_node", "") or ""),
        "event_deltas": _event_deltas(values),
    }
    if unobserved_prior_events:
        event_record["unobserved_prior_events"] = unobserved_prior_events
    relations[symbol] = event_record
    return {"neighborhood_symbol": symbol, "event_count": len(values)}


def passive_mcm_neighborhood_event_relations(data: dict) -> dict[str, dict]:
    """Expand relation events for diagnostics without changing stored deltas."""

    store = _store(data)
    out = {}
    for symbol, raw_record in dict(store.get("relations", {}) or {}).items():
        record = dict(raw_record or {})
        events = []
        for event_index, values in enumerate(_numeric_events(record), start=1):
            event = {field: values[index] for index, field in enumerate(EVENT_FIELDS)}
            event["event_index"] = event_index
            events.append(event)
        out[str(symbol)] = {
            **PASSIVE_EVENT_BOUNDARY,
            "neighborhood_symbol": str(
                record.get("neighborhood_symbol", symbol) or symbol
            ),
            "left_node": str(record.get("left_node", "") or ""),
            "right_node": str(record.get("right_node", "") or ""),
            "unobserved_prior_events": _safe_int(
                record.get("unobserved_prior_events")
            ),
            "event_count": len(events),
            "total_growth_event_count": _safe_int(
                record.get("unobserved_prior_events")
            )
            + len(events),
            "events": events,
        }
    return out


def passive_mcm_neighborhood_event_profile(data: dict) -> dict:
    store = _store(data)
    relations = dict(store.get("relations", {}) or {})
    counts = [len(_numeric_events(dict(record or {}))) for record in relations.values()]
    legacy_counts = [
        _safe_int(dict(record or {}).get("unobserved_prior_events"))
        for record in relations.values()
    ]
    return {
        **PASSIVE_EVENT_BOUNDARY,
        "format": EVENT_FORMAT,
        "relations": len(relations),
        "events": sum(counts),
        "legacy_unobserved_events": sum(legacy_counts),
        "total_growth_events": sum(counts) + sum(legacy_counts),
        "multi_event_relations": sum(count >= 2 for count in counts),
        "maximum_events": max(counts, default=0),
    }


__all__ = [
    "EVENT_FIELDS",
    "EVENT_FORMAT",
    "PASSIVE_EVENT_BOUNDARY",
    "SCOPE_FIELDS",
    "observe_passive_mcm_neighborhood_growth_event",
    "passive_mcm_neighborhood_event_profile",
    "passive_mcm_neighborhood_event_relations",
]
