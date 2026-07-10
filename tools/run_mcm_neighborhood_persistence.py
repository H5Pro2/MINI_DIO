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
GENERATED_DIR = ROOT / "data" / "generated" / "2080_mcm_neighborhood_persistence"
MEMORY_DIR = ROOT / "memory"
DEBUG_ROOT = ROOT / "debug" / "2080_mcm_neighborhood_persistence"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
RELATION_CSV = FINDING_DIR / "2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.relations.csv"
GROUP_CSV = FINDING_DIR / "2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.groups.csv"
SEPARATION_CSV = FINDING_DIR / "2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.separation.csv"
ORDER_CSV = FINDING_DIR / "2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.order.csv"
SUMMARY_CSV = FINDING_DIR / "2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.summary.csv"
PARETO_CSV = FINDING_DIR / "2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.pareto.csv"
OFFLINE_LINK_CSV = (
    FINDING_DIR / "2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.links.csv"
)

METRICS = (
    "world_pair_count",
    "world_count",
    "growth_seen_count",
    "scope_count",
    "scope_balance",
    "pair_density",
    "confirmation_ratio",
    "recency_score",
)
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
        WorldSpec(index, f"W2080_{index:03d}", archive, member)
        for index, (archive, member) in enumerate(pending, start=1)
    ]


def _memory_path(sequence: str) -> Path:
    return MEMORY_DIR / f"topology_2080_{sequence}.json"


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


def _run_sequence(sequence: str, specs: list[WorldSpec]) -> tuple[str, dict, int]:
    memory_path = _memory_path(sequence)
    debug_root = DEBUG_ROOT / sequence
    order = specs if sequence == "forward" else list(reversed(specs))
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
        if position % 10 == 0 or position == len(order):
            print(f"{sequence}_worlds_completed={position}/{len(order)}", flush=True)
    memory = json.loads(memory_path.read_text(encoding="utf-8"))
    return sequence, memory, memory_path.stat().st_size


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


def _relation_rows(sequence: str, memory: dict, strict_core: set[str]) -> list[dict[str, object]]:
    layer = dict(memory.get("passive_mcm_neighborhood_memory", {}) or {})
    finalization_count = int(layer.get("finalization_count", 0) or 0)
    rows = []
    for record in dict(layer.get("neighborhoods", {}) or {}).values():
        if int(record.get("active", 0) or 0) != 1:
            continue
        pair_key = "|".join(sorted((str(record["left_node"]), str(record["right_node"]))))
        scope_support = {
            key: int(value or 0)
            for key, value in dict(record.get("current_scope_support", {}) or {}).items()
        }
        support_values = [value for value in scope_support.values() if value > 0]
        world_pair_count = int(record.get("current_world_pair_count", 0) or 0)
        world_count = int(record.get("current_world_count", 0) or 0)
        growth_seen_count = int(record.get("growth_seen_count", 0) or 0)
        first_run = int(record.get("first_run", 0) or 0)
        last_finalization = int(record.get("last_finalization", 0) or 0)
        age = max(1, finalization_count - first_run + 1)
        silence = max(0, finalization_count - last_finalization)
        possible_pairs = max(1, world_count * (world_count - 1) // 2)
        rows.append(
            {
                "sequence": sequence,
                "pair_key": pair_key,
                "left_node": record["left_node"],
                "right_node": record["right_node"],
                "strict_2078_core": int(pair_key in strict_core),
                "world_pair_count": world_pair_count,
                "world_count": world_count,
                "growth_seen_count": growth_seen_count,
                "scope_count": int(record.get("current_scope_count", 0) or 0),
                "scope_balance": min(support_values) / max(support_values) if support_values else 0.0,
                "pair_density": world_pair_count / possible_pairs,
                "age_finalizations": age,
                "silence_finalizations": silence,
                "confirmation_ratio": growth_seen_count / age,
                "recency_score": 1.0 / (1.0 + silence),
                "core_scope_support": scope_support.get("field_core_raw", 0),
                "full_scope_support": scope_support.get("field_full_raw", 0),
                "duration_scope_support": scope_support.get(
                    "field_full_plus_duration_standardized", 0
                ),
            }
        )
    rows.sort(key=lambda row: str(row["pair_key"]))
    return rows


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


def _group_rows(relation_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for sequence in ("forward", "reverse"):
        sequence_rows = [row for row in relation_rows if row["sequence"] == sequence]
        for group_name, group_value in (("strict_core", 1), ("periphery", 0)):
            group = [row for row in sequence_rows if int(row["strict_2078_core"]) == group_value]
            for metric in METRICS:
                values = [float(row[metric]) for row in group]
                rows.append(
                    {
                        "sequence": sequence,
                        "group": group_name,
                        "metric": metric,
                        "count": len(values),
                        "minimum": min(values) if values else 0.0,
                        "p25": _quantile(values, 0.25),
                        "median": _quantile(values, 0.5),
                        "p75": _quantile(values, 0.75),
                        "maximum": max(values) if values else 0.0,
                        "mean": sum(values) / max(1, len(values)),
                    }
                )
    return rows


def _auc(core: list[float], periphery: list[float]) -> float:
    wins = 0.0
    for core_value in core:
        for peripheral_value in periphery:
            if core_value > peripheral_value:
                wins += 1.0
            elif core_value == peripheral_value:
                wins += 0.5
    return wins / max(1, len(core) * len(periphery))


def _separation_rows(relation_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for sequence in ("forward", "reverse"):
        sequence_rows = [row for row in relation_rows if row["sequence"] == sequence]
        core_rows = [row for row in sequence_rows if int(row["strict_2078_core"]) == 1]
        peripheral_rows = [row for row in sequence_rows if int(row["strict_2078_core"]) == 0]
        for metric in METRICS:
            core = [float(row[metric]) for row in core_rows]
            periphery = [float(row[metric]) for row in peripheral_rows]
            peripheral_p75 = _quantile(periphery, 0.75)
            rows.append(
                {
                    "sequence": sequence,
                    "metric": metric,
                    "auc_core_over_periphery": _auc(core, periphery),
                    "minimum_core": min(core),
                    "maximum_periphery": max(periphery),
                    "clean_separation": int(min(core) > max(periphery)),
                    "core_above_periphery_p75": sum(value > peripheral_p75 for value in core),
                    "core_count": len(core),
                }
            )
    return rows


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


def _order_rows(relation_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_sequence = {
        sequence: {
            str(row["pair_key"]): row
            for row in relation_rows
            if row["sequence"] == sequence
        }
        for sequence in ("forward", "reverse")
    }
    shared = sorted(set(by_sequence["forward"]) & set(by_sequence["reverse"]))
    rows = []
    for metric in METRICS:
        forward_values = {
            pair: float(by_sequence["forward"][pair][metric]) for pair in shared
        }
        reverse_values = {
            pair: float(by_sequence["reverse"][pair][metric]) for pair in shared
        }
        forward_ranks = _rank_map(forward_values)
        reverse_ranks = _rank_map(reverse_values)
        rows.append(
            {
                "metric": metric,
                "shared_relations": len(shared),
                "pearson": _correlation(
                    [forward_values[pair] for pair in shared],
                    [reverse_values[pair] for pair in shared],
                ),
                "spearman": _correlation(
                    [forward_ranks[pair] for pair in shared],
                    [reverse_ranks[pair] for pair in shared],
                ),
            }
        )
    return rows


def _dominates(left: dict[str, object], right: dict[str, object]) -> bool:
    left_values = [float(left[metric]) for metric in SUPPORT_AXES]
    right_values = [float(right[metric]) for metric in SUPPORT_AXES]
    return all(
        left_values[index] >= right_values[index] for index in range(len(SUPPORT_AXES))
    ) and any(
        left_values[index] > right_values[index] for index in range(len(SUPPORT_AXES))
    )


def _pareto_rows(relation_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for sequence in ("forward", "reverse"):
        sequence_rows = [row for row in relation_rows if row["sequence"] == sequence]
        core = [row for row in sequence_rows if int(row["strict_2078_core"]) == 1]
        periphery = [row for row in sequence_rows if int(row["strict_2078_core"]) == 0]
        for relation in core:
            dominated = sum(_dominates(relation, other) for other in periphery)
            dominating = sum(_dominates(other, relation) for other in periphery)
            rows.append(
                {
                    "sequence": sequence,
                    "pair_key": relation["pair_key"],
                    "world_pair_count": relation["world_pair_count"],
                    "world_count": relation["world_count"],
                    "growth_seen_count": relation["growth_seen_count"],
                    "dominated_periphery": dominated,
                    "dominating_periphery": dominating,
                    "incomparable_periphery": len(periphery) - dominated - dominating,
                    "dominated_periphery_ratio": dominated / max(1, len(periphery)),
                    "undominated_by_periphery": int(dominating == 0),
                }
            )
    return rows


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
    _clean_local_state()
    try:
        _prepare_worlds(specs)
        results = {}
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = {
                executor.submit(_run_sequence, sequence, specs): sequence
                for sequence in ("forward", "reverse")
            }
            for future in as_completed(futures):
                sequence, memory, size = future.result()
                results[sequence] = {"memory": memory, "memory_size_bytes": size}

        strict_core = _strict_core()
        relation_rows = []
        summary_rows = []
        for sequence in ("forward", "reverse"):
            rows = _relation_rows(sequence, results[sequence]["memory"], strict_core)
            relation_rows.extend(rows)
            summary_rows.append(
                {
                    "sequence": sequence,
                    "relations": len(rows),
                    "strict_core_present": sum(int(row["strict_2078_core"]) for row in rows),
                    "three_scope_relations": sum(int(row["scope_count"]) == 3 for row in rows),
                    "memory_size_bytes": results[sequence]["memory_size_bytes"],
                }
            )

        _write_csv(RELATION_CSV, relation_rows)
        _write_csv(GROUP_CSV, _group_rows(relation_rows))
        _write_csv(SEPARATION_CSV, _separation_rows(relation_rows))
        _write_csv(ORDER_CSV, _order_rows(relation_rows))
        _write_csv(SUMMARY_CSV, summary_rows)
        _write_csv(PARETO_CSV, _pareto_rows(relation_rows))
        print(f"relation_rows={len(relation_rows)}")
        print(f"group_rows={len(_group_rows(relation_rows))}")
        print(f"separation_rows={len(_separation_rows(relation_rows))}")
        print(f"order_rows={len(_order_rows(relation_rows))}")
        print(f"pareto_rows={len(_pareto_rows(relation_rows))}")
        return 0
    finally:
        _clean_local_state()


def analyze_existing_outputs() -> int:
    with RELATION_CSV.open(newline="", encoding="utf-8") as handle:
        relation_rows = list(csv.DictReader(handle))
    _write_csv(PARETO_CSV, _pareto_rows(relation_rows))
    print(f"pareto_rows={len(_pareto_rows(relation_rows))}")
    return 0


if __name__ == "__main__":
    if "--analyze-existing" in sys.argv:
        raise SystemExit(analyze_existing_outputs())
    raise SystemExit(main())
