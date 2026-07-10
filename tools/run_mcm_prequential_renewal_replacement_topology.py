from __future__ import annotations

import csv
import hashlib
import math
import random
import statistics
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
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
PREFIX = "2119_MCM_PRAEQUENTIELLE_ERNEUERUNGSABLOESUNGSTOPOLOGIE"
TRANSITIONS_PER_PAIR = 6
SOURCE_PERMUTATIONS = 200
SUMMARY_PERMUTATIONS = 500


@dataclass(frozen=True)
class ReplacementOpportunity:
    neuron_pair: int
    historical_frequency: int
    carried_candidates: tuple[int, ...]
    new_candidates: tuple[int, ...]
    ending_carried: tuple[int, ...]
    continuing_new: tuple[int, ...]

    @property
    def edge_instances(self) -> int:
        return len(self.ending_carried) * len(self.continuing_new)


def _replacement_opportunities(
    episodes: list[ClosedRankEpisode],
) -> tuple[ReplacementOpportunity, ...]:
    supports = [
        tuple(int(value != 0) for value in episode.values)
        for episode in episodes
    ]
    if len(supports) < 3:
        return ()

    cumulative = list(supports[0])
    opportunities = []
    for index in range(1, len(supports) - 1):
        previous = supports[index - 1]
        current = supports[index]
        following = supports[index + 1]
        for slot, active in enumerate(current):
            cumulative[slot] += active

        groups: dict[tuple[int, int], list[list[int]]] = defaultdict(
            lambda: [[], []]
        )
        for slot, active in enumerate(current):
            if not active:
                continue
            key = (slot // TRANSITIONS_PER_PAIR, cumulative[slot])
            status = 0 if previous[slot] else 1
            groups[key][status].append(slot)

        for (neuron_pair, frequency), candidate_groups in groups.items():
            carried, new = candidate_groups
            if not carried or not new:
                continue
            ending = tuple(slot for slot in carried if not following[slot])
            continuing = tuple(slot for slot in new if following[slot])
            opportunities.append(
                ReplacementOpportunity(
                    neuron_pair=neuron_pair,
                    historical_frequency=frequency,
                    carried_candidates=tuple(carried),
                    new_candidates=tuple(new),
                    ending_carried=ending,
                    continuing_new=continuing,
                )
            )
    return tuple(opportunities)


def _observed_edges(
    opportunities: tuple[ReplacementOpportunity, ...] | list[ReplacementOpportunity],
) -> Counter:
    return Counter(
        (left, right)
        for opportunity in opportunities
        for left in opportunity.ending_carried
        for right in opportunity.continuing_new
    )


def _is_resample_mutable(opportunity: ReplacementOpportunity) -> bool:
    return opportunity.edge_instances > 0 and (
        len(opportunity.ending_carried) < len(opportunity.carried_candidates)
        or len(opportunity.continuing_new) < len(opportunity.new_candidates)
    )


def _resampled_edges(
    opportunities: tuple[ReplacementOpportunity, ...] | list[ReplacementOpportunity],
    rng: random.Random,
) -> Counter:
    edges = Counter()
    for opportunity in opportunities:
        if opportunity.edge_instances == 0:
            continue
        if not _is_resample_mutable(opportunity):
            edges.update(
                (left, right)
                for left in opportunity.ending_carried
                for right in opportunity.continuing_new
            )
            continue
        ending = rng.sample(
            opportunity.carried_candidates,
            len(opportunity.ending_carried),
        )
        continuing = rng.sample(
            opportunity.new_candidates,
            len(opportunity.continuing_new),
        )
        edges.update((left, right) for left in ending for right in continuing)
    return edges


def _collision_pairs(edges: Counter) -> int:
    return sum(support * (support - 1) // 2 for support in edges.values())


def _cross_universe_matches(left: Counter, right: Counter) -> int:
    return sum(
        support * right.get(edge, 0)
        for edge, support in left.items()
    )


def _seed(label: str) -> int:
    return int.from_bytes(
        hashlib.sha256(label.encode("utf-8")).digest()[:8],
        "big",
    )


def _empirical_upper_p(observed: int, null_values: list[int]) -> float:
    return (1 + sum(value >= observed for value in null_values)) / (
        len(null_values) + 1
    )


def _within_result(
    opportunities: list[ReplacementOpportunity],
    permutations: int,
    seed_label: str,
) -> dict[str, object]:
    observed_edges = _observed_edges(opportunities)
    observed = _collision_pairs(observed_edges)
    mutable = [item for item in opportunities if _is_resample_mutable(item)]
    if mutable:
        rng = random.Random(_seed(seed_label))
        null_values = [
            _collision_pairs(_resampled_edges(opportunities, rng))
            for _ in range(permutations)
        ]
    else:
        null_values = [observed] * permutations
    return {
        "opportunities": len(opportunities),
        "realized_replacement_events": sum(
            opportunity.edge_instances > 0 for opportunity in opportunities
        ),
        "resample_mutable_replacement_events": sum(
            _is_resample_mutable(opportunity) for opportunity in opportunities
        ),
        "edge_instances_from_mutable_events": sum(
            opportunity.edge_instances
            for opportunity in opportunities
            if _is_resample_mutable(opportunity)
        ),
        "edge_instances": sum(observed_edges.values()),
        "unique_edges": len(observed_edges),
        "recurring_edges": sum(value > 1 for value in observed_edges.values()),
        "maximum_edge_support": max(observed_edges.values(), default=0),
        "observed_collision_pairs": observed,
        "null_collision_mean": statistics.mean(null_values),
        "null_collision_min": min(null_values),
        "null_collision_max": max(null_values),
        "collision_delta": observed - statistics.mean(null_values),
        "empirical_upper_p": _empirical_upper_p(observed, null_values),
        "permutations": permutations,
    }


def _cross_result(
    left: list[ReplacementOpportunity],
    right: list[ReplacementOpportunity],
    permutations: int,
    seed_label: str,
) -> dict[str, object]:
    left_edges = _observed_edges(left)
    right_edges = _observed_edges(right)
    observed = _cross_universe_matches(left_edges, right_edges)
    if any(_is_resample_mutable(item) for item in left + right):
        rng = random.Random(_seed(seed_label))
        null_values = []
        for _ in range(permutations):
            null_left = _resampled_edges(left, rng)
            null_right = _resampled_edges(right, rng)
            null_values.append(_cross_universe_matches(null_left, null_right))
    else:
        null_values = [observed] * permutations
    return {
        "opportunities_a": len(left),
        "opportunities_b": len(right),
        "edge_instances_a": sum(left_edges.values()),
        "edge_instances_b": sum(right_edges.values()),
        "observed_cross_edge_matches": observed,
        "null_cross_mean": statistics.mean(null_values),
        "null_cross_min": min(null_values),
        "null_cross_max": max(null_values),
        "cross_match_delta": observed - statistics.mean(null_values),
        "empirical_upper_p": _empirical_upper_p(observed, null_values),
        "permutations": permutations,
    }


def _direction_counts(rows: list[dict], value: str) -> tuple[int, int, int]:
    positive = sum(float(row[value]) > 0 for row in rows)
    negative = sum(float(row[value]) < 0 for row in rows)
    return positive, negative, len(rows) - positive - negative


def _source_and_summary_rows(
    dataset: str,
    observations: list[dict],
) -> tuple[list[dict], list[dict], list[dict]]:
    source_rows = []
    summary_rows = []
    edge_rows = []
    source_keys = sorted({item["source_key"] for item in observations})

    for universe_scope in ("all", "universe_a", "universe_b"):
        universe = universe_scope[-1]
        selected = (
            observations
            if universe_scope == "all"
            else [item for item in observations if item["universe"] == universe]
        )
        per_source = []
        for source_key in source_keys:
            opportunities = [
                opportunity
                for item in selected
                if item["source_key"] == source_key
                for opportunity in item["opportunities"]
            ]
            result = _within_result(
                opportunities,
                SOURCE_PERMUTATIONS,
                f"2119|{dataset}|{source_key}|{universe_scope}|within",
            )
            row = {
                "dataset": dataset,
                "analysis_kind": "within_universe_edge_recurrence",
                "universe_scope": universe_scope,
                "source_key_posthoc": source_key,
                **result,
                "source_labels_used_by_topology": 0,
            }
            source_rows.append(row)
            per_source.append(row)

        all_opportunities = [
            opportunity
            for item in selected
            for opportunity in item["opportunities"]
        ]
        aggregate = _within_result(
            all_opportunities,
            SUMMARY_PERMUTATIONS,
            f"2119|{dataset}|{universe_scope}|within_summary",
        )
        positive, negative, tied = _direction_counts(
            per_source, "collision_delta"
        )
        lower_p = _binomial_lower_p(positive, negative)
        upper_p = _binomial_upper_p(positive, negative)
        summary_rows.append(
            {
                "dataset": dataset,
                "analysis_kind": "within_universe_edge_recurrence",
                "universe_scope": universe_scope,
                **aggregate,
                "sources_above_null_mean": positive,
                "sources_below_null_mean": negative,
                "sources_tied_null_mean": tied,
                "source_sign_lower_p": lower_p,
                "source_sign_upper_p": upper_p,
                "source_sign_two_sided_p": min(
                    1.0, 2 * min(lower_p, upper_p)
                ),
                "null_preserves_real_opportunity_sets": 1,
                "null_preserves_pair_frequency_and_group_counts": 1,
                "fixed_support_threshold_used": 0,
                "future_used_for_candidate_grouping": 0,
                "future_used_for_replacement_outcome": 1,
                "memory_read": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
        )
        edge_counter = _observed_edges(all_opportunities)
        for (left, right), support in sorted(edge_counter.items()):
            edge_rows.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "neuron_pair": left // TRANSITIONS_PER_PAIR,
                    "ending_carried_slot": left,
                    "continuing_new_slot": right,
                    "edge_support": support,
                }
            )

    transfer_source_rows = []
    for source_key in source_keys:
        left = [
            opportunity
            for item in observations
            if item["source_key"] == source_key and item["universe"] == "a"
            for opportunity in item["opportunities"]
        ]
        right = [
            opportunity
            for item in observations
            if item["source_key"] == source_key and item["universe"] == "b"
            for opportunity in item["opportunities"]
        ]
        result = _cross_result(
            left,
            right,
            SOURCE_PERMUTATIONS,
            f"2119|{dataset}|{source_key}|cross",
        )
        row = {
            "dataset": dataset,
            "analysis_kind": "cross_universe_edge_identity",
            "universe_scope": "a_to_b",
            "source_key_posthoc": source_key,
            **result,
            "source_labels_used_by_topology": 0,
        }
        source_rows.append(row)
        transfer_source_rows.append(row)

    all_a = [
        opportunity
        for item in observations
        if item["universe"] == "a"
        for opportunity in item["opportunities"]
    ]
    all_b = [
        opportunity
        for item in observations
        if item["universe"] == "b"
        for opportunity in item["opportunities"]
    ]
    aggregate_transfer = _cross_result(
        all_a,
        all_b,
        SUMMARY_PERMUTATIONS,
        f"2119|{dataset}|cross_summary",
    )
    positive, negative, tied = _direction_counts(
        transfer_source_rows, "cross_match_delta"
    )
    lower_p = _binomial_lower_p(positive, negative)
    upper_p = _binomial_upper_p(positive, negative)
    summary_rows.append(
        {
            "dataset": dataset,
            "analysis_kind": "cross_universe_edge_identity",
            "universe_scope": "a_to_b",
            **aggregate_transfer,
            "sources_above_null_mean": positive,
            "sources_below_null_mean": negative,
            "sources_tied_null_mean": tied,
            "source_sign_lower_p": lower_p,
            "source_sign_upper_p": upper_p,
            "source_sign_two_sided_p": min(1.0, 2 * min(lower_p, upper_p)),
            "null_preserves_real_opportunity_sets": 1,
            "null_preserves_pair_frequency_and_group_counts": 1,
            "fixed_support_threshold_used": 0,
            "future_used_for_candidate_grouping": 0,
            "future_used_for_replacement_outcome": 1,
            "memory_read": 0,
            "memory_written": 0,
            "influences_action": 0,
        }
    )
    return source_rows, summary_rows, edge_rows


def _dataset_rows(
    dataset: str,
    worlds: list,
) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    sources, universe_a, universe_b = _universe_split(worlds)
    targets = universe_a + universe_b
    senses = {
        world.key: _world_senses(str(world.source), world.start)
        for world in worlds
    }
    universes = {
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
            opportunities = _replacement_opportunities(strict)
            edges = _observed_edges(opportunities)
            observations.append(
                {
                    "source_key": source.key,
                    "universe": universes[target.key],
                    "opportunities": opportunities,
                }
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
                    "replacement_opportunities": len(opportunities),
                    "realized_replacement_events": sum(
                        opportunity.edge_instances > 0
                        for opportunity in opportunities
                    ),
                    "replacement_edge_instances": sum(edges.values()),
                    "unique_replacement_edges": len(edges),
                    "replacement_collision_pairs": _collision_pairs(edges),
                    "candidate_grouping_uses_next_episode": 0,
                    "replacement_outcome_uses_next_episode": 1,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
    source_rows, summary_rows, edge_rows = _source_and_summary_rows(
        dataset, observations
    )
    return path_rows, source_rows, summary_rows, edge_rows


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
    paths, sources, summaries, edges = _all_rows()
    for name, rows in (
        ("paths", paths),
        ("sources", sources),
        ("summary", summaries),
        ("edges", edges),
    ):
        _write_csv(name, rows)
    for row in summaries:
        print(
            f"dataset={row['dataset']} kind={row['analysis_kind']} "
            f"scope={row['universe_scope']}"
        )
        if row["analysis_kind"] == "within_universe_edge_recurrence":
            print(
                f"collision={row['observed_collision_pairs']} "
                f"null={row['null_collision_mean']} "
                f"p={row['empirical_upper_p']}"
            )
        else:
            print(
                f"cross_matches={row['observed_cross_edge_matches']} "
                f"null={row['null_cross_mean']} "
                f"p={row['empirical_upper_p']}"
            )
        print(
            "source_directions="
            f"{row['sources_above_null_mean']}/"
            f"{row['sources_below_null_mean']}/"
            f"{row['sources_tied_null_mean']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
