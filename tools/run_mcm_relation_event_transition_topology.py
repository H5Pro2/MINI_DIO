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

from tools.run_mcm_relation_synchrony_topology import (
    BASIS_EVENT_ARCHIVE,
    BASIS_LIFECYCLE_ARCHIVE,
    HOLDOUT_ARCHIVE,
    _archive_rows,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2097_MCM_RELATIONSEREIGNIS_GETRAGENE_ZUSTANDSUEBERGANGSTOPOLOGIE"
GAP_PERMUTATIONS = 500
ACTIVITY_PERMUTATIONS = 200
SWAP_ATTEMPTS_PER_MUTABLE_EVENT = 20
SEED = 2097


def _event_sequences(rows: list[dict[str, str]]) -> dict[str, list[int]]:
    grouped: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for row in rows:
        grouped[row["neighborhood_symbol"]].append(
            (int(row["event_index"]), int(row["finalization_index"]))
        )
    result = {}
    for symbol, events in grouped.items():
        ordered = sorted(events)
        indexes = [index for index, _ in ordered]
        if indexes != list(range(1, len(indexes) + 1)):
            raise RuntimeError(f"non-consecutive event indexes for {symbol}")
        finalizations = [finalization for _, finalization in ordered]
        if any(left >= right for left, right in zip(finalizations, finalizations[1:])):
            raise RuntimeError(f"non-increasing event finalizations for {symbol}")
        result[symbol] = finalizations
    return result


def _topology_counters(
    sequences: dict[str, list[int]],
) -> tuple[Counter, Counter]:
    edges = Counter(
        (left, right)
        for sequence in sequences.values()
        for left, right in zip(sequence, sequence[1:])
    )
    paths = Counter(
        (left, middle, right)
        for sequence in sequences.values()
        for left, middle, right in zip(sequence, sequence[1:], sequence[2:])
    )
    return edges, paths


def _collision_pairs(counter: Counter) -> int:
    return sum(support * (support - 1) // 2 for support in counter.values())


def _metrics(sequences: dict[str, list[int]]) -> dict[str, object]:
    edges, paths = _topology_counters(sequences)
    event_rows = sum(len(sequence) for sequence in sequences.values())
    return {
        "relations": len(sequences),
        "event_rows": event_rows,
        "transition_links": sum(edges.values()),
        "transition_nodes": len(
            {node for edge in edges for node in edge}
        ),
        "unique_transition_edges": len(edges),
        "recurring_transition_edges": sum(support > 1 for support in edges.values()),
        "transition_links_on_recurring_edges": sum(
            support for support in edges.values() if support > 1
        ),
        "transition_collision_pairs": _collision_pairs(edges),
        "maximum_transition_support": max(edges.values(), default=0),
        "consecutive_world_transition_links": sum(
            support for (left, right), support in edges.items() if right == left + 1
        ),
        "two_step_path_instances": sum(paths.values()),
        "unique_two_step_paths": len(paths),
        "recurring_two_step_paths": sum(support > 1 for support in paths.values()),
        "two_step_instances_on_recurring_paths": sum(
            support for support in paths.values() if support > 1
        ),
        "two_step_path_collision_pairs": _collision_pairs(paths),
        "maximum_two_step_path_support": max(paths.values(), default=0),
    }


def _support_rows(
    dataset: str, sequences: dict[str, list[int]]
) -> list[dict[str, object]]:
    edges, paths = _topology_counters(sequences)
    rows = []
    for kind, counter in (("transition_edge", edges), ("two_step_path", paths)):
        distribution = Counter(counter.values())
        for support in sorted(distribution):
            structures = distribution[support]
            rows.append(
                {
                    "dataset": dataset,
                    "kind": kind,
                    "support": support,
                    "structures": structures,
                    "instances": support * structures,
                    "collision_pairs": support
                    * (support - 1)
                    // 2
                    * structures,
                }
            )
    return rows


def _gap_order_shuffle(
    sequences: dict[str, list[int]], rng: random.Random
) -> dict[str, list[int]]:
    result = {}
    for symbol, sequence in sequences.items():
        gaps = [right - left for left, right in zip(sequence, sequence[1:])]
        rng.shuffle(gaps)
        shuffled = [sequence[0]]
        for gap in gaps:
            shuffled.append(shuffled[-1] + gap)
        result[symbol] = shuffled
    return result


def _activity_preserving_rewire(
    sequences: dict[str, list[int]], rng: random.Random
) -> tuple[dict[str, list[int]], int, int]:
    event_sets = {symbol: set(sequence) for symbol, sequence in sequences.items()}
    bounds = {
        symbol: (sequence[0], sequence[-1])
        for symbol, sequence in sequences.items()
    }
    mutable = [
        [symbol, finalization]
        for symbol, sequence in sequences.items()
        for finalization in sequence[1:-1]
    ]
    if len(mutable) < 2:
        return (
            {symbol: list(sequence) for symbol, sequence in sequences.items()},
            0,
            0,
        )
    attempts = SWAP_ATTEMPTS_PER_MUTABLE_EVENT * len(mutable)
    accepted = 0
    for _ in range(attempts):
        left_index = rng.randrange(len(mutable))
        right_index = rng.randrange(len(mutable))
        if left_index == right_index:
            continue
        left_symbol, left_time = mutable[left_index]
        right_symbol, right_time = mutable[right_index]
        if left_symbol == right_symbol:
            continue
        left_start, left_end = bounds[left_symbol]
        right_start, right_end = bounds[right_symbol]
        if not left_start < right_time < left_end:
            continue
        if not right_start < left_time < right_end:
            continue
        if right_time in event_sets[left_symbol]:
            continue
        if left_time in event_sets[right_symbol]:
            continue
        event_sets[left_symbol].remove(left_time)
        event_sets[left_symbol].add(right_time)
        event_sets[right_symbol].remove(right_time)
        event_sets[right_symbol].add(left_time)
        mutable[left_index][1] = right_time
        mutable[right_index][1] = left_time
        accepted += 1
    return (
        {symbol: sorted(events) for symbol, events in event_sets.items()},
        accepted,
        attempts,
    )


def _null_row(
    control: str,
    metric: str,
    observed: int,
    values: list[int],
    direction: str,
    permutations: int,
    seed: int,
    accepted_swaps_mean: float | str = "",
    attempted_swaps: int | str = "",
) -> dict[str, object]:
    extreme = (
        sum(value >= observed for value in values)
        if direction == "higher"
        else sum(value <= observed for value in values)
    )
    return {
        "control": control,
        "metric": metric,
        "direction": direction,
        "observed": observed,
        "null_mean": statistics.mean(values),
        "null_sd": statistics.pstdev(values),
        "null_min": min(values),
        "null_max": max(values),
        "empirical_p": (1 + extreme) / (permutations + 1),
        "permutations": permutations,
        "seed": seed,
        "accepted_swaps_mean": accepted_swaps_mean,
        "attempted_swaps": attempted_swaps,
    }


def _null_rows(
    sequences: dict[str, list[int]], seed: int
) -> list[dict[str, object]]:
    observed = _metrics(sequences)
    primary = (
        ("unique_transition_edges", "lower"),
        ("transition_collision_pairs", "higher"),
        ("unique_two_step_paths", "lower"),
        ("two_step_path_collision_pairs", "higher"),
        ("maximum_transition_support", "higher"),
        ("maximum_two_step_path_support", "higher"),
    )
    gap_rng = random.Random(seed)
    gap_values = {metric: [] for metric, _ in primary}
    for _ in range(GAP_PERMUTATIONS):
        metrics = _metrics(_gap_order_shuffle(sequences, gap_rng))
        for metric in gap_values:
            gap_values[metric].append(int(metrics[metric]))

    activity_rng = random.Random(seed + 1)
    activity_values = {metric: [] for metric, _ in primary}
    accepted_swaps = []
    attempted_swaps = 0
    for _ in range(ACTIVITY_PERMUTATIONS):
        rewired, accepted, attempts = _activity_preserving_rewire(
            sequences, activity_rng
        )
        metrics = _metrics(rewired)
        for metric in activity_values:
            activity_values[metric].append(int(metrics[metric]))
        accepted_swaps.append(accepted)
        attempted_swaps = attempts

    rows = []
    for metric, direction in primary:
        rows.append(
            _null_row(
                "relation_internal_gap_order",
                metric,
                int(observed[metric]),
                gap_values[metric],
                direction,
                GAP_PERMUTATIONS,
                seed,
            )
        )
        rows.append(
            _null_row(
                "world_activity_and_relation_degree_preserving_swaps",
                metric,
                int(observed[metric]),
                activity_values[metric],
                direction,
                ACTIVITY_PERMUTATIONS,
                seed + 1,
                statistics.mean(accepted_swaps),
                attempted_swaps,
            )
        )
    return rows


def _analyze(
    dataset: str,
    event_archive: Path,
    order_archive: Path,
    seed: int,
) -> dict[str, object]:
    event_rows = _archive_rows(event_archive, "event_histories.csv")
    order_rows = _archive_rows(order_archive, "holdout_order.csv")
    sequences = _event_sequences(event_rows)
    metrics = _metrics(sequences)
    null_rows = _null_rows(sequences, seed)
    null_lookup = {
        (row["control"], row["metric"]): row for row in null_rows
    }
    summary = {
        "dataset": dataset,
        "worlds": len(order_rows),
        **metrics,
        "gap_transition_collision_p": null_lookup[
            ("relation_internal_gap_order", "transition_collision_pairs")
        ]["empirical_p"],
        "activity_transition_collision_p": null_lookup[
            (
                "world_activity_and_relation_degree_preserving_swaps",
                "transition_collision_pairs",
            )
        ]["empirical_p"],
        "gap_two_step_collision_p": null_lookup[
            ("relation_internal_gap_order", "two_step_path_collision_pairs")
        ]["empirical_p"],
        "activity_two_step_collision_p": null_lookup[
            (
                "world_activity_and_relation_degree_preserving_swaps",
                "two_step_path_collision_pairs",
            )
        ]["empirical_p"],
        "read_by_mini_dio": 0,
        "influences_field": 0,
        "influences_action": 0,
    }
    return {
        "metrics": [{"dataset": dataset, **metrics}],
        "support": _support_rows(dataset, sequences),
        "null": [{"dataset": dataset, **row} for row in null_rows],
        "summary": [summary],
    }


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
            SEED + 2,
        ),
    ]
    for name in ("metrics", "support", "null", "summary"):
        _write_csv(name, [row for result in analyses for row in result[name]])
    for result in analyses:
        summary = result["summary"][0]
        print(f"dataset={summary['dataset']}")
        print(f"transition_edges={summary['unique_transition_edges']}")
        print(f"transition_collisions={summary['transition_collision_pairs']}")
        print(f"two_step_paths={summary['unique_two_step_paths']}")
        print(f"two_step_collisions={summary['two_step_path_collision_pairs']}")
        print(
            "activity_transition_p="
            f"{summary['activity_transition_collision_p']}"
        )
        print(f"activity_two_step_p={summary['activity_two_step_collision_p']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
