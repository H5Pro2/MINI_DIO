from __future__ import annotations

import copy
import csv
import hashlib
import statistics
import sys
from dataclasses import dataclass
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
from tools.run_mcm_continuity_source_identity import (
    NULL_PERMUTATIONS,
    _shape_vector,
)
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_continuous_rank_self_segmentation import (
    ClosedRankEpisode,
    RankCycleSegmenter,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2113_MCM_EPISODEN_RELATIONALE_SALIENZ"
MASK_64 = (1 << 64) - 1


@dataclass(frozen=True)
class StreamSalience:
    candidate_distance: float
    candidate_all_percentile: float
    candidate_source_percentile: float
    candidate_target_percentile: float
    candidate_descending_rank: int
    candidate_distance_ties: int
    candidate_left_crosses_boundary: int
    candidate_right_open_delay: int
    candidate_right_closure_delay: int
    all_transition_count: int
    source_transition_count: int
    target_transition_count: int
    all_transition_percentiles: tuple[float, ...]


def _shape_distance(left: tuple[int, ...], right: tuple[int, ...]) -> float:
    left_shape = _shape_vector(left)
    right_shape = _shape_vector(right)
    return sum(
        abs(float(left_shape[index]) - float(right_shape[index]))
        for index in range(len(left_shape))
    )


def _midrank_percentile(value: float, population: list[float]) -> float:
    if not population:
        raise ValueError("percentile population must not be empty")
    below = sum(item < value for item in population)
    equal = sum(item == value for item in population)
    return (below + 0.5 * equal) / len(population)


def _stream_salience(
    episodes: list[ClosedRankEpisode],
    boundary_tick: int,
) -> StreamSalience:
    if len(episodes) < 2:
        raise ValueError("at least two closed episodes are required")
    try:
        candidate_right_index = next(
            index
            for index, episode in enumerate(episodes)
            if episode.opened_tick > boundary_tick
        )
    except StopIteration as error:
        raise ValueError("no strict postboundary episode") from error
    if candidate_right_index == 0:
        raise ValueError("candidate has no preceding episode")

    distances = [
        _shape_distance(left.values, right.values)
        for left, right in zip(episodes, episodes[1:])
    ]
    source_distances = [
        distance
        for distance, right in zip(distances, episodes[1:])
        if right.closure_tick <= boundary_tick
    ]
    target_distances = [
        distance
        for distance, left, right in zip(
            distances,
            episodes,
            episodes[1:],
        )
        if left.opened_tick > boundary_tick
        and right.opened_tick > boundary_tick
    ]
    if not source_distances or not target_distances:
        raise ValueError("source and target controls must both be present")

    candidate_transition_index = candidate_right_index - 1
    candidate_distance = distances[candidate_transition_index]
    left = episodes[candidate_right_index - 1]
    right = episodes[candidate_right_index]
    return StreamSalience(
        candidate_distance=candidate_distance,
        candidate_all_percentile=_midrank_percentile(
            candidate_distance,
            distances,
        ),
        candidate_source_percentile=_midrank_percentile(
            candidate_distance,
            source_distances,
        ),
        candidate_target_percentile=_midrank_percentile(
            candidate_distance,
            target_distances,
        ),
        candidate_descending_rank=1 + sum(
            distance > candidate_distance for distance in distances
        ),
        candidate_distance_ties=sum(
            distance == candidate_distance for distance in distances
        ),
        candidate_left_crosses_boundary=int(
            left.opened_tick <= boundary_tick < left.closure_tick
        ),
        candidate_right_open_delay=right.opened_tick - boundary_tick,
        candidate_right_closure_delay=right.closure_tick - boundary_tick,
        all_transition_count=len(distances),
        source_transition_count=len(source_distances),
        target_transition_count=len(target_distances),
        all_transition_percentiles=tuple(
            _midrank_percentile(distance, distances) for distance in distances
        ),
    )


def _source_state(
    source_senses: tuple[dict, ...],
) -> tuple[MiniMCMField, RankCycleSegmenter, list[ClosedRankEpisode]]:
    field = MiniMCMField(neuron_count=NEURON_COUNT)
    segmenter = RankCycleSegmenter(
        tuple(float(neuron.activation) for neuron in field.neurons)
    )
    episodes = []
    for tick, senses in enumerate(source_senses, start=1):
        state = field.step(senses)
        episode = segmenter.observe(state["activations"], tick)
        if episode is not None:
            episodes.append(episode)
    return field, segmenter, episodes


def _continued_episodes(
    source_field: MiniMCMField,
    source_segmenter: RankCycleSegmenter,
    source_episodes: list[ClosedRankEpisode],
    boundary_tick: int,
    target_senses: tuple[dict, ...],
) -> list[ClosedRankEpisode]:
    field = copy.deepcopy(source_field)
    segmenter = copy.deepcopy(source_segmenter)
    episodes = list(source_episodes)
    for offset, senses in enumerate(target_senses, start=1):
        state = field.step(senses)
        episode = segmenter.observe(
            state["activations"],
            boundary_tick + offset,
        )
        if episode is not None:
            episodes.append(episode)
    return episodes


def _splitmix_index(base: int, permutation: int, size: int) -> int:
    if size <= 0:
        raise ValueError("permutation population must not be empty")
    value = (base + (permutation + 1) * 0x9E3779B97F4A7C15) & MASK_64
    value = ((value ^ (value >> 30)) * 0xBF58476D1CE4E5B9) & MASK_64
    value = ((value ^ (value >> 27)) * 0x94D049BB133111EB) & MASK_64
    value ^= value >> 31
    return value % size


def _position_null(observations: list[dict], seed: str) -> dict[str, float]:
    observed = statistics.mean(
        float(item["row"]["candidate_all_percentile"])
        for item in observations
    )
    bases = [
        int.from_bytes(
            hashlib.sha256(
                f"{seed}|{item['path_key']}".encode("utf-8")
            ).digest()[:8],
            "big",
        )
        for item in observations
    ]
    null_values = []
    for permutation in range(NULL_PERMUTATIONS):
        selected = []
        for base, item in zip(bases, observations):
            percentiles = item["null_percentiles"]
            selected.append(
                percentiles[
                    _splitmix_index(base, permutation, len(percentiles))
                ]
            )
        null_values.append(statistics.mean(selected))
    return {
        "position_null_permutations": NULL_PERMUTATIONS,
        "position_null_mean_percentile": statistics.mean(null_values),
        "position_null_max_percentile": max(null_values),
        "candidate_high_salience_position_p": (
            1 + sum(value >= observed for value in null_values)
        )
        / (NULL_PERMUTATIONS + 1),
        "candidate_low_change_position_p": (
            1 + sum(value <= observed for value in null_values)
        )
        / (NULL_PERMUTATIONS + 1),
        "candidate_two_sided_position_p": min(
            1.0,
            2
            * min(
                (1 + sum(value >= observed for value in null_values))
                / (NULL_PERMUTATIONS + 1),
                (1 + sum(value <= observed for value in null_values))
                / (NULL_PERMUTATIONS + 1),
            ),
        ),
    }


def _scope_observations(observations: list[dict], scope: str) -> list[dict]:
    if scope == "all":
        return observations
    if scope == "universe_a":
        return [item for item in observations if item["universe"] == "a"]
    if scope == "universe_b":
        return [item for item in observations if item["universe"] == "b"]
    if scope == "crossing":
        return [item for item in observations if item["crossing"] == 1]
    if scope == "no_crossing":
        return [item for item in observations if item["crossing"] == 0]
    raise ValueError(f"unknown scope: {scope}")


def _summary_row(dataset: str, scope: str, observations: list[dict]) -> dict:
    selected = _scope_observations(observations, scope)
    if not selected:
        raise ValueError(f"empty scope: {dataset} {scope}")
    rows = [item["row"] for item in selected]
    all_percentiles = [float(row["candidate_all_percentile"]) for row in rows]
    return {
        "dataset": dataset,
        "scope": scope,
        "streams": len(rows),
        "mean_candidate_shape_distance": statistics.mean(
            float(row["candidate_shape_distance"]) for row in rows
        ),
        "median_candidate_shape_distance": statistics.median(
            float(row["candidate_shape_distance"]) for row in rows
        ),
        "mean_candidate_all_percentile": statistics.mean(all_percentiles),
        "median_candidate_all_percentile": statistics.median(all_percentiles),
        "candidate_above_own_midrank_share": statistics.mean(
            percentile > 0.5 for percentile in all_percentiles
        ),
        "mean_candidate_source_percentile": statistics.mean(
            float(row["candidate_source_percentile"]) for row in rows
        ),
        "mean_candidate_target_percentile": statistics.mean(
            float(row["candidate_target_percentile"]) for row in rows
        ),
        "minimum_all_transition_count": min(
            int(row["all_transition_count"]) for row in rows
        ),
        "median_all_transition_count": statistics.median(
            int(row["all_transition_count"]) for row in rows
        ),
        "maximum_all_transition_count": max(
            int(row["all_transition_count"]) for row in rows
        ),
        **_position_null(selected, f"2113|{dataset}|{scope}"),
        "episode_shapes_strength_normalized": 1,
        "exact_distance_ties_preserved": 1,
        "contact_boundary_visible_to_field": 0,
        "contact_boundary_visible_to_segmenter": 0,
        "contact_candidate_selected_posthoc": 1,
        "fixed_salience_threshold_used": 0,
        "field_learning_used": 0,
        "memory_read": 0,
        "memory_written": 0,
        "influences_action": 0,
    }


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict]]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    senses = {
        world.key: _world_senses(str(world.source), world.start)
        for world in worlds
    }
    target_universe = {
        target.key: "a" if target in universe_a else "b"
        for target in targets
    }
    observations = []
    path_rows = []
    for source in sources:
        source_field, source_segmenter, source_episodes = _source_state(
            senses[source.key]
        )
        boundary_tick = len(senses[source.key])
        for target in targets:
            episodes = _continued_episodes(
                source_field,
                source_segmenter,
                source_episodes,
                boundary_tick,
                senses[target.key],
            )
            salience = _stream_salience(episodes, boundary_tick)
            path_key = f"{source.key}->{target.key}"
            row = {
                "dataset": dataset,
                "path_key_posthoc": path_key,
                "source_key_posthoc": source.key,
                "source_asset_posthoc": source.asset,
                "source_year_posthoc": source.year,
                "target_key_posthoc": target.key,
                "target_universe": target_universe[target.key],
                "candidate_shape_distance": salience.candidate_distance,
                "candidate_all_percentile": salience.candidate_all_percentile,
                "candidate_source_percentile": salience.candidate_source_percentile,
                "candidate_target_percentile": salience.candidate_target_percentile,
                "candidate_descending_rank": salience.candidate_descending_rank,
                "candidate_distance_ties": salience.candidate_distance_ties,
                "candidate_left_crosses_boundary": (
                    salience.candidate_left_crosses_boundary
                ),
                "candidate_right_open_delay": salience.candidate_right_open_delay,
                "candidate_right_closure_delay": (
                    salience.candidate_right_closure_delay
                ),
                "all_transition_count": salience.all_transition_count,
                "source_transition_count": salience.source_transition_count,
                "target_transition_count": salience.target_transition_count,
                "episode_shapes_strength_normalized": 1,
                "contact_boundary_visible_to_field": 0,
                "contact_boundary_visible_to_segmenter": 0,
                "contact_candidate_selected_posthoc": 1,
                "fixed_salience_threshold_used": 0,
                "field_learning_used": 0,
                "memory_read": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
            path_rows.append(row)
            observations.append(
                {
                    "path_key": path_key,
                    "universe": target_universe[target.key],
                    "crossing": salience.candidate_left_crosses_boundary,
                    "row": row,
                    "null_percentiles": salience.all_transition_percentiles,
                }
            )
    summary_rows = [
        _summary_row(dataset, scope, observations)
        for scope in (
            "all",
            "universe_a",
            "universe_b",
            "crossing",
            "no_crossing",
        )
    ]
    return path_rows, summary_rows


def _all_rows() -> tuple[list[dict], list[dict]]:
    worlds = _worlds()
    path_rows = []
    summary_rows = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected = [world for world in worlds if world.dataset == dataset]
        paths, summaries = _dataset_rows(dataset, selected)
        path_rows.extend(paths)
        summary_rows.extend(summaries)
    return path_rows, summary_rows


def _write_csv(name: str, rows: list[dict]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    path_rows, summary_rows = _all_rows()
    _write_csv("paths", path_rows)
    _write_csv("summary", summary_rows)
    for row in summary_rows:
        print(f"dataset={row['dataset']} scope={row['scope']}")
        print(f"streams={row['streams']}")
        print(
            "mean_candidate_percentile="
            f"{row['mean_candidate_all_percentile']}"
        )
        print(
            "mean_source_percentile="
            f"{row['mean_candidate_source_percentile']}"
        )
        print(
            "mean_target_percentile="
            f"{row['mean_candidate_target_percentile']}"
        )
        print(
            "position_null_max="
            f"{row['position_null_max_percentile']}"
        )
        print(
            "candidate_high_salience_p="
            f"{row['candidate_high_salience_position_p']}"
        )
        print(
            "candidate_low_change_p="
            f"{row['candidate_low_change_position_p']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
