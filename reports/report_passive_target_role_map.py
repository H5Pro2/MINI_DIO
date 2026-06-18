from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = ROOT / "debug" / "dio_mini_passive_target_access_dynamics_20260618"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_target_role_map_20260618"


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


def _as_int(row: dict[str, str], key: str) -> int:
    return int(float(row.get(key, 0) or 0))


def _median(values: list[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2.0


def _role(row: dict[str, object], med_self_share: float, med_prev_count: float, med_count: float) -> str:
    self_share = float(row["self_share"])
    prev_count = float(row["prev_symbol_count"])
    count = float(row["count"])
    quality = str(row["dominant_transition_quality"])
    dominant_prev = str(row["dominant_prev_symbol"])
    target = str(row["target_symbol"])

    self_near = dominant_prev == target and self_share >= med_self_share
    open_access = prev_count >= med_prev_count
    strong_presence = count >= med_count

    if self_near and strong_presence and quality in {"tragend_steigend", "entlastend"}:
        return "zentrum_nahe_stabilisierung"
    if self_near and quality in {"tragend_fallend", "entlastend"}:
        return "selbstnah_driftend"
    if open_access and quality in {"tragend_steigend", "rekoppelnd"}:
        return "offene_bruecke_tragend"
    if open_access and quality in {"tragend_fallend", "entlastend"}:
        return "offene_bruecke_entlastend"
    if quality == "belastend":
        return "spannungsrand_belastend"
    return "gemischter_zielraum"


def run(input_dir: Path, out_dir: Path) -> dict[str, object]:
    target_rows_raw = _read_csv(input_dir / "target_access_dynamics_by_target.csv")
    pair_rows = _read_csv(input_dir / "target_access_dynamics_by_pair.csv")

    self_share_by_target: dict[str, float] = {}
    for pair in pair_rows:
        target = pair.get("target_symbol", "")
        if target and pair.get("prev_symbol") == target:
            self_share_by_target[target] = _as_float(pair, "share_of_target")

    counts = [_as_float(row, "count") for row in target_rows_raw]
    prev_counts = [_as_float(row, "prev_symbol_count") for row in target_rows_raw]
    self_shares = [self_share_by_target.get(row.get("target_symbol", ""), 0.0) for row in target_rows_raw]
    med_count = _median(counts)
    med_prev_count = _median(prev_counts)
    med_self_share = _median(self_shares)

    role_rows: list[dict[str, object]] = []
    for row in target_rows_raw:
        target = row.get("target_symbol", "")
        item = {
            "target_symbol": target,
            "count": _as_int(row, "count"),
            "world_presence": _as_int(row, "world_presence"),
            "prev_symbol_count": _as_int(row, "prev_symbol_count"),
            "self_share": round(self_share_by_target.get(target, 0.0), 6),
            "dominant_prev_symbol": row.get("dominant_prev_symbol", "-"),
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
        item["target_role"] = _role(item, med_self_share, med_prev_count, med_count)
        role_rows.append(item)

    role_rows.sort(key=lambda item: (str(item["target_role"]), -int(item["count"])))
    role_counts: dict[str, int] = {}
    for row in role_rows:
        role = str(row["target_role"])
        role_counts[role] = role_counts.get(role, 0) + 1

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "target_role_map.csv",
        role_rows,
        [
            "target_symbol",
            "target_role",
            "count",
            "world_presence",
            "prev_symbol_count",
            "self_share",
            "dominant_prev_symbol",
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
    summary = {
        "target_count": len(role_rows),
        "role_counts": role_counts,
        "medians": {
            "count": round(med_count, 6),
            "prev_symbol_count": round(med_prev_count, 6),
            "self_share": round(med_self_share, 6),
        },
        "top_roles": role_rows,
        "interpretation": "passive_target_role_map_built",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "target_role_map_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Zielraum-Rollenkarte")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_IN)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(json.dumps(run(args.input_dir, args.out_dir), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
