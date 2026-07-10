from __future__ import annotations

import csv
import hashlib
import random
import statistics
import sys
from collections import Counter, defaultdict
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
PREFIX = "2120_MCM_KOLLEKTIVE_ERNEUERUNGSKONFIGURATIONSTOPOLOGIE"
TRANSITIONS_PER_PAIR = 6
SOURCE_PERMUTATIONS = 100
SUMMARY_PERMUTATIONS = 300
SWAP_ATTEMPTS_PER_MEMBERSHIP = 5


def _renewal_configurations(
    episodes: list[ClosedRankEpisode],
) -> tuple[tuple[int, ...], ...]:
    supports = [
        tuple(int(value != 0) for value in episode.values)
        for episode in episodes
    ]
    if len(supports) < 3:
        return ()

    cumulative = list(supports[0])
    configurations = []
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

        renewing_pairs = set()
        for (neuron_pair, _), (carried, new) in groups.items():
            if not carried or not new:
                continue
            ending = any(not following[slot] for slot in carried)
            continuing = any(following[slot] for slot in new)
            if ending and continuing:
                renewing_pairs.add(neuron_pair)
        if renewing_pairs:
            configurations.append(tuple(sorted(renewing_pairs)))
    return tuple(configurations)


def _configuration_counter(
    paths: list[tuple[tuple[int, ...], ...]],
) -> Counter:
    return Counter(
        configuration
        for path in paths
        for configuration in path
        if len(configuration) > 1
    )


def _co_pair_counter(paths: list[tuple[tuple[int, ...], ...]]) -> Counter:
    return Counter(
        pair
        for path in paths
        for configuration in path
        for pair in combinations(configuration, 2)
    )


def _collision_pairs(counter: Counter) -> int:
    return sum(support * (support - 1) // 2 for support in counter.values())


def _cross_matches(left: Counter, right: Counter) -> int:
    return sum(support * right.get(key, 0) for key, support in left.items())


def _path_has_swap(path: tuple[tuple[int, ...], ...]) -> bool:
    sets = [set(configuration) for configuration in path]
    return any(left - right and right - left for left, right in combinations(sets, 2))


def _degree_preserving_rewire(
    path: tuple[tuple[int, ...], ...],
    rng: random.Random,
) -> tuple[tuple[tuple[int, ...], ...], int, int]:
    rows = [set(configuration) for configuration in path]
    memberships = sum(len(row) for row in rows)
    attempts = SWAP_ATTEMPTS_PER_MEMBERSHIP * memberships
    accepted = 0
    if len(rows) < 2:
        return path, accepted, attempts
    for _ in range(attempts):
        left_index, right_index = rng.sample(range(len(rows)), 2)
        left = rows[left_index]
        right = rows[right_index]
        left_only = tuple(left - right)
        right_only = tuple(right - left)
        if not left_only or not right_only:
            continue
        left_pair = rng.choice(left_only)
        right_pair = rng.choice(right_only)
        left.remove(left_pair)
        left.add(right_pair)
        right.remove(right_pair)
        right.add(left_pair)
        accepted += 1
    return (
        tuple(tuple(sorted(row)) for row in rows),
        accepted,
        attempts,
    )


def _seed(label: str) -> int:
    return int.from_bytes(
        hashlib.sha256(label.encode("utf-8")).digest()[:8],
        "big",
    )


def _empirical_upper_p(observed: int, values: list[int]) -> float:
    return (1 + sum(value >= observed for value in values)) / (len(values) + 1)


def _rewired_paths(
    paths: list[tuple[tuple[int, ...], ...]],
    rng: random.Random,
) -> tuple[list[tuple[tuple[int, ...], ...]], int, int]:
    rewired = []
    accepted = attempted = 0
    for path in paths:
        changed, path_accepted, path_attempted = _degree_preserving_rewire(
            path, rng
        )
        rewired.append(changed)
        accepted += path_accepted
        attempted += path_attempted
    return rewired, accepted, attempted


def _within_result(
    paths: list[tuple[tuple[int, ...], ...]],
    permutations: int,
    seed_label: str,
) -> dict[str, object]:
    configurations = _configuration_counter(paths)
    co_pairs = _co_pair_counter(paths)
    observed_configuration = _collision_pairs(configurations)
    observed_co_pair = _collision_pairs(co_pairs)
    mutable_paths = sum(_path_has_swap(path) for path in paths)
    configuration_null = []
    co_pair_null = []
    accepted_values = []
    attempted = 0
    if mutable_paths:
        rng = random.Random(_seed(seed_label))
        for _ in range(permutations):
            rewired, accepted, attempted = _rewired_paths(paths, rng)
            configuration_null.append(
                _collision_pairs(_configuration_counter(rewired))
            )
            co_pair_null.append(_collision_pairs(_co_pair_counter(rewired)))
            accepted_values.append(accepted)
    else:
        configuration_null = [observed_configuration] * permutations
        co_pair_null = [observed_co_pair] * permutations
        accepted_values = [0] * permutations
        attempted = sum(
            SWAP_ATTEMPTS_PER_MEMBERSHIP
            * sum(len(configuration) for configuration in path)
            for path in paths
        )
    config_mean = statistics.mean(configuration_null)
    co_pair_mean = statistics.mean(co_pair_null)
    widths = [len(configuration) for path in paths for configuration in path]
    return {
        "paths": len(paths),
        "renewal_moments": len(widths),
        "multi_pair_moments": sum(width > 1 for width in widths),
        "maximum_configuration_width": max(widths, default=0),
        "pair_memberships": sum(widths),
        "unique_configurations": len(configurations),
        "recurring_configurations": sum(value > 1 for value in configurations.values()),
        "observed_configuration_collision_pairs": observed_configuration,
        "null_configuration_collision_mean": config_mean,
        "configuration_collision_delta": observed_configuration - config_mean,
        "configuration_empirical_upper_p": _empirical_upper_p(
            observed_configuration, configuration_null
        ),
        "unique_co_pair_edges": len(co_pairs),
        "recurring_co_pair_edges": sum(value > 1 for value in co_pairs.values()),
        "observed_co_pair_collision_pairs": observed_co_pair,
        "null_co_pair_collision_mean": co_pair_mean,
        "co_pair_collision_delta": observed_co_pair - co_pair_mean,
        "co_pair_empirical_upper_p": _empirical_upper_p(
            observed_co_pair, co_pair_null
        ),
        "resample_mutable_paths": mutable_paths,
        "accepted_swaps_mean": statistics.mean(accepted_values),
        "attempted_swaps_per_permutation": attempted,
        "permutations": permutations,
    }


def _cross_result(
    left: list[tuple[tuple[int, ...], ...]],
    right: list[tuple[tuple[int, ...], ...]],
    permutations: int,
    seed_label: str,
) -> dict[str, object]:
    observed_configuration = _cross_matches(
        _configuration_counter(left), _configuration_counter(right)
    )
    observed_co_pair = _cross_matches(
        _co_pair_counter(left), _co_pair_counter(right)
    )
    mutable_paths = sum(_path_has_swap(path) for path in left + right)
    configuration_null = []
    co_pair_null = []
    accepted_values = []
    if mutable_paths:
        rng = random.Random(_seed(seed_label))
        for _ in range(permutations):
            null_left, accepted_left, _ = _rewired_paths(left, rng)
            null_right, accepted_right, _ = _rewired_paths(right, rng)
            configuration_null.append(
                _cross_matches(
                    _configuration_counter(null_left),
                    _configuration_counter(null_right),
                )
            )
            co_pair_null.append(
                _cross_matches(
                    _co_pair_counter(null_left),
                    _co_pair_counter(null_right),
                )
            )
            accepted_values.append(accepted_left + accepted_right)
    else:
        configuration_null = [observed_configuration] * permutations
        co_pair_null = [observed_co_pair] * permutations
        accepted_values = [0] * permutations
    config_mean = statistics.mean(configuration_null)
    co_pair_mean = statistics.mean(co_pair_null)
    return {
        "paths_a": len(left),
        "paths_b": len(right),
        "observed_cross_configuration_matches": observed_configuration,
        "null_cross_configuration_mean": config_mean,
        "cross_configuration_delta": observed_configuration - config_mean,
        "cross_configuration_empirical_upper_p": _empirical_upper_p(
            observed_configuration, configuration_null
        ),
        "observed_cross_co_pair_matches": observed_co_pair,
        "null_cross_co_pair_mean": co_pair_mean,
        "cross_co_pair_delta": observed_co_pair - co_pair_mean,
        "cross_co_pair_empirical_upper_p": _empirical_upper_p(
            observed_co_pair, co_pair_null
        ),
        "resample_mutable_paths": mutable_paths,
        "accepted_swaps_mean": statistics.mean(accepted_values),
        "permutations": permutations,
    }


def _sign_fields(rows: list[dict], value: str, prefix: str) -> dict[str, object]:
    positive = sum(float(row[value]) > 0 for row in rows)
    negative = sum(float(row[value]) < 0 for row in rows)
    tied = len(rows) - positive - negative
    lower = _binomial_lower_p(positive, negative)
    upper = _binomial_upper_p(positive, negative)
    return {
        f"sources_{prefix}_above_null": positive,
        f"sources_{prefix}_below_null": negative,
        f"sources_{prefix}_tied_null": tied,
        f"source_{prefix}_sign_lower_p": lower,
        f"source_{prefix}_sign_upper_p": upper,
        f"source_{prefix}_sign_two_sided_p": min(
            1.0, 2 * min(lower, upper)
        ),
    }


def _source_summary_and_configuration_rows(
    dataset: str,
    observations: list[dict],
) -> tuple[list[dict], list[dict], list[dict]]:
    source_rows = []
    summary_rows = []
    configuration_rows = []
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
            paths = [
                item["configurations"]
                for item in selected
                if item["source_key"] == source_key
            ]
            result = _within_result(
                paths,
                SOURCE_PERMUTATIONS,
                f"2120|{dataset}|{source_key}|{universe_scope}|within",
            )
            row = {
                "dataset": dataset,
                "analysis_kind": "within_collective_topology",
                "universe_scope": universe_scope,
                "source_key_posthoc": source_key,
                **result,
            }
            source_rows.append(row)
            per_source.append(row)

        paths = [item["configurations"] for item in selected]
        aggregate = _within_result(
            paths,
            SUMMARY_PERMUTATIONS,
            f"2120|{dataset}|{universe_scope}|within_summary",
        )
        summary_rows.append(
            {
                "dataset": dataset,
                "analysis_kind": "within_collective_topology",
                "universe_scope": universe_scope,
                **aggregate,
                **_sign_fields(
                    per_source,
                    "configuration_collision_delta",
                    "configuration",
                ),
                **_sign_fields(
                    per_source,
                    "co_pair_collision_delta",
                    "co_pair",
                ),
                "null_preserves_each_path": 1,
                "null_preserves_moment_widths": 1,
                "null_preserves_pair_renewal_counts": 1,
                "fixed_support_threshold_used": 0,
                "memory_read": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
        )
        counter = _configuration_counter(paths)
        for configuration, support in sorted(counter.items()):
            configuration_rows.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "configuration": "|".join(map(str, configuration)),
                    "width": len(configuration),
                    "support": support,
                }
            )

    transfer_sources = []
    for source_key in source_keys:
        left = [
            item["configurations"]
            for item in observations
            if item["source_key"] == source_key and item["universe"] == "a"
        ]
        right = [
            item["configurations"]
            for item in observations
            if item["source_key"] == source_key and item["universe"] == "b"
        ]
        result = _cross_result(
            left,
            right,
            SOURCE_PERMUTATIONS,
            f"2120|{dataset}|{source_key}|cross",
        )
        row = {
            "dataset": dataset,
            "analysis_kind": "cross_universe_collective_identity",
            "universe_scope": "a_to_b",
            "source_key_posthoc": source_key,
            **result,
        }
        source_rows.append(row)
        transfer_sources.append(row)

    left = [item["configurations"] for item in observations if item["universe"] == "a"]
    right = [item["configurations"] for item in observations if item["universe"] == "b"]
    aggregate = _cross_result(
        left,
        right,
        SUMMARY_PERMUTATIONS,
        f"2120|{dataset}|cross_summary",
    )
    summary_rows.append(
        {
            "dataset": dataset,
            "analysis_kind": "cross_universe_collective_identity",
            "universe_scope": "a_to_b",
            **aggregate,
            **_sign_fields(
                transfer_sources,
                "cross_configuration_delta",
                "configuration",
            ),
            **_sign_fields(
                transfer_sources,
                "cross_co_pair_delta",
                "co_pair",
            ),
            "null_preserves_each_path": 1,
            "null_preserves_moment_widths": 1,
            "null_preserves_pair_renewal_counts": 1,
            "fixed_support_threshold_used": 0,
            "memory_read": 0,
            "memory_written": 0,
            "influences_action": 0,
        }
    )
    return source_rows, summary_rows, configuration_rows


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
            configurations = _renewal_configurations(strict)
            widths = [len(configuration) for configuration in configurations]
            observations.append(
                {
                    "source_key": source.key,
                    "universe": universes[target.key],
                    "configurations": configurations,
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
                    "renewal_moments": len(configurations),
                    "multi_pair_moments": sum(width > 1 for width in widths),
                    "maximum_configuration_width": max(widths, default=0),
                    "pair_memberships": sum(widths),
                    "future_used_for_candidate_grouping": 0,
                    "future_used_for_renewal_outcome": 1,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
    sources_out, summaries, configurations = (
        _source_summary_and_configuration_rows(dataset, observations)
    )
    return path_rows, sources_out, summaries, configurations


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
    paths, sources, summaries, configurations = _all_rows()
    for name, rows in (
        ("paths", paths),
        ("sources", sources),
        ("summary", summaries),
        ("configurations", configurations),
    ):
        _write_csv(name, rows)
    for row in summaries:
        print(
            f"dataset={row['dataset']} kind={row['analysis_kind']} "
            f"scope={row['universe_scope']}"
        )
        if row["analysis_kind"] == "within_collective_topology":
            print(
                f"moments={row['renewal_moments']} "
                f"multi={row['multi_pair_moments']} "
                f"max_width={row['maximum_configuration_width']}"
            )
            print(
                f"config_collision={row['observed_configuration_collision_pairs']} "
                f"null={row['null_configuration_collision_mean']} "
                f"p={row['configuration_empirical_upper_p']}"
            )
            print(
                f"co_pair_collision={row['observed_co_pair_collision_pairs']} "
                f"null={row['null_co_pair_collision_mean']} "
                f"p={row['co_pair_empirical_upper_p']}"
            )
        else:
            print(
                f"cross_config={row['observed_cross_configuration_matches']} "
                f"null={row['null_cross_configuration_mean']} "
                f"p={row['cross_configuration_empirical_upper_p']}"
            )
            print(
                f"cross_co_pair={row['observed_cross_co_pair_matches']} "
                f"null={row['null_cross_co_pair_mean']} "
                f"p={row['cross_co_pair_empirical_upper_p']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
