from __future__ import annotations

import csv
import math
import statistics
import sys
from collections import Counter
from dataclasses import dataclass
from functools import reduce
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_continuous_field_instance import _world_senses, _worlds
from tools.run_mcm_continuity_source_identity import (
    FINGERPRINT_SIZE,
    _identity_observations,
    _label_null,
    _observed_metrics,
    _shape_vector,
    _sum_vectors,
)
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_continuous_rank_self_segmentation import (
    ClosedRankEpisode,
    _source_state,
    _target_episodes,
)
from tools.run_mcm_intrinsic_form_self_readability import (
    _edge_label_null,
    _mutual_nearest_edges,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2115_MCM_MEHREPISODEN_EXAKTE_FORMWIEDERKEHR"
PROFILE_KINDS = ("all_episode_forms", "exact_recurrence_forms")


@dataclass(frozen=True)
class StreamFormProfiles:
    all_episode_values: tuple[int, ...]
    recurrence_values: tuple[int, ...]
    episode_count: int
    unique_form_count: int
    recurrent_form_classes: int
    recurrence_observations: int
    maximum_form_occurrences: int


def _canonical_episode_form(values: tuple[int, ...]) -> tuple[int, ...]:
    nonzero = [int(value) for value in values if int(value) != 0]
    if not nonzero:
        return (0,) * len(values)
    divisor = reduce(math.gcd, nonzero)
    return tuple(int(value) // divisor for value in values)


def _stream_form_profiles(
    episodes: list[ClosedRankEpisode],
) -> StreamFormProfiles:
    forms = [_canonical_episode_form(episode.values) for episode in episodes]
    counts = Counter(forms)
    all_values = [0] * FINGERPRINT_SIZE
    recurrence_values = [0] * FINGERPRINT_SIZE
    for form, occurrences in counts.items():
        for index, value in enumerate(form):
            all_values[index] += int(value) * occurrences
            recurrence_values[index] += int(value) * max(0, occurrences - 1)
    return StreamFormProfiles(
        all_episode_values=tuple(all_values),
        recurrence_values=tuple(recurrence_values),
        episode_count=len(episodes),
        unique_form_count=len(counts),
        recurrent_form_classes=sum(occurrences > 1 for occurrences in counts.values()),
        recurrence_observations=sum(
            max(0, occurrences - 1) for occurrences in counts.values()
        ),
        maximum_form_occurrences=max(counts.values(), default=0),
    )


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict], list[dict]]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    senses = {
        world.key: _world_senses(str(world.source), world.start)
        for world in worlds
    }
    target_universe = {
        target.key: "a" if target in universe_a else "b"
        for target in targets
    }
    profiles: dict[str, dict[str, StreamFormProfiles]] = {}
    path_rows = []
    for source in sources:
        source_field, source_segmenter, boundary_tick, _ = _source_state(
            senses[source.key]
        )
        profiles[source.key] = {}
        for target in targets:
            _, strict = _target_episodes(
                source_field,
                source_segmenter,
                boundary_tick,
                senses[target.key],
            )
            stream_profile = _stream_form_profiles(strict)
            profiles[source.key][target.key] = stream_profile
            path_rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "target_key_posthoc": target.key,
                    "target_universe": target_universe[target.key],
                    "strict_episode_count": stream_profile.episode_count,
                    "unique_canonical_forms": stream_profile.unique_form_count,
                    "recurrent_form_classes": stream_profile.recurrent_form_classes,
                    "recurrence_observations": stream_profile.recurrence_observations,
                    "maximum_form_occurrences": (
                        stream_profile.maximum_form_occurrences
                    ),
                    "recurrence_episode_share": (
                        stream_profile.recurrence_observations
                        / max(1, stream_profile.episode_count)
                    ),
                    "recurrence_profile_is_zero": int(
                        sum(stream_profile.recurrence_values) == 0
                    ),
                    "form_strength_removed_by_exact_gcd": 1,
                    "recurrence_requires_second_observation": 1,
                    "fixed_distance_threshold_used": 0,
                    "field_received_contact_boundary": 0,
                    "segmenter_received_contact_boundary": 0,
                    "profile_selection_uses_posthoc_boundary": 1,
                    "field_learning_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )

    edge_rows = []
    summary_rows = []
    for profile_kind in PROFILE_KINDS:
        attribute = (
            "all_episode_values"
            if profile_kind == "all_episode_forms"
            else "recurrence_values"
        )
        raw_a = {
            source.key: _sum_vectors(
                [
                    getattr(profiles[source.key][target.key], attribute)
                    for target in universe_a
                ]
            )
            for source in sources
        }
        raw_b = {
            source.key: _sum_vectors(
                [
                    getattr(profiles[source.key][target.key], attribute)
                    for target in universe_b
                ]
            )
            for source in sources
        }
        shapes_a = {key: _shape_vector(values) for key, values in raw_a.items()}
        shapes_b = {key: _shape_vector(values) for key, values in raw_b.items()}
        observations_a, matrix, keys = _identity_observations(shapes_a, shapes_b)
        observations_b, reverse_matrix, reverse_keys = _identity_observations(
            shapes_b,
            shapes_a,
        )
        if keys != reverse_keys:
            raise RuntimeError("universe identity order differs")
        metrics_a = _observed_metrics(observations_a)
        metrics_b = _observed_metrics(observations_b)
        auc_null_a = _label_null(
            [(matrix, keys)],
            metrics_a,
            f"2115|{dataset}|{profile_kind}|a_to_b",
        )
        auc_null_b = _label_null(
            [(reverse_matrix, keys)],
            metrics_b,
            f"2115|{dataset}|{profile_kind}|b_to_a",
        )
        edges = _mutual_nearest_edges(matrix)
        same_source_edges = sum(left == right for left, right in edges)
        edge_null = _edge_label_null(
            edges,
            keys,
            same_source_edges,
            f"2115|{dataset}|{profile_kind}|edges",
        )
        for edge_index, (left_index, right_index) in enumerate(edges, start=1):
            edge_rows.append(
                {
                    "dataset": dataset,
                    "profile_kind": profile_kind,
                    "edge_index": edge_index,
                    "left_anonymous_node": f"a_{left_index + 1:03d}",
                    "right_anonymous_node": f"b_{right_index + 1:03d}",
                    "distance": matrix[left_index][right_index],
                    "same_source_posthoc": int(left_index == right_index),
                    "left_source_posthoc": keys[left_index],
                    "right_source_posthoc": keys[right_index],
                    "graph_used_source_label": 0,
                    "graph_used_asset_or_year": 0,
                    "graph_used_contact_boundary": 0,
                    "fixed_distance_threshold_used": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )

        recurrence_counts = [
            int(row["recurrence_observations"]) for row in path_rows
        ]
        summary_rows.append(
            {
                "dataset": dataset,
                "profile_kind": profile_kind,
                "source_identities": len(sources),
                "universe_a_targets": len(universe_a),
                "universe_b_targets": len(universe_b),
                "source_target_streams": len(path_rows),
                "streams_with_exact_recurrence": sum(
                    count > 0 for count in recurrence_counts
                ),
                "minimum_recurrence_observations": min(recurrence_counts),
                "median_recurrence_observations": statistics.median(
                    recurrence_counts
                ),
                "maximum_recurrence_observations": max(recurrence_counts),
                "zero_universe_a_profiles": sum(
                    int(sum(profile) == 0) for profile in shapes_a.values()
                ),
                "zero_universe_b_profiles": sum(
                    int(sum(profile) == 0) for profile in shapes_b.values()
                ),
                "minimum_universe_a_profile_observations": min(
                    sum(values) for values in raw_a.values()
                ),
                "maximum_universe_a_profile_observations": max(
                    sum(values) for values in raw_a.values()
                ),
                "minimum_universe_b_profile_observations": min(
                    sum(values) for values in raw_b.values()
                ),
                "maximum_universe_b_profile_observations": max(
                    sum(values) for values in raw_b.values()
                ),
                "a_to_b_mean_identity_auc": metrics_a["mean_identity_auc"],
                "a_to_b_median_identity_rank": metrics_a["median_identity_rank"],
                "a_to_b_unique_nearest": metrics_a["identity_unique_nearest"],
                "a_to_b_label_null_max_auc": auc_null_a[
                    "label_null_max_identity_auc"
                ],
                "a_to_b_auc_label_p": auc_null_a["identity_auc_label_p"],
                "b_to_a_mean_identity_auc": metrics_b["mean_identity_auc"],
                "b_to_a_median_identity_rank": metrics_b["median_identity_rank"],
                "b_to_a_unique_nearest": metrics_b["identity_unique_nearest"],
                "b_to_a_label_null_max_auc": auc_null_b[
                    "label_null_max_identity_auc"
                ],
                "b_to_a_auc_label_p": auc_null_b["identity_auc_label_p"],
                "mutual_nearest_edges": len(edges),
                "same_source_mutual_edges_posthoc": same_source_edges,
                "same_source_edge_share_posthoc": same_source_edges
                / max(1, len(edges)),
                **edge_null,
                "form_strength_removed_by_exact_gcd": 1,
                "recurrence_requires_second_observation": 1,
                "formerhaltende_source_label_null": 1,
                "fixed_distance_threshold_used": 0,
                "graph_used_source_label": 0,
                "graph_used_asset_or_year": 0,
                "field_learning_used": 0,
                "memory_read": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
        )
    return path_rows, edge_rows, summary_rows


def _all_rows() -> tuple[list[dict], list[dict], list[dict]]:
    worlds = _worlds()
    path_rows = []
    edge_rows = []
    summary_rows = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected = [world for world in worlds if world.dataset == dataset]
        paths, edges, summaries = _dataset_rows(dataset, selected)
        path_rows.extend(paths)
        edge_rows.extend(edges)
        summary_rows.extend(summaries)
    return path_rows, edge_rows, summary_rows


def _write_csv(name: str, rows: list[dict]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    path_rows, edge_rows, summary_rows = _all_rows()
    _write_csv("paths", path_rows)
    _write_csv("edges", edge_rows)
    _write_csv("summary", summary_rows)
    for row in summary_rows:
        print(
            f"dataset={row['dataset']} "
            f"profile_kind={row['profile_kind']}"
        )
        print(
            "recurrence_observations="
            f"{row['minimum_recurrence_observations']}.."
            f"{row['maximum_recurrence_observations']}"
        )
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
