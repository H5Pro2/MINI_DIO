from __future__ import annotations

import csv
import io
import math
import random
import statistics
import zipfile
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
LIFECYCLE_ARCHIVE = ROOT / "data" / "2090_mcm_relation_lifecycle_events.zip"
EVENT_ARCHIVE = ROOT / "data" / "2089_mcm_breadth_data_holdout_events.zip"
PREFIX = "2091_MCM_RELATIONSLEBENSLAUF_EIGENSTABILITAET"
LABEL_PERMUTATIONS = 2000
GRAPH_PERMUTATIONS = 1000
SEED = 2091


def _edge_sets() -> dict[int, set[tuple[str, str]]]:
    edges: dict[int, set[tuple[str, str]]] = defaultdict(set)
    with zipfile.ZipFile(LIFECYCLE_ARCHIVE) as archive:
        with archive.open("lifecycle_observations.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8"))
            for row in reader:
                pair = tuple(
                    sorted((str(row["left_relation"]), str(row["right_relation"])))
                )
                edges[int(row["relation_age"])].add(pair)
    return dict(edges)


def _maximum_relation_ages() -> dict[str, int]:
    ages = {}
    with zipfile.ZipFile(EVENT_ARCHIVE) as archive:
        with archive.open("event_histories.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8"))
            for row in reader:
                symbol = str(row["neighborhood_symbol"])
                ages[symbol] = max(ages.get(symbol, 0), int(row["event_index"]))
    return ages


def _restricted_edges(
    edges: set[tuple[str, str]], nodes: set[str]
) -> set[tuple[str, str]]:
    return {edge for edge in edges if edge[0] in nodes and edge[1] in nodes}


def _hypergeometric_moments(
    population: int, successes: int, draws: int
) -> tuple[float, float]:
    if population <= 0:
        return 0.0, 0.0
    mean = draws * successes / population
    if population <= 1:
        return mean, 0.0
    variance = (
        draws
        * successes
        * (population - successes)
        * (population - draws)
        / (population * population * (population - 1))
    )
    return mean, variance


def _transition_records(
    edges: dict[int, set[tuple[str, str]]], maximum_ages: dict[str, int]
) -> list[dict[str, object]]:
    records = []
    for age in range(3, max(edges, default=2)):
        eligible_nodes = {
            symbol
            for symbol, maximum_age in maximum_ages.items()
            if maximum_age >= age + 1
        }
        current = _restricted_edges(edges.get(age, set()), eligible_nodes)
        prior = _restricted_edges(edges.get(age - 1, set()), eligible_nodes)
        future = _restricted_edges(edges.get(age + 1, set()), eligible_nodes)
        carried = current & prior
        new = current - carried
        carried_continued = len(carried & future)
        new_continued = len(new & future)
        future_current = len(current & future)
        expected, variance = _hypergeometric_moments(
            len(current), future_current, len(carried)
        )
        z_score = (
            (carried_continued - expected) / math.sqrt(variance)
            if variance > 0.0
            else 0.0
        )
        records.append(
            {
                "relation_age": age,
                "eligible_nodes": len(eligible_nodes),
                "eligible_current_edges": len(current),
                "carried_edges": len(carried),
                "carried_continued": carried_continued,
                "carried_continuation_rate": carried_continued
                / max(1, len(carried)),
                "new_edges": len(new),
                "new_continued": new_continued,
                "new_continuation_rate": new_continued / max(1, len(new)),
                "continuation_rate_difference": carried_continued
                / max(1, len(carried))
                - new_continued / max(1, len(new)),
                "continuation_rate_ratio": (
                    carried_continued / max(1, len(carried))
                )
                / max(1e-12, new_continued / max(1, len(new))),
                "future_edges": len(future),
                "future_current_edges": future_current,
                "label_null_expected_carried_continuations": expected,
                "label_null_sd": math.sqrt(variance),
                "label_null_z_score": z_score,
                "informative": int(bool(carried) and bool(new)),
                "_eligible_node_symbols": sorted(eligible_nodes),
                "_carried_set": carried,
                "_new_set": new,
                "_future_set": future,
            }
        )
    return records


def _public_transition_rows(records: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        {key: value for key, value in record.items() if not key.startswith("_")}
        for record in records
    ]


def _mantel_haenszel_stats(records: list[dict[str, object]]) -> dict[str, object]:
    informative = [
        record
        for record in records
        if int(record["carried_edges"]) > 0 and int(record["new_edges"]) > 0
    ]
    carried_continued = sum(int(record["carried_continued"]) for record in informative)
    carried_stopped = sum(
        int(record["carried_edges"]) - int(record["carried_continued"])
        for record in informative
    )
    new_continued = sum(int(record["new_continued"]) for record in informative)
    new_stopped = sum(
        int(record["new_edges"]) - int(record["new_continued"])
        for record in informative
    )
    expected_sum = 0.0
    variance_sum = 0.0
    odds_numerator = 0.0
    odds_denominator = 0.0
    for record in informative:
        population = int(record["eligible_current_edges"])
        carried = int(record["carried_edges"])
        future_current = int(record["future_current_edges"])
        expected, variance = _hypergeometric_moments(
            population, future_current, carried
        )
        expected_sum += expected
        variance_sum += variance
        a = int(record["carried_continued"])
        b = carried - a
        c = int(record["new_continued"])
        d = int(record["new_edges"]) - c
        odds_numerator += a * d / max(1, population)
        odds_denominator += b * c / max(1, population)
    z_score = (
        (carried_continued - expected_sum) / math.sqrt(variance_sum)
        if variance_sum > 0.0
        else 0.0
    )
    carried_rate = carried_continued / max(1, carried_continued + carried_stopped)
    new_rate = new_continued / max(1, new_continued + new_stopped)
    return {
        "strata": len(informative),
        "minimum_age": min(
            (int(record["relation_age"]) for record in informative), default=0
        ),
        "maximum_age": max(
            (int(record["relation_age"]) for record in informative), default=0
        ),
        "carried_eligible": carried_continued + carried_stopped,
        "carried_continued": carried_continued,
        "carried_continuation_rate": carried_rate,
        "new_eligible": new_continued + new_stopped,
        "new_continued": new_continued,
        "new_continuation_rate": new_rate,
        "continuation_rate_difference": carried_rate - new_rate,
        "continuation_rate_ratio": carried_rate / max(1e-12, new_rate),
        "mantel_haenszel_common_odds_ratio": odds_numerator
        / max(1e-12, odds_denominator),
        "stratified_null_expected_carried_continuations": expected_sum,
        "stratified_null_sd": math.sqrt(variance_sum),
        "stratified_z_score": z_score,
        "stratified_one_sided_p": 0.5 * math.erfc(z_score / math.sqrt(2.0)),
    }


def _sensitivity_rows(records: list[dict[str, object]]) -> list[dict[str, object]]:
    groups = (
        ("all_informative", lambda age: age >= 3),
        ("without_age_3", lambda age: age >= 4),
        ("from_age_5", lambda age: age >= 5),
        ("from_age_10", lambda age: age >= 10),
        ("age_3_4", lambda age: 3 <= age <= 4),
        ("age_5_9", lambda age: 5 <= age <= 9),
        ("age_10_20", lambda age: 10 <= age <= 20),
        ("age_21_40", lambda age: 21 <= age <= 40),
    )
    return [
        {
            "scope": name,
            **_mantel_haenszel_stats(
                [record for record in records if predicate(int(record["relation_age"]))]
            ),
        }
        for name, predicate in groups
    ]


def _sample_hypergeometric(
    population: int, successes: int, draws: int, rng: random.Random
) -> int:
    if draws <= population - draws:
        return sum(index < successes for index in rng.sample(range(population), draws))
    excluded = population - draws
    excluded_successes = sum(
        index < successes for index in rng.sample(range(population), excluded)
    )
    return successes - excluded_successes


def _label_null(
    records: list[dict[str, object]],
    permutations: int = LABEL_PERMUTATIONS,
    seed: int = SEED,
) -> dict[str, object]:
    informative = [record for record in records if int(record["informative"]) == 1]
    observed = sum(int(record["carried_continued"]) for record in informative)
    rng = random.Random(seed)
    values = []
    for _ in range(permutations):
        values.append(
            sum(
                _sample_hypergeometric(
                    int(record["eligible_current_edges"]),
                    int(record["future_current_edges"]),
                    int(record["carried_edges"]),
                    rng,
                )
                for record in informative
            )
        )
    return {
        "control": "age_stratified_edge_label",
        "observed_statistic": observed,
        "null_mean": statistics.mean(values),
        "null_sd": statistics.pstdev(values),
        "null_max": max(values),
        "empirical_p_ge_observed": (
            1 + sum(value >= observed for value in values)
        )
        / (permutations + 1),
        "permutations": permutations,
        "seed": seed,
    }


def _permuted_edges(
    edges: set[tuple[str, str]], members: list[str], rng: random.Random
) -> set[tuple[str, str]]:
    shuffled = members[:]
    rng.shuffle(shuffled)
    mapping = dict(zip(members, shuffled))
    return {
        tuple(sorted((mapping[left], mapping[right]))) for left, right in edges
    }


def _graph_identity_null(
    records: list[dict[str, object]],
    permutations: int = GRAPH_PERMUTATIONS,
    seed: int = SEED + 1,
) -> dict[str, object]:
    informative = [record for record in records if int(record["informative"]) == 1]
    carried_denominator = sum(int(record["carried_edges"]) for record in informative)
    new_denominator = sum(int(record["new_edges"]) for record in informative)
    observed_carried = sum(
        int(record["carried_continued"]) for record in informative
    )
    observed_new = sum(int(record["new_continued"]) for record in informative)
    observed_difference = observed_carried / max(
        1, carried_denominator
    ) - observed_new / max(1, new_denominator)
    rng = random.Random(seed)
    differences = []
    carried_hits = []
    new_hits = []
    for _ in range(permutations):
        permuted_carried = 0
        permuted_new = 0
        for record in informative:
            future = set(record["_future_set"])
            members = list(record["_eligible_node_symbols"])
            permuted_future = _permuted_edges(future, members, rng)
            permuted_carried += len(set(record["_carried_set"]) & permuted_future)
            permuted_new += len(set(record["_new_set"]) & permuted_future)
        carried_hits.append(permuted_carried)
        new_hits.append(permuted_new)
        differences.append(
            permuted_carried / max(1, carried_denominator)
            - permuted_new / max(1, new_denominator)
        )
    return {
        "control": "future_graph_relation_identity",
        "observed_statistic": observed_difference,
        "null_mean": statistics.mean(differences),
        "null_sd": statistics.pstdev(differences),
        "null_max": max(differences),
        "empirical_p_ge_observed": (
            1 + sum(value >= observed_difference for value in differences)
        )
        / (permutations + 1),
        "null_mean_carried_hits": statistics.mean(carried_hits),
        "null_max_carried_hits": max(carried_hits),
        "null_mean_new_hits": statistics.mean(new_hits),
        "null_max_new_hits": max(new_hits),
        "permutations": permutations,
        "seed": seed,
    }


def _longest_consecutive_run(ages: set[int]) -> int:
    if not ages:
        return 0
    best = 1
    current = 1
    ordered = sorted(ages)
    for left, right in zip(ordered, ordered[1:]):
        if right == left + 1:
            current += 1
            best = max(best, current)
        else:
            current = 1
    return best


def _run_rows(edges: dict[int, set[tuple[str, str]]]) -> tuple[list[dict[str, object]], dict[str, int]]:
    histories: dict[tuple[str, str], set[int]] = defaultdict(set)
    for age, age_edges in edges.items():
        for edge in age_edges:
            histories[edge].add(age)
    distribution = Counter(
        _longest_consecutive_run(ages) for ages in histories.values()
    )
    recurring = {edge: ages for edge, ages in histories.items() if len(ages) >= 2}
    consecutive = sum(_longest_consecutive_run(ages) >= 2 for ages in recurring.values())
    return (
        [
            {"longest_consecutive_age_run": length, "edges": count}
            for length, count in sorted(distribution.items())
        ],
        {
            "unique_edges": len(histories),
            "recurring_edges": len(recurring),
            "recurring_with_consecutive_age": consecutive,
            "recurring_with_gaps_only": len(recurring) - consecutive,
            "maximum_consecutive_age_run": max(distribution, default=0),
        },
    )


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    fieldnames = []
    seen = set()
    for row in rows:
        for field in row:
            if field not in seen:
                seen.add(field)
                fieldnames.append(field)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    edges = _edge_sets()
    maximum_ages = _maximum_relation_ages()
    records = _transition_records(edges, maximum_ages)
    primary = _mantel_haenszel_stats(records)
    label_null = _label_null(records)
    graph_null = _graph_identity_null(records)
    run_rows, run_summary = _run_rows(edges)
    summary_rows = [
        {
            **run_summary,
            **primary,
            "label_null_empirical_p": label_null["empirical_p_ge_observed"],
            "graph_identity_null_mean_rate_difference": graph_null["null_mean"],
            "graph_identity_null_max_rate_difference": graph_null["null_max"],
            "graph_identity_empirical_p": graph_null["empirical_p_ge_observed"],
            "read_by_mini_dio": 0,
            "influences_field": 0,
            "influences_action": 0,
        }
    ]
    _write_csv("transitions", _public_transition_rows(records))
    _write_csv("sensitivity", _sensitivity_rows(records))
    _write_csv("null", [label_null, graph_null])
    _write_csv("runs", run_rows)
    _write_csv("summary", summary_rows)
    print(f"transition_ages={len(records)}")
    print(f"informative_strata={primary['strata']}")
    print(f"rate_ratio={primary['continuation_rate_ratio']}")
    print(f"graph_identity_p={graph_null['empirical_p_ge_observed']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
