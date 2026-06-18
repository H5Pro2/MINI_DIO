from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.report_passive_reifespur_landkarte import DEFAULT_MEMORY, run as run_landkarte


DEFAULT_MATRIX = ROOT / "debug" / "dio_mini_passive_reifespur_matrix_20260618" / "reifespur_matrix.csv"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_reifespur_matrix_extension_20260618"
DEFAULT_WORLDS = [
    ROOT / "data" / "kontrolliert_2025_altseq_a_follow_10k_5m_SOLUSDT.csv",
    ROOT / "data" / "kontrolliert_2025_late_negative_10k_5m_SOLUSDT.csv",
    ROOT / "data" / "kontrolliert_2025_moderate_positive_10k_5m_SOLUSDT.csv",
    ROOT / "data" / "kontrolliert_2025_positive_recovery_10k_5m_SOLUSDT.csv",
    ROOT / "data" / "kontrolliert_2025_stress_10k_5m_SOLUSDT.csv",
]


def _safe_label(path: Path) -> str:
    return "".join(ch if ch.isalnum() or ch in ("_", "-") else "_" for ch in path.stem)


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _load_matrix(path: Path) -> dict[str, dict[str, object]]:
    entries = {}
    for row in _read_csv(path):
        symbol = str(row.get("reifespur_symbol", "") or "")
        if not symbol:
            continue
        entries[symbol] = {
            "matrix_zone": str(row.get("matrix_zone", "") or ""),
            "zone_role": str(row.get("zone_role", "") or ""),
            "candidate_kind": str(row.get("candidate_kind", "") or ""),
            "baseline_mean_share": float(row.get("mean_share", 0.0) or 0.0),
            "baseline_spread": float(row.get("spread", 0.0) or 0.0),
        }
    return entries


def _extension_state(share: float, baseline_mean: float, baseline_spread: float) -> str:
    lower = baseline_mean - baseline_spread
    upper = baseline_mean + baseline_spread
    if share < lower:
        return "unter_bisheriger_varianz"
    if share > upper:
        return "oberhalb_bisheriger_varianz"
    return "innerhalb_bisheriger_varianz"


def run(worlds: list[Path], memory_path: Path, matrix_path: Path, out_dir: Path) -> dict:
    matrix = _load_matrix(matrix_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    extension_rows: list[dict[str, object]] = []
    world_summaries: list[dict[str, object]] = []

    for world in worlds:
        label = _safe_label(world)
        summary = run_landkarte(world, memory_path, out_dir / f"world_{label}", label)
        rows = int(summary.get("rows", 0) or 0)
        counts = summary.get("nearest_symbol_counts", {}) or {}
        world_summaries.append(
            {
                "world_label": label,
                "data_path": str(world),
                "rows": rows,
                "landkarte_state_counts": summary.get("landkarte_state_counts", {}),
                "exact_candidate_kind_counts": summary.get("exact_candidate_kind_counts", {}),
            }
        )
        for symbol, matrix_entry in matrix.items():
            count = int(counts.get(symbol, 0) or 0)
            share = round(count / rows, 6) if rows else 0.0
            baseline_mean = float(matrix_entry["baseline_mean_share"])
            baseline_spread = float(matrix_entry["baseline_spread"])
            extension_rows.append(
                {
                    "world_label": label,
                    "data_path": str(world),
                    "reifespur_symbol": symbol,
                    "matrix_zone": matrix_entry["matrix_zone"],
                    "zone_role": matrix_entry["zone_role"],
                    "candidate_kind": matrix_entry["candidate_kind"],
                    "nearest_count": count,
                    "nearest_share": share,
                    "baseline_mean_share": baseline_mean,
                    "baseline_spread": baseline_spread,
                    "delta_to_baseline_mean": round(share - baseline_mean, 6),
                    "extension_state": _extension_state(share, baseline_mean, baseline_spread),
                    "passive_only": 1,
                    "influences_action": 0,
                    "is_gate": 0,
                    "is_entry_signal": 0,
                }
            )

    fieldnames = [
        "world_label",
        "data_path",
        "reifespur_symbol",
        "matrix_zone",
        "zone_role",
        "candidate_kind",
        "nearest_count",
        "nearest_share",
        "baseline_mean_share",
        "baseline_spread",
        "delta_to_baseline_mean",
        "extension_state",
        "passive_only",
        "influences_action",
        "is_gate",
        "is_entry_signal",
    ]
    _write_csv(out_dir / "reifespur_matrix_extension_rows.csv", extension_rows, fieldnames)

    state_counts: dict[str, int] = {}
    symbol_state_counts: dict[str, dict[str, int]] = {}
    for row in extension_rows:
        state = str(row["extension_state"])
        symbol = str(row["reifespur_symbol"])
        state_counts[state] = state_counts.get(state, 0) + 1
        symbol_state_counts.setdefault(symbol, {})
        symbol_state_counts[symbol][state] = symbol_state_counts[symbol].get(state, 0) + 1

    symbol_rows = []
    for symbol, states in sorted(symbol_state_counts.items()):
        entry = matrix[symbol]
        symbol_rows.append(
            {
                "reifespur_symbol": symbol,
                "matrix_zone": entry["matrix_zone"],
                "zone_role": entry["zone_role"],
                "candidate_kind": entry["candidate_kind"],
                "innerhalb_bisheriger_varianz": states.get("innerhalb_bisheriger_varianz", 0),
                "oberhalb_bisheriger_varianz": states.get("oberhalb_bisheriger_varianz", 0),
                "unter_bisheriger_varianz": states.get("unter_bisheriger_varianz", 0),
            }
        )
    _write_csv(
        out_dir / "reifespur_matrix_extension_by_symbol.csv",
        symbol_rows,
        [
            "reifespur_symbol",
            "matrix_zone",
            "zone_role",
            "candidate_kind",
            "innerhalb_bisheriger_varianz",
            "oberhalb_bisheriger_varianz",
            "unter_bisheriger_varianz",
        ],
    )

    summary = {
        "memory_path": str(memory_path),
        "matrix_path": str(matrix_path),
        "worlds": world_summaries,
        "extension_state_counts": state_counts,
        "symbol_state_counts": symbol_state_counts,
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "reifespur_matrix_extension_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Mini-DIO reifespur matrix extension diagnosis")
    parser.add_argument("--memory", type=Path, default=DEFAULT_MEMORY)
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--world", type=Path, action="append", dest="worlds")
    args = parser.parse_args()
    summary = run(args.worlds or DEFAULT_WORLDS, args.memory, args.matrix, args.out_dir)
    print(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
