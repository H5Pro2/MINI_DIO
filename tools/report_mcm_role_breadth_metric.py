from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


def _float(value: Any) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _milieu_name(world: str) -> str:
    upper = world.upper()
    if "QUIET" in upper:
        return "quiet"
    if "STRESS" in upper:
        return "stress"
    if "SHIFT" in upper:
        return "shift"
    if "PAXG" in upper:
        return "paxg"
    if "BTC" in upper:
        return "btc"
    if "SOL" in upper:
        return "sol"
    if "DOGE" in upper:
        return "doge"
    if "XRP" in upper:
        return "xrp"
    if "SYNTH" in upper or "NULL" in upper:
        return "synthetic"
    return "other"


def _entropy(counter: Counter[str]) -> float:
    total = sum(counter.values())
    if total <= 0:
        return 0.0
    entropy = 0.0
    for value in counter.values():
        p = value / total
        if p > 0.0:
            entropy -= p * math.log(p)
    max_entropy = math.log(max(1, len(counter)))
    if max_entropy <= 0.0:
        return 0.0
    return entropy / max_entropy


def _scores(count: int, world_count: int, top_world_share: float, milieu_counter: Counter[str]) -> dict[str, float]:
    total = max(1, sum(milieu_counter.values()))
    quiet_share = milieu_counter.get("quiet", 0) / total
    stress_share = milieu_counter.get("stress", 0) / total
    shift_share = milieu_counter.get("shift", 0) / total
    top_milieu_share = 0.0
    if milieu_counter:
        top_milieu_share = milieu_counter.most_common(1)[0][1] / total

    count_weight = _clamp(math.log10(max(1, count)) / 4.0)
    world_weight = _clamp(math.log(max(1, world_count), 2) / 5.0)
    distribution = _entropy(milieu_counter)
    stress_shift_share = stress_share + shift_share

    broad_score = _clamp(count_weight * world_weight * (0.45 + 0.55 * distribution) * (1.0 - top_world_share * 0.35))
    transition_score = _clamp(count_weight * world_weight * min(1.0, (stress_shift_share * 2.4) + (distribution * 0.25)))
    milieu_score = _clamp(count_weight * top_milieu_share * (1.0 - world_weight * 0.22))
    side_score = _clamp((1.0 - count_weight) * 0.65 + (1.0 - world_weight) * 0.35)

    return {
        "grundrolle_score": broad_score,
        "uebergangsrolle_score": transition_score,
        "milieurolle_score": milieu_score,
        "nebenrolle_score": side_score,
        "quiet_share": quiet_share,
        "stress_share": stress_share,
        "shift_share": shift_share,
        "stress_shift_share": stress_shift_share,
        "top_milieu_share": top_milieu_share,
        "distribution_entropy": distribution,
    }


def _role_reading(scores: dict[str, float]) -> str:
    keys = [
        ("breite_grundrolle", scores["grundrolle_score"]),
        ("uebergangsrolle", scores["uebergangsrolle_score"]),
        ("milieurolle", scores["milieurolle_score"]),
        ("nebenrolle", scores["nebenrolle_score"]),
    ]
    return max(keys, key=lambda item: item[1])[0]


def _load_memory(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    memory = data.get("passive_mcm_preview_anchor_depth_memory", {})
    if not isinstance(memory, dict):
        return {}
    return memory


def main() -> int:
    parser = argparse.ArgumentParser(description="Passive Rollenbreiten-Metrik fuer MCM-Preview-Anker.")
    parser.add_argument("--memory", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", default="")
    parser.add_argument("--target", action="append", default=[])
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()

    memory_path = Path(args.memory)
    memory = _load_memory(memory_path)
    targets = set(args.target or [])

    rows: list[dict[str, Any]] = []
    for symbol, item in memory.items():
        if targets and symbol not in targets:
            continue
        worlds = Counter(item.get("worlds", {}) or {})
        count = int(item.get("count", 0) or 0)
        world_count = int(item.get("world_count", len(worlds)) or 0)
        total_world_hits = max(1, sum(worlds.values()))
        top_world_share = 0.0
        top_world = "-"
        if worlds:
            top_world, top_count = worlds.most_common(1)[0]
            top_world_share = top_count / total_world_hits
        milieu_counter: Counter[str] = Counter()
        for world, value in worlds.items():
            milieu_counter[_milieu_name(world)] += int(value)
        scores = _scores(count, world_count, top_world_share, milieu_counter)
        row = {
            "preview_symbol": symbol,
            "role_reading": _role_reading(scores),
            "count": count,
            "world_count": world_count,
            "depth_score": round(_float(item.get("depth_score")), 6),
            "top_world": top_world,
            "top_world_share": round(top_world_share, 6),
            "top_worlds": ";".join(f"{key}:{value}" for key, value in worlds.most_common(10)),
            "milieu_counts": ";".join(f"{key}:{value}" for key, value in milieu_counter.most_common()),
            **{key: round(value, 6) for key, value in scores.items()},
        }
        rows.append(row)

    rows.sort(
        key=lambda row: (
            float(row["grundrolle_score"]),
            float(row["uebergangsrolle_score"]),
            float(row["milieurolle_score"]),
            int(row["count"]),
        ),
        reverse=True,
    )
    if args.limit and args.limit > 0:
        rows = rows[: args.limit]

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        with out_csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    else:
        out_csv.write_text("preview_symbol,role_reading,count,world_count\n", encoding="utf-8")

    if args.out_md:
        out_md = Path(args.out_md)
        out_md.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# MCM-Rollenbreiten-Metrik",
            "",
            "## Zweck",
            "",
            "Diese Diagnose liest vorhandene Preview-Anker passiv nach Rollenbreite.",
            "Sie verändert keine Feldmechanik und erzeugt keine Handlungssignale.",
            "",
            "## Lesarten",
            "",
            "- `breite_grundrolle`: viele Welten, breite Verteilung, hohe Wiederkehr",
            "- `uebergangsrolle`: deutliche Stress-/Shift- oder Milieu-Überbrückung",
            "- `milieurolle`: hohe Spezifität für ein Milieu",
            "- `nebenrolle`: geringe Breite oder geringe Wiederkehr",
            "",
            "## Top-Rollen",
            "",
            "| Rolle | Lesart | Count | Welten | Top-Welt | Breite | Übergang | Milieu | Neben |",
            "|---|---:|---:|---:|---|---:|---:|---:|---:|",
        ]
        for row in rows[:25]:
            lines.append(
                "| {preview_symbol} | {role_reading} | {count} | {world_count} | {top_world} | "
                "{grundrolle_score:.3f} | {uebergangsrolle_score:.3f} | {milieurolle_score:.3f} | {nebenrolle_score:.3f} |".format(
                    **row
                )
            )
        lines.extend(
            [
                "",
            ]
        )
        out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote={out_csv}")
    if args.out_md:
        print(f"wrote={args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
