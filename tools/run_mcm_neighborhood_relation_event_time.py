from __future__ import annotations

import csv
import io
import json
import math
import shutil
import subprocess
import sys
import zipfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neighborhood_consolidation import pareto_depths
from mini_dio.mcm_neighborhood_event_memory import EVENT_FIELDS, EVENT_FORMAT, SCOPE_FIELDS
from mini_dio.semantic_memory import SemanticMemory


GENERATED_DIR = ROOT / "data" / "generated" / "2085_mcm_neighborhood_event_time"
DEBUG_ROOT = ROOT / "debug" / "2085_mcm_neighborhood_event_time"
MEMORY_DIR = ROOT / "memory"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2085_RELATIONSINTERNE_MCM_NACHBARSCHAFTS_EREIGNISZEIT"
EVENT_ARCHIVE = ROOT / "data" / "2085_mcm_neighborhood_event_histories.zip"
REFERENCE_SNAPSHOT = (
    FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.snapshots.csv"
)
REFERENCE_SUMMARY = (
    FINDING_DIR / "2081_DYNAMISCHE_MCM_NACHBARSCHAFT_PARETO_TIEFE.summary.csv"
)
SEQUENCES = ("forward", "reverse")


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
        WorldSpec(index, f"W2085_{index:03d}", archive, member)
        for index, (archive, member) in enumerate(pending, start=1)
    ]


def _memory_path(sequence: str) -> Path:
    return MEMORY_DIR / f"topology_2085_{sequence}.json"


def _clean_local_state() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    if DEBUG_ROOT.exists():
        shutil.rmtree(DEBUG_ROOT)
    for sequence in SEQUENCES:
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


def _reference_rows() -> dict[str, dict[str, dict[str, str]]]:
    out = {sequence: {} for sequence in SEQUENCES}
    with REFERENCE_SNAPSHOT.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if int(row["position"]) == 81:
                out[row["sequence"]][row["pair_key"]] = row
    return out


def _baseline_sizes() -> dict[str, int]:
    out = {}
    with REFERENCE_SUMMARY.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if int(row["position"]) == 81:
                out[row["sequence"]] = int(row["memory_size_bytes"])
    return out


def _source_rows(memory: SemanticMemory) -> dict[str, dict[str, object]]:
    layer = dict(memory.data.get("passive_mcm_neighborhood_memory", {}) or {})
    rows = []
    for symbol, raw_record in dict(layer.get("neighborhoods", {}) or {}).items():
        record = dict(raw_record or {})
        if int(record.get("active", 0) or 0) != 1:
            continue
        pair_key = "|".join(sorted((str(record["left_node"]), str(record["right_node"]))))
        rows.append(
            {
                "pair_key": pair_key,
                "neighborhood_symbol": str(
                    record.get("neighborhood_symbol", symbol) or symbol
                ),
                "world_pair_count": int(record.get("current_world_pair_count", 0) or 0),
                "world_count": int(record.get("current_world_count", 0) or 0),
                "growth_seen_count": int(record.get("growth_seen_count", 0) or 0),
                "last_finalization": int(record.get("last_finalization", 0) or 0),
                "scope_support": dict(record.get("current_scope_support", {}) or {}),
            }
        )
    depths = pareto_depths(rows)
    for row in rows:
        row["pareto_depth"] = depths[str(row["pair_key"])]
    return {str(row["pair_key"]): row for row in rows}


def _compare_reference(
    source: dict[str, dict[str, object]], reference: dict[str, dict[str, str]]
) -> dict[str, int]:
    shared = set(source) & set(reference)
    support_mismatches = sum(
        any(
            int(source[key][axis]) != int(reference[key][axis])
            for axis in ("world_pair_count", "world_count", "growth_seen_count")
        )
        for key in shared
    )
    depth_mismatches = sum(
        int(source[key]["pareto_depth"]) != int(reference[key]["pareto_depth"])
        for key in shared
    )
    exact_set = int(set(source) == set(reference))
    return {
        "exact_relation_set": exact_set,
        "support_mismatches": support_mismatches,
        "pareto_depth_mismatches": depth_mismatches,
        "field_exact_2081": int(
            exact_set == 1 and support_mismatches == 0 and depth_mismatches == 0
        ),
    }


def _event_rows(
    sequence: str,
    relations: dict[str, dict],
) -> list[dict[str, object]]:
    rows = []
    for relation in relations.values():
        pair_key = "|".join(sorted((relation["left_node"], relation["right_node"])))
        for event in relation["events"]:
            rows.append(
                {
                    "sequence": sequence,
                    "pair_key": pair_key,
                    "neighborhood_symbol": relation["neighborhood_symbol"],
                    "event_index": event["event_index"],
                    **{field: event[field] for field in EVENT_FIELDS},
                }
            )
    rows.sort(key=lambda row: (str(row["sequence"]), str(row["pair_key"]), int(row["event_index"])))
    return rows


def _event_integrity(
    source: dict[str, dict[str, object]], relations: dict[str, dict]
) -> dict[str, int]:
    event_by_pair = {
        "|".join(sorted((relation["left_node"], relation["right_node"]))): relation
        for relation in relations.values()
    }
    exact_set = int(set(source) == set(event_by_pair))
    shared = set(source) & set(event_by_pair)
    count_mismatches = 0
    final_state_mismatches = 0
    for pair_key in shared:
        source_record = source[pair_key]
        relation = event_by_pair[pair_key]
        if int(relation["total_growth_event_count"]) != int(
            source_record["growth_seen_count"]
        ):
            count_mismatches += 1
        latest = relation["events"][-1]
        expected = {
            "finalization_index": int(source_record["last_finalization"]),
            "world_pair_count": int(source_record["world_pair_count"]),
            "world_count": int(source_record["world_count"]),
            "growth_seen_count": int(source_record["growth_seen_count"]),
            **{
                scope: int(dict(source_record["scope_support"]).get(scope, 0) or 0)
                for scope in SCOPE_FIELDS
            },
        }
        if any(int(latest[field]) != value for field, value in expected.items()):
            final_state_mismatches += 1
    return {
        "exact_event_relation_set": exact_set,
        "event_count_mismatches": count_mismatches,
        "event_final_state_mismatches": final_state_mismatches,
        "event_integrity_exact": int(
            exact_set == 1 and count_mismatches == 0 and final_state_mismatches == 0
        ),
    }


def _run_sequence(
    sequence: str,
    specs: list[WorldSpec],
    reference: dict[str, dict[str, str]],
) -> dict[str, object]:
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

    memory = SemanticMemory(memory_path)
    memory.load()
    source = _source_rows(memory)
    relations = memory.passive_mcm_neighborhood_event_relations()
    event_store = memory.data["passive_mcm_neighborhood_event_memory"]
    return {
        "equivalence": {
            "sequence": sequence,
            "reference_relations": len(reference),
            "source_relations": len(source),
            "event_relations": len(relations),
            **_compare_reference(source, reference),
            **_event_integrity(source, relations),
        },
        "source": source,
        "relations": relations,
        "events": _event_rows(sequence, relations),
        "profile": memory.passive_mcm_neighborhood_event_profile(),
        "memory_size_bytes": memory_path.stat().st_size,
        "event_document_bytes": len(
            json.dumps(event_store, indent=2, sort_keys=True).encode("utf-8")
        ),
    }


def _rank_map(values: dict[str, int]) -> dict[str, float]:
    ordered = sorted(values.items(), key=lambda item: (item[1], item[0]))
    ranks = {}
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


def _spearman(left: dict[str, int], right: dict[str, int], shared: list[str]) -> float:
    left_rank = _rank_map({key: left[key] for key in shared})
    right_rank = _rank_map({key: right[key] for key in shared})
    left_mean = sum(left_rank.values()) / max(1, len(shared))
    right_mean = sum(right_rank.values()) / max(1, len(shared))
    numerator = sum(
        (left_rank[key] - left_mean) * (right_rank[key] - right_mean) for key in shared
    )
    left_scale = math.sqrt(sum((left_rank[key] - left_mean) ** 2 for key in shared))
    right_scale = math.sqrt(sum((right_rank[key] - right_mean) ** 2 for key in shared))
    return numerator / max(1e-12, left_scale * right_scale)


def _trajectory_fingerprint(relation: dict) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(int(event[field]) for field in EVENT_FIELDS if field != "finalization_index")
        for event in relation["events"]
    )


def _comparison_rows(
    forward: dict[str, dict], reverse: dict[str, dict]
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    shared = sorted(set(forward) & set(reverse))
    forward_counts = {key: int(forward[key]["event_count"]) for key in shared}
    reverse_counts = {key: int(reverse[key]["event_count"]) for key in shared}
    same_count = [key for key in shared if forward_counts[key] == reverse_counts[key]]
    exact = [
        key
        for key in same_count
        if _trajectory_fingerprint(forward[key]) == _trajectory_fingerprint(reverse[key])
    ]
    order_rows = [
        {
            "shared_relations": len(shared),
            "both_multi_event_relations": sum(
                forward_counts[key] >= 2 and reverse_counts[key] >= 2 for key in shared
            ),
            "event_count_spearman": _spearman(forward_counts, reverse_counts, shared),
            "same_event_count_relations": len(same_count),
            "same_event_count_share": len(same_count) / max(1, len(shared)),
            "exact_relation_age_trajectories": len(exact),
            "same_multi_event_count_relations": sum(
                forward_counts[key] >= 2 for key in same_count
            ),
            "exact_multi_event_trajectories": sum(
                forward_counts[key] >= 2 for key in exact
            ),
        }
    ]
    length_rows = []
    for minimum_events in (1, 2, 3, 5, 10, 20):
        eligible = [
            key for key in same_count if forward_counts[key] >= minimum_events
        ]
        exact_count = sum(key in exact for key in eligible)
        length_rows.append(
            {
                "minimum_events": minimum_events,
                "same_event_count_relations": len(eligible),
                "exact_relation_age_trajectories": exact_count,
                "exact_trajectory_share": exact_count / max(1, len(eligible)),
            }
        )
    return order_rows, length_rows


def _comparison_rows_from_results(
    results: dict[str, dict[str, object]]
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    by_sequence = {}
    for sequence in SEQUENCES:
        by_sequence[sequence] = {
            "|".join(sorted((relation["left_node"], relation["right_node"]))): relation
            for relation in results[sequence]["relations"].values()
        }
    return _comparison_rows(by_sequence["forward"], by_sequence["reverse"])


def _comparison_rows_from_archive() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    by_sequence: dict[str, dict[str, dict]] = {sequence: {} for sequence in SEQUENCES}
    with zipfile.ZipFile(EVENT_ARCHIVE) as archive:
        with archive.open("event_histories.csv") as raw_handle:
            handle = io.TextIOWrapper(raw_handle, encoding="utf-8", newline="")
            for row in csv.DictReader(handle):
                relation = by_sequence[row["sequence"]].setdefault(
                    row["pair_key"], {"event_count": 0, "events": []}
                )
                event = {field: int(row[field]) for field in EVENT_FIELDS}
                relation["events"].append(event)
                relation["event_count"] = len(relation["events"])
    return _comparison_rows(by_sequence["forward"], by_sequence["reverse"])


def _coverage_rows(results: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    rows = []
    for sequence in SEQUENCES:
        counts = Counter(
            int(relation["event_count"])
            for relation in results[sequence]["relations"].values()
        )
        for event_count in sorted(counts):
            rows.append(
                {
                    "sequence": sequence,
                    "event_count": event_count,
                    "relations": counts[event_count],
                }
            )
    return rows


def _csv_bytes(rows: list[dict[str, object]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def _write_event_archive(
    event_rows: list[dict[str, object]], manifest_rows: list[dict[str, object]]
) -> None:
    EVENT_ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(EVENT_ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, payload in (
            ("event_histories.csv", _csv_bytes(event_rows)),
            ("manifest.csv", _csv_bytes(manifest_rows)),
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


def main() -> int:
    specs = _world_specs()
    if len(specs) != 81:
        raise RuntimeError(f"expected 81 worlds, found {len(specs)}")
    reference = _reference_rows()
    baselines = _baseline_sizes()
    _clean_local_state()
    try:
        _prepare_worlds(specs)
        results: dict[str, dict[str, object]] = {}
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = {
                executor.submit(_run_sequence, sequence, specs, reference[sequence]): sequence
                for sequence in SEQUENCES
            }
            for future in as_completed(futures):
                results[futures[future]] = future.result()

        equivalence_rows = [results[sequence]["equivalence"] for sequence in SEQUENCES]
        coverage_rows = _coverage_rows(results)
        order_rows, length_rows = _comparison_rows_from_results(results)
        event_rows = results["forward"]["events"] + results["reverse"]["events"]
        manifest_rows = [
            {
                "sequence": sequence,
                "worlds": len(specs),
                "relations": results[sequence]["profile"]["relations"],
                "events": results[sequence]["profile"]["events"],
                "format": EVENT_FORMAT,
                "event_fields": "|".join(EVENT_FIELDS),
            }
            for sequence in SEQUENCES
        ]
        _write_event_archive(event_rows, manifest_rows)
        summary_rows = []
        for sequence in SEQUENCES:
            profile = results[sequence]["profile"]
            size = int(results[sequence]["memory_size_bytes"])
            baseline = baselines[sequence]
            summary_rows.append(
                {
                    "sequence": sequence,
                    "worlds": len(specs),
                    "relations": profile["relations"],
                    "events": profile["events"],
                    "legacy_unobserved_events": profile["legacy_unobserved_events"],
                    "total_growth_events": profile["total_growth_events"],
                    "multi_event_relations": profile["multi_event_relations"],
                    "maximum_events": profile["maximum_events"],
                    "format": profile["format"],
                    "field_exact_2081": results[sequence]["equivalence"][
                        "field_exact_2081"
                    ],
                    "event_integrity_exact": results[sequence]["equivalence"][
                        "event_integrity_exact"
                    ],
                    "memory_size_bytes": size,
                    "event_document_bytes": results[sequence]["event_document_bytes"],
                    "2081_baseline_memory_size_bytes": baseline,
                    "event_memory_overhead_bytes": size - baseline,
                    "event_memory_overhead_percent": ((size - baseline) / baseline) * 100.0,
                    "event_archive_bytes": EVENT_ARCHIVE.stat().st_size,
                    "read_by_mini_dio": profile["read_by_mini_dio"],
                    "influences_field": profile["influences_field"],
                    "influences_action": profile["influences_action"],
                }
            )

        _write_csv("equivalence", equivalence_rows)
        _write_csv("coverage", coverage_rows)
        _write_csv("order", order_rows)
        _write_csv("length", length_rows)
        _write_csv("summary", summary_rows)
        if not all(
            int(row["field_exact_2081"]) == 1
            and int(row["event_integrity_exact"]) == 1
            for row in equivalence_rows
        ):
            raise RuntimeError("relation event time changed field growth or lost events")
        print(f"event_rows={len(event_rows)}")
        print(f"coverage_rows={len(coverage_rows)}")
        print(f"archive_bytes={EVENT_ARCHIVE.stat().st_size}")
        return 0
    finally:
        _clean_local_state()


def analyze_existing_outputs() -> int:
    order_rows, length_rows = _comparison_rows_from_archive()
    _write_csv("order", order_rows)
    _write_csv("length", length_rows)
    summary_path = FINDING_DIR / f"{PREFIX}.summary.csv"
    with summary_path.open(newline="", encoding="utf-8") as handle:
        summary_rows = list(csv.DictReader(handle))
    for row in summary_rows:
        row["legacy_unobserved_events"] = "0"
        row["total_growth_events"] = row["events"]
    _write_csv("summary", summary_rows)
    print(f"order_rows={len(order_rows)}")
    print(f"length_rows={len(length_rows)}")
    print(f"summary_rows={len(summary_rows)}")
    return 0


if __name__ == "__main__":
    if "--analyze-existing" in sys.argv:
        raise SystemExit(analyze_existing_outputs())
    raise SystemExit(main())
