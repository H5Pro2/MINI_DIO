from __future__ import annotations

import csv
import json
import math
import shutil
import subprocess
import sys
import zipfile
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = ROOT / "data" / "generated" / "2077_mcm_topology_sequence_distance"
MEMORY_DIR = ROOT / "memory"
DEBUG_ROOT = ROOT / "debug" / "2077_mcm_topology_sequence_distance"
FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
WORLD_CSV = FINDING_DIR / "2077_MCM_TOPOLOGIE_FOLGEN_UND_PROFILABSTAENDE.worlds.csv"
MOTIF_CSV = FINDING_DIR / "2077_MCM_TOPOLOGIE_FOLGEN_UND_PROFILABSTAENDE.motifs.csv"
DISTANCE_CSV = FINDING_DIR / "2077_MCM_TOPOLOGIE_FOLGEN_UND_PROFILABSTAENDE.distances.csv"

PROFILE_FIELDS = (
    "avg_duration",
    "avg_mcm_carry_quality",
    "avg_mcm_strain_quality",
    "avg_mcm_rekopplung_quality",
    "avg_mcm_adaptive_rekopplung_quality",
    "avg_sensory_coupling",
    "avg_visual_field_gap",
    "avg_hearing_field_gap",
)
CORE_PROFILE_FIELDS = (
    "avg_mcm_carry_quality",
    "avg_mcm_strain_quality",
    "avg_mcm_rekopplung_quality",
    "avg_mcm_adaptive_rekopplung_quality",
)
FULL_QUALITY_FIELDS = PROFILE_FIELDS[1:]


@dataclass(frozen=True)
class WorldSpec:
    key: str
    kind: str
    archive: Path
    member: str

    @property
    def extracted_path(self) -> Path:
        return GENERATED_DIR / f"{self.kind}.csv"

    @property
    def memory_path(self) -> Path:
        return MEMORY_DIR / f"topology_2077_{self.kind}.json"

    @property
    def debug_root(self) -> Path:
        return DEBUG_ROOT / self.kind


WORLDS = {
    "real_anchor": WorldSpec(
        key="TOPO2077_REAL_ANCHOR_BTC_2025_1H_5000_6000",
        kind="real_anchor",
        archive=ROOT / "data" / "2070_role_family_followworlds.zip",
        member="kontrolliert_2070_btc_2025_1h_start5000_rows1000.csv",
    ),
    "real_follow": WorldSpec(
        key="TOPO2077_REAL_FOLLOW_BTC_2025_1H_6000_7000",
        kind="real_follow",
        archive=ROOT / "data" / "2070_role_family_followworlds.zip",
        member="kontrolliert_2070_btc_2025_1h_start6000_rows1000.csv",
    ),
    "null_shuffle": WorldSpec(
        key="TOPO2077_NULL_SHUFFLE_BTC_2025_1H_6000_7000",
        kind="null_shuffle",
        archive=ROOT / "data" / "2073_role_family_null_controls.zip",
        member="kontrolliert_2073_btc_start6000_shuffle_order_1000.csv",
    ),
    "null_random": WorldSpec(
        key="TOPO2077_NULL_RANDOM_BTC_2025_1H_6000_7000",
        kind="null_random_sign",
        archive=ROOT / "data" / "2073_role_family_null_controls.zip",
        member="kontrolliert_2073_btc_start6000_random_sign_1000.csv",
    ),
}


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if not math.isfinite(result) else result


def _prepare_worlds() -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    for spec in WORLDS.values():
        if not spec.archive.exists():
            raise FileNotFoundError(spec.archive)
        with zipfile.ZipFile(spec.archive) as archive:
            with archive.open(spec.member) as source, spec.extracted_path.open("wb") as target:
                shutil.copyfileobj(source, target)


def _clean_local_state() -> None:
    if GENERATED_DIR.exists():
        shutil.rmtree(GENERATED_DIR)
    if DEBUG_ROOT.exists():
        shutil.rmtree(DEBUG_ROOT)
    for spec in WORLDS.values():
        if spec.memory_path.exists():
            spec.memory_path.unlink()


def _run_world(spec: WorldSpec) -> dict:
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
    return json.loads(spec.memory_path.read_text(encoding="utf-8"))


def _episode_sequence(spec: WorldSpec, topology: dict) -> list[str]:
    episode_path = spec.debug_root / "dio_mini_lauf_1" / "episodes.csv"
    sequence: list[str] = []
    with episode_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            symbol = str(row.get("mcm_topology_node_symbol", "") or "").strip()
            if symbol and symbol != "-":
                sequence.append(symbol)

    # The final tracker flush is stored after episodes.csv has been written.
    final_symbol = str(topology.get("last_node_symbol", "") or "").strip()
    if final_symbol:
        sequence.append(final_symbol)
    expected = sum(
        int(record.get("seen_count", 0) or 0)
        for record in dict(topology.get("nodes", {}) or {}).values()
    )
    if len(sequence) != expected:
        raise RuntimeError(
            f"episode sequence mismatch for {spec.kind}: got {len(sequence)}, expected {expected}"
        )
    return sequence


def _motifs(sequence: list[str], length: int) -> Counter[tuple[str, ...]]:
    return Counter(
        tuple(sequence[index : index + length])
        for index in range(max(0, len(sequence) - length + 1))
    )


def _motif_comparison(
    left: list[str], right: list[str], length: int
) -> dict[str, int | float]:
    left_counter = _motifs(left, length)
    right_counter = _motifs(right, length)
    left_set = set(left_counter)
    right_set = set(right_counter)
    union = left_set | right_set
    shared = left_set & right_set
    weighted_intersection = sum(
        min(left_counter[motif], right_counter[motif]) for motif in union
    )
    weighted_union = sum(max(left_counter[motif], right_counter[motif]) for motif in union)
    return {
        "left_unique": len(left_set),
        "right_unique": len(right_set),
        "shared_unique": len(shared),
        "set_jaccard": len(shared) / max(1, len(union)),
        "weighted_jaccard": weighted_intersection / max(1, weighted_union),
    }


def _raw_profile(record: dict, fields: tuple[str, ...]) -> list[float]:
    values = [_safe_float(record.get(field)) for field in fields]
    if "avg_duration" in fields:
        duration_index = fields.index("avg_duration")
        values[duration_index] = math.log1p(max(0.0, values[duration_index]))
    return values


def _profile_scaler(raw_vectors: list[list[float]]) -> tuple[list[float], list[float]]:
    dimensions = len(raw_vectors[0])
    means = [
        sum(vector[index] for vector in raw_vectors) / max(1, len(raw_vectors))
        for index in range(dimensions)
    ]
    deviations = []
    for index in range(dimensions):
        variance = sum((vector[index] - means[index]) ** 2 for vector in raw_vectors) / max(
            1, len(raw_vectors)
        )
        deviations.append(math.sqrt(variance) or 1.0)
    return means, deviations


def _scaled_sequence(
    symbols: list[str],
    nodes: dict[str, dict],
    fields: tuple[str, ...],
    means: list[float],
    deviations: list[float],
) -> list[list[float]]:
    vectors = []
    for symbol in symbols:
        raw = _raw_profile(dict(nodes[symbol] or {}), fields)
        vectors.append(
            [(value - means[index]) / deviations[index] for index, value in enumerate(raw)]
        )
    return vectors


def _distance(left: list[float], right: list[float]) -> float:
    return math.sqrt(
        sum((left[index] - right[index]) ** 2 for index in range(len(left))) / len(left)
    )


def _cloud_distance(left: list[list[float]], right: list[list[float]]) -> float:
    def directed(source: list[list[float]], target: list[list[float]]) -> float:
        return sum(min(_distance(item, other) for other in target) for item in source) / max(
            1, len(source)
        )

    return (directed(left, right) + directed(right, left)) / 2.0


def _dtw_distance(left: list[list[float]], right: list[list[float]]) -> float:
    rows = len(left)
    columns = len(right)
    costs = [[math.inf] * (columns + 1) for _ in range(rows + 1)]
    steps = [[0] * (columns + 1) for _ in range(rows + 1)]
    costs[0][0] = 0.0
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            predecessors = (
                (costs[row - 1][column], steps[row - 1][column]),
                (costs[row][column - 1], steps[row][column - 1]),
                (costs[row - 1][column - 1], steps[row - 1][column - 1]),
            )
            previous_cost, previous_steps = min(predecessors, key=lambda item: (item[0], item[1]))
            costs[row][column] = previous_cost + _distance(left[row - 1], right[column - 1])
            steps[row][column] = previous_steps + 1
    return costs[rows][columns] / max(1, steps[rows][columns])


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    _clean_local_state()
    try:
        _prepare_worlds()
        sequences: dict[str, list[str]] = {}
        state_sequences: dict[str, list[str]] = {}
        nodes_by_world: dict[str, dict[str, dict]] = {}
        world_rows: list[dict[str, object]] = []

        for world_name, spec in WORLDS.items():
            memory = _run_world(spec)
            topology = dict(memory.get("passive_mcm_topology", {}) or {})
            nodes = dict(topology.get("nodes", {}) or {})
            sequence = _episode_sequence(spec, topology)
            state_sequence = [str(nodes[symbol].get("episode_state", "") or "-") for symbol in sequence]
            sequences[world_name] = sequence
            state_sequences[world_name] = state_sequence
            nodes_by_world[world_name] = nodes
            world_rows.append(
                {
                    "world": world_name,
                    "episodes": len(sequence),
                    "unique_nodes": len(set(sequence)),
                    "unique_states": len(set(state_sequence)),
                    "unique_node_pairs": len(_motifs(sequence, 2)),
                    "unique_node_triples": len(_motifs(sequence, 3)),
                    "unique_node_quadruples": len(_motifs(sequence, 4)),
                    "unique_state_pairs": len(_motifs(state_sequence, 2)),
                    "unique_state_triples": len(_motifs(state_sequence, 3)),
                    "unique_state_quadruples": len(_motifs(state_sequence, 4)),
                }
            )

        motif_rows: list[dict[str, object]] = []
        for left_name, right_name in combinations(WORLDS, 2):
            for representation, source in (
                ("node_identity", sequences),
                ("episode_state", state_sequences),
            ):
                for length in (2, 3, 4):
                    motif_rows.append(
                        {
                            "left_world": left_name,
                            "right_world": right_name,
                            "representation": representation,
                            "motif_length": length,
                            **_motif_comparison(source[left_name], source[right_name], length),
                        }
                    )

        distance_rows: list[dict[str, object]] = []
        profile_scopes = (
            ("field_core_raw", CORE_PROFILE_FIELDS, False),
            ("field_full_raw", FULL_QUALITY_FIELDS, False),
            ("field_full_plus_duration_standardized", PROFILE_FIELDS, True),
        )
        for profile_scope, fields, standardize in profile_scopes:
            all_raw_vectors = [
                _raw_profile(nodes_by_world[world_name][symbol], fields)
                for world_name, sequence in sequences.items()
                for symbol in sequence
            ]
            if standardize:
                means, deviations = _profile_scaler(all_raw_vectors)
            else:
                means = [0.0] * len(fields)
                deviations = [1.0] * len(fields)
            profiles = {
                world_name: _scaled_sequence(
                    sequences[world_name],
                    nodes_by_world[world_name],
                    fields,
                    means,
                    deviations,
                )
                for world_name in WORLDS
            }
            for left_name, right_name in combinations(WORLDS, 2):
                cloud = _cloud_distance(profiles[left_name], profiles[right_name])
                dtw = _dtw_distance(profiles[left_name], profiles[right_name])
                distance_rows.append(
                    {
                        "left_world": left_name,
                        "right_world": right_name,
                        "profile_scope": profile_scope,
                        "left_episodes": len(profiles[left_name]),
                        "right_episodes": len(profiles[right_name]),
                        "profile_dimensions": len(fields),
                        "profile_cloud_distance": cloud,
                        "profile_dtw_distance": dtw,
                        "ordered_to_cloud_ratio": dtw / max(1e-12, cloud),
                    }
                )

        _write_csv(WORLD_CSV, world_rows)
        _write_csv(MOTIF_CSV, motif_rows)
        _write_csv(DISTANCE_CSV, distance_rows)
        print(f"world_rows={len(world_rows)}")
        print(f"motif_rows={len(motif_rows)}")
        print(f"distance_rows={len(distance_rows)}")
        print(f"worlds={WORLD_CSV.relative_to(ROOT)}")
        print(f"motifs={MOTIF_CSV.relative_to(ROOT)}")
        print(f"distances={DISTANCE_CSV.relative_to(ROOT)}")
        return 0
    finally:
        _clean_local_state()


if __name__ == "__main__":
    raise SystemExit(main())
