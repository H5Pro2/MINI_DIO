from __future__ import annotations

import csv
import hashlib
import random
import statistics
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_continuous_field_instance import _world_senses, _worlds
from tools.run_mcm_continuity_source_identity import (
    _identity_observations,
    _label_null,
    _observed_metrics,
    _shape_vector,
)
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_intrinsic_form_self_readability import (
    _edge_label_null,
    _mutual_nearest_edges,
)
from tools.run_mcm_label_invariant_relational_event_carrier import (
    PREFIX_TICKS,
    _event_prefix_profiles,
    _source_state,
)
from tools.run_mcm_passive_observer_boundary import _empirical_upper_p, _seed


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2129_MCM_PASSIVE_TRIADEN_RELATIONSMOBILITAET"
CORE_PATH = ROOT / "mini_dio" / "mcm_neuron.py"
PERMUTATIONS = 32
HORIZON = PREFIX_TICKS[-1]
PAIR_SLOTS = ((0, 1), (0, 2), (1, 2))
CENTER_SLOTS = (0, 1, 2)


def _hash_key(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _source_triads(sources: list) -> tuple[tuple, ...]:
    ordered = tuple(sorted(sources, key=lambda item: (_hash_key(item.key), item.key)))
    triads = [ordered[index : index + 3] for index in range(0, len(ordered) - 2, 3)]
    remainder = len(ordered) % 3
    if remainder:
        tail = ordered[-remainder:]
        triads.append(tail + ordered[: 3 - remainder])
    return tuple(tuple(triad) for triad in triads)


def _mutual_nearest_pairs(values: tuple[int, int, int]) -> tuple[tuple[int, int], ...]:
    distances = {
        pair: abs(values[pair[0]] - values[pair[1]])
        for pair in PAIR_SLOTS
    }
    nearest = {}
    for field_index in range(3):
        incident = {
            pair: distance
            for pair, distance in distances.items()
            if field_index in pair
        }
        minimum = min(incident.values())
        nearest[field_index] = {
            pair for pair, distance in incident.items() if distance == minimum
        }
    return tuple(
        pair
        for pair in PAIR_SLOTS
        if pair in nearest[pair[0]] and pair in nearest[pair[1]]
    )


def _medoid_centers(values: tuple[int, int, int]) -> tuple[int, ...]:
    scores = tuple(
        sum(abs(values[field_index] - values[other]) for other in range(3))
        for field_index in range(3)
    )
    minimum = min(scores)
    return tuple(index for index, score in enumerate(scores) if score == minimum)


def _relation_traces(
    delta_sequences: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]],
) -> tuple[tuple[tuple[tuple[int, int], ...], ...], tuple[tuple[int, ...], ...]]:
    if len({len(sequence) for sequence in delta_sequences}) != 1:
        raise ValueError("triad sequences differ in length")
    edge_states = []
    center_states = []
    for tick in range(len(delta_sequences[0])):
        values = tuple(sequence[tick] for sequence in delta_sequences)
        edge_states.append(_mutual_nearest_pairs(values))
        center_states.append(_medoid_centers(values))
    return tuple(edge_states), tuple(center_states)


def _collision_count(states: tuple) -> int:
    counts = Counter(states)
    return sum(support * (support - 1) // 2 for support in counts.values())


def _collision_rate(states: tuple) -> float:
    opportunities = len(states) * (len(states) - 1) // 2
    return _collision_count(states) / opportunities if opportunities else 0.0


def _state_changes(states: tuple) -> int:
    return sum(left != right for left, right in zip(states, states[1:]))


def _support_vector(
    states: tuple,
    slots: tuple,
) -> tuple[int, ...]:
    return tuple(sum(slot in state for state in states) for slot in slots)


def _trace_metrics(delta_sequences: tuple[tuple[int, ...], ...]) -> dict[str, object]:
    edges, centers = _relation_traces(delta_sequences)
    edge_support = _support_vector(edges, PAIR_SLOTS)
    center_support = _support_vector(centers, CENTER_SLOTS)
    strict_edges = []
    strict_centers = []
    for tick in range(len(delta_sequences[0])):
        values = tuple(sequence[tick] for sequence in delta_sequences)
        if len(set(values)) == 3:
            strict_edges.append(edges[tick][0])
            strict_centers.append(centers[tick][0])
    strict_edge_support = tuple(strict_edges.count(slot) for slot in PAIR_SLOTS)
    strict_center_support = tuple(strict_centers.count(slot) for slot in CENTER_SLOTS)
    return {
        "edge_states": edges,
        "center_states": centers,
        "edge_collision_count": _collision_count(edges),
        "center_collision_count": _collision_count(centers),
        "edge_state_changes": _state_changes(edges),
        "center_state_changes": _state_changes(centers),
        "distinct_edge_states": len(set(edges)),
        "distinct_center_states": len(set(centers)),
        "multi_edge_ticks": sum(len(state) > 1 for state in edges),
        "multi_center_ticks": sum(len(state) > 1 for state in centers),
        "edge_support": edge_support,
        "center_support": center_support,
        "strict_distinct_ticks": len(strict_edges),
        "strict_edge_collision_count": _collision_count(tuple(strict_edges)),
        "strict_center_collision_count": _collision_count(tuple(strict_centers)),
        "strict_edge_collision_rate": _collision_rate(tuple(strict_edges)),
        "strict_center_collision_rate": _collision_rate(tuple(strict_centers)),
        "strict_edge_support": strict_edge_support,
        "strict_center_support": strict_center_support,
    }


def _triad_shifts(label: str, horizon: int) -> tuple[int, int, int]:
    rng = random.Random(_seed(label))
    shifts = tuple(rng.randrange(horizon) for _ in range(3))
    if len(set(shifts)) == 1:
        shifts = (shifts[0], shifts[1], (shifts[2] + 1) % horizon)
    return shifts


def _shift_sequences(
    sequences: tuple[tuple[int, ...], ...], shifts: tuple[int, int, int]
) -> tuple[tuple[int, ...], ...]:
    horizon = len(sequences[0])
    return tuple(
        tuple(sequence[(tick + shifts[index]) % horizon] for tick in range(horizon))
        for index, sequence in enumerate(sequences)
    )


def _event_deltas(previous_event: int, events: tuple[int, ...]) -> tuple[int, ...]:
    deltas = []
    prior = int(previous_event)
    for event in events:
        deltas.append(int(event) - prior)
        prior = int(event)
    return tuple(deltas)


def _temporal_summary(dataset: str, paths: list[dict]) -> list[dict]:
    rows = []
    for scope in ("a", "b", "all"):
        selected = [row for row in paths if scope == "all" or row["target_universe"] == scope]
        edge_observed = sum(int(row["edge_collision_count"]) for row in selected)
        center_observed = sum(int(row["center_collision_count"]) for row in selected)
        edge_nulls = [
            sum(int(row[f"edge_null_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        center_nulls = [
            sum(int(row[f"center_null_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        strict_edge_observed = sum(int(row["strict_edge_collision_count"]) for row in selected)
        strict_center_observed = sum(int(row["strict_center_collision_count"]) for row in selected)
        strict_edge_nulls = [
            sum(int(row[f"strict_edge_null_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        strict_center_nulls = [
            sum(int(row[f"strict_center_null_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        strict_edge_rate_observed = sum(float(row["strict_edge_collision_rate"]) for row in selected)
        strict_center_rate_observed = sum(float(row["strict_center_collision_rate"]) for row in selected)
        strict_edge_rate_nulls = [
            sum(float(row[f"strict_edge_rate_null_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        strict_center_rate_nulls = [
            sum(float(row[f"strict_center_rate_null_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        rows.append(
            {
                "dataset": dataset,
                "universe_scope": scope,
                "triad_paths": len(selected),
                "triads": len({row["triad_index"] for row in selected}),
                "edge_collision_excess": edge_observed - statistics.fmean(edge_nulls),
                "edge_empirical_upper_p": _empirical_upper_p(edge_observed, edge_nulls),
                "center_collision_excess": center_observed - statistics.fmean(center_nulls),
                "center_empirical_upper_p": _empirical_upper_p(center_observed, center_nulls),
                "strict_edge_collision_excess": strict_edge_observed - statistics.fmean(strict_edge_nulls),
                "strict_edge_empirical_upper_p": _empirical_upper_p(strict_edge_observed, strict_edge_nulls),
                "strict_center_collision_excess": strict_center_observed - statistics.fmean(strict_center_nulls),
                "strict_center_empirical_upper_p": _empirical_upper_p(strict_center_observed, strict_center_nulls),
                "strict_edge_rate_excess": strict_edge_rate_observed - statistics.fmean(strict_edge_rate_nulls),
                "strict_edge_rate_empirical_upper_p": _empirical_upper_p(strict_edge_rate_observed, strict_edge_rate_nulls),
                "strict_center_rate_excess": strict_center_rate_observed - statistics.fmean(strict_center_rate_nulls),
                "strict_center_rate_empirical_upper_p": _empirical_upper_p(strict_center_rate_observed, strict_center_rate_nulls),
                "positive_edge_excess_paths": sum(float(row["edge_collision_excess"]) > 0 for row in selected),
                "positive_center_excess_paths": sum(float(row["center_collision_excess"]) > 0 for row in selected),
                "mean_edge_state_changes": statistics.fmean(int(row["edge_state_changes"]) for row in selected),
                "mean_center_state_changes": statistics.fmean(int(row["center_state_changes"]) for row in selected),
                "mean_distinct_edge_states": statistics.fmean(int(row["distinct_edge_states"]) for row in selected),
                "mean_distinct_center_states": statistics.fmean(int(row["distinct_center_states"]) for row in selected),
                "mean_strict_distinct_ticks": statistics.fmean(int(row["strict_distinct_ticks"]) for row in selected),
                "fields_connected": 0,
                "production_field_modified": 0,
                "memory_written": 0,
                "influences_action": 0,
                "viranz_parameter_used": 0,
            }
        )
    return rows


def _transfer_rows(
    dataset: str,
    triads: tuple[tuple, ...],
    path_internal: list[dict],
) -> tuple[list[dict], list[dict]]:
    transfer_rows = []
    graph_rows = []
    for component in (
        "edge",
        "center",
        "combined",
        "strict_edge",
        "strict_center",
        "strict_combined",
    ):
        raw_a = {}
        raw_b = {}
        for triad_index in range(1, len(triads) + 1):
            triad_paths = [row for row in path_internal if row["triad_index"] == triad_index]
            edge_a = tuple(sum(row["edge_support"][slot] for row in triad_paths if row["target_universe"] == "a") for slot in range(3))
            edge_b = tuple(sum(row["edge_support"][slot] for row in triad_paths if row["target_universe"] == "b") for slot in range(3))
            center_a = tuple(sum(row["center_support"][slot] for row in triad_paths if row["target_universe"] == "a") for slot in range(3))
            center_b = tuple(sum(row["center_support"][slot] for row in triad_paths if row["target_universe"] == "b") for slot in range(3))
            strict_edge_a = tuple(sum(row["strict_edge_support"][slot] for row in triad_paths if row["target_universe"] == "a") for slot in range(3))
            strict_edge_b = tuple(sum(row["strict_edge_support"][slot] for row in triad_paths if row["target_universe"] == "b") for slot in range(3))
            strict_center_a = tuple(sum(row["strict_center_support"][slot] for row in triad_paths if row["target_universe"] == "a") for slot in range(3))
            strict_center_b = tuple(sum(row["strict_center_support"][slot] for row in triad_paths if row["target_universe"] == "b") for slot in range(3))
            key = f"triad_{triad_index:03d}"
            if component == "edge":
                raw_a[key], raw_b[key] = edge_a, edge_b
            elif component == "center":
                raw_a[key], raw_b[key] = center_a, center_b
            elif component == "strict_edge":
                raw_a[key], raw_b[key] = strict_edge_a, strict_edge_b
            elif component == "strict_center":
                raw_a[key], raw_b[key] = strict_center_a, strict_center_b
            elif component == "strict_combined":
                raw_a[key], raw_b[key] = (
                    strict_edge_a + strict_center_a,
                    strict_edge_b + strict_center_b,
                )
            else:
                raw_a[key], raw_b[key] = edge_a + center_a, edge_b + center_b
        profiles_a = {key: _shape_vector(values) for key, values in raw_a.items()}
        profiles_b = {key: _shape_vector(values) for key, values in raw_b.items()}
        observations_a, matrix, keys = _identity_observations(profiles_a, profiles_b)
        observations_b, reverse_matrix, reverse_keys = _identity_observations(profiles_b, profiles_a)
        if keys != reverse_keys:
            raise RuntimeError("triad identity order differs")
        metrics_a = _observed_metrics(observations_a)
        metrics_b = _observed_metrics(observations_b)
        null_a = _label_null([(matrix, keys)], metrics_a, f"2129|{dataset}|{component}|a_to_b")
        null_b = _label_null([(reverse_matrix, keys)], metrics_b, f"2129|{dataset}|{component}|b_to_a")
        edges = _mutual_nearest_edges(matrix)
        same_triad_edges = sum(left == right for left, right in edges)
        edge_null = _edge_label_null(edges, keys, same_triad_edges, f"2129|{dataset}|{component}|edges")
        for edge_index, (left_index, right_index) in enumerate(edges, start=1):
            graph_rows.append(
                {
                    "dataset": dataset,
                    "profile_component": component,
                    "edge_index": edge_index,
                    "left_anonymous_node": f"a_{left_index + 1:03d}",
                    "right_anonymous_node": f"b_{right_index + 1:03d}",
                    "distance": matrix[left_index][right_index],
                    "same_triad_posthoc": int(left_index == right_index),
                    "left_triad_posthoc": keys[left_index],
                    "right_triad_posthoc": keys[right_index],
                    "graph_used_triad_label": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
        transfer_rows.append(
            {
                "dataset": dataset,
                "profile_component": component,
                "triads": len(triads),
                "a_to_b_mean_identity_auc": metrics_a["mean_identity_auc"],
                "a_to_b_median_identity_rank": metrics_a["median_identity_rank"],
                "a_to_b_label_null_max_auc": null_a["label_null_max_identity_auc"],
                "a_to_b_auc_label_p": null_a["identity_auc_label_p"],
                "b_to_a_mean_identity_auc": metrics_b["mean_identity_auc"],
                "b_to_a_median_identity_rank": metrics_b["median_identity_rank"],
                "b_to_a_label_null_max_auc": null_b["label_null_max_identity_auc"],
                "b_to_a_auc_label_p": null_b["identity_auc_label_p"],
                "mutual_nearest_edges": len(edges),
                "same_triad_mutual_edges_posthoc": same_triad_edges,
                **edge_null,
                "profile_used_source_label": 0,
                "fields_connected": 0,
                "production_field_modified": 0,
                "memory_written": 0,
                "influences_action": 0,
                "viranz_parameter_used": 0,
            }
        )
    return transfer_rows, graph_rows


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    triads = _source_triads(sources)
    senses = {world.key: _world_senses(str(world.source), world.start) for world in worlds}
    source_states = {source.key: _source_state(senses[source.key]) for source in sources}
    event_sequences = {}
    for source in sources:
        source_field, previous_event = source_states[source.key]
        event_sequences[source.key] = {}
        for target in targets:
            _, events, invariant_ticks = _event_prefix_profiles(source_field, previous_event, senses[target.key])
            if invariant_ticks != HORIZON:
                raise RuntimeError("2128 event lost relabel invariance")
            event_sequences[source.key][target.key] = _event_deltas(previous_event, events)

    core_hash = hashlib.sha256(CORE_PATH.read_bytes()).hexdigest()
    path_rows = []
    internal_rows = []
    for triad_index, triad in enumerate(triads, start=1):
        for target in targets:
            sequences = tuple(event_sequences[source.key][target.key] for source in triad)
            observed = _trace_metrics(sequences)
            edge_nulls = []
            center_nulls = []
            strict_edge_nulls = []
            strict_center_nulls = []
            strict_edge_rate_nulls = []
            strict_center_rate_nulls = []
            for permutation_index in range(PERMUTATIONS):
                shifts = _triad_shifts(
                    f"2129|{dataset}|{triad_index}|{target.key}|{permutation_index}",
                    HORIZON,
                )
                null_metrics = _trace_metrics(_shift_sequences(sequences, shifts))
                edge_nulls.append(int(null_metrics["edge_collision_count"]))
                center_nulls.append(int(null_metrics["center_collision_count"]))
                strict_edge_nulls.append(int(null_metrics["strict_edge_collision_count"]))
                strict_center_nulls.append(int(null_metrics["strict_center_collision_count"]))
                strict_edge_rate_nulls.append(float(null_metrics["strict_edge_collision_rate"]))
                strict_center_rate_nulls.append(float(null_metrics["strict_center_collision_rate"]))
            universe = "a" if target in universe_a else "b"
            internal_rows.append(
                {
                    "triad_index": triad_index,
                    "target_universe": universe,
                    "edge_support": observed["edge_support"],
                    "center_support": observed["center_support"],
                    "strict_edge_support": observed["strict_edge_support"],
                    "strict_center_support": observed["strict_center_support"],
                }
            )
            path_rows.append(
                {
                    "dataset": dataset,
                    "triad_index": triad_index,
                    "source_0_posthoc": triad[0].key,
                    "source_1_posthoc": triad[1].key,
                    "source_2_posthoc": triad[2].key,
                    "target_key_posthoc": target.key,
                    "target_universe": universe,
                    "observed_ticks": HORIZON,
                    "edge_collision_count": observed["edge_collision_count"],
                    "edge_null_mean": statistics.fmean(edge_nulls),
                    "edge_collision_excess": observed["edge_collision_count"] - statistics.fmean(edge_nulls),
                    "center_collision_count": observed["center_collision_count"],
                    "center_null_mean": statistics.fmean(center_nulls),
                    "center_collision_excess": observed["center_collision_count"] - statistics.fmean(center_nulls),
                    "strict_distinct_ticks": observed["strict_distinct_ticks"],
                    "strict_edge_collision_count": observed["strict_edge_collision_count"],
                    "strict_edge_null_mean": statistics.fmean(strict_edge_nulls),
                    "strict_edge_collision_excess": observed["strict_edge_collision_count"] - statistics.fmean(strict_edge_nulls),
                    "strict_center_collision_count": observed["strict_center_collision_count"],
                    "strict_center_null_mean": statistics.fmean(strict_center_nulls),
                    "strict_center_collision_excess": observed["strict_center_collision_count"] - statistics.fmean(strict_center_nulls),
                    "strict_edge_collision_rate": observed["strict_edge_collision_rate"],
                    "strict_edge_rate_null_mean": statistics.fmean(strict_edge_rate_nulls),
                    "strict_edge_rate_excess": observed["strict_edge_collision_rate"] - statistics.fmean(strict_edge_rate_nulls),
                    "strict_center_collision_rate": observed["strict_center_collision_rate"],
                    "strict_center_rate_null_mean": statistics.fmean(strict_center_rate_nulls),
                    "strict_center_rate_excess": observed["strict_center_collision_rate"] - statistics.fmean(strict_center_rate_nulls),
                    "edge_state_changes": observed["edge_state_changes"],
                    "center_state_changes": observed["center_state_changes"],
                    "distinct_edge_states": observed["distinct_edge_states"],
                    "distinct_center_states": observed["distinct_center_states"],
                    "multi_edge_ticks": observed["multi_edge_ticks"],
                    "multi_center_ticks": observed["multi_center_ticks"],
                    "edge_support_01": observed["edge_support"][0],
                    "edge_support_02": observed["edge_support"][1],
                    "edge_support_12": observed["edge_support"][2],
                    "center_support_0": observed["center_support"][0],
                    "center_support_1": observed["center_support"][1],
                    "center_support_2": observed["center_support"][2],
                    "strict_edge_support_01": observed["strict_edge_support"][0],
                    "strict_edge_support_02": observed["strict_edge_support"][1],
                    "strict_edge_support_12": observed["strict_edge_support"][2],
                    "strict_center_support_0": observed["strict_center_support"][0],
                    "strict_center_support_1": observed["strict_center_support"][1],
                    "strict_center_support_2": observed["strict_center_support"][2],
                    "source_grouping_used_asset_or_year": 0,
                    "fields_connected": 0,
                    "production_core_sha256": core_hash,
                    "production_field_modified": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                    "viranz_parameter_used": 0,
                    **{f"edge_null_{index:02d}": value for index, value in enumerate(edge_nulls)},
                    **{f"center_null_{index:02d}": value for index, value in enumerate(center_nulls)},
                    **{f"strict_edge_null_{index:02d}": value for index, value in enumerate(strict_edge_nulls)},
                    **{f"strict_center_null_{index:02d}": value for index, value in enumerate(strict_center_nulls)},
                    **{f"strict_edge_rate_null_{index:02d}": value for index, value in enumerate(strict_edge_rate_nulls)},
                    **{f"strict_center_rate_null_{index:02d}": value for index, value in enumerate(strict_center_rate_nulls)},
                }
            )
    temporal = _temporal_summary(dataset, path_rows)
    transfer, graph = _transfer_rows(dataset, triads, internal_rows)
    return path_rows, temporal, transfer, graph


def _all_rows() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    worlds = _worlds()
    paths_out = []
    temporal_out = []
    transfer_out = []
    graph_out = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected = [world for world in worlds if world.dataset == dataset]
        paths, temporal, transfer, graph = _dataset_rows(dataset, selected)
        paths_out.extend(paths)
        temporal_out.extend(temporal)
        transfer_out.extend(transfer)
        graph_out.extend(graph)
    return paths_out, temporal_out, transfer_out, graph_out


def _write_csv(name: str, rows: list[dict]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    paths, temporal, transfer, graph = _all_rows()
    for name, rows in (("paths", paths), ("temporal", temporal), ("transfer", transfer), ("graph", graph)):
        _write_csv(name, rows)
    print(f"paths={len(paths)} temporal={len(temporal)} transfer={len(transfer)} graph={len(graph)}")
    for row in temporal:
        print(
            f"dataset={row['dataset']} scope={row['universe_scope']} "
            f"edge_excess={row['edge_collision_excess']:.3f} "
            f"center_excess={row['center_collision_excess']:.3f}"
        )
    for row in transfer:
        print(
            f"dataset={row['dataset']} component={row['profile_component']} "
            f"auc={row['a_to_b_mean_identity_auc']:.6f}/"
            f"{row['b_to_a_mean_identity_auc']:.6f} "
            f"same={row['same_triad_mutual_edges_posthoc']}/"
            f"{row['mutual_nearest_edges']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
