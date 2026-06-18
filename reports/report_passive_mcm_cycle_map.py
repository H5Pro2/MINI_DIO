from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MATRIX = ROOT / "debug" / "dio_mini_passive_mcm_topology_matrix_20260618" / "passive_mcm_topology_matrix.csv"
DEFAULT_WORLD_DIR = ROOT / "debug" / "dio_mini_passive_topology_year_hardtest_worlds_20260618"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_mcm_cycle_map_20260618"
BRIDGE_ROLES = {
    "tragende_bruecke",
    "entlastende_bruecke",
    "entlastende_bruecke_mit_offener_varianz",
}


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _as_float(value: object) -> float:
    return float(value or 0.0)


def _mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def _iter_worlds(input_dir: Path) -> list[tuple[str, list[dict[str, str]]]]:
    worlds: list[tuple[str, list[dict[str, str]]]] = []
    for world_dir in sorted(input_dir.glob("world_*")):
        path = world_dir / "reifespur_landkarte_rows.csv"
        if not path.exists():
            continue
        rows = sorted(_read_csv(path), key=lambda row: int(float(row.get("tick", 0) or 0)))
        worlds.append((world_dir.name.removeprefix("world_"), rows))
    return worlds


def _role_for(row: dict[str, str], matrix: dict[str, str]) -> str:
    return matrix.get(row.get("nearest_reifespur_symbol", "-"), "unmapped")


def _classify_cycle(seq: tuple[str, ...]) -> str:
    if all(role == "zentrum" for role in seq):
        return "zentrum_haelt"
    if seq[0] == "zentrum" and seq[-1] == "zentrum" and "selbstnahe_drift" in seq:
        return "zentrum_drift_zentrum"
    if seq[0] == "zentrum" and seq[-1] == "zentrum" and "uebergangszone" in seq:
        return "zentrum_uebergang_zentrum"
    if seq[0] in BRIDGE_ROLES and seq[-1] in BRIDGE_ROLES and "zentrum" in seq:
        return "bruecke_zentrum_bruecke"
    if seq[0] == "selbstnahe_drift" and "zentrum" in seq and seq[-1] in BRIDGE_ROLES:
        return "drift_zentrum_bruecke"
    if seq[0] == "uebergangszone" and "zentrum" in seq and seq[-1] in BRIDGE_ROLES:
        return "uebergang_zentrum_bruecke"
    if "zentrum" in seq and seq[0] != "zentrum" and seq[-1] == "zentrum":
        return "rueckfuehrung_zum_zentrum"
    if "zentrum" in seq and seq[0] == "zentrum" and seq[-1] != "zentrum":
        return "auslauf_aus_zentrum"
    if any(role in BRIDGE_ROLES for role in seq) and "zentrum" in seq:
        return "zentrum_bruecken_kopplung"
    if "selbstnahe_drift" in seq or "uebergangszone" in seq:
        return "offene_peripherie_bewegung"
    return "sonstige_folge"


def _collect_sequences(
    roles: list[str],
    rows: list[dict[str, str]],
    world_label: str,
    length: int,
) -> tuple[Counter[tuple[str, ...]], dict[tuple[str, ...], dict[str, list[float]]], Counter[tuple[str, ...]]]:
    sequence_counter: Counter[tuple[str, ...]] = Counter()
    sequence_values: dict[tuple[str, ...], dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    world_counter: Counter[tuple[str, ...]] = Counter()
    for idx in range(0, max(0, len(roles) - length + 1)):
        seq = tuple(roles[idx : idx + length])
        sequence_counter[seq] += 1
        world_counter[seq] += 1
        window = rows[idx : idx + length]
        sequence_values[seq]["carry"].append(_mean([_as_float(row.get("mcm_carry_quality", 0.0)) for row in window]))
        sequence_values[seq]["strain"].append(_mean([_as_float(row.get("mcm_strain_quality", 0.0)) for row in window]))
        sequence_values[seq]["rekopplung"].append(
            _mean([_as_float(row.get("mcm_rekopplung_quality", 0.0)) for row in window])
        )
        sequence_values[seq]["worlds"].append(world_label)
    return sequence_counter, sequence_values, world_counter


def run(matrix_path: Path, input_dir: Path, out_dir: Path) -> dict[str, object]:
    matrix = {
        row["reifespur_symbol"]: row["matrix_interpretation"]
        for row in _read_csv(matrix_path)
        if row.get("reifespur_symbol")
    }
    worlds = _iter_worlds(input_dir)

    length_counters: dict[int, Counter[tuple[str, ...]]] = {3: Counter(), 4: Counter(), 5: Counter()}
    length_values: dict[int, dict[tuple[str, ...], dict[str, list[float]]]] = {
        3: defaultdict(lambda: defaultdict(list)),
        4: defaultdict(lambda: defaultdict(list)),
        5: defaultdict(lambda: defaultdict(list)),
    }
    length_world_presence: dict[int, dict[tuple[str, ...], set[str]]] = {3: defaultdict(set), 4: defaultdict(set), 5: defaultdict(set)}
    class_counts: Counter[str] = Counter()

    for world_label, rows in worlds:
        roles = [_role_for(row, matrix) for row in rows]
        for length in (3, 4, 5):
            seq_counter, seq_values, _ = _collect_sequences(roles, rows, world_label, length)
            length_counters[length].update(seq_counter)
            for seq, values in seq_values.items():
                length_values[length][seq]["carry"].extend(values["carry"])
                length_values[length][seq]["strain"].extend(values["strain"])
                length_values[length][seq]["rekopplung"].extend(values["rekopplung"])
                length_world_presence[length][seq].add(world_label)

    sequence_rows: list[dict[str, object]] = []
    for length in (3, 4, 5):
        total = sum(length_counters[length].values())
        for seq, count in length_counters[length].most_common():
            cycle_class = _classify_cycle(seq)
            class_counts[cycle_class] += count
            sequence_rows.append(
                {
                    "sequence_length": length,
                    "cycle_class": cycle_class,
                    "sequence": " -> ".join(seq),
                    "count": count,
                    "share": round(count / total, 6) if total else 0.0,
                    "world_presence": len(length_world_presence[length][seq]),
                    "mean_carry": _mean(length_values[length][seq]["carry"]),
                    "mean_strain": _mean(length_values[length][seq]["strain"]),
                    "mean_rekopplung": _mean(length_values[length][seq]["rekopplung"]),
                    "passive_only": 1,
                    "influences_action": 0,
                    "is_gate": 0,
                    "is_entry_signal": 0,
                }
            )

    class_rows: list[dict[str, object]] = []
    class_total = sum(class_counts.values())
    for cycle_class, count in class_counts.most_common():
        class_rows.append(
            {
                "cycle_class": cycle_class,
                "count": count,
                "share": round(count / class_total, 6) if class_total else 0.0,
                "passive_only": 1,
                "influences_action": 0,
                "is_gate": 0,
                "is_entry_signal": 0,
            }
        )

    target_classes = {
        "zentrum_drift_zentrum",
        "zentrum_uebergang_zentrum",
        "bruecke_zentrum_bruecke",
        "drift_zentrum_bruecke",
        "uebergang_zentrum_bruecke",
        "zentrum_haelt",
    }
    target_rows = [row for row in sequence_rows if row["cycle_class"] in target_classes]
    target_rows.sort(key=lambda row: (str(row["cycle_class"]), -int(row["count"])))

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "mcm_cycle_sequences.csv",
        sequence_rows,
        [
            "sequence_length",
            "cycle_class",
            "sequence",
            "count",
            "share",
            "world_presence",
            "mean_carry",
            "mean_strain",
            "mean_rekopplung",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    _write_csv(
        out_dir / "mcm_cycle_class_summary.csv",
        class_rows,
        ["cycle_class", "count", "share", "passive_only", "influences_action", "is_gate", "is_entry_signal"],
    )
    _write_csv(
        out_dir / "mcm_target_cycle_sequences.csv",
        target_rows,
        [
            "sequence_length",
            "cycle_class",
            "sequence",
            "count",
            "share",
            "world_presence",
            "mean_carry",
            "mean_strain",
            "mean_rekopplung",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    summary = {
        "world_count": len(worlds),
        "sequence_rows": len(sequence_rows),
        "cycle_class_counts": dict(class_counts),
        "top_target_cycles": target_rows[:20],
        "interpretation": "passive_mcm_cycle_map",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "mcm_cycle_map_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive MCM-Zykluskarte bauen")
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_WORLD_DIR)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(json.dumps(run(args.matrix, args.input_dir, args.out_dir), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
