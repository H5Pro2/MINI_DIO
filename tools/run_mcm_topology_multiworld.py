from __future__ import annotations

import csv
import json
import shutil
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "data" / "generated" / "2076_mcm_topology_multiworld"
MEMORY_DIR = ROOT / "memory"
DEBUG_ROOT = ROOT / "debug" / "2076_mcm_topology_multiworld"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
SUMMARY_CSV = FINDING_DIR / "2076_MCM_TOPOLOGIE_MEHRWELT_WACHSTUM.summary.csv"
OVERLAP_CSV = FINDING_DIR / "2076_MCM_TOPOLOGIE_MEHRWELT_WACHSTUM.overlap.csv"
ORDER_CSV = FINDING_DIR / "2076_MCM_TOPOLOGIE_MEHRWELT_WACHSTUM.order.csv"


@dataclass(frozen=True)
class WorldSpec:
    key: str
    kind: str
    archive: Path
    member: str

    @property
    def extracted_path(self) -> Path:
        return GENERATED_DIR / self.member


WORLDS = {
    "real_anchor": WorldSpec(
        key="TOPO_REAL_ANCHOR_BTC_2025_1H_5000_6000",
        kind="real_anchor",
        archive=ROOT / "data" / "2070_role_family_followworlds.zip",
        member="kontrolliert_2070_btc_2025_1h_start5000_rows1000.csv",
    ),
    "real_follow": WorldSpec(
        key="TOPO_REAL_FOLLOW_BTC_2025_1H_6000_7000",
        kind="real_follow",
        archive=ROOT / "data" / "2070_role_family_followworlds.zip",
        member="kontrolliert_2070_btc_2025_1h_start6000_rows1000.csv",
    ),
    "null_shuffle": WorldSpec(
        key="TOPO_NULL_SHUFFLE_BTC_2025_1H_6000_7000",
        kind="null_shuffle",
        archive=ROOT / "data" / "2073_role_family_null_controls.zip",
        member="kontrolliert_2073_btc_start6000_shuffle_order_1000.csv",
    ),
    "null_random": WorldSpec(
        key="TOPO_NULL_RANDOM_BTC_2025_1H_6000_7000",
        kind="null_random_sign",
        archive=ROOT / "data" / "2073_role_family_null_controls.zip",
        member="kontrolliert_2073_btc_start6000_random_sign_1000.csv",
    ),
}

SEQUENCES = {
    "real_first": ["real_anchor", "real_follow", "null_shuffle", "null_random"],
    "null_first": ["null_shuffle", "null_random", "real_anchor", "real_follow"],
}


def _prepare_worlds() -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    for spec in WORLDS.values():
        with zipfile.ZipFile(spec.archive) as archive:
            with archive.open(spec.member) as source, spec.extracted_path.open("wb") as target:
                shutil.copyfileobj(source, target)


def _clean_sequence_state(sequence: str) -> tuple[Path, Path]:
    memory_path = MEMORY_DIR / f"topology_2076_{sequence}.json"
    debug_root = DEBUG_ROOT / sequence
    if memory_path.exists():
        memory_path.unlink()
    if debug_root.exists():
        shutil.rmtree(debug_root)
    return memory_path, debug_root


def _run_world(spec: WorldSpec, memory_path: Path, debug_root: Path) -> dict:
    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        str(spec.extracted_path),
        "--runs",
        "1",
        "--memory",
        str(memory_path),
        "--debug-root",
        str(debug_root),
        "--world-label",
        spec.key,
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
        raise RuntimeError(result.stderr or f"run failed for {spec.key}")
    memory = json.loads(memory_path.read_text(encoding="utf-8"))
    return dict(memory.get("passive_mcm_topology", {}) or {})


def _profile(topology: dict) -> dict[str, int]:
    nodes = dict(topology.get("nodes", {}) or {})
    edges = dict(topology.get("edges", {}) or {})
    node_observations = sum(int(item.get("seen_count", 0) or 0) for item in nodes.values())
    edge_observations = sum(int(item.get("seen_count", 0) or 0) for item in edges.values())
    return {
        "nodes": len(nodes),
        "edges": len(edges),
        "node_observations": node_observations,
        "edge_observations": edge_observations,
        "node_returns": max(0, node_observations - len(nodes)),
        "edge_returns": max(0, edge_observations - len(edges)),
    }


def _context_sets(topology: dict, record_key: str) -> dict[str, set[str]]:
    records = dict(topology.get(record_key, {}) or {})
    out = {spec.key: set() for spec in WORLDS.values()}
    symbol_key = "node_symbol" if record_key == "nodes" else "edge_symbol"
    for fallback_symbol, record in records.items():
        symbol = str(record.get(symbol_key, fallback_symbol) or fallback_symbol)
        contexts = dict(record.get("world_observations", {}) or {})
        for world_key in out:
            if world_key in contexts:
                out[world_key].add(symbol)
    return out


def _overlap_rows(sequence: str, topology: dict) -> list[dict[str, object]]:
    node_sets = _context_sets(topology, "nodes")
    edge_sets = _context_sets(topology, "edges")
    rows: list[dict[str, object]] = []
    for left_name, right_name in combinations(WORLDS, 2):
        left = WORLDS[left_name]
        right = WORLDS[right_name]
        left_nodes = node_sets[left.key]
        right_nodes = node_sets[right.key]
        left_edges = edge_sets[left.key]
        right_edges = edge_sets[right.key]
        node_union = left_nodes | right_nodes
        edge_union = left_edges | right_edges
        rows.append(
            {
                "sequence": sequence,
                "left_world": left_name,
                "right_world": right_name,
                "left_nodes": len(left_nodes),
                "right_nodes": len(right_nodes),
                "shared_nodes": len(left_nodes & right_nodes),
                "node_jaccard": len(left_nodes & right_nodes) / max(1, len(node_union)),
                "left_edges": len(left_edges),
                "right_edges": len(right_edges),
                "shared_edges": len(left_edges & right_edges),
                "edge_jaccard": len(left_edges & right_edges) / max(1, len(edge_union)),
            }
        )
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _order_rows(topologies: dict[str, dict]) -> list[dict[str, object]]:
    left_name = "real_first"
    right_name = "null_first"
    left = topologies[left_name]
    right = topologies[right_name]
    rows: list[dict[str, object]] = []
    for record_key in ("nodes", "edges"):
        symbol_key = "node_symbol" if record_key == "nodes" else "edge_symbol"
        left_records = dict(left.get(record_key, {}) or {})
        right_records = dict(right.get(record_key, {}) or {})
        left_symbols = set(left_records)
        right_symbols = set(right_records)
        union = left_symbols | right_symbols
        shared = left_symbols & right_symbols
        rows.append(
            {
                "scope": "global",
                "world": "all",
                "record_kind": record_key,
                "real_first_count": len(left_symbols),
                "null_first_count": len(right_symbols),
                "shared": len(shared),
                "jaccard": len(shared) / max(1, len(union)),
                "seen_count_differences": sum(
                    1
                    for symbol in shared
                    if int(left_records[symbol].get("seen_count", 0) or 0)
                    != int(right_records[symbol].get("seen_count", 0) or 0)
                ),
            }
        )
        left_contexts = _context_sets(left, record_key)
        right_contexts = _context_sets(right, record_key)
        for spec in WORLDS.values():
            left_symbols = left_contexts[spec.key]
            right_symbols = right_contexts[spec.key]
            union = left_symbols | right_symbols
            shared = left_symbols & right_symbols
            rows.append(
                {
                    "scope": "world",
                    "world": spec.kind,
                    "record_kind": record_key,
                    "real_first_count": len(left_symbols),
                    "null_first_count": len(right_symbols),
                    "shared": len(shared),
                    "jaccard": len(shared) / max(1, len(union)),
                    "seen_count_differences": "",
                }
            )
    return rows


def main() -> int:
    _prepare_worlds()
    summary_rows: list[dict[str, object]] = []
    overlap_rows: list[dict[str, object]] = []
    topologies: dict[str, dict] = {}
    for sequence, order in SEQUENCES.items():
        memory_path, debug_root = _clean_sequence_state(sequence)
        previous = {key: 0 for key in _profile({})}
        topology: dict = {}
        for position, world_name in enumerate(order, start=1):
            spec = WORLDS[world_name]
            topology = _run_world(spec, memory_path, debug_root)
            current = _profile(topology)
            node_observation_delta = current["node_observations"] - previous["node_observations"]
            edge_observation_delta = current["edge_observations"] - previous["edge_observations"]
            new_nodes = current["nodes"] - previous["nodes"]
            new_edges = current["edges"] - previous["edges"]
            summary_rows.append(
                {
                    "sequence": sequence,
                    "position": position,
                    "world": world_name,
                    "world_kind": spec.kind,
                    "node_observations": node_observation_delta,
                    "new_nodes": new_nodes,
                    "returning_node_observations": max(0, node_observation_delta - new_nodes),
                    "cumulative_nodes": current["nodes"],
                    "edge_observations": edge_observation_delta,
                    "new_edges": new_edges,
                    "returning_edge_observations": max(0, edge_observation_delta - new_edges),
                    "cumulative_edges": current["edges"],
                }
            )
            previous = current
        overlap_rows.extend(_overlap_rows(sequence, topology))
        topologies[sequence] = topology

    _write_csv(SUMMARY_CSV, summary_rows)
    _write_csv(OVERLAP_CSV, overlap_rows)
    order_rows = _order_rows(topologies)
    _write_csv(ORDER_CSV, order_rows)
    print(f"summary_rows={len(summary_rows)}")
    print(f"overlap_rows={len(overlap_rows)}")
    print(f"order_rows={len(order_rows)}")
    print(f"summary={SUMMARY_CSV.relative_to(ROOT)}")
    print(f"overlap={OVERLAP_CSV.relative_to(ROOT)}")
    print(f"order={ORDER_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
