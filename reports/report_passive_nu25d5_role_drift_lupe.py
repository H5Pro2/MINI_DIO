from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE = ROOT / "debug" / "dio_mini_passive_target_access_dynamics_20260618" / "target_access_dynamics_by_pair.csv"
DEFAULT_YEAR = ROOT / "debug" / "dio_mini_passive_target_access_dynamics_year_hardtest_20260618" / "target_access_dynamics_by_pair.csv"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_nu25d5_role_drift_lupe_20260618"
TARGET = "dio_reifespur_nu25d5"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _as_float(row: dict[str, str], key: str) -> float:
    return float(row.get(key, 0.0) or 0.0)


def _target_rows(path: Path, phase: str) -> list[dict[str, object]]:
    rows = [row for row in _read_csv(path) if row.get("target_symbol") == TARGET]
    result: list[dict[str, object]] = []
    for row in rows:
        result.append(
            {
                "phase": phase,
                "target_symbol": row.get("target_symbol", ""),
                "prev_symbol": row.get("prev_symbol", ""),
                "count": int(float(row.get("count", 0) or 0)),
                "share_of_target": _as_float(row, "share_of_target"),
                "world_presence": int(float(row.get("world_presence", 0) or 0)),
                "dominant_transition_quality": row.get("dominant_transition_quality", "-"),
                "rekoppelnd_share": _as_float(row, "rekoppelnd_share"),
                "entlastend_share": _as_float(row, "entlastend_share"),
                "belastend_share": _as_float(row, "belastend_share"),
                "entkoppelnd_share": _as_float(row, "entkoppelnd_share"),
                "tragend_steigend_share": _as_float(row, "tragend_steigend_share"),
                "tragend_fallend_share": _as_float(row, "tragend_fallend_share"),
                "mean_delta_carry": _as_float(row, "mean_delta_carry"),
                "mean_delta_strain": _as_float(row, "mean_delta_strain"),
                "mean_delta_rekopplung": _as_float(row, "mean_delta_rekopplung"),
            }
        )
    result.sort(key=lambda item: int(item["count"]), reverse=True)
    return result


def run(base_path: Path, year_path: Path, out_dir: Path) -> dict[str, object]:
    base_rows = _target_rows(base_path, "base_10k")
    year_rows = _target_rows(year_path, "year_hardtest")
    combined = base_rows + year_rows

    by_prev_base = {str(row["prev_symbol"]): row for row in base_rows}
    by_prev_year = {str(row["prev_symbol"]): row for row in year_rows}
    prev_symbols = sorted(set(by_prev_base) | set(by_prev_year))
    compare_rows: list[dict[str, object]] = []
    for prev_symbol in prev_symbols:
        base = by_prev_base.get(prev_symbol, {})
        year = by_prev_year.get(prev_symbol, {})
        compare_rows.append(
            {
                "prev_symbol": prev_symbol,
                "base_share": base.get("share_of_target", 0.0),
                "year_share": year.get("share_of_target", 0.0),
                "delta_share": round(float(year.get("share_of_target", 0.0)) - float(base.get("share_of_target", 0.0)), 6),
                "base_quality": base.get("dominant_transition_quality", "-"),
                "year_quality": year.get("dominant_transition_quality", "-"),
                "quality_stable": int(base.get("dominant_transition_quality", "-") == year.get("dominant_transition_quality", "-")),
                "base_belastend_share": base.get("belastend_share", 0.0),
                "year_belastend_share": year.get("belastend_share", 0.0),
                "delta_belastend_share": round(float(year.get("belastend_share", 0.0)) - float(base.get("belastend_share", 0.0)), 6),
                "base_entlastend_share": base.get("entlastend_share", 0.0),
                "year_entlastend_share": year.get("entlastend_share", 0.0),
                "delta_entlastend_share": round(float(year.get("entlastend_share", 0.0)) - float(base.get("entlastend_share", 0.0)), 6),
                "base_tragend_fallend_share": base.get("tragend_fallend_share", 0.0),
                "year_tragend_fallend_share": year.get("tragend_fallend_share", 0.0),
                "delta_tragend_fallend_share": round(float(year.get("tragend_fallend_share", 0.0)) - float(base.get("tragend_fallend_share", 0.0)), 6),
            }
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "nu25d5_role_drift_rows.csv",
        combined,
        [
            "phase",
            "target_symbol",
            "prev_symbol",
            "count",
            "share_of_target",
            "world_presence",
            "dominant_transition_quality",
            "rekoppelnd_share",
            "entlastend_share",
            "belastend_share",
            "entkoppelnd_share",
            "tragend_steigend_share",
            "tragend_fallend_share",
            "mean_delta_carry",
            "mean_delta_strain",
            "mean_delta_rekopplung",
        ],
    )
    _write_csv(
        out_dir / "nu25d5_role_drift_compare.csv",
        compare_rows,
        [
            "prev_symbol",
            "base_share",
            "year_share",
            "delta_share",
            "base_quality",
            "year_quality",
            "quality_stable",
            "base_belastend_share",
            "year_belastend_share",
            "delta_belastend_share",
            "base_entlastend_share",
            "year_entlastend_share",
            "delta_entlastend_share",
            "base_tragend_fallend_share",
            "year_tragend_fallend_share",
            "delta_tragend_fallend_share",
        ],
    )

    top_base = base_rows[0] if base_rows else {}
    top_year = year_rows[0] if year_rows else {}
    summary = {
        "target_symbol": TARGET,
        "base_top_prev": top_base,
        "year_top_prev": top_year,
        "prev_symbol_count": len(prev_symbols),
        "quality_stable_count": sum(int(row["quality_stable"]) for row in compare_rows),
        "interpretation": "nu25d5_role_drift_lupe_built",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "nu25d5_role_drift_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive nu25d5 Rollen-Drift-Lupe")
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--year", type=Path, default=DEFAULT_YEAR)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(json.dumps(run(args.base, args.year, args.out_dir), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
