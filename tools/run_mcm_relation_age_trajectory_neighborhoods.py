from __future__ import annotations

import csv
import io
import random
import statistics
import sys
import zipfile
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_maturation_trajectory_neighborhoods import (
    _mutual_nearest_edges,
    _rank_maturity,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
EVENT_ARCHIVE = ROOT / "data" / "2085_mcm_neighborhood_event_histories.zip"
PREFIX = "2086_MCM_EIGENZEIT_BEWEGUNGSNACHBARSCHAFTEN"
AGES = (2, 3, 5, 10)
SEQUENCES = ("forward", "reverse")
FIELDS = (
    "finalization_index",
    "world_pair_count",
    "world_count",
    "field_core_raw",
    "field_full_raw",
    "field_full_plus_duration_standardized",
)
SCOPES = {
    "event_cadence": (0,),
    "breadth_growth": (1, 2),
    "profile_growth": (3, 4, 5),
    "full_movement": (0, 1, 2, 3, 4, 5),
}
ROBUST_SCOPES = ("event_cadence", "breadth_growth", "profile_growth")
PERMUTATIONS = 200
SEED = 2086


def _event_histories() -> dict[tuple[str, str], list[dict[str, int]]]:
    histories: dict[tuple[str, str], list[dict[str, int]]] = defaultdict(list)
    with zipfile.ZipFile(EVENT_ARCHIVE) as archive:
        with archive.open("event_histories.csv") as raw_handle:
            handle = io.TextIOWrapper(raw_handle, encoding="utf-8", newline="")
            for row in csv.DictReader(handle):
                histories[(row["sequence"], row["pair_key"])].append(
                    {
                        "event_index": int(row["event_index"]),
                        **{field: int(row[field]) for field in FIELDS},
                    }
                )
    for history in histories.values():
        history.sort(key=lambda event: event["event_index"])
    return dict(histories)


def _prefix_vector(history: list[dict[str, int]], age: int) -> tuple[int, ...]:
    prefix = history[:age]
    values = []
    for left, right in zip(prefix, prefix[1:]):
        values.extend(right[field] - left[field] for field in FIELDS)
    return tuple(values)


def _eligible_vectors(
    histories: dict[tuple[str, str], list[dict[str, int]]],
    sequence: str,
    age: int,
) -> dict[str, tuple[int, ...]]:
    return {
        pair_key: _prefix_vector(history, age)
        for (relation_sequence, pair_key), history in histories.items()
        if relation_sequence == sequence and len(history) >= age
    }


def _rank_vectors(
    vectors: dict[str, tuple[int, ...]], dimensions: tuple[int, ...]
) -> dict[str, list[float]]:
    keys = sorted(vectors)
    selected_positions = [
        interval * len(FIELDS) + dimension
        for interval in range(len(next(iter(vectors.values()))) // len(FIELDS))
        for dimension in dimensions
    ]
    ranked_by_position = {}
    for position in selected_positions:
        ranked_by_position[position] = _rank_maturity(
            [float(vectors[key][position]) for key in keys],
            higher_is_stronger=False,
        )
    return {
        key: [ranked_by_position[position][index] for position in selected_positions]
        for index, key in enumerate(keys)
    }


def _raw_equivalence_edges(
    vectors: dict[str, tuple[int, ...]]
) -> set[tuple[str, str]]:
    classes: dict[tuple[int, ...], list[str]] = defaultdict(list)
    for pair_key, vector in vectors.items():
        classes[vector].append(pair_key)
    return {
        tuple(sorted(edge))
        for members in classes.values()
        for edge in combinations(members, 2)
    }


def _coverage_rows(
    vectors: dict[tuple[str, int], dict[str, tuple[int, ...]]]
) -> list[dict[str, object]]:
    rows = []
    for sequence in SEQUENCES:
        for age in AGES:
            counts = Counter(vectors[(sequence, age)].values())
            sizes = sorted(counts.values(), reverse=True)
            relation_count = sum(sizes)
            rows.append(
                {
                    "sequence": sequence,
                    "relation_age": age,
                    "relations": relation_count,
                    "exact_raw_prefixes": len(sizes),
                    "singleton_prefixes": sum(size == 1 for size in sizes),
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
    vectors: dict[tuple[str, int], dict[str, tuple[int, ...]]]
) -> list[dict[str, object]]:
    rows = []
    for age in AGES:
        forward = vectors[("forward", age)]
        reverse = vectors[("reverse", age)]
        shared = set(forward) & set(reverse)
        exact = sum(forward[key] == reverse[key] for key in shared)
        rows.append(
            {
                "relation_age": age,
                "forward_relations": len(forward),
                "reverse_relations": len(reverse),
                "shared_relations": len(shared),
                "exact_raw_prefix_matches": exact,
                "exact_raw_prefix_share": exact / max(1, len(shared)),
            }
        )
    return rows


def _graph_rows(
    edges: dict[tuple[str, int, str], set[tuple[str, str]]],
    zero_edges: dict[tuple[str, int, str], set[tuple[str, str]]],
) -> list[dict[str, object]]:
    rows = []
    for sequence in SEQUENCES:
        for age in AGES:
            for scope in ("raw_equal", *SCOPES, "robust"):
                graph = edges[(sequence, age, scope)]
                nodes = {node for edge in graph for node in edge}
                rows.append(
                    {
                        "sequence": sequence,
                        "relation_age": age,
                        "scope": scope,
                        "edges": len(graph),
                        "nodes": len(nodes),
                        "mean_degree": (2 * len(graph)) / max(1, len(nodes)),
                        "zero_distance_edges": len(
                            zero_edges.get((sequence, age, scope), set())
                        ),
                    }
                )
    return rows


def _order_rows(
    edges: dict[tuple[str, int, str], set[tuple[str, str]]]
) -> list[dict[str, object]]:
    rows = []
    for age in AGES:
        for scope in ("raw_equal", *SCOPES, "robust"):
            forward = edges[("forward", age, scope)]
            reverse = edges[("reverse", age, scope)]
            shared = forward & reverse
            rows.append(
                {
                    "relation_age": age,
                    "scope": scope,
                    "forward_edges": len(forward),
                    "reverse_edges": len(reverse),
                    "shared_edges": len(shared),
                    "shared_edge_nodes": len(
                        {node for edge in shared for node in edge}
                    ),
                    "edge_jaccard": len(shared) / max(1, len(forward | reverse)),
                }
            )
    return rows


def _null_rows(
    vectors: dict[tuple[str, int], dict[str, tuple[int, ...]]],
    edges: dict[tuple[str, int, str], set[tuple[str, str]]],
) -> list[dict[str, object]]:
    rng = random.Random(SEED)
    scopes = ("raw_equal", *SCOPES, "robust")
    null_values = {(age, scope): [] for age in AGES for scope in scopes}
    for age in AGES:
        reverse_members = sorted(vectors[("reverse", age)])
        for _ in range(PERMUTATIONS):
            shuffled = reverse_members[:]
            rng.shuffle(shuffled)
            mapping = dict(zip(reverse_members, shuffled))
            for scope in scopes:
                permuted = {
                    tuple(sorted((mapping[left], mapping[right])))
                    for left, right in edges[("reverse", age, scope)]
                }
                null_values[(age, scope)].append(
                    len(edges[("forward", age, scope)] & permuted)
                )

    rows = []
    for age in AGES:
        for scope in scopes:
            forward = edges[("forward", age, scope)]
            reverse = edges[("reverse", age, scope)]
            observed = len(forward & reverse)
            values = null_values[(age, scope)]
            mean = statistics.mean(values)
            deviation = statistics.pstdev(values)
            rows.append(
                {
                    "relation_age": age,
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
    return rows


def _summary_rows(
    identity_rows: list[dict[str, object]],
    graph_rows: list[dict[str, object]],
    order_rows: list[dict[str, object]],
    null_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    rows = []
    for identity in identity_rows:
        age = int(identity["relation_age"])
        forward_graph = next(
            row
            for row in graph_rows
            if row["sequence"] == "forward"
            and int(row["relation_age"]) == age
            and row["scope"] == "robust"
        )
        reverse_graph = next(
            row
            for row in graph_rows
            if row["sequence"] == "reverse"
            and int(row["relation_age"]) == age
            and row["scope"] == "robust"
        )
        order = next(
            row
            for row in order_rows
            if int(row["relation_age"]) == age and row["scope"] == "robust"
        )
        null = next(
            row
            for row in null_rows
            if int(row["relation_age"]) == age and row["scope"] == "robust"
        )
        rows.append(
            {
                **identity,
                "forward_robust_edges": forward_graph["edges"],
                "reverse_robust_edges": reverse_graph["edges"],
                "shared_robust_edges": order["shared_edges"],
                "shared_robust_nodes": order["shared_edge_nodes"],
                "robust_edge_jaccard": order["edge_jaccard"],
                "robust_null_mean_shared_edges": null["null_mean_shared_edges"],
                "robust_observed_to_null_ratio": null["observed_to_null_ratio"],
                "robust_empirical_p": null["empirical_p_ge_observed"],
                "read_by_mini_dio": 0,
                "influences_field": 0,
                "influences_action": 0,
            }
        )
    return rows


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
    zero_edges: dict[tuple[str, int, str], set[tuple[str, str]]] = {}
    for sequence in SEQUENCES:
        for age in AGES:
            raw_vectors = vectors[(sequence, age)]
            for scope, dimensions in SCOPES.items():
                ranked = _rank_vectors(raw_vectors, dimensions)
                graph, zeros = _mutual_nearest_edges({(age,): ranked})
                edges[(sequence, age, scope)] = graph
                zero_edges[(sequence, age, scope)] = zeros
            edges[(sequence, age, "robust")] = set.intersection(
                *(edges[(sequence, age, scope)] for scope in ROBUST_SCOPES)
            )
            zero_edges[(sequence, age, "robust")] = set.intersection(
                *(zero_edges[(sequence, age, scope)] for scope in ROBUST_SCOPES)
            )
            edges[(sequence, age, "raw_equal")] = _raw_equivalence_edges(raw_vectors)
            zero_edges[(sequence, age, "raw_equal")] = set(
                edges[(sequence, age, "raw_equal")]
            )

    coverage_rows = _coverage_rows(vectors)
    identity_rows = _identity_rows(vectors)
    graph_rows = _graph_rows(edges, zero_edges)
    order_rows = _order_rows(edges)
    null_rows = _null_rows(vectors, edges)
    summary_rows = _summary_rows(identity_rows, graph_rows, order_rows, null_rows)
    _write_csv("coverage", coverage_rows)
    _write_csv("identity", identity_rows)
    _write_csv("graphs", graph_rows)
    _write_csv("order", order_rows)
    _write_csv("null", null_rows)
    _write_csv("summary", summary_rows)
    print(f"coverage_rows={len(coverage_rows)}")
    print(f"graph_rows={len(graph_rows)}")
    print(f"null_rows={len(null_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
