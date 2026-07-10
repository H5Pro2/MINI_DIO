from __future__ import annotations

import copy
import csv
import hashlib
import random
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


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
from tools.run_mcm_continuity_topology_transfer import _activation_order


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2122_MCM_PASSIVE_BEOBACHTERGRENZE"
PERMUTATIONS = 200


@dataclass(frozen=True)
class FieldFrame:
    activations: tuple[float, ...]
    afterimages: tuple[float, ...]


@dataclass(frozen=True)
class ClosureEvent:
    opened_tick: int
    closure_tick: int


Projection = Callable[[FieldFrame], tuple[int, ...]]


def _rank_projection(values: tuple[float, ...]) -> tuple[int, ...]:
    return _activation_order(values)


def _above_mean_projection(values: tuple[float, ...]) -> tuple[int, ...]:
    mean = statistics.fmean(values)
    return tuple(index for index, value in enumerate(values) if value > mean)


PROJECTIONS: dict[str, Projection] = {
    "activation_rank": lambda frame: _rank_projection(frame.activations),
    "activation_above_mean": lambda frame: _above_mean_projection(frame.activations),
    "afterimage_rank": lambda frame: _rank_projection(frame.afterimages),
    "afterimage_above_mean": lambda frame: _above_mean_projection(frame.afterimages),
}

PROJECTION_PAIRS = (
    ("activation_rank", "activation_above_mean"),
    ("activation_rank", "afterimage_rank"),
    ("activation_rank", "afterimage_above_mean"),
    ("activation_above_mean", "afterimage_above_mean"),
)


class RecurrenceObserver:
    def __init__(self, initial_state: tuple[int, ...]) -> None:
        self.previous_state = initial_state
        self.seen_states = {initial_state: 0}
        self.opened_tick = 0

    def observe(self, state: tuple[int, ...], tick: int) -> ClosureEvent | None:
        if self.opened_tick == 0 and state != self.previous_state:
            self.opened_tick = tick

        event = None
        if self.opened_tick > 0 and state in self.seen_states:
            event = ClosureEvent(self.opened_tick, tick)
            self.seen_states = {state: tick}
            self.opened_tick = 0
        else:
            self.seen_states.setdefault(state, tick)

        self.previous_state = state
        return event


def _frame(field: MiniMCMField, activations: list[float]) -> FieldFrame:
    return FieldFrame(
        activations=tuple(float(value) for value in activations),
        afterimages=tuple(float(neuron.afterimage) for neuron in field.neurons),
    )


def _trace(field: MiniMCMField, senses: tuple[dict, ...]) -> tuple[FieldFrame, ...]:
    frames = []
    for item in senses:
        state = field.step(item)
        frames.append(_frame(field, state["activations"]))
    return tuple(frames)


def _trace_digest(trace: tuple[FieldFrame, ...]) -> str:
    digest = hashlib.sha256()
    for frame in trace:
        for group in (frame.activations, frame.afterimages):
            for value in group:
                digest.update(float(value).hex().encode("ascii"))
                digest.update(b"|")
        digest.update(b"\n")
    return digest.hexdigest()


def _field_digest(field: MiniMCMField) -> str:
    digest = hashlib.sha256()
    digest.update(float(field.last_signature).hex().encode("ascii"))
    for neuron in field.neurons:
        digest.update(float(neuron.activation).hex().encode("ascii"))
        digest.update(float(neuron.afterimage).hex().encode("ascii"))
    return digest.hexdigest()


def _projection_events(
    trace: tuple[FieldFrame, ...],
    projection: Projection,
    boundary_tick: int,
) -> tuple[int, ...]:
    initial = FieldFrame(
        activations=(0.0,) * NEURON_COUNT,
        afterimages=(0.0,) * NEURON_COUNT,
    )
    observer = RecurrenceObserver(projection(initial))
    closures = []
    for tick, frame in enumerate(trace, start=1):
        event = observer.observe(projection(frame), tick)
        if event is not None and event.opened_tick > boundary_tick:
            closures.append(event.closure_tick - boundary_tick)
    return tuple(closures)


def _observe_all(
    trace: tuple[FieldFrame, ...],
    boundary_tick: int,
    order: tuple[str, ...],
) -> dict[str, tuple[int, ...]]:
    return {
        name: _projection_events(trace, PROJECTIONS[name], boundary_tick)
        for name in order
    }


def _overlap(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return len(set(left).intersection(right))


def _shifted_overlap(
    left: tuple[int, ...],
    right: tuple[int, ...],
    horizon: int,
    shift: int,
) -> int:
    shifted = {((tick - 1 + shift) % horizon) + 1 for tick in right}
    return len(set(left).intersection(shifted))


def _nonzero_shift_expected(
    left: tuple[int, ...],
    right: tuple[int, ...],
    horizon: int,
) -> float:
    if horizon <= 1:
        return 0.0
    return (len(left) * len(right) - _overlap(left, right)) / (horizon - 1)


def _seed(label: str) -> int:
    return int.from_bytes(hashlib.sha256(label.encode("utf-8")).digest()[:8], "big")


def _empirical_upper_p(observed: int, null_values: list[int]) -> float:
    return (1 + sum(value >= observed for value in null_values)) / (
        len(null_values) + 1
    )


def _path_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict]]:
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
    event_rows = []
    projection_order = tuple(PROJECTIONS)
    reverse_order = tuple(reversed(projection_order))
    for source in sources:
        source_field = MiniMCMField(neuron_count=NEURON_COUNT)
        source_trace = _trace(source_field, senses[source.key])
        boundary_tick = len(source_trace)
        for target in targets:
            field = copy.deepcopy(source_field)
            target_trace = _trace(field, senses[target.key])
            trace = source_trace + target_trace
            trace_before = _trace_digest(trace)
            field_before = _field_digest(field)
            forward = _observe_all(trace, boundary_tick, projection_order)
            reverse = _observe_all(trace, boundary_tick, reverse_order)
            trace_after = _trace_digest(trace)
            field_after = _field_digest(field)

            rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "target_key_posthoc": target.key,
                    "target_universe": universes[target.key],
                    "source_ticks": boundary_tick,
                    "target_ticks": len(target_trace),
                    "raw_trace_sha256": trace_before,
                    "raw_trace_unchanged": int(trace_before == trace_after),
                    "field_state_unchanged_by_observers": int(field_before == field_after),
                    "projection_order_invariant": int(forward == reverse),
                    "observer_receives_field_object": 0,
                    "observer_writes_field": 0,
                    "viranz_parameter_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                    **{
                        f"{name}_closures": len(forward[name])
                        for name in projection_order
                    },
                    **{
                        f"overlap_{left}__{right}": _overlap(
                            forward[left], forward[right]
                        )
                        for left, right in PROJECTION_PAIRS
                    },
                }
            )
            for left, right in PROJECTION_PAIRS:
                event_rows.append(
                    {
                        "dataset": dataset,
                        "source_key_posthoc": source.key,
                        "target_key_posthoc": target.key,
                        "target_universe": universes[target.key],
                        "projection_left": left,
                        "projection_right": right,
                        "target_ticks": len(target_trace),
                        "left_events": forward[left],
                        "right_events": forward[right],
                        "observed_same_tick_closures": _overlap(
                            forward[left], forward[right]
                        ),
                    }
                )
    return rows, event_rows


def _summary_rows(dataset: str, event_rows: list[dict]) -> tuple[list[dict], list[dict]]:
    summaries = []
    sources_out = []
    for universe_scope in ("a", "b", "all"):
        selected_scope = [
            row
            for row in event_rows
            if universe_scope == "all" or row["target_universe"] == universe_scope
        ]
        for left, right in PROJECTION_PAIRS:
            selected = [
                row
                for row in selected_scope
                if row["projection_left"] == left
                and row["projection_right"] == right
            ]
            observed = sum(row["observed_same_tick_closures"] for row in selected)
            expected = sum(
                _nonzero_shift_expected(
                    row["left_events"],
                    row["right_events"],
                    row["target_ticks"],
                )
                for row in selected
            )
            null_values = []
            for permutation in range(PERMUTATIONS):
                rng = random.Random(
                    _seed(
                        f"2122|{dataset}|{universe_scope}|{left}|{right}|{permutation}"
                    )
                )
                null_values.append(
                    sum(
                        _shifted_overlap(
                            row["left_events"],
                            row["right_events"],
                            row["target_ticks"],
                            rng.randrange(1, row["target_ticks"]),
                        )
                        for row in selected
                    )
                )

            by_source: dict[str, list[dict]] = {}
            for row in selected:
                by_source.setdefault(row["source_key_posthoc"], []).append(row)
            signs = {"positive": 0, "negative": 0, "tie": 0}
            for source_key, source_rows in sorted(by_source.items()):
                source_observed = sum(
                    row["observed_same_tick_closures"] for row in source_rows
                )
                source_expected = sum(
                    _nonzero_shift_expected(
                        row["left_events"],
                        row["right_events"],
                        row["target_ticks"],
                    )
                    for row in source_rows
                )
                sign = (
                    "positive"
                    if source_observed > source_expected
                    else "negative"
                    if source_observed < source_expected
                    else "tie"
                )
                signs[sign] += 1
                sources_out.append(
                    {
                        "dataset": dataset,
                        "universe_scope": universe_scope,
                        "projection_left": left,
                        "projection_right": right,
                        "source_key_posthoc": source_key,
                        "paths": len(source_rows),
                        "observed_same_tick_closures": source_observed,
                        "uniform_shift_expected": round(source_expected, 6),
                        "observed_minus_expected": round(
                            source_observed - source_expected, 6
                        ),
                        "direction": sign,
                    }
                )
            summaries.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "projection_left": left,
                    "projection_right": right,
                    "paths": len(selected),
                    "sources": len(by_source),
                    "left_closures": sum(len(row["left_events"]) for row in selected),
                    "right_closures": sum(len(row["right_events"]) for row in selected),
                    "observed_same_tick_closures": observed,
                    "uniform_shift_expected": round(expected, 6),
                    "observed_to_expected_ratio": round(
                        observed / expected if expected else 0.0, 6
                    ),
                    "null_mean": round(statistics.fmean(null_values), 6),
                    "null_max": max(null_values),
                    "empirical_upper_p": round(
                        _empirical_upper_p(observed, null_values), 6
                    ),
                    "positive_sources": signs["positive"],
                    "negative_sources": signs["negative"],
                    "tie_sources": signs["tie"],
                }
            )
    return summaries, sources_out


def _all_rows() -> tuple[list[dict], list[dict], list[dict]]:
    worlds = _worlds()
    paths_out = []
    summaries_out = []
    sources_out = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected = [world for world in worlds if world.dataset == dataset]
        path_rows, event_rows = _path_rows(dataset, selected)
        summaries, sources = _summary_rows(dataset, event_rows)
        paths_out.extend(path_rows)
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
        "audit "
        f"paths={len(paths)} "
        f"trace_unchanged={sum(row['raw_trace_unchanged'] for row in paths)} "
        f"field_unchanged={sum(row['field_state_unchanged_by_observers'] for row in paths)} "
        f"order_invariant={sum(row['projection_order_invariant'] for row in paths)}"
    )
    for row in summaries:
        print(
            f"dataset={row['dataset']} scope={row['universe_scope']} "
            f"pair={row['projection_left']}|{row['projection_right']} "
            f"observed={row['observed_same_tick_closures']} "
            f"null={row['null_mean']} ratio={row['observed_to_expected_ratio']} "
            f"p={row['empirical_upper_p']} "
            f"sources={row['positive_sources']}/{row['negative_sources']}/{row['tie_sources']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
