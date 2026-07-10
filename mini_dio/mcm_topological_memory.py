"""Passive online topology built from completed inner MCM field episodes."""

from __future__ import annotations

from mini_dio.dio_syntax import make_mcm_field_episode_symbol


PASSIVE_BOUNDARY = {
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

METRIC_FIELDS = (
    "avg_mcm_carry_quality",
    "avg_mcm_strain_quality",
    "avg_mcm_rekopplung_quality",
    "avg_mcm_adaptive_rekopplung_quality",
    "avg_sensory_coupling",
    "avg_visual_field_gap",
    "avg_hearing_field_gap",
)


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if result != result else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def _mean_update(previous: object, value: object, seen_count: int) -> float:
    current = _safe_float(value)
    if seen_count <= 1:
        return current
    return ((_safe_float(previous) * (seen_count - 1)) + current) / seen_count


def _topology(data: dict) -> dict:
    topology = data.setdefault("passive_mcm_topology", {})
    if not isinstance(topology, dict):
        topology = {}
        data["passive_mcm_topology"] = topology
    if not isinstance(topology.get("nodes"), dict):
        topology["nodes"] = {}
    if not isinstance(topology.get("edges"), dict):
        topology["edges"] = {}
    topology.update(PASSIVE_BOUNDARY)
    return topology


def _edge_symbol(source: str, target: str) -> str:
    hash_value = 2166136261
    for char in f"{source}->{target}":
        hash_value ^= ord(char) + 97
        hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    encoded = "0"
    if hash_value:
        parts: list[str] = []
        while hash_value:
            hash_value, remainder = divmod(hash_value, 36)
            parts.append(alphabet[remainder])
        encoded = "".join(reversed(parts))
    return f"dio_mcm_edge_{encoded.rjust(7, '0')}"


def _observe_context(record: dict, world: str, carrier_family: str) -> None:
    world = str(world or "").strip()
    if world:
        worlds = record.setdefault("world_observations", {})
        worlds[world] = _safe_int(worlds.get(world)) + 1
        record["world_count"] = len(worlds)
    carrier_family = str(carrier_family or "").strip()
    if carrier_family and carrier_family != "-":
        carriers = record.setdefault("carrier_observations", {})
        carriers[carrier_family] = _safe_int(carriers.get(carrier_family)) + 1
        record["carrier_family_count"] = len(carriers)


def store_passive_mcm_topology_episode(
    data: dict,
    payload: dict,
    *,
    previous_node_symbol: str = "",
    world: str = "",
    run_index: int = 0,
) -> dict:
    """Grow one node and its directed predecessor edge from an inner episode."""

    if not isinstance(payload, dict) or not payload:
        return {"node_symbol": "", "edge_symbol": ""}

    topology = _topology(data)
    nodes = topology["nodes"]
    edges = topology["edges"]
    node_symbol = make_mcm_field_episode_symbol(payload)
    node = dict(nodes.get(node_symbol, {}) or {})
    seen_count = _safe_int(node.get("seen_count")) + 1
    node.update(
        {
            **PASSIVE_BOUNDARY,
            "node_symbol": node_symbol,
            "episode_state": str(payload.get("episode_state", "") or ""),
            "base_field_effect_state": str(payload.get("base_field_effect_state", "") or ""),
            "passive_mcm_effect_class": str(payload.get("passive_mcm_effect_class", "") or ""),
            "seen_count": seen_count,
            "avg_duration": _mean_update(node.get("avg_duration"), payload.get("duration"), seen_count),
            "first_run": _safe_int(node.get("first_run")) or _safe_int(run_index),
            "last_run": _safe_int(run_index),
            "last_start_tick": _safe_int(payload.get("start_tick")),
            "last_end_tick": _safe_int(payload.get("end_tick")),
            "incoming_observations": _safe_int(node.get("incoming_observations")),
            "outgoing_observations": _safe_int(node.get("outgoing_observations")),
        }
    )
    for key in METRIC_FIELDS:
        node[key] = _mean_update(node.get(key), payload.get(key), seen_count)
    _observe_context(node, world, str(payload.get("dominant_family", "") or ""))
    nodes[node_symbol] = node

    source_symbol = str(previous_node_symbol or "").strip()
    edge_symbol = ""
    if source_symbol:
        edge_symbol = _edge_symbol(source_symbol, node_symbol)
        edge = dict(edges.get(edge_symbol, {}) or {})
        edge_seen = _safe_int(edge.get("seen_count")) + 1
        edge.update(
            {
                **PASSIVE_BOUNDARY,
                "edge_symbol": edge_symbol,
                "source_node": source_symbol,
                "target_node": node_symbol,
                "seen_count": edge_seen,
                "avg_target_duration": _mean_update(
                    edge.get("avg_target_duration"), payload.get("duration"), edge_seen
                ),
                "first_run": _safe_int(edge.get("first_run")) or _safe_int(run_index),
                "last_run": _safe_int(run_index),
                "last_tick": _safe_int(payload.get("end_tick")),
            }
        )
        for key in METRIC_FIELDS:
            edge[f"target_{key}"] = _mean_update(
                edge.get(f"target_{key}"), payload.get(key), edge_seen
            )
        _observe_context(edge, world, str(payload.get("dominant_family", "") or ""))
        edges[edge_symbol] = edge

        node["incoming_observations"] = _safe_int(node.get("incoming_observations")) + 1
        source_node = dict(nodes.get(source_symbol, {}) or {})
        if source_node:
            source_node["outgoing_observations"] = _safe_int(
                source_node.get("outgoing_observations")
            ) + 1
            nodes[source_symbol] = source_node
        nodes[node_symbol] = node

    topology["node_observations"] = _safe_int(topology.get("node_observations")) + 1
    if edge_symbol:
        topology["edge_observations"] = _safe_int(topology.get("edge_observations")) + 1
    topology["last_node_symbol"] = node_symbol
    topology["last_edge_symbol"] = edge_symbol
    return {"node_symbol": node_symbol, "edge_symbol": edge_symbol}


def passive_mcm_topology_profile(data: dict) -> dict:
    topology = _topology(data)
    nodes = topology["nodes"]
    edges = topology["edges"]
    node_observations = sum(_safe_int(item.get("seen_count")) for item in nodes.values())
    edge_observations = sum(_safe_int(item.get("seen_count")) for item in edges.values())
    return {
        **PASSIVE_BOUNDARY,
        "nodes": len(nodes),
        "edges": len(edges),
        "node_observations": node_observations,
        "edge_observations": edge_observations,
        "node_return_observations": max(0, node_observations - len(nodes)),
        "edge_return_observations": max(0, edge_observations - len(edges)),
    }


def top_passive_mcm_topology_nodes(data: dict, limit: int = 8) -> list[dict]:
    nodes = list(_topology(data)["nodes"].values())
    nodes.sort(
        key=lambda item: (
            _safe_int(item.get("seen_count")),
            _safe_int(item.get("world_count")),
            _safe_int(item.get("incoming_observations")) + _safe_int(item.get("outgoing_observations")),
        ),
        reverse=True,
    )
    return nodes[: max(1, int(limit))]


def top_passive_mcm_topology_edges(data: dict, limit: int = 8) -> list[dict]:
    edges = list(_topology(data)["edges"].values())
    edges.sort(
        key=lambda item: (
            _safe_int(item.get("seen_count")),
            _safe_int(item.get("world_count")),
        ),
        reverse=True,
    )
    return edges[: max(1, int(limit))]


__all__ = [
    "PASSIVE_BOUNDARY",
    "passive_mcm_topology_profile",
    "store_passive_mcm_topology_episode",
    "top_passive_mcm_topology_edges",
    "top_passive_mcm_topology_nodes",
]
