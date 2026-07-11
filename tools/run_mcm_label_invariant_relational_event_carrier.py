from __future__ import annotations

import copy
import csv
import hashlib
import sys
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
    _identity_observations,
    _label_null,
    _observed_metrics,
    _shape_vector,
    _sum_vectors,
)
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_continuity_topology_transfer import _pair_relation
from tools.run_mcm_intrinsic_form_self_readability import (
    _edge_label_null,
    _mutual_nearest_edges,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2128_MCM_LABELINVARIANTER_RELATIONSEREIGNISTRAEGER"
CORE_PATH = ROOT / "mini_dio" / "mcm_neuron.py"
PREFIX_TICKS = (1, 2, 4, 8, 16, 32, 64)
PAIR_COUNT = NEURON_COUNT * (NEURON_COUNT - 1) // 2
EVENT_COUNT_SIZE = PAIR_COUNT + 1
EVENT_DELTA_SIZE = PAIR_COUNT * 2 + 1
PROFILE_SIZE = EVENT_COUNT_SIZE + EVENT_DELTA_SIZE
PROFILE_COMPONENTS = ("count", "delta", "combined")


def _relation_change_count(
    previous: tuple[float, ...] | list[float],
    current: tuple[float, ...] | list[float],
) -> int:
    if len(previous) != NEURON_COUNT or len(current) != NEURON_COUNT:
        raise ValueError("unexpected neuron count")
    changed = 0
    for left in range(NEURON_COUNT):
        for right in range(left + 1, NEURON_COUNT):
            previous_relation = _pair_relation(
                float(previous[left]) - float(previous[right])
            )
            current_relation = _pair_relation(
                float(current[left]) - float(current[right])
            )
            changed += int(previous_relation != current_relation)
    return changed


def _relabel(
    values: tuple[float, ...], permutation: tuple[int, ...]
) -> tuple[float, ...]:
    if sorted(permutation) != list(range(len(values))):
        raise ValueError("invalid neuron permutation")
    return tuple(values[index] for index in permutation)


def _permutation(offset: int) -> tuple[int, ...]:
    order = tuple(range(NEURON_COUNT))
    shift = offset % NEURON_COUNT
    rotated = order[shift:] + order[:shift]
    return tuple(reversed(rotated)) if offset % 2 else rotated


def _observe_event(
    previous: tuple[float, ...],
    current: tuple[float, ...],
    permutation_offset: int,
) -> tuple[int, int]:
    event = _relation_change_count(previous, current)
    permutation = _permutation(permutation_offset)
    permuted_event = _relation_change_count(
        _relabel(previous, permutation),
        _relabel(current, permutation),
    )
    return event, int(event == permuted_event)


def _source_state(source_senses: tuple[dict, ...]) -> tuple[MiniMCMField, int]:
    field = MiniMCMField(neuron_count=NEURON_COUNT)
    previous = tuple(float(neuron.activation) for neuron in field.neurons)
    last_event = 0
    for tick, senses in enumerate(source_senses, start=1):
        state = field.step(senses)
        current = tuple(float(value) for value in state["activations"])
        last_event, invariant = _observe_event(previous, current, tick)
        if not invariant:
            raise RuntimeError("relation event changed under neuron relabeling")
        previous = current
    return field, last_event


def _event_prefix_profiles(
    source_field: MiniMCMField,
    previous_event: int,
    target_senses: tuple[dict, ...],
) -> tuple[dict[int, tuple[int, ...]], tuple[int, ...], int]:
    if len(target_senses) < PREFIX_TICKS[-1]:
        raise ValueError("target is shorter than event prefix scale")
    field = copy.deepcopy(source_field)
    previous = tuple(float(neuron.activation) for neuron in field.neurons)
    counts = [0] * PROFILE_SIZE
    events = []
    invariant_ticks = 0
    prior_event = int(previous_event)
    profiles = {}
    for tick, senses in enumerate(target_senses[: PREFIX_TICKS[-1]], start=1):
        state = field.step(senses)
        current = tuple(float(value) for value in state["activations"])
        event, invariant = _observe_event(previous, current, tick)
        delta = event - prior_event
        counts[event] += 1
        counts[EVENT_COUNT_SIZE + delta + PAIR_COUNT] += 1
        events.append(event)
        invariant_ticks += invariant
        if tick in PREFIX_TICKS:
            profiles[tick] = tuple(counts)
        previous = current
        prior_event = event
    return profiles, tuple(events), invariant_ticks


def _profile_component(values: tuple[int, ...], component: str) -> tuple[int, ...]:
    if component == "count":
        return values[:EVENT_COUNT_SIZE]
    if component == "delta":
        return values[EVENT_COUNT_SIZE:]
    if component == "combined":
        return values
    raise ValueError(f"unknown profile component: {component}")


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict], list[dict]]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    senses = {
        world.key: _world_senses(str(world.source), world.start)
        for world in worlds
    }
    source_states = {
        source.key: _source_state(senses[source.key])
        for source in sources
    }
    path_profiles = {}
    path_rows = []
    core_hash = hashlib.sha256(CORE_PATH.read_bytes()).hexdigest()
    for source in sources:
        source_field, previous_event = source_states[source.key]
        path_profiles[source.key] = {}
        for target in targets:
            profiles, events, invariant_ticks = _event_prefix_profiles(
                source_field,
                previous_event,
                senses[target.key],
            )
            path_profiles[source.key][target.key] = profiles
            path_rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "target_key_posthoc": target.key,
                    "target_universe": "a" if target in universe_a else "b",
                    "observed_ticks": len(events),
                    "minimum_relation_change_count": min(events),
                    "maximum_relation_change_count": max(events),
                    "unique_relation_change_counts": len(set(events)),
                    "nonzero_relation_change_ticks": sum(value > 0 for value in events),
                    "neuron_relabel_invariant_ticks": invariant_ticks,
                    "all_ticks_neuron_relabel_invariant": int(invariant_ticks == len(events)),
                    "profile_uses_neuron_identity": 0,
                    "profile_uses_fixed_threshold": 0,
                    "profile_uses_global_field_mean": 0,
                    "profile_available_during_contact": 1,
                    "production_core_sha256": core_hash,
                    "production_field_modified": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                    "viranz_parameter_used": 0,
                }
            )

    edge_rows = []
    summary_rows = []
    for prefix_ticks, component in (
        (prefix_ticks, component)
        for prefix_ticks in PREFIX_TICKS
        for component in PROFILE_COMPONENTS
    ):
        raw_a = {
            source.key: _sum_vectors([
                _profile_component(
                    path_profiles[source.key][target.key][prefix_ticks], component
                )
                for target in universe_a
            ])
            for source in sources
        }
        raw_b = {
            source.key: _sum_vectors([
                _profile_component(
                    path_profiles[source.key][target.key][prefix_ticks], component
                )
                for target in universe_b
            ])
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
        null_a = _label_null(
            [(matrix, keys)], metrics_a,
            f"2128|{dataset}|{prefix_ticks}|{component}|a_to_b",
        )
        null_b = _label_null(
            [(reverse_matrix, keys)], metrics_b,
            f"2128|{dataset}|{prefix_ticks}|{component}|b_to_a",
        )
        edges = _mutual_nearest_edges(matrix)
        same_source_edges = sum(left == right for left, right in edges)
        edge_null = _edge_label_null(
            edges,
            keys,
            same_source_edges,
            f"2128|{dataset}|{prefix_ticks}|{component}|edges",
        )
        for edge_index, (left_index, right_index) in enumerate(edges, start=1):
            edge_rows.append(
                {
                    "dataset": dataset,
                    "prefix_ticks": prefix_ticks,
                    "profile_component": component,
                    "edge_index": edge_index,
                    "left_anonymous_node": f"a_{left_index + 1:03d}",
                    "right_anonymous_node": f"b_{right_index + 1:03d}",
                    "distance": matrix[left_index][right_index],
                    "same_source_posthoc": int(left_index == right_index),
                    "left_source_posthoc": keys[left_index],
                    "right_source_posthoc": keys[right_index],
                    "graph_used_source_label": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
        summary_rows.append(
            {
                "dataset": dataset,
                "prefix_ticks": prefix_ticks,
                "profile_component": component,
                "source_identities": len(sources),
                "source_target_paths": len(sources) * len(targets),
                "all_path_ticks_neuron_relabel_invariant": int(
                    all(row["all_ticks_neuron_relabel_invariant"] for row in path_rows)
                ),
                "a_to_b_mean_identity_auc": metrics_a["mean_identity_auc"],
                "a_to_b_median_identity_rank": metrics_a["median_identity_rank"],
                "a_to_b_unique_nearest": metrics_a["identity_unique_nearest"],
                "a_to_b_label_null_max_auc": null_a["label_null_max_identity_auc"],
                "a_to_b_auc_label_p": null_a["identity_auc_label_p"],
                "b_to_a_mean_identity_auc": metrics_b["mean_identity_auc"],
                "b_to_a_median_identity_rank": metrics_b["median_identity_rank"],
                "b_to_a_unique_nearest": metrics_b["identity_unique_nearest"],
                "b_to_a_label_null_max_auc": null_b["label_null_max_identity_auc"],
                "b_to_a_auc_label_p": null_b["identity_auc_label_p"],
                "mutual_nearest_edges": len(edges),
                "same_source_mutual_edges_posthoc": same_source_edges,
                **edge_null,
                "event_uses_neuron_identity": 0,
                "event_uses_fixed_threshold": 0,
                "event_uses_global_field_mean": 0,
                "event_available_during_contact": 1,
                "production_field_modified": 0,
                "memory_written": 0,
                "influences_action": 0,
                "viranz_parameter_used": 0,
            }
        )
    return path_rows, edge_rows, summary_rows


def _all_rows() -> tuple[list[dict], list[dict], list[dict]]:
    worlds = _worlds()
    paths_out = []
    edges_out = []
    summaries_out = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected = [world for world in worlds if world.dataset == dataset]
        paths, edges, summaries = _dataset_rows(dataset, selected)
        paths_out.extend(paths)
        edges_out.extend(edges)
        summaries_out.extend(summaries)
    return paths_out, edges_out, summaries_out


def _write_csv(name: str, rows: list[dict]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    paths, edges, summaries = _all_rows()
    _write_csv("paths", paths)
    _write_csv("edges", edges)
    _write_csv("summary", summaries)
    print(f"paths={len(paths)} edges={len(edges)} summaries={len(summaries)}")
    for row in summaries:
        print(
            f"dataset={row['dataset']} ticks={row['prefix_ticks']} "
            f"component={row['profile_component']} "
            f"auc={row['a_to_b_mean_identity_auc']:.6f}/"
            f"{row['b_to_a_mean_identity_auc']:.6f} "
            f"nullmax={row['a_to_b_label_null_max_auc']:.6f}/"
            f"{row['b_to_a_label_null_max_auc']:.6f} "
            f"edges={row['same_source_mutual_edges_posthoc']}/"
            f"{row['mutual_nearest_edges']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
