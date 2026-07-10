from __future__ import annotations

import csv
import math
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_continuous_field_instance import _world_senses, _worlds
from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuity_target_universe_transfer import _universe_split
from tools.run_mcm_continuous_rank_self_segmentation import (
    ClosedRankEpisode,
    _source_state,
    _target_episodes,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2117_MCM_PRAEQUENTIELLE_PARTIALRELATIONSFORTSETZUNG"
MATCH_SCOPES = ("frequency", "neuron_pair_and_frequency")


@dataclass(frozen=True)
class MatchedContinuation:
    wins: int
    ties: int
    losses: int
    pairs: int
    matched_steps: int
    matched_carried_candidates: int
    matched_new_candidates: int

    @property
    def auc(self) -> float:
        if self.pairs == 0:
            return 0.5
        return (self.wins + 0.5 * self.ties) / self.pairs


def _matched_continuation(
    episodes: list[ClosedRankEpisode],
    same_neuron_pair: bool,
) -> MatchedContinuation:
    supports = [
        tuple(int(value != 0) for value in episode.values)
        for episode in episodes
    ]
    if len(supports) < 3:
        return MatchedContinuation(0, 0, 0, 0, 0, 0, 0)

    cumulative = list(supports[0])
    wins = ties = losses = pairs = 0
    matched_steps = 0
    matched_carried = 0
    matched_new = 0
    transitions_per_pair = 6

    for index in range(1, len(supports) - 1):
        previous = supports[index - 1]
        current = supports[index]
        following = supports[index + 1]
        for slot, active in enumerate(current):
            cumulative[slot] += active

        groups: dict[tuple[int, ...], list[list[int]]] = defaultdict(
            lambda: [[], []]
        )
        for slot, active in enumerate(current):
            if not active:
                continue
            key = (cumulative[slot],)
            if same_neuron_pair:
                key = (slot // transitions_per_pair, cumulative[slot])
            carried_index = 0 if previous[slot] else 1
            groups[key][carried_index].append(following[slot])

        step_matched = False
        for carried_outcomes, new_outcomes in groups.values():
            if not carried_outcomes or not new_outcomes:
                continue
            step_matched = True
            matched_carried += len(carried_outcomes)
            matched_new += len(new_outcomes)
            carried_one = sum(carried_outcomes)
            carried_zero = len(carried_outcomes) - carried_one
            new_one = sum(new_outcomes)
            new_zero = len(new_outcomes) - new_one
            wins += carried_one * new_zero
            losses += carried_zero * new_one
            ties += carried_one * new_one + carried_zero * new_zero
            pairs += len(carried_outcomes) * len(new_outcomes)
        matched_steps += int(step_matched)

    return MatchedContinuation(
        wins=wins,
        ties=ties,
        losses=losses,
        pairs=pairs,
        matched_steps=matched_steps,
        matched_carried_candidates=matched_carried,
        matched_new_candidates=matched_new,
    )


def _binomial_upper_p(positive: int, negative: int) -> float:
    trials = positive + negative
    if trials == 0:
        return 1.0
    numerator = sum(math.comb(trials, count) for count in range(positive, trials + 1))
    return numerator / (2**trials)


def _binomial_lower_p(positive: int, negative: int) -> float:
    trials = positive + negative
    if trials == 0:
        return 1.0
    numerator = sum(math.comb(trials, count) for count in range(0, positive + 1))
    return numerator / (2**trials)


def _combine(results: list[MatchedContinuation]) -> MatchedContinuation:
    return MatchedContinuation(
        wins=sum(result.wins for result in results),
        ties=sum(result.ties for result in results),
        losses=sum(result.losses for result in results),
        pairs=sum(result.pairs for result in results),
        matched_steps=sum(result.matched_steps for result in results),
        matched_carried_candidates=sum(
            result.matched_carried_candidates for result in results
        ),
        matched_new_candidates=sum(
            result.matched_new_candidates for result in results
        ),
    )


def _scope_paths(observations: list[dict], universe_scope: str) -> list[dict]:
    if universe_scope == "all":
        return observations
    if universe_scope == "universe_a":
        return [item for item in observations if item["universe"] == "a"]
    if universe_scope == "universe_b":
        return [item for item in observations if item["universe"] == "b"]
    raise ValueError(f"unknown universe scope: {universe_scope}")


def _result_for_scope(item: dict, match_scope: str) -> MatchedContinuation:
    if match_scope == "frequency":
        return item["frequency_result"]
    if match_scope == "neuron_pair_and_frequency":
        return item["pair_frequency_result"]
    raise ValueError(f"unknown match scope: {match_scope}")


def _source_and_summary_rows(
    dataset: str,
    observations: list[dict],
) -> tuple[list[dict], list[dict]]:
    source_rows = []
    summary_rows = []
    source_keys = sorted({item["source_key"] for item in observations})
    for match_scope in MATCH_SCOPES:
        for universe_scope in ("all", "universe_a", "universe_b"):
            selected = _scope_paths(observations, universe_scope)
            source_results = []
            for source_key in source_keys:
                paths = [item for item in selected if item["source_key"] == source_key]
                combined = _combine(
                    [_result_for_scope(item, match_scope) for item in paths]
                )
                if combined.pairs > 0:
                    source_results.append(combined)
                source_rows.append(
                    {
                        "dataset": dataset,
                        "match_scope": match_scope,
                        "universe_scope": universe_scope,
                        "source_key_posthoc": source_key,
                        "source_target_streams": len(paths),
                        "matched_steps": combined.matched_steps,
                        "matched_pairs": combined.pairs,
                        "carried_wins": combined.wins,
                        "ties": combined.ties,
                        "carried_losses": combined.losses,
                        "prequential_auc": combined.auc,
                        "predictor_reads_next_episode": 0,
                        "outcome_is_next_episode": 1,
                        "field_learning_used": 0,
                        "memory_read": 0,
                        "memory_written": 0,
                        "influences_action": 0,
                    }
                )

            path_results = [_result_for_scope(item, match_scope) for item in selected]
            combined_all = _combine(path_results)
            source_aucs = [result.auc for result in source_results]
            positive = sum(auc > 0.5 for auc in source_aucs)
            negative = sum(auc < 0.5 for auc in source_aucs)
            tied = sum(auc == 0.5 for auc in source_aucs)
            path_pair_counts = [result.pairs for result in path_results]
            upper_p = _binomial_upper_p(positive, negative)
            lower_p = _binomial_lower_p(positive, negative)
            summary_rows.append(
                {
                    "dataset": dataset,
                    "match_scope": match_scope,
                    "universe_scope": universe_scope,
                    "source_target_streams": len(selected),
                    "paths_with_matched_pairs": sum(
                        count > 0 for count in path_pair_counts
                    ),
                    "minimum_matched_pairs_per_path": min(path_pair_counts),
                    "median_matched_pairs_per_path": statistics.median(
                        path_pair_counts
                    ),
                    "maximum_matched_pairs_per_path": max(path_pair_counts),
                    "total_matched_steps": combined_all.matched_steps,
                    "total_matched_pairs": combined_all.pairs,
                    "carried_wins": combined_all.wins,
                    "ties": combined_all.ties,
                    "carried_losses": combined_all.losses,
                    "pair_weighted_prequential_auc": combined_all.auc,
                    "sources_with_matched_pairs": len(source_results),
                    "median_source_prequential_auc": statistics.median(
                        source_aucs
                    ) if source_aucs else 0.5,
                    "mean_source_prequential_auc": statistics.mean(
                        source_aucs
                    ) if source_aucs else 0.5,
                    "sources_above_half": positive,
                    "sources_below_half": negative,
                    "sources_tied_half": tied,
                    "source_sign_upper_p": upper_p,
                    "source_sign_lower_p": lower_p,
                    "source_sign_two_sided_p": min(
                        1.0,
                        2 * min(upper_p, lower_p),
                    ),
                    "matching_uses_historical_frequency_through_current": 1,
                    "strict_matching_uses_same_neuron_pair": int(
                        match_scope == "neuron_pair_and_frequency"
                    ),
                    "predictor_reads_next_episode": 0,
                    "outcome_is_next_episode": 1,
                    "source_labels_used_by_predictor": 0,
                    "asset_or_year_used_by_predictor": 0,
                    "fixed_threshold_used": 0,
                    "field_learning_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
    return source_rows, summary_rows


def _dataset_rows(dataset: str, worlds: list) -> tuple[list[dict], list[dict], list[dict]]:
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
        source_field, source_segmenter, boundary_tick, _ = _source_state(
            senses[source.key]
        )
        for target in targets:
            _, strict = _target_episodes(
                source_field,
                source_segmenter,
                boundary_tick,
                senses[target.key],
            )
            frequency_result = _matched_continuation(
                strict,
                same_neuron_pair=False,
            )
            pair_frequency_result = _matched_continuation(
                strict,
                same_neuron_pair=True,
            )
            observations.append(
                {
                    "source_key": source.key,
                    "universe": target_universe[target.key],
                    "frequency_result": frequency_result,
                    "pair_frequency_result": pair_frequency_result,
                }
            )
            path_rows.append(
                {
                    "dataset": dataset,
                    "source_key_posthoc": source.key,
                    "source_asset_posthoc": source.asset,
                    "source_year_posthoc": source.year,
                    "target_key_posthoc": target.key,
                    "target_universe": target_universe[target.key],
                    "strict_episode_count": len(strict),
                    "frequency_matched_steps": frequency_result.matched_steps,
                    "frequency_matched_pairs": frequency_result.pairs,
                    "frequency_carried_wins": frequency_result.wins,
                    "frequency_ties": frequency_result.ties,
                    "frequency_carried_losses": frequency_result.losses,
                    "frequency_prequential_auc": frequency_result.auc,
                    "pair_frequency_matched_steps": (
                        pair_frequency_result.matched_steps
                    ),
                    "pair_frequency_matched_pairs": pair_frequency_result.pairs,
                    "pair_frequency_carried_wins": pair_frequency_result.wins,
                    "pair_frequency_ties": pair_frequency_result.ties,
                    "pair_frequency_carried_losses": pair_frequency_result.losses,
                    "pair_frequency_prequential_auc": pair_frequency_result.auc,
                    "matching_uses_historical_frequency_through_current": 1,
                    "predictor_reads_next_episode": 0,
                    "outcome_is_next_episode": 1,
                    "source_labels_used_by_predictor": 0,
                    "asset_or_year_used_by_predictor": 0,
                    "fixed_threshold_used": 0,
                    "field_learning_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
    source_rows, summary_rows = _source_and_summary_rows(
        dataset,
        observations,
    )
    return path_rows, source_rows, summary_rows


def _all_rows() -> tuple[list[dict], list[dict], list[dict]]:
    worlds = _worlds()
    path_rows = []
    source_rows = []
    summary_rows = []
    for dataset in ("2091_basis", "2092_holdout"):
        selected = [world for world in worlds if world.dataset == dataset]
        paths, sources, summaries = _dataset_rows(dataset, selected)
        path_rows.extend(paths)
        source_rows.extend(sources)
        summary_rows.extend(summaries)
    return path_rows, source_rows, summary_rows


def _write_csv(name: str, rows: list[dict]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    path_rows, source_rows, summary_rows = _all_rows()
    _write_csv("paths", path_rows)
    _write_csv("sources", source_rows)
    _write_csv("summary", summary_rows)
    for row in summary_rows:
        print(
            f"dataset={row['dataset']} match_scope={row['match_scope']} "
            f"universe_scope={row['universe_scope']}"
        )
        print(f"matched_pairs={row['total_matched_pairs']}")
        print(f"prequential_auc={row['pair_weighted_prequential_auc']}")
        print(
            "source_directions="
            f"{row['sources_above_half']}/"
            f"{row['sources_below_half']}/"
            f"{row['sources_tied_half']}"
        )
        print(f"source_sign_p={row['source_sign_upper_p']}")
        print(f"source_sign_lower_p={row['source_sign_lower_p']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
