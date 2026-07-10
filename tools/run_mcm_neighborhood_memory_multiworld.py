from __future__ import annotations

import csv
import json
import shutil
import subprocess
import sys
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "data" / "generated" / "2079_mcm_neighborhood_memory"
MEMORY_DIR = ROOT / "memory"
DEBUG_ROOT = ROOT / "debug" / "2079_mcm_neighborhood_memory"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
GROWTH_CSV = FINDING_DIR / "2079_PASSIVE_WACHSENDE_MCM_NACHBARSCHAFTS_MEMORY.growth.csv"
SUMMARY_CSV = FINDING_DIR / "2079_PASSIVE_WACHSENDE_MCM_NACHBARSCHAFTS_MEMORY.summary.csv"
COMPARISON_CSV = FINDING_DIR / "2079_PASSIVE_WACHSENDE_MCM_NACHBARSCHAFTS_MEMORY.comparison.csv"
TOP_CSV = FINDING_DIR / "2079_PASSIVE_WACHSENDE_MCM_NACHBARSCHAFTS_MEMORY.top.csv"
OFFLINE_LINK_CSV = (
    FINDING_DIR / "2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.links.csv"
)


@dataclass(frozen=True)
class WorldSpec:
    index: int
    world_id: str
    corpus: str
    variant: str
    archive: Path
    member: str

    @property
    def extracted_path(self) -> Path:
        return GENERATED_DIR / f"{self.index:03d}.csv"


def _variant(member: str) -> str:
    if "_shuffle_order_" in member:
        return "shuffle"
    if "_random_sign_" in member:
        return "random_sign"
    return "real"


def _world_specs() -> list[WorldSpec]:
    archives = (
        ("follow_2025_1h", ROOT / "data" / "2070_role_family_followworlds.zip"),
        ("null_2025_1h", ROOT / "data" / "2073_role_family_null_controls.zip"),
        ("holdout_2024", ROOT / "data" / "2074_rf05_crossyear_timeframe_holdout.zip"),
    )
    pending: list[tuple[str, Path, str]] = []
    for corpus, archive_path in archives:
        with zipfile.ZipFile(archive_path) as archive:
            for member in sorted(archive.namelist()):
                if member.lower().endswith(".csv") and Path(member).name.lower() != "manifest.csv":
                    pending.append((corpus, archive_path, member))
    return [
        WorldSpec(
            index=index,
            world_id=f"W2079_{index:03d}",
            corpus=corpus,
            variant=_variant(member),
            archive=archive,
            member=member,
        )
        for index, (corpus, archive, member) in enumerate(pending, start=1)
    ]


def _memory_path(sequence: str) -> Path:
    return MEMORY_DIR / f"topology_2079_{sequence}.json"


def _clean_local_state(specs: list[WorldSpec]) -> None:
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


def _layer(memory: dict) -> dict:
    return dict(memory.get("passive_mcm_neighborhood_memory", {}) or {})


def _profile(memory: dict) -> dict[str, int]:
    layer = _layer(memory)
    neighborhoods = dict(layer.get("neighborhoods", {}) or {})
    active = [
        record for record in neighborhoods.values() if int(record.get("active", 0) or 0) == 1
    ]
    return {
        "world_profiles": len(dict(layer.get("world_profiles", {}) or {})),
        "episode_observations": int(layer.get("episode_observations", 0) or 0),
        "active_neighborhoods": len(active),
        "historical_neighborhoods": len(neighborhoods),
        "active_three_scope_neighborhoods": sum(
            1 for record in active if int(record.get("current_scope_count", 0) or 0) == 3
        ),
        "active_world_pair_observations": sum(
            int(record.get("current_world_pair_count", 0) or 0) for record in active
        ),
    }


def _run_sequence(
    sequence: str, specs: list[WorldSpec]
) -> tuple[str, dict, list[dict[str, object]], int]:
    memory_path = _memory_path(sequence)
    debug_root = DEBUG_ROOT / sequence
    order = specs if sequence == "forward" else list(reversed(specs))
    growth_rows: list[dict[str, object]] = []
    final_memory: dict = {}
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
        final_memory = json.loads(memory_path.read_text(encoding="utf-8"))
        current = _profile(final_memory)
        growth_rows.append(
            {
                "sequence": sequence,
                "position": position,
                "world_id": spec.world_id,
                "corpus": spec.corpus,
                "variant": spec.variant,
                **current,
            }
        )
        if position % 10 == 0 or position == len(order):
            print(f"{sequence}_worlds_completed={position}/{len(order)}", flush=True)
    return sequence, final_memory, growth_rows, memory_path.stat().st_size


def _active_records(memory: dict) -> dict[str, dict]:
    return {
        symbol: dict(record or {})
        for symbol, record in dict(_layer(memory).get("neighborhoods", {}) or {}).items()
        if int(dict(record or {}).get("active", 0) or 0) == 1
    }


def _offline_sets() -> tuple[set[str], set[str], set[str]]:
    all_links: set[str] = set()
    three_scope: set[str] = set()
    strict_core: set[str] = set()
    with OFFLINE_LINK_CSV.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            pair = "|".join(sorted((row["left_node"], row["right_node"])))
            all_links.add(pair)
            if int(row["scope_count"]) == 3:
                three_scope.add(pair)
            if (
                int(row["real_2025_all_scopes"]) > 0
                and int(row["real_crossyear_all_scopes"]) > 0
                and int(row["real_2024_all_scopes"]) > 0
            ):
                strict_core.add(pair)
    return all_links, three_scope, strict_core


def _pair_keys(records: dict[str, dict], *, three_scope: bool = False) -> set[str]:
    return {
        "|".join(sorted((str(record["left_node"]), str(record["right_node"]))))
        for record in records.values()
        if not three_scope or int(record.get("current_scope_count", 0) or 0) == 3
    }


def _comparison_row(scope: str, left_name: str, right_name: str, left: set, right: set) -> dict:
    union = left | right
    shared = left & right
    return {
        "scope": scope,
        "left": left_name,
        "right": right_name,
        "left_count": len(left),
        "right_count": len(right),
        "shared": len(shared),
        "jaccard": len(shared) / max(1, len(union)),
    }


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
    _clean_local_state(specs)
    try:
        _prepare_worlds(specs)
        results = {}
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = {
                executor.submit(_run_sequence, sequence, specs): sequence
                for sequence in ("forward", "reverse")
            }
            for future in as_completed(futures):
                sequence, memory, growth, size = future.result()
                results[sequence] = {
                    "memory": memory,
                    "growth": growth,
                    "memory_size_bytes": size,
                }

        growth_rows = results["forward"]["growth"] + results["reverse"]["growth"]
        records = {
            sequence: _active_records(results[sequence]["memory"])
            for sequence in ("forward", "reverse")
        }
        active_sets = {sequence: _pair_keys(records[sequence]) for sequence in records}
        three_scope_sets = {
            sequence: _pair_keys(records[sequence], three_scope=True) for sequence in records
        }
        offline_all, offline_three_scope, offline_strict_core = _offline_sets()

        summary_rows = []
        top_rows = []
        for sequence in ("forward", "reverse"):
            profile = _profile(results[sequence]["memory"])
            summary_rows.append(
                {
                    "sequence": sequence,
                    **profile,
                    "offline_all_links_present": len(active_sets[sequence] & offline_all),
                    "offline_three_scope_links_present": len(
                        three_scope_sets[sequence] & offline_three_scope
                    ),
                    "offline_strict_core_present": len(active_sets[sequence] & offline_strict_core),
                    "memory_size_bytes": results[sequence]["memory_size_bytes"],
                }
            )
            ranked = sorted(
                records[sequence].values(),
                key=lambda record: (
                    int(record.get("current_world_pair_count", 0) or 0),
                    int(record.get("current_scope_count", 0) or 0),
                    int(record.get("current_world_count", 0) or 0),
                    str(record.get("neighborhood_symbol", "")),
                ),
                reverse=True,
            )
            for rank, record in enumerate(ranked[:20], start=1):
                top_rows.append(
                    {
                        "sequence": sequence,
                        "rank": rank,
                        "neighborhood_symbol": record.get("neighborhood_symbol", ""),
                        "left_node": record.get("left_node", ""),
                        "right_node": record.get("right_node", ""),
                        "scope_count": record.get("current_scope_count", 0),
                        "world_pair_count": record.get("current_world_pair_count", 0),
                        "world_count": record.get("current_world_count", 0),
                        "growth_seen_count": record.get("growth_seen_count", 0),
                        "peak_world_pair_count": record.get("peak_world_pair_count", 0),
                    }
                )

        comparison_rows = [
            _comparison_row(
                "active_online",
                "forward",
                "reverse",
                active_sets["forward"],
                active_sets["reverse"],
            ),
            _comparison_row(
                "three_scope_online",
                "forward",
                "reverse",
                three_scope_sets["forward"],
                three_scope_sets["reverse"],
            ),
            _comparison_row(
                "active_vs_2078",
                "forward",
                "offline_2078",
                active_sets["forward"],
                offline_all,
            ),
            _comparison_row(
                "active_vs_2078",
                "reverse",
                "offline_2078",
                active_sets["reverse"],
                offline_all,
            ),
            _comparison_row(
                "three_scope_vs_2078",
                "forward",
                "offline_2078",
                three_scope_sets["forward"],
                offline_three_scope,
            ),
            _comparison_row(
                "three_scope_vs_2078",
                "reverse",
                "offline_2078",
                three_scope_sets["reverse"],
                offline_three_scope,
            ),
        ]
        strict_forward = active_sets["forward"] & offline_strict_core
        strict_reverse = active_sets["reverse"] & offline_strict_core
        comparison_rows.append(
            _comparison_row(
                "offline_strict_core_presence",
                "forward",
                "reverse",
                strict_forward,
                strict_reverse,
            )
        )

        _write_csv(GROWTH_CSV, growth_rows)
        _write_csv(SUMMARY_CSV, summary_rows)
        _write_csv(COMPARISON_CSV, comparison_rows)
        _write_csv(TOP_CSV, top_rows)
        print(f"growth_rows={len(growth_rows)}")
        print(f"summary_rows={len(summary_rows)}")
        print(f"comparison_rows={len(comparison_rows)}")
        print(f"top_rows={len(top_rows)}")
        return 0
    finally:
        _clean_local_state(specs)


if __name__ == "__main__":
    raise SystemExit(main())
