from __future__ import annotations

import copy
import csv
import hashlib
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
    _dynamic_state,
    _world_senses,
    _worlds,
)
from tools.run_mcm_continuity_topology_transfer import (
    NEURON_COUNT,
    TickState,
    _pair_relation,
    _reset_trajectory,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2107_MCM_KONTINUITAET_QUELLIDENTITAET"
TARGET_COUNT = 8
COHORT_SIZE = 4
NULL_PERMUTATIONS = 4096
RELATION_TRANSITIONS = (
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
)
NEURON_PAIRS = NEURON_COUNT * (NEURON_COUNT - 1) // 2
FINGERPRINT_SIZE = NEURON_PAIRS * len(RELATION_TRANSITIONS)


@dataclass(frozen=True)
class Fingerprint:
    values: tuple[int, ...]
    changed_ticks: int
    transition_observations: int
    exact_convergence_tick: int


def _hash_key(world: World) -> str:
    return hashlib.sha256(world.key.encode("utf-8")).hexdigest()


def _source_and_target_worlds(
    worlds: list[World],
) -> tuple[list[World], tuple[World, ...], tuple[World, ...]]:
    ordered = sorted(worlds, key=lambda world: (_hash_key(world), world.key))
    if len(ordered) <= TARGET_COUNT:
        raise ValueError("not enough worlds for independent sources and targets")
    targets = ordered[:TARGET_COUNT]
    sources = ordered[TARGET_COUNT:]
    return sources, tuple(targets[:COHORT_SIZE]), tuple(targets[COHORT_SIZE:])


def _transition_slot(
    pair_index: int,
    reset_relation: int,
    continuous_relation: int,
) -> int:
    if reset_relation == continuous_relation:
        raise ValueError("equal relations have no transition slot")
    transition = (int(reset_relation), int(continuous_relation))
    return pair_index * len(RELATION_TRANSITIONS) + RELATION_TRANSITIONS.index(
        transition
    )


def _deviation_fingerprint(
    field,
    target_senses: tuple[dict, ...],
    reset: tuple[TickState, ...],
) -> Fingerprint:
    if len(target_senses) != len(reset):
        raise ValueError("target senses and reset trajectory differ in length")
    values = [0] * FINGERPRINT_SIZE
    changed_ticks = 0
    transition_observations = 0
    exact_convergence_tick = 0

    for offset, senses in enumerate(target_senses):
        tick = offset + 1
        state = field.step(senses)
        continuous = tuple(float(value) for value in state["activations"])
        reset_activations = reset[offset].activations
        tick_changed = False
        pair_index = 0
        for left in range(NEURON_COUNT):
            for right in range(left + 1, NEURON_COUNT):
                reset_relation = _pair_relation(
                    reset_activations[left] - reset_activations[right]
                )
                continuous_relation = _pair_relation(
                    continuous[left] - continuous[right]
                )
                if reset_relation != continuous_relation:
                    slot = _transition_slot(
                        pair_index, reset_relation, continuous_relation
                    )
                    values[slot] += 1
                    transition_observations += 1
                    tick_changed = True
                pair_index += 1
        changed_ticks += int(tick_changed)
        if _dynamic_state(field) == reset[offset].dynamic:
            exact_convergence_tick = tick
            break

    return Fingerprint(
        values=tuple(values),
        changed_ticks=changed_ticks,
        transition_observations=transition_observations,
        exact_convergence_tick=exact_convergence_tick,
    )


def _sum_vectors(vectors: list[tuple[int, ...]]) -> tuple[int, ...]:
    if not vectors:
        return tuple()
    return tuple(sum(values) for values in zip(*vectors))


def _shape_vector(values: tuple[int, ...]) -> tuple[float, ...]:
    total = sum(values)
    if total <= 0:
        return tuple(0.0 for _ in values)
    return tuple(value / total for value in values)


def _l1_distance(left: tuple, right: tuple) -> float:
    if len(left) != len(right):
        raise ValueError("profile vectors differ in length")
    return sum(abs(float(a) - float(b)) for a, b in zip(left, right))


def _identity_observations(
    left: dict[str, tuple],
    right: dict[str, tuple],
) -> tuple[list[dict[str, object]], list[list[float]], list[str]]:
    keys = sorted(left)
    if keys != sorted(right):
        raise ValueError("identity sets differ between cohorts")
    distance_matrix = [
        [_l1_distance(left[source], right[candidate]) for candidate in keys]
        for source in keys
    ]
    observations = []
    for source_index, source in enumerate(keys):
        distances = distance_matrix[source_index]
        same_distance = distances[source_index]
        smaller = sum(distance < same_distance for distance in distances)
        equal = sum(distance == same_distance for distance in distances)
        minimum = min(distances)
        nearest_tie_size = sum(distance == minimum for distance in distances)
        other_distances = [
            distance
            for candidate_index, distance in enumerate(distances)
            if candidate_index != source_index
        ]
        auc = (
            sum(distance > same_distance for distance in other_distances)
            + 0.5 * sum(distance == same_distance for distance in other_distances)
        ) / max(1, len(other_distances))
        observations.append(
            {
                "source_key": source,
                "candidate_pool_size": len(keys),
                "same_source_distance": same_distance,
                "nearest_other_distance": min(other_distances),
                "identity_rank": smaller + 1,
                "identity_distance_tie_size": equal,
                "identity_in_nearest_tie": int(smaller == 0),
                "identity_unique_nearest": int(
                    smaller == 0 and nearest_tie_size == 1
                ),
                "nearest_tie_size": nearest_tie_size,
                "identity_auc": auc,
            }
        )
    return observations, distance_matrix, keys


def _observed_metrics(observations: list[dict[str, object]]) -> dict[str, float]:
    return {
        "median_identity_rank": statistics.median(
            int(row["identity_rank"]) for row in observations
        ),
        "mean_identity_rank": statistics.mean(
            int(row["identity_rank"]) for row in observations
        ),
        "mean_identity_auc": statistics.mean(
            float(row["identity_auc"]) for row in observations
        ),
        "identity_unique_nearest": sum(
            int(row["identity_unique_nearest"]) for row in observations
        ),
        "identity_in_nearest_tie": sum(
            int(row["identity_in_nearest_tie"]) for row in observations
        ),
    }


def _matrix_metrics(
    distance_matrix: list[list[float]],
    identity_positions: list[int],
) -> dict[str, float]:
    ranks = []
    aucs = []
    unique_nearest = 0
    nearest_tie = 0
    for source_index, identity_position in enumerate(identity_positions):
        distances = distance_matrix[source_index]
        same_distance = distances[identity_position]
        smaller = sum(distance < same_distance for distance in distances)
        minimum = min(distances)
        nearest_count = sum(distance == minimum for distance in distances)
        ranks.append(smaller + 1)
        nearest_tie += int(smaller == 0)
        unique_nearest += int(smaller == 0 and nearest_count == 1)
        others = [
            distance
            for candidate_index, distance in enumerate(distances)
            if candidate_index != identity_position
        ]
        aucs.append(
            (
                sum(distance > same_distance for distance in others)
                + 0.5 * sum(distance == same_distance for distance in others)
            )
            / max(1, len(others))
        )
    return {
        "median_identity_rank": statistics.median(ranks),
        "mean_identity_rank": statistics.mean(ranks),
        "mean_identity_auc": statistics.mean(aucs),
        "identity_unique_nearest": unique_nearest,
        "identity_in_nearest_tie": nearest_tie,
    }


def _label_null(
    blocks: list[tuple[list[list[float]], list[str]]],
    observed: dict[str, float],
    seed_label: str,
) -> dict[str, float]:
    seed = int(hashlib.sha256(seed_label.encode("utf-8")).hexdigest()[:16], 16)
    rng = random.Random(seed)
    null_aucs = []
    null_unique = []
    null_nearest_tie = []
    for _ in range(NULL_PERMUTATIONS):
        total_sources = 0
        auc_sum = 0.0
        unique_sum = 0
        nearest_tie_sum = 0
        for distance_matrix, keys in blocks:
            shuffled_positions = list(range(len(keys)))
            rng.shuffle(shuffled_positions)
            metrics = _matrix_metrics(distance_matrix, shuffled_positions)
            total_sources += len(keys)
            auc_sum += float(metrics["mean_identity_auc"]) * len(keys)
            unique_sum += int(metrics["identity_unique_nearest"])
            nearest_tie_sum += int(metrics["identity_in_nearest_tie"])
        null_aucs.append(auc_sum / max(1, total_sources))
        null_unique.append(unique_sum)
        null_nearest_tie.append(nearest_tie_sum)
    return {
        "label_null_permutations": NULL_PERMUTATIONS,
        "label_null_mean_identity_auc": statistics.mean(null_aucs),
        "label_null_max_identity_auc": max(null_aucs),
        "identity_auc_label_p": (
            1
            + sum(
                value >= float(observed["mean_identity_auc"])
                for value in null_aucs
            )
        )
        / (NULL_PERMUTATIONS + 1),
        "label_null_mean_unique_nearest": statistics.mean(null_unique),
        "unique_nearest_label_p": (
            1
            + sum(
                value >= int(observed["identity_unique_nearest"])
                for value in null_unique
            )
        )
        / (NULL_PERMUTATIONS + 1),
        "label_null_mean_nearest_tie": statistics.mean(null_nearest_tie),
        "nearest_tie_label_p": (
            1
            + sum(
                value >= int(observed["identity_in_nearest_tie"])
                for value in null_nearest_tie
            )
        )
        / (NULL_PERMUTATIONS + 1),
    }


def _comparison_groups(
    sources: list[World],
    scope: str,
) -> list[list[str]]:
    if scope == "global":
        return [sorted(source.key for source in sources)]
    if scope != "within_asset_year":
        raise ValueError(f"unknown comparison scope: {scope}")
    grouped: dict[tuple[str, int], list[str]] = {}
    for source in sources:
        grouped.setdefault((source.asset, source.year), []).append(source.key)
    return [sorted(keys) for _, keys in sorted(grouped.items())]


def _dataset_rows(
    dataset: str,
    worlds: list[World],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    sources, cohort_a, cohort_b = _source_and_target_worlds(worlds)
    targets = cohort_a + cohort_b
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

    raw_a = {
        source.key: _sum_vectors(
            [fingerprints[source.key][target.key].values for target in cohort_a]
        )
        for source in sources
    }
    raw_b = {
        source.key: _sum_vectors(
            [fingerprints[source.key][target.key].values for target in cohort_b]
        )
        for source in sources
    }
    modes = {
        "raw": (raw_a, raw_b),
        "shape": (
            {key: _shape_vector(value) for key, value in raw_a.items()},
            {key: _shape_vector(value) for key, value in raw_b.items()},
        ),
    }
    all_fingerprints = [
        fingerprints[source.key][target.key]
        for source in sources
        for target in targets
    ]
    source_by_key = {source.key: source for source in sources}
    source_rows = []
    summary_rows = []
    for mode, (profiles_a, profiles_b) in modes.items():
        for direction, left, right in (
            ("a_to_b", profiles_a, profiles_b),
            ("b_to_a", profiles_b, profiles_a),
        ):
            for comparison_scope in ("global", "within_asset_year"):
                observations = []
                blocks = []
                groups = _comparison_groups(sources, comparison_scope)
                for group in groups:
                    group_left = {key: left[key] for key in group}
                    group_right = {key: right[key] for key in group}
                    group_observations, matrix, keys = _identity_observations(
                        group_left, group_right
                    )
                    observations.extend(group_observations)
                    blocks.append((matrix, keys))
                observed_metrics = _observed_metrics(observations)
                label_null = _label_null(
                    blocks,
                    observed_metrics,
                    f"2107|{dataset}|{mode}|{direction}|{comparison_scope}",
                )
                for observation in observations:
                    source = source_by_key[str(observation["source_key"])]
                    source_rows.append(
                        {
                            "dataset": dataset,
                            "profile_mode": mode,
                            "direction": direction,
                            "comparison_scope": comparison_scope,
                            "source_key": source.key,
                            "source_asset": source.asset,
                            "source_year": source.year,
                            "source_file": source.source.name,
                            "source_start": source.start,
                            "cohort_a_transition_observations": sum(
                                raw_a[source.key]
                            ),
                            "cohort_b_transition_observations": sum(
                                raw_b[source.key]
                            ),
                            "cohort_a_exact_convergence_count": sum(
                                int(
                                    fingerprints[source.key][
                                        target.key
                                    ].exact_convergence_tick
                                    > 0
                                )
                                for target in cohort_a
                            ),
                            "cohort_b_exact_convergence_count": sum(
                                int(
                                    fingerprints[source.key][
                                        target.key
                                    ].exact_convergence_tick
                                    > 0
                                )
                                for target in cohort_b
                            ),
                            "cohort_a_max_convergence_tick": max(
                                fingerprints[source.key][
                                    target.key
                                ].exact_convergence_tick
                                for target in cohort_a
                            ),
                            "cohort_b_max_convergence_tick": max(
                                fingerprints[source.key][
                                    target.key
                                ].exact_convergence_tick
                                for target in cohort_b
                            ),
                            **observation,
                            "source_label_read_by_field": 0,
                            "field_learning_used": 0,
                            "memory_read": 0,
                            "memory_written": 0,
                            "influences_action": 0,
                        }
                    )
                summary_rows.append(
                    {
                        "dataset": dataset,
                        "profile_mode": mode,
                        "direction": direction,
                        "comparison_scope": comparison_scope,
                        "source_identities": len(sources),
                        "comparison_groups": len(groups),
                        "minimum_candidate_pool": min(len(group) for group in groups),
                        "maximum_candidate_pool": max(len(group) for group in groups),
                        "targets_per_cohort": COHORT_SIZE,
                        "source_target_paths": len(all_fingerprints),
                        "paths_with_rank_change": sum(
                            int(item.transition_observations > 0)
                            for item in all_fingerprints
                        ),
                        "exact_convergence_paths": sum(
                            int(item.exact_convergence_tick > 0)
                            for item in all_fingerprints
                        ),
                        "maximum_exact_convergence_tick": max(
                            item.exact_convergence_tick
                            for item in all_fingerprints
                        ),
                        "cohort_a_targets": ";".join(
                            target.key for target in cohort_a
                        ),
                        "cohort_b_targets": ";".join(
                            target.key for target in cohort_b
                        ),
                        "zero_profiles_left": sum(
                            int(sum(profile) == 0) for profile in left.values()
                        ),
                        "zero_profiles_right": sum(
                            int(sum(profile) == 0) for profile in right.values()
                        ),
                        "median_identity_rank": observed_metrics[
                            "median_identity_rank"
                        ],
                        "mean_identity_rank": observed_metrics[
                            "mean_identity_rank"
                        ],
                        "mean_identity_auc": observed_metrics[
                            "mean_identity_auc"
                        ],
                        "identity_unique_nearest": observed_metrics[
                            "identity_unique_nearest"
                        ],
                        "identity_in_nearest_tie": observed_metrics[
                            "identity_in_nearest_tie"
                        ],
                        **label_null,
                        "source_label_read_by_field": 0,
                        "field_learning_used": 0,
                        "memory_read": 0,
                        "memory_written": 0,
                        "influences_action": 0,
                    }
                )
    return source_rows, summary_rows


def _all_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    worlds = _worlds()
    source_rows = []
    summary_rows = []
    for dataset in ("2091_basis", "2092_holdout"):
        dataset_worlds = [world for world in worlds if world.dataset == dataset]
        sources, summaries = _dataset_rows(dataset, dataset_worlds)
        source_rows.extend(sources)
        summary_rows.extend(summaries)
    return source_rows, summary_rows


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    source_rows, summary_rows = _all_rows()
    _write_csv("sources", source_rows)
    _write_csv("summary", summary_rows)
    for row in summary_rows:
        print(
            f"dataset={row['dataset']} mode={row['profile_mode']} "
            f"direction={row['direction']} scope={row['comparison_scope']}"
        )
        print(f"source_identities={row['source_identities']}")
        print(f"median_identity_rank={row['median_identity_rank']}")
        print(f"mean_identity_auc={row['mean_identity_auc']}")
        print(f"identity_auc_label_p={row['identity_auc_label_p']}")
        print(f"identity_unique_nearest={row['identity_unique_nearest']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
