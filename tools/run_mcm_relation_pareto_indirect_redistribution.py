from __future__ import annotations

import csv
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neighborhood_consolidation import SUPPORT_AXES
from tools.run_mcm_relation_pareto_self_deviation import (
    _event_trajectories,
    _null_row,
    _pareto_depths_fast,
    _permute_timing_within_event_count,
    _support_trajectory_signature,
    _timing_age_signature,
)
from tools.run_mcm_relation_synchrony_topology import (
    BASIS_EVENT_ARCHIVE,
    BASIS_LIFECYCLE_ARCHIVE,
    HOLDOUT_ARCHIVE,
    _archive_rows,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2103_MCM_PARETO_INDIREKTE_FELDUMVERTEILUNG"
PERMUTATIONS = 100
SEED = 2103
PRIMARY_METRICS = (
    "indirect_depth_change_share",
    "indirect_mean_absolute_depth_change",
    "indirect_minus_direct_depth_change_share",
    "mean_world_indirect_depth_change_share",
)


def _movement(
    symbols: set[str],
    previous_depths: dict[str, int],
    depths: dict[str, int],
) -> dict[str, object]:
    shallower = sum(depths[symbol] < previous_depths[symbol] for symbol in symbols)
    deeper = sum(depths[symbol] > previous_depths[symbol] for symbol in symbols)
    changed = shallower + deeper
    absolute = sum(
        abs(depths[symbol] - previous_depths[symbol]) for symbol in symbols
    )
    return {
        "relations": len(symbols),
        "moved_shallower": shallower,
        "moved_deeper": deeper,
        "unchanged": len(symbols) - changed,
        "depth_changes": changed,
        "depth_change_share": changed / max(1, len(symbols)),
        "absolute_depth_change_sum": absolute,
        "mean_absolute_depth_change": absolute / max(1, len(symbols)),
    }


def _redistribution_rows(
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
        incoming_symbols = {symbol for symbol, _ in incoming}
        for symbol, event in incoming:
            state[symbol] = tuple(event[axis] for axis in SUPPORT_AXES)
        depths = _pareto_depths_fast(state)
        shared = previous_symbols & set(depths)
        direct_symbols = shared & incoming_symbols
        indirect_symbols = shared - incoming_symbols
        direct = _movement(direct_symbols, previous_depths, depths)
        indirect = _movement(indirect_symbols, previous_depths, depths)
        all_changes = int(direct["depth_changes"]) + int(
            indirect["depth_changes"]
        )
        rows.append(
            {
                "finalization_index": finalization,
                "incoming_relation_events": len(incoming),
                "new_relations": len(set(depths) - previous_symbols),
                "active_relations": len(depths),
                "shared_relations": len(shared),
                "direct_relations": direct["relations"],
                "direct_moved_shallower": direct["moved_shallower"],
                "direct_moved_deeper": direct["moved_deeper"],
                "direct_unchanged": direct["unchanged"],
                "direct_depth_changes": direct["depth_changes"],
                "direct_depth_change_share": direct["depth_change_share"],
                "direct_absolute_depth_change_sum": direct[
                    "absolute_depth_change_sum"
                ],
                "direct_mean_absolute_depth_change": direct[
                    "mean_absolute_depth_change"
                ],
                "indirect_relations": indirect["relations"],
                "indirect_moved_shallower": indirect["moved_shallower"],
                "indirect_moved_deeper": indirect["moved_deeper"],
                "indirect_unchanged": indirect["unchanged"],
                "indirect_depth_changes": indirect["depth_changes"],
                "indirect_depth_change_share": indirect["depth_change_share"],
                "indirect_absolute_depth_change_sum": indirect[
                    "absolute_depth_change_sum"
                ],
                "indirect_mean_absolute_depth_change": indirect[
                    "mean_absolute_depth_change"
                ],
                "indirect_minus_direct_depth_change_share": float(
                    indirect["depth_change_share"]
                )
                - float(direct["depth_change_share"]),
                "indirect_share_of_all_depth_changes": int(
                    indirect["depth_changes"]
                )
                / max(1, all_changes),
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

    direct_relations = sum(int(row["direct_relations"]) for row in selected)
    indirect_relations = sum(int(row["indirect_relations"]) for row in selected)
    direct_changes = sum(int(row["direct_depth_changes"]) for row in selected)
    indirect_changes = sum(int(row["indirect_depth_changes"]) for row in selected)
    indirect_absolute = sum(
        int(row["indirect_absolute_depth_change_sum"]) for row in selected
    )
    direct_share = direct_changes / max(1, direct_relations)
    indirect_share = indirect_changes / max(1, indirect_relations)
    informative = [row for row in selected if int(row["indirect_relations"]) > 0]
    return {
        "phase": phase,
        "worlds": len(selected),
        "direct_relation_comparisons": direct_relations,
        "direct_depth_changes": direct_changes,
        "direct_depth_change_share": direct_share,
        "indirect_relation_comparisons": indirect_relations,
        "indirect_depth_changes": indirect_changes,
        "indirect_depth_change_share": indirect_share,
        "indirect_absolute_depth_change_sum": indirect_absolute,
        "indirect_mean_absolute_depth_change": indirect_absolute
        / max(1, indirect_relations),
        "indirect_minus_direct_depth_change_share": indirect_share
        - direct_share,
        "indirect_share_of_all_depth_changes": indirect_changes
        / max(1, direct_changes + indirect_changes),
        "mean_world_indirect_depth_change_share": statistics.mean(
            float(row["indirect_depth_change_share"]) for row in informative
        )
        if informative
        else 0.0,
        "worlds_with_indirect_depth_change": sum(
            int(row["indirect_depth_changes"]) > 0 for row in informative
        ),
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
    observed_rows = _redistribution_rows(trajectories, worlds)
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
        permuted_rows = _redistribution_rows(permuted, worlds)
        for index, row in enumerate(permuted_rows):
            world_null_sums[index] += float(row["indirect_depth_change_share"])
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
                "null_mean_indirect_depth_change_share": null_mean,
                "observed_minus_null_mean_indirect_depth_change_share": float(
                    row["indirect_depth_change_share"]
                )
                - null_mean,
            }
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
    lookup = {(row["phase"], row["metric"]): row for row in null_rows}
    all_summary = observed_phases["all"]
    summary = {
        "dataset": dataset,
        "worlds": worlds,
        "relations": len(trajectories),
        "event_rows": len(event_rows),
        **all_summary,
        "indirect_change_null_mean": lookup[
            ("all", "indirect_depth_change_share")
        ]["null_mean"],
        "indirect_change_observed_minus_null": lookup[
            ("all", "indirect_depth_change_share")
        ]["observed_minus_null_mean"],
        "indirect_change_two_sided_p": lookup[
            ("all", "indirect_depth_change_share")
        ]["two_sided_empirical_p"],
        "indirect_absolute_null_mean": lookup[
            ("all", "indirect_mean_absolute_depth_change")
        ]["null_mean"],
        "indirect_absolute_observed_minus_null": lookup[
            ("all", "indirect_mean_absolute_depth_change")
        ]["observed_minus_null_mean"],
        "indirect_absolute_two_sided_p": lookup[
            ("all", "indirect_mean_absolute_depth_change")
        ]["two_sided_empirical_p"],
        "indirect_direct_difference_null_mean": lookup[
            ("all", "indirect_minus_direct_depth_change_share")
        ]["null_mean"],
        "indirect_direct_difference_observed_minus_null": lookup[
            ("all", "indirect_minus_direct_depth_change_share")
        ]["observed_minus_null_mean"],
        "indirect_direct_difference_two_sided_p": lookup[
            ("all", "indirect_minus_direct_depth_change_share")
        ]["two_sided_empirical_p"],
        "mean_world_indirect_null_mean": lookup[
            ("all", "mean_world_indirect_depth_change_share")
        ]["null_mean"],
        "mean_world_indirect_observed_minus_null": lookup[
            ("all", "mean_world_indirect_depth_change_share")
        ]["observed_minus_null_mean"],
        "mean_world_indirect_two_sided_p": lookup[
            ("all", "mean_world_indirect_depth_change_share")
        ]["two_sided_empirical_p"],
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
        print(f"direct_change_share={summary['direct_depth_change_share']}")
        print(f"indirect_change_share={summary['indirect_depth_change_share']}")
        print(
            "indirect_change_observed_minus_null="
            f"{summary['indirect_change_observed_minus_null']}"
        )
        print(f"indirect_change_p={summary['indirect_change_two_sided_p']}")
        print(
            "indirect_absolute_observed_minus_null="
            f"{summary['indirect_absolute_observed_minus_null']}"
        )
        print(f"indirect_absolute_p={summary['indirect_absolute_two_sided_p']}")
        print(f"future_event_reads={summary['future_event_reads']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
