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
from tools.run_mcm_multi_episode_exact_recurrence import _canonical_episode_form
from tools.run_mcm_prequential_partial_relation_continuation import (
    _binomial_lower_p,
    _binomial_upper_p,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2121_MCM_INNENFORM_KOLLEKTIVE_ERNEUERUNGSKOPPLUNG"
TRANSITIONS_PER_PAIR = 6
SOURCE_PERMUTATIONS = 200
SUMMARY_PERMUTATIONS = 500

Context = tuple[int, ...]
Configuration = tuple[int, ...]
Observation = tuple[Context, Configuration]
PathObservations = tuple[Observation, ...]


def _contextual_renewal_observations(
    episodes: list[ClosedRankEpisode],
) -> PathObservations:
    supports = [
        tuple(int(value != 0) for value in episode.values)
        for episode in episodes
    ]
    if len(supports) < 3:
        return ()

    cumulative = list(supports[0])
    observations = []
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
            observations.append(
                (
                    _canonical_episode_form(episodes[index].values),
                    tuple(sorted(renewing_pairs)),
                )
            )
    return tuple(observations)


def _context_configuration_counter(paths: list[PathObservations]) -> Counter:
    return Counter(
        (context, configuration)
        for path in paths
        for context, configuration in path
        if len(configuration) > 1
    )


def _context_co_pair_counter(paths: list[PathObservations]) -> Counter:
    return Counter(
        (context, pair)
        for path in paths
        for context, configuration in path
        for pair in combinations(configuration, 2)
    )


def _context_counter(
    paths: list[PathObservations],
    *,
    collective_only: bool,
) -> Counter:
    return Counter(
        context
        for path in paths
        for context, configuration in path
        if not collective_only or len(configuration) > 1
    )


def _collision_pairs(counter: Counter) -> int:
    return sum(support * (support - 1) // 2 for support in counter.values())


def _cross_matches(left: Counter, right: Counter) -> int:
    return sum(support * right.get(key, 0) for key, support in left.items())


def _path_is_mutable(path: PathObservations) -> bool:
    by_width: dict[int, list[Observation]] = defaultdict(list)
    for observation in path:
        by_width[len(observation[1])].append(observation)
    return any(
        len({configuration for _, configuration in observations}) > 1
        and len({context for context, _ in observations}) > 1
        for observations in by_width.values()
    )


def _shuffle_configurations_within_width(
    path: PathObservations,
    rng: random.Random,
) -> PathObservations:
    configurations = [configuration for _, configuration in path]
    by_width: dict[int, list[int]] = defaultdict(list)
    for index, configuration in enumerate(configurations):
        by_width[len(configuration)].append(index)
    for indices in by_width.values():
        selected = [configurations[index] for index in indices]
        rng.shuffle(selected)
        for index, configuration in zip(indices, selected):
            configurations[index] = configuration
    return tuple(
        (context, configurations[index])
        for index, (context, _) in enumerate(path)
    )


def _seed(label: str) -> int:
    return int.from_bytes(
        hashlib.sha256(label.encode("utf-8")).digest()[:8],
        "big",
    )


def _empirical_upper_p(observed: int, values: list[int]) -> float:
    return (1 + sum(value >= observed for value in values)) / (len(values) + 1)


def _shuffled_paths(
    paths: list[PathObservations],
    rng: random.Random,
) -> list[PathObservations]:
    return [
        _shuffle_configurations_within_width(path, rng)
        for path in paths
    ]


def _coverage(paths: list[PathObservations]) -> dict[str, object]:
    contexts = _context_counter(paths, collective_only=False)
    collective_contexts = _context_counter(paths, collective_only=True)
    return {
        "paths": len(paths),
        "renewal_moments": sum(len(path) for path in paths),
        "collective_moments": sum(
            len(configuration) > 1
            for path in paths
            for _, configuration in path
        ),
        "unique_preceding_contexts": len(contexts),
        "repeated_preceding_context_classes": sum(
            support > 1 for support in contexts.values()
        ),
        "collective_context_classes": len(collective_contexts),
        "repeated_collective_context_classes": sum(
            support > 1 for support in collective_contexts.values()
        ),
        "collective_moments_in_repeated_contexts": sum(
            support for support in collective_contexts.values() if support > 1
        ),
        "shuffle_mutable_paths": sum(_path_is_mutable(path) for path in paths),
    }


def _within_result(
    paths: list[PathObservations],
    permutations: int,
    seed_label: str,
) -> dict[str, object]:
    observed_configuration = _collision_pairs(
        _context_configuration_counter(paths)
    )
    observed_co_pair = _collision_pairs(_context_co_pair_counter(paths))
    mutable_paths = sum(_path_is_mutable(path) for path in paths)
    if mutable_paths:
        rng = random.Random(_seed(seed_label))
        configuration_null = []
        co_pair_null = []
        for _ in range(permutations):
            shuffled = _shuffled_paths(paths, rng)
            configuration_null.append(
                _collision_pairs(_context_configuration_counter(shuffled))
            )
            co_pair_null.append(
                _collision_pairs(_context_co_pair_counter(shuffled))
            )
    else:
        configuration_null = [observed_configuration] * permutations
        co_pair_null = [observed_co_pair] * permutations
    configuration_mean = statistics.mean(configuration_null)
    co_pair_mean = statistics.mean(co_pair_null)
    return {
        **_coverage(paths),
        "observed_same_context_configuration_collisions": observed_configuration,
        "null_same_context_configuration_mean": configuration_mean,
        "same_context_configuration_delta": (
            observed_configuration - configuration_mean
        ),
        "same_context_configuration_empirical_upper_p": _empirical_upper_p(
            observed_configuration, configuration_null
        ),
        "observed_same_context_co_pair_collisions": observed_co_pair,
        "null_same_context_co_pair_mean": co_pair_mean,
        "same_context_co_pair_delta": observed_co_pair - co_pair_mean,
        "same_context_co_pair_empirical_upper_p": _empirical_upper_p(
            observed_co_pair, co_pair_null
        ),
        "permutations": permutations,
    }


def _cross_result(
    left: list[PathObservations],
    right: list[PathObservations],
    permutations: int,
    seed_label: str,
) -> dict[str, object]:
    observed_configuration = _cross_matches(
        _context_configuration_counter(left),
        _context_configuration_counter(right),
    )
    observed_co_pair = _cross_matches(
        _context_co_pair_counter(left),
        _context_co_pair_counter(right),
    )
    mutable_paths = sum(_path_is_mutable(path) for path in left + right)
    if mutable_paths:
        rng = random.Random(_seed(seed_label))
        configuration_null = []
        co_pair_null = []
        for _ in range(permutations):
            shuffled_left = _shuffled_paths(left, rng)
            shuffled_right = _shuffled_paths(right, rng)
            configuration_null.append(
                _cross_matches(
                    _context_configuration_counter(shuffled_left),
                    _context_configuration_counter(shuffled_right),
                )
            )
            co_pair_null.append(
                _cross_matches(
                    _context_co_pair_counter(shuffled_left),
                    _context_co_pair_counter(shuffled_right),
                )
            )
    else:
        configuration_null = [observed_configuration] * permutations
        co_pair_null = [observed_co_pair] * permutations
    configuration_mean = statistics.mean(configuration_null)
    co_pair_mean = statistics.mean(co_pair_null)
    left_contexts = _context_counter(left, collective_only=True)
    right_contexts = _context_counter(right, collective_only=True)
    return {
        "paths_a": len(left),
        "paths_b": len(right),
        "collective_context_instance_matches_a_b": _cross_matches(
            left_contexts, right_contexts
        ),
        "collective_context_classes_shared_a_b": len(
            set(left_contexts) & set(right_contexts)
        ),
        "shuffle_mutable_paths": mutable_paths,
        "observed_cross_context_configuration_matches": observed_configuration,
        "null_cross_context_configuration_mean": configuration_mean,
        "cross_context_configuration_delta": (
            observed_configuration - configuration_mean
        ),
        "cross_context_configuration_empirical_upper_p": _empirical_upper_p(
            observed_configuration, configuration_null
        ),
        "observed_cross_context_co_pair_matches": observed_co_pair,
        "null_cross_context_co_pair_mean": co_pair_mean,
        "cross_context_co_pair_delta": observed_co_pair - co_pair_mean,
        "cross_context_co_pair_empirical_upper_p": _empirical_upper_p(
            observed_co_pair, co_pair_null
        ),
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
        f"source_{prefix}_sign_two_sided_p": min(
            1.0, 2 * min(lower, upper)
        ),
    }


def _context_hash(context: Context) -> str:
    payload = ",".join(map(str, context)).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def _source_summary_and_association_rows(
    dataset: str,
    observations: list[dict],
) -> tuple[list[dict], list[dict], list[dict]]:
    source_rows = []
    summary_rows = []
    association_rows = []
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
                item["observations"]
                for item in selected
                if item["source_key"] == source_key
            ]
            result = _within_result(
                paths,
                SOURCE_PERMUTATIONS,
                f"2121|{dataset}|{source_key}|{universe_scope}|within",
            )
            row = {
                "dataset": dataset,
                "analysis_kind": "within_context_coupling",
                "universe_scope": universe_scope,
                "source_key_posthoc": source_key,
                **result,
            }
            source_rows.append(row)
            per_source.append(row)

        paths = [item["observations"] for item in selected]
        result = _within_result(
            paths,
            SUMMARY_PERMUTATIONS,
            f"2121|{dataset}|{universe_scope}|within_summary",
        )
        summary_rows.append(
            {
                "dataset": dataset,
                "analysis_kind": "within_context_coupling",
                "universe_scope": universe_scope,
                **result,
                **_sign_fields(
                    per_source,
                    "same_context_configuration_delta",
                    "configuration",
                ),
                **_sign_fields(
                    per_source,
                    "same_context_co_pair_delta",
                    "co_pair",
                ),
                "context_is_current_closed_episode_form": 1,
                "context_uses_next_episode": 0,
                "null_preserves_path_width_and_configuration_multiset": 1,
                "fixed_similarity_threshold_used": 0,
                "viranz_parameter_used": 0,
                "memory_read": 0,
                "memory_written": 0,
                "influences_action": 0,
            }
        )
        counter = _context_configuration_counter(paths)
        for (context, configuration), support in sorted(
            counter.items(), key=lambda item: (_context_hash(item[0][0]), item[0][1])
        ):
            association_rows.append(
                {
                    "dataset": dataset,
                    "universe_scope": universe_scope,
                    "preceding_context_sha256": _context_hash(context),
                    "context_nonzero_slots": sum(value != 0 for value in context),
                    "context_total_strength": sum(abs(value) for value in context),
                    "collective_configuration": "|".join(map(str, configuration)),
                    "support": support,
                }
            )

    transfer_sources = []
    for source_key in source_keys:
        left = [
            item["observations"]
            for item in observations
            if item["source_key"] == source_key and item["universe"] == "a"
        ]
        right = [
            item["observations"]
            for item in observations
            if item["source_key"] == source_key and item["universe"] == "b"
        ]
        result = _cross_result(
            left,
            right,
            SOURCE_PERMUTATIONS,
            f"2121|{dataset}|{source_key}|cross",
        )
        row = {
            "dataset": dataset,
            "analysis_kind": "cross_universe_context_coupling",
            "universe_scope": "a_to_b",
            "source_key_posthoc": source_key,
            **result,
        }
        source_rows.append(row)
        transfer_sources.append(row)

    left = [item["observations"] for item in observations if item["universe"] == "a"]
    right = [item["observations"] for item in observations if item["universe"] == "b"]
    result = _cross_result(
        left,
        right,
        SUMMARY_PERMUTATIONS,
        f"2121|{dataset}|cross_summary",
    )
    summary_rows.append(
        {
            "dataset": dataset,
            "analysis_kind": "cross_universe_context_coupling",
            "universe_scope": "a_to_b",
            **result,
            **_sign_fields(
                transfer_sources,
                "cross_context_configuration_delta",
                "configuration",
            ),
            **_sign_fields(
                transfer_sources,
                "cross_context_co_pair_delta",
                "co_pair",
            ),
            "context_is_current_closed_episode_form": 1,
            "context_uses_next_episode": 0,
            "null_preserves_path_width_and_configuration_multiset": 1,
            "fixed_similarity_threshold_used": 0,
            "viranz_parameter_used": 0,
            "memory_read": 0,
            "memory_written": 0,
            "influences_action": 0,
        }
    )
    return source_rows, summary_rows, association_rows


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
            path = _contextual_renewal_observations(strict)
            contexts = Counter(context for context, _ in path)
            observations.append(
                {
                    "source_key": source.key,
                    "universe": universes[target.key],
                    "observations": path,
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
                    "renewal_moments": len(path),
                    "collective_moments": sum(
                        len(configuration) > 1 for _, configuration in path
                    ),
                    "unique_preceding_contexts": len(contexts),
                    "repeated_preceding_context_classes": sum(
                        support > 1 for support in contexts.values()
                    ),
                    "shuffle_mutable": int(_path_is_mutable(path)),
                    "context_uses_next_episode": 0,
                    "viranz_parameter_used": 0,
                    "memory_read": 0,
                    "memory_written": 0,
                    "influences_action": 0,
                }
            )
    sources_out, summaries, associations = _source_summary_and_association_rows(
        dataset, observations
    )
    return path_rows, sources_out, summaries, associations


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
    paths, sources, summaries, associations = _all_rows()
    for name, rows in (
        ("paths", paths),
        ("sources", sources),
        ("summary", summaries),
        ("associations", associations),
    ):
        _write_csv(name, rows)
    for row in summaries:
        print(
            f"dataset={row['dataset']} kind={row['analysis_kind']} "
            f"scope={row['universe_scope']}"
        )
        if row["analysis_kind"] == "within_context_coupling":
            print(
                f"moments={row['renewal_moments']} "
                f"collective={row['collective_moments']} "
                f"repeated_context_collective={row['collective_moments_in_repeated_contexts']}"
            )
            print(
                f"configuration={row['observed_same_context_configuration_collisions']} "
                f"null={row['null_same_context_configuration_mean']} "
                f"p={row['same_context_configuration_empirical_upper_p']}"
            )
            print(
                f"co_pair={row['observed_same_context_co_pair_collisions']} "
                f"null={row['null_same_context_co_pair_mean']} "
                f"p={row['same_context_co_pair_empirical_upper_p']}"
            )
        else:
            print(
                f"shared_contexts={row['collective_context_classes_shared_a_b']} "
                f"configuration={row['observed_cross_context_configuration_matches']} "
                f"null={row['null_cross_context_configuration_mean']} "
                f"p={row['cross_context_configuration_empirical_upper_p']}"
            )
            print(
                f"co_pair={row['observed_cross_context_co_pair_matches']} "
                f"null={row['null_cross_context_co_pair_mean']} "
                f"p={row['cross_context_co_pair_empirical_upper_p']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
