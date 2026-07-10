from __future__ import annotations

import copy
import csv
import statistics
import sys
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
    TARGET_COUNT,
    Fingerprint,
    _deviation_fingerprint,
    _hash_key,
    _identity_observations,
    _label_null,
    _observed_metrics,
    _shape_vector,
    _sum_vectors,
)
from tools.run_mcm_continuity_topology_transfer import _reset_trajectory


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2109_MCM_KONTINUITAET_ZIELUNIVERSUM_TRANSFER"


def _universe_split(
    worlds: list[World],
) -> tuple[list[World], tuple[World, ...], tuple[World, ...]]:
    ordered = sorted(worlds, key=lambda world: (_hash_key(world), world.key))
    required = TARGET_COUNT * 2
    if len(ordered) <= required:
        raise ValueError("not enough worlds for two targets universes and sources")
    universe_a = tuple(ordered[:TARGET_COUNT])
    universe_b = tuple(ordered[TARGET_COUNT:required])
    sources = ordered[required:]
    return sources, universe_a, universe_b


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
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
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
            [
                fingerprints[source.key][target.key].values
                for target in universe_a
            ]
        )
        for source in sources
    }
    raw_b = {
        source.key: _sum_vectors(
            [
                fingerprints[source.key][target.key].values
                for target in universe_b
            ]
        )
        for source in sources
    }
    profiles_a = {key: _shape_vector(values) for key, values in raw_a.items()}
    profiles_b = {key: _shape_vector(values) for key, values in raw_b.items()}
    source_by_key = {source.key: source for source in sources}
    all_fingerprints = [
        fingerprints[source.key][target.key]
        for source in sources
        for target in targets
    ]

    source_rows = []
    summary_rows = []
    for direction, left, right in (
        ("a_to_b", profiles_a, profiles_b),
        ("b_to_a", profiles_b, profiles_a),
    ):
        for comparison_scope in ("global", "within_asset_year"):
            observations = []
            blocks = []
            groups = _comparison_groups(sources, comparison_scope)
            for group_keys in groups:
                group_left = {key: left[key] for key in group_keys}
                group_right = {key: right[key] for key in group_keys}
                group_observations, matrix, keys = _identity_observations(
                    group_left, group_right
                )
                observations.extend(group_observations)
                blocks.append((matrix, keys))
            observed = _observed_metrics(observations)
            label_null = _label_null(
                blocks,
                observed,
                f"2109|{dataset}|{direction}|{comparison_scope}",
            )
            for observation in observations:
                source = source_by_key[str(observation["source_key"])]
                source_rows.append(
                    {
                        "dataset": dataset,
                        "direction": direction,
                        "comparison_scope": comparison_scope,
                        "source_key": source.key,
                        "source_asset": source.asset,
                        "source_year": source.year,
                        "source_file": source.source.name,
                        "source_start": source.start,
                        "universe_a_transition_observations": sum(
                            raw_a[source.key]
                        ),
                        "universe_b_transition_observations": sum(
                            raw_b[source.key]
                        ),
                        **observation,
                        "profile_mode": "shape",
                        "source_label_read_by_field": 0,
                        "field_learning_used": 0,
                        "memory_read": 0,
                        "memory_written": 0,
                        "influences_action": 0,
                    }
                )
            same_distances = [
                float(row["same_source_distance"]) for row in observations
            ]
            other_distances = [
                float(row["nearest_other_distance"]) for row in observations
            ]
            summary_rows.append(
                {
                    "dataset": dataset,
                    "direction": direction,
                    "comparison_scope": comparison_scope,
                    "source_identities": len(sources),
                    "comparison_groups": len(groups),
                    "minimum_candidate_pool": min(len(group) for group in groups),
                    "maximum_candidate_pool": max(len(group) for group in groups),
                    "universe_a_targets": ";".join(
                        target.key for target in universe_a
                    ),
                    "universe_b_targets": ";".join(
                        target.key for target in universe_b
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
                    "maximum_exact_convergence_tick": max(
                        item.exact_convergence_tick for item in all_fingerprints
                    ),
                    "zero_universe_a_profiles": sum(
                        int(sum(profile) == 0) for profile in profiles_a.values()
                    ),
                    "zero_universe_b_profiles": sum(
                        int(sum(profile) == 0) for profile in profiles_b.values()
                    ),
                    "median_identity_rank": observed["median_identity_rank"],
                    "mean_identity_rank": observed["mean_identity_rank"],
                    "mean_identity_auc": observed["mean_identity_auc"],
                    "identity_unique_nearest": observed[
                        "identity_unique_nearest"
                    ],
                    "identity_in_nearest_tie": observed[
                        "identity_in_nearest_tie"
                    ],
                    "median_same_source_distance": statistics.median(
                        same_distances
                    ),
                    "median_nearest_other_distance": statistics.median(
                        other_distances
                    ),
                    **label_null,
                    "profile_mode": "shape",
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
            f"dataset={row['dataset']} direction={row['direction']} "
            f"scope={row['comparison_scope']}"
        )
        print(f"source_identities={row['source_identities']}")
        print(f"mean_identity_auc={row['mean_identity_auc']}")
        print(f"median_identity_rank={row['median_identity_rank']}")
        print(f"identity_unique_nearest={row['identity_unique_nearest']}")
        print(f"identity_auc_label_p={row['identity_auc_label_p']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
