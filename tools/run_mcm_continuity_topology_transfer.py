from __future__ import annotations

import copy
import csv
import statistics
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.dio_syntax import make_syntax_symbol
from mini_dio.mcm_neuron import MiniMCMField
from mini_dio.mini_world import _empty_senses
from tools.run_mcm_continuous_field_instance import (
    GAP_TICKS,
    NEURON_COUNT,
    _contact_field,
    _correlation,
    _directed_pairs,
    _dynamic_state,
    _world_senses,
    _worlds,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2106_MCM_KONTINUITAET_TOPOLOGIEDURCHGRIFF"


@dataclass(frozen=True)
class TickState:
    dynamic: tuple
    syntax_symbol: str
    activation_order: tuple[tuple[int, ...], ...]
    activations: tuple[float, ...]


def _activation_order(values: tuple[float, ...] | list[float]) -> tuple[tuple[int, ...], ...]:
    """Return exact activation layers without an epsilon or value threshold."""

    ranked = sorted(
        ((float(value), index) for index, value in enumerate(values)),
        key=lambda item: (-item[0], item[1]),
    )
    layers: list[tuple[int, ...]] = []
    index = 0
    while index < len(ranked):
        value = ranked[index][0]
        tied = []
        while index < len(ranked) and ranked[index][0] == value:
            tied.append(ranked[index][1])
            index += 1
        layers.append(tuple(tied))
    return tuple(layers)


def _pair_relation(value: float) -> int:
    if value > 0.0:
        return 1
    if value < 0.0:
        return -1
    return 0


def _rank_pair_disagreements(
    left: tuple[float, ...] | list[float],
    right: tuple[float, ...] | list[float],
) -> int:
    """Count changed neuron-pair orders while preserving exact ties."""

    if len(left) != len(right):
        raise ValueError("activation vectors differ in length")
    disagreements = 0
    for left_index in range(len(left)):
        for right_index in range(left_index + 1, len(left)):
            left_relation = _pair_relation(
                float(left[left_index]) - float(left[right_index])
            )
            right_relation = _pair_relation(
                float(right[left_index]) - float(right[right_index])
            )
            disagreements += int(left_relation != right_relation)
    return disagreements


def _path_profile(states: list[object] | tuple[object, ...]) -> dict[str, object]:
    """Compress only consecutive equal states into an unlabeled path topology."""

    episodes: list[object] = []
    boundaries: list[int] = []
    for tick, state in enumerate(states, start=1):
        if not episodes or state != episodes[-1]:
            if episodes:
                boundaries.append(tick)
            episodes.append(state)
    edges = list(zip(episodes, episodes[1:]))
    return {
        "episodes": tuple(episodes),
        "boundaries": frozenset(boundaries),
        "node_counts": Counter(episodes),
        "edge_counts": Counter(edges),
    }


def _counter_l1(left: Counter, right: Counter) -> int:
    return sum(abs(left[key] - right[key]) for key in set(left) | set(right))


def _path_difference(left_states: list[object], right_states: list[object]) -> dict[str, int]:
    left = _path_profile(left_states)
    right = _path_profile(right_states)
    left_nodes = set(left["node_counts"])
    right_nodes = set(right["node_counts"])
    left_edges = set(left["edge_counts"])
    right_edges = set(right["edge_counts"])
    return {
        "left_episode_count": len(left["episodes"]),
        "right_episode_count": len(right["episodes"]),
        "episode_count_difference": abs(
            len(left["episodes"]) - len(right["episodes"])
        ),
        "boundary_difference_count": len(
            left["boundaries"] ^ right["boundaries"]
        ),
        "node_set_difference_count": len(left_nodes ^ right_nodes),
        "node_observation_difference": _counter_l1(
            left["node_counts"], right["node_counts"]
        ),
        "edge_set_difference_count": len(left_edges ^ right_edges),
        "edge_observation_difference": _counter_l1(
            left["edge_counts"], right["edge_counts"]
        ),
    }


def _reset_trajectory(senses: tuple[dict, ...]) -> tuple[TickState, ...]:
    field = MiniMCMField(neuron_count=NEURON_COUNT)
    trajectory = []
    for item in senses:
        field_state = field.step(item)
        activations = tuple(float(value) for value in field_state["activations"])
        trajectory.append(
            TickState(
                dynamic=_dynamic_state(field),
                syntax_symbol=make_syntax_symbol(item, field_state["signature"]),
                activation_order=_activation_order(activations),
                activations=activations,
            )
        )
    return tuple(trajectory)


def _compare_paths(
    continuous_field: MiniMCMField,
    target_senses: tuple[dict, ...],
    reset: tuple[TickState, ...],
) -> dict[str, object]:
    if len(target_senses) != len(reset):
        raise ValueError("target senses and reset trajectory differ in length")

    reset_symbols = [state.syntax_symbol for state in reset]
    reset_orders = [state.activation_order for state in reset]
    continuous_symbols: list[str] = []
    continuous_orders: list[tuple[tuple[int, ...], ...]] = []
    signature_differences: list[float] = []
    rank_pair_differences: list[int] = []
    syntax_difference_ticks: list[int] = []
    order_difference_ticks: list[int] = []
    exact_convergence_tick = 0

    for offset, item in enumerate(target_senses):
        tick = offset + 1
        field_state = continuous_field.step(item)
        activations = tuple(float(value) for value in field_state["activations"])
        symbol = make_syntax_symbol(item, field_state["signature"])
        order = _activation_order(activations)
        continuous_symbols.append(symbol)
        continuous_orders.append(order)

        reset_state = reset[offset]
        signature_difference = abs(
            float(field_state["signature"]) - float(reset_state.dynamic[0])
        )
        pair_difference = _rank_pair_disagreements(
            activations, reset_state.activations
        )
        signature_differences.append(signature_difference)
        rank_pair_differences.append(pair_difference)
        if symbol != reset_state.syntax_symbol:
            syntax_difference_ticks.append(tick)
        if order != reset_state.activation_order:
            order_difference_ticks.append(tick)

        if _dynamic_state(continuous_field) == reset_state.dynamic:
            exact_convergence_tick = tick
            continuous_symbols.extend(reset_symbols[tick:])
            continuous_orders.extend(reset_orders[tick:])
            remaining = len(target_senses) - tick
            signature_differences.extend([0.0] * remaining)
            rank_pair_differences.extend([0] * remaining)
            break

    target_ticks = len(target_senses)
    syntax_path = _path_difference(reset_symbols, continuous_symbols)
    order_path = _path_difference(reset_orders, continuous_orders)
    rank_changed = len(order_difference_ticks)
    maximum_pairs = max(1, NEURON_COUNT * (NEURON_COUNT - 1) // 2)
    return {
        "target_ticks": target_ticks,
        "exact_field_convergence_tick": exact_convergence_tick,
        "field_affected_ticks": max(0, exact_convergence_tick - 1)
        if exact_convergence_tick
        else target_ticks,
        "first_signature_difference": signature_differences[0],
        "maximum_signature_difference": max(signature_differences),
        "mean_signature_difference": statistics.mean(signature_differences),
        "syntax_different_ticks": len(syntax_difference_ticks),
        "syntax_first_difference_tick": syntax_difference_ticks[0]
        if syntax_difference_ticks
        else 0,
        "syntax_last_difference_tick": syntax_difference_ticks[-1]
        if syntax_difference_ticks
        else 0,
        "syntax_path_exact": int(reset_symbols == continuous_symbols),
        **{f"syntax_{key}": value for key, value in syntax_path.items()},
        "order_different_ticks": rank_changed,
        "order_first_difference_tick": order_difference_ticks[0]
        if order_difference_ticks
        else 0,
        "order_last_difference_tick": order_difference_ticks[-1]
        if order_difference_ticks
        else 0,
        "order_path_exact": int(reset_orders == continuous_orders),
        "mean_rank_pair_disagreements": statistics.mean(rank_pair_differences),
        "mean_rank_pair_disagreements_when_changed": (
            sum(rank_pair_differences) / rank_changed if rank_changed else 0.0
        ),
        "mean_rank_pair_disagreement_share": statistics.mean(
            rank_pair_differences
        )
        / maximum_pairs,
        "maximum_rank_pair_disagreements": max(rank_pair_differences),
        **{f"order_{key}": value for key, value in order_path.items()},
    }


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
        world.key: _reset_trajectory(senses[world.key])
        for world in worlds
    }

    rows = []
    for pair_index, (direction, source, target) in enumerate(
        _directed_pairs(worlds), start=1
    ):
        for gap_ticks in GAP_TICKS:
            continuous = copy.deepcopy(contact_fields[source.key])
            for _ in range(gap_ticks):
                continuous.step(_empty_senses())
            comparison = _compare_paths(
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
                    **comparison,
                    "uses_existing_dio_syntax": 1,
                    "activation_order_threshold": 0,
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
    syntax_changed = [
        row for row in selected if int(row["syntax_path_exact"]) == 0
    ]
    order_changed = [
        row for row in selected if int(row["order_path_exact"]) == 0
    ]
    return {
        "dataset": dataset,
        "gap_ticks": gap_ticks,
        "scope": scope,
        "directed_pairs": len(selected),
        "syntax_changed_pairs": len(syntax_changed),
        "syntax_changed_pair_share": len(syntax_changed) / max(1, len(selected)),
        "syntax_different_ticks_total": sum(
            int(row["syntax_different_ticks"]) for row in selected
        ),
        "syntax_boundary_differences_total": sum(
            int(row["syntax_boundary_difference_count"]) for row in selected
        ),
        "syntax_node_set_differences_total": sum(
            int(row["syntax_node_set_difference_count"]) for row in selected
        ),
        "syntax_edge_set_differences_total": sum(
            int(row["syntax_edge_set_difference_count"]) for row in selected
        ),
        "order_changed_pairs": len(order_changed),
        "order_changed_pair_share": len(order_changed) / max(1, len(selected)),
        "minimum_order_different_ticks": min(
            int(row["order_different_ticks"]) for row in selected
        ),
        "median_order_different_ticks": statistics.median(
            int(row["order_different_ticks"]) for row in selected
        ),
        "mean_order_different_ticks": statistics.mean(
            int(row["order_different_ticks"]) for row in selected
        ),
        "maximum_order_different_ticks": max(
            int(row["order_different_ticks"]) for row in selected
        ),
        "median_order_last_difference_tick": statistics.median(
            int(row["order_last_difference_tick"]) for row in selected
        ),
        "maximum_order_last_difference_tick": max(
            int(row["order_last_difference_tick"]) for row in selected
        ),
        "mean_rank_pair_disagreements_when_changed": statistics.mean(
            float(row["mean_rank_pair_disagreements_when_changed"])
            for row in selected
        ),
        "maximum_rank_pair_disagreements": max(
            int(row["maximum_rank_pair_disagreements"]) for row in selected
        ),
        "order_boundary_differences_total": sum(
            int(row["order_boundary_difference_count"]) for row in selected
        ),
        "order_node_set_differences_total": sum(
            int(row["order_node_set_difference_count"]) for row in selected
        ),
        "order_edge_set_differences_total": sum(
            int(row["order_edge_set_difference_count"]) for row in selected
        ),
        "order_edge_observation_differences_total": sum(
            int(row["order_edge_observation_difference"]) for row in selected
        ),
        "first_signature_order_duration_correlation": _correlation(
            [float(row["first_signature_difference"]) for row in selected],
            [float(row["order_different_ticks"]) for row in selected],
        ),
        "uses_existing_dio_syntax": 1,
        "activation_order_threshold": 0,
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
        print(f"syntax_changed_pairs={row['syntax_changed_pairs']}")
        print(f"order_changed_pairs={row['order_changed_pairs']}")
        print(f"median_order_different_ticks={row['median_order_different_ticks']}")
        print(
            "order_edge_set_differences_total="
            f"{row['order_edge_set_differences_total']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
