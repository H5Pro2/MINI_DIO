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

from tools.run_mcm_continuous_field_instance import (
    _contact_field,
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
PREFIX = "2111_MCM_ENDOGENE_RANGZYKLUS_SCHLIESSUNG"


@dataclass(frozen=True)
class CycleEpisode:
    values: tuple[int, ...]
    opened_tick: int
    closure_tick: int
    repeated_from_tick: int
    cycle_span: int
    unique_rank_orders: int
    transition_observations: int
    closed: int


def _endogenous_cycle_episode(field, target_senses: tuple[dict, ...]) -> CycleEpisode:
    previous_activations = tuple(
        float(neuron.activation) for neuron in field.neurons
    )
    previous_order = _activation_order(previous_activations)
    seen_orders = {previous_order: 0}
    counts = [0] * FINGERPRINT_SIZE
    transition_observations = 0
    opened_tick = 0

    for tick, senses in enumerate(target_senses, start=1):
        state = field.step(senses)
        current_activations = tuple(
            float(value) for value in state["activations"]
        )
        transition_observations += _record_relation_transitions(
            previous_activations,
            current_activations,
            counts,
        )
        current_order = _activation_order(current_activations)
        if opened_tick == 0 and current_order != previous_order:
            opened_tick = tick
        if opened_tick > 0 and current_order in seen_orders:
            repeated_from_tick = seen_orders[current_order]
            return CycleEpisode(
                values=tuple(counts),
                opened_tick=opened_tick,
                closure_tick=tick,
                repeated_from_tick=repeated_from_tick,
                cycle_span=tick - repeated_from_tick,
                unique_rank_orders=len(seen_orders),
                transition_observations=transition_observations,
                closed=1,
            )
        seen_orders.setdefault(current_order, tick)
        previous_activations = current_activations
        previous_order = current_order

    return CycleEpisode(
        values=tuple(counts),
        opened_tick=opened_tick,
        closure_tick=0,
        repeated_from_tick=0,
        cycle_span=0,
        unique_rank_orders=len(seen_orders),
        transition_observations=transition_observations,
        closed=0,
    )


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict], list[dict]]:
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
    episodes = {}
    path_rows = []
    for source in sources:
        episodes[source.key] = {}
        for target in targets:
            episode = _endogenous_cycle_episode(
                copy.deepcopy(source_fields[source.key]),
                senses[target.key],
            )
            episodes[source.key][target.key] = episode
            universe = "a" if target in universe_a else "b"
            path_rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "source_start_posthoc": source.start,
                    "target_key_posthoc": target.key,
                    "target_universe": universe,
                    "opened_tick": episode.opened_tick,
                    "closure_tick": episode.closure_tick,
                    "repeated_from_tick": episode.repeated_from_tick,
                    "cycle_span": episode.cycle_span,
                    "unique_rank_orders": episode.unique_rank_orders,
                    "transition_observations": episode.transition_observations,
                    "closed": episode.closed,
                    "closure_used_fixed_tick_limit": 0,
                    "profile_used_reset_field": 0,
                    "profile_used_source_label": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )

    raw_a = {
        source.key: _sum_vectors(
            [episodes[source.key][target.key].values for target in universe_a]
        )
        for source in sources
    }
    raw_b = {
        source.key: _sum_vectors(
            [episodes[source.key][target.key].values for target in universe_b]
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
        f"2111|{dataset}|a_to_b",
    )
    auc_null_b = _label_null(
        [(reverse_matrix, keys)],
        metrics_b,
        f"2111|{dataset}|b_to_a",
    )
    edges = _mutual_nearest_edges(matrix)
    same_source_edges = sum(left == right for left, right in edges)
    edge_null = _edge_label_null(
        edges,
        keys,
        same_source_edges,
        f"2111|{dataset}|edges",
    )
    edge_rows = []
    for edge_index, (left_index, right_index) in enumerate(edges, start=1):
        edge_rows.append(
            {
                "dataset": dataset,
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
                "graph_used_fixed_tick_limit": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
        )

    closed = [row for row in path_rows if int(row["closed"]) == 1]
    opened = [row for row in path_rows if int(row["opened_tick"]) > 0]
    summary_rows = [
        {
            "dataset": dataset,
            "source_identities": len(sources),
            "universe_a_targets": len(universe_a),
            "universe_b_targets": len(universe_b),
            "source_target_paths": len(path_rows),
            "opened_paths": len(opened),
            "closed_paths": len(closed),
            "closure_share": len(closed) / max(1, len(path_rows)),
            "minimum_opened_tick": min(int(row["opened_tick"]) for row in opened),
            "median_opened_tick": statistics.median(
                int(row["opened_tick"]) for row in opened
            ),
            "maximum_opened_tick": max(int(row["opened_tick"]) for row in opened),
            "minimum_closure_tick": min(int(row["closure_tick"]) for row in closed),
            "median_closure_tick": statistics.median(
                int(row["closure_tick"]) for row in closed
            ),
            "mean_closure_tick": statistics.mean(
                int(row["closure_tick"]) for row in closed
            ),
            "maximum_closure_tick": max(int(row["closure_tick"]) for row in closed),
            "minimum_cycle_span": min(int(row["cycle_span"]) for row in closed),
            "median_cycle_span": statistics.median(
                int(row["cycle_span"]) for row in closed
            ),
            "maximum_cycle_span": max(int(row["cycle_span"]) for row in closed),
            "minimum_unique_rank_orders": min(
                int(row["unique_rank_orders"]) for row in closed
            ),
            "median_unique_rank_orders": statistics.median(
                int(row["unique_rank_orders"]) for row in closed
            ),
            "maximum_unique_rank_orders": max(
                int(row["unique_rank_orders"]) for row in closed
            ),
            "minimum_transition_observations": min(
                int(row["transition_observations"]) for row in closed
            ),
            "median_transition_observations": statistics.median(
                int(row["transition_observations"]) for row in closed
            ),
            "maximum_transition_observations": max(
                int(row["transition_observations"]) for row in closed
            ),
            "zero_universe_a_profiles": sum(
                int(sum(profile) == 0) for profile in profiles_a.values()
            ),
            "zero_universe_b_profiles": sum(
                int(sum(profile) == 0) for profile in profiles_b.values()
            ),
            "a_to_b_mean_identity_auc": metrics_a["mean_identity_auc"],
            "a_to_b_median_identity_rank": metrics_a["median_identity_rank"],
            "a_to_b_unique_nearest": metrics_a["identity_unique_nearest"],
            "a_to_b_label_null_mean_auc": auc_null_a[
                "label_null_mean_identity_auc"
            ],
            "a_to_b_label_null_max_auc": auc_null_a[
                "label_null_max_identity_auc"
            ],
            "a_to_b_auc_label_p": auc_null_a["identity_auc_label_p"],
            "b_to_a_mean_identity_auc": metrics_b["mean_identity_auc"],
            "b_to_a_median_identity_rank": metrics_b["median_identity_rank"],
            "b_to_a_unique_nearest": metrics_b["identity_unique_nearest"],
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
            "same_source_identity_coverage_posthoc": len(
                {keys[left] for left, right in edges if left == right}
            ),
            **edge_null,
            "episode_start_is_external_contact_boundary": 1,
            "episode_end_is_endogenous_exact_rank_recurrence": 1,
            "closure_used_fixed_tick_limit": 0,
            "profile_used_reset_field": 0,
            "graph_used_source_label": 0,
            "graph_used_asset_or_year": 0,
            "field_learning_used": 0,
            "memory_read": 0,
            "memory_written": 0,
            "influences_action": 0,
        }
    ]
    return path_rows, edge_rows, summary_rows


def _all_rows() -> tuple[list[dict], list[dict], list[dict]]:
    worlds = _worlds()
    path_rows = []
    edge_rows = []
    summary_rows = []
    for dataset in ("2091_basis", "2092_holdout"):
        dataset_worlds = [world for world in worlds if world.dataset == dataset]
        paths, edges, summaries = _dataset_rows(dataset, dataset_worlds)
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
        print(f"dataset={row['dataset']}")
        print(f"closed_paths={row['closed_paths']}")
        print(f"median_closure_tick={row['median_closure_tick']}")
        print(f"maximum_closure_tick={row['maximum_closure_tick']}")
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
