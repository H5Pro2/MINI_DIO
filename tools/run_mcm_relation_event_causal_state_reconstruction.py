from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neighborhood_event_memory import EVENT_FIELDS
from tools.run_mcm_maturation_trajectory_neighborhoods import (
    _mutual_nearest_edges,
)
from tools.run_mcm_relation_age_trajectory_neighborhoods import (
    SCOPES,
    _prefix_vector,
    _rank_vectors,
)
from tools.run_mcm_relation_synchrony_topology import (
    BASIS_EVENT_ARCHIVE,
    BASIS_LIFECYCLE_ARCHIVE,
    HOLDOUT_ARCHIVE,
    _archive_rows,
    _event_finalizations,
    _synchrony_graphs,
)


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2096_MCM_RELATIONSEREIGNISZEIT_KAUSALE_ZUSTANDSREKONSTRUKTION"


def _actual_lifecycle_by_finalization(
    rows: list[dict[str, str]],
) -> dict[int, set[tuple[str, str, int, int]]]:
    result: dict[int, set[tuple[str, str, int, int]]] = defaultdict(set)
    for row in rows:
        finalization = int(row["finalization_index"])
        left, right = sorted((row["left_relation"], row["right_relation"]))
        result[finalization].add(
            (left, right, finalization, int(row["relation_age"]))
        )
    return dict(result)


def _event_token(symbol: str, event_index: int, event: dict[str, int]) -> bytes:
    payload = [symbol, event_index, *[event[field] for field in EVENT_FIELDS]]
    return (json.dumps(payload, separators=(",", ":")) + "\n").encode("utf-8")


def _causal_reconstruction(
    event_rows: list[dict[str, str]],
    lifecycle_rows: list[dict[str, str]],
    order_rows: list[dict[str, str]],
) -> dict[str, object]:
    worlds = len(order_rows)
    labels = {int(row["position"]): row["world_label"] for row in order_rows}
    events_by_finalization: dict[
        int, list[tuple[str, int, dict[str, int]]]
    ] = defaultdict(list)
    event_index_exact = 1
    archived_histories: dict[str, list[int]] = defaultdict(list)
    for row in event_rows:
        symbol = row["neighborhood_symbol"]
        event_index = int(row["event_index"])
        event = {field: int(row[field]) for field in EVENT_FIELDS}
        events_by_finalization[event["finalization_index"]].append(
            (symbol, event_index, event)
        )
        archived_histories[symbol].append(event_index)
    for indexes in archived_histories.values():
        if sorted(indexes) != list(range(1, len(indexes) + 1)):
            event_index_exact = 0

    actual_by_finalization = _actual_lifecycle_by_finalization(lifecycle_rows)
    histories: dict[str, list[dict[str, int]]] = defaultdict(list)
    causal_lifecycle: set[tuple[str, str, int, int]] = set()
    actual_cumulative: set[tuple[str, str, int, int]] = set()
    causal_synchrony: dict[int, set[tuple[str, str]]] = defaultdict(set)
    fingerprint = hashlib.sha256()
    previous_fingerprint = ""
    snapshots = []
    prefix_exact = 0
    future_event_reads = 0

    for finalization in range(1, worlds + 1):
        incoming = sorted(
            events_by_finalization.get(finalization, []),
            key=lambda item: (item[0], item[1]),
        )
        changed = set()
        for symbol, event_index, event in incoming:
            if event["finalization_index"] > finalization:
                future_event_reads += 1
            if event_index != len(histories[symbol]) + 1:
                event_index_exact = 0
            histories[symbol].append(event)
            changed.add(symbol)
            fingerprint.update(_event_token(symbol, event_index, event))

        expected_now: set[tuple[str, str, int, int]] = set()
        changed_ages = {
            len(histories[symbol])
            for symbol in changed
            if len(histories[symbol]) >= 2
        }
        for age in sorted(changed_ages):
            vectors = {
                symbol: _prefix_vector(history, age)
                for symbol, history in histories.items()
                if len(history) == age
            }
            if len(vectors) < 2:
                continue
            ranked = _rank_vectors(vectors, SCOPES["breadth_growth"])
            edges, _ = _mutual_nearest_edges({(age,): ranked})
            expected_now.update(
                (*tuple(sorted(edge)), finalization, age)
                for edge in edges
                if changed.intersection(edge)
            )
        actual_now = actual_by_finalization.get(finalization, set())
        causal_lifecycle.update(expected_now)
        actual_cumulative.update(actual_now)
        exact_now = int(expected_now == actual_now)
        exact_prefix = int(causal_lifecycle == actual_cumulative)
        prefix_exact += exact_prefix

        cohorts: dict[int, list[str]] = defaultdict(list)
        for symbol, history in histories.items():
            if len(history) >= 2:
                cohorts[len(history)].append(symbol)
        synchrony_pairs = 0
        for age, members in cohorts.items():
            pairs = set(combinations(sorted(members), 2))
            causal_synchrony[age].update(pairs)
            synchrony_pairs += len(pairs)

        state_fingerprint = fingerprint.copy().hexdigest()
        snapshots.append(
            {
                "finalization_index": finalization,
                "world_label": labels.get(finalization, ""),
                "new_relation_events": len(incoming),
                "changed_relations": len(changed),
                "active_relations": len(histories),
                "active_age_cohorts": len(cohorts),
                "maximum_current_relation_age": max(cohorts, default=0),
                "current_synchrony_pairs": synchrony_pairs,
                "new_lifecycle_observations": len(expected_now),
                "cumulative_lifecycle_observations": len(causal_lifecycle),
                "lifecycle_exact_at_finalization": exact_now,
                "lifecycle_prefix_exact": exact_prefix,
                "event_prefix_fingerprint": state_fingerprint,
                "event_state_changed": int(
                    state_fingerprint != previous_fingerprint
                ),
                "maximum_event_finalization_read": finalization,
                "future_event_reads": future_event_reads,
            }
        )
        previous_fingerprint = state_fingerprint

    full_finalizations = _event_finalizations(event_rows)
    _, offline_synchrony = _synchrony_graphs(full_finalizations, worlds)
    causal_sync_set = {
        (age, edge) for age, edges in causal_synchrony.items() for edge in edges
    }
    offline_sync_set = {
        (age, edge) for age, edges in offline_synchrony.items() for edge in edges
    }
    actual_all = {
        observation
        for observations in actual_by_finalization.values()
        for observation in observations
    }
    integrity = {
        "worlds": worlds,
        "event_rows": len(event_rows),
        "event_relations": len(archived_histories),
        "event_index_exact": event_index_exact,
        "future_event_reads": future_event_reads,
        "lifecycle_prefixes_exact": prefix_exact,
        "lifecycle_prefixes_total": worlds,
        "lifecycle_all_prefixes_exact": int(prefix_exact == worlds),
        "causal_lifecycle_observations": len(causal_lifecycle),
        "archived_lifecycle_observations": len(actual_all),
        "lifecycle_exact": int(causal_lifecycle == actual_all),
        "causal_synchrony_pair_ages": len(causal_sync_set),
        "offline_synchrony_pair_ages": len(offline_sync_set),
        "synchrony_exact": int(causal_sync_set == offline_sync_set),
        "unique_event_prefix_states": len(
            {row["event_prefix_fingerprint"] for row in snapshots}
        ),
        "unchanged_event_prefix_worlds": sum(
            int(row["event_state_changed"]) == 0 for row in snapshots
        ),
    }
    return {"snapshots": snapshots, "integrity": integrity}


def _analyze(
    dataset: str,
    event_archive: Path,
    lifecycle_archive: Path,
) -> dict[str, object]:
    event_rows = _archive_rows(event_archive, "event_histories.csv")
    lifecycle_rows = _archive_rows(lifecycle_archive, "lifecycle_observations.csv")
    order_rows = _archive_rows(lifecycle_archive, "holdout_order.csv")
    result = _causal_reconstruction(event_rows, lifecycle_rows, order_rows)
    integrity = {"dataset": dataset, **result["integrity"]}
    if not all(
        int(integrity[field]) == 1
        for field in (
            "event_index_exact",
            "lifecycle_all_prefixes_exact",
            "lifecycle_exact",
            "synchrony_exact",
        )
    ):
        raise RuntimeError(f"causal reconstruction failed for {dataset}")
    summary = {
        **integrity,
        "additional_state_memory_required": 0,
        "read_by_mini_dio": 0,
        "influences_field": 0,
        "influences_action": 0,
    }
    return {
        "snapshots": [
            {"dataset": dataset, **row} for row in result["snapshots"]
        ],
        "integrity": [integrity],
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
        _analyze("2091_basis", BASIS_EVENT_ARCHIVE, BASIS_LIFECYCLE_ARCHIVE),
        _analyze("2092_holdout", HOLDOUT_ARCHIVE, HOLDOUT_ARCHIVE),
    ]
    for name in ("snapshots", "integrity", "summary"):
        _write_csv(name, [row for result in analyses for row in result[name]])
    for result in analyses:
        summary = result["summary"][0]
        print(f"dataset={summary['dataset']}")
        print(
            "lifecycle_prefixes_exact="
            f"{summary['lifecycle_prefixes_exact']}/"
            f"{summary['lifecycle_prefixes_total']}"
        )
        print(f"synchrony_exact={summary['synchrony_exact']}")
        print(f"future_event_reads={summary['future_event_reads']}")
        print(
            "unique_event_prefix_states="
            f"{summary['unique_event_prefix_states']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
