from __future__ import annotations

import csv
import math
import random
import statistics
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
SOURCE_CSV = (
    FINDING_DIR
    / "2082_PASSIVE_OFFLINE_KONSOLIDIERUNG_MCM_NACHBARSCHAFT.histories.csv"
)
PREFIX = "2084_MCM_REIFUNGSBAHN_NACHBARSCHAFTEN"
SEQUENCES = ("forward", "reverse")
CHECKPOINTS = (10, 20, 40, 60, 81)
AXES = ("pareto_depth", "world_pair_count", "world_count", "growth_seen_count")
SCOPES = {
    "depth_rank_movement": (0,),
    "support_rank_movement": (1, 2, 3),
    "full_rank_movement": (0, 1, 2, 3),
}
PERMUTATIONS = 200
SEED = 2084


def _read_rows() -> list[dict[str, str]]:
    with SOURCE_CSV.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _by_relation(rows: list[dict[str, str]]) -> dict[tuple[str, str], list[dict[str, str]]]:
    out: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        out[(row["sequence"], row["pair_key"])].append(row)
    for history in out.values():
        history.sort(key=lambda row: int(row["run_index"]))
    return dict(out)


def _rank_maturity(values: list[float], *, higher_is_stronger: bool) -> list[float]:
    order = sorted(
        range(len(values)),
        key=lambda index: values[index],
        reverse=higher_is_stronger,
    )
    ranks = [0.0] * len(values)
    index = 0
    while index < len(order):
        end = index + 1
        while end < len(order) and values[order[end]] == values[order[index]]:
            end += 1
        average_rank = (index + end - 1) / 2.0
        maturity = 1.0 - (average_rank / max(1, len(values) - 1))
        for offset in range(index, end):
            ranks[order[offset]] = maturity
        index = end
    return ranks


def _ranked_observations(rows: list[dict[str, str]]) -> dict[tuple[str, str, int], list[float]]:
    checkpoints: dict[tuple[str, int], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        checkpoints[(row["sequence"], int(row["run_index"]))].append(row)
    out = {}
    for (sequence, checkpoint), group in checkpoints.items():
        axis_ranks = []
        for axis in AXES:
            axis_ranks.append(
                _rank_maturity(
                    [float(row[axis]) for row in group],
                    higher_is_stronger=axis != "pareto_depth",
                )
            )
        for index, row in enumerate(group):
            out[(sequence, row["pair_key"], checkpoint)] = [
                axis_ranks[axis][index] for axis in range(len(AXES))
            ]
    return out


def _signature(history: list[dict[str, str]]) -> tuple[int, ...]:
    return tuple(int(row["run_index"]) for row in history)


def _raw_fingerprint(history: list[dict[str, str]]) -> tuple[int, ...]:
    values = []
    for left, right in zip(history, history[1:]):
        values.extend(int(right[axis]) - int(left[axis]) for axis in AXES)
    return tuple(values)


def _trajectory_groups(
    relations: dict[tuple[str, str], list[dict[str, str]]],
    ranked: dict[tuple[str, str, int], list[float]],
    sequence: str,
    dimensions: tuple[int, ...],
) -> dict[tuple[int, ...], dict[str, list[float]]]:
    groups: dict[tuple[int, ...], dict[str, list[float]]] = defaultdict(dict)
    for (relation_sequence, pair_key), history in relations.items():
        if relation_sequence != sequence or len(history) < 2:
            continue
        signature = _signature(history)
        vector = []
        for left, right in zip(signature, signature[1:]):
            left_values = ranked[(sequence, pair_key, left)]
            right_values = ranked[(sequence, pair_key, right)]
            vector.extend(right_values[index] - left_values[index] for index in dimensions)
        groups[signature][pair_key] = vector
    return dict(groups)


def _distance(left: list[float], right: list[float]) -> float:
    return math.sqrt(
        sum((left[index] - right[index]) ** 2 for index in range(len(left)))
        / max(1, len(left))
    )


def _mutual_nearest_edges(
    groups: dict[tuple[int, ...], dict[str, list[float]]]
) -> tuple[set[tuple[str, str]], set[tuple[str, str]]]:
    edges: set[tuple[str, str]] = set()
    zero_distance_edges: set[tuple[str, str]] = set()
    for vectors in groups.values():
        keys = sorted(vectors)
        nearest: dict[str, set[str]] = {}
        minimums: dict[str, float] = {}
        for left in keys:
            distances = [
                (_distance(vectors[left], vectors[right]), right)
                for right in keys
                if right != left
            ]
            if not distances:
                continue
            minimum = min(value for value, _ in distances)
            minimums[left] = minimum
            nearest[left] = {
                right for value, right in distances if abs(value - minimum) <= 1e-12
            }
        for left, neighbors in nearest.items():
            for right in neighbors:
                edge = tuple(sorted((left, right)))
                if left in nearest.get(right, set()) and edge not in edges:
                    edges.add(edge)
                    if abs(minimums[left]) <= 1e-12:
                        zero_distance_edges.add(edge)
    return edges, zero_distance_edges


def _raw_classes(
    relations: dict[tuple[str, str], list[dict[str, str]]], sequence: str
) -> dict[tuple[int, ...], dict[tuple[int, ...], list[str]]]:
    classes: dict[tuple[int, ...], dict[tuple[int, ...], list[str]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for (relation_sequence, pair_key), history in relations.items():
        if relation_sequence == sequence and len(history) >= 2:
            classes[_signature(history)][_raw_fingerprint(history)].append(pair_key)
    return {signature: dict(group) for signature, group in classes.items()}


def _raw_equivalence_edges(
    classes: dict[tuple[int, ...], dict[tuple[int, ...], list[str]]]
) -> set[tuple[str, str]]:
    return {
        tuple(sorted(edge))
        for signature_classes in classes.values()
        for members in signature_classes.values()
        for edge in combinations(members, 2)
    }


def _coverage_rows(
    relations: dict[tuple[str, str], list[dict[str, str]]]
) -> list[dict[str, object]]:
    rows = []
    for sequence in SEQUENCES:
        for signature, classes in sorted(
            _raw_classes(relations, sequence).items(), key=lambda item: len(item[0])
        ):
            sizes = sorted((len(members) for members in classes.values()), reverse=True)
            relation_count = sum(sizes)
            rows.append(
                {
                    "sequence": sequence,
                    "checkpoint_signature": "-".join(str(value) for value in signature),
                    "trajectory_points": len(signature),
                    "relations": relation_count,
                    "exact_raw_fingerprints": len(sizes),
                    "singleton_fingerprints": sum(size == 1 for size in sizes),
                    "largest_exact_class": max(sizes, default=0),
                    "largest_exact_class_share": max(sizes, default=0)
                    / max(1, relation_count),
                    "raw_equivalence_edges": sum(
                        size * (size - 1) // 2 for size in sizes
                    ),
                }
            )
    return rows


def _identity_rows(
    relations: dict[tuple[str, str], list[dict[str, str]]]
) -> list[dict[str, object]]:
    forward = {
        pair_key: history
        for (sequence, pair_key), history in relations.items()
        if sequence == "forward"
    }
    reverse = {
        pair_key: history
        for (sequence, pair_key), history in relations.items()
        if sequence == "reverse"
    }
    shared = set(forward) & set(reverse)
    rows = []
    for length in range(2, len(CHECKPOINTS) + 1):
        same_signature = [
            pair_key
            for pair_key in shared
            if len(forward[pair_key]) == length
            and _signature(forward[pair_key]) == _signature(reverse[pair_key])
        ]
        exact = sum(
            _raw_fingerprint(forward[pair_key]) == _raw_fingerprint(reverse[pair_key])
            for pair_key in same_signature
        )
        rows.append(
            {
                "trajectory_points": length,
                "same_signature_relations": len(same_signature),
                "exact_raw_fingerprint_matches": exact,
                "exact_match_share": exact / max(1, len(same_signature)),
            }
        )
    total_relations = sum(int(row["same_signature_relations"]) for row in rows)
    total_exact = sum(int(row["exact_raw_fingerprint_matches"]) for row in rows)
    rows.append(
        {
            "trajectory_points": "all",
            "same_signature_relations": total_relations,
            "exact_raw_fingerprint_matches": total_exact,
            "exact_match_share": total_exact / max(1, total_relations),
        }
    )
    return rows


def _graph_rows(
    edges: dict[tuple[str, str], set[tuple[str, str]]],
    zero_edges: dict[tuple[str, str], set[tuple[str, str]]],
) -> list[dict[str, object]]:
    rows = []
    for sequence in SEQUENCES:
        for scope in ("raw_equal", *SCOPES, "robust"):
            graph = edges[(sequence, scope)]
            nodes = {node for edge in graph for node in edge}
            rows.append(
                {
                    "sequence": sequence,
                    "scope": scope,
                    "edges": len(graph),
                    "nodes": len(nodes),
                    "mean_degree": (2 * len(graph)) / max(1, len(nodes)),
                    "zero_distance_edges": len(zero_edges.get((sequence, scope), set())),
                }
            )
    return rows


def _order_rows(
    edges: dict[tuple[str, str], set[tuple[str, str]]]
) -> list[dict[str, object]]:
    rows = []
    for scope in ("raw_equal", *SCOPES, "robust"):
        forward = edges[("forward", scope)]
        reverse = edges[("reverse", scope)]
        shared = forward & reverse
        rows.append(
            {
                "scope": scope,
                "forward_edges": len(forward),
                "reverse_edges": len(reverse),
                "shared_edges": len(shared),
                "edge_jaccard": len(shared) / max(1, len(forward | reverse)),
            }
        )
    return rows


def _permutation_rows(
    relations: dict[tuple[str, str], list[dict[str, str]]],
    reverse_groups: dict[tuple[int, ...], dict[str, list[float]]],
    edges: dict[tuple[str, str], set[tuple[str, str]]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rng = random.Random(SEED)
    reverse_members = {
        signature: sorted(vectors) for signature, vectors in reverse_groups.items()
    }
    scopes = ("raw_equal", *SCOPES, "robust")
    null_shared = {scope: [] for scope in scopes}
    same_length_nodes = {}
    for length in range(2, len(CHECKPOINTS) + 1):
        same_length_nodes[length] = {
            pair_key
            for (sequence, pair_key), history in relations.items()
            if sequence == "forward"
            and len(history) == length
            and len(relations.get(("reverse", pair_key), [])) == length
        }
    longevity_scopes = ("raw_equal", "robust")
    longevity_null = {
        (scope, length): []
        for scope in longevity_scopes
        for length in same_length_nodes
    }

    for _ in range(PERMUTATIONS):
        mapping = {}
        for members in reverse_members.values():
            shuffled = members[:]
            rng.shuffle(shuffled)
            mapping.update(zip(members, shuffled))
        for scope in scopes:
            permuted = {
                tuple(sorted((mapping[left], mapping[right])))
                for left, right in edges[("reverse", scope)]
            }
            null_shared[scope].append(len(edges[("forward", scope)] & permuted))
            if scope in longevity_scopes:
                for length, nodes in same_length_nodes.items():
                    forward_subset = {
                        edge
                        for edge in edges[("forward", scope)]
                        if edge[0] in nodes and edge[1] in nodes
                    }
                    permuted_subset = {
                        edge for edge in permuted if edge[0] in nodes and edge[1] in nodes
                    }
                    longevity_null[(scope, length)].append(
                        len(forward_subset & permuted_subset)
                    )

    null_rows = []
    for scope in scopes:
        forward = edges[("forward", scope)]
        reverse = edges[("reverse", scope)]
        observed = len(forward & reverse)
        values = null_shared[scope]
        mean = statistics.mean(values)
        deviation = statistics.pstdev(values)
        null_rows.append(
            {
                "scope": scope,
                "permutations": PERMUTATIONS,
                "seed": SEED,
                "observed_shared_edges": observed,
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
        )

    longevity_rows = []
    for scope in longevity_scopes:
        for length, nodes in same_length_nodes.items():
            forward = {
                edge
                for edge in edges[("forward", scope)]
                if edge[0] in nodes and edge[1] in nodes
            }
            reverse = {
                edge
                for edge in edges[("reverse", scope)]
                if edge[0] in nodes and edge[1] in nodes
            }
            observed = len(forward & reverse)
            values = longevity_null[(scope, length)]
            mean = statistics.mean(values)
            longevity_rows.append(
                {
                    "scope": scope,
                    "trajectory_points_in_both_sequences": length,
                    "eligible_relations": len(nodes),
                    "forward_edges": len(forward),
                    "reverse_edges": len(reverse),
                    "shared_edges": observed,
                    "edge_jaccard": observed / max(1, len(forward | reverse)),
                    "null_mean_shared_edges": mean,
                    "observed_to_null_ratio": observed / max(1e-12, mean),
                    "empirical_p_ge_observed": (
                        1 + sum(value >= observed for value in values)
                    )
                    / (PERMUTATIONS + 1),
                }
            )
    return null_rows, longevity_rows


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    rows = _read_rows()
    relations = _by_relation(rows)
    ranked = _ranked_observations(rows)
    edges: dict[tuple[str, str], set[tuple[str, str]]] = {}
    zero_edges: dict[tuple[str, str], set[tuple[str, str]]] = {}
    trajectory_groups = {}
    for sequence in SEQUENCES:
        for scope, dimensions in SCOPES.items():
            groups = _trajectory_groups(relations, ranked, sequence, dimensions)
            trajectory_groups[(sequence, scope)] = groups
            graph, zero_count = _mutual_nearest_edges(groups)
            edges[(sequence, scope)] = graph
            zero_edges[(sequence, scope)] = zero_count
        edges[(sequence, "robust")] = set.intersection(
            *(edges[(sequence, scope)] for scope in SCOPES)
        )
        zero_edges[(sequence, "robust")] = set.intersection(
            *(zero_edges[(sequence, scope)] for scope in SCOPES)
        )
        raw_classes = _raw_classes(relations, sequence)
        edges[(sequence, "raw_equal")] = _raw_equivalence_edges(raw_classes)
        zero_edges[(sequence, "raw_equal")] = set(edges[(sequence, "raw_equal")])

    coverage_rows = _coverage_rows(relations)
    identity_rows = _identity_rows(relations)
    graph_rows = _graph_rows(edges, zero_edges)
    order_rows = _order_rows(edges)
    null_rows, longevity_rows = _permutation_rows(
        relations,
        trajectory_groups[("reverse", "full_rank_movement")],
        edges,
    )
    robust_order = next(row for row in order_rows if row["scope"] == "robust")
    robust_null = next(row for row in null_rows if row["scope"] == "robust")
    identity_total = identity_rows[-1]
    full_length = next(
        row
        for row in longevity_rows
        if row["scope"] == "robust"
        and row["trajectory_points_in_both_sequences"] == len(CHECKPOINTS)
    )
    summary_rows = [
        {
            "forward_movement_relations": sum(
                len(group)
                for group in trajectory_groups[("forward", "full_rank_movement")].values()
            ),
            "reverse_movement_relations": sum(
                len(group)
                for group in trajectory_groups[("reverse", "full_rank_movement")].values()
            ),
            "shared_movement_relations": sum(
                len(forward) >= 2 and len(relations.get(("reverse", pair_key), [])) >= 2
                for (sequence, pair_key), forward in relations.items()
                if sequence == "forward"
            ),
            "same_signature_relations": identity_total["same_signature_relations"],
            "exact_raw_fingerprint_matches": identity_total[
                "exact_raw_fingerprint_matches"
            ],
            "forward_robust_edges": robust_order["forward_edges"],
            "reverse_robust_edges": robust_order["reverse_edges"],
            "shared_robust_edges": robust_order["shared_edges"],
            "robust_edge_jaccard": robust_order["edge_jaccard"],
            "robust_null_mean_shared_edges": robust_null["null_mean_shared_edges"],
            "robust_observed_to_null_ratio": robust_null["observed_to_null_ratio"],
            "robust_empirical_p": robust_null["empirical_p_ge_observed"],
            "full_length_relations_in_both": full_length["eligible_relations"],
            "full_length_shared_robust_edges": full_length["shared_edges"],
            "full_length_robust_jaccard": full_length["edge_jaccard"],
            "full_length_observed_to_null_ratio": full_length[
                "observed_to_null_ratio"
            ],
            "read_by_mini_dio": 0,
            "influences_field": 0,
            "influences_action": 0,
        }
    ]

    _write_csv("coverage", coverage_rows)
    _write_csv("identity", identity_rows)
    _write_csv("graphs", graph_rows)
    _write_csv("order", order_rows)
    _write_csv("null", null_rows)
    _write_csv("longevity", longevity_rows)
    _write_csv("summary", summary_rows)
    print(f"coverage_rows={len(coverage_rows)}")
    print(f"graph_rows={len(graph_rows)}")
    print(f"null_rows={len(null_rows)}")
    print(f"longevity_rows={len(longevity_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
