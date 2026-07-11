from __future__ import annotations

import copy
import csv
import hashlib
import statistics
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neuron import MiniMCMField, flatten_senses
from tools.run_mcm_collective_observer_coordination_null import (
    _observe_prefix,
    _paired_target_events,
    _synchrony_excess,
)
from tools.run_mcm_continuous_field_instance import (
    NEURON_COUNT,
    _world_senses,
    _worlds,
)
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_passive_observer_boundary import (
    FieldFrame,
    _empirical_upper_p,
    _overlap,
    _trace,
    _trace_digest,
)
from tools.run_mcm_prequential_partial_relation_continuation import (
    _binomial_upper_p,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2125_MCM_KETTENLAGE_RICHTUNG_BEOBACHTERKOORDINATION"
CORE_PATH = ROOT / "mini_dio" / "mcm_neuron.py"


def _chain_orders(neuron_count: int) -> tuple[tuple[str, tuple[int, ...]], ...]:
    original = tuple(range(neuron_count))
    reverse = tuple(reversed(original))
    orders = [("original_forward_00", original)]
    orders.extend(
        (
            f"forward_rotation_{offset:02d}",
            original[offset:] + original[:offset],
        )
        for offset in range(1, neuron_count)
    )
    orders.extend(
        (
            f"reverse_rotation_{offset:02d}",
            reverse[offset:] + reverse[:offset],
        )
        for offset in range(neuron_count)
    )
    return tuple(orders)


def _trace_with_order(
    field: MiniMCMField,
    senses: tuple[dict, ...],
    order: tuple[int, ...],
) -> tuple[FieldFrame, ...]:
    if tuple(sorted(order)) != tuple(range(len(field.neurons))):
        raise ValueError("order must contain every neuron exactly once")
    frames = []
    for item in senses:
        flat = flatten_senses(item)
        activations = [0.0] * len(field.neurons)
        previous = 0.0
        for neuron_index in order:
            activation = field.neurons[neuron_index].step(flat, previous)
            activations[neuron_index] = activation
            previous = activation
        field.last_signature = sum(activations) / max(1, len(activations))
        frames.append(
            FieldFrame(
                activations=tuple(float(value) for value in activations),
                afterimages=tuple(
                    float(neuron.afterimage) for neuron in field.neurons
                ),
            )
        )
    return tuple(frames)


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
    orders = _chain_orders(NEURON_COUNT)
    rows = []
    for source in sources:
        target_results = {
            target.key: {
                "target": target,
                "values": {},
                "same_ticks": {},
            }
            for target in targets
        }
        original_source_digest = ""
        for order_label, order in orders:
            source_field = MiniMCMField(neuron_count=NEURON_COUNT)
            source_trace = _trace_with_order(
                source_field,
                senses[source.key],
                order,
            )
            if order_label == "original_forward_00":
                original_source_digest = _trace_digest(source_trace)
            boundary_tick = len(source_trace)
            activation_initial = _observe_prefix(source_trace, "activation")
            afterimage_initial = _observe_prefix(source_trace, "afterimage")
            for target in targets:
                field = copy.deepcopy(source_field)
                target_trace = _trace_with_order(
                    field,
                    senses[target.key],
                    order,
                )
                activation_events, afterimage_events = _paired_target_events(
                    activation_initial,
                    afterimage_initial,
                    target_trace,
                    boundary_tick,
                )
                target_results[target.key]["values"][order_label] = (
                    _synchrony_excess(
                        activation_events,
                        afterimage_events,
                        len(target_trace),
                    )
                )
                target_results[target.key]["same_ticks"][order_label] = _overlap(
                    activation_events,
                    afterimage_events,
                )

        control_labels = tuple(label for label, _ in orders[1:])
        for target in targets:
            item = target_results[target.key]
            values = item["values"]
            controls = [values[label] for label in control_labels]
            original = values["original_forward_00"]
            control_mean = statistics.fmean(controls)
            rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "target_key_posthoc": target.key,
                    "target_universe": universes[target.key],
                    "target_ticks": len(senses[target.key]),
                    "original_same_tick_closures": item["same_ticks"][
                        "original_forward_00"
                    ],
                    "original_synchrony_excess": round(original, 9),
                    "alternative_order_excess_mean": round(control_mean, 9),
                    "alternative_order_excess_min": round(min(controls), 9),
                    "alternative_order_excess_max": round(max(controls), 9),
                    "original_minus_alternative_mean": round(
                        original - control_mean, 9
                    ),
                    "alternative_orders_at_least_original": sum(
                        value >= original for value in controls
                    ),
                    "alternative_orders": len(controls),
                    "direction": (
                        "original_higher"
                        if original > control_mean
                        else "alternative_mean_higher"
                        if original < control_mean
                        else "tie"
                    ),
                    "same_external_senses": 1,
                    "same_weights": 1,
                    "same_coupling_strength": 1,
                    "same_afterimage_mechanism": 1,
                    "original_source_trace_sha256": original_source_digest,
                    "production_field_modified": 0,
                    "viranz_parameter_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                    **{
                        f"excess_{label}": round(values[label], 9)
                        for label in control_labels
                    },
                }
            )
    return rows


def _source_summary_and_order_rows(
    dataset: str,
    paths: list[dict],
) -> tuple[list[dict], list[dict], list[dict]]:
    control_labels = tuple(
        label for label, _ in _chain_orders(NEURON_COUNT)[1:]
    )
    forward_labels = tuple(
        label for label in control_labels if label.startswith("forward_")
    )
    reverse_labels = tuple(
        label for label in control_labels if label.startswith("reverse_")
    )
    sources_out = []
    summaries = []
    orders_out = []
    for universe_scope in ("a", "b", "all"):
        selected = [
            row
            for row in paths
            if universe_scope == "all" or row["target_universe"] == universe_scope
        ]
        original_total = sum(
            float(row["original_synchrony_excess"]) for row in selected
        )
        order_totals = {
            label: sum(float(row[f"excess_{label}"]) for row in selected)
            for label in control_labels
        }
        control_values = list(order_totals.values())
        for label, value in order_totals.items():
            orders_out.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "order_label": label,
                    "synchrony_excess": round(value, 9),
                    "minus_original": round(value - original_total, 9),
                    "at_least_original": int(value >= original_total),
                }
            )

        by_source: dict[str, list[dict]] = {}
        for row in selected:
            by_source.setdefault(row["source_key_posthoc"], []).append(row)
        signs = {"positive": 0, "negative": 0, "tie": 0}
        forward_signs = {"positive": 0, "negative": 0, "tie": 0}
        reverse_signs = {"positive": 0, "negative": 0, "tie": 0}
        for source_key, source_paths in sorted(by_source.items()):
            source_original = sum(
                float(row["original_synchrony_excess"])
                for row in source_paths
            )
            source_controls = [
                sum(float(row[f"excess_{label}"]) for row in source_paths)
                for label in control_labels
            ]
            source_control_mean = statistics.fmean(source_controls)
            source_forward_mean = statistics.fmean(
                sum(
                    float(row[f"excess_{label}"])
                    for row in source_paths
                )
                for label in forward_labels
            )
            source_reverse_mean = statistics.fmean(
                sum(
                    float(row[f"excess_{label}"])
                    for row in source_paths
                )
                for label in reverse_labels
            )
            difference = source_original - source_control_mean
            direction = (
                "positive"
                if difference > 0
                else "negative"
                if difference < 0
                else "tie"
            )
            signs[direction] += 1
            forward_direction = (
                "positive"
                if source_original > source_forward_mean
                else "negative"
                if source_original < source_forward_mean
                else "tie"
            )
            reverse_direction = (
                "positive"
                if source_original > source_reverse_mean
                else "negative"
                if source_original < source_reverse_mean
                else "tie"
            )
            forward_signs[forward_direction] += 1
            reverse_signs[reverse_direction] += 1
            sources_out.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "source_key_posthoc": source_key,
                    "paths": len(source_paths),
                    "original_synchrony_excess": round(source_original, 9),
                    "alternative_order_excess_mean": round(
                        source_control_mean, 9
                    ),
                    "forward_rotation_excess_mean": round(
                        source_forward_mean, 9
                    ),
                    "reverse_rotation_excess_mean": round(
                        source_reverse_mean, 9
                    ),
                    "original_minus_alternative_mean": round(difference, 9),
                    "original_minus_forward_mean": round(
                        source_original - source_forward_mean, 9
                    ),
                    "original_minus_reverse_mean": round(
                        source_original - source_reverse_mean, 9
                    ),
                    "alternative_orders_at_least_original": sum(
                        value >= source_original for value in source_controls
                    ),
                    "direction": direction,
                    "direction_vs_forward": forward_direction,
                    "direction_vs_reverse": reverse_direction,
                }
            )

        path_positive = sum(
            float(row["original_minus_alternative_mean"]) > 0
            for row in selected
        )
        path_negative = sum(
            float(row["original_minus_alternative_mean"]) < 0
            for row in selected
        )
        path_forward_positive = sum(
            float(row["original_synchrony_excess"])
            > statistics.fmean(
                float(row[f"excess_{label}"]) for label in forward_labels
            )
            for row in selected
        )
        path_reverse_positive = sum(
            float(row["original_synchrony_excess"])
            > statistics.fmean(
                float(row[f"excess_{label}"]) for label in reverse_labels
            )
            for row in selected
        )
        forward_values = [order_totals[label] for label in forward_labels]
        reverse_values = [order_totals[label] for label in reverse_labels]
        summaries.append(
            {
                "dataset": dataset,
                "universe_scope": universe_scope,
                "paths": len(selected),
                "sources": len(by_source),
                "original_synchrony_excess": round(original_total, 9),
                "alternative_order_excess_mean": round(
                    statistics.fmean(control_values), 9
                ),
                "alternative_order_excess_min": round(min(control_values), 9),
                "alternative_order_excess_max": round(max(control_values), 9),
                "forward_rotation_excess_mean": round(
                    statistics.fmean(forward_values), 9
                ),
                "forward_rotation_excess_min": round(min(forward_values), 9),
                "forward_rotation_excess_max": round(max(forward_values), 9),
                "reverse_rotation_excess_mean": round(
                    statistics.fmean(reverse_values), 9
                ),
                "reverse_rotation_excess_min": round(min(reverse_values), 9),
                "reverse_rotation_excess_max": round(max(reverse_values), 9),
                "original_minus_alternative_mean": round(
                    original_total - statistics.fmean(control_values), 9
                ),
                "alternative_orders_at_least_original": sum(
                    value >= original_total for value in control_values
                ),
                "forward_orders_at_least_original": sum(
                    value >= original_total for value in forward_values
                ),
                "reverse_orders_at_least_original": sum(
                    value >= original_total for value in reverse_values
                ),
                "order_empirical_upper_p": round(
                    _empirical_upper_p(original_total, control_values), 6
                ),
                "positive_sources": signs["positive"],
                "negative_sources": signs["negative"],
                "tie_sources": signs["tie"],
                "positive_sources_vs_forward": forward_signs["positive"],
                "negative_sources_vs_forward": forward_signs["negative"],
                "tie_sources_vs_forward": forward_signs["tie"],
                "positive_sources_vs_reverse": reverse_signs["positive"],
                "negative_sources_vs_reverse": reverse_signs["negative"],
                "tie_sources_vs_reverse": reverse_signs["tie"],
                "source_sign_upper_p": format(
                    _binomial_upper_p(signs["positive"], signs["negative"]),
                    ".12g",
                ),
                "positive_paths": path_positive,
                "negative_paths": path_negative,
                "tie_paths": len(selected) - path_positive - path_negative,
                "positive_paths_vs_forward": path_forward_positive,
                "nonpositive_paths_vs_forward": len(selected)
                - path_forward_positive,
                "positive_paths_vs_reverse": path_reverse_positive,
                "nonpositive_paths_vs_reverse": len(selected)
                - path_reverse_positive,
                "alternative_orders": len(control_values),
            }
        )
    return sources_out, summaries, orders_out


def _all_rows() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    core_hash_before = hashlib.sha256(CORE_PATH.read_bytes()).hexdigest()
    worlds = _worlds()
    paths_out = []
    sources_out = []
    summaries_out = []
    orders_out = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected_worlds = [world for world in worlds if world.dataset == dataset]
        paths = _path_rows(dataset, selected_worlds)
        sources, summaries, orders = _source_summary_and_order_rows(
            dataset, paths
        )
        paths_out.extend(paths)
        sources_out.extend(sources)
        summaries_out.extend(summaries)
        orders_out.extend(orders)
    core_hash_after = hashlib.sha256(CORE_PATH.read_bytes()).hexdigest()
    for row in paths_out:
        row["production_core_sha256"] = core_hash_before
        row["production_core_unchanged"] = int(core_hash_before == core_hash_after)
    return paths_out, sources_out, summaries_out, orders_out


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
    paths, sources, summaries, orders = _all_rows()
    for name, rows in (
        ("paths", paths),
        ("sources", sources),
        ("summary", summaries),
        ("orders", orders),
    ):
        _write_csv(name, rows)
    print(
        f"audit paths={len(paths)} "
        f"orders={len(_chain_orders(NEURON_COUNT))} "
        f"core_unchanged={sum(row['production_core_unchanged'] for row in paths)}"
    )
    for row in summaries:
        print(
            f"dataset={row['dataset']} scope={row['universe_scope']} "
            f"original={row['original_synchrony_excess']} "
            f"alternative_mean={row['alternative_order_excess_mean']} "
            f"range={row['alternative_order_excess_min']}..{row['alternative_order_excess_max']} "
            f"orders_ge={row['alternative_orders_at_least_original']} "
            f"p={row['order_empirical_upper_p']} "
            f"sources={row['positive_sources']}/{row['negative_sources']}/{row['tie_sources']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
