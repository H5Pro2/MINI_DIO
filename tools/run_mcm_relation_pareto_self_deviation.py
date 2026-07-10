from __future__ import annotations

import csv
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neighborhood_consolidation import SUPPORT_AXES
from tools.run_mcm_relation_synchrony_topology import (
    BASIS_EVENT_ARCHIVE,
    BASIS_LIFECYCLE_ARCHIVE,
    HOLDOUT_ARCHIVE,
    _archive_rows,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2102_MCM_RELATIONALE_PARETO_SELBSTABWEICHUNG"
PERMUTATIONS = 100
SEED = 2102
PRIMARY_METRICS = (
    "depth_change_share",
    "mean_absolute_depth_change",
    "mean_world_depth_change_share",
)


def _event_trajectories(
    rows: list[dict[str, str]],
) -> dict[str, list[dict[str, int]]]:
    grouped: dict[str, list[tuple[int, dict[str, int]]]] = defaultdict(list)
    for row in rows:
        symbol = row["neighborhood_symbol"]
        event_index = int(row["event_index"])
        event = {
            "finalization_index": int(row["finalization_index"]),
            **{axis: int(row[axis]) for axis in SUPPORT_AXES},
        }
        grouped[symbol].append((event_index, event))

    trajectories = {}
    for symbol, indexed_events in grouped.items():
        ordered = sorted(indexed_events)
        indexes = [index for index, _ in ordered]
        if indexes != list(range(1, len(indexes) + 1)):
            raise RuntimeError(f"non-consecutive event indexes for {symbol}")
        events = [event for _, event in ordered]
        times = [event["finalization_index"] for event in events]
        if any(left >= right for left, right in zip(times, times[1:])):
            raise RuntimeError(f"non-increasing event finalizations for {symbol}")
        for axis in SUPPORT_AXES:
            values = [event[axis] for event in events]
            if any(left > right for left, right in zip(values, values[1:])):
                raise RuntimeError(f"decreasing {axis} for {symbol}")
        trajectories[symbol] = events
    return trajectories


def _pareto_depths_fast(
    state: dict[str, tuple[int, int, int]],
) -> dict[str, int]:
    if not state:
        return {}
    unique_values = sorted(set(state.values()), reverse=True)
    maximum_y = max(values[1] for values in unique_values)
    maximum_z = max(values[2] for values in unique_values)
    tree = [
        [0] * (maximum_z + 2)
        for _ in range(maximum_y + 2)
    ]
    value_depths: dict[tuple[int, int, int], int] = {}

    def query(y: int, z: int) -> int:
        y_index = maximum_y - y + 1
        z_limit = maximum_z - z + 1
        best = 0
        while y_index > 0:
            z_index = z_limit
            while z_index > 0:
                best = max(best, tree[y_index][z_index])
                z_index -= z_index & -z_index
            y_index -= y_index & -y_index
        return best

    def update(y: int, z: int, depth: int) -> None:
        y_index = maximum_y - y + 1
        z_start = maximum_z - z + 1
        while y_index <= maximum_y + 1:
            z_index = z_start
            while z_index <= maximum_z + 1:
                tree[y_index][z_index] = max(tree[y_index][z_index], depth)
                z_index += z_index & -z_index
            y_index += y_index & -y_index

    for values in unique_values:
        _, y, z = values
        depth = query(y, z) + 1
        value_depths[values] = depth
        update(y, z, depth)
    return {symbol: value_depths[values] for symbol, values in state.items()}


def _timing_age_signature(
    trajectories: dict[str, list[dict[str, int]]],
) -> Counter:
    return Counter(
        (event_index, event["finalization_index"])
        for events in trajectories.values()
        for event_index, event in enumerate(events, start=1)
    )


def _support_trajectory_signature(
    trajectories: dict[str, list[dict[str, int]]],
) -> dict[str, tuple[tuple[int, int, int], ...]]:
    return {
        symbol: tuple(tuple(event[axis] for axis in SUPPORT_AXES) for event in events)
        for symbol, events in trajectories.items()
    }


def _permute_timing_within_event_count(
    trajectories: dict[str, list[dict[str, int]]],
    rng: random.Random,
) -> dict[str, list[dict[str, int]]]:
    by_count: dict[int, list[str]] = defaultdict(list)
    for symbol, events in trajectories.items():
        by_count[len(events)].append(symbol)

    result = {}
    for count in sorted(by_count):
        targets = sorted(by_count[count])
        donors = list(targets)
        rng.shuffle(donors)
        for target, donor in zip(targets, donors):
            donor_times = [
                event["finalization_index"] for event in trajectories[donor]
            ]
            result[target] = [
                {
                    "finalization_index": donor_times[index],
                    **{axis: event[axis] for axis in SUPPORT_AXES},
                }
                for index, event in enumerate(trajectories[target])
            ]
    return result


def _reorganization_rows(
    trajectories: dict[str, list[dict[str, int]]],
    worlds: int,
) -> list[dict[str, object]]:
    events_by_finalization: dict[int, list[tuple[str, dict[str, int]]]] = (
        defaultdict(list)
    )
    for symbol, events in trajectories.items():
        for event in events:
            finalization = event["finalization_index"]
            if not 1 <= finalization <= worlds:
                raise RuntimeError(
                    f"event finalization outside causal world range: {finalization}"
                )
            events_by_finalization[finalization].append((symbol, event))

    state: dict[str, tuple[int, int, int]] = {}
    previous_depths: dict[str, int] = {}
    rows = []
    for finalization in range(1, worlds + 1):
        incoming = sorted(events_by_finalization.get(finalization, []))
        previous_symbols = set(previous_depths)
        for symbol, event in incoming:
            state[symbol] = tuple(event[axis] for axis in SUPPORT_AXES)
        depths = _pareto_depths_fast(state)
        shared = sorted(previous_symbols & set(depths))
        shallower = sum(depths[symbol] < previous_depths[symbol] for symbol in shared)
        deeper = sum(depths[symbol] > previous_depths[symbol] for symbol in shared)
        unchanged = len(shared) - shallower - deeper
        absolute_change = sum(
            abs(depths[symbol] - previous_depths[symbol]) for symbol in shared
        )
        changed = shallower + deeper
        rows.append(
            {
                "finalization_index": finalization,
                "incoming_relation_events": len(incoming),
                "incoming_existing_relations": sum(
                    symbol in previous_symbols for symbol, _ in incoming
                ),
                "new_relations": len(set(depths) - previous_symbols),
                "active_relations": len(depths),
                "shared_relations": len(shared),
                "previous_maximum_pareto_depth": max(
                    previous_depths.values(), default=0
                ),
                "current_maximum_pareto_depth": max(depths.values(), default=0),
                "moved_shallower": shallower,
                "moved_deeper": deeper,
                "unchanged_depth": unchanged,
                "depth_change_count": changed,
                "depth_change_share": changed / max(1, len(shared)),
                "absolute_depth_change_sum": absolute_change,
                "mean_absolute_depth_change": absolute_change
                / max(1, len(shared)),
                "future_event_reads": 0,
            }
        )
        previous_depths = depths
    return rows


def _phase_summary(
    rows: list[dict[str, object]],
    phase: str,
) -> dict[str, object]:
    worlds = len(rows)
    if phase == "first_half":
        selected = rows[: worlds // 2]
    elif phase == "second_half":
        selected = rows[worlds // 2 :]
    elif phase == "all":
        selected = rows
    else:
        raise ValueError(f"unknown phase: {phase}")
    shared = sum(int(row["shared_relations"]) for row in selected)
    changed = sum(int(row["depth_change_count"]) for row in selected)
    absolute = sum(int(row["absolute_depth_change_sum"]) for row in selected)
    informative = [row for row in selected if int(row["shared_relations"]) > 0]
    return {
        "phase": phase,
        "worlds": len(selected),
        "shared_relation_comparisons": shared,
        "depth_changes": changed,
        "depth_change_share": changed / max(1, shared),
        "absolute_depth_change_sum": absolute,
        "mean_absolute_depth_change": absolute / max(1, shared),
        "mean_world_depth_change_share": statistics.mean(
            float(row["depth_change_share"]) for row in informative
        )
        if informative
        else 0.0,
        "moved_shallower": sum(int(row["moved_shallower"]) for row in selected),
        "moved_deeper": sum(int(row["moved_deeper"]) for row in selected),
        "worlds_with_depth_change": sum(
            int(row["depth_change_count"]) > 0 for row in selected
        ),
    }


def _null_row(
    phase: str,
    metric: str,
    observed: float,
    values: list[float],
    seed: int,
) -> dict[str, object]:
    null_mean = statistics.mean(values)
    lower_p = (1 + sum(value <= observed for value in values)) / (len(values) + 1)
    upper_p = (1 + sum(value >= observed for value in values)) / (len(values) + 1)
    return {
        "control": "world_activity_event_age_and_support_trajectory_preserving",
        "phase": phase,
        "metric": metric,
        "observed": observed,
        "null_mean": null_mean,
        "null_sd": statistics.pstdev(values),
        "null_min": min(values),
        "null_max": max(values),
        "observed_minus_null_mean": observed - null_mean,
        "lower_empirical_p": lower_p,
        "upper_empirical_p": upper_p,
        "two_sided_empirical_p": min(1.0, 2.0 * min(lower_p, upper_p)),
        "permutations": len(values),
        "seed": seed,
    }


def _analyze(
    dataset: str,
    event_archive: Path,
    order_archive: Path,
    seed: int,
) -> dict[str, list[dict[str, object]]]:
    event_rows = _archive_rows(event_archive, "event_histories.csv")
    order_rows = _archive_rows(order_archive, "holdout_order.csv")
    trajectories = _event_trajectories(event_rows)
    worlds = len(order_rows)
    observed_rows = _reorganization_rows(trajectories, worlds)
    phases = ("all", "first_half", "second_half")
    observed_phases = {
        phase: _phase_summary(observed_rows, phase) for phase in phases
    }

    timing_signature = _timing_age_signature(trajectories)
    support_signature = _support_trajectory_signature(trajectories)
    rng = random.Random(seed)
    null_values = {
        (phase, metric): [] for phase in phases for metric in PRIMARY_METRICS
    }
    world_null_sums = [0.0] * worlds
    for _ in range(PERMUTATIONS):
        permuted = _permute_timing_within_event_count(trajectories, rng)
        if _timing_age_signature(permuted) != timing_signature:
            raise RuntimeError("timing-age signature changed under null")
        if _support_trajectory_signature(permuted) != support_signature:
            raise RuntimeError("support trajectory changed under null")
        permuted_rows = _reorganization_rows(permuted, worlds)
        for index, row in enumerate(permuted_rows):
            world_null_sums[index] += float(row["depth_change_share"])
        for phase in phases:
            summary = _phase_summary(permuted_rows, phase)
            for metric in PRIMARY_METRICS:
                null_values[(phase, metric)].append(float(summary[metric]))

    snapshots = []
    for index, row in enumerate(observed_rows):
        null_mean = world_null_sums[index] / PERMUTATIONS
        snapshots.append(
            {
                "dataset": dataset,
                **row,
                "null_mean_depth_change_share": null_mean,
                "observed_minus_null_mean_depth_change_share": float(
                    row["depth_change_share"]
                )
                - null_mean,
            }
        )

    worlds_above_null = sum(
        float(row["observed_minus_null_mean_depth_change_share"]) > 0
        for row in snapshots
        if int(row["shared_relations"]) > 0
    )
    worlds_below_null = sum(
        float(row["observed_minus_null_mean_depth_change_share"]) < 0
        for row in snapshots
        if int(row["shared_relations"]) > 0
    )
    worlds_equal_null = sum(
        float(row["observed_minus_null_mean_depth_change_share"]) == 0
        for row in snapshots
        if int(row["shared_relations"]) > 0
    )

    null_rows = []
    for phase in phases:
        for metric in PRIMARY_METRICS:
            null_rows.append(
                {
                    "dataset": dataset,
                    **_null_row(
                        phase,
                        metric,
                        float(observed_phases[phase][metric]),
                        null_values[(phase, metric)],
                        seed,
                    ),
                }
            )

    all_summary = observed_phases["all"]
    lookup = {(row["phase"], row["metric"]): row for row in null_rows}
    summary = {
        "dataset": dataset,
        "worlds": worlds,
        "relations": len(trajectories),
        "event_rows": len(event_rows),
        **all_summary,
        "depth_change_null_mean": lookup[("all", "depth_change_share")][
            "null_mean"
        ],
        "depth_change_observed_minus_null": lookup[
            ("all", "depth_change_share")
        ]["observed_minus_null_mean"],
        "depth_change_two_sided_p": lookup[("all", "depth_change_share")][
            "two_sided_empirical_p"
        ],
        "absolute_change_null_mean": lookup[
            ("all", "mean_absolute_depth_change")
        ]["null_mean"],
        "absolute_change_observed_minus_null": lookup[
            ("all", "mean_absolute_depth_change")
        ]["observed_minus_null_mean"],
        "absolute_change_two_sided_p": lookup[
            ("all", "mean_absolute_depth_change")
        ]["two_sided_empirical_p"],
        "mean_world_depth_change_share": all_summary[
            "mean_world_depth_change_share"
        ],
        "mean_world_depth_change_null_mean": lookup[
            ("all", "mean_world_depth_change_share")
        ]["null_mean"],
        "mean_world_depth_change_observed_minus_null": lookup[
            ("all", "mean_world_depth_change_share")
        ]["observed_minus_null_mean"],
        "mean_world_depth_change_two_sided_p": lookup[
            ("all", "mean_world_depth_change_share")
        ]["two_sided_empirical_p"],
        "worlds_above_null_mean": worlds_above_null,
        "worlds_below_null_mean": worlds_below_null,
        "worlds_equal_null_mean": worlds_equal_null,
        "future_event_reads": sum(
            int(row["future_event_reads"]) for row in observed_rows
        ),
        "additional_memory_required": 0,
        "read_by_mini_dio": 0,
        "influences_field": 0,
        "influences_action": 0,
    }
    return {"snapshots": snapshots, "null": null_rows, "summary": [summary]}


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    fieldnames = []
    for row in rows:
        for field in row:
            if field not in fieldnames:
                fieldnames.append(field)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    analyses = [
        _analyze(
            "2091_basis",
            BASIS_EVENT_ARCHIVE,
            BASIS_LIFECYCLE_ARCHIVE,
            SEED,
        ),
        _analyze(
            "2092_holdout",
            HOLDOUT_ARCHIVE,
            HOLDOUT_ARCHIVE,
            SEED + 1,
        ),
    ]
    for name in ("snapshots", "null", "summary"):
        _write_csv(name, [row for result in analyses for row in result[name]])
    for result in analyses:
        summary = result["summary"][0]
        print(f"dataset={summary['dataset']}")
        print(f"depth_change_share={summary['depth_change_share']}")
        print(
            "depth_change_observed_minus_null="
            f"{summary['depth_change_observed_minus_null']}"
        )
        print(f"depth_change_p={summary['depth_change_two_sided_p']}")
        print(
            "absolute_change_observed_minus_null="
            f"{summary['absolute_change_observed_minus_null']}"
        )
        print(f"absolute_change_p={summary['absolute_change_two_sided_p']}")
        print(f"future_event_reads={summary['future_event_reads']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
