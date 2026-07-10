from __future__ import annotations

import csv
import io
import math
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

ARCHIVE = ROOT / "data" / "2092_mcm_lifecycle_holdout_events.zip"
BASIS_LIFECYCLE_ARCHIVE = ROOT / "data" / "2090_mcm_relation_lifecycle_events.zip"
BASIS_EVENT_ARCHIVE = ROOT / "data" / "2089_mcm_breadth_data_holdout_events.zip"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2093_MCM_RELATIONSLEBENSLAUF_EXAKTE_GELEGENHEIT_HERKUNFTSBALANCE"
PERMUTATIONS = 2000
SEED = 2093


from tools.run_mcm_relation_lifecycle_eigenstability import (
    _label_null,
    _mantel_haenszel_stats,
)


def _archive_rows(name: str, path: Path = ARCHIVE) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as archive:
        with archive.open(name) as raw:
            return list(csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8")))


def _event_finalizations(
    rows: list[dict[str, str]],
) -> dict[str, dict[int, int]]:
    result: dict[str, dict[int, int]] = defaultdict(dict)
    for row in rows:
        result[row["neighborhood_symbol"]][int(row["event_index"])] = int(
            row["finalization_index"]
        )
    return dict(result)


def _edge_sets(
    rows: list[dict[str, str]],
) -> dict[int, set[tuple[str, str]]]:
    result: dict[int, set[tuple[str, str]]] = defaultdict(set)
    for row in rows:
        edge = tuple(sorted((row["left_relation"], row["right_relation"])))
        result[int(row["relation_age"])].add(edge)
    return dict(result)


def _source_by_finalization(rows: list[dict[str, str]]) -> dict[int, str]:
    return {
        int(row["position"]): f"{row['asset']}_{row['year']}"
        for row in rows
    }


def _has_simultaneous_next_age(
    edge: tuple[str, str],
    age: int,
    opportunity_finalization: int,
    finalizations: dict[str, dict[int, int]],
) -> bool:
    return all(
        finalizations[symbol].get(age + 2, math.inf) > opportunity_finalization
        for symbol in edge
    )


def _opportunities(
    finalizations: dict[str, dict[int, int]],
    edges: dict[int, set[tuple[str, str]]],
    sources: dict[int, str],
) -> tuple[list[dict[str, object]], Counter]:
    exact = []
    counts: Counter = Counter()
    for age in range(3, max(edges, default=3)):
        prior = edges.get(age - 1, set())
        current = edges.get(age, set())
        future = edges.get(age + 1, set())
        for edge in sorted(current):
            if any(age + 1 not in finalizations.get(symbol, {}) for symbol in edge):
                continue
            label = "carried" if edge in prior else "new"
            counts[f"approximate_{label}"] += 1
            opportunity = max(
                finalizations[symbol][age + 1] for symbol in edge
            )
            simultaneous = _has_simultaneous_next_age(
                edge, age, opportunity, finalizations
            )
            if not simultaneous:
                if edge in future:
                    raise RuntimeError("continued edge lacks simultaneous opportunity")
                counts[f"excluded_non_simultaneous_{label}"] += 1
                continue
            if opportunity not in sources:
                raise RuntimeError(f"missing provenance for finalization {opportunity}")
            continued = int(edge in future)
            counts[f"exact_{label}"] += 1
            counts[f"exact_{label}_continued"] += continued
            exact.append(
                {
                    "relation_age": age,
                    "source": sources[opportunity],
                    "label": label,
                    "continued": continued,
                }
            )
    return exact, counts


def _records(
    opportunities: list[dict[str, object]], keys: tuple[str, ...]
) -> list[dict[str, object]]:
    grouped: dict[tuple[object, ...], Counter] = defaultdict(Counter)
    for row in opportunities:
        group = tuple(row[key] for key in keys)
        label = str(row["label"])
        grouped[group][label] += 1
        grouped[group][f"{label}_continued"] += int(row["continued"])
    records = []
    for group, counts in sorted(grouped.items()):
        carried = counts["carried"]
        new = counts["new"]
        carried_continued = counts["carried_continued"]
        new_continued = counts["new_continued"]
        record = {
            key: value for key, value in zip(keys, group)
        }
        record.update(
            {
                "eligible_current_edges": carried + new,
                "carried_edges": carried,
                "carried_continued": carried_continued,
                "carried_continuation_rate": carried_continued / max(1, carried),
                "new_edges": new,
                "new_continued": new_continued,
                "new_continuation_rate": new_continued / max(1, new),
                "continuation_rate_difference": carried_continued
                / max(1, carried)
                - new_continued / max(1, new),
                "future_current_edges": carried_continued + new_continued,
                "informative": int(bool(carried) and bool(new)),
            }
        )
        records.append(record)
    return records


def _descriptive(rows: list[dict[str, object]]) -> dict[str, object]:
    carried = sum(row["label"] == "carried" for row in rows)
    new = sum(row["label"] == "new" for row in rows)
    carried_continued = sum(
        int(row["continued"])
        for row in rows
        if row["label"] == "carried"
    )
    new_continued = sum(
        int(row["continued"]) for row in rows if row["label"] == "new"
    )
    carried_rate = carried_continued / max(1, carried)
    new_rate = new_continued / max(1, new)
    return {
        "carried_opportunities": carried,
        "carried_continued": carried_continued,
        "carried_continuation_rate": carried_rate,
        "new_opportunities": new,
        "new_continued": new_continued,
        "new_continuation_rate": new_rate,
        "continuation_rate_difference": carried_rate - new_rate,
        "continuation_rate_ratio": carried_rate / max(1e-12, new_rate),
    }


def _source_rows(
    opportunities: list[dict[str, object]],
    source_age_records: list[dict[str, object]],
) -> list[dict[str, object]]:
    result = []
    for source in sorted({str(row["source"]) for row in opportunities}):
        selected = [row for row in opportunities if row["source"] == source]
        strata = [row for row in source_age_records if row["source"] == source]
        result.append(
            {
                "source": source,
                **_descriptive(selected),
                "informative_age_strata": sum(
                    int(row["informative"]) for row in strata
                ),
                "age_stratified_one_sided_p": _mantel_haenszel_stats(strata)[
                    "stratified_one_sided_p"
                ],
            }
        )
    return result


def _leave_one_source_out_rows(
    opportunities: list[dict[str, object]],
) -> list[dict[str, object]]:
    sources = sorted({str(row["source"]) for row in opportunities})
    return [
        {
            "excluded_source": source,
            **_descriptive(
                [row for row in opportunities if row["source"] != source]
            ),
        }
        for source in sources
    ]


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


def _analyze(
    dataset: str,
    event_rows: list[dict[str, str]],
    lifecycle_rows: list[dict[str, str]],
    order_rows: list[dict[str, str]],
) -> dict[str, object]:
    opportunities, counts = _opportunities(
        _event_finalizations(event_rows),
        _edge_sets(lifecycle_rows),
        _source_by_finalization(order_rows),
    )
    age_records = _records(opportunities, ("relation_age",))
    source_age_records = _records(opportunities, ("source", "relation_age"))
    corrected = _descriptive(opportunities)
    age_stats = _mantel_haenszel_stats(age_records)
    source_age_stats = _mantel_haenszel_stats(source_age_records)
    label_null = _label_null(
        source_age_records,
        permutations=PERMUTATIONS,
        seed=SEED + int(dataset == "2092_holdout"),
    )
    sources = _source_rows(opportunities, source_age_records)
    leave_one_out = _leave_one_source_out_rows(opportunities)
    summary = {
        "dataset": dataset,
        "worlds": len(order_rows),
        "sources": len(sources),
        "approximate_carried_opportunities": counts["approximate_carried"],
        "approximate_new_opportunities": counts["approximate_new"],
        "excluded_non_simultaneous_carried": counts[
            "excluded_non_simultaneous_carried"
        ],
        "excluded_non_simultaneous_new": counts["excluded_non_simultaneous_new"],
        **corrected,
        "age_strata": age_stats["strata"],
        "age_stratified_common_odds_ratio": age_stats[
            "mantel_haenszel_common_odds_ratio"
        ],
        "age_stratified_one_sided_p": age_stats["stratified_one_sided_p"],
        "source_age_strata": source_age_stats["strata"],
        "source_age_common_odds_ratio": source_age_stats[
            "mantel_haenszel_common_odds_ratio"
        ],
        "source_age_one_sided_p": source_age_stats["stratified_one_sided_p"],
        "source_age_label_null_empirical_p": label_null[
            "empirical_p_ge_observed"
        ],
        "sources_with_positive_difference": sum(
            float(row["continuation_rate_difference"]) > 0.0 for row in sources
        ),
        "sources_with_negative_difference": sum(
            float(row["continuation_rate_difference"]) < 0.0 for row in sources
        ),
        "leave_one_out_positive": sum(
            float(row["continuation_rate_difference"]) > 0.0
            for row in leave_one_out
        ),
        "leave_one_out_negative": sum(
            float(row["continuation_rate_difference"]) < 0.0
            for row in leave_one_out
        ),
        "read_by_mini_dio": 0,
        "influences_field": 0,
        "influences_action": 0,
    }
    return {
        "summary": summary,
        "source_age": [
            {"dataset": dataset, **row} for row in source_age_records
        ],
        "sources": [{"dataset": dataset, **row} for row in sources],
        "leave_one_source_out": [
            {"dataset": dataset, **row} for row in leave_one_out
        ],
        "null": {"dataset": dataset, **label_null},
    }


def main() -> int:
    basis = _analyze(
        "2091_basis",
        _archive_rows("event_histories.csv", BASIS_EVENT_ARCHIVE),
        _archive_rows("lifecycle_observations.csv", BASIS_LIFECYCLE_ARCHIVE),
        _archive_rows("holdout_order.csv", BASIS_LIFECYCLE_ARCHIVE),
    )
    holdout = _analyze(
        "2092_holdout",
        _archive_rows("event_histories.csv"),
        _archive_rows("lifecycle_observations.csv"),
        _archive_rows("holdout_order.csv"),
    )
    analyses = [basis, holdout]
    for name in ("source_age", "sources", "leave_one_source_out"):
        _write_csv(name, [row for result in analyses for row in result[name]])
    _write_csv("null", [result["null"] for result in analyses])
    _write_csv("summary", [result["summary"] for result in analyses])
    for result in analyses:
        summary = result["summary"]
        print(f"dataset={summary['dataset']}")
        print(
            "exact_opportunities="
            f"{summary['carried_opportunities'] + summary['new_opportunities']}"
        )
        print(f"rate_difference={summary['continuation_rate_difference']}")
        print(
            "source_age_label_p="
            f"{summary['source_age_label_null_empirical_p']}"
        )
        print(
            "source_directions="
            f"{summary['sources_with_positive_difference']}/"
            f"{summary['sources_with_negative_difference']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
