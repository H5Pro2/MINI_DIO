from __future__ import annotations

import copy
import csv
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neuron import MiniMCMField
from tools.run_mcm_continuous_field_instance import (
    NEURON_COUNT,
    _world_senses,
    _worlds,
)
from tools.run_mcm_continuity_source_identity import (
    FINGERPRINT_SIZE,
    _identity_observations,
    _label_null,
    _observed_metrics,
    _shape_vector,
    _sum_vectors,
)
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_continuity_topology_transfer import _activation_order
from tools.run_mcm_intrinsic_form_self_readability import (
    _edge_label_null,
    _mutual_nearest_edges,
    _record_relation_transitions,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2112_MCM_KONTINUIERLICHE_RANGZYKLUS_SEGMENTIERUNG"
EPISODE_PREFIXES: tuple[int | str, ...] = (1, 2, 4, 8, 16, 32, 64, "all")


@dataclass(frozen=True)
class ClosedRankEpisode:
    values: tuple[int, ...]
    opened_tick: int
    closure_tick: int
    repeated_from_tick: int
    cycle_span: int
    unique_rank_orders: int
    transition_observations: int


class RankCycleSegmenter:
    def __init__(self, activations: tuple[float, ...]) -> None:
        self.previous_activations = tuple(float(value) for value in activations)
        self.previous_order = _activation_order(self.previous_activations)
        self.seen_orders = {self.previous_order: 0}
        self.counts = [0] * FINGERPRINT_SIZE
        self.opened_tick = 0

    def observe(
        self,
        activations: tuple[float, ...] | list[float],
        tick: int,
    ) -> ClosedRankEpisode | None:
        current = tuple(float(value) for value in activations)
        current_order = _activation_order(current)
        _record_relation_transitions(
            self.previous_activations,
            current,
            self.counts,
        )

        if self.opened_tick == 0 and current_order != self.previous_order:
            self.opened_tick = tick

        episode = None
        if self.opened_tick > 0 and current_order in self.seen_orders:
            repeated_from_tick = self.seen_orders[current_order]
            episode = ClosedRankEpisode(
                values=tuple(self.counts),
                opened_tick=self.opened_tick,
                closure_tick=tick,
                repeated_from_tick=repeated_from_tick,
                cycle_span=tick - repeated_from_tick,
                unique_rank_orders=len(self.seen_orders),
                transition_observations=sum(self.counts),
            )
            self.seen_orders = {current_order: tick}
            self.counts = [0] * FINGERPRINT_SIZE
            self.opened_tick = 0
        else:
            self.seen_orders.setdefault(current_order, tick)

        self.previous_activations = current
        self.previous_order = current_order
        return episode


def _strict_postboundary_episodes(
    episodes: list[ClosedRankEpisode],
    boundary_tick: int,
) -> list[ClosedRankEpisode]:
    return [episode for episode in episodes if episode.opened_tick > boundary_tick]


def _source_state(source_senses: tuple[dict, ...]) -> tuple:
    field = MiniMCMField(neuron_count=NEURON_COUNT)
    segmenter = RankCycleSegmenter(
        tuple(float(neuron.activation) for neuron in field.neurons)
    )
    closed_episodes = 0
    for tick, senses in enumerate(source_senses, start=1):
        state = field.step(senses)
        if segmenter.observe(state["activations"], tick) is not None:
            closed_episodes += 1
    return field, segmenter, len(source_senses), closed_episodes


def _target_episodes(
    source_field,
    source_segmenter: RankCycleSegmenter,
    boundary_tick: int,
    target_senses: tuple[dict, ...],
) -> tuple[list[ClosedRankEpisode], list[ClosedRankEpisode]]:
    field = copy.deepcopy(source_field)
    segmenter = copy.deepcopy(source_segmenter)
    emitted = []
    for offset, senses in enumerate(target_senses, start=1):
        state = field.step(senses)
        episode = segmenter.observe(
            state["activations"],
            boundary_tick + offset,
        )
        if episode is not None:
            emitted.append(episode)
    return emitted, _strict_postboundary_episodes(emitted, boundary_tick)


def _episode_profile(
    episodes: list[ClosedRankEpisode],
    prefix: int | str,
) -> tuple[int, ...]:
    selected = episodes if prefix == "all" else episodes[: int(prefix)]
    return _sum_vectors([episode.values for episode in selected])


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

    profiles: dict[str, dict[str, dict[int | str, tuple[int, ...]]]] = {}
    path_rows = []
    for source in sources:
        source_field, source_segmenter, boundary_tick, source_episode_count = (
            _source_state(senses[source.key])
        )
        profiles[source.key] = {}
        for target in targets:
            emitted, strict = _target_episodes(
                source_field,
                source_segmenter,
                boundary_tick,
                senses[target.key],
            )
            crossing = [
                episode
                for episode in emitted
                if episode.opened_tick <= boundary_tick < episode.closure_tick
            ]
            profiles[source.key][target.key] = {
                prefix: _episode_profile(strict, prefix)
                for prefix in EPISODE_PREFIXES
            }
            first = strict[0] if strict else None
            path_rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "source_start_posthoc": source.start,
                    "target_key_posthoc": target.key,
                    "target_universe": target_universe[target.key],
                    "source_ticks": boundary_tick,
                    "target_ticks": len(senses[target.key]),
                    "source_closed_episodes": source_episode_count,
                    "target_emitted_episodes": len(emitted),
                    "boundary_crossing_episodes": len(crossing),
                    "strict_postboundary_episodes": len(strict),
                    "first_strict_open_delay": (
                        first.opened_tick - boundary_tick if first else 0
                    ),
                    "first_strict_closure_delay": (
                        first.closure_tick - boundary_tick if first else 0
                    ),
                    "first_strict_cycle_span": first.cycle_span if first else 0,
                    "first_strict_transition_observations": (
                        first.transition_observations if first else 0
                    ),
                    "field_reset_at_hidden_boundary": 0,
                    "segmenter_reset_at_hidden_boundary": 0,
                    "segmenter_received_hidden_boundary": 0,
                    "profile_includes_preboundary_episode": 0,
                    "profile_used_reset_field": 0,
                    "field_learning_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )

    edge_rows = []
    summary_rows = []
    path_episode_counts = [
        int(row["strict_postboundary_episodes"]) for row in path_rows
    ]
    first_open_delays = [
        int(row["first_strict_open_delay"])
        for row in path_rows
        if int(row["first_strict_open_delay"]) > 0
    ]
    first_closure_delays = [
        int(row["first_strict_closure_delay"])
        for row in path_rows
        if int(row["first_strict_closure_delay"]) > 0
    ]
    for prefix in EPISODE_PREFIXES:
        raw_a = {
            source.key: _sum_vectors(
                [
                    profiles[source.key][target.key][prefix]
                    for target in universe_a
                ]
            )
            for source in sources
        }
        raw_b = {
            source.key: _sum_vectors(
                [
                    profiles[source.key][target.key][prefix]
                    for target in universe_b
                ]
            )
            for source in sources
        }
        profiles_a = {key: _shape_vector(values) for key, values in raw_a.items()}
        profiles_b = {key: _shape_vector(values) for key, values in raw_b.items()}
        observations_a, matrix, keys = _identity_observations(profiles_a, profiles_b)
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
            f"2112|{dataset}|{prefix}|a_to_b",
        )
        auc_null_b = _label_null(
            [(reverse_matrix, keys)],
            metrics_b,
            f"2112|{dataset}|{prefix}|b_to_a",
        )
        edges = _mutual_nearest_edges(matrix)
        same_source_edges = sum(left == right for left, right in edges)
        edge_null = _edge_label_null(
            edges,
            keys,
            same_source_edges,
            f"2112|{dataset}|{prefix}|edges",
        )
        for edge_index, (left_index, right_index) in enumerate(edges, start=1):
            edge_rows.append(
                {
                    "dataset": dataset,
                    "episode_prefix": prefix,
                    "edge_index": edge_index,
                    "left_anonymous_node": f"a_{left_index + 1:03d}",
                    "right_anonymous_node": f"b_{right_index + 1:03d}",
                    "distance": matrix[left_index][right_index],
                    "same_source_posthoc": int(left_index == right_index),
                    "left_source_posthoc": keys[left_index],
                    "right_source_posthoc": keys[right_index],
                    "graph_used_source_label": 0,
                    "graph_used_asset_or_year": 0,
                    "graph_used_hidden_boundary": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )

        required = 0 if prefix == "all" else int(prefix)
        summary_rows.append(
            {
                "dataset": dataset,
                "episode_prefix": prefix,
                "source_identities": len(sources),
                "universe_a_targets": len(universe_a),
                "universe_b_targets": len(universe_b),
                "source_target_streams": len(path_rows),
                "streams_reaching_episode_prefix": sum(
                    count >= required for count in path_episode_counts
                ),
                "minimum_strict_postboundary_episodes": min(path_episode_counts),
                "median_strict_postboundary_episodes": statistics.median(
                    path_episode_counts
                ),
                "maximum_strict_postboundary_episodes": max(path_episode_counts),
                "minimum_first_strict_open_delay": min(first_open_delays),
                "median_first_strict_open_delay": statistics.median(
                    first_open_delays
                ),
                "maximum_first_strict_open_delay": max(first_open_delays),
                "minimum_first_strict_closure_delay": min(first_closure_delays),
                "median_first_strict_closure_delay": statistics.median(
                    first_closure_delays
                ),
                "maximum_first_strict_closure_delay": max(first_closure_delays),
                "streams_with_boundary_crossing_episode": sum(
                    int(row["boundary_crossing_episodes"]) > 0
                    for row in path_rows
                ),
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
                "field_reset_at_hidden_boundary": 0,
                "segmenter_reset_at_hidden_boundary": 0,
                "segmenter_received_hidden_boundary": 0,
                "profile_includes_preboundary_episode": 0,
                "episode_prefix_is_research_scale": 1,
                "profile_used_reset_field": 0,
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
            f"episode_prefix={row['episode_prefix']}"
        )
        print(
            "strict_episodes="
            f"{row['minimum_strict_postboundary_episodes']}.."
            f"{row['maximum_strict_postboundary_episodes']}"
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
