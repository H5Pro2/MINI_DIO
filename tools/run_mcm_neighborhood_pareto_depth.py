from __future__ import annotations

import csv
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
GENERATED_DIR = ROOT / "data" / "generated" / "2081_mcm_neighborhood_pareto_depth"
MEMORY_DIR = ROOT / "memory"
DEBUG_ROOT = ROOT / "debug" / "2081_mcm_neighborhood_pareto_depth"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
SNAPSHOT_CSV = FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.snapshots.csv"
LAYER_CSV = FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.layers.csv"
MIGRATION_CSV = FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.migration.csv"
ORDER_CSV = FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.order.csv"
CORE_CSV = FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.core.csv"
SUMMARY_CSV = FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.summary.csv"
OFFLINE_LINK_CSV = (
    FINDING_DIR / "2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.links.csv"
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
        WorldSpec(index, f"W2081_{index:03d}", archive, member)
        for index, (archive, member) in enumerate(pending, start=1)
    ]


def _memory_path(sequence: str) -> Path:
    return MEMORY_DIR / f"topology_2081_{sequence}.json"


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


def _strict_core() -> set[str]:
    core = set()
    with OFFLINE_LINK_CSV.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if (
                int(row["real_2025_all_scopes"]) > 0
                and int(row["real_crossyear_all_scopes"]) > 0
                and int(row["real_2024_all_scopes"]) > 0
            ):
                core.add("|".join(sorted((row["left_node"], row["right_node"]))))
    return core


def _dominates(left: dict[str, object], right: dict[str, object]) -> bool:
    left_values = [int(left[axis]) for axis in SUPPORT_AXES]
    right_values = [int(right[axis]) for axis in SUPPORT_AXES]
    return all(
        left_values[index] >= right_values[index] for index in range(len(SUPPORT_AXES))
    ) and any(
        left_values[index] > right_values[index] for index in range(len(SUPPORT_AXES))
    )


def _pareto_depths(rows: list[dict[str, object]]) -> dict[str, int]:
    count = len(rows)
    dominated_by_count = [0] * count
    dominates: list[list[int]] = [[] for _ in rows]
    for left_index in range(count):
        for right_index in range(left_index + 1, count):
            if _dominates(rows[left_index], rows[right_index]):
                dominates[left_index].append(right_index)
                dominated_by_count[right_index] += 1
            elif _dominates(rows[right_index], rows[left_index]):
                dominates[right_index].append(left_index)
                dominated_by_count[left_index] += 1

    front = [index for index, value in enumerate(dominated_by_count) if value == 0]
    depths: dict[str, int] = {}
    depth = 1
    assigned = 0
    while front:
        next_front = []
        for index in front:
            depths[str(rows[index]["pair_key"])] = depth
            assigned += 1
            for dominated_index in dominates[index]:
                dominated_by_count[dominated_index] -= 1
                if dominated_by_count[dominated_index] == 0:
                    next_front.append(dominated_index)
        front = next_front
        depth += 1
    if assigned != count:
        raise RuntimeError(f"Pareto depth assignment incomplete: {assigned}/{count}")
    return depths


def _snapshot_rows(
    sequence: str,
    position: int,
    memory: dict,
    strict_core: set[str],
) -> list[dict[str, object]]:
    layer = dict(memory.get("passive_mcm_neighborhood_memory", {}) or {})
    rows = []
    for record in dict(layer.get("neighborhoods", {}) or {}).values():
        if int(record.get("active", 0) or 0) != 1:
            continue
        pair_key = "|".join(sorted((str(record["left_node"]), str(record["right_node"]))))
        rows.append(
            {
                "sequence": sequence,
                "position": position,
                "pair_key": pair_key,
                "strict_2078_core": int(pair_key in strict_core),
                "world_pair_count": int(record.get("current_world_pair_count", 0) or 0),
                "world_count": int(record.get("current_world_count", 0) or 0),
                "growth_seen_count": int(record.get("growth_seen_count", 0) or 0),
            }
        )
    rows.sort(key=lambda row: str(row["pair_key"]))
    depths = _pareto_depths(rows)
    max_depth = max(depths.values(), default=1)
    for row in rows:
        depth = depths[str(row["pair_key"])]
        row["pareto_depth"] = depth
        row["normalized_depth"] = (depth - 1) / max(1, max_depth - 1)
    return rows


def _run_sequence(
    sequence: str, specs: list[WorldSpec], strict_core: set[str]
) -> tuple[str, list[dict[str, object]], int]:
    memory_path = _memory_path(sequence)
    debug_root = DEBUG_ROOT / sequence
    order = specs if sequence == "forward" else list(reversed(specs))
    snapshots = []
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
            memory = json.loads(memory_path.read_text(encoding="utf-8"))
            snapshots.extend(_snapshot_rows(sequence, position, memory, strict_core))
        if position % 10 == 0 or position == len(order):
            print(f"{sequence}_worlds_completed={position}/{len(order)}", flush=True)
    return sequence, snapshots, memory_path.stat().st_size


def _quantile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return 0.0
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def _rank_map(values: dict[str, float]) -> dict[str, float]:
    ordered = sorted(values.items(), key=lambda item: (item[1], item[0]))
    ranks: dict[str, float] = {}
    index = 0
    while index < len(ordered):
        end = index + 1
        while end < len(ordered) and ordered[end][1] == ordered[index][1]:
            end += 1
        rank = ((index + 1) + end) / 2.0
        for position in range(index, end):
            ranks[ordered[position][0]] = rank
        index = end
    return ranks


def _correlation(left: list[float], right: list[float]) -> float:
    if not left or len(left) != len(right):
        return 0.0
    left_mean = sum(left) / len(left)
    right_mean = sum(right) / len(right)
    numerator = sum(
        (left[index] - left_mean) * (right[index] - right_mean)
        for index in range(len(left))
    )
    left_scale = math.sqrt(sum((value - left_mean) ** 2 for value in left))
    right_scale = math.sqrt(sum((value - right_mean) ** 2 for value in right))
    return numerator / max(1e-12, left_scale * right_scale)


def _spearman(left: dict[str, float], right: dict[str, float], shared: list[str]) -> float:
    left_ranks = _rank_map({key: left[key] for key in shared})
    right_ranks = _rank_map({key: right[key] for key in shared})
    return _correlation(
        [left_ranks[key] for key in shared],
        [right_ranks[key] for key in shared],
    )


def _by_checkpoint(snapshot_rows: list[dict[str, object]]) -> dict[tuple[str, int], dict[str, dict]]:
    out: dict[tuple[str, int], dict[str, dict]] = {}
    for row in snapshot_rows:
        key = (str(row["sequence"]), int(row["position"]))
        out.setdefault(key, {})[str(row["pair_key"])] = row
    return out


def _layer_rows(snapshot_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    checkpoints = _by_checkpoint(snapshot_rows)
    rows = []
    for (sequence, position), records in sorted(checkpoints.items()):
        max_depth = max(int(row["pareto_depth"]) for row in records.values())
        for depth in range(1, max_depth + 1):
            layer = [row for row in records.values() if int(row["pareto_depth"]) == depth]
            rows.append(
                {
                    "sequence": sequence,
                    "position": position,
                    "pareto_depth": depth,
                    "relations": len(layer),
                    "strict_core_relations": sum(int(row["strict_2078_core"]) for row in layer),
                }
            )
    return rows


def _depth_auc(core_depths: list[int], peripheral_depths: list[int]) -> float:
    wins = 0.0
    for core_depth in core_depths:
        for peripheral_depth in peripheral_depths:
            if core_depth < peripheral_depth:
                wins += 1.0
            elif core_depth == peripheral_depth:
                wins += 0.5
    return wins / max(1, len(core_depths) * len(peripheral_depths))


def _summary_rows(snapshot_rows: list[dict[str, object]], sizes: dict[str, int]) -> list[dict[str, object]]:
    checkpoints = _by_checkpoint(snapshot_rows)
    rows = []
    for (sequence, position), records in sorted(checkpoints.items()):
        core_depths = [
            int(row["pareto_depth"])
            for row in records.values()
            if int(row["strict_2078_core"]) == 1
        ]
        peripheral_depths = [
            int(row["pareto_depth"])
            for row in records.values()
            if int(row["strict_2078_core"]) == 0
        ]
        max_depth = max(int(row["pareto_depth"]) for row in records.values())
        core_normalized = [
            (depth - 1) / max(1, max_depth - 1) for depth in core_depths
        ]
        peripheral_normalized = [
            (depth - 1) / max(1, max_depth - 1) for depth in peripheral_depths
        ]
        rows.append(
            {
                "sequence": sequence,
                "position": position,
                "relations": len(records),
                "max_pareto_depth": max_depth,
                "layer_one_relations": sum(int(row["pareto_depth"]) == 1 for row in records.values()),
                "strict_core_present": len(core_depths),
                "strict_core_layer_one": sum(depth == 1 for depth in core_depths),
                "median_core_depth": _quantile([float(value) for value in core_depths], 0.5),
                "median_periphery_depth": _quantile(
                    [float(value) for value in peripheral_depths], 0.5
                ),
                "median_core_normalized_depth": _quantile(core_normalized, 0.5),
                "median_periphery_normalized_depth": _quantile(
                    peripheral_normalized, 0.5
                ),
                "auc_core_shallower": _depth_auc(core_depths, peripheral_depths),
                "maximum_core_depth": max(core_depths) if core_depths else 0,
                "minimum_periphery_depth": min(peripheral_depths) if peripheral_depths else 0,
                "clean_depth_separation": int(
                    bool(core_depths)
                    and bool(peripheral_depths)
                    and max(core_depths) < min(peripheral_depths)
                ),
                "memory_size_bytes": sizes[sequence] if position == CHECKPOINTS[-1] else "",
            }
        )
    return rows


def _migration_rows(snapshot_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    checkpoints = _by_checkpoint(snapshot_rows)
    rows = []
    for sequence in ("forward", "reverse"):
        for left_position, right_position in zip(CHECKPOINTS, CHECKPOINTS[1:]):
            left = checkpoints[(sequence, left_position)]
            right = checkpoints[(sequence, right_position)]
            shared = sorted(set(left) & set(right))
            left_depth = {key: float(left[key]["pareto_depth"]) for key in shared}
            right_depth = {key: float(right[key]["pareto_depth"]) for key in shared}
            left_normalized = {key: float(left[key]["normalized_depth"]) for key in shared}
            right_normalized = {key: float(right[key]["normalized_depth"]) for key in shared}
            rows.append(
                {
                    "sequence": sequence,
                    "from_position": left_position,
                    "to_position": right_position,
                    "shared_relations": len(shared),
                    "depth_spearman": _spearman(left_depth, right_depth, shared),
                    "normalized_depth_spearman": _spearman(
                        left_normalized, right_normalized, shared
                    ),
                    "same_depth": sum(left_depth[key] == right_depth[key] for key in shared),
                    "mean_absolute_normalized_change": sum(
                        abs(left_normalized[key] - right_normalized[key]) for key in shared
                    )
                    / max(1, len(shared)),
                }
            )
    return rows


def _order_rows(snapshot_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    checkpoints = _by_checkpoint(snapshot_rows)
    rows = []
    for position in CHECKPOINTS:
        forward = checkpoints[("forward", position)]
        reverse = checkpoints[("reverse", position)]
        shared = sorted(set(forward) & set(reverse))
        union = set(forward) | set(reverse)
        forward_depth = {key: float(forward[key]["pareto_depth"]) for key in shared}
        reverse_depth = {key: float(reverse[key]["pareto_depth"]) for key in shared}
        forward_top = {key for key, row in forward.items() if int(row["pareto_depth"]) == 1}
        reverse_top = {key for key, row in reverse.items() if int(row["pareto_depth"]) == 1}
        rows.append(
            {
                "position": position,
                "forward_relations": len(forward),
                "reverse_relations": len(reverse),
                "shared_relations": len(shared),
                "relation_jaccard": len(shared) / max(1, len(union)),
                "shared_depth_spearman": _spearman(
                    forward_depth, reverse_depth, shared
                ),
                "forward_layer_one": len(forward_top),
                "reverse_layer_one": len(reverse_top),
                "shared_layer_one": len(forward_top & reverse_top),
                "layer_one_jaccard": len(forward_top & reverse_top)
                / max(1, len(forward_top | reverse_top)),
            }
        )
    return rows


def _core_rows(snapshot_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [row for row in snapshot_rows if int(row["strict_2078_core"]) == 1]


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
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
    strict_core = _strict_core()
    _clean_local_state()
    try:
        _prepare_worlds(specs)
        results = {}
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = {
                executor.submit(_run_sequence, sequence, specs, strict_core): sequence
                for sequence in ("forward", "reverse")
            }
            for future in as_completed(futures):
                sequence, snapshots, size = future.result()
                results[sequence] = {"snapshots": snapshots, "memory_size_bytes": size}
        snapshot_rows = results["forward"]["snapshots"] + results["reverse"]["snapshots"]
        sizes = {sequence: int(results[sequence]["memory_size_bytes"]) for sequence in results}
        _write_csv(SNAPSHOT_CSV, snapshot_rows)
        _write_csv(LAYER_CSV, _layer_rows(snapshot_rows))
        _write_csv(MIGRATION_CSV, _migration_rows(snapshot_rows))
        _write_csv(ORDER_CSV, _order_rows(snapshot_rows))
        _write_csv(CORE_CSV, _core_rows(snapshot_rows))
        _write_csv(SUMMARY_CSV, _summary_rows(snapshot_rows, sizes))
        print(f"snapshot_rows={len(snapshot_rows)}")
        print(f"layer_rows={len(_layer_rows(snapshot_rows))}")
        print(f"migration_rows={len(_migration_rows(snapshot_rows))}")
        print(f"order_rows={len(_order_rows(snapshot_rows))}")
        print(f"core_rows={len(_core_rows(snapshot_rows))}")
        return 0
    finally:
        _clean_local_state()


def analyze_existing_outputs() -> int:
    with SNAPSHOT_CSV.open(newline="", encoding="utf-8") as handle:
        snapshot_rows = list(csv.DictReader(handle))
    sizes = {"forward": 0, "reverse": 0}
    if SUMMARY_CSV.exists():
        with SUMMARY_CSV.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if int(row["position"]) == CHECKPOINTS[-1]:
                    sizes[row["sequence"]] = int(row.get("memory_size_bytes", 0) or 0)
    _write_csv(LAYER_CSV, _layer_rows(snapshot_rows))
    _write_csv(MIGRATION_CSV, _migration_rows(snapshot_rows))
    _write_csv(ORDER_CSV, _order_rows(snapshot_rows))
    _write_csv(CORE_CSV, _core_rows(snapshot_rows))
    _write_csv(SUMMARY_CSV, _summary_rows(snapshot_rows, sizes))
    print(f"snapshot_rows={len(snapshot_rows)}")
    return 0


if __name__ == "__main__":
    if "--analyze-existing" in sys.argv:
        raise SystemExit(analyze_existing_outputs())
    raise SystemExit(main())
