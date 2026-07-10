from __future__ import annotations

import csv
import random
import statistics
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_maturation_trajectory_neighborhoods import _mutual_nearest_edges
from tools.run_mcm_relation_age_trajectory_neighborhoods import (
    _eligible_vectors,
    _event_histories,
    _rank_vectors,
    SCOPES,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2087_MCM_EIGENZEIT_KANTENPERSISTENZ"
OFFLINE_LINK_CSV = (
    FINDING_DIR / "2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.links.csv"
)
AGES = (3, 5, 10)
TRANSITIONS = ((3, 5), (5, 10), (3, 10))
SEQUENCES = ("forward", "reverse")
PERSISTENCE_SCOPES = ("event_cadence", "breadth_growth", "profile_growth")
PERMUTATIONS = 200
SEED = 2087


def _restricted_edges(
    edges: set[tuple[str, str]], nodes: set[str]
) -> set[tuple[str, str]]:
    return {edge for edge in edges if edge[0] in nodes and edge[1] in nodes}


def _persistent_edges(
    graphs: list[set[tuple[str, str]]], nodes: set[str]
) -> set[tuple[str, str]]:
    restricted = [_restricted_edges(graph, nodes) for graph in graphs]
    return set.intersection(*restricted) if restricted else set()


def _connected_components(edges: set[tuple[str, str]]) -> list[set[str]]:
    neighbors: dict[str, set[str]] = {}
    for left, right in edges:
        neighbors.setdefault(left, set()).add(right)
        neighbors.setdefault(right, set()).add(left)
    components = []
    pending = set(neighbors)
    while pending:
        start = min(pending)
        component = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in component:
                continue
            component.add(node)
            stack.extend(neighbors.get(node, set()) - component)
        pending -= component
        components.append(component)
    components.sort(key=lambda component: (-len(component), sorted(component)))
    return components


def _strict_core() -> set[str]:
    core = set()
    with OFFLINE_LINK_CSV.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if (
                int(row["real_2025_all_scopes"]) > 0
                and int(row["real_crossyear_all_scopes"]) > 0
                and int(row["real_2024_all_scopes"]) > 0
            ):
                core.add("|".join(sorted((row["left_node"], row["right_node"]))))
    return core


def _permuted_edges(
    edges: set[tuple[str, str]], members: list[str], rng: random.Random
) -> set[tuple[str, str]]:
    shuffled = members[:]
    rng.shuffle(shuffled)
    mapping = dict(zip(members, shuffled))
    return {
        tuple(sorted((mapping[left], mapping[right]))) for left, right in edges
    }


def _null_metrics(observed: int, values: list[int]) -> dict[str, float | int]:
    mean = statistics.mean(values)
    deviation = statistics.pstdev(values)
    return {
        "null_mean_shared_edges": mean,
        "null_sd_shared_edges": deviation,
        "null_max_shared_edges": max(values),
        "observed_to_null_ratio": observed / max(1e-12, mean),
        "z_score": (observed - mean) / max(1e-12, deviation),
        "empirical_p_ge_observed": (
            1 + sum(value >= observed for value in values)
        )
        / (PERMUTATIONS + 1),
    }


def _transition_rows(
    vectors: dict[tuple[str, int], dict[str, tuple[int, ...]]],
    edges: dict[tuple[str, int, str], set[tuple[str, str]]],
    rng: random.Random,
) -> list[dict[str, object]]:
    rows = []
    for sequence in SEQUENCES:
        for scope in PERSISTENCE_SCOPES:
            for from_age, to_age in TRANSITIONS:
                members = sorted(vectors[(sequence, to_age)])
                nodes = set(members)
                earlier = _restricted_edges(edges[(sequence, from_age, scope)], nodes)
                later = _restricted_edges(edges[(sequence, to_age, scope)], nodes)
                shared = earlier & later
                null_values = []
                for _ in range(PERMUTATIONS):
                    permuted = _permuted_edges(later, members, rng)
                    null_values.append(len(earlier & permuted))
                rows.append(
                    {
                        "sequence": sequence,
                        "scope": scope,
                        "from_age": from_age,
                        "to_age": to_age,
                        "surviving_relations": len(nodes),
                        "from_edges_on_survivors": len(earlier),
                        "to_edges": len(later),
                        "persistent_edges": len(shared),
                        "persistent_nodes": len(
                            {node for edge in shared for node in edge}
                        ),
                        "edge_jaccard": len(shared) / max(1, len(earlier | later)),
                        "from_edge_retention": len(shared) / max(1, len(earlier)),
                        "permutations": PERMUTATIONS,
                        "seed": SEED,
                        **_null_metrics(len(shared), null_values),
                    }
                )
    return rows


def _persistence_rows(
    vectors: dict[tuple[str, int], dict[str, tuple[int, ...]]],
    edges: dict[tuple[str, int, str], set[tuple[str, str]]],
    rng: random.Random,
) -> tuple[list[dict[str, object]], dict[tuple[str, str], set[tuple[str, str]]]]:
    rows = []
    persistent: dict[tuple[str, str], set[tuple[str, str]]] = {}
    for sequence in SEQUENCES:
        members = sorted(vectors[(sequence, 10)])
        nodes = set(members)
        for scope in PERSISTENCE_SCOPES:
            restricted = [
                _restricted_edges(edges[(sequence, age, scope)], nodes) for age in AGES
            ]
            stable = set.intersection(*restricted)
            persistent[(sequence, scope)] = stable
            null_values = []
            for _ in range(PERMUTATIONS):
                permuted_age5 = _permuted_edges(restricted[1], members, rng)
                permuted_age10 = _permuted_edges(restricted[2], members, rng)
                null_values.append(
                    len(restricted[0] & permuted_age5 & permuted_age10)
                )
            union = set.union(*restricted)
            rows.append(
                {
                    "sequence": sequence,
                    "scope": scope,
                    "age10_relations": len(nodes),
                    "age3_edges_on_age10_relations": len(restricted[0]),
                    "age5_edges_on_age10_relations": len(restricted[1]),
                    "age10_edges": len(restricted[2]),
                    "persistent_edges_3_5_10": len(stable),
                    "persistent_nodes_3_5_10": len(
                        {node for edge in stable for node in edge}
                    ),
                    "three_age_jaccard": len(stable) / max(1, len(union)),
                    "age3_edge_retention": len(stable) / max(1, len(restricted[0])),
                    "permutations": PERMUTATIONS,
                    "seed": SEED,
                    **_null_metrics(len(stable), null_values),
                }
            )
    return rows, persistent


def _order_rows(
    persistent: dict[tuple[str, str], set[tuple[str, str]]],
    rng: random.Random,
) -> list[dict[str, object]]:
    rows = []
    for scope in PERSISTENCE_SCOPES:
        forward = persistent[("forward", scope)]
        reverse = persistent[("reverse", scope)]
        shared = forward & reverse
        reverse_members = sorted({node for edge in reverse for node in edge})
        null_values = []
        if reverse_members:
            for _ in range(PERMUTATIONS):
                permuted = _permuted_edges(reverse, reverse_members, rng)
                null_values.append(len(forward & permuted))
        else:
            null_values = [0] * PERMUTATIONS
        rows.append(
            {
                "scope": scope,
                "forward_persistent_edges": len(forward),
                "reverse_persistent_edges": len(reverse),
                "shared_persistent_edges": len(shared),
                "shared_persistent_nodes": len(
                    {node for edge in shared for node in edge}
                ),
                "persistent_edge_jaccard": len(shared)
                / max(1, len(forward | reverse)),
                "permutations": PERMUTATIONS,
                "seed": SEED,
                **_null_metrics(len(shared), null_values),
                "read_by_mini_dio": 0,
                "influences_field": 0,
                "influences_action": 0,
            }
        )
    return rows


def _component_rows(
    persistent: dict[tuple[str, str], set[tuple[str, str]]]
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    strict_core = _strict_core()
    shared_edges = {
        scope: persistent[("forward", scope)] & persistent[("reverse", scope)]
        for scope in PERSISTENCE_SCOPES
    }
    rows = []
    scope_nodes = {}
    for scope in PERSISTENCE_SCOPES:
        scope_nodes[scope] = {node for edge in shared_edges[scope] for node in edge}
        for index, component in enumerate(
            _connected_components(shared_edges[scope]), start=1
        ):
            component_edges = _restricted_edges(shared_edges[scope], component)
            maximum_edges = len(component) * (len(component) - 1) // 2
            rows.append(
                {
                    "scope": scope,
                    "component_index": index,
                    "relations": len(component),
                    "edges": len(component_edges),
                    "complete_clique": int(len(component_edges) == maximum_edges),
                    "strict_2078_core_relations": len(component & strict_core),
                    "members": ";".join(sorted(component)),
                }
            )
    overlap_rows = []
    for left_index, left_scope in enumerate(PERSISTENCE_SCOPES):
        for right_scope in PERSISTENCE_SCOPES[left_index + 1 :]:
            left = scope_nodes[left_scope]
            right = scope_nodes[right_scope]
            overlap_rows.append(
                {
                    "left_scope": left_scope,
                    "right_scope": right_scope,
                    "left_relations": len(left),
                    "right_relations": len(right),
                    "shared_relations": len(left & right),
                    "relation_jaccard": len(left & right) / max(1, len(left | right)),
                }
            )
    return rows, overlap_rows


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    histories = _event_histories()
    vectors = {
        (sequence, age): _eligible_vectors(histories, sequence, age)
        for sequence in SEQUENCES
        for age in AGES
    }
    edges: dict[tuple[str, int, str], set[tuple[str, str]]] = {}
    for sequence in SEQUENCES:
        for age in AGES:
            for scope in PERSISTENCE_SCOPES:
                ranked = _rank_vectors(vectors[(sequence, age)], SCOPES[scope])
                graph, _ = _mutual_nearest_edges({(age,): ranked})
                edges[(sequence, age, scope)] = graph

    rng = random.Random(SEED)
    transition_rows = _transition_rows(vectors, edges, rng)
    persistence_rows, persistent = _persistence_rows(vectors, edges, rng)
    order_rows = _order_rows(persistent, rng)
    component_rows, overlap_rows = _component_rows(persistent)
    _write_csv("transitions", transition_rows)
    _write_csv("persistence", persistence_rows)
    _write_csv("order", order_rows)
    _write_csv("components", component_rows)
    _write_csv("overlap", overlap_rows)
    _write_csv("summary", order_rows)
    print(f"transition_rows={len(transition_rows)}")
    print(f"persistence_rows={len(persistence_rows)}")
    print(f"order_rows={len(order_rows)}")
    print(f"component_rows={len(component_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
