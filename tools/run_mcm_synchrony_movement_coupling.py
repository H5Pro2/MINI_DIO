from __future__ import annotations

import csv
import math
import random
import statistics
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_relation_lifecycle_eigenstability import (
    _hypergeometric_moments,
    _sample_hypergeometric,
)
from tools.run_mcm_relation_synchrony_topology import (
    BASIS_EVENT_ARCHIVE,
    BASIS_LIFECYCLE_ARCHIVE,
    HOLDOUT_ARCHIVE,
    _archive_rows,
    _event_finalizations,
    _lifecycle_edges,
    _synchrony_graphs,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2095_MCM_SYNCHRONISATION_BEWEGUNGSKOPPLUNG"
LABEL_PERMUTATIONS = 2000
GRAPH_PERMUTATIONS = 200
SEED = 2095


def _coupling_records(
    nodes: dict[int, set[str]],
    synchrony: dict[int, set[tuple[str, str]]],
    lifecycle: dict[int, set[tuple[str, str]]],
) -> list[dict[str, object]]:
    records = []
    for age in sorted(synchrony):
        common = nodes.get(age, set()) & nodes.get(age + 1, set())
        if len(common) < 2:
            continue
        current = {
            edge
            for edge in synchrony[age]
            if edge[0] in common and edge[1] in common
        }
        future = {
            edge
            for edge in synchrony.get(age + 1, set())
            if edge[0] in common and edge[1] in common
        }
        selected = current & lifecycle.get(age, set())
        unselected = current - selected
        if not selected or not unselected or not future:
            continue
        selected_retained = len(selected & future)
        unselected_retained = len(unselected & future)
        expected, variance = _hypergeometric_moments(
            len(current), len(current & future), len(selected)
        )
        records.append(
            {
                "relation_age": age,
                "common_relations": len(common),
                "synchrony_pairs": len(current),
                "movement_selected_pairs": len(selected),
                "movement_selected_retained": selected_retained,
                "movement_selected_retention_rate": selected_retained
                / len(selected),
                "not_selected_pairs": len(unselected),
                "not_selected_retained": unselected_retained,
                "not_selected_retention_rate": unselected_retained
                / len(unselected),
                "retention_rate_difference": selected_retained / len(selected)
                - unselected_retained / len(unselected),
                "retention_rate_ratio": (selected_retained / len(selected))
                / max(1e-12, unselected_retained / len(unselected)),
                "future_synchrony_pairs": len(future),
                "retained_current_pairs": len(current & future),
                "label_null_expected_selected_retained": expected,
                "label_null_sd": math.sqrt(variance),
                "informative": 1,
                "_members": sorted(common),
                "_current": current,
                "_future": future,
                "_selected": selected,
                "_unselected": unselected,
            }
        )
    return records


def _stats(records: list[dict[str, object]]) -> dict[str, object]:
    selected_retained = sum(
        int(row["movement_selected_retained"]) for row in records
    )
    selected_stopped = sum(
        int(row["movement_selected_pairs"])
        - int(row["movement_selected_retained"])
        for row in records
    )
    unselected_retained = sum(int(row["not_selected_retained"]) for row in records)
    unselected_stopped = sum(
        int(row["not_selected_pairs"]) - int(row["not_selected_retained"])
        for row in records
    )
    expected_sum = 0.0
    variance_sum = 0.0
    odds_numerator = 0.0
    odds_denominator = 0.0
    for row in records:
        population = int(row["synchrony_pairs"])
        selected = int(row["movement_selected_pairs"])
        retained = int(row["retained_current_pairs"])
        expected, variance = _hypergeometric_moments(
            population, retained, selected
        )
        expected_sum += expected
        variance_sum += variance
        a = int(row["movement_selected_retained"])
        b = selected - a
        c = int(row["not_selected_retained"])
        d = int(row["not_selected_pairs"]) - c
        odds_numerator += a * d / population
        odds_denominator += b * c / population
    selected_total = selected_retained + selected_stopped
    unselected_total = unselected_retained + unselected_stopped
    selected_rate = selected_retained / max(1, selected_total)
    unselected_rate = unselected_retained / max(1, unselected_total)
    z_score = (
        (selected_retained - expected_sum) / math.sqrt(variance_sum)
        if variance_sum > 0.0
        else 0.0
    )
    return {
        "strata": len(records),
        "minimum_age": min(
            (int(row["relation_age"]) for row in records), default=0
        ),
        "maximum_age": max(
            (int(row["relation_age"]) for row in records), default=0
        ),
        "movement_selected_pairs": selected_total,
        "movement_selected_retained": selected_retained,
        "movement_selected_retention_rate": selected_rate,
        "not_selected_pairs": unselected_total,
        "not_selected_retained": unselected_retained,
        "not_selected_retention_rate": unselected_rate,
        "retention_rate_difference": selected_rate - unselected_rate,
        "retention_rate_ratio": selected_rate / max(1e-12, unselected_rate),
        "mantel_haenszel_common_odds_ratio": odds_numerator
        / max(1e-12, odds_denominator),
        "label_null_expected_selected_retained": expected_sum,
        "label_null_sd": math.sqrt(variance_sum),
        "label_null_z_score": z_score,
        "label_null_analytic_one_sided_p": 0.5
        * math.erfc(z_score / math.sqrt(2.0)),
    }


def _sensitivity_rows(records: list[dict[str, object]]) -> list[dict[str, object]]:
    groups = (
        ("all", lambda age: age >= 2),
        ("without_age_2", lambda age: age >= 3),
        ("from_age_5", lambda age: age >= 5),
        ("age_2_4", lambda age: 2 <= age <= 4),
        ("age_5_10", lambda age: 5 <= age <= 10),
        ("age_11_plus", lambda age: age >= 11),
    )
    return [
        {
            "scope": name,
            **_stats(
                [row for row in records if predicate(int(row["relation_age"]))]
            ),
        }
        for name, predicate in groups
    ]


def _label_null(records: list[dict[str, object]], seed: int) -> dict[str, object]:
    observed = sum(int(row["movement_selected_retained"]) for row in records)
    rng = random.Random(seed)
    values = [
        sum(
            _sample_hypergeometric(
                int(row["synchrony_pairs"]),
                int(row["retained_current_pairs"]),
                int(row["movement_selected_pairs"]),
                rng,
            )
            for row in records
        )
        for _ in range(LABEL_PERMUTATIONS)
    ]
    return {
        "control": "age_stratified_movement_selection_label",
        "observed_statistic": observed,
        "null_mean": statistics.mean(values),
        "null_sd": statistics.pstdev(values),
        "null_min": min(values),
        "null_max": max(values),
        "empirical_p_ge_observed": (
            1 + sum(value >= observed for value in values)
        )
        / (LABEL_PERMUTATIONS + 1),
        "permutations": LABEL_PERMUTATIONS,
        "seed": seed,
    }


def _graph_identity_null(
    records: list[dict[str, object]], seed: int
) -> dict[str, object]:
    selected_denominator = sum(
        int(row["movement_selected_pairs"]) for row in records
    )
    unselected_denominator = sum(int(row["not_selected_pairs"]) for row in records)
    observed = _stats(records)["retention_rate_difference"]
    rng = random.Random(seed)
    differences = []
    for _ in range(GRAPH_PERMUTATIONS):
        selected_hits = 0
        unselected_hits = 0
        for row in records:
            members = list(row["_members"])
            shuffled = members[:]
            rng.shuffle(shuffled)
            mapping = dict(zip(members, shuffled))
            current = set(row["_current"])
            selected = set(row["_selected"])
            for left, right in set(row["_future"]):
                edge = tuple(sorted((mapping[left], mapping[right])))
                if edge in current:
                    if edge in selected:
                        selected_hits += 1
                    else:
                        unselected_hits += 1
        differences.append(
            selected_hits / selected_denominator
            - unselected_hits / unselected_denominator
        )
    return {
        "control": "next_age_synchrony_graph_relation_identity",
        "observed_statistic": observed,
        "null_mean": statistics.mean(differences),
        "null_sd": statistics.pstdev(differences),
        "null_min": min(differences),
        "null_max": max(differences),
        "empirical_p_ge_observed": (
            1 + sum(value >= observed for value in differences)
        )
        / (GRAPH_PERMUTATIONS + 1),
        "permutations": GRAPH_PERMUTATIONS,
        "seed": seed,
    }


def _analyze(
    dataset: str,
    event_archive: Path,
    lifecycle_archive: Path,
    seed: int,
) -> dict[str, object]:
    events = _archive_rows(event_archive, "event_histories.csv")
    worlds = len(_archive_rows(lifecycle_archive, "holdout_order.csv"))
    lifecycle = _lifecycle_edges(
        _archive_rows(lifecycle_archive, "lifecycle_observations.csv")
    )
    nodes, synchrony = _synchrony_graphs(_event_finalizations(events), worlds)
    records = _coupling_records(nodes, synchrony, lifecycle)
    summary = {
        "dataset": dataset,
        "worlds": worlds,
        **_stats(records),
        "label_null_empirical_p": 0.0,
        "graph_identity_null_empirical_p": 0.0,
        "read_by_mini_dio": 0,
        "influences_field": 0,
        "influences_action": 0,
    }
    label_null = _label_null(records, seed)
    graph_null = _graph_identity_null(records, seed + 1)
    summary["label_null_empirical_p"] = label_null["empirical_p_ge_observed"]
    summary["graph_identity_null_empirical_p"] = graph_null[
        "empirical_p_ge_observed"
    ]
    return {
        "summary": summary,
        "ages": [
            {
                "dataset": dataset,
                **{
                    key: value
                    for key, value in row.items()
                    if not key.startswith("_")
                },
            }
            for row in records
        ],
        "sensitivity": [
            {"dataset": dataset, **row} for row in _sensitivity_rows(records)
        ],
        "null": [
            {"dataset": dataset, **label_null},
            {"dataset": dataset, **graph_null},
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
    for name in ("ages", "sensitivity", "null"):
        _write_csv(name, [row for result in analyses for row in result[name]])
    _write_csv("summary", [result["summary"] for result in analyses])
    for result in analyses:
        summary = result["summary"]
        print(f"dataset={summary['dataset']}")
        print(f"retention_rate_difference={summary['retention_rate_difference']}")
        print(f"retention_rate_ratio={summary['retention_rate_ratio']}")
        print(f"label_p={summary['label_null_empirical_p']}")
        print(f"graph_p={summary['graph_identity_null_empirical_p']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
