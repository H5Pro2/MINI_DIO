"""Field-free passive consolidation of MCM neighborhood maturation layers."""

from __future__ import annotations

import hashlib


PASSIVE_CONSOLIDATION_BOUNDARY = {
    "passive_only": 1,
    "offline_only": 1,
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
CONSOLIDATION_FORMAT = "compact_delta_v1"
SUPPORT_AXES = ("world_pair_count", "world_count", "growth_seen_count")
DELTA_FIELDS = (
    "checkpoint_index",
    "pareto_depth",
    "world_pair_count",
    "world_count",
    "growth_seen_count",
)


def _safe_int(value: object) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def _checkpoint_symbol(label: str, run_index: int) -> str:
    digest = hashlib.sha256(f"{label}|{_safe_int(run_index)}".encode("utf-8")).hexdigest()[:14]
    return f"dio_mcm_consolidation_{digest}"


def _store(data: dict) -> dict:
    store = data.setdefault("passive_mcm_neighborhood_consolidation", {})
    if not isinstance(store, dict):
        store = {}
        data["passive_mcm_neighborhood_consolidation"] = store
    if not isinstance(store.get("checkpoints"), list):
        store["checkpoints"] = []
    if not isinstance(store.get("relations"), dict):
        store["relations"] = {}
    store.update(PASSIVE_CONSOLIDATION_BOUNDARY)
    has_verbose_relations = any(
        isinstance(record, dict)
        and "history" in record
        and "history_deltas" not in record
        for record in store["relations"].values()
    )
    store["format"] = "verbose_v1" if has_verbose_relations else CONSOLIDATION_FORMAT
    return store


def _dominates(left: dict[str, object], right: dict[str, object]) -> bool:
    left_values = [_safe_int(left[axis]) for axis in SUPPORT_AXES]
    right_values = [_safe_int(right[axis]) for axis in SUPPORT_AXES]
    return all(
        left_values[index] >= right_values[index] for index in range(len(SUPPORT_AXES))
    ) and any(
        left_values[index] > right_values[index] for index in range(len(SUPPORT_AXES))
    )


def pareto_depths(rows: list[dict[str, object]]) -> dict[str, int]:
    """Return non-dominated sorting depth without weights or thresholds."""

    count = len(rows)
    dominated_by_count = [0] * count
    dominates: list[list[int]] = [[] for _ in rows]
    for left_index in range(count):
        for right_index in range(left_index + 1, count):
            if _dominates(rows[left_index], rows[right_index]):
                dominates[left_index].append(right_index)
                dominated_by_count[right_index] += 1
            elif _dominates(rows[right_index], rows[left_index]):
                dominates[right_index].append(left_index)
                dominated_by_count[left_index] += 1

    front = [index for index, value in enumerate(dominated_by_count) if value == 0]
    depths: dict[str, int] = {}
    depth = 1
    assigned = 0
    while front:
        next_front = []
        for index in front:
            depths[str(rows[index]["pair_key"])] = depth
            assigned += 1
            for dominated_index in dominates[index]:
                dominated_by_count[dominated_index] -= 1
                if dominated_by_count[dominated_index] == 0:
                    next_front.append(dominated_index)
        front = next_front
        depth += 1
    if assigned != count:
        raise RuntimeError(f"Pareto depth assignment incomplete: {assigned}/{count}")
    return depths


def _active_neighborhood_rows(data: dict) -> list[dict[str, object]]:
    layer = dict(data.get("passive_mcm_neighborhood_memory", {}) or {})
    rows = []
    for symbol, raw_record in dict(layer.get("neighborhoods", {}) or {}).items():
        record = dict(raw_record or {})
        if _safe_int(record.get("active")) != 1:
            continue
        left_node = str(record.get("left_node", "") or "")
        right_node = str(record.get("right_node", "") or "")
        pair_key = "|".join(sorted((left_node, right_node)))
        rows.append(
            {
                "pair_key": pair_key,
                "neighborhood_symbol": str(
                    record.get("neighborhood_symbol", symbol) or symbol
                ),
                "left_node": left_node,
                "right_node": right_node,
                "world_pair_count": _safe_int(record.get("current_world_pair_count")),
                "world_count": _safe_int(record.get("current_world_count")),
                "growth_seen_count": _safe_int(record.get("growth_seen_count")),
            }
        )
    rows.sort(key=lambda row: str(row["pair_key"]))
    return rows


def _checkpoint_map(store: dict) -> dict[int, dict]:
    return {
        _safe_int(item.get("checkpoint_index")): dict(item or {})
        for item in list(store.get("checkpoints", []) or [])
        if isinstance(item, dict)
    }


def _numeric_history(record: dict) -> list[list[int]]:
    deltas = list(record.get("history_deltas", []) or [])
    if deltas:
        values: list[list[int]] = []
        previous = [0] * len(DELTA_FIELDS)
        for raw_delta in deltas:
            delta = [_safe_int(value) for value in list(raw_delta or [])]
            if len(delta) != len(DELTA_FIELDS):
                raise ValueError("invalid passive neighborhood consolidation delta")
            current = [previous[index] + delta[index] for index in range(len(delta))]
            values.append(current)
            previous = current
        return values
    return [
        [
            _safe_int(entry.get("checkpoint_index")),
            _safe_int(entry.get("pareto_depth")),
            _safe_int(entry.get("world_pair_count")),
            _safe_int(entry.get("world_count")),
            _safe_int(entry.get("growth_seen_count")),
        ]
        for entry in list(record.get("history", []) or [])
        if isinstance(entry, dict)
    ]


def _history_deltas(values: list[list[int]]) -> list[list[int]]:
    deltas = []
    previous = [0] * len(DELTA_FIELDS)
    for current in values:
        if len(current) != len(DELTA_FIELDS):
            raise ValueError("invalid passive neighborhood consolidation history")
        deltas.append(
            [current[index] - previous[index] for index in range(len(DELTA_FIELDS))]
        )
        previous = current
    return deltas


def _compact_relation(record: dict, symbol: str) -> dict:
    values = _numeric_history(record)
    return {
        "neighborhood_symbol": str(record.get("neighborhood_symbol", symbol) or symbol),
        "left_node": str(record.get("left_node", "") or ""),
        "right_node": str(record.get("right_node", "") or ""),
        "history_deltas": _history_deltas(values),
    }


def _expanded_relation(record: dict, store: dict, symbol: str) -> dict:
    checkpoints = _checkpoint_map(store)
    history = []
    for values in _numeric_history(record):
        checkpoint_index, depth, world_pairs, worlds, growth = values
        checkpoint = checkpoints.get(checkpoint_index, {})
        max_depth = _safe_int(checkpoint.get("max_pareto_depth")) or 1
        history.append(
            {
                "checkpoint_symbol": str(checkpoint.get("checkpoint_symbol", "") or ""),
                "checkpoint_index": checkpoint_index,
                "checkpoint_label": str(checkpoint.get("checkpoint_label", "") or ""),
                "run_index": _safe_int(checkpoint.get("run_index")),
                "pareto_depth": depth,
                "max_pareto_depth": max_depth,
                "normalized_depth": (depth - 1) / max(1, max_depth - 1),
                "world_pair_count": world_pairs,
                "world_count": worlds,
                "growth_seen_count": growth,
            }
        )
    latest = history[-1] if history else {}
    return {
        **PASSIVE_CONSOLIDATION_BOUNDARY,
        "neighborhood_symbol": str(record.get("neighborhood_symbol", symbol) or symbol),
        "left_node": str(record.get("left_node", "") or ""),
        "right_node": str(record.get("right_node", "") or ""),
        "first_checkpoint": _safe_int(history[0].get("checkpoint_index")) if history else 0,
        "last_checkpoint": _safe_int(latest.get("checkpoint_index")),
        "observed_checkpoint_count": len(history),
        "latest_pareto_depth": _safe_int(latest.get("pareto_depth")),
        "latest_normalized_depth": float(latest.get("normalized_depth", 0.0) or 0.0),
        "history": history,
    }


def passive_mcm_neighborhood_consolidation_relations(data: dict) -> dict[str, dict]:
    """Return expanded diagnostic records without expanding the stored document."""

    store = _store(data)
    return {
        str(symbol): _expanded_relation(dict(record or {}), store, str(symbol))
        for symbol, record in dict(store.get("relations", {}) or {}).items()
    }


def consolidate_passive_mcm_neighborhood_layers(
    data: dict,
    *,
    checkpoint_label: str,
    run_index: int = 0,
) -> dict:
    """Store one offline Pareto-depth checkpoint without changing source evidence."""

    label = str(checkpoint_label or "offline_checkpoint")
    symbol = _checkpoint_symbol(label, run_index)
    store = _store(data)
    if any(str(item.get("checkpoint_symbol", "")) == symbol for item in store["checkpoints"]):
        return passive_mcm_neighborhood_consolidation_profile(data)

    rows = _active_neighborhood_rows(data)
    depths = pareto_depths(rows)
    max_depth = max(depths.values(), default=1)
    checkpoint_index = len(store["checkpoints"]) + 1
    layer_counts: dict[str, int] = {}
    relations = {
        str(relation_symbol): _compact_relation(
            dict(record or {}), str(relation_symbol)
        )
        for relation_symbol, record in dict(store.get("relations", {}) or {}).items()
    }
    for row in rows:
        depth = depths[str(row["pair_key"])]
        layer_counts[str(depth)] = _safe_int(layer_counts.get(str(depth))) + 1
        relation_symbol = str(row["neighborhood_symbol"])
        relation = dict(relations.get(relation_symbol, {}) or {})
        if not relation:
            relation = {
                "neighborhood_symbol": relation_symbol,
                "left_node": row["left_node"],
                "right_node": row["right_node"],
                "history_deltas": [],
            }
        values = _numeric_history(relation)
        values.append(
            [
                checkpoint_index,
                depth,
                _safe_int(row["world_pair_count"]),
                _safe_int(row["world_count"]),
                _safe_int(row["growth_seen_count"]),
            ]
        )
        relation["history_deltas"] = _history_deltas(values)
        relations[relation_symbol] = relation

    store["relations"] = relations
    store["format"] = CONSOLIDATION_FORMAT
    store["checkpoints"] = [
        {
            key: value
            for key, value in dict(checkpoint or {}).items()
            if key not in PASSIVE_CONSOLIDATION_BOUNDARY
        }
        for checkpoint in store["checkpoints"]
    ]
    store["checkpoints"].append(
        {
            "checkpoint_symbol": symbol,
            "checkpoint_index": checkpoint_index,
            "checkpoint_label": label,
            "run_index": _safe_int(run_index),
            "relation_count": len(rows),
            "max_pareto_depth": max_depth,
            "layer_one_count": _safe_int(layer_counts.get("1")),
            "layer_counts": layer_counts,
        }
    )
    for key in (
        "latest_checkpoint_symbol",
        "latest_relation_count",
        "latest_max_pareto_depth",
        "latest_layer_one_count",
    ):
        store.pop(key, None)
    return passive_mcm_neighborhood_consolidation_profile(data)


def passive_mcm_neighborhood_consolidation_profile(data: dict) -> dict:
    store = _store(data)
    relations = dict(store.get("relations", {}) or {})
    checkpoints = list(store.get("checkpoints", []) or [])
    latest = dict(checkpoints[-1] or {}) if checkpoints else {}
    return {
        **PASSIVE_CONSOLIDATION_BOUNDARY,
        "format": str(store.get("format", CONSOLIDATION_FORMAT)),
        "checkpoints": len(checkpoints),
        "relations": len(relations),
        "history_entries": sum(
            len(_numeric_history(dict(record or {}))) for record in relations.values()
        ),
        "latest_relation_count": _safe_int(latest.get("relation_count")),
        "latest_max_pareto_depth": _safe_int(latest.get("max_pareto_depth")),
        "latest_layer_one_count": _safe_int(latest.get("layer_one_count")),
    }


def top_passive_mcm_neighborhood_consolidation(
    data: dict, limit: int = 8
) -> list[dict]:
    records = list(passive_mcm_neighborhood_consolidation_relations(data).values())
    records.sort(
        key=lambda record: (
            _safe_int(record.get("latest_pareto_depth")),
            -_safe_int(record.get("observed_checkpoint_count")),
            str(record.get("neighborhood_symbol", "")),
        ),
    )
    return records[: max(1, int(limit))]


__all__ = [
    "CONSOLIDATION_FORMAT",
    "PASSIVE_CONSOLIDATION_BOUNDARY",
    "SUPPORT_AXES",
    "consolidate_passive_mcm_neighborhood_layers",
    "pareto_depths",
    "passive_mcm_neighborhood_consolidation_profile",
    "passive_mcm_neighborhood_consolidation_relations",
    "top_passive_mcm_neighborhood_consolidation",
]
