from __future__ import annotations

import csv
import hashlib
import json
import math
import shutil
import subprocess
import sys
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.semantic_memory import SemanticMemory


RUN_ID = "2082"
GENERATED_DIR = ROOT / "data" / "generated" / "2082_mcm_neighborhood_consolidation"
MEMORY_DIR = ROOT / "memory"
DEBUG_ROOT = ROOT / "debug" / "2082_mcm_neighborhood_consolidation"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2082_PASSIVE_OFFLINE_KONSOLIDIERUNG_MCM_NACHBARSCHAFT"
REFERENCE_SNAPSHOT = (
    FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.snapshots.csv"
)
REFERENCE_SUMMARY = (
    FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.summary.csv"
)
CHECKPOINTS = (10, 20, 40, 60, 81)
SUPPORT_AXES = ("world_pair_count", "world_count", "growth_seen_count")


@dataclass(frozen=True)
class WorldSpec:
    index: int
    world_id: str
    archive: Path
    member: str

    @property
    def extracted_path(self) -> Path:
        return GENERATED_DIR / f"{self.index:03d}.csv"


def _world_specs() -> list[WorldSpec]:
    archives = (
        ROOT / "data" / "2070_role_family_followworlds.zip",
        ROOT / "data" / "2073_role_family_null_controls.zip",
        ROOT / "data" / "2074_rf05_crossyear_timeframe_holdout.zip",
    )
    pending: list[tuple[Path, str]] = []
    for archive_path in archives:
        with zipfile.ZipFile(archive_path) as archive:
            for member in sorted(archive.namelist()):
                if member.lower().endswith(".csv") and Path(member).name.lower() != "manifest.csv":
                    pending.append((archive_path, member))
    return [
        WorldSpec(index, f"W{RUN_ID}_{index:03d}", archive, member)
        for index, (archive, member) in enumerate(pending, start=1)
    ]


def _memory_path(sequence: str) -> Path:
    return MEMORY_DIR / f"topology_{RUN_ID}_{sequence}.json"


def _clean_local_state() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    if DEBUG_ROOT.exists():
        shutil.rmtree(DEBUG_ROOT)
    for sequence in ("forward", "reverse"):
        path = _memory_path(sequence)
        if path.exists():
            path.unlink()


def _prepare_worlds(specs: list[WorldSpec]) -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    archives: dict[Path, zipfile.ZipFile] = {}
    try:
        for spec in specs:
            archive = archives.get(spec.archive)
            if archive is None:
                archive = zipfile.ZipFile(spec.archive)
                archives[spec.archive] = archive
            with archive.open(spec.member) as source, spec.extracted_path.open("wb") as target:
                shutil.copyfileobj(source, target)
    finally:
        for archive in archives.values():
            archive.close()


def _read_reference() -> dict[tuple[str, int], dict[str, dict[str, str]]]:
    out: dict[tuple[str, int], dict[str, dict[str, str]]] = {}
    with REFERENCE_SNAPSHOT.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            key = (row["sequence"], int(row["position"]))
            out.setdefault(key, {})[row["pair_key"]] = row
    return out


def _read_baseline_sizes() -> dict[str, int]:
    out: dict[str, int] = {}
    with REFERENCE_SUMMARY.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if int(row["position"]) == CHECKPOINTS[-1]:
                out[row["sequence"]] = int(row["memory_size_bytes"])
    return out


def _digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _active_source(memory: SemanticMemory) -> dict[str, dict[str, object]]:
    layer = dict(memory.data.get("passive_mcm_neighborhood_memory", {}) or {})
    out = {}
    for symbol, raw in dict(layer.get("neighborhoods", {}) or {}).items():
        record = dict(raw or {})
        if int(record.get("active", 0) or 0) != 1:
            continue
        pair_key = "|".join(sorted((str(record["left_node"]), str(record["right_node"]))))
        out[pair_key] = {
            "neighborhood_symbol": str(record.get("neighborhood_symbol", symbol) or symbol),
            "world_pair_count": int(record.get("current_world_pair_count", 0) or 0),
            "world_count": int(record.get("current_world_count", 0) or 0),
            "growth_seen_count": int(record.get("growth_seen_count", 0) or 0),
        }
    return out


def _checkpoint_records(memory: SemanticMemory, source: dict[str, dict]) -> dict[str, dict]:
    store = memory.data["passive_mcm_neighborhood_consolidation"]
    checkpoint_symbol = str(store["checkpoints"][-1]["checkpoint_symbol"])
    relations = memory.passive_mcm_neighborhood_consolidation_relations()
    out = {}
    for pair_key, source_record in source.items():
        relation = dict(relations[source_record["neighborhood_symbol"]] or {})
        entries = [
            dict(entry or {})
            for entry in list(relation.get("history", []) or [])
            if str(dict(entry or {}).get("checkpoint_symbol", "")) == checkpoint_symbol
        ]
        if len(entries) != 1:
            raise RuntimeError(f"expected one consolidation entry for {pair_key}")
        out[pair_key] = entries[0]
    return out


def _compare_reference(
    source: dict[str, dict], consolidated: dict[str, dict], reference: dict[str, dict]
) -> dict[str, int]:
    same_set = set(source) == set(consolidated) == set(reference)
    shared = set(source) & set(consolidated) & set(reference)
    source_support_mismatches = sum(
        any(int(source[key][axis]) != int(reference[key][axis]) for axis in SUPPORT_AXES)
        for key in shared
    )
    consolidated_support_mismatches = sum(
        any(int(consolidated[key][axis]) != int(reference[key][axis]) for axis in SUPPORT_AXES)
        for key in shared
    )
    depth_mismatches = sum(
        int(consolidated[key]["pareto_depth"]) != int(reference[key]["pareto_depth"])
        for key in shared
    )
    return {
        "exact_relation_set": int(same_set),
        "source_support_mismatches": source_support_mismatches,
        "consolidated_support_mismatches": consolidated_support_mismatches,
        "depth_mismatches": depth_mismatches,
        "all_exact": int(
            same_set
            and source_support_mismatches == 0
            and consolidated_support_mismatches == 0
            and depth_mismatches == 0
        ),
    }


def _run_sequence(
    sequence: str,
    specs: list[WorldSpec],
    reference: dict[tuple[str, int], dict[str, dict[str, str]]],
) -> dict[str, object]:
    memory_path = _memory_path(sequence)
    debug_root = DEBUG_ROOT / sequence
    order = specs if sequence == "forward" else list(reversed(specs))
    checkpoint_rows: list[dict[str, object]] = []
    equivalence_rows: list[dict[str, object]] = []
    continuity_rows: list[dict[str, object]] = []
    snapshots: dict[int, dict[str, dict]] = {}
    previous_histories: dict[str, list[dict]] = {}
    previous_position = 0
    for position, spec in enumerate(order, start=1):
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
            raise RuntimeError(result.stderr or f"run failed for {sequence}:{spec.world_id}")
        if position in CHECKPOINTS:
            memory = SemanticMemory(memory_path)
            memory.load()
            source = _active_source(memory)
            source_digest = _digest(memory.data["passive_mcm_neighborhood_memory"])
            memory.consolidate_passive_mcm_neighborhood_layers(
                checkpoint_label=f"{sequence}_{position}", run_index=position
            )
            unchanged_in_memory = int(
                source_digest == _digest(memory.data["passive_mcm_neighborhood_memory"])
            )
            memory.save()
            reloaded = SemanticMemory(memory_path)
            reloaded.load()
            unchanged_after_reload = int(
                source_digest == _digest(reloaded.data["passive_mcm_neighborhood_memory"])
            )
            consolidated = _checkpoint_records(reloaded, source)
            snapshots[position] = consolidated
            comparison = _compare_reference(
                source, consolidated, reference[(sequence, position)]
            )
            store = reloaded.data["passive_mcm_neighborhood_consolidation"]
            current_histories = {
                symbol: list(dict(record or {}).get("history", []) or [])
                for symbol, record in (
                    reloaded.passive_mcm_neighborhood_consolidation_relations().items()
                )
            }
            preserved = all(
                current_histories.get(symbol, [])[: len(history)] == history
                for symbol, history in previous_histories.items()
            )
            previous_entries = sum(len(history) for history in previous_histories.values())
            current_entries = sum(len(history) for history in current_histories.values())
            continuity_rows.append(
                {
                    "sequence": sequence,
                    "from_position": previous_position,
                    "to_position": position,
                    "previous_relations": len(previous_histories),
                    "current_relations": len(current_histories),
                    "previous_history_entries": previous_entries,
                    "current_history_entries": current_entries,
                    "expected_added_entries": len(source),
                    "actual_added_entries": current_entries - previous_entries,
                    "history_prefix_preserved": int(preserved),
                }
            )
            latest = dict(store["checkpoints"][-1])
            checkpoint_rows.append(
                {
                    "sequence": sequence,
                    "position": position,
                    "relations": int(latest["relation_count"]),
                    "max_pareto_depth": int(latest["max_pareto_depth"]),
                    "layer_one_relations": int(latest["layer_one_count"]),
                    "history_entries": current_entries,
                    "memory_size_bytes": memory_path.stat().st_size,
                }
            )
            equivalence_rows.append(
                {
                    "sequence": sequence,
                    "position": position,
                    "reference_relations": len(reference[(sequence, position)]),
                    "source_relations": len(source),
                    "consolidated_relations": len(consolidated),
                    **comparison,
                    "source_unchanged_in_memory": unchanged_in_memory,
                    "source_unchanged_after_reload": unchanged_after_reload,
                }
            )
            previous_histories = json.loads(json.dumps(current_histories))
            previous_position = position
        if position % 10 == 0 or position == len(order):
            print(f"{sequence}_worlds_completed={position}/{len(order)}", flush=True)
    final_memory = SemanticMemory(memory_path)
    final_memory.load()
    history_rows = []
    relations = final_memory.passive_mcm_neighborhood_consolidation_relations()
    for relation in relations.values():
        record = dict(relation or {})
        pair_key = "|".join(sorted((str(record["left_node"]), str(record["right_node"]))))
        for entry in list(record.get("history", []) or []):
            history_rows.append(
                {
                    "sequence": sequence,
                    "pair_key": pair_key,
                    "neighborhood_symbol": record["neighborhood_symbol"],
                    "checkpoint_index": entry["checkpoint_index"],
                    "checkpoint_label": entry["checkpoint_label"],
                    "run_index": entry["run_index"],
                    "pareto_depth": entry["pareto_depth"],
                    "max_pareto_depth": entry["max_pareto_depth"],
                    "normalized_depth": entry["normalized_depth"],
                    "world_pair_count": entry["world_pair_count"],
                    "world_count": entry["world_count"],
                    "growth_seen_count": entry["growth_seen_count"],
                }
            )
    return {
        "checkpoints": checkpoint_rows,
        "equivalence": equivalence_rows,
        "continuity": continuity_rows,
        "histories": history_rows,
        "snapshots": snapshots,
        "profile": final_memory.passive_mcm_neighborhood_consolidation_profile(),
        "consolidation_document_bytes": len(
            json.dumps(
                final_memory.data["passive_mcm_neighborhood_consolidation"],
                indent=2,
                sort_keys=True,
            ).encode("utf-8")
        ),
        "memory_size_bytes": memory_path.stat().st_size,
    }


def _rank_map(values: dict[str, int]) -> dict[str, float]:
    ordered = sorted(values.items(), key=lambda item: (item[1], item[0]))
    ranks: dict[str, float] = {}
    index = 0
    while index < len(ordered):
        end = index + 1
        while end < len(ordered) and ordered[end][1] == ordered[index][1]:
            end += 1
        rank = ((index + 1) + end) / 2.0
        for offset in range(index, end):
            ranks[ordered[offset][0]] = rank
        index = end
    return ranks


def _spearman(left: dict[str, dict], right: dict[str, dict], shared: list[str]) -> float:
    left_ranks = _rank_map({key: int(left[key]["pareto_depth"]) for key in shared})
    right_ranks = _rank_map({key: int(right[key]["pareto_depth"]) for key in shared})
    left_mean = sum(left_ranks.values()) / max(1, len(shared))
    right_mean = sum(right_ranks.values()) / max(1, len(shared))
    numerator = sum(
        (left_ranks[key] - left_mean) * (right_ranks[key] - right_mean)
        for key in shared
    )
    left_scale = math.sqrt(sum((left_ranks[key] - left_mean) ** 2 for key in shared))
    right_scale = math.sqrt(sum((right_ranks[key] - right_mean) ** 2 for key in shared))
    return numerator / max(1e-12, left_scale * right_scale)


def _order_rows(results: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for position in CHECKPOINTS:
        forward = results["forward"]["snapshots"][position]
        reverse = results["reverse"]["snapshots"][position]
        shared = sorted(set(forward) & set(reverse))
        union = set(forward) | set(reverse)
        forward_top = {key for key, row in forward.items() if int(row["pareto_depth"]) == 1}
        reverse_top = {key for key, row in reverse.items() if int(row["pareto_depth"]) == 1}
        rows.append(
            {
                "position": position,
                "forward_relations": len(forward),
                "reverse_relations": len(reverse),
                "shared_relations": len(shared),
                "relation_jaccard": len(shared) / max(1, len(union)),
                "shared_depth_spearman": _spearman(forward, reverse, shared),
                "forward_layer_one": len(forward_top),
                "reverse_layer_one": len(reverse_top),
                "shared_layer_one": len(forward_top & reverse_top),
                "layer_one_jaccard": len(forward_top & reverse_top)
                / max(1, len(forward_top | reverse_top)),
            }
        )
    return rows


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        if not rows:
            return
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    specs = _world_specs()
    if len(specs) != 81:
        raise RuntimeError(f"expected 81 worlds, found {len(specs)}")
    reference = _read_reference()
    baselines = _read_baseline_sizes()
    _clean_local_state()
    try:
        _prepare_worlds(specs)
        results: dict[str, dict[str, object]] = {}
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = {
                executor.submit(_run_sequence, sequence, specs, reference): sequence
                for sequence in ("forward", "reverse")
            }
            for future in as_completed(futures):
                results[futures[future]] = future.result()
        checkpoint_rows = results["forward"]["checkpoints"] + results["reverse"]["checkpoints"]
        equivalence_rows = results["forward"]["equivalence"] + results["reverse"]["equivalence"]
        continuity_rows = results["forward"]["continuity"] + results["reverse"]["continuity"]
        history_rows = results["forward"]["histories"] + results["reverse"]["histories"]
        order_rows = _order_rows(results)
        summary_rows = []
        for sequence in ("forward", "reverse"):
            size = int(results[sequence]["memory_size_bytes"])
            baseline = baselines[sequence]
            profile = results[sequence]["profile"]
            sequence_equivalence = [
                row for row in equivalence_rows if row["sequence"] == sequence
            ]
            sequence_continuity = [
                row for row in continuity_rows if row["sequence"] == sequence
            ]
            summary_rows.append(
                {
                    "sequence": sequence,
                    "worlds": len(specs),
                    "checkpoints": profile["checkpoints"],
                    "final_relations": profile["relations"],
                    "history_entries": profile["history_entries"],
                    "storage_format": profile["format"],
                    "all_checkpoints_exact_2081": int(
                        all(int(row["all_exact"]) == 1 for row in sequence_equivalence)
                    ),
                    "all_sources_unchanged": int(
                        all(
                            int(row["source_unchanged_in_memory"]) == 1
                            and int(row["source_unchanged_after_reload"]) == 1
                            for row in sequence_equivalence
                        )
                    ),
                    "all_history_prefixes_preserved": int(
                        all(int(row["history_prefix_preserved"]) == 1 for row in sequence_continuity)
                    ),
                    "memory_size_bytes": size,
                    "consolidation_document_bytes": results[sequence][
                        "consolidation_document_bytes"
                    ],
                    "2081_baseline_memory_size_bytes": baseline,
                    "consolidation_overhead_bytes": size - baseline,
                    "consolidation_overhead_percent": ((size - baseline) / baseline) * 100.0,
                    "passive_only": profile["passive_only"],
                    "offline_only": profile["offline_only"],
                    "read_by_mini_dio": profile["read_by_mini_dio"],
                    "influences_field": profile["influences_field"],
                    "influences_action": profile["influences_action"],
                    "deletes_memory": profile["deletes_memory"],
                    "dampens_memory": profile["dampens_memory"],
                }
            )
        _write_csv("checkpoints", checkpoint_rows)
        _write_csv("equivalence", equivalence_rows)
        _write_csv("continuity", continuity_rows)
        _write_csv("histories", history_rows)
        _write_csv("order", order_rows)
        _write_csv("summary", summary_rows)
        if not all(
            int(row["all_checkpoints_exact_2081"]) == 1
            and int(row["all_sources_unchanged"]) == 1
            and int(row["all_history_prefixes_preserved"]) == 1
            for row in summary_rows
        ):
            raise RuntimeError("offline consolidation boundary or equivalence failed")
        print(f"checkpoint_rows={len(checkpoint_rows)}")
        print(f"history_rows={len(history_rows)}")
        print(f"order_rows={len(order_rows)}")
        return 0
    finally:
        _clean_local_state()


if __name__ == "__main__":
    raise SystemExit(main())
