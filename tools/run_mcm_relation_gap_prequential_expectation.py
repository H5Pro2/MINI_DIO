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

from tools.run_mcm_relation_event_transition_topology import (
    _activity_preserving_rewire,
    _event_sequences,
    _gap_order_shuffle,
)
from tools.run_mcm_relation_synchrony_topology import (
    BASIS_EVENT_ARCHIVE,
    BASIS_LIFECYCLE_ARCHIVE,
    HOLDOUT_ARCHIVE,
    _archive_rows,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2098_MCM_RELATIONSGAP_PRAEQUENTIELLE_ERWARTUNG"
GAP_PERMUTATIONS = 200
ACTIVITY_PERMUTATIONS = 50
SEED = 2098


def _percentile_score(
    counts: Counter, actual: int, candidate_values: set[int]
) -> float:
    candidates = set(candidate_values)
    candidates.add(actual)
    if len(candidates) == 1:
        return 1.0
    actual_count = counts.get(actual, 0)
    greater = sum(counts.get(value, 0) > actual_count for value in candidates)
    equal = sum(counts.get(value, 0) == actual_count for value in candidates)
    average_rank = greater + (equal + 1) / 2
    return 1.0 - (average_rank - 1) / (len(candidates) - 1)


def _prequential_rows(
    sequences: dict[str, list[int]],
) -> tuple[list[dict[str, object]], int]:
    gap_records = []
    transition_records = []
    predictions = []
    for symbol, sequence in sequences.items():
        gaps = [right - left for left, right in zip(sequence, sequence[1:])]
        for index, gap in enumerate(gaps):
            gap_records.append((sequence[index + 1], symbol, gap))
        for index, (previous_gap, next_gap) in enumerate(zip(gaps, gaps[1:])):
            transition_records.append(
                (sequence[index + 2], symbol, previous_gap, next_gap)
            )
            predictions.append(
                (
                    sequence[index + 1],
                    sequence[index + 2],
                    symbol,
                    previous_gap,
                    next_gap,
                )
            )
    gap_records.sort()
    transition_records.sort()
    predictions.sort()

    global_counts: Counter = Counter()
    relation_counts: dict[str, Counter] = defaultdict(Counter)
    conditional_counts: dict[int, Counter] = defaultdict(Counter)
    candidates: set[int] = set()
    gap_index = 0
    transition_index = 0
    future_training_reads = 0
    rows = []
    for origin, target_end, symbol, previous_gap, actual_gap in predictions:
        while (
            gap_index < len(gap_records)
            and gap_records[gap_index][0] <= origin
        ):
            end, relation, gap = gap_records[gap_index]
            future_training_reads += int(end > origin)
            global_counts[gap] += 1
            relation_counts[relation][gap] += 1
            candidates.add(gap)
            gap_index += 1
        while (
            transition_index < len(transition_records)
            and transition_records[transition_index][0] <= origin
        ):
            end, _, left_gap, right_gap = transition_records[transition_index]
            future_training_reads += int(end > origin)
            conditional_counts[left_gap][right_gap] += 1
            transition_index += 1

        conditional = conditional_counts[previous_gap]
        conditional_score = _percentile_score(
            conditional, actual_gap, candidates
        )
        global_score = _percentile_score(global_counts, actual_gap, candidates)
        relation_score = _percentile_score(
            relation_counts[symbol], actual_gap, candidates
        )
        rows.append(
            {
                "prediction_origin": origin,
                "target_event_finalization": target_end,
                "relation": symbol,
                "previous_gap": previous_gap,
                "actual_next_gap": actual_gap,
                "known_gap_values": len(candidates),
                "conditional_history_count": sum(conditional.values()),
                "conditional_history_known": int(bool(conditional)),
                "conditional_percentile_score": conditional_score,
                "global_percentile_score": global_score,
                "relation_percentile_score": relation_score,
                "conditional_minus_global": conditional_score - global_score,
                "conditional_minus_relation": conditional_score - relation_score,
                "maximum_training_finalization": origin,
            }
        )
    return rows, future_training_reads


def _summary(rows: list[dict[str, object]]) -> dict[str, object]:
    conditional = [float(row["conditional_percentile_score"]) for row in rows]
    global_scores = [float(row["global_percentile_score"]) for row in rows]
    relation = [float(row["relation_percentile_score"]) for row in rows]
    versus_global = [left - right for left, right in zip(conditional, global_scores)]
    versus_relation = [left - right for left, right in zip(conditional, relation)]
    return {
        "predictions": len(rows),
        "conditional_history_known": sum(
            int(row["conditional_history_known"]) for row in rows
        ),
        "conditional_history_known_share": sum(
            int(row["conditional_history_known"]) for row in rows
        )
        / max(1, len(rows)),
        "conditional_mean_percentile_score": statistics.mean(conditional),
        "global_mean_percentile_score": statistics.mean(global_scores),
        "relation_mean_percentile_score": statistics.mean(relation),
        "conditional_minus_global_mean": statistics.mean(versus_global),
        "conditional_minus_relation_mean": statistics.mean(versus_relation),
        "conditional_better_than_global": sum(value > 0.0 for value in versus_global),
        "conditional_equal_to_global": sum(value == 0.0 for value in versus_global),
        "conditional_worse_than_global": sum(value < 0.0 for value in versus_global),
        "conditional_global_nontie_win_share": sum(
            value > 0.0 for value in versus_global
        )
        / max(1, sum(value != 0.0 for value in versus_global)),
        "conditional_better_than_relation": sum(
            value > 0.0 for value in versus_relation
        ),
        "conditional_equal_to_relation": sum(
            value == 0.0 for value in versus_relation
        ),
        "conditional_worse_than_relation": sum(
            value < 0.0 for value in versus_relation
        ),
    }


def _aggregate_rows(
    dataset: str,
    rows: list[dict[str, object]],
    field: str,
    output_name: str,
) -> list[dict[str, object]]:
    grouped: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[int(row[field])].append(row)
    result = []
    for value, group in sorted(grouped.items()):
        summary = _summary(group)
        result.append(
            {
                "dataset": dataset,
                output_name: value,
                **summary,
            }
        )
    return result


def _null_row(
    control: str,
    metric: str,
    observed: float,
    values: list[float],
    permutations: int,
    seed: int,
    accepted_swaps_mean: float | str = "",
    attempted_swaps: int | str = "",
) -> dict[str, object]:
    return {
        "control": control,
        "metric": metric,
        "direction": "higher",
        "observed": observed,
        "null_mean": statistics.mean(values),
        "null_sd": statistics.pstdev(values),
        "null_min": min(values),
        "null_max": max(values),
        "empirical_p_ge_observed": (
            1 + sum(value >= observed for value in values)
        )
        / (permutations + 1),
        "permutations": permutations,
        "seed": seed,
        "accepted_swaps_mean": accepted_swaps_mean,
        "attempted_swaps": attempted_swaps,
    }


def _null_rows(
    sequences: dict[str, list[int]], seed: int
) -> list[dict[str, object]]:
    observed_rows, _ = _prequential_rows(sequences)
    observed = _summary(observed_rows)
    metrics = (
        "conditional_minus_global_mean",
        "conditional_minus_relation_mean",
    )

    gap_rng = random.Random(seed)
    gap_values = {metric: [] for metric in metrics}
    for _ in range(GAP_PERMUTATIONS):
        rows, _ = _prequential_rows(_gap_order_shuffle(sequences, gap_rng))
        summary = _summary(rows)
        for metric in metrics:
            gap_values[metric].append(float(summary[metric]))

    activity_rng = random.Random(seed + 1)
    activity_values = {metric: [] for metric in metrics}
    accepted_swaps = []
    attempted_swaps = 0
    for _ in range(ACTIVITY_PERMUTATIONS):
        rewired, accepted, attempts = _activity_preserving_rewire(
            sequences, activity_rng
        )
        rows, _ = _prequential_rows(rewired)
        summary = _summary(rows)
        for metric in metrics:
            activity_values[metric].append(float(summary[metric]))
        accepted_swaps.append(accepted)
        attempted_swaps = attempts

    result = []
    for metric in metrics:
        result.append(
            _null_row(
                "relation_internal_gap_order",
                metric,
                float(observed[metric]),
                gap_values[metric],
                GAP_PERMUTATIONS,
                seed,
            )
        )
        result.append(
            _null_row(
                "world_activity_and_relation_degree_preserving_swaps",
                metric,
                float(observed[metric]),
                activity_values[metric],
                ACTIVITY_PERMUTATIONS,
                seed + 1,
                statistics.mean(accepted_swaps),
                attempted_swaps,
            )
        )
    return result


def _analyze(
    dataset: str,
    event_archive: Path,
    order_archive: Path,
    seed: int,
) -> dict[str, object]:
    event_rows = _archive_rows(event_archive, "event_histories.csv")
    worlds = len(_archive_rows(order_archive, "holdout_order.csv"))
    sequences = _event_sequences(event_rows)
    rows, future_reads = _prequential_rows(sequences)
    summary = {
        "dataset": dataset,
        "worlds": worlds,
        "relations": len(sequences),
        **_summary(rows),
        "future_training_reads": future_reads,
        "read_by_mini_dio": 0,
        "influences_field": 0,
        "influences_action": 0,
    }
    null_rows = _null_rows(sequences, seed)
    lookup = {(row["control"], row["metric"]): row for row in null_rows}
    summary["gap_null_conditional_vs_global_p"] = lookup[
        ("relation_internal_gap_order", "conditional_minus_global_mean")
    ]["empirical_p_ge_observed"]
    summary["activity_null_conditional_vs_global_p"] = lookup[
        (
            "world_activity_and_relation_degree_preserving_swaps",
            "conditional_minus_global_mean",
        )
    ]["empirical_p_ge_observed"]
    return {
        "origins": _aggregate_rows(
            dataset, rows, "prediction_origin", "prediction_origin"
        ),
        "previous_gaps": _aggregate_rows(
            dataset, rows, "previous_gap", "previous_gap"
        ),
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
    for name in ("origins", "previous_gaps", "null", "summary"):
        _write_csv(name, [row for result in analyses for row in result[name]])
    for result in analyses:
        summary = result["summary"][0]
        print(f"dataset={summary['dataset']}")
        print(f"predictions={summary['predictions']}")
        print(
            "conditional_minus_global="
            f"{summary['conditional_minus_global_mean']}"
        )
        print(
            "conditional_minus_relation="
            f"{summary['conditional_minus_relation_mean']}"
        )
        print(f"future_training_reads={summary['future_training_reads']}")
        print(
            "activity_global_p="
            f"{summary['activity_null_conditional_vs_global_p']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
