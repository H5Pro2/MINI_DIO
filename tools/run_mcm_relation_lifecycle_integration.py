from __future__ import annotations

import csv
import io
import json
import shutil
import subprocess
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.semantic_memory import SemanticMemory
from tools.create_csv_slice import create_slice
from tools.run_mcm_breadth_data_holdout import (
    ROWS,
    _order_rows,
    _world_specs,
)
from tools.run_mcm_maturation_trajectory_neighborhoods import (
    _mutual_nearest_edges,
)
from tools.run_mcm_neighborhood_relation_event_time import (
    _csv_bytes,
    _event_integrity,
    _event_rows,
    _source_rows,
)
from tools.run_mcm_relation_age_trajectory_neighborhoods import (
    SCOPES,
    _prefix_vector,
    _rank_vectors,
)


GENERATED_DIR = ROOT / "data" / "generated" / "2090_mcm_relation_lifecycle"
DEBUG_ROOT = ROOT / "debug" / "2090_mcm_relation_lifecycle"
MEMORY_PATH = ROOT / "memory" / "topology_2090_relation_lifecycle.json"
BASELINE_ARCHIVE = ROOT / "data" / "2089_mcm_breadth_data_holdout_events.zip"
OUTPUT_ARCHIVE = ROOT / "data" / "2090_mcm_relation_lifecycle_events.zip"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2090_PASSIVE_MCM_RELATIONSNACHBARSCHAFT_LEBENSLAUF"


def _world_path(spec) -> Path:
    return GENERATED_DIR / (
        f"{spec.position:03d}_{spec.asset.lower()}_{spec.year}_30m_"
        f"start{spec.start}_rows{ROWS}.csv"
    )


def _clean_local_state() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    if DEBUG_ROOT.exists():
        shutil.rmtree(DEBUG_ROOT)
    if MEMORY_PATH.exists():
        MEMORY_PATH.unlink()


def _prepare_worlds(specs: list) -> None:
    for spec in specs:
        result = create_slice(
            spec.source,
            _world_path(spec),
            start=spec.start,
            rows=ROWS,
        )
        if int(result["rows_written"]) != ROWS:
            raise RuntimeError(
                f"{spec.source.name} start {spec.start} wrote "
                f"{result['rows_written']} instead of {ROWS} rows"
            )


def _run_worlds(specs: list) -> None:
    for position, spec in enumerate(specs, start=1):
        command = [
            sys.executable,
            "-m",
            "mini_dio.run_mini",
            "--data",
            str(_world_path(spec)),
            "--runs",
            "1",
            "--memory",
            str(MEMORY_PATH),
            "--debug-root",
            str(DEBUG_ROOT),
            "--world-label",
            spec.world_id,
            "--sense-mode",
            "world_relative",
        ]
        result = subprocess.run(
            command,
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr or f"replay failed at {spec.world_id}")
        if position % 8 == 0 or position == len(specs):
            print(f"replay_worlds_completed={position}/{len(specs)}", flush=True)


def _baseline_payload(name: str) -> bytes:
    with zipfile.ZipFile(BASELINE_ARCHIVE) as archive:
        return archive.read(name)


def _expected_observations(
    relations: dict[str, dict],
) -> set[tuple[str, str, int, int]]:
    maximum_finalization = max(
        (
            int(event["finalization_index"])
            for relation in relations.values()
            for event in relation["events"]
        ),
        default=0,
    )
    expected: set[tuple[str, str, int, int]] = set()
    for finalization in range(1, maximum_finalization + 1):
        current = {}
        changed = set()
        for symbol, relation in relations.items():
            if int(relation.get("unobserved_prior_events", 0) or 0) != 0:
                continue
            history = [
                event
                for event in relation["events"]
                if int(event["finalization_index"]) <= finalization
            ]
            if history:
                current[symbol] = history
            if history and int(history[-1]["finalization_index"]) == finalization:
                changed.add(symbol)
        changed_ages = {
            len(current[symbol])
            for symbol in changed
            if len(current[symbol]) >= 2
        }
        for age in sorted(changed_ages):
            vectors = {
                symbol: _prefix_vector(history, age)
                for symbol, history in current.items()
                if len(history) == age
            }
            if len(vectors) < 2:
                continue
            ranked = _rank_vectors(vectors, SCOPES["breadth_growth"])
            edges, _ = _mutual_nearest_edges({(age,): ranked})
            expected.update(
                (pair[0], pair[1], finalization, age)
                for pair in edges
                if changed.intersection(pair)
            )
    return expected


def _lifecycle_rows(edges: dict[str, dict]) -> list[dict[str, object]]:
    rows = []
    for edge in edges.values():
        for observation in edge["observations"]:
            rows.append(
                {
                    "edge_symbol": edge["edge_symbol"],
                    "left_relation": edge["left_relation"],
                    "right_relation": edge["right_relation"],
                    "observation_index": observation["observation_index"],
                    "finalization_index": observation["finalization_index"],
                    "relation_age": observation["relation_age"],
                }
            )
    rows.sort(
        key=lambda row: (
            int(row["finalization_index"]),
            str(row["left_relation"]),
            str(row["right_relation"]),
        )
    )
    return rows


def _actual_observations(
    rows: list[dict[str, object]],
) -> set[tuple[str, str, int, int]]:
    return {
        (
            str(row["left_relation"]),
            str(row["right_relation"]),
            int(row["finalization_index"]),
            int(row["relation_age"]),
        )
        for row in rows
    }


def _age_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_age: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_age[int(row["relation_age"])].append(row)
    return [
        {
            "relation_age": age,
            "observations": len(group),
            "edges": len({str(row["edge_symbol"]) for row in group}),
            "finalizations": len(
                {int(row["finalization_index"]) for row in group}
            ),
        }
        for age, group in sorted(by_age.items())
    ]


def _recurrence_rows(edges: dict[str, dict]) -> list[dict[str, object]]:
    distribution = Counter(
        int(edge["observation_count"]) for edge in edges.values()
    )
    return [
        {"observation_count": count, "edges": edges_at_count}
        for count, edges_at_count in sorted(distribution.items())
    ]


def _partner_rows(edges: dict[str, dict]) -> list[dict[str, object]]:
    partners: dict[str, set[str]] = defaultdict(set)
    for edge in edges.values():
        left = str(edge["left_relation"])
        right = str(edge["right_relation"])
        partners[left].add(right)
        partners[right].add(left)
    distribution = Counter(len(values) for values in partners.values())
    return [
        {"distinct_partners": count, "relations": relations}
        for count, relations in sorted(distribution.items())
    ]


def _write_archive(
    lifecycle_rows: list[dict[str, object]], order_rows: list[dict[str, object]]
) -> None:
    with zipfile.ZipFile(
        OUTPUT_ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name, payload in (
            ("lifecycle_observations.csv", _csv_bytes(lifecycle_rows)),
            ("holdout_order.csv", _csv_bytes(order_rows)),
        ):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(
                info,
                payload,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    specs = _world_specs()
    if len(specs) != 64:
        raise RuntimeError(f"expected 64 worlds, found {len(specs)}")
    order_rows = _order_rows(specs)
    order_exact = int(
        _csv_bytes(order_rows) == _baseline_payload("holdout_order.csv")
    )
    if order_exact != 1:
        raise RuntimeError("2090 order differs from 2089 baseline")

    _clean_local_state()
    try:
        _prepare_worlds(specs)
        _run_worlds(specs)
        memory = SemanticMemory(MEMORY_PATH)
        memory.load()
        source = _source_rows(memory)
        relations = memory.passive_mcm_neighborhood_event_relations()
        event_integrity = _event_integrity(source, relations)
        event_rows = _event_rows("holdout", relations)
        event_history_exact = int(
            _csv_bytes(event_rows) == _baseline_payload("event_histories.csv")
        )
        lifecycle_profile = memory.passive_mcm_relation_lifecycle_profile()
        lifecycle_edges = memory.passive_mcm_relation_lifecycle_edges()
        lifecycle_rows = _lifecycle_rows(lifecycle_edges)
        actual = _actual_observations(lifecycle_rows)
        expected = _expected_observations(relations)
        missing = expected - actual
        unexpected = actual - expected
        lifecycle_integrity_exact = int(not missing and not unexpected)
        if int(event_integrity["event_integrity_exact"]) != 1:
            raise RuntimeError("relation event integrity failed")
        if event_history_exact != 1:
            raise RuntimeError("2090 changed the 2089 relation event history")
        if lifecycle_integrity_exact != 1:
            raise RuntimeError("stored lifecycle differs from offline reconstruction")

        _write_archive(lifecycle_rows, order_rows)
        integrity_rows = [
            {
                "order_exact": order_exact,
                "event_integrity_exact": event_integrity["event_integrity_exact"],
                "event_history_exact": event_history_exact,
                "stored_lifecycle_observations": len(actual),
                "expected_lifecycle_observations": len(expected),
                "missing_lifecycle_observations": len(missing),
                "unexpected_lifecycle_observations": len(unexpected),
                "lifecycle_integrity_exact": lifecycle_integrity_exact,
            }
        ]
        summary_rows = [
            {
                "worlds": len(specs),
                "relations": len(source),
                "events": len(event_rows),
                "event_history_exact": event_history_exact,
                "lifecycle_relations": lifecycle_profile["relations"],
                "lifecycle_edges": lifecycle_profile["edges"],
                "lifecycle_observations": lifecycle_profile["observations"],
                "recurring_edges": lifecycle_profile["recurring_edges"],
                "edges_reappearing_at_later_age": lifecycle_profile[
                    "edges_reappearing_at_later_age"
                ],
                "relations_with_multiple_partners": lifecycle_profile[
                    "relations_with_multiple_partners"
                ],
                "maximum_relation_age": lifecycle_profile["maximum_relation_age"],
                "source_events_before_start": lifecycle_profile[
                    "source_events_before_start"
                ],
                "memory_size_bytes": MEMORY_PATH.stat().st_size,
                "lifecycle_document_bytes": len(
                    json.dumps(
                        memory.data["passive_mcm_relation_lifecycle_memory"],
                        indent=2,
                        sort_keys=True,
                    ).encode("utf-8")
                ),
                "archive_bytes": OUTPUT_ARCHIVE.stat().st_size,
                "read_by_mini_dio": lifecycle_profile["read_by_mini_dio"],
                "influences_field": lifecycle_profile["influences_field"],
                "influences_action": lifecycle_profile["influences_action"],
                "stores_components": lifecycle_profile["stores_components"],
                "uses_fixed_members": lifecycle_profile["uses_fixed_members"],
                "uses_distance_threshold": lifecycle_profile[
                    "uses_distance_threshold"
                ],
            }
        ]
        _write_csv("integrity", integrity_rows)
        _write_csv("ages", _age_rows(lifecycle_rows))
        _write_csv("recurrence", _recurrence_rows(lifecycle_edges))
        _write_csv("partners", _partner_rows(lifecycle_edges))
        _write_csv("summary", summary_rows)
        print(f"lifecycle_edges={lifecycle_profile['edges']}")
        print(f"lifecycle_observations={lifecycle_profile['observations']}")
        print(f"archive_bytes={OUTPUT_ARCHIVE.stat().st_size}")
        return 0
    finally:
        _clean_local_state()


if __name__ == "__main__":
    raise SystemExit(main())
