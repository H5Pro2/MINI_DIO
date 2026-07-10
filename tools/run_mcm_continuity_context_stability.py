from __future__ import annotations

import copy
import csv
import hashlib
import itertools
import random
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_continuous_field_instance import (
    World,
    _contact_field,
    _world_senses,
    _worlds,
)
from tools.run_mcm_continuity_source_identity import (
    COHORT_SIZE,
    NULL_PERMUTATIONS,
    Fingerprint,
    _deviation_fingerprint,
    _identity_observations,
    _observed_metrics,
    _shape_vector,
    _source_and_target_worlds,
    _sum_vectors,
)
from tools.run_mcm_continuity_topology_transfer import _reset_trajectory


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2108_MCM_KONTINUITAET_KONTEXTSTABILITAET"


@dataclass(frozen=True)
class ScoreBlock:
    group_key: str
    keys: tuple[str, ...]
    auc_scores: tuple[tuple[float, ...], ...]
    unique_scores: tuple[tuple[int, ...], ...]
    nearest_tie_scores: tuple[tuple[int, ...], ...]


def _balanced_partitions(
    targets: tuple[World, ...],
) -> list[tuple[tuple[World, ...], tuple[World, ...]]]:
    """Return every complementary 4/4 split once, without result selection."""

    if len(targets) != COHORT_SIZE * 2:
        raise ValueError("expected exactly two balanced target cohorts")
    partitions = []
    indexes = tuple(range(len(targets)))
    for selected in itertools.combinations(indexes, COHORT_SIZE):
        if 0 not in selected:
            continue
        selected_set = set(selected)
        cohort_a = tuple(targets[index] for index in selected)
        cohort_b = tuple(
            targets[index] for index in indexes if index not in selected_set
        )
        partitions.append((cohort_a, cohort_b))
    return partitions


def _source_groups(sources: list[World]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for source in sources:
        key = f"{source.asset}|{source.year}"
        grouped.setdefault(key, []).append(source.key)
    return {
        group_key: sorted(keys)
        for group_key, keys in sorted(grouped.items())
    }


def _candidate_score_block(
    group_key: str,
    distance_matrix: list[list[float]],
    keys: list[str],
) -> ScoreBlock:
    auc_rows = []
    unique_rows = []
    nearest_tie_rows = []
    for distances in distance_matrix:
        minimum = min(distances)
        nearest_count = sum(distance == minimum for distance in distances)
        auc_row = []
        unique_row = []
        nearest_tie_row = []
        for identity_position, same_distance in enumerate(distances):
            others = [
                distance
                for candidate_index, distance in enumerate(distances)
                if candidate_index != identity_position
            ]
            auc_row.append(
                (
                    sum(distance > same_distance for distance in others)
                    + 0.5 * sum(distance == same_distance for distance in others)
                )
                / max(1, len(others))
            )
            nearest_tie_row.append(int(same_distance == minimum))
            unique_row.append(
                int(same_distance == minimum and nearest_count == 1)
            )
        auc_rows.append(tuple(auc_row))
        unique_rows.append(tuple(unique_row))
        nearest_tie_rows.append(tuple(nearest_tie_row))
    return ScoreBlock(
        group_key=group_key,
        keys=tuple(keys),
        auc_scores=tuple(auc_rows),
        unique_scores=tuple(unique_rows),
        nearest_tie_scores=tuple(nearest_tie_rows),
    )


def _shared_label_null(
    blocks: list[ScoreBlock],
    observed_auc: float,
    observed_unique: int,
    observed_nearest_tie: int,
    seed_label: str,
) -> dict[str, float]:
    seed = int(hashlib.sha256(seed_label.encode("utf-8")).hexdigest()[:16], 16)
    rng = random.Random(seed)
    group_sizes = {}
    for block in blocks:
        group_sizes[block.group_key] = len(block.keys)
    total_observations = sum(len(block.keys) for block in blocks)
    null_aucs = []
    null_unique = []
    null_nearest_tie = []
    for _ in range(NULL_PERMUTATIONS):
        permutations = {}
        for group_key, size in group_sizes.items():
            positions = list(range(size))
            rng.shuffle(positions)
            permutations[group_key] = positions
        auc_sum = 0.0
        unique_sum = 0
        nearest_tie_sum = 0
        for block in blocks:
            positions = permutations[block.group_key]
            for row_index, identity_position in enumerate(positions):
                auc_sum += block.auc_scores[row_index][identity_position]
                unique_sum += block.unique_scores[row_index][identity_position]
                nearest_tie_sum += block.nearest_tie_scores[row_index][
                    identity_position
                ]
        null_aucs.append(auc_sum / max(1, total_observations))
        null_unique.append(unique_sum)
        null_nearest_tie.append(nearest_tie_sum)
    return {
        "label_null_permutations": NULL_PERMUTATIONS,
        "shared_label_across_partitions": 1,
        "label_null_mean_auc": statistics.mean(null_aucs),
        "label_null_max_auc": max(null_aucs),
        "aggregate_auc_label_p": (
            1 + sum(value >= observed_auc for value in null_aucs)
        )
        / (NULL_PERMUTATIONS + 1),
        "label_null_mean_unique_nearest": statistics.mean(null_unique),
        "unique_nearest_label_p": (
            1 + sum(value >= observed_unique for value in null_unique)
        )
        / (NULL_PERMUTATIONS + 1),
        "label_null_mean_nearest_tie": statistics.mean(null_nearest_tie),
        "nearest_tie_label_p": (
            1 + sum(value >= observed_nearest_tie for value in null_nearest_tie)
        )
        / (NULL_PERMUTATIONS + 1),
    }


def _dataset_rows(
    dataset: str,
    worlds: list[World],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    sources, initial_a, initial_b = _source_and_target_worlds(worlds)
    targets = initial_a + initial_b
    partitions = _balanced_partitions(targets)
    senses = {
        world.key: _world_senses(str(world.source), world.start)
        for world in worlds
    }
    reset = {
        target.key: _reset_trajectory(senses[target.key])
        for target in targets
    }
    source_fields = {
        source.key: _contact_field(senses[source.key])
        for source in sources
    }
    fingerprints: dict[str, dict[str, Fingerprint]] = {}
    for source in sources:
        fingerprints[source.key] = {}
        for target in targets:
            fingerprints[source.key][target.key] = _deviation_fingerprint(
                copy.deepcopy(source_fields[source.key]),
                senses[target.key],
                reset[target.key],
            )

    groups = _source_groups(sources)
    partition_rows = []
    direction_blocks: dict[str, list[ScoreBlock]] = {
        "a_to_b": [],
        "b_to_a": [],
    }
    direction_observations: dict[str, list[dict[str, object]]] = {
        "a_to_b": [],
        "b_to_a": [],
    }
    source_aucs: dict[str, dict[str, list[float]]] = {
        direction: {source.key: [] for source in sources}
        for direction in direction_blocks
    }

    for partition_index, (cohort_a, cohort_b) in enumerate(partitions, start=1):
        raw_a = {
            source.key: _sum_vectors(
                [
                    fingerprints[source.key][target.key].values
                    for target in cohort_a
                ]
            )
            for source in sources
        }
        raw_b = {
            source.key: _sum_vectors(
                [
                    fingerprints[source.key][target.key].values
                    for target in cohort_b
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
        for direction, left, right in (
            ("a_to_b", profiles_a, profiles_b),
            ("b_to_a", profiles_b, profiles_a),
        ):
            observations = []
            for group_key, group_keys in groups.items():
                group_left = {key: left[key] for key in group_keys}
                group_right = {key: right[key] for key in group_keys}
                group_observations, matrix, keys = _identity_observations(
                    group_left, group_right
                )
                observations.extend(group_observations)
                direction_blocks[direction].append(
                    _candidate_score_block(group_key, matrix, keys)
                )
            metrics = _observed_metrics(observations)
            direction_observations[direction].extend(observations)
            for observation in observations:
                source_aucs[direction][str(observation["source_key"])].append(
                    float(observation["identity_auc"])
                )
            partition_rows.append(
                {
                    "dataset": dataset,
                    "partition_index": partition_index,
                    "direction": direction,
                    "cohort_a_targets": ";".join(
                        target.key for target in cohort_a
                    ),
                    "cohort_b_targets": ";".join(
                        target.key for target in cohort_b
                    ),
                    "source_identities": len(sources),
                    "asset_year_groups": len(groups),
                    "minimum_candidate_pool": min(
                        len(keys) for keys in groups.values()
                    ),
                    "maximum_candidate_pool": max(
                        len(keys) for keys in groups.values()
                    ),
                    "median_identity_rank": metrics["median_identity_rank"],
                    "mean_identity_rank": metrics["mean_identity_rank"],
                    "mean_identity_auc": metrics["mean_identity_auc"],
                    "identity_unique_nearest": metrics[
                        "identity_unique_nearest"
                    ],
                    "identity_in_nearest_tie": metrics[
                        "identity_in_nearest_tie"
                    ],
                    "profile_mode": "shape",
                    "comparison_scope": "within_asset_year",
                    "source_label_read_by_field": 0,
                    "field_learning_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )

    all_fingerprints = [
        fingerprints[source.key][target.key]
        for source in sources
        for target in targets
    ]
    summary_rows = []
    for direction in ("a_to_b", "b_to_a"):
        selected = [
            row for row in partition_rows if row["direction"] == direction
        ]
        observations = direction_observations[direction]
        observed = _observed_metrics(observations)
        partition_aucs = [float(row["mean_identity_auc"]) for row in selected]
        partition_unique = [
            int(row["identity_unique_nearest"]) for row in selected
        ]
        source_mean_aucs = [
            statistics.mean(values)
            for values in source_aucs[direction].values()
        ]
        source_minimum_aucs = [
            min(values) for values in source_aucs[direction].values()
        ]
        label_null = _shared_label_null(
            direction_blocks[direction],
            float(observed["mean_identity_auc"]),
            int(observed["identity_unique_nearest"]),
            int(observed["identity_in_nearest_tie"]),
            f"2108|{dataset}|{direction}",
        )
        summary_rows.append(
            {
                "dataset": dataset,
                "direction": direction,
                "target_worlds": len(targets),
                "balanced_partitions": len(partitions),
                "source_identities": len(sources),
                "asset_year_groups": len(groups),
                "minimum_candidate_pool": min(
                    len(keys) for keys in groups.values()
                ),
                "maximum_candidate_pool": max(
                    len(keys) for keys in groups.values()
                ),
                "source_target_paths": len(all_fingerprints),
                "paths_with_rank_change": sum(
                    int(item.transition_observations > 0)
                    for item in all_fingerprints
                ),
                "exact_convergence_paths": sum(
                    int(item.exact_convergence_tick > 0)
                    for item in all_fingerprints
                ),
                "minimum_partition_auc": min(partition_aucs),
                "median_partition_auc": statistics.median(partition_aucs),
                "mean_partition_auc": statistics.mean(partition_aucs),
                "maximum_partition_auc": max(partition_aucs),
                "partitions_above_half_auc": sum(
                    auc > 0.5 for auc in partition_aucs
                ),
                "minimum_unique_nearest": min(partition_unique),
                "median_unique_nearest": statistics.median(partition_unique),
                "maximum_unique_nearest": max(partition_unique),
                "aggregate_mean_identity_auc": observed["mean_identity_auc"],
                "aggregate_unique_nearest": observed[
                    "identity_unique_nearest"
                ],
                "aggregate_identity_in_nearest_tie": observed[
                    "identity_in_nearest_tie"
                ],
                "minimum_source_mean_auc": min(source_mean_aucs),
                "median_source_mean_auc": statistics.median(source_mean_aucs),
                "maximum_source_mean_auc": max(source_mean_aucs),
                "sources_mean_auc_above_half": sum(
                    auc > 0.5 for auc in source_mean_aucs
                ),
                "sources_all_partitions_above_half": sum(
                    auc > 0.5 for auc in source_minimum_aucs
                ),
                **label_null,
                "profile_mode": "shape",
                "comparison_scope": "within_asset_year",
                "source_label_read_by_field": 0,
                "field_learning_used": 0,
                "memory_read": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
        )
    return partition_rows, summary_rows


def _all_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    worlds = _worlds()
    partition_rows = []
    summary_rows = []
    for dataset in ("2091_basis", "2092_holdout"):
        dataset_worlds = [world for world in worlds if world.dataset == dataset]
        partitions, summaries = _dataset_rows(dataset, dataset_worlds)
        partition_rows.extend(partitions)
        summary_rows.extend(summaries)
    return partition_rows, summary_rows


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    partition_rows, summary_rows = _all_rows()
    _write_csv("partitions", partition_rows)
    _write_csv("summary", summary_rows)
    for row in summary_rows:
        print(f"dataset={row['dataset']} direction={row['direction']}")
        print(f"balanced_partitions={row['balanced_partitions']}")
        print(f"minimum_partition_auc={row['minimum_partition_auc']}")
        print(f"median_partition_auc={row['median_partition_auc']}")
        print(f"maximum_partition_auc={row['maximum_partition_auc']}")
        print(f"partitions_above_half_auc={row['partitions_above_half_auc']}")
        print(f"aggregate_auc_label_p={row['aggregate_auc_label_p']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
