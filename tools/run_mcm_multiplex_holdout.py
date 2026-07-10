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
from tools.run_mcm_maturation_trajectory_neighborhoods import _mutual_nearest_edges
from tools.run_mcm_neighborhood_relation_event_time import (
    _csv_bytes,
    _event_integrity,
    _event_rows,
    _source_rows,
)
from tools.run_mcm_relation_age_edge_persistence import (
    _connected_components,
    _persistent_edges,
    _restricted_edges,
)
from tools.run_mcm_relation_age_trajectory_neighborhoods import (
    _eligible_vectors,
    _rank_vectors,
    SCOPES,
)


GENERATED_DIR = ROOT / "data" / "generated" / "2088_mcm_multiplex_holdout"
DEBUG_ROOT = ROOT / "debug" / "2088_mcm_multiplex_holdout"
MEMORY_PATH = ROOT / "memory" / "topology_2088_holdout.json"
EVENT_ARCHIVE = ROOT / "data" / "2088_mcm_multiplex_holdout_events.zip"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2088_MCM_MULTIPLEX_BLIND_HOLDOUT"
REFERENCE_COMPONENTS = (
    FINDING_DIR / "2087_MCM_EIGENZEIT_KANTENPERSISTENZ.components.csv"
)
REFERENCE_SNAPSHOT = (
    FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.snapshots.csv"
)
HOLDOUT_KEY = "2088_mcm_multiplex_holdout_v1"
AGES = (3, 5, 10)
DISCOVERY_SCOPES = ("event_cadence", "breadth_growth", "profile_growth")
REFERENCE_SCOPES = ("breadth_growth", "profile_growth")
PERMUTATIONS = 1000
SEED = 2088


@dataclass(frozen=True)
class WorldSpec:
    source_archive: Path
    member: str
    order_digest: str
    position: int

    @property
    def world_id(self) -> str:
        return f"W2088_H_{self.position:03d}"

    @property
    def extracted_path(self) -> Path:
        return GENERATED_DIR / f"{self.position:03d}.csv"


def _world_specs() -> list[WorldSpec]:
    archives = (
        ROOT / "data" / "2070_role_family_followworlds.zip",
        ROOT / "data" / "2073_role_family_null_controls.zip",
        ROOT / "data" / "2074_rf05_crossyear_timeframe_holdout.zip",
    )
    pending = []
    for archive_path in archives:
        with zipfile.ZipFile(archive_path) as archive:
            for member in sorted(archive.namelist()):
                if member.lower().endswith(".csv") and Path(member).name.lower() != "manifest.csv":
                    source = f"{HOLDOUT_KEY}|{archive_path.name}|{member}"
                    pending.append(
                        (
                            hashlib.sha256(source.encode("utf-8")).hexdigest(),
                            archive_path,
                            member,
                        )
                    )
    pending.sort(key=lambda item: (item[0], item[1].name, item[2]))
    return [
        WorldSpec(archive, member, digest, position)
        for position, (digest, archive, member) in enumerate(pending, start=1)
    ]


def _clean_local_state() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    if DEBUG_ROOT.exists():
        shutil.rmtree(DEBUG_ROOT)
    if MEMORY_PATH.exists():
        MEMORY_PATH.unlink()


def _prepare_worlds(specs: list[WorldSpec]) -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    archives: dict[Path, zipfile.ZipFile] = {}
    try:
        for spec in specs:
            archive = archives.get(spec.source_archive)
            if archive is None:
                archive = zipfile.ZipFile(spec.source_archive)
                archives[spec.source_archive] = archive
            with archive.open(spec.member) as source, spec.extracted_path.open("wb") as target:
                shutil.copyfileobj(source, target)
    finally:
        for archive in archives.values():
            archive.close()


def _order_rows(specs: list[WorldSpec]) -> list[dict[str, object]]:
    return [
        {
            "position": spec.position,
            "world_label": spec.world_id,
            "source_archive": spec.source_archive.name,
            "source_member": spec.member,
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
        if position % 10 == 0 or position == len(specs):
            print(f"holdout_worlds_completed={position}/{len(specs)}", flush=True)


def _event_histories(relations: dict[str, dict]) -> dict[tuple[str, str], list[dict]]:
    return {
        (
            "holdout",
            "|".join(sorted((relation["left_node"], relation["right_node"]))),
        ): list(relation["events"])
        for relation in relations.values()
    }


def _discover_components(
    histories: dict[tuple[str, str], list[dict]],
) -> tuple[
    dict[str, set[tuple[str, str]]],
    dict[str, list[set[str]]],
    list[dict[str, object]],
]:
    vectors = {
        age: _eligible_vectors(histories, "holdout", age) for age in AGES
    }
    age_edges = {}
    for age in AGES:
        for scope in DISCOVERY_SCOPES:
            ranked = _rank_vectors(vectors[age], SCOPES[scope])
            graph, _ = _mutual_nearest_edges({(age,): ranked})
            age_edges[(age, scope)] = graph
    age10_nodes = set(vectors[10])
    persistent = {
        scope: _persistent_edges(
            [age_edges[(age, scope)] for age in AGES], age10_nodes
        )
        for scope in DISCOVERY_SCOPES
    }
    components = {
        scope: _connected_components(persistent[scope]) for scope in DISCOVERY_SCOPES
    }
    rows = []
    for scope in DISCOVERY_SCOPES:
        for index, component in enumerate(components[scope], start=1):
            component_edges = _restricted_edges(persistent[scope], component)
            maximum_edges = len(component) * (len(component) - 1) // 2
            rows.append(
                {
                    "scope": scope,
                    "component_index": index,
                    "relations": len(component),
                    "edges": len(component_edges),
                    "complete_clique": int(len(component_edges) == maximum_edges),
                }
            )
    return persistent, components, rows


def _reference_components() -> dict[str, set[str]]:
    references = {}
    with REFERENCE_COMPONENTS.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["scope"] in REFERENCE_SCOPES and int(row["component_index"]) == 1:
                references[row["scope"]] = set(row["members"].split(";"))
    return references


def _best_component_match(
    reference: set[str], components: list[set[str]]
) -> tuple[int, int, float]:
    best_intersection = 0
    best_size = 0
    best_jaccard = 0.0
    for component in components:
        intersection = len(reference & component)
        jaccard = intersection / max(1, len(reference | component))
        if (jaccard, intersection, -len(component)) > (
            best_jaccard,
            best_intersection,
            -best_size,
        ):
            best_intersection = intersection
            best_size = len(component)
            best_jaccard = jaccard
    return best_intersection, best_size, best_jaccard


def _largest_overlap_component(
    reference: set[str], components: list[set[str]]
) -> tuple[int, int, float]:
    best_intersection = 0
    best_size = 0
    best_jaccard = 0.0
    for component in components:
        intersection = len(reference & component)
        jaccard = intersection / max(1, len(reference | component))
        if (intersection, jaccard, -len(component)) > (
            best_intersection,
            best_jaccard,
            -best_size,
        ):
            best_intersection = intersection
            best_size = len(component)
            best_jaccard = jaccard
    return best_intersection, best_size, best_jaccard


def _internal_edge_count(edges: set[tuple[str, str]], nodes: set[str]) -> int:
    return len(_restricted_edges(edges, nodes))


def _reference_rows(
    persistent: dict[str, set[tuple[str, str]]],
    components: dict[str, list[set[str]]],
    references: dict[str, set[str]],
    eligible_nodes: set[str],
) -> list[dict[str, object]]:
    rng = random.Random(SEED)
    population = sorted(eligible_nodes)
    rows = []
    for scope in REFERENCE_SCOPES:
        reference = references[scope]
        present = reference & eligible_nodes
        observed_edges = _internal_edge_count(persistent[scope], present)
        best_intersection, best_size, best_jaccard = _best_component_match(
            reference, components[scope]
        )
        overlap_intersection, overlap_size, overlap_jaccard = (
            _largest_overlap_component(reference, components[scope])
        )
        edge_null = []
        component_jaccard_null = []
        component_overlap_null = []
        for _ in range(PERMUTATIONS):
            conditional_sample = set(rng.sample(population, len(present)))
            full_sample = set(rng.sample(population, len(reference)))
            edge_null.append(
                _internal_edge_count(persistent[scope], conditional_sample)
            )
            component_jaccard_null.append(
                _best_component_match(full_sample, components[scope])[2]
            )
            component_overlap_null.append(
                _largest_overlap_component(full_sample, components[scope])[0]
            )
        edge_mean = sum(edge_null) / len(edge_null)
        component_jaccard_mean = sum(component_jaccard_null) / len(
            component_jaccard_null
        )
        component_overlap_mean = sum(component_overlap_null) / len(
            component_overlap_null
        )
        rows.append(
            {
                "scope": scope,
                "reference_relations": len(reference),
                "holdout_present_relations": len(present),
                "holdout_present_share": len(present) / max(1, len(reference)),
                "possible_reference_edges": len(reference) * (len(reference) - 1) // 2,
                "retained_reference_edges": observed_edges,
                "retained_reference_edge_share": observed_edges
                / max(1, len(reference) * (len(reference) - 1) // 2),
                "conditional_edge_null_mean": edge_mean,
                "conditional_edge_null_max": max(edge_null),
                "conditional_edge_null_ratio": observed_edges / max(1e-12, edge_mean),
                "conditional_edge_empirical_p": (
                    1 + sum(value >= observed_edges for value in edge_null)
                )
                / (PERMUTATIONS + 1),
                "largest_overlap_component_relations": overlap_size,
                "largest_component_shared_relations": overlap_intersection,
                "largest_overlap_component_jaccard": overlap_jaccard,
                "component_overlap_null_mean": component_overlap_mean,
                "component_overlap_null_max": max(component_overlap_null),
                "component_overlap_empirical_p": (
                    1
                    + sum(
                        value >= overlap_intersection
                        for value in component_overlap_null
                    )
                )
                / (PERMUTATIONS + 1),
                "best_jaccard_component_relations": best_size,
                "best_jaccard_shared_relations": best_intersection,
                "best_component_jaccard": best_jaccard,
                "component_jaccard_null_mean": component_jaccard_mean,
                "component_jaccard_null_max": max(component_jaccard_null),
                "component_jaccard_empirical_p": (
                    1
                    + sum(
                        value >= best_jaccard for value in component_jaccard_null
                    )
                )
                / (PERMUTATIONS + 1),
                "permutations": PERMUTATIONS,
                "seed": SEED,
            }
        )
    return rows


def _final_reference_rows(source: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    with REFERENCE_SNAPSHOT.open(newline="", encoding="utf-8") as handle:
        reference_rows = list(csv.DictReader(handle))
    for sequence in ("forward", "reverse"):
        reference = {
            row["pair_key"]: row
            for row in reference_rows
            if row["sequence"] == sequence and int(row["position"]) == 81
        }
        shared = set(source) & set(reference)
        rows.append(
            {
                "reference_sequence": sequence,
                "holdout_relations": len(source),
                "reference_relations": len(reference),
                "shared_relations": len(shared),
                "relation_jaccard": len(shared) / max(1, len(set(source) | set(reference))),
            }
        )
    return rows


def _write_archive(
    event_rows: list[dict[str, object]], order_rows: list[dict[str, object]]
) -> None:
    EVENT_ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(EVENT_ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, payload in (
            ("event_histories.csv", _csv_bytes(event_rows)),
            ("holdout_order.csv", _csv_bytes(order_rows)),
        ):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, payload, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _histories_from_archive() -> dict[tuple[str, str], list[dict[str, int]]]:
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


def _reanalyze_existing() -> int:
    histories = _histories_from_archive()
    persistent, components, discovery_rows = _discover_components(histories)

    # The known 2087 identities are loaded only after blind holdout discovery.
    references = _reference_components()
    age10_nodes = set(_eligible_vectors(histories, "holdout", 10))
    reference_rows = _reference_rows(
        persistent, components, references, age10_nodes
    )
    _write_csv("discovery", discovery_rows)
    _write_csv("reference", reference_rows)
    print(f"reanalyzed_event_relations={len(histories)}")
    print(f"discovery_components={len(discovery_rows)}")
    return 0


def main() -> int:
    if sys.argv[1:] == ["--reanalyze"]:
        return _reanalyze_existing()
    if sys.argv[1:]:
        raise SystemExit("usage: run_mcm_multiplex_holdout.py [--reanalyze]")
    specs = _world_specs()
    if len(specs) != 81:
        raise RuntimeError(f"expected 81 worlds, found {len(specs)}")
    order_rows = _order_rows(specs)
    _clean_local_state()
    try:
        _prepare_worlds(specs)
        _run_holdout(specs)
        memory = SemanticMemory(MEMORY_PATH)
        memory.load()
        source = _source_rows(memory)
        relations = memory.passive_mcm_neighborhood_event_relations()
        integrity = _event_integrity(source, relations)
        if int(integrity["event_integrity_exact"]) != 1:
            raise RuntimeError("holdout relation event history is incomplete")

        histories = _event_histories(relations)
        persistent, components, discovery_rows = _discover_components(histories)

        # The known 2087 identities are loaded only after blind holdout discovery.
        references = _reference_components()
        age10_nodes = set(_eligible_vectors(histories, "holdout", 10))
        reference_rows = _reference_rows(
            persistent, components, references, age10_nodes
        )
        event_rows = _event_rows("holdout", relations)
        _write_archive(event_rows, order_rows)
        summary_rows = [
            {
                "worlds": len(specs),
                "relations": len(source),
                "events": len(event_rows),
                "multi_event_relations": sum(
                    int(relation["event_count"]) >= 2 for relation in relations.values()
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
        _write_csv("equivalence", _final_reference_rows(source))
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
