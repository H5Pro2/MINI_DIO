from __future__ import annotations

import csv
import hashlib
import io
import json
import random
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neighborhood_event_memory import EVENT_FIELDS, EVENT_FORMAT
from mini_dio.semantic_memory import SemanticMemory
from tools.create_csv_slice import create_slice
from tools.run_mcm_multiplex_holdout import (
    _best_component_match,
    _discover_components,
    _event_histories,
    _final_reference_rows,
    _histories_from_archive,
    _internal_edge_count,
    _largest_overlap_component,
    _reference_components,
)
from tools.run_mcm_neighborhood_relation_event_time import (
    _csv_bytes,
    _event_integrity,
    _event_rows,
    _source_rows,
)
from tools.run_mcm_relation_age_trajectory_neighborhoods import _eligible_vectors


GENERATED_DIR = ROOT / "data" / "generated" / "2089_mcm_breadth_data_holdout"
DEBUG_ROOT = ROOT / "debug" / "2089_mcm_breadth_data_holdout"
MEMORY_PATH = ROOT / "memory" / "topology_2089_data_holdout.json"
EVENT_ARCHIVE = ROOT / "data" / "2089_mcm_breadth_data_holdout_events.zip"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2089_MCM_BREITENSCHICHT_DATEN_HOLDOUT"
HOLDOUT_KEY = "2089_mcm_breadth_data_holdout_v1"
ROWS = 1000
STARTS = tuple(range(0, 16000, ROWS))
PERMUTATIONS = 1000
SEED = 2089
SOURCES = (
    ("BTC", 2024, ROOT / "data" / "1-12_2024_30m_BTCUSDT.csv"),
    ("SOL", 2024, ROOT / "data" / "1-12_2024_30m_SOLUSDT.csv"),
    ("BTC", 2025, ROOT / "data" / "1-12_2025_30m_BTCUSDT.csv"),
    ("SOL", 2025, ROOT / "data" / "1-12_2025_30m_SOLUSDT.csv"),
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
        return f"W2089_D_{self.position:03d}"

    @property
    def extracted_path(self) -> Path:
        return GENERATED_DIR / (
            f"{self.position:03d}_{self.asset.lower()}_{self.year}_30m_"
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
            "timeframe": "30m",
            "source_file": spec.source.name,
            "source_sha256": source_digests[spec.source],
            "window_start": spec.start,
            "window_end": spec.start + ROWS,
            "rows": ROWS,
            "sha256_order_key": spec.order_digest,
        }
        for spec in specs
    ]


def _run_holdout(specs: list[WorldSpec]) -> None:
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
        if position % 8 == 0 or position == len(specs):
            print(f"holdout_worlds_completed={position}/{len(specs)}", flush=True)


def _prior_breadth_references() -> dict[str, set[str]]:
    reference_2087 = _reference_components()["breadth_growth"]
    histories_2088 = _histories_from_archive()
    _, components_2088, _ = _discover_components(histories_2088)
    reference_2088 = max(
        components_2088["breadth_growth"], key=lambda component: len(component)
    )
    return {
        "2087_closed_breadth_19": reference_2087,
        "2088_blind_breadth_70": reference_2088,
    }


def _reference_rows(
    persistent_edges: set[tuple[str, str]],
    components: list[set[str]],
    references: dict[str, set[str]],
    eligible_nodes: set[str],
) -> list[dict[str, object]]:
    rng = random.Random(SEED)
    population = sorted(eligible_nodes)
    rows = []
    for reference_name, reference in references.items():
        present = reference & eligible_nodes
        observed_edges = _internal_edge_count(persistent_edges, present)
        overlap_intersection, overlap_size, overlap_jaccard = (
            _largest_overlap_component(present, components)
        )
        jaccard_intersection, jaccard_size, best_jaccard = _best_component_match(
            present, components
        )
        edge_null = []
        overlap_null = []
        jaccard_null = []
        for _ in range(PERMUTATIONS):
            conditional_sample = set(rng.sample(population, len(present)))
            edge_null.append(
                _internal_edge_count(persistent_edges, conditional_sample)
            )
            overlap_null.append(
                _largest_overlap_component(conditional_sample, components)[0]
            )
            jaccard_null.append(
                _best_component_match(conditional_sample, components)[2]
            )
        edge_mean = sum(edge_null) / len(edge_null)
        overlap_mean = sum(overlap_null) / len(overlap_null)
        jaccard_mean = sum(jaccard_null) / len(jaccard_null)
        possible_edges = len(reference) * (len(reference) - 1) // 2
        possible_present_edges = len(present) * (len(present) - 1) // 2
        rows.append(
            {
                "reference": reference_name,
                "reference_relations": len(reference),
                "holdout_present_relations": len(present),
                "holdout_present_share": len(present) / max(1, len(reference)),
                "possible_reference_edges": possible_edges,
                "possible_present_edges": possible_present_edges,
                "retained_reference_edges": observed_edges,
                "retained_reference_edge_share": observed_edges
                / max(1, possible_edges),
                "retained_present_edge_share": observed_edges
                / max(1, possible_present_edges),
                "conditional_edge_null_mean": edge_mean,
                "conditional_edge_null_max": max(edge_null),
                "conditional_edge_null_ratio": observed_edges
                / max(1e-12, edge_mean),
                "conditional_edge_empirical_p": (
                    1 + sum(value >= observed_edges for value in edge_null)
                )
                / (PERMUTATIONS + 1),
                "largest_present_overlap_component_relations": overlap_size,
                "largest_component_shared_present_relations": overlap_intersection,
                "largest_present_overlap_component_jaccard": overlap_jaccard,
                "component_overlap_null_mean": overlap_mean,
                "component_overlap_null_max": max(overlap_null),
                "component_overlap_empirical_p": (
                    1
                    + sum(
                        value >= overlap_intersection for value in overlap_null
                    )
                )
                / (PERMUTATIONS + 1),
                "best_jaccard_component_relations": jaccard_size,
                "best_jaccard_shared_relations": jaccard_intersection,
                "best_component_jaccard": best_jaccard,
                "component_jaccard_null_mean": jaccard_mean,
                "component_jaccard_null_max": max(jaccard_null),
                "component_jaccard_empirical_p": (
                    1 + sum(value >= best_jaccard for value in jaccard_null)
                )
                / (PERMUTATIONS + 1),
                "permutations": PERMUTATIONS,
                "seed": SEED,
            }
        )
    return rows


def _equivalence_rows(source: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    rows = _final_reference_rows(source)
    histories_2088 = _histories_from_archive()
    reference_2088 = {
        pair_key for sequence, pair_key in histories_2088 if sequence == "holdout"
    }
    shared = set(source) & reference_2088
    rows.append(
        {
            "reference_sequence": "2088_data_order",
            "holdout_relations": len(source),
            "reference_relations": len(reference_2088),
            "shared_relations": len(shared),
            "relation_jaccard": len(shared)
            / max(1, len(set(source) | reference_2088)),
        }
    )
    return rows


def _write_archive(
    event_rows: list[dict[str, object]], order_rows: list[dict[str, object]]
) -> None:
    EVENT_ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        EVENT_ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name, payload in (
            ("event_histories.csv", _csv_bytes(event_rows)),
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


def _histories_from_event_archive() -> dict[tuple[str, str], list[dict[str, int]]]:
    histories: dict[tuple[str, str], list[dict[str, int]]] = {}
    with zipfile.ZipFile(EVENT_ARCHIVE) as archive:
        with archive.open("event_histories.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8"))
            for row in reader:
                key = (row["sequence"], row["pair_key"])
                event = {
                    "event_index": int(row["event_index"]),
                    **{field: int(row[field]) for field in EVENT_FIELDS},
                }
                histories.setdefault(key, []).append(event)
    for history in histories.values():
        history.sort(key=lambda event: event["event_index"])
    return histories


def _analyze_histories(
    histories: dict[tuple[str, str], list[dict[str, int]]]
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    persistent, components, discovery_rows = _discover_components(histories)

    # Prior component identities are loaded only after blind 2089 discovery.
    references = _prior_breadth_references()
    age10_nodes = set(_eligible_vectors(histories, "holdout", 10))
    reference_rows = _reference_rows(
        persistent["breadth_growth"],
        components["breadth_growth"],
        references,
        age10_nodes,
    )
    return discovery_rows, reference_rows


def _reanalyze_existing() -> int:
    histories = _histories_from_event_archive()
    discovery_rows, reference_rows = _analyze_histories(histories)
    _write_csv("discovery", discovery_rows)
    _write_csv("reference", reference_rows)
    print(f"reanalyzed_event_relations={len(histories)}")
    print(f"discovery_components={len(discovery_rows)}")
    return 0


def main() -> int:
    if sys.argv[1:] == ["--reanalyze"]:
        return _reanalyze_existing()
    if sys.argv[1:]:
        raise SystemExit("usage: run_mcm_breadth_data_holdout.py [--reanalyze]")

    specs = _world_specs()
    if len(specs) != 64:
        raise RuntimeError(f"expected 64 worlds, found {len(specs)}")
    _clean_local_state()
    try:
        _prepare_worlds(specs)
        order_rows = _order_rows(specs)
        _run_holdout(specs)
        memory = SemanticMemory(MEMORY_PATH)
        memory.load()
        source = _source_rows(memory)
        relations = memory.passive_mcm_neighborhood_event_relations()
        integrity = _event_integrity(source, relations)
        if int(integrity["event_integrity_exact"]) != 1:
            raise RuntimeError("data holdout relation event history is incomplete")

        histories = _event_histories(relations)
        discovery_rows, reference_rows = _analyze_histories(histories)
        age10_nodes = set(_eligible_vectors(histories, "holdout", 10))
        event_rows = _event_rows("holdout", relations)
        _write_archive(event_rows, order_rows)
        summary_rows = [
            {
                "worlds": len(specs),
                "sources": len(SOURCES),
                "real_worlds": len(specs),
                "synthetic_worlds": 0,
                "relations": len(source),
                "events": len(event_rows),
                "multi_event_relations": sum(
                    int(relation["event_count"]) >= 2
                    for relation in relations.values()
                ),
                "age10_relations": len(age10_nodes),
                "event_integrity_exact": integrity["event_integrity_exact"],
                "memory_size_bytes": MEMORY_PATH.stat().st_size,
                "event_document_bytes": len(
                    json.dumps(
                        memory.data["passive_mcm_neighborhood_event_memory"],
                        indent=2,
                        sort_keys=True,
                    ).encode("utf-8")
                ),
                "event_archive_bytes": EVENT_ARCHIVE.stat().st_size,
                "format": EVENT_FORMAT,
                "holdout_key": HOLDOUT_KEY,
                "read_by_mini_dio": 0,
                "influences_field": 0,
                "influences_action": 0,
            }
        ]
        _write_csv("order", order_rows)
        _write_csv("equivalence", _equivalence_rows(source))
        _write_csv("discovery", discovery_rows)
        _write_csv("reference", reference_rows)
        _write_csv("summary", summary_rows)
        print(f"event_rows={len(event_rows)}")
        print(f"discovery_components={len(discovery_rows)}")
        print(f"archive_bytes={EVENT_ARCHIVE.stat().st_size}")
        return 0
    finally:
        _clean_local_state()


if __name__ == "__main__":
    raise SystemExit(main())
