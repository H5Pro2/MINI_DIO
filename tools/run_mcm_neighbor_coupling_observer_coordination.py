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
    _field_digest,
    _overlap,
    _trace,
    _trace_digest,
)
from tools.run_mcm_prequential_partial_relation_continuation import (
    _binomial_upper_p,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2124_MCM_NACHBARSCHAFTSKOPPLUNG_BEOBACHTERKOORDINATION"
CORE_PATH = ROOT / "mini_dio" / "mcm_neuron.py"


def _trace_without_neighbor_signal(
    field: MiniMCMField,
    senses: tuple[dict, ...],
) -> tuple[FieldFrame, ...]:
    frames = []
    for item in senses:
        flat = flatten_senses(item)
        activations = [
            neuron.step(flat, 0.0)
            for neuron in field.neurons
        ]
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


def _neuron_trace_digest(
    trace: tuple[FieldFrame, ...],
    neuron_index: int,
) -> str:
    digest = hashlib.sha256()
    for frame in trace:
        digest.update(float(frame.activations[neuron_index]).hex().encode("ascii"))
        digest.update(b"|")
        digest.update(float(frame.afterimages[neuron_index]).hex().encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def _weights_digest(field: MiniMCMField) -> str:
    digest = hashlib.sha256()
    for neuron in field.neurons:
        for name, value in sorted(neuron.weights.items()):
            digest.update(name.encode("utf-8"))
            digest.update(float(value).hex().encode("ascii"))
        for name, value in sorted(neuron.action_weights.items()):
            digest.update(name.encode("utf-8"))
            digest.update(float(value).hex().encode("ascii"))
    return digest.hexdigest()


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
        coupled_source_field = MiniMCMField(neuron_count=NEURON_COUNT)
        control_source_field = MiniMCMField(neuron_count=NEURON_COUNT)
        initial_weights_equal = int(
            _weights_digest(coupled_source_field)
            == _weights_digest(control_source_field)
        )
        coupled_source_trace = _trace(
            coupled_source_field,
            senses[source.key],
        )
        control_source_trace = _trace_without_neighbor_signal(
            control_source_field,
            senses[source.key],
        )
        boundary_tick = len(coupled_source_trace)
        coupled_activation_initial = _observe_prefix(
            coupled_source_trace, "activation"
        )
        coupled_afterimage_initial = _observe_prefix(
            coupled_source_trace, "afterimage"
        )
        control_activation_initial = _observe_prefix(
            control_source_trace, "activation"
        )
        control_afterimage_initial = _observe_prefix(
            control_source_trace, "afterimage"
        )

        for target in targets:
            coupled_field = copy.deepcopy(coupled_source_field)
            control_field = copy.deepcopy(control_source_field)
            coupled_trace = _trace(coupled_field, senses[target.key])
            control_trace = _trace_without_neighbor_signal(
                control_field,
                senses[target.key],
            )
            coupled_trace_before = _trace_digest(coupled_trace)
            control_trace_before = _trace_digest(control_trace)
            coupled_field_before = _field_digest(coupled_field)
            control_field_before = _field_digest(control_field)

            coupled_activation, coupled_afterimage = _paired_target_events(
                coupled_activation_initial,
                coupled_afterimage_initial,
                coupled_trace,
                boundary_tick,
            )
            control_activation, control_afterimage = _paired_target_events(
                control_activation_initial,
                control_afterimage_initial,
                control_trace,
                boundary_tick,
            )
            horizon = len(coupled_trace)
            coupled_excess = _synchrony_excess(
                coupled_activation,
                coupled_afterimage,
                horizon,
            )
            control_excess = _synchrony_excess(
                control_activation,
                control_afterimage,
                horizon,
            )
            difference = coupled_excess - control_excess
            rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "target_key_posthoc": target.key,
                    "target_universe": universes[target.key],
                    "target_ticks": horizon,
                    "coupled_activation_closures": len(coupled_activation),
                    "coupled_afterimage_closures": len(coupled_afterimage),
                    "coupled_same_tick_closures": _overlap(
                        coupled_activation, coupled_afterimage
                    ),
                    "coupled_synchrony_excess": round(coupled_excess, 9),
                    "no_neighbor_activation_closures": len(control_activation),
                    "no_neighbor_afterimage_closures": len(control_afterimage),
                    "no_neighbor_same_tick_closures": _overlap(
                        control_activation, control_afterimage
                    ),
                    "no_neighbor_synchrony_excess": round(control_excess, 9),
                    "coupled_minus_no_neighbor_excess": round(difference, 9),
                    "direction": (
                        "coupled_higher"
                        if difference > 0
                        else "no_neighbor_higher"
                        if difference < 0
                        else "tie"
                    ),
                    "same_external_senses": 1,
                    "initial_weights_equal": initial_weights_equal,
                    "first_neuron_source_trace_equal": int(
                        _neuron_trace_digest(coupled_source_trace, 0)
                        == _neuron_trace_digest(control_source_trace, 0)
                    ),
                    "first_neuron_target_trace_equal": int(
                        _neuron_trace_digest(coupled_trace, 0)
                        == _neuron_trace_digest(control_trace, 0)
                    ),
                    "coupled_trace_unchanged_by_observer": int(
                        coupled_trace_before == _trace_digest(coupled_trace)
                    ),
                    "control_trace_unchanged_by_observer": int(
                        control_trace_before == _trace_digest(control_trace)
                    ),
                    "coupled_field_unchanged_by_observer": int(
                        coupled_field_before == _field_digest(coupled_field)
                    ),
                    "control_field_unchanged_by_observer": int(
                        control_field_before == _field_digest(control_field)
                    ),
                    "production_field_modified": 0,
                    "neighbor_signal_coupled": 1,
                    "neighbor_signal_control": 0,
                    "viranz_parameter_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
    return rows


def _source_and_summary_rows(
    dataset: str,
    paths: list[dict],
) -> tuple[list[dict], list[dict]]:
    sources_out = []
    summaries = []
    for universe_scope in ("a", "b", "all"):
        selected = [
            row
            for row in paths
            if universe_scope == "all" or row["target_universe"] == universe_scope
        ]
        by_source: dict[str, list[dict]] = {}
        for row in selected:
            by_source.setdefault(row["source_key_posthoc"], []).append(row)

        source_signs = {"positive": 0, "negative": 0, "tie": 0}
        for source_key, source_paths in sorted(by_source.items()):
            coupled = sum(
                float(row["coupled_synchrony_excess"])
                for row in source_paths
            )
            control = sum(
                float(row["no_neighbor_synchrony_excess"])
                for row in source_paths
            )
            difference = coupled - control
            direction = (
                "positive"
                if difference > 0
                else "negative"
                if difference < 0
                else "tie"
            )
            source_signs[direction] += 1
            sources_out.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "source_key_posthoc": source_key,
                    "paths": len(source_paths),
                    "coupled_synchrony_excess": round(coupled, 9),
                    "no_neighbor_synchrony_excess": round(control, 9),
                    "coupled_minus_no_neighbor_excess": round(difference, 9),
                    "direction": direction,
                }
            )

        coupled_total = sum(
            float(row["coupled_synchrony_excess"]) for row in selected
        )
        control_total = sum(
            float(row["no_neighbor_synchrony_excess"]) for row in selected
        )
        path_positive = sum(
            float(row["coupled_minus_no_neighbor_excess"]) > 0
            for row in selected
        )
        path_negative = sum(
            float(row["coupled_minus_no_neighbor_excess"]) < 0
            for row in selected
        )
        summaries.append(
            {
                "dataset": dataset,
                "universe_scope": universe_scope,
                "paths": len(selected),
                "sources": len(by_source),
                "coupled_same_tick_closures": sum(
                    int(row["coupled_same_tick_closures"]) for row in selected
                ),
                "no_neighbor_same_tick_closures": sum(
                    int(row["no_neighbor_same_tick_closures"])
                    for row in selected
                ),
                "coupled_synchrony_excess": round(coupled_total, 9),
                "no_neighbor_synchrony_excess": round(control_total, 9),
                "coupled_minus_no_neighbor_excess": round(
                    coupled_total - control_total, 9
                ),
                "coupled_to_no_neighbor_ratio": (
                    round(coupled_total / control_total, 9)
                    if control_total > 0
                    else ""
                ),
                "positive_sources": source_signs["positive"],
                "negative_sources": source_signs["negative"],
                "tie_sources": source_signs["tie"],
                "source_sign_upper_p": format(
                    _binomial_upper_p(
                        source_signs["positive"],
                        source_signs["negative"],
                    ),
                    ".12g",
                ),
                "positive_paths": path_positive,
                "negative_paths": path_negative,
                "tie_paths": len(selected) - path_positive - path_negative,
            }
        )
    return sources_out, summaries


def _all_rows() -> tuple[list[dict], list[dict], list[dict]]:
    core_hash_before = hashlib.sha256(CORE_PATH.read_bytes()).hexdigest()
    worlds = _worlds()
    paths_out = []
    sources_out = []
    summaries_out = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected_worlds = [world for world in worlds if world.dataset == dataset]
        paths = _path_rows(dataset, selected_worlds)
        sources, summaries = _source_and_summary_rows(dataset, paths)
        paths_out.extend(paths)
        sources_out.extend(sources)
        summaries_out.extend(summaries)
    core_hash_after = hashlib.sha256(CORE_PATH.read_bytes()).hexdigest()
    for row in paths_out:
        row["production_core_sha256"] = core_hash_before
        row["production_core_unchanged"] = int(core_hash_before == core_hash_after)
    return paths_out, sources_out, summaries_out


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
    paths, sources, summaries = _all_rows()
    for name, rows in (("paths", paths), ("sources", sources), ("summary", summaries)):
        _write_csv(name, rows)
    print(
        f"audit paths={len(paths)} "
        f"first_neuron_source_equal={sum(row['first_neuron_source_trace_equal'] for row in paths)} "
        f"first_neuron_target_equal={sum(row['first_neuron_target_trace_equal'] for row in paths)} "
        f"core_unchanged={sum(row['production_core_unchanged'] for row in paths)}"
    )
    for row in summaries:
        print(
            f"dataset={row['dataset']} scope={row['universe_scope']} "
            f"coupled={row['coupled_synchrony_excess']} "
            f"no_neighbor={row['no_neighbor_synchrony_excess']} "
            f"difference={row['coupled_minus_no_neighbor_excess']} "
            f"ratio={row['coupled_to_no_neighbor_ratio']} "
            f"sources={row['positive_sources']}/{row['negative_sources']}/{row['tie_sources']} "
            f"p={row['source_sign_upper_p']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
