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
SUPPORT_AXES = ("world_pair_count", "world_count", "growth_seen_count")


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
    relations = dict(store.get("relations", {}) or {})
    for row in rows:
        depth = depths[str(row["pair_key"])]
        normalized_depth = (depth - 1) / max(1, max_depth - 1)
        layer_counts[str(depth)] = _safe_int(layer_counts.get(str(depth))) + 1
        relation_symbol = str(row["neighborhood_symbol"])
        relation = dict(relations.get(relation_symbol, {}) or {})
        history = list(relation.get("history", []) or [])
        history.append(
            {
                "checkpoint_symbol": symbol,
                "checkpoint_index": checkpoint_index,
                "checkpoint_label": label,
                "run_index": _safe_int(run_index),
                "pareto_depth": depth,
                "max_pareto_depth": max_depth,
                "normalized_depth": normalized_depth,
                "world_pair_count": _safe_int(row["world_pair_count"]),
                "world_count": _safe_int(row["world_count"]),
                "growth_seen_count": _safe_int(row["growth_seen_count"]),
            }
        )
        relation.update(
            {
                **PASSIVE_CONSOLIDATION_BOUNDARY,
                "neighborhood_symbol": relation_symbol,
                "left_node": row["left_node"],
                "right_node": row["right_node"],
                "first_checkpoint": _safe_int(relation.get("first_checkpoint"))
                or checkpoint_index,
                "last_checkpoint": checkpoint_index,
                "observed_checkpoint_count": len(history),
                "latest_pareto_depth": depth,
                "latest_normalized_depth": normalized_depth,
                "history": history,
            }
        )
        relations[relation_symbol] = relation

    store["relations"] = relations
    store["checkpoints"].append(
        {
            **PASSIVE_CONSOLIDATION_BOUNDARY,
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
    store["latest_checkpoint_symbol"] = symbol
    store["latest_relation_count"] = len(rows)
    store["latest_max_pareto_depth"] = max_depth
    store["latest_layer_one_count"] = _safe_int(layer_counts.get("1"))
    return passive_mcm_neighborhood_consolidation_profile(data)


def passive_mcm_neighborhood_consolidation_profile(data: dict) -> dict:
    store = _store(data)
    relations = dict(store.get("relations", {}) or {})
    return {
        **PASSIVE_CONSOLIDATION_BOUNDARY,
        "checkpoints": len(list(store.get("checkpoints", []) or [])),
        "relations": len(relations),
        "history_entries": sum(
            len(list(dict(record or {}).get("history", []) or []))
            for record in relations.values()
        ),
        "latest_relation_count": _safe_int(store.get("latest_relation_count")),
        "latest_max_pareto_depth": _safe_int(store.get("latest_max_pareto_depth")),
        "latest_layer_one_count": _safe_int(store.get("latest_layer_one_count")),
    }


def top_passive_mcm_neighborhood_consolidation(
    data: dict, limit: int = 8
) -> list[dict]:
    records = [
        dict(record or {})
        for record in dict(_store(data).get("relations", {}) or {}).values()
    ]
    records.sort(
        key=lambda record: (
            _safe_int(record.get("latest_pareto_depth")),
            -_safe_int(record.get("observed_checkpoint_count")),
            str(record.get("neighborhood_symbol", "")),
        ),
    )
    return records[: max(1, int(limit))]


__all__ = [
    "PASSIVE_CONSOLIDATION_BOUNDARY",
    "SUPPORT_AXES",
    "consolidate_passive_mcm_neighborhood_layers",
    "pareto_depths",
    "passive_mcm_neighborhood_consolidation_profile",
    "top_passive_mcm_neighborhood_consolidation",
]
