from __future__ import annotations

import csv
import json
import math
import shutil
import subprocess
import sys
import zipfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "data" / "generated" / "2078_mcm_topology_neighborhoods"
MEMORY_DIR = ROOT / "memory"
DEBUG_ROOT = ROOT / "debug" / "2078_mcm_topology_neighborhoods"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
WORLD_CSV = FINDING_DIR / "2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.worlds.csv"
SUMMARY_CSV = FINDING_DIR / "2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.summary.csv"
LINK_CSV = FINDING_DIR / "2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.links.csv"
OVERLAP_CSV = FINDING_DIR / "2078_WIEDERKEHRENDE_MCM_EPISODENNACHBARSCHAFTEN.overlap.csv"

CORE_FIELDS = (
    "avg_mcm_carry_quality",
    "avg_mcm_strain_quality",
    "avg_mcm_rekopplung_quality",
    "avg_mcm_adaptive_rekopplung_quality",
)
FULL_FIELDS = CORE_FIELDS + (
    "avg_sensory_coupling",
    "avg_visual_field_gap",
    "avg_hearing_field_gap",
)
FULL_DURATION_FIELDS = ("avg_duration",) + FULL_FIELDS
PROFILE_SCOPES = (
    ("field_core_raw", CORE_FIELDS, False),
    ("field_full_raw", FULL_FIELDS, False),
    ("field_full_plus_duration_standardized", FULL_DURATION_FIELDS, True),
)
PAIR_KINDS = ("real_real", "real_null", "null_null")
REAL_COHORT_KINDS = ("real_2025_2025", "real_crossyear", "real_2024_2024")


@dataclass(frozen=True)
class WorldSpec:
    index: int
    world_id: str
    corpus: str
    variant: str
    archive: Path
    member: str

    @property
    def is_real(self) -> bool:
        return self.variant == "real"

    @property
    def year(self) -> str:
        if "_2025_" in self.member:
            return "2025"
        if "_2024_" in self.member:
            return "2024"
        return "unknown"

    @property
    def extracted_path(self) -> Path:
        return GENERATED_DIR / f"{self.index:03d}.csv"

    @property
    def memory_path(self) -> Path:
        return MEMORY_DIR / f"topology_2078_{self.index:03d}.json"

    @property
    def debug_root(self) -> Path:
        return DEBUG_ROOT / f"{self.index:03d}"


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
        if not archive_path.exists():
            raise FileNotFoundError(archive_path)
        with zipfile.ZipFile(archive_path) as archive:
            for member in sorted(archive.namelist()):
                if member.lower().endswith(".csv") and Path(member).name.lower() != "manifest.csv":
                    pending.append((corpus, archive_path, member))
    return [
        WorldSpec(
            index=index,
            world_id=f"W2078_{index:03d}",
            corpus=corpus,
            variant=_variant(member),
            archive=archive,
            member=member,
        )
        for index, (corpus, archive, member) in enumerate(pending, start=1)
    ]


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if not math.isfinite(result) else result


def _clean_local_state(specs: list[WorldSpec]) -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    if DEBUG_ROOT.exists():
        shutil.rmtree(DEBUG_ROOT)
    for spec in specs:
        if spec.memory_path.exists():
            spec.memory_path.unlink()


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


def _run_world(spec: WorldSpec) -> tuple[str, dict]:
    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        str(spec.extracted_path),
        "--runs",
        "1",
        "--memory",
        str(spec.memory_path),
        "--debug-root",
        str(spec.debug_root),
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
        raise RuntimeError(result.stderr or f"run failed for {spec.world_id}")
    memory = json.loads(spec.memory_path.read_text(encoding="utf-8"))
    topology = dict(memory.get("passive_mcm_topology", {}) or {})
    return spec.world_id, dict(topology.get("nodes", {}) or {})


def _run_all_worlds(specs: list[WorldSpec]) -> dict[str, dict[str, dict]]:
    results: dict[str, dict[str, dict]] = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(_run_world, spec): spec for spec in specs}
        completed = 0
        for future in as_completed(futures):
            world_id, nodes = future.result()
            results[world_id] = nodes
            completed += 1
            if completed % 10 == 0 or completed == len(specs):
                print(f"worlds_completed={completed}/{len(specs)}", flush=True)
    return results


def _raw_profile(record: dict, fields: tuple[str, ...]) -> list[float]:
    values = [_safe_float(record.get(field)) for field in fields]
    if "avg_duration" in fields:
        index = fields.index("avg_duration")
        values[index] = math.log1p(max(0.0, values[index]))
    return values


def _scaler(vectors: list[list[float]]) -> tuple[list[float], list[float]]:
    dimensions = len(vectors[0])
    means = [sum(vector[index] for vector in vectors) / len(vectors) for index in range(dimensions)]
    deviations = []
    for index in range(dimensions):
        variance = sum((vector[index] - means[index]) ** 2 for vector in vectors) / len(vectors)
        deviations.append(math.sqrt(variance) or 1.0)
    return means, deviations


def _profiles_for_scope(
    nodes_by_world: dict[str, dict[str, dict]],
    fields: tuple[str, ...],
    standardize: bool,
) -> dict[str, dict[str, list[float]]]:
    raw = {
        world: {symbol: _raw_profile(record, fields) for symbol, record in nodes.items()}
        for world, nodes in nodes_by_world.items()
    }
    all_vectors = [vector for world in raw.values() for vector in world.values()]
    if standardize:
        means, deviations = _scaler(all_vectors)
    else:
        means = [0.0] * len(fields)
        deviations = [1.0] * len(fields)
    return {
        world: {
            symbol: [
                (value - means[index]) / deviations[index]
                for index, value in enumerate(vector)
            ]
            for symbol, vector in profiles.items()
        }
        for world, profiles in raw.items()
    }


def _distance(left: list[float], right: list[float]) -> float:
    return math.sqrt(
        sum((left[index] - right[index]) ** 2 for index in range(len(left))) / len(left)
    )


def _nearest(
    source: dict[str, list[float]], target: dict[str, list[float]]
) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for source_symbol, source_vector in source.items():
        distances = {
            target_symbol: _distance(source_vector, target_vector)
            for target_symbol, target_vector in target.items()
            if target_symbol != source_symbol
        }
        if not distances:
            continue
        minimum = min(distances.values())
        result[source_symbol] = {
            symbol for symbol, value in distances.items() if abs(value - minimum) <= 1e-12
        }
    return result


def _mutual_links(
    left: dict[str, list[float]], right: dict[str, list[float]]
) -> set[tuple[str, str]]:
    left_nearest = _nearest(left, right)
    right_nearest = _nearest(right, left)
    links = set()
    for left_symbol, right_symbols in left_nearest.items():
        for right_symbol in right_symbols:
            if left_symbol in right_nearest.get(right_symbol, set()):
                links.add(tuple(sorted((left_symbol, right_symbol))))
    return links


def _pair_kind(left: WorldSpec, right: WorldSpec) -> str:
    real_count = int(left.is_real) + int(right.is_real)
    if real_count == 2:
        return "real_real"
    if real_count == 1:
        return "real_null"
    return "null_null"


def _real_cohort_kind(left: WorldSpec, right: WorldSpec) -> str:
    if not left.is_real or not right.is_real:
        return ""
    if left.year == right.year == "2025":
        return "real_2025_2025"
    if left.year == right.year == "2024":
        return "real_2024_2024"
    return "real_crossyear"


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _jaccard_row(
    comparison_type: str, left_name: str, right_name: str, left: set, right: set
) -> dict[str, object]:
    union = left | right
    shared = left & right
    return {
        "comparison_type": comparison_type,
        "left": left_name,
        "right": right_name,
        "left_links": len(left),
        "right_links": len(right),
        "shared_links": len(shared),
        "jaccard": len(shared) / max(1, len(union)),
    }


def main() -> int:
    specs = _world_specs()
    if len(specs) != 81:
        raise RuntimeError(f"expected 81 worlds, found {len(specs)}")
    _clean_local_state(specs)
    try:
        _prepare_worlds(specs)
        nodes_by_world = _run_all_worlds(specs)
        nodes_by_world = {spec.world_id: nodes_by_world[spec.world_id] for spec in specs}
        world_pairs = list(combinations(specs, 2))

        support: dict[str, dict[str, dict[tuple[str, str], set[str]]]] = {
            scope: {kind: defaultdict(set) for kind in PAIR_KINDS}
            for scope, _, _ in PROFILE_SCOPES
        }
        cohort_support: dict[str, dict[str, dict[tuple[str, str], set[str]]]] = {
            scope: {kind: defaultdict(set) for kind in REAL_COHORT_KINDS}
            for scope, _, _ in PROFILE_SCOPES
        }
        pair_link_counts: dict[tuple[str, str], list[int]] = defaultdict(list)
        pair_link_fractions: dict[tuple[str, str], list[float]] = defaultdict(list)
        possible_pairs = {kind: 0 for kind in PAIR_KINDS}
        for left, right in world_pairs:
            kind = _pair_kind(left, right)
            possible_pairs[kind] += 1

        for scope, fields, standardize in PROFILE_SCOPES:
            profiles = _profiles_for_scope(nodes_by_world, fields, standardize)
            for left, right in world_pairs:
                kind = _pair_kind(left, right)
                pair_key = f"{left.world_id}|{right.world_id}"
                links = _mutual_links(profiles[left.world_id], profiles[right.world_id])
                pair_link_counts[(scope, kind)].append(len(links))
                pair_link_fractions[(scope, kind)].append(
                    len(links)
                    / max(1, min(len(profiles[left.world_id]), len(profiles[right.world_id])))
                )
                cohort_kind = _real_cohort_kind(left, right)
                for link in links:
                    support[scope][kind][link].add(pair_key)
                    if cohort_kind:
                        cohort_support[scope][cohort_kind][link].add(pair_key)

        all_links = {
            link
            for scope, _, _ in PROFILE_SCOPES
            for kind in PAIR_KINDS
            for link in support[scope][kind]
        }
        eligible: dict[str, dict[tuple[str, str], set[str]]] = {
            kind: defaultdict(set) for kind in PAIR_KINDS
        }
        cohort_eligible: dict[str, dict[tuple[str, str], set[str]]] = {
            kind: defaultdict(set) for kind in REAL_COHORT_KINDS
        }
        node_sets = {world: set(nodes) for world, nodes in nodes_by_world.items()}
        for left, right in world_pairs:
            kind = _pair_kind(left, right)
            pair_key = f"{left.world_id}|{right.world_id}"
            left_nodes = node_sets[left.world_id]
            right_nodes = node_sets[right.world_id]
            cohort_kind = _real_cohort_kind(left, right)
            for first, second in all_links:
                if (first in left_nodes and second in right_nodes) or (
                    second in left_nodes and first in right_nodes
                ):
                    eligible[kind][(first, second)].add(pair_key)
                    if cohort_kind:
                        cohort_eligible[cohort_kind][(first, second)].add(pair_key)

        world_rows = []
        for spec in specs:
            nodes = nodes_by_world[spec.world_id]
            world_rows.append(
                {
                    "world_id": spec.world_id,
                    "corpus": spec.corpus,
                    "year": spec.year,
                    "variant": spec.variant,
                    "world_kind": "real" if spec.is_real else "null",
                    "episode_observations": sum(
                        int(record.get("seen_count", 0) or 0) for record in nodes.values()
                    ),
                    "unique_episode_identities": len(nodes),
                    "source_archive": spec.archive.name,
                    "source_member": spec.member,
                }
            )

        summary_rows = []
        for scope, _, _ in PROFILE_SCOPES:
            for kind in PAIR_KINDS:
                counts = pair_link_counts[(scope, kind)]
                fractions = pair_link_fractions[(scope, kind)]
                links = set(support[scope][kind])
                summary_rows.append(
                    {
                        "profile_scope": scope,
                        "pair_kind": kind,
                        "world_pairs": possible_pairs[kind],
                        "mutual_link_observations": sum(counts),
                        "unique_links": len(links),
                        "mean_links_per_world_pair": sum(counts) / max(1, len(counts)),
                        "mean_link_fraction_of_smaller_topology": sum(fractions)
                        / max(1, len(fractions)),
                        "max_links_in_world_pair": max(counts) if counts else 0,
                    }
                )

        link_rows = []
        scope_names = [scope for scope, _, _ in PROFILE_SCOPES]
        for link in all_links:
            union_support = {
                kind: set().union(*(support[scope][kind].get(link, set()) for scope in scope_names))
                for kind in PAIR_KINDS
            }
            all_scope_support = {
                kind: set.intersection(
                    *(set(support[scope][kind].get(link, set())) for scope in scope_names)
                )
                for kind in PAIR_KINDS
            }
            cohort_union_support = {
                kind: set().union(
                    *(cohort_support[scope][kind].get(link, set()) for scope in scope_names)
                )
                for kind in REAL_COHORT_KINDS
            }
            cohort_all_scope_support = {
                kind: set.intersection(
                    *(set(cohort_support[scope][kind].get(link, set())) for scope in scope_names)
                )
                for kind in REAL_COHORT_KINDS
            }
            rates = {
                kind: len(union_support[kind]) / max(1, len(eligible[kind].get(link, set())))
                for kind in PAIR_KINDS
            }
            link_rows.append(
                {
                    "left_node": link[0],
                    "right_node": link[1],
                    "scope_count": sum(
                        1
                        for scope in scope_names
                        if any(support[scope][kind].get(link) for kind in PAIR_KINDS)
                    ),
                    "total_supported_world_pairs": len(set().union(*union_support.values())),
                    "real_real_supported": len(union_support["real_real"]),
                    "real_real_all_scopes": len(all_scope_support["real_real"]),
                    "real_real_eligible": len(eligible["real_real"].get(link, set())),
                    "real_real_rate": rates["real_real"],
                    "real_null_supported": len(union_support["real_null"]),
                    "real_null_all_scopes": len(all_scope_support["real_null"]),
                    "real_null_eligible": len(eligible["real_null"].get(link, set())),
                    "real_null_rate": rates["real_null"],
                    "null_null_supported": len(union_support["null_null"]),
                    "null_null_all_scopes": len(all_scope_support["null_null"]),
                    "null_null_eligible": len(eligible["null_null"].get(link, set())),
                    "null_null_rate": rates["null_null"],
                    "real_rate_advantage": rates["real_real"]
                    - max(rates["real_null"], rates["null_null"]),
                    "real_2025_supported": len(cohort_union_support["real_2025_2025"]),
                    "real_2025_all_scopes": len(cohort_all_scope_support["real_2025_2025"]),
                    "real_2025_eligible": len(
                        cohort_eligible["real_2025_2025"].get(link, set())
                    ),
                    "real_crossyear_supported": len(cohort_union_support["real_crossyear"]),
                    "real_crossyear_all_scopes": len(
                        cohort_all_scope_support["real_crossyear"]
                    ),
                    "real_crossyear_eligible": len(
                        cohort_eligible["real_crossyear"].get(link, set())
                    ),
                    "real_2024_supported": len(cohort_union_support["real_2024_2024"]),
                    "real_2024_all_scopes": len(cohort_all_scope_support["real_2024_2024"]),
                    "real_2024_eligible": len(
                        cohort_eligible["real_2024_2024"].get(link, set())
                    ),
                }
            )
        link_rows.sort(
            key=lambda row: (
                int(row["total_supported_world_pairs"]),
                int(row["scope_count"]),
                float(row["real_rate_advantage"]),
                str(row["left_node"]),
                str(row["right_node"]),
            ),
            reverse=True,
        )
        for rank, row in enumerate(link_rows, start=1):
            row["support_rank"] = rank
        link_rows = [
            {"support_rank": row.pop("support_rank"), **row}
            for row in link_rows
        ]

        kind_link_sets = {
            kind: {
                link
                for scope in scope_names
                for link in support[scope][kind]
            }
            for kind in PAIR_KINDS
        }
        scope_link_sets = {
            scope: {
                link for kind in PAIR_KINDS for link in support[scope][kind]
            }
            for scope in scope_names
        }
        overlap_rows = [
            _jaccard_row("world_pair_kind", left, right, kind_link_sets[left], kind_link_sets[right])
            for left, right in combinations(PAIR_KINDS, 2)
        ] + [
            _jaccard_row("profile_scope", left, right, scope_link_sets[left], scope_link_sets[right])
            for left, right in combinations(scope_names, 2)
        ]

        _write_csv(WORLD_CSV, world_rows)
        _write_csv(SUMMARY_CSV, summary_rows)
        _write_csv(LINK_CSV, link_rows)
        _write_csv(OVERLAP_CSV, overlap_rows)
        print(f"world_rows={len(world_rows)}")
        print(f"summary_rows={len(summary_rows)}")
        print(f"link_rows={len(link_rows)}")
        print(f"overlap_rows={len(overlap_rows)}")
        return 0
    finally:
        _clean_local_state(specs)


if __name__ == "__main__":
    raise SystemExit(main())
