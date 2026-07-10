from __future__ import annotations

import csv
import math
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_continuous_field_instance import _world_senses, _worlds
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_continuous_rank_self_segmentation import (
    ClosedRankEpisode,
    _source_state,
    _target_episodes,
)
from tools.run_mcm_prequential_partial_relation_continuation import (
    _binomial_lower_p,
    _binomial_upper_p,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2118_MCM_PRAEQUENTIELLE_RELATIONSALTERUNG"
TRANSITIONS_PER_PAIR = 6


@dataclass(frozen=True)
class AgePairOutcome:
    younger_age: int
    older_age: int
    wins: int
    ties: int
    losses: int

    @property
    def pairs(self) -> int:
        return self.wins + self.ties + self.losses

    @property
    def auc(self) -> float:
        if self.pairs == 0:
            return 0.5
        return (self.wins + 0.5 * self.ties) / self.pairs


@dataclass(frozen=True)
class AgeContinuation:
    outcomes: tuple[AgePairOutcome, ...]
    matched_steps: int

    @property
    def wins(self) -> int:
        return sum(item.wins for item in self.outcomes)

    @property
    def ties(self) -> int:
        return sum(item.ties for item in self.outcomes)

    @property
    def losses(self) -> int:
        return sum(item.losses for item in self.outcomes)

    @property
    def pairs(self) -> int:
        return sum(item.pairs for item in self.outcomes)

    @property
    def auc(self) -> float:
        if self.pairs == 0:
            return 0.5
        return (self.wins + 0.5 * self.ties) / self.pairs

    def where(self, *, minimum_younger_age: int) -> AgeContinuation:
        return AgeContinuation(
            outcomes=tuple(
                item
                for item in self.outcomes
                if item.younger_age >= minimum_younger_age
            ),
            matched_steps=self.matched_steps,
        )


def _matched_age_continuation(
    episodes: list[ClosedRankEpisode],
) -> AgeContinuation:
    supports = [
        tuple(int(value != 0) for value in episode.values)
        for episode in episodes
    ]
    if len(supports) < 3:
        return AgeContinuation((), 0)

    cumulative = list(supports[0])
    streak = list(supports[0])
    counts: dict[tuple[int, int], list[int]] = defaultdict(lambda: [0, 0, 0])
    matched_steps = 0

    for index in range(1, len(supports) - 1):
        current = supports[index]
        following = supports[index + 1]
        for slot, active in enumerate(current):
            cumulative[slot] += active
            streak[slot] = streak[slot] + 1 if active else 0

        groups: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
        for slot, active in enumerate(current):
            if active:
                key = (slot // TRANSITIONS_PER_PAIR, cumulative[slot])
                groups[key].append((streak[slot], following[slot]))

        step_matched = False
        for candidates in groups.values():
            for left, right in combinations(candidates, 2):
                if left[0] == right[0]:
                    continue
                step_matched = True
                younger, older = sorted((left, right), key=lambda item: item[0])
                younger_outcome = younger[1]
                older_outcome = older[1]
                bucket = counts[(younger[0], older[0])]
                if older_outcome and not younger_outcome:
                    bucket[0] += 1
                elif younger_outcome and not older_outcome:
                    bucket[2] += 1
                else:
                    bucket[1] += 1
        matched_steps += int(step_matched)

    outcomes = tuple(
        AgePairOutcome(
            younger_age=ages[0],
            older_age=ages[1],
            wins=values[0],
            ties=values[1],
            losses=values[2],
        )
        for ages, values in sorted(counts.items())
    )
    return AgeContinuation(outcomes, matched_steps)


def _combine(results: list[AgeContinuation]) -> AgeContinuation:
    counts: dict[tuple[int, int], list[int]] = defaultdict(lambda: [0, 0, 0])
    for result in results:
        for item in result.outcomes:
            bucket = counts[(item.younger_age, item.older_age)]
            bucket[0] += item.wins
            bucket[1] += item.ties
            bucket[2] += item.losses
    return AgeContinuation(
        outcomes=tuple(
            AgePairOutcome(ages[0], ages[1], *values)
            for ages, values in sorted(counts.items())
        ),
        matched_steps=sum(result.matched_steps for result in results),
    )


def _scope(observations: list[dict], universe: str) -> list[dict]:
    if universe == "all":
        return observations
    return [item for item in observations if item["universe"] == universe[-1]]


def _source_summary_and_age_rows(
    dataset: str,
    observations: list[dict],
) -> tuple[list[dict], list[dict], list[dict]]:
    source_rows = []
    summary_rows = []
    age_rows = []
    source_keys = sorted({item["source_key"] for item in observations})
    for universe_scope in ("all", "universe_a", "universe_b"):
        selected = _scope(observations, universe_scope)
        source_results = []
        source_carried_results = []
        for source_key in source_keys:
            result = _combine(
                [
                    item["result"]
                    for item in selected
                    if item["source_key"] == source_key
                ]
            )
            carried = result.where(minimum_younger_age=2)
            if result.pairs:
                source_results.append(result)
            if carried.pairs:
                source_carried_results.append(carried)
            source_rows.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "source_key_posthoc": source_key,
                    "matched_steps": result.matched_steps,
                    "all_unequal_age_pairs": result.pairs,
                    "older_wins": result.wins,
                    "ties": result.ties,
                    "older_losses": result.losses,
                    "older_age_auc": result.auc,
                    "both_already_carried_pairs": carried.pairs,
                    "carried_older_age_auc": carried.auc,
                    "predictor_reads_next_episode": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )

        combined = _combine([item["result"] for item in selected])
        carried = combined.where(minimum_younger_age=2)
        for item in combined.outcomes:
            age_rows.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "younger_exact_run_length": item.younger_age,
                    "older_exact_run_length": item.older_age,
                    "exact_age_gap": item.older_age - item.younger_age,
                    "matched_pairs": item.pairs,
                    "older_wins": item.wins,
                    "ties": item.ties,
                    "older_losses": item.losses,
                    "older_age_auc": item.auc,
                }
            )

        aucs = [result.auc for result in source_results]
        carried_aucs = [result.auc for result in source_carried_results]
        positive = sum(value > 0.5 for value in aucs)
        negative = sum(value < 0.5 for value in aucs)
        carried_positive = sum(value > 0.5 for value in carried_aucs)
        carried_negative = sum(value < 0.5 for value in carried_aucs)
        carried_lower_p = _binomial_lower_p(
            carried_positive, carried_negative
        )
        carried_upper_p = _binomial_upper_p(
            carried_positive, carried_negative
        )
        path_results = [item["result"] for item in selected]
        path_pairs = [result.pairs for result in path_results]
        summary_rows.append(
            {
                "dataset": dataset,
                "universe_scope": universe_scope,
                "source_target_streams": len(selected),
                "paths_with_pairs": sum(value > 0 for value in path_pairs),
                "minimum_pairs_per_path": min(path_pairs),
                "median_pairs_per_path": statistics.median(path_pairs),
                "maximum_pairs_per_path": max(path_pairs),
                "all_unequal_age_pairs": combined.pairs,
                "older_wins": combined.wins,
                "ties": combined.ties,
                "older_losses": combined.losses,
                "older_age_auc": combined.auc,
                "sources_above_half": positive,
                "sources_below_half": negative,
                "sources_tied_half": len(aucs) - positive - negative,
                "source_sign_lower_p": _binomial_lower_p(positive, negative),
                "source_sign_upper_p": _binomial_upper_p(positive, negative),
                "both_already_carried_pairs": carried.pairs,
                "carried_older_wins": carried.wins,
                "carried_ties": carried.ties,
                "carried_older_losses": carried.losses,
                "carried_older_age_auc": carried.auc,
                "carried_sources_above_half": carried_positive,
                "carried_sources_below_half": carried_negative,
                "carried_sources_tied_half": (
                    len(carried_aucs) - carried_positive - carried_negative
                ),
                "carried_source_sign_lower_p": carried_lower_p,
                "carried_source_sign_upper_p": carried_upper_p,
                "carried_source_sign_two_sided_p": min(
                    1.0,
                    2 * min(carried_lower_p, carried_upper_p),
                ),
                "maximum_observed_run_length": max(
                    (item.older_age for item in combined.outcomes),
                    default=0,
                ),
                "matching_uses_same_neuron_pair": 1,
                "matching_uses_historical_frequency_through_current": 1,
                "age_uses_consecutive_active_episodes_through_current": 1,
                "fixed_age_bins_used": 0,
                "fixed_threshold_used_by_primary_comparison": 0,
                "predictor_reads_next_episode": 0,
                "outcome_is_next_episode": 1,
                "source_labels_used_by_predictor": 0,
                "asset_or_year_used_by_predictor": 0,
                "field_learning_used": 0,
                "memory_read": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
        )
    return source_rows, summary_rows, age_rows


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    senses = {world.key: _world_senses(str(world.source), world.start) for world in worlds}
    universes = {target.key: "a" if target in universe_a else "b" for target in targets}
    observations = []
    path_rows = []
    for source in sources:
        source_field, source_segmenter, boundary_tick, _ = _source_state(senses[source.key])
        for target in targets:
            _, strict = _target_episodes(
                source_field,
                source_segmenter,
                boundary_tick,
                senses[target.key],
            )
            result = _matched_age_continuation(strict)
            carried = result.where(minimum_younger_age=2)
            observations.append(
                {"source_key": source.key, "universe": universes[target.key], "result": result}
            )
            path_rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "target_key_posthoc": target.key,
                    "target_universe": universes[target.key],
                    "strict_episode_count": len(strict),
                    "matched_steps": result.matched_steps,
                    "all_unequal_age_pairs": result.pairs,
                    "older_wins": result.wins,
                    "ties": result.ties,
                    "older_losses": result.losses,
                    "older_age_auc": result.auc,
                    "both_already_carried_pairs": carried.pairs,
                    "carried_older_age_auc": carried.auc,
                    "predictor_reads_next_episode": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
    sources_out, summaries, ages = _source_summary_and_age_rows(dataset, observations)
    return path_rows, sources_out, summaries, ages


def _all_rows() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    worlds = _worlds()
    outputs = ([], [], [], [])
    for dataset in ("2091_basis", "2092_holdout"):
        selected = [world for world in worlds if world.dataset == dataset]
        rows = _dataset_rows(dataset, selected)
        for output, additions in zip(outputs, rows):
            output.extend(additions)
    return outputs


def _write_csv(name: str, rows: list[dict]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    paths, sources, summaries, ages = _all_rows()
    for name, rows in (
        ("paths", paths),
        ("sources", sources),
        ("summary", summaries),
        ("exact_ages", ages),
    ):
        _write_csv(name, rows)
    for row in summaries:
        print(f"dataset={row['dataset']} universe_scope={row['universe_scope']}")
        print(f"pairs={row['all_unequal_age_pairs']} auc={row['older_age_auc']}")
        print(
            "source_directions="
            f"{row['sources_above_half']}/"
            f"{row['sources_below_half']}/"
            f"{row['sources_tied_half']}"
        )
        print(
            f"both_carried_pairs={row['both_already_carried_pairs']} "
            f"auc={row['carried_older_age_auc']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
