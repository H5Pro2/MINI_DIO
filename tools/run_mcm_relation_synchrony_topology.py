from __future__ import annotations

import csv
import heapq
import io
import random
import statistics
import sys
import zipfile
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2094_MCM_RELATIONSSYNCHRONISATION_TOPOLOGIE"
BASIS_EVENT_ARCHIVE = ROOT / "data" / "2089_mcm_breadth_data_holdout_events.zip"
BASIS_LIFECYCLE_ARCHIVE = ROOT / "data" / "2090_mcm_relation_lifecycle_events.zip"
HOLDOUT_ARCHIVE = ROOT / "data" / "2092_mcm_lifecycle_holdout_events.zip"
RHYTHM_PERMUTATIONS = 500
IDENTITY_PERMUTATIONS = 200
SEED = 2094


def _archive_rows(path: Path, name: str) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        with archive.open(name) as raw:
            return list(csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8")))


def _event_finalizations(rows: list[dict[str, str]]) -> dict[str, list[int]]:
    grouped: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for row in rows:
        grouped[row["neighborhood_symbol"]].append(
            (int(row["event_index"]), int(row["finalization_index"]))
        )
    return {
        symbol: [finalization for _, finalization in sorted(events)]
        for symbol, events in grouped.items()
    }


def _intervals_by_age(
    finalizations: dict[str, list[int]], worlds: int
) -> dict[int, list[tuple[str, int, int]]]:
    result: dict[int, list[tuple[str, int, int]]] = defaultdict(list)
    for symbol, sequence in finalizations.items():
        for offset, start in enumerate(sequence[1:], start=1):
            age = offset + 1
            end = sequence[offset + 1] if offset + 1 < len(sequence) else worlds + 1
            result[age].append((symbol, start, end))
    return dict(result)


def _overlap_edges(
    intervals: list[tuple[str, int, int]],
) -> set[tuple[str, str]]:
    ordered = sorted(intervals, key=lambda row: (row[1], row[0]))
    edges = set()
    for index, (left, _, left_end) in enumerate(ordered):
        for right, right_start, _ in ordered[index + 1 :]:
            if right_start >= left_end:
                break
            edges.add(tuple(sorted((left, right))))
    return edges


def _synchrony_graphs(
    finalizations: dict[str, list[int]], worlds: int
) -> tuple[dict[int, set[str]], dict[int, set[tuple[str, str]]]]:
    intervals = _intervals_by_age(finalizations, worlds)
    nodes = {
        age: {symbol for symbol, _, _ in rows} for age, rows in intervals.items()
    }
    edges = {age: _overlap_edges(rows) for age, rows in intervals.items()}
    return nodes, edges


def _lifecycle_edges(
    rows: list[dict[str, str]],
) -> dict[int, set[tuple[str, str]]]:
    result: dict[int, set[tuple[str, str]]] = defaultdict(set)
    for row in rows:
        edge = tuple(sorted((row["left_relation"], row["right_relation"])))
        result[int(row["relation_age"])].add(edge)
    return dict(result)


def _age_rows(
    nodes: dict[int, set[str]],
    synchrony: dict[int, set[tuple[str, str]]],
    lifecycle: dict[int, set[tuple[str, str]]],
) -> list[dict[str, object]]:
    rows = []
    for age in sorted(synchrony):
        sync_edges = synchrony[age]
        lifecycle_edges = lifecycle.get(age, set())
        unexpected = lifecycle_edges - sync_edges
        if unexpected:
            raise RuntimeError(
                f"age {age} has {len(unexpected)} lifecycle edges without synchrony"
            )
        rows.append(
            {
                "relation_age": age,
                "relations": len(nodes[age]),
                "synchrony_pairs": len(sync_edges),
                "lifecycle_pairs": len(lifecycle_edges),
                "lifecycle_share_of_synchrony": len(lifecycle_edges)
                / max(1, len(sync_edges)),
            }
        )
    return rows


def _transition_records(
    nodes: dict[int, set[str]],
    edges: dict[int, set[tuple[str, str]]],
) -> list[dict[str, object]]:
    records = []
    for age in sorted(edges):
        common = nodes.get(age, set()) & nodes.get(age + 1, set())
        if len(common) < 2:
            continue
        current = {
            edge for edge in edges[age] if edge[0] in common and edge[1] in common
        }
        future = {
            edge
            for edge in edges.get(age + 1, set())
            if edge[0] in common and edge[1] in common
        }
        if not current or not future:
            continue
        retained = len(current & future)
        possible = len(common) * (len(common) - 1) / 2
        expected = len(current) * len(future) / possible
        records.append(
            {
                "relation_age": age,
                "common_relations": len(common),
                "current_pairs": len(current),
                "future_pairs": len(future),
                "retained_pair_identities": retained,
                "retention_rate": retained / len(current),
                "turnover_rate": 1.0 - retained / len(current),
                "jaccard": retained / (len(current) + len(future) - retained),
                "identity_null_analytic_expected": expected,
                "observed_to_expected_ratio": retained / max(1e-12, expected),
                "_members": sorted(common),
                "_current": current,
                "_future": future,
            }
        )
    return records


def _public_records(records: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        {key: value for key, value in record.items() if not key.startswith("_")}
        for record in records
    ]


def _count_synchrony_pairs(
    finalizations: dict[str, list[int]], worlds: int
) -> int:
    total = 0
    for intervals in _intervals_by_age(finalizations, worlds).values():
        active_ends: list[int] = []
        for _, start, end in sorted(intervals, key=lambda row: (row[1], row[0])):
            while active_ends and active_ends[0] <= start:
                heapq.heappop(active_ends)
            total += len(active_ends)
            heapq.heappush(active_ends, end)
    return total


def _shuffled_gaps(
    finalizations: dict[str, list[int]], rng: random.Random
) -> dict[str, list[int]]:
    result = {}
    for symbol, sequence in finalizations.items():
        gaps = [right - left for left, right in zip(sequence, sequence[1:])]
        rng.shuffle(gaps)
        shuffled = [sequence[0]]
        for gap in gaps:
            shuffled.append(shuffled[-1] + gap)
        result[symbol] = shuffled
    return result


def _rhythm_null(
    finalizations: dict[str, list[int]], worlds: int, seed: int
) -> dict[str, object]:
    observed = _count_synchrony_pairs(finalizations, worlds)
    rng = random.Random(seed)
    values = [
        _count_synchrony_pairs(_shuffled_gaps(finalizations, rng), worlds)
        for _ in range(RHYTHM_PERMUTATIONS)
    ]
    return {
        "control": "relation_internal_gap_order",
        "observed_statistic": observed,
        "null_mean": statistics.mean(values),
        "null_sd": statistics.pstdev(values),
        "null_min": min(values),
        "null_max": max(values),
        "empirical_p_ge_observed": (
            1 + sum(value >= observed for value in values)
        )
        / (RHYTHM_PERMUTATIONS + 1),
        "permutations": RHYTHM_PERMUTATIONS,
        "seed": seed,
    }


def _identity_null(
    records: list[dict[str, object]], seed: int
) -> dict[str, object]:
    observed = sum(int(record["retained_pair_identities"]) for record in records)
    rng = random.Random(seed)
    values = []
    for _ in range(IDENTITY_PERMUTATIONS):
        retained = 0
        for record in records:
            members = list(record["_members"])
            shuffled = members[:]
            rng.shuffle(shuffled)
            mapping = dict(zip(members, shuffled))
            current = set(record["_current"])
            retained += sum(
                tuple(sorted((mapping[left], mapping[right]))) in current
                for left, right in set(record["_future"])
            )
        values.append(retained)
    return {
        "control": "next_age_graph_relation_identity",
        "observed_statistic": observed,
        "null_mean": statistics.mean(values),
        "null_sd": statistics.pstdev(values),
        "null_min": min(values),
        "null_max": max(values),
        "empirical_p_ge_observed": (
            1 + sum(value >= observed for value in values)
        )
        / (IDENTITY_PERMUTATIONS + 1),
        "permutations": IDENTITY_PERMUTATIONS,
        "seed": seed,
    }


def _analyze(
    dataset: str,
    event_archive: Path,
    lifecycle_archive: Path,
    seed: int,
) -> dict[str, object]:
    event_rows = _archive_rows(event_archive, "event_histories.csv")
    order_rows = _archive_rows(lifecycle_archive, "holdout_order.csv")
    lifecycle_rows = _archive_rows(lifecycle_archive, "lifecycle_observations.csv")
    finalizations = _event_finalizations(event_rows)
    nodes, synchrony = _synchrony_graphs(finalizations, len(order_rows))
    lifecycle = _lifecycle_edges(lifecycle_rows)
    age_rows = _age_rows(nodes, synchrony, lifecycle)
    transitions = _transition_records(nodes, synchrony)
    rhythm_null = _rhythm_null(finalizations, len(order_rows), seed)
    identity_null = _identity_null(transitions, seed + 1)
    current_pairs = sum(int(row["current_pairs"]) for row in transitions)
    retained = sum(int(row["retained_pair_identities"]) for row in transitions)
    future_pairs = sum(int(row["future_pairs"]) for row in transitions)
    analytic_expected = sum(
        float(row["identity_null_analytic_expected"]) for row in transitions
    )
    sync_pairs = sum(len(edges) for edges in synchrony.values())
    lifecycle_pairs = sum(len(edges) for edges in lifecycle.values())
    summary = {
        "dataset": dataset,
        "worlds": len(order_rows),
        "relations": len(finalizations),
        "age_layers": len(synchrony),
        "synchrony_pair_ages": sync_pairs,
        "lifecycle_pair_ages": lifecycle_pairs,
        "lifecycle_share_of_synchrony": lifecycle_pairs / sync_pairs,
        "lifecycle_without_synchrony": 0,
        "transitions": len(transitions),
        "transition_current_pairs": current_pairs,
        "transition_future_pairs": future_pairs,
        "retained_pair_identities": retained,
        "retention_rate": retained / current_pairs,
        "turnover_rate": 1.0 - retained / current_pairs,
        "identity_null_analytic_expected": analytic_expected,
        "identity_observed_to_expected_ratio": retained / analytic_expected,
        "rhythm_null_empirical_p": rhythm_null["empirical_p_ge_observed"],
        "identity_null_empirical_p": identity_null["empirical_p_ge_observed"],
        "read_by_mini_dio": 0,
        "influences_field": 0,
        "influences_action": 0,
    }
    return {
        "summary": summary,
        "ages": [{"dataset": dataset, **row} for row in age_rows],
        "transitions": [
            {"dataset": dataset, **row} for row in _public_records(transitions)
        ],
        "null": [
            {"dataset": dataset, **rhythm_null},
            {"dataset": dataset, **identity_null},
        ],
    }


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    fieldnames = []
    for row in rows:
        for field in row:
            if field not in fieldnames:
                fieldnames.append(field)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    analyses = [
        _analyze(
            "2091_basis",
            BASIS_EVENT_ARCHIVE,
            BASIS_LIFECYCLE_ARCHIVE,
            SEED,
        ),
        _analyze(
            "2092_holdout",
            HOLDOUT_ARCHIVE,
            HOLDOUT_ARCHIVE,
            SEED + 2,
        ),
    ]
    for name in ("ages", "transitions", "null"):
        _write_csv(name, [row for result in analyses for row in result[name]])
    _write_csv("summary", [result["summary"] for result in analyses])
    for result in analyses:
        summary = result["summary"]
        print(f"dataset={summary['dataset']}")
        print(f"synchrony_pair_ages={summary['synchrony_pair_ages']}")
        print(f"turnover_rate={summary['turnover_rate']}")
        print(
            "identity_observed_to_expected_ratio="
            f"{summary['identity_observed_to_expected_ratio']}"
        )
        print(f"rhythm_p={summary['rhythm_null_empirical_p']}")
        print(f"identity_p={summary['identity_null_empirical_p']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
