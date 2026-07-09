from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _real_world_count(item: dict) -> int:
    worlds = item.get("worlds", {}) or {}
    return len([key for key, value in worlds.items() if value and not str(key).startswith("NULL_") and key != "-"])


def _null_world_count(item: dict) -> int:
    worlds = item.get("worlds", {}) or {}
    return len([key for key, value in worlds.items() if value and str(key).startswith("NULL_")])


def _count(item: dict, *, null: bool) -> int:
    worlds = item.get("worlds", {}) or {}
    total = 0
    for key, value in worlds.items():
        is_null = str(key).startswith("NULL_")
        if is_null == null:
            total += int(value or 0)
    return total


def _classify(real_item: dict, null_item: dict) -> str:
    real_worlds = _real_world_count(real_item)
    null_worlds = _null_world_count(null_item)
    real_score = float(real_item.get("depth_score", 0.0) or 0.0)
    null_score = float(null_item.get("depth_score", 0.0) or 0.0)
    real_count = _count(real_item, null=False)
    null_count = _count(null_item, null=True)
    if real_worlds >= 3 and null_worlds == 0:
        return "weltgebunden_ohne_nullspur"
    if real_worlds >= 3 and null_worlds <= 1 and null_count <= max(3, real_count * 0.05):
        return "weltgebunden_schwache_nullspur"
    if real_worlds >= 3 and null_worlds <= 2 and (real_score - null_score) >= 0.08:
        return "weltnaehe_mit_scoreabfall_in_null"
    if null_worlds >= 3 and null_score >= real_score * 0.96:
        return "allgemeiner_strukturanker"
    return "gemischte_bindung"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--real-memory", required=True)
    parser.add_argument("--null-memory", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    real_memory = _load(Path(args.real_memory)).get("passive_mcm_preview_anchor_depth_memory", {})
    null_memory = _load(Path(args.null_memory)).get("passive_mcm_preview_anchor_depth_memory", {})
    rows = []
    for symbol, real_item in real_memory.items():
        if real_item.get("depth_state") != "multiworld_depth_seed":
            continue
        null_item = null_memory.get(symbol, {})
        row = {
            "preview_symbol": symbol,
            "binding_class": _classify(real_item, null_item),
            "real_depth_state": real_item.get("depth_state", "-"),
            "null_depth_state": null_item.get("depth_state", "missing"),
            "real_world_count": _real_world_count(real_item),
            "null_world_count": _null_world_count(null_item),
            "real_count": _count(real_item, null=False),
            "null_count": _count(null_item, null=True),
            "real_depth_score": float(real_item.get("depth_score", 0.0) or 0.0),
            "null_depth_score": float(null_item.get("depth_score", 0.0) or 0.0),
            "score_delta_real_minus_null": round(
                float(real_item.get("depth_score", 0.0) or 0.0) - float(null_item.get("depth_score", 0.0) or 0.0),
                6,
            ),
            "real_profile": float(real_item.get("avg_profile_proximity", 0.0) or 0.0),
            "null_profile": float(null_item.get("avg_profile_proximity", 0.0) or 0.0),
        }
        rows.append(row)

    rows.sort(
        key=lambda row: (
            row["binding_class"],
            -int(row["real_world_count"]),
            int(row["null_world_count"]),
            -float(row["real_depth_score"]),
        )
    )

    out = Path(args.out_csv)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else [])
        if rows:
            writer.writeheader()
            writer.writerows(rows)

    print(f"wrote={out} rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
