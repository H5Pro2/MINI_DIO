from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.semantic_memory import SemanticMemory
from tools.create_csv_slice import create_slice
from tools.run_mcm_neighborhood_relation_event_time import (
    _csv_bytes,
    _event_integrity,
    _event_rows,
    _source_rows,
)
from tools.run_mcm_relation_lifecycle_eigenstability import (
    GRAPH_PERMUTATIONS,
    LABEL_PERMUTATIONS,
    _graph_identity_null,
    _label_null,
    _mantel_haenszel_stats,
    _public_transition_rows,
    _run_rows,
    _sensitivity_rows,
    _transition_records,
)
from tools.run_mcm_relation_lifecycle_integration import (
    _actual_observations,
    _expected_observations,
    _lifecycle_rows,
)


GENERATED_DIR = ROOT / "data" / "generated" / "2092_mcm_lifecycle_holdout"
DEBUG_ROOT = ROOT / "debug" / "2092_mcm_lifecycle_holdout"
MEMORY_PATH = ROOT / "memory" / "topology_2092_lifecycle_holdout.json"
OUTPUT_ARCHIVE = ROOT / "data" / "2092_mcm_lifecycle_holdout_events.zip"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT"
BASELINE_SUMMARY = (
    FINDING_DIR / "2091_MCM_RELATIONSLEBENSLAUF_EIGENSTABILITAET.summary.csv"
)
HOLDOUT_KEY = "2092_mcm_relation_lifecycle_independent_holdout_v1"
ROWS = 1000
STARTS = tuple(range(0, 10000, ROWS))
SEED = 2092
SOURCES = (
    ("DOGE", 2024, ROOT / "data" / "kontrolliert_doge_2024_5m_17k_DOGEUSDT.csv"),
    ("DOGE", 2025, ROOT / "data" / "kontrolliert_doge_2025_5m_16992_DOGEUSDT.csv"),
    ("PAXG", 2024, ROOT / "data" / "kontrolliert_paxg_2024_5m_17k_PAXGUSDT.csv"),
    ("PAXG", 2025, ROOT / "data" / "kontrolliert_paxg_2025_5m_16992_PAXGUSDT.csv"),
    ("XRP", 2024, ROOT / "data" / "kontrolliert_xrp_2024_5m_17k_XRPUSDT.csv"),
    ("XRP", 2025, ROOT / "data" / "kontrolliert_xrp_2025_5m_16992_XRPUSDT.csv"),
)


@dataclass(frozen=True)
class WorldSpec:
    asset: str
    year: int
    source: Path
    start: int
    order_digest: str
    position: int

    @property
    def world_id(self) -> str:
        return f"W2092_H_{self.position:03d}"

    @property
    def extracted_path(self) -> Path:
        return GENERATED_DIR / (
            f"{self.position:03d}_{self.asset.lower()}_{self.year}_5m_"
            f"start{self.start}_rows{ROWS}.csv"
        )


def _world_specs() -> list[WorldSpec]:
    pending = []
    for asset, year, source in SOURCES:
        for start in STARTS:
            key = f"{HOLDOUT_KEY}|{source.name}|{start}|{ROWS}"
            pending.append(
                (
                    hashlib.sha256(key.encode("utf-8")).hexdigest(),
                    asset,
                    year,
                    source,
                    start,
                )
            )
    pending.sort(key=lambda item: (item[0], item[2], item[1], item[4]))
    return [
        WorldSpec(asset, year, source, start, digest, position)
        for position, (digest, asset, year, source, start) in enumerate(
            pending, start=1
        )
    ]


def _clean_local_state() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    if DEBUG_ROOT.exists():
        shutil.rmtree(DEBUG_ROOT)
    if MEMORY_PATH.exists():
        MEMORY_PATH.unlink()


def _prepare_worlds(specs: list[WorldSpec]) -> None:
    for spec in specs:
        result = create_slice(
            spec.source,
            spec.extracted_path,
            start=spec.start,
            rows=ROWS,
        )
        if int(result["rows_written"]) != ROWS:
            raise RuntimeError(
                f"{spec.source.name} start {spec.start} wrote "
                f"{result['rows_written']} instead of {ROWS} rows"
            )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _order_rows(specs: list[WorldSpec]) -> list[dict[str, object]]:
    source_digests = {source: _sha256(source) for _, _, source in SOURCES}
    return [
        {
            "position": spec.position,
            "world_label": spec.world_id,
            "asset": spec.asset,
            "year": spec.year,
            "timeframe": "5m",
            "source_file": spec.source.name,
            "source_sha256": source_digests[spec.source],
            "window_start": spec.start,
            "window_end": spec.start + ROWS,
            "rows": ROWS,
            "sha256_order_key": spec.order_digest,
        }
        for spec in specs
    ]


def _run_worlds(specs: list[WorldSpec]) -> None:
    for position, spec in enumerate(specs, start=1):
        command = [
            sys.executable,
            "-m",
            "mini_dio.run_mini",
            "--data",
            str(spec.extracted_path),
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
            raise RuntimeError(result.stderr or f"holdout failed at {spec.world_id}")
        if position % 10 == 0 or position == len(specs):
            print(f"holdout_worlds_completed={position}/{len(specs)}", flush=True)


def _edge_sets_from_rows(
    rows: list[dict[str, object]],
) -> dict[int, set[tuple[str, str]]]:
    edges: dict[int, set[tuple[str, str]]] = defaultdict(set)
    for row in rows:
        pair = tuple(
            sorted((str(row["left_relation"]), str(row["right_relation"])))
        )
        edges[int(row["relation_age"])].add(pair)
    return dict(edges)


def _maximum_relation_ages(relations: dict[str, dict]) -> dict[str, int]:
    return {
        symbol: int(relation.get("event_count", 0) or 0)
        for symbol, relation in relations.items()
        if int(relation.get("unobserved_prior_events", 0) or 0) == 0
    }


def _comparison_rows(holdout: dict[str, object]) -> list[dict[str, object]]:
    with BASELINE_SUMMARY.open(newline="", encoding="utf-8") as handle:
        baseline = next(csv.DictReader(handle))
    fields = (
        "carried_continuation_rate",
        "new_continuation_rate",
        "continuation_rate_difference",
        "continuation_rate_ratio",
        "mantel_haenszel_common_odds_ratio",
        "label_null_empirical_p",
        "graph_identity_empirical_p",
    )
    return [
        {
            "metric": field,
            "2091_btc_sol_30m": baseline[field],
            "2092_doge_paxg_xrp_5m": holdout[field],
            "holdout_minus_basis": float(holdout[field]) - float(baseline[field]),
        }
        for field in fields
    ]


def _write_archive(
    event_rows: list[dict[str, object]],
    lifecycle_rows: list[dict[str, object]],
    order_rows: list[dict[str, object]],
) -> None:
    with zipfile.ZipFile(
        OUTPUT_ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name, payload in (
            ("event_histories.csv", _csv_bytes(event_rows)),
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
    specs = _world_specs()
    if len(specs) != 60:
        raise RuntimeError(f"expected 60 worlds, found {len(specs)}")
    order_rows = _order_rows(specs)
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
        lifecycle_profile = memory.passive_mcm_relation_lifecycle_profile()
        lifecycle_edges = memory.passive_mcm_relation_lifecycle_edges()
        lifecycle_rows = _lifecycle_rows(lifecycle_edges)
        actual = _actual_observations(lifecycle_rows)
        expected = _expected_observations(relations)
        missing = expected - actual
        unexpected = actual - expected
        lifecycle_integrity_exact = int(not missing and not unexpected)
        if int(event_integrity["event_integrity_exact"]) != 1:
            raise RuntimeError("holdout relation event integrity failed")
        if lifecycle_integrity_exact != 1:
            raise RuntimeError("holdout lifecycle differs from reconstruction")

        edge_sets = _edge_sets_from_rows(lifecycle_rows)
        records = _transition_records(edge_sets, _maximum_relation_ages(relations))
        primary = _mantel_haenszel_stats(records)
        label_null = _label_null(
            records, permutations=LABEL_PERMUTATIONS, seed=SEED
        )
        graph_null = _graph_identity_null(
            records, permutations=GRAPH_PERMUTATIONS, seed=SEED + 1
        )
        run_rows, run_summary = _run_rows(edge_sets)
        analysis_summary = {
            **run_summary,
            **primary,
            "label_null_empirical_p": label_null["empirical_p_ge_observed"],
            "graph_identity_null_mean_rate_difference": graph_null["null_mean"],
            "graph_identity_null_max_rate_difference": graph_null["null_max"],
            "graph_identity_empirical_p": graph_null["empirical_p_ge_observed"],
        }
        _write_archive(event_rows, lifecycle_rows, order_rows)
        summary_rows = [
            {
                "worlds": len(specs),
                "sources": len(SOURCES),
                "assets": len({spec.asset for spec in specs}),
                "years": len({spec.year for spec in specs}),
                "timeframe": "5m",
                "relations": len(source),
                "events": len(event_rows),
                "event_integrity_exact": event_integrity["event_integrity_exact"],
                "lifecycle_integrity_exact": lifecycle_integrity_exact,
                "lifecycle_relations": lifecycle_profile["relations"],
                "lifecycle_edges": lifecycle_profile["edges"],
                "lifecycle_observations": lifecycle_profile["observations"],
                **analysis_summary,
                "memory_size_bytes": MEMORY_PATH.stat().st_size,
                "lifecycle_document_bytes": len(
                    json.dumps(
                        memory.data["passive_mcm_relation_lifecycle_memory"],
                        indent=2,
                        sort_keys=True,
                    ).encode("utf-8")
                ),
                "archive_bytes": OUTPUT_ARCHIVE.stat().st_size,
                "holdout_key": HOLDOUT_KEY,
                "read_by_mini_dio": lifecycle_profile["read_by_mini_dio"],
                "influences_field": lifecycle_profile["influences_field"],
                "influences_action": lifecycle_profile["influences_action"],
            }
        ]
        integrity_rows = [
            {
                "event_integrity_exact": event_integrity["event_integrity_exact"],
                "stored_lifecycle_observations": len(actual),
                "expected_lifecycle_observations": len(expected),
                "missing_lifecycle_observations": len(missing),
                "unexpected_lifecycle_observations": len(unexpected),
                "lifecycle_integrity_exact": lifecycle_integrity_exact,
                "source_events_before_start": lifecycle_profile[
                    "source_events_before_start"
                ],
            }
        ]
        _write_csv("order", order_rows)
        _write_csv("integrity", integrity_rows)
        _write_csv("transitions", _public_transition_rows(records))
        _write_csv("sensitivity", _sensitivity_rows(records))
        _write_csv("null", [label_null, graph_null])
        _write_csv("runs", run_rows)
        _write_csv("comparison", _comparison_rows(summary_rows[0]))
        _write_csv("summary", summary_rows)
        print(f"lifecycle_observations={len(actual)}")
        print(f"rate_ratio={primary['continuation_rate_ratio']}")
        print(f"graph_identity_p={graph_null['empirical_p_ge_observed']}")
        print(f"archive_bytes={OUTPUT_ARCHIVE.stat().st_size}")
        return 0
    finally:
        _clean_local_state()


if __name__ == "__main__":
    raise SystemExit(main())
