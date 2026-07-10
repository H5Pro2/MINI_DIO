from __future__ import annotations

import csv
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_mcm_relation_event_transition_topology import _event_sequences
from tools.run_mcm_relation_gap_prequential_expectation import _percentile_score
from tools.run_mcm_relation_synchrony_topology import (
    BASIS_EVENT_ARCHIVE,
    BASIS_LIFECYCLE_ARCHIVE,
    HOLDOUT_ARCHIVE,
    _archive_rows,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2099_MCM_KOLLEKTIVE_GAP_KADENZ_TRANSFER"
LABEL_PERMUTATIONS = 1000
SEED = 2099


def _gap_counts(sequences: dict[str, list[int]]) -> Counter:
    return Counter(
        right - left
        for sequence in sequences.values()
        for left, right in zip(sequence, sequence[1:])
    )


def _target_source_map(order_rows: list[dict[str, str]]) -> dict[int, str]:
    return {
        int(row["position"]): f"{row['asset']}_{row['year']}"
        for row in order_rows
    }


def _transfer_rows(
    source_sequences: dict[str, list[int]],
    target_sequences: dict[str, list[int]],
    target_order_rows: list[dict[str, str]],
) -> tuple[list[dict[str, object]], int]:
    worlds = len(target_order_rows)
    candidates = set(range(1, worlds))
    source_counts = _gap_counts(source_sequences)
    target_full_counts = _gap_counts(target_sequences)
    source_map = _target_source_map(target_order_rows)
    gap_records = sorted(
        (right, symbol, right - left)
        for symbol, sequence in target_sequences.items()
        for left, right in zip(sequence, sequence[1:])
    )
    predictions = sorted(
        (left, right, symbol, right - left)
        for symbol, sequence in target_sequences.items()
        for left, right in zip(sequence, sequence[1:])
    )
    online_counts: Counter = Counter()
    gap_index = 0
    future_target_reads = 0
    rows = []
    for origin, target_end, symbol, actual_gap in predictions:
        while (
            gap_index < len(gap_records)
            and gap_records[gap_index][0] <= origin
        ):
            end, _, gap = gap_records[gap_index]
            future_target_reads += int(end > origin)
            online_counts[gap] += 1
            gap_index += 1
        frozen_score = _percentile_score(
            source_counts, actual_gap, candidates
        )
        online_score = _percentile_score(
            online_counts, actual_gap, candidates
        )
        target_full_score = _percentile_score(
            target_full_counts, actual_gap, candidates
        )
        rows.append(
            {
                "prediction_origin": origin,
                "target_event_finalization": target_end,
                "target_source": source_map[target_end],
                "target_relation": symbol,
                "actual_gap": actual_gap,
                "phase": "first_half" if origin <= worlds // 2 else "second_half",
                "frozen_source_score": frozen_score,
                "target_online_score": online_score,
                "target_full_score_diagnostic": target_full_score,
                "frozen_minus_online": frozen_score - online_score,
                "frozen_minus_target_full": frozen_score - target_full_score,
                "maximum_target_training_finalization": origin,
            }
        )
    return rows, future_target_reads


def _summary(rows: list[dict[str, object]]) -> dict[str, object]:
    frozen = [float(row["frozen_source_score"]) for row in rows]
    online = [float(row["target_online_score"]) for row in rows]
    target_full = [float(row["target_full_score_diagnostic"]) for row in rows]
    versus_online = [left - right for left, right in zip(frozen, online)]
    versus_full = [left - right for left, right in zip(frozen, target_full)]
    return {
        "predictions": len(rows),
        "frozen_source_mean_score": statistics.mean(frozen),
        "target_online_mean_score": statistics.mean(online),
        "target_full_mean_score_diagnostic": statistics.mean(target_full),
        "frozen_minus_online_mean": statistics.mean(versus_online),
        "frozen_minus_target_full_mean": statistics.mean(versus_full),
        "frozen_better_than_online": sum(value > 0.0 for value in versus_online),
        "frozen_equal_to_online": sum(value == 0.0 for value in versus_online),
        "frozen_worse_than_online": sum(value < 0.0 for value in versus_online),
        "frozen_online_nontie_win_share": sum(
            value > 0.0 for value in versus_online
        )
        / max(1, sum(value != 0.0 for value in versus_online)),
    }


def _group_rows(
    transfer: str,
    rows: list[dict[str, object]],
    field: str,
    output_field: str,
) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row[field])].append(row)
    return [
        {"transfer": transfer, output_field: value, **_summary(group)}
        for value, group in sorted(grouped.items())
    ]


def _permuted_counts(
    source_counts: Counter,
    candidate_values: set[int],
    rng: random.Random,
) -> Counter:
    labels = sorted(candidate_values)
    values = [source_counts[label] for label in labels]
    rng.shuffle(values)
    return Counter(dict(zip(labels, values)))


def _label_null_rows(
    rows: list[dict[str, object]],
    source_counts: Counter,
    worlds: int,
    seed: int,
) -> list[dict[str, object]]:
    candidates = set(range(1, worlds))
    scopes = {
        "all": rows,
        "first_half": [row for row in rows if row["phase"] == "first_half"],
        "second_half": [row for row in rows if row["phase"] == "second_half"],
    }
    observed = {
        scope: statistics.mean(
            float(row["frozen_minus_online"]) for row in selected
        )
        for scope, selected in scopes.items()
    }
    rng = random.Random(seed)
    values = {scope: [] for scope in scopes}
    for _ in range(LABEL_PERMUTATIONS):
        permuted = _permuted_counts(source_counts, candidates, rng)
        score_by_gap = {
            gap: _percentile_score(permuted, gap, candidates)
            for gap in candidates
        }
        for scope, selected in scopes.items():
            values[scope].append(
                statistics.mean(
                    score_by_gap[int(row["actual_gap"])]
                    - float(row["target_online_score"])
                    for row in selected
                )
            )
    return [
        {
            "control": "frozen_gap_label_identity",
            "scope": scope,
            "direction": "higher",
            "observed_frozen_minus_online": observed[scope],
            "null_mean": statistics.mean(null_values),
            "null_sd": statistics.pstdev(null_values),
            "null_min": min(null_values),
            "null_max": max(null_values),
            "empirical_p_ge_observed": (
                1 + sum(value >= observed[scope] for value in null_values)
            )
            / (LABEL_PERMUTATIONS + 1),
            "permutations": LABEL_PERMUTATIONS,
            "seed": seed,
        }
        for scope, null_values in values.items()
    ]


def _analyze(
    transfer: str,
    source_event_archive: Path,
    target_event_archive: Path,
    target_order_archive: Path,
    seed: int,
) -> dict[str, object]:
    source_sequences = _event_sequences(
        _archive_rows(source_event_archive, "event_histories.csv")
    )
    target_sequences = _event_sequences(
        _archive_rows(target_event_archive, "event_histories.csv")
    )
    order_rows = _archive_rows(target_order_archive, "holdout_order.csv")
    rows, future_reads = _transfer_rows(
        source_sequences, target_sequences, order_rows
    )
    source_counts = _gap_counts(source_sequences)
    phases = _group_rows(transfer, rows, "phase", "phase")
    groups = _group_rows(
        transfer, rows, "target_source", "target_source"
    )
    null_rows = _label_null_rows(rows, source_counts, len(order_rows), seed)
    summary = {
        "transfer": transfer,
        "source_relations": len(source_sequences),
        "source_gap_instances": sum(source_counts.values()),
        "target_relations": len(target_sequences),
        "target_worlds": len(order_rows),
        **_summary(rows),
        "first_half_frozen_minus_online": next(
            row["frozen_minus_online_mean"]
            for row in phases
            if row["phase"] == "first_half"
        ),
        "second_half_frozen_minus_online": next(
            row["frozen_minus_online_mean"]
            for row in phases
            if row["phase"] == "second_half"
        ),
        "positive_target_sources": sum(
            float(row["frozen_minus_online_mean"]) > 0.0 for row in groups
        ),
        "target_sources": len(groups),
        "future_target_reads": future_reads,
        "label_identity_p": next(
            row["empirical_p_ge_observed"]
            for row in null_rows
            if row["scope"] == "all"
        ),
        "read_by_mini_dio": 0,
        "influences_field": 0,
        "influences_action": 0,
    }
    return {
        "groups": groups,
        "phases": phases,
        "null": [{"transfer": transfer, **row} for row in null_rows],
        "summary": [summary],
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
            "2091_basis_to_2092_holdout",
            BASIS_EVENT_ARCHIVE,
            HOLDOUT_ARCHIVE,
            HOLDOUT_ARCHIVE,
            SEED,
        ),
        _analyze(
            "2092_holdout_to_2091_basis",
            HOLDOUT_ARCHIVE,
            BASIS_EVENT_ARCHIVE,
            BASIS_LIFECYCLE_ARCHIVE,
            SEED + 1,
        ),
    ]
    for name in ("groups", "phases", "null", "summary"):
        _write_csv(name, [row for result in analyses for row in result[name]])
    for result in analyses:
        summary = result["summary"][0]
        print(f"transfer={summary['transfer']}")
        print(f"predictions={summary['predictions']}")
        print(f"frozen_minus_online={summary['frozen_minus_online_mean']}")
        print(
            "second_half_frozen_minus_online="
            f"{summary['second_half_frozen_minus_online']}"
        )
        print(
            "positive_sources="
            f"{summary['positive_target_sources']}/"
            f"{summary['target_sources']}"
        )
        print(f"future_target_reads={summary['future_target_reads']}")
        print(f"label_identity_p={summary['label_identity_p']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
