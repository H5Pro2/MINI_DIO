from __future__ import annotations

import copy
import csv
import statistics
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.config import Config
from mini_dio.mcm_neuron import MiniMCMField
from mini_dio.mini_world import (
    _empty_senses,
    build_senses_world_relative,
    build_sensory_profile,
    load_candles,
)
from tools.run_mcm_breadth_data_holdout import (
    SOURCES as BASIS_SOURCES,
    STARTS as BASIS_STARTS,
)
from tools.run_mcm_relation_lifecycle_independent_holdout import (
    SOURCES as HOLDOUT_SOURCES,
    STARTS as HOLDOUT_STARTS,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2105_MCM_KONTINUIERLICHE_FELDINSTANZ"
ROWS = 1000
HORIZON = 5
GAP_TICKS = (0, 1, 2, 4, 8, 16, 32, 64)
NEURON_COUNT = int(getattr(Config, "DIO_MINI_MCM_NEURON_COUNT", 12))


@dataclass(frozen=True)
class World:
    dataset: str
    asset: str
    year: int
    source: Path
    start: int

    @property
    def key(self) -> str:
        return f"{self.dataset}|{self.asset}|{self.year}|{self.start}"


def _worlds() -> list[World]:
    worlds = []
    for dataset, sources, starts in (
        ("2091_basis", BASIS_SOURCES, BASIS_STARTS),
        ("2092_holdout", HOLDOUT_SOURCES, HOLDOUT_STARTS),
    ):
        for asset, year, source in sources:
            for start in starts:
                worlds.append(World(dataset, asset, year, source, start))
    return worlds


def _directed_pairs(worlds: list[World]) -> list[tuple[str, World, World]]:
    grouped: dict[tuple[str, str, int, Path], list[World]] = {}
    for world in worlds:
        key = (world.dataset, world.asset, world.year, world.source)
        grouped.setdefault(key, []).append(world)
    pairs = []
    for group in grouped.values():
        ordered = sorted(group, key=lambda item: item.start)
        for left, right in zip(ordered, ordered[1:]):
            pairs.append(("forward", left, right))
            pairs.append(("reverse", right, left))
    return pairs


@lru_cache(maxsize=None)
def _source_candles(path: str) -> tuple[dict, ...]:
    candles = load_candles(Path(path))
    return tuple(candles)


@lru_cache(maxsize=None)
def _world_senses(path: str, start: int) -> tuple[dict, ...]:
    candles = list(_source_candles(path))[start : start + ROWS]
    if len(candles) != ROWS:
        raise RuntimeError(f"expected {ROWS} rows from {path}:{start}, found {len(candles)}")
    profile = build_sensory_profile(candles)
    return tuple(
        build_senses_world_relative(candles, index, profile=profile)
        for index in range(1, max(1, len(candles) - HORIZON))
    )


def _dynamic_state(field: MiniMCMField) -> tuple:
    return (
        field.last_signature,
        tuple(
            (neuron.activation, neuron.afterimage)
            for neuron in field.neurons
        ),
    )


def _mean_afterimage(field: MiniMCMField) -> float:
    return sum(abs(float(neuron.afterimage)) for neuron in field.neurons) / max(
        1, len(field.neurons)
    )


def _contact_field(senses: tuple[dict, ...]) -> MiniMCMField:
    field = MiniMCMField(neuron_count=NEURON_COUNT)
    for item in senses:
        field.step(item)
    return field


def _reset_states(senses: tuple[dict, ...]) -> tuple[tuple, ...]:
    field = MiniMCMField(neuron_count=NEURON_COUNT)
    states = []
    for item in senses:
        field.step(item)
        states.append(_dynamic_state(field))
    return tuple(states)


def _state_differences(left: tuple, right: tuple) -> tuple[float, float, float]:
    signature_difference = abs(float(left[0]) - float(right[0]))
    left_neurons = left[1]
    right_neurons = right[1]
    activation_difference = statistics.mean(
        abs(float(left_neurons[index][0]) - float(right_neurons[index][0]))
        for index in range(len(left_neurons))
    )
    afterimage_difference = statistics.mean(
        abs(float(left_neurons[index][1]) - float(right_neurons[index][1]))
        for index in range(len(left_neurons))
    )
    return signature_difference, activation_difference, afterimage_difference


def _correlation(left: list[float], right: list[float]) -> float:
    if not left or len(left) != len(right):
        return 0.0
    left_mean = statistics.mean(left)
    right_mean = statistics.mean(right)
    numerator = sum(
        (left[index] - left_mean) * (right[index] - right_mean)
        for index in range(len(left))
    )
    left_scale = sum((value - left_mean) ** 2 for value in left) ** 0.5
    right_scale = sum((value - right_mean) ** 2 for value in right) ** 0.5
    if left_scale == 0.0 or right_scale == 0.0:
        return 0.0
    return numerator / (left_scale * right_scale)


def _compare_target(
    continuous_field: MiniMCMField,
    target_senses: tuple[dict, ...],
    reset_states: tuple[tuple, ...],
) -> dict[str, object]:
    if len(target_senses) != len(reset_states):
        raise ValueError("target senses and reset trajectory differ in length")
    signature_sum = 0.0
    activation_sum = 0.0
    afterimage_sum = 0.0
    first_signature_difference = 0.0
    maximum_signature_difference = 0.0
    last_signature_difference = 0.0
    exact_convergence_tick = 0
    affected_ticks = len(target_senses)
    for tick, item in enumerate(target_senses, start=1):
        continuous_field.step(item)
        continuous_state = _dynamic_state(continuous_field)
        reset_state = reset_states[tick - 1]
        signature, activation, afterimage = _state_differences(
            continuous_state, reset_state
        )
        if tick == 1:
            first_signature_difference = signature
        signature_sum += signature
        activation_sum += activation
        afterimage_sum += afterimage
        maximum_signature_difference = max(maximum_signature_difference, signature)
        last_signature_difference = signature
        if continuous_state == reset_state:
            exact_convergence_tick = tick
            affected_ticks = tick - 1
            last_signature_difference = 0.0
            break
    ticks = len(target_senses)
    return {
        "target_ticks": ticks,
        "continuity_affected_ticks": affected_ticks,
        "exact_convergence_tick": exact_convergence_tick,
        "exact_convergence_reached": int(exact_convergence_tick > 0),
        "affected_target_share": affected_ticks / max(1, ticks),
        "first_signature_difference": first_signature_difference,
        "maximum_signature_difference": maximum_signature_difference,
        "final_signature_difference": last_signature_difference,
        "mean_absolute_signature_difference": signature_sum / max(1, ticks),
        "mean_absolute_activation_difference": activation_sum / max(1, ticks),
        "mean_absolute_afterimage_difference": afterimage_sum / max(1, ticks),
    }


def _blank_field_remains_fresh(gap_ticks: int) -> bool:
    field = MiniMCMField(neuron_count=NEURON_COUNT)
    fresh = MiniMCMField(neuron_count=NEURON_COUNT)
    for _ in range(max(0, int(gap_ticks))):
        field.step(_empty_senses())
    return _dynamic_state(field) == _dynamic_state(fresh)


def _pair_rows() -> list[dict[str, object]]:
    worlds = _worlds()
    senses = {
        world.key: _world_senses(str(world.source), world.start)
        for world in worlds
    }
    contact_fields = {
        world.key: _contact_field(senses[world.key])
        for world in worlds
    }
    reset_trajectories = {
        world.key: _reset_states(senses[world.key])
        for world in worlds
    }
    rows = []
    for pair_index, (direction, source, target) in enumerate(
        _directed_pairs(worlds), start=1
    ):
        source_field = contact_fields[source.key]
        source_terminal_signature = float(source_field.last_signature)
        source_terminal_afterimage = _mean_afterimage(source_field)
        for gap_ticks in GAP_TICKS:
            continuous = copy.deepcopy(source_field)
            for _ in range(gap_ticks):
                continuous.step(_empty_senses())
            post_gap_signature = float(continuous.last_signature)
            post_gap_afterimage = _mean_afterimage(continuous)
            comparison = _compare_target(
                continuous,
                senses[target.key],
                reset_trajectories[target.key],
            )
            rows.append(
                {
                    "dataset": source.dataset,
                    "pair_index": pair_index,
                    "direction": direction,
                    "asset": source.asset,
                    "year": source.year,
                    "source_file": source.source.name,
                    "source_start": source.start,
                    "target_start": target.start,
                    "gap_ticks": gap_ticks,
                    "source_terminal_signature": source_terminal_signature,
                    "source_terminal_afterimage": source_terminal_afterimage,
                    "post_gap_signature": post_gap_signature,
                    "post_gap_afterimage": post_gap_afterimage,
                    "blank_gap_control_exact": int(
                        _blank_field_remains_fresh(gap_ticks)
                    ),
                    **comparison,
                    "field_learning_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
    return rows


def _aggregate(
    rows: list[dict[str, object]],
    dataset: str,
    gap_ticks: int,
    scope: str,
) -> dict[str, object]:
    selected = [
        row
        for row in rows
        if row["dataset"] == dataset
        and int(row["gap_ticks"]) == gap_ticks
        and (scope == "all" or row["direction"] == scope)
    ]
    durations = [int(row["continuity_affected_ticks"]) for row in selected]
    return {
        "dataset": dataset,
        "gap_ticks": gap_ticks,
        "scope": scope,
        "directed_pairs": len(selected),
        "exact_convergence_count": sum(
            int(row["exact_convergence_reached"]) for row in selected
        ),
        "exact_convergence_share": statistics.mean(
            int(row["exact_convergence_reached"]) for row in selected
        ),
        "minimum_affected_ticks": min(durations),
        "median_affected_ticks": statistics.median(durations),
        "mean_affected_ticks": statistics.mean(durations),
        "maximum_affected_ticks": max(durations),
        "mean_affected_target_share": statistics.mean(
            float(row["affected_target_share"]) for row in selected
        ),
        "mean_first_signature_difference": statistics.mean(
            float(row["first_signature_difference"]) for row in selected
        ),
        "mean_maximum_signature_difference": statistics.mean(
            float(row["maximum_signature_difference"]) for row in selected
        ),
        "mean_absolute_signature_difference": statistics.mean(
            float(row["mean_absolute_signature_difference"]) for row in selected
        ),
        "mean_absolute_activation_difference": statistics.mean(
            float(row["mean_absolute_activation_difference"]) for row in selected
        ),
        "mean_absolute_afterimage_difference": statistics.mean(
            float(row["mean_absolute_afterimage_difference"]) for row in selected
        ),
        "source_afterimage_first_difference_correlation": _correlation(
            [float(row["source_terminal_afterimage"]) for row in selected],
            [float(row["first_signature_difference"]) for row in selected],
        ),
        "post_gap_afterimage_first_difference_correlation": _correlation(
            [float(row["post_gap_afterimage"]) for row in selected],
            [float(row["first_signature_difference"]) for row in selected],
        ),
        "post_gap_signature_first_difference_correlation": _correlation(
            [float(row["post_gap_signature"]) for row in selected],
            [float(row["first_signature_difference"]) for row in selected],
        ),
        "maximum_final_signature_difference": max(
            float(row["final_signature_difference"]) for row in selected
        ),
        "all_blank_gap_controls_exact": int(
            all(int(row["blank_gap_control_exact"]) == 1 for row in selected)
        ),
        "field_learning_used": 0,
        "memory_read": 0,
        "memory_written": 0,
        "influences_action": 0,
    }


def _summary_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        _aggregate(rows, dataset, gap_ticks, scope)
        for dataset in ("2091_basis", "2092_holdout")
        for gap_ticks in GAP_TICKS
        for scope in ("all", "forward", "reverse")
    ]


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    rows = _pair_rows()
    summaries = _summary_rows(rows)
    _write_csv("pairs", rows)
    _write_csv("summary", summaries)
    for row in summaries:
        if row["scope"] != "all":
            continue
        print(f"dataset={row['dataset']} gap_ticks={row['gap_ticks']}")
        print(f"directed_pairs={row['directed_pairs']}")
        print(f"exact_convergence_share={row['exact_convergence_share']}")
        print(f"median_affected_ticks={row['median_affected_ticks']}")
        print(
            "mean_absolute_signature_difference="
            f"{row['mean_absolute_signature_difference']}"
        )
        print(
            "all_blank_gap_controls_exact="
            f"{row['all_blank_gap_controls_exact']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
