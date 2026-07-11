from __future__ import annotations

import copy
import csv
import random
import statistics
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
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_passive_observer_boundary import (
    FieldFrame,
    RecurrenceObserver,
    _above_mean_projection,
    _empirical_upper_p,
    _field_digest,
    _nonzero_shift_expected,
    _overlap,
    _seed,
    _trace,
    _trace_digest,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2123_MCM_KOLLEKTIVE_BEOBACHTERKOORDINATIONSNULL"
PERMUTATIONS = 32


def _initial_observer(projection: str) -> RecurrenceObserver:
    if projection not in ("activation", "afterimage"):
        raise ValueError(f"unknown projection: {projection}")
    return RecurrenceObserver(())


def _support_state(frame: FieldFrame, projection: str) -> tuple[int, ...]:
    values = frame.activations if projection == "activation" else frame.afterimages
    return _above_mean_projection(values)


def _observe_prefix(
    trace: tuple[FieldFrame, ...],
    projection: str,
) -> RecurrenceObserver:
    observer = _initial_observer(projection)
    for tick, frame in enumerate(trace, start=1):
        observer.observe(_support_state(frame, projection), tick)
    return observer


def _paired_target_events(
    activation_initial: RecurrenceObserver,
    afterimage_initial: RecurrenceObserver,
    frames,
    boundary_tick: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    activation_observer = copy.deepcopy(activation_initial)
    afterimage_observer = copy.deepcopy(afterimage_initial)
    activation_closures = []
    afterimage_closures = []
    for offset, frame in enumerate(frames, start=1):
        tick = boundary_tick + offset
        activation_event = activation_observer.observe(
            _support_state(frame, "activation"), tick
        )
        afterimage_event = afterimage_observer.observe(
            _support_state(frame, "afterimage"), tick
        )
        if activation_event is not None and activation_event.opened_tick > boundary_tick:
            activation_closures.append(offset)
        if afterimage_event is not None and afterimage_event.opened_tick > boundary_tick:
            afterimage_closures.append(offset)
    return tuple(activation_closures), tuple(afterimage_closures)


def _neuron_shifts(label: str, horizon: int, neuron_count: int) -> tuple[int, ...]:
    rng = random.Random(_seed(label))
    shifts = tuple(rng.randrange(horizon) for _ in range(neuron_count))
    if len(set(shifts)) == 1:
        replacement = (shifts[-1] + 1) % horizon
        shifts = shifts[:-1] + (replacement,)
    return shifts


def _shift_neuron_pairs(
    trace: tuple[FieldFrame, ...],
    shifts: tuple[int, ...],
) -> tuple[FieldFrame, ...]:
    if not trace:
        return ()
    if len(shifts) != len(trace[0].activations):
        raise ValueError("one shift is required per neuron")
    horizon = len(trace)
    frames = []
    for tick in range(horizon):
        frames.append(
            FieldFrame(
                activations=tuple(
                    trace[(tick + shifts[neuron]) % horizon].activations[neuron]
                    for neuron in range(len(shifts))
                ),
                afterimages=tuple(
                    trace[(tick + shifts[neuron]) % horizon].afterimages[neuron]
                    for neuron in range(len(shifts))
                ),
            )
        )
    return tuple(frames)


def _synchrony_excess(
    activation_events: tuple[int, ...],
    afterimage_events: tuple[int, ...],
    horizon: int,
) -> float:
    return _overlap(activation_events, afterimage_events) - _nonzero_shift_expected(
        activation_events,
        afterimage_events,
        horizon,
    )


def _path_rows(dataset: str, worlds: list) -> list[dict]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    universes = {
        target.key: "a" if target in universe_a else "b"
        for target in targets
    }
    senses = {
        world.key: _world_senses(str(world.source), world.start)
        for world in worlds
    }

    rows = []
    for source in sources:
        source_field = MiniMCMField(neuron_count=NEURON_COUNT)
        source_trace = _trace(source_field, senses[source.key])
        boundary_tick = len(source_trace)
        activation_initial = _observe_prefix(source_trace, "activation")
        afterimage_initial = _observe_prefix(source_trace, "afterimage")
        for target in targets:
            field = copy.deepcopy(source_field)
            target_trace = _trace(field, senses[target.key])
            target_digest_before = _trace_digest(target_trace)
            field_digest_before = _field_digest(field)
            activation_events, afterimage_events = _paired_target_events(
                activation_initial,
                afterimage_initial,
                target_trace,
                boundary_tick,
            )
            observed_overlap = _overlap(activation_events, afterimage_events)
            observed_excess = _synchrony_excess(
                activation_events,
                afterimage_events,
                len(target_trace),
            )
            null_excesses = []
            null_overlaps = []
            for permutation in range(PERMUTATIONS):
                shifts = _neuron_shifts(
                    f"2123|{dataset}|{source.key}|{target.key}|{permutation}",
                    len(target_trace),
                    NEURON_COUNT,
                )
                shifted_trace = _shift_neuron_pairs(target_trace, shifts)
                null_activation, null_afterimage = _paired_target_events(
                    activation_initial,
                    afterimage_initial,
                    shifted_trace,
                    boundary_tick,
                )
                null_overlaps.append(_overlap(null_activation, null_afterimage))
                null_excesses.append(
                    _synchrony_excess(
                        null_activation,
                        null_afterimage,
                        len(target_trace),
                    )
                )

            rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "target_key_posthoc": target.key,
                    "target_universe": universes[target.key],
                    "target_ticks": len(target_trace),
                    "activation_closures": len(activation_events),
                    "afterimage_closures": len(afterimage_events),
                    "observed_same_tick_closures": observed_overlap,
                    "observed_synchrony_excess": round(observed_excess, 9),
                    "collective_null_overlap_mean": round(
                        statistics.fmean(null_overlaps), 9
                    ),
                    "collective_null_excess_mean": round(
                        statistics.fmean(null_excesses), 9
                    ),
                    "observed_minus_collective_null_mean": round(
                        observed_excess - statistics.fmean(null_excesses), 9
                    ),
                    "collective_null_exceedances": sum(
                        value >= observed_excess for value in null_excesses
                    ),
                    "target_trace_sha256": target_digest_before,
                    "target_trace_unchanged": int(
                        target_digest_before == _trace_digest(target_trace)
                    ),
                    "field_state_unchanged_by_nulls": int(
                        field_digest_before == _field_digest(field)
                    ),
                    "local_activation_afterimage_pair_preserved": 1,
                    "collective_timing_preserved": 0,
                    "viranz_parameter_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                    **{
                        f"null_excess_{index:02d}": round(value, 9)
                        for index, value in enumerate(null_excesses)
                    },
                }
            )
    return rows


def _summary_and_source_rows(
    dataset: str,
    paths: list[dict],
) -> tuple[list[dict], list[dict]]:
    summaries = []
    sources_out = []
    for universe_scope in ("a", "b", "all"):
        selected = [
            row
            for row in paths
            if universe_scope == "all" or row["target_universe"] == universe_scope
        ]
        observed = sum(float(row["observed_synchrony_excess"]) for row in selected)
        null_values = [
            sum(float(row[f"null_excess_{index:02d}"]) for row in selected)
            for index in range(PERMUTATIONS)
        ]
        by_source: dict[str, list[dict]] = {}
        for row in selected:
            by_source.setdefault(row["source_key_posthoc"], []).append(row)
        signs = {"positive": 0, "negative": 0, "tie": 0}
        for source_key, source_paths in sorted(by_source.items()):
            source_observed = sum(
                float(row["observed_synchrony_excess"]) for row in source_paths
            )
            source_null_values = [
                sum(
                    float(row[f"null_excess_{index:02d}"])
                    for row in source_paths
                )
                for index in range(PERMUTATIONS)
            ]
            source_null_mean = statistics.fmean(source_null_values)
            direction = (
                "positive"
                if source_observed > source_null_mean
                else "negative"
                if source_observed < source_null_mean
                else "tie"
            )
            signs[direction] += 1
            sources_out.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "source_key_posthoc": source_key,
                    "paths": len(source_paths),
                    "observed_synchrony_excess": round(source_observed, 9),
                    "collective_null_excess_mean": round(source_null_mean, 9),
                    "observed_minus_collective_null_mean": round(
                        source_observed - source_null_mean, 9
                    ),
                    "direction": direction,
                    "empirical_upper_p": round(
                        _empirical_upper_p(source_observed, source_null_values), 6
                    ),
                }
            )
        summaries.append(
            {
                "dataset": dataset,
                "universe_scope": universe_scope,
                "paths": len(selected),
                "sources": len(by_source),
                "observed_same_tick_closures": sum(
                    int(row["observed_same_tick_closures"]) for row in selected
                ),
                "observed_synchrony_excess": round(observed, 9),
                "collective_null_excess_mean": round(
                    statistics.fmean(null_values), 9
                ),
                "collective_null_excess_max": round(max(null_values), 9),
                "observed_minus_collective_null_mean": round(
                    observed - statistics.fmean(null_values), 9
                ),
                "empirical_upper_p": round(
                    _empirical_upper_p(observed, null_values), 6
                ),
                "positive_sources": signs["positive"],
                "negative_sources": signs["negative"],
                "tie_sources": signs["tie"],
                "permutations": PERMUTATIONS,
            }
        )
    return summaries, sources_out


def _all_rows() -> tuple[list[dict], list[dict], list[dict]]:
    worlds = _worlds()
    paths_out = []
    summaries_out = []
    sources_out = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected_worlds = [world for world in worlds if world.dataset == dataset]
        paths = _path_rows(dataset, selected_worlds)
        summaries, sources = _summary_and_source_rows(dataset, paths)
        paths_out.extend(paths)
        summaries_out.extend(summaries)
        sources_out.extend(sources)
    return paths_out, summaries_out, sources_out


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
    paths, summaries, sources = _all_rows()
    for name, rows in (("paths", paths), ("summary", summaries), ("sources", sources)):
        _write_csv(name, rows)
    print(
        f"audit paths={len(paths)} "
        f"trace_unchanged={sum(row['target_trace_unchanged'] for row in paths)} "
        f"field_unchanged={sum(row['field_state_unchanged_by_nulls'] for row in paths)}"
    )
    for row in summaries:
        print(
            f"dataset={row['dataset']} scope={row['universe_scope']} "
            f"observed_excess={row['observed_synchrony_excess']} "
            f"null_mean={row['collective_null_excess_mean']} "
            f"null_max={row['collective_null_excess_max']} "
            f"p={row['empirical_upper_p']} "
            f"sources={row['positive_sources']}/{row['negative_sources']}/{row['tie_sources']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
