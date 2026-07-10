from __future__ import annotations

import copy
import csv
import hashlib
import random
import statistics
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_continuous_field_instance import (
    _contact_field,
    _world_senses,
    _worlds,
)
from tools.run_mcm_continuity_source_identity import (
    FINGERPRINT_SIZE,
    NEURON_COUNT,
    NULL_PERMUTATIONS,
    _identity_observations,
    _label_null,
    _observed_metrics,
    _shape_vector,
    _sum_vectors,
    _transition_slot,
)
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_continuity_topology_transfer import _pair_relation


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2110_MCM_INTRINSISCHE_FORM_SELBSTLESBARKEIT"
PREFIX_TICKS = (1, 2, 4, 8, 16, 32, 64)


def _record_relation_transitions(
    previous: tuple[float, ...] | list[float],
    current: tuple[float, ...] | list[float],
    counts: list[int],
) -> int:
    if len(previous) != NEURON_COUNT or len(current) != NEURON_COUNT:
        raise ValueError("unexpected neuron count")
    changed = 0
    pair_index = 0
    for left in range(NEURON_COUNT):
        for right in range(left + 1, NEURON_COUNT):
            previous_relation = _pair_relation(
                float(previous[left]) - float(previous[right])
            )
            current_relation = _pair_relation(
                float(current[left]) - float(current[right])
            )
            if previous_relation != current_relation:
                counts[
                    _transition_slot(
                        pair_index, previous_relation, current_relation
                    )
                ] += 1
                changed += 1
            pair_index += 1
    return changed


def _intrinsic_prefix_profiles(field, target_senses: tuple[dict, ...]) -> dict[int, tuple[int, ...]]:
    if len(target_senses) < PREFIX_TICKS[-1]:
        raise ValueError("target is shorter than intrinsic prefix scale")
    previous = tuple(float(neuron.activation) for neuron in field.neurons)
    counts = [0] * FINGERPRINT_SIZE
    profiles = {}
    for tick, senses in enumerate(target_senses[: PREFIX_TICKS[-1]], start=1):
        state = field.step(senses)
        current = tuple(float(value) for value in state["activations"])
        _record_relation_transitions(previous, current, counts)
        if tick in PREFIX_TICKS:
            profiles[tick] = tuple(counts)
        previous = current
    return profiles


def _mutual_nearest_edges(
    distance_matrix: list[list[float]],
) -> list[tuple[int, int]]:
    if not distance_matrix or not distance_matrix[0]:
        return []
    width = len(distance_matrix[0])
    if any(len(row) != width for row in distance_matrix):
        raise ValueError("distance matrix is not rectangular")
    left_nearest = []
    for row in distance_matrix:
        minimum = min(row)
        left_nearest.append(
            {index for index, distance in enumerate(row) if distance == minimum}
        )
    right_nearest = []
    for right_index in range(width):
        column = [row[right_index] for row in distance_matrix]
        minimum = min(column)
        right_nearest.append(
            {
                index
                for index, distance in enumerate(column)
                if distance == minimum
            }
        )
    return [
        (left_index, right_index)
        for left_index, nearest in enumerate(left_nearest)
        for right_index in sorted(nearest)
        if left_index in right_nearest[right_index]
    ]


def _edge_label_null(
    edges: list[tuple[int, int]],
    keys: list[str],
    observed_same_source_edges: int,
    seed_label: str,
) -> dict[str, float]:
    seed = int(hashlib.sha256(seed_label.encode("utf-8")).hexdigest()[:16], 16)
    rng = random.Random(seed)
    null_same_edges = []
    for _ in range(NULL_PERMUTATIONS):
        shuffled_labels = keys[:]
        rng.shuffle(shuffled_labels)
        null_same_edges.append(
            sum(
                keys[left_index] == shuffled_labels[right_index]
                for left_index, right_index in edges
            )
        )
    return {
        "edge_label_null_permutations": NULL_PERMUTATIONS,
        "edge_label_null_mean_same_source_edges": statistics.mean(
            null_same_edges
        ),
        "edge_label_null_max_same_source_edges": max(null_same_edges),
        "same_source_edge_label_p": (
            1
            + sum(
                value >= observed_same_source_edges
                for value in null_same_edges
            )
        )
        / (NULL_PERMUTATIONS + 1),
    }


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict]]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    senses = {
        world.key: _world_senses(str(world.source), world.start)
        for world in worlds
    }
    source_fields = {
        source.key: _contact_field(senses[source.key])
        for source in sources
    }
    path_profiles = {}
    for source in sources:
        path_profiles[source.key] = {}
        for target in targets:
            path_profiles[source.key][target.key] = _intrinsic_prefix_profiles(
                copy.deepcopy(source_fields[source.key]),
                senses[target.key],
            )

    edge_rows = []
    summary_rows = []
    for prefix_ticks in PREFIX_TICKS:
        raw_a = {
            source.key: _sum_vectors(
                [
                    path_profiles[source.key][target.key][prefix_ticks]
                    for target in universe_a
                ]
            )
            for source in sources
        }
        raw_b = {
            source.key: _sum_vectors(
                [
                    path_profiles[source.key][target.key][prefix_ticks]
                    for target in universe_b
                ]
            )
            for source in sources
        }
        profiles_a = {
            key: _shape_vector(values) for key, values in raw_a.items()
        }
        profiles_b = {
            key: _shape_vector(values) for key, values in raw_b.items()
        }
        observations_a, matrix, keys = _identity_observations(
            profiles_a, profiles_b
        )
        observations_b, reverse_matrix, reverse_keys = _identity_observations(
            profiles_b, profiles_a
        )
        if keys != reverse_keys:
            raise RuntimeError("universe identity order differs")
        metrics_a = _observed_metrics(observations_a)
        metrics_b = _observed_metrics(observations_b)
        auc_null_a = _label_null(
            [(matrix, keys)],
            metrics_a,
            f"2110|{dataset}|{prefix_ticks}|a_to_b",
        )
        auc_null_b = _label_null(
            [(reverse_matrix, keys)],
            metrics_b,
            f"2110|{dataset}|{prefix_ticks}|b_to_a",
        )
        edges = _mutual_nearest_edges(matrix)
        same_source_edges = sum(left == right for left, right in edges)
        edge_null = _edge_label_null(
            edges,
            keys,
            same_source_edges,
            f"2110|{dataset}|{prefix_ticks}|edges",
        )
        same_sources = {
            keys[left]
            for left, right in edges
            if left == right
        }
        for edge_index, (left_index, right_index) in enumerate(edges, start=1):
            edge_rows.append(
                {
                    "dataset": dataset,
                    "prefix_ticks": prefix_ticks,
                    "edge_index": edge_index,
                    "left_anonymous_node": f"a_{left_index + 1:03d}",
                    "right_anonymous_node": f"b_{right_index + 1:03d}",
                    "distance": matrix[left_index][right_index],
                    "same_source_posthoc": int(left_index == right_index),
                    "left_source_posthoc": keys[left_index],
                    "right_source_posthoc": keys[right_index],
                    "graph_used_source_label": 0,
                    "graph_used_asset_or_year": 0,
                    "graph_used_reset_field": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
        summary_rows.append(
            {
                "dataset": dataset,
                "prefix_ticks": prefix_ticks,
                "source_identities": len(sources),
                "universe_a_targets": len(universe_a),
                "universe_b_targets": len(universe_b),
                "source_target_paths": len(sources) * len(targets),
                "zero_universe_a_profiles": sum(
                    int(sum(profile) == 0) for profile in profiles_a.values()
                ),
                "zero_universe_b_profiles": sum(
                    int(sum(profile) == 0) for profile in profiles_b.values()
                ),
                "minimum_universe_a_transition_observations": min(
                    sum(values) for values in raw_a.values()
                ),
                "maximum_universe_a_transition_observations": max(
                    sum(values) for values in raw_a.values()
                ),
                "minimum_universe_b_transition_observations": min(
                    sum(values) for values in raw_b.values()
                ),
                "maximum_universe_b_transition_observations": max(
                    sum(values) for values in raw_b.values()
                ),
                "a_to_b_mean_identity_auc": metrics_a["mean_identity_auc"],
                "a_to_b_median_identity_rank": metrics_a[
                    "median_identity_rank"
                ],
                "a_to_b_unique_nearest": metrics_a[
                    "identity_unique_nearest"
                ],
                "a_to_b_label_null_mean_auc": auc_null_a[
                    "label_null_mean_identity_auc"
                ],
                "a_to_b_label_null_max_auc": auc_null_a[
                    "label_null_max_identity_auc"
                ],
                "a_to_b_auc_label_p": auc_null_a["identity_auc_label_p"],
                "b_to_a_mean_identity_auc": metrics_b["mean_identity_auc"],
                "b_to_a_median_identity_rank": metrics_b[
                    "median_identity_rank"
                ],
                "b_to_a_unique_nearest": metrics_b[
                    "identity_unique_nearest"
                ],
                "b_to_a_label_null_mean_auc": auc_null_b[
                    "label_null_mean_identity_auc"
                ],
                "b_to_a_label_null_max_auc": auc_null_b[
                    "label_null_max_identity_auc"
                ],
                "b_to_a_auc_label_p": auc_null_b["identity_auc_label_p"],
                "mutual_nearest_edges": len(edges),
                "same_source_mutual_edges_posthoc": same_source_edges,
                "same_source_edge_share_posthoc": same_source_edges
                / max(1, len(edges)),
                "same_source_identity_coverage_posthoc": len(same_sources),
                **edge_null,
                "profile_uses_only_consecutive_field_states": 1,
                "profile_used_reset_field": 0,
                "graph_used_source_label": 0,
                "graph_used_asset_or_year": 0,
                "field_learning_used": 0,
                "memory_read": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
        )
    return edge_rows, summary_rows


def _all_rows() -> tuple[list[dict], list[dict]]:
    worlds = _worlds()
    edge_rows = []
    summary_rows = []
    for dataset in ("2091_basis", "2092_holdout"):
        dataset_worlds = [world for world in worlds if world.dataset == dataset]
        edges, summaries = _dataset_rows(dataset, dataset_worlds)
        edge_rows.extend(edges)
        summary_rows.extend(summaries)
    return edge_rows, summary_rows


def _write_csv(name: str, rows: list[dict]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    edge_rows, summary_rows = _all_rows()
    _write_csv("edges", edge_rows)
    _write_csv("summary", summary_rows)
    for row in summary_rows:
        print(f"dataset={row['dataset']} prefix_ticks={row['prefix_ticks']}")
        print(f"a_to_b_auc={row['a_to_b_mean_identity_auc']}")
        print(f"b_to_a_auc={row['b_to_a_mean_identity_auc']}")
        print(f"mutual_edges={row['mutual_nearest_edges']}")
        print(
            "same_source_mutual_edges="
            f"{row['same_source_mutual_edges_posthoc']}"
        )
        print(f"same_source_edge_label_p={row['same_source_edge_label_p']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
