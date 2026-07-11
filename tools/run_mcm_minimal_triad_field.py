from __future__ import annotations

import copy
import csv
import hashlib
import random
import statistics
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neuron import MiniMCMField, flatten_senses
from tools.run_mcm_continuous_field_instance import (
    NEURON_COUNT,
    _contact_field,
    _world_senses,
    _worlds,
)
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_passive_observer_boundary import (
    FieldFrame,
    _empirical_upper_p,
    _seed,
    _trace_digest,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2127_MCM_MINIMALES_TRIADENFELD"
CORE_PATH = ROOT / "mini_dio" / "mcm_neuron.py"
PERMUTATIONS = 32

LocalState = tuple[int, int, int]


def _source_triads(sources: list) -> tuple[tuple, ...]:
    ordered = tuple(sorted(sources, key=lambda item: item.key))
    triads = [ordered[index : index + 3] for index in range(0, len(ordered) - 2, 3)]
    remainder = len(ordered) % 3
    if remainder:
        tail = ordered[-remainder:]
        triads.append(tail + ordered[: 3 - remainder])
    return tuple(tuple(triad) for triad in triads)


def _step_with_boundary(
    field: MiniMCMField,
    senses: dict,
    boundary_signal: float,
) -> tuple[FieldFrame, float, float]:
    flat = flatten_senses(senses)
    previous = float(boundary_signal)
    activations = []
    for neuron in field.neurons:
        activation = neuron.step(flat, previous)
        activations.append(activation)
        previous = activation
    signature = sum(activations) / max(1, len(activations))
    field.last_signature = signature
    afterimages = tuple(float(neuron.afterimage) for neuron in field.neurons)
    return (
        FieldFrame(
            activations=tuple(float(value) for value in activations),
            afterimages=afterimages,
        ),
        signature,
        statistics.fmean(afterimages),
    )


def _run_target_triad(
    source_fields: tuple[MiniMCMField, MiniMCMField, MiniMCMField],
    target_senses: tuple[dict, ...],
    *,
    connected: bool,
) -> tuple[tuple[FieldFrame, ...], tuple[tuple[float, ...], ...], tuple[tuple[float, ...], ...]]:
    fields = [copy.deepcopy(field) for field in source_fields]
    traces = [[], [], []]
    signatures = [[], [], []]
    afterimage_means = [[], [], []]
    previous_signatures = [float(field.last_signature) for field in fields]
    for senses in target_senses:
        boundaries = (
            [
                statistics.fmean(
                    previous_signatures[other]
                    for other in range(3)
                    if other != field_index
                )
                for field_index in range(3)
            ]
            if connected
            else [0.0, 0.0, 0.0]
        )
        current_signatures = []
        for field_index, field in enumerate(fields):
            frame, signature, afterimage_mean = _step_with_boundary(
                field,
                senses,
                boundaries[field_index],
            )
            traces[field_index].append(frame)
            signatures[field_index].append(signature)
            afterimage_means[field_index].append(afterimage_mean)
            current_signatures.append(signature)
        previous_signatures = current_signatures
    return (
        tuple(tuple(trace) for trace in traces),
        tuple(tuple(values) for values in signatures),
        tuple(tuple(values) for values in afterimage_means),
    )


def _rank_disagreement(frame: FieldFrame) -> int:
    disagreement = 0
    for left, right in combinations(range(len(frame.activations)), 2):
        activation_order = (frame.activations[left] > frame.activations[right]) - (
            frame.activations[left] < frame.activations[right]
        )
        afterimage_order = (frame.afterimages[left] > frame.afterimages[right]) - (
            frame.afterimages[left] < frame.afterimages[right]
        )
        disagreement += int(activation_order != afterimage_order)
    return disagreement


def _local_state(frame: FieldFrame) -> LocalState:
    activation_mean = statistics.fmean(frame.activations)
    afterimage_mean = statistics.fmean(frame.afterimages)
    return (
        sum(value > activation_mean for value in frame.activations),
        sum(value > afterimage_mean for value in frame.afterimages),
        _rank_disagreement(frame),
    )


def _local_sequences(
    traces: tuple[tuple[FieldFrame, ...], ...],
) -> tuple[tuple[LocalState, ...], ...]:
    return tuple(
        tuple(_local_state(frame) for frame in trace)
        for trace in traces
    )


def _joint_states(
    sequences: tuple[tuple[LocalState, ...], ...],
) -> tuple[tuple[LocalState, ...], ...]:
    return tuple(
        tuple(sorted(sequences[field_index][tick] for field_index in range(3)))
        for tick in range(len(sequences[0]))
    )


def _transition_collisions(joint_states: tuple) -> int:
    counter = Counter(zip(joint_states, joint_states[1:]))
    return sum(support * (support - 1) // 2 for support in counter.values())


def _shifted_transition_collisions(
    sequences: tuple[tuple[LocalState, ...], ...],
    shifts: tuple[int, int, int],
) -> int:
    horizon = len(sequences[0])
    shifted = tuple(
        tuple(
            sequences[field_index][(tick + shifts[field_index]) % horizon]
            for tick in range(horizon)
        )
        for field_index in range(3)
    )
    return _transition_collisions(_joint_states(shifted))


def _triad_shifts(label: str, horizon: int) -> tuple[int, int, int]:
    rng = random.Random(_seed(label))
    shifts = tuple(rng.randrange(horizon) for _ in range(3))
    if len(set(shifts)) == 1:
        shifts = (shifts[0], shifts[1], (shifts[2] + 1) % horizon)
    return shifts


def _midranks(values: tuple[int, int, int]) -> tuple[float, float, float]:
    order = sorted(range(3), key=lambda index: values[index])
    ranks = [0.0, 0.0, 0.0]
    index = 0
    while index < 3:
        end = index + 1
        while end < 3 and values[order[end]] == values[order[index]]:
            end += 1
        rank = (index + end - 1) / 2.0
        for offset in range(index, end):
            ranks[order[offset]] = rank
        index = end
    return tuple(ranks)


def _center_metrics(
    sequences: tuple[tuple[LocalState, ...], ...],
) -> tuple[int, int, int, float]:
    centers = []
    for tick in range(len(sequences[0])):
        states = [sequences[field_index][tick] for field_index in range(3)]
        scores = [0.0, 0.0, 0.0]
        for coordinate in range(3):
            ranks = _midranks(tuple(state[coordinate] for state in states))
            for field_index, rank in enumerate(ranks):
                scores[field_index] += (rank - 1.0) ** 2
        minimum = min(scores)
        winners = [index for index, score in enumerate(scores) if score == minimum]
        centers.append(winners[0] if len(winners) == 1 else -1)
    unique = [center for center in centers if center >= 0]
    changes = sum(left != right for left, right in zip(unique, unique[1:]))
    counts = Counter(unique)
    return (
        len(unique),
        len(counts),
        changes,
        max(counts.values(), default=0) / max(1, len(unique)),
    )


def _convergence_tick(sequences: tuple[tuple[LocalState, ...], ...]) -> int:
    equal = [
        len({sequences[field_index][tick] for field_index in range(3)}) == 1
        for tick in range(len(sequences[0]))
    ]
    last_not_equal = max((index for index, value in enumerate(equal) if not value), default=-1)
    return last_not_equal + 2 if last_not_equal + 1 < len(equal) else len(equal) + 1


def _triad_metrics(
    traces: tuple[tuple[FieldFrame, ...], ...],
    signatures: tuple[tuple[float, ...], ...],
    afterimage_means: tuple[tuple[float, ...], ...],
) -> dict[str, object]:
    sequences = _local_sequences(traces)
    horizon = len(sequences[0])
    pair_disagreement = statistics.fmean(
        statistics.fmean(
            sequences[left][tick] != sequences[right][tick]
            for left, right in combinations(range(3), 2)
        )
        for tick in range(horizon)
    )
    signature_variance = statistics.fmean(
        statistics.pvariance(signatures[field_index][tick] for field_index in range(3))
        for tick in range(horizon)
    )
    afterimage_variance = statistics.fmean(
        statistics.pvariance(
            afterimage_means[field_index][tick] for field_index in range(3)
        )
        for tick in range(horizon)
    )
    unique_center_ticks, distinct_centers, center_changes, max_center_share = (
        _center_metrics(sequences)
    )
    return {
        "sequences": sequences,
        "joint_transition_collisions": _transition_collisions(
            _joint_states(sequences)
        ),
        "mean_pair_state_disagreement": pair_disagreement,
        "mean_signature_variance": signature_variance,
        "mean_afterimage_variance": afterimage_variance,
        "convergence_tick": _convergence_tick(sequences),
        "unique_center_ticks": unique_center_ticks,
        "distinct_center_fields": distinct_centers,
        "center_changes": center_changes,
        "max_center_share": max_center_share,
    }


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict]]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    universes = {target.key: "a" if target in universe_a else "b" for target in targets}
    senses = {world.key: _world_senses(str(world.source), world.start) for world in worlds}
    source_fields = {
        source.key: _contact_field(senses[source.key])
        for source in sources
    }
    triads = _source_triads(sources)
    triad_rows = [
        {
            "dataset": dataset,
            "triad_index": index,
            "source_0": triad[0].key,
            "source_1": triad[1].key,
            "source_2": triad[2].key,
            "unique_sources": len({source.key for source in triad}),
            "semantic_roles_assigned": 0,
        }
        for index, triad in enumerate(triads, start=1)
    ]
    rows = []
    for triad_index, triad in enumerate(triads, start=1):
        fields = tuple(source_fields[source.key] for source in triad)
        for target in targets:
            connected = _run_target_triad(fields, senses[target.key], connected=True)
            isolated = _run_target_triad(fields, senses[target.key], connected=False)
            connected_metrics = _triad_metrics(*connected)
            isolated_metrics = _triad_metrics(*isolated)
            connected_nulls = []
            isolated_nulls = []
            for permutation in range(PERMUTATIONS):
                shifts = _triad_shifts(
                    f"2127|{dataset}|{triad_index}|{target.key}|{permutation}",
                    len(connected[0][0]),
                )
                connected_nulls.append(
                    _shifted_transition_collisions(
                        connected_metrics["sequences"], shifts
                    )
                )
                isolated_nulls.append(
                    _shifted_transition_collisions(
                        isolated_metrics["sequences"], shifts
                    )
                )
            connected_observed = int(connected_metrics["joint_transition_collisions"])
            isolated_observed = int(isolated_metrics["joint_transition_collisions"])
            rows.append(
                {
                    "dataset": dataset,
                    "triad_index": triad_index,
                    "source_0_posthoc": triad[0].key,
                    "source_1_posthoc": triad[1].key,
                    "source_2_posthoc": triad[2].key,
                    "target_key_posthoc": target.key,
                    "target_universe": universes[target.key],
                    "target_ticks": len(connected[0][0]),
                    "connected_joint_transition_collisions": connected_observed,
                    "connected_null_mean": round(statistics.fmean(connected_nulls), 6),
                    "connected_collision_excess": round(
                        connected_observed - statistics.fmean(connected_nulls), 6
                    ),
                    "isolated_joint_transition_collisions": isolated_observed,
                    "isolated_null_mean": round(statistics.fmean(isolated_nulls), 6),
                    "isolated_collision_excess": round(
                        isolated_observed - statistics.fmean(isolated_nulls), 6
                    ),
                    "connected_minus_isolated_excess": round(
                        (connected_observed - statistics.fmean(connected_nulls))
                        - (isolated_observed - statistics.fmean(isolated_nulls)),
                        6,
                    ),
                    **{
                        f"connected_{key}": round(value, 9)
                        if isinstance(value, float)
                        else value
                        for key, value in connected_metrics.items()
                        if key != "sequences" and key != "joint_transition_collisions"
                    },
                    **{
                        f"isolated_{key}": round(value, 9)
                        if isinstance(value, float)
                        else value
                        for key, value in isolated_metrics.items()
                        if key != "sequences" and key != "joint_transition_collisions"
                    },
                    "no_central_field": 1,
                    "symmetric_previous_tick_exchange": 1,
                    "microfield_semantic_roles_assigned": 0,
                    "microfield_identity_affects_joint_state": 0,
                    "production_field_modified": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                    "viranz_parameter_used": 0,
                    **{
                        f"connected_null_{index:02d}": value
                        for index, value in enumerate(connected_nulls)
                    },
                    **{
                        f"isolated_null_{index:02d}": value
                        for index, value in enumerate(isolated_nulls)
                    },
                }
            )
    return rows, triad_rows


def _summary_rows(dataset: str, paths: list[dict]) -> list[dict]:
    summaries = []
    for scope in ("a", "b", "all"):
        selected = [row for row in paths if scope == "all" or row["target_universe"] == scope]
        connected_observed = sum(int(row["connected_joint_transition_collisions"]) for row in selected)
        isolated_observed = sum(int(row["isolated_joint_transition_collisions"]) for row in selected)
        connected_nulls = [
            sum(int(row[f"connected_null_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        isolated_nulls = [
            sum(int(row[f"isolated_null_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        connected_excess = connected_observed - statistics.fmean(connected_nulls)
        isolated_excess = isolated_observed - statistics.fmean(isolated_nulls)
        summaries.append(
            {
                "dataset": dataset,
                "universe_scope": scope,
                "triad_paths": len(selected),
                "triads": len({row["triad_index"] for row in selected}),
                "connected_collision_excess": round(connected_excess, 6),
                "connected_empirical_upper_p": round(
                    _empirical_upper_p(connected_observed, connected_nulls), 6
                ),
                "isolated_collision_excess": round(isolated_excess, 6),
                "isolated_empirical_upper_p": round(
                    _empirical_upper_p(isolated_observed, isolated_nulls), 6
                ),
                "connected_minus_isolated_excess": round(
                    connected_excess - isolated_excess, 6
                ),
                "connected_higher_excess_paths": sum(
                    float(row["connected_minus_isolated_excess"]) > 0
                    for row in selected
                ),
                "isolated_higher_excess_paths": sum(
                    float(row["connected_minus_isolated_excess"]) < 0
                    for row in selected
                ),
                "connected_mean_pair_state_disagreement": round(
                    statistics.fmean(float(row["connected_mean_pair_state_disagreement"]) for row in selected), 9
                ),
                "isolated_mean_pair_state_disagreement": round(
                    statistics.fmean(float(row["isolated_mean_pair_state_disagreement"]) for row in selected), 9
                ),
                "connected_mean_signature_variance": round(
                    statistics.fmean(float(row["connected_mean_signature_variance"]) for row in selected), 12
                ),
                "isolated_mean_signature_variance": round(
                    statistics.fmean(float(row["isolated_mean_signature_variance"]) for row in selected), 12
                ),
                "connected_mean_afterimage_variance": round(
                    statistics.fmean(float(row["connected_mean_afterimage_variance"]) for row in selected), 12
                ),
                "isolated_mean_afterimage_variance": round(
                    statistics.fmean(float(row["isolated_mean_afterimage_variance"]) for row in selected), 12
                ),
                "connected_median_convergence_tick": statistics.median(
                    int(row["connected_convergence_tick"]) for row in selected
                ),
                "isolated_median_convergence_tick": statistics.median(
                    int(row["isolated_convergence_tick"]) for row in selected
                ),
                "connected_dynamic_center_paths": sum(
                    int(row["connected_distinct_center_fields"]) > 1
                    and int(row["connected_center_changes"]) > 0
                    for row in selected
                ),
                "connected_no_unique_center_paths": sum(
                    int(row["connected_unique_center_ticks"]) == 0
                    for row in selected
                ),
                "no_central_field": 1,
                "production_field_modified": 0,
                "memory_written": 0,
                "influences_action": 0,
                "viranz_parameter_used": 0,
            }
        )
    return summaries


def _all_rows() -> tuple[list[dict], list[dict], list[dict]]:
    core_hash_before = hashlib.sha256(CORE_PATH.read_bytes()).hexdigest()
    worlds = _worlds()
    paths_out = []
    triads_out = []
    summaries_out = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected_worlds = [world for world in worlds if world.dataset == dataset]
        paths, triads = _dataset_rows(dataset, selected_worlds)
        paths_out.extend(paths)
        triads_out.extend(triads)
        summaries_out.extend(_summary_rows(dataset, paths))
    core_hash_after = hashlib.sha256(CORE_PATH.read_bytes()).hexdigest()
    for row in paths_out:
        row["production_core_sha256"] = core_hash_before
        row["production_core_unchanged"] = int(core_hash_before == core_hash_after)
    return paths_out, triads_out, summaries_out


def _write_csv(name: str, rows: list[dict]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    fieldnames = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    paths, triads, summaries = _all_rows()
    for name, rows in (("paths", paths), ("triads", triads), ("summary", summaries)):
        _write_csv(name, rows)
    print(f"paths={len(paths)} triads={len(triads)} core_unchanged={sum(row['production_core_unchanged'] for row in paths)}")
    for row in summaries:
        print(
            f"dataset={row['dataset']} scope={row['universe_scope']} "
            f"connected_excess={row['connected_collision_excess']} "
            f"isolated_excess={row['isolated_collision_excess']} "
            f"difference={row['connected_minus_isolated_excess']} "
            f"disagreement={row['connected_mean_pair_state_disagreement']}/"
            f"{row['isolated_mean_pair_state_disagreement']} "
            f"center={row['connected_dynamic_center_paths']}/{row['triad_paths']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
