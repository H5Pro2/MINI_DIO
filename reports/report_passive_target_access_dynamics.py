from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = ROOT / "debug" / "dio_mini_passive_reifespur_matrix_extension_20260618"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_target_access_dynamics_20260618"


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


def _mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def _share(count: int, total: int) -> float:
    return round(count / total, 6) if total else 0.0


def _dominant(counter: Counter[str]) -> str:
    return counter.most_common(1)[0][0] if counter else "-"


def _transition_quality(prev: dict[str, str], current: dict[str, str]) -> str:
    carry_delta = _as_float(current, "mcm_carry_quality") - _as_float(prev, "mcm_carry_quality")
    strain_delta = _as_float(current, "mcm_strain_quality") - _as_float(prev, "mcm_strain_quality")
    rekopplung_delta = _as_float(current, "mcm_rekopplung_quality") - _as_float(prev, "mcm_rekopplung_quality")
    strongest = max(
        [
            ("carry", abs(carry_delta), carry_delta),
            ("strain", abs(strain_delta), strain_delta),
            ("rekopplung", abs(rekopplung_delta), rekopplung_delta),
        ],
        key=lambda item: item[1],
    )
    axis, _, delta = strongest
    if axis == "rekopplung" and delta > 0:
        return "rekoppelnd"
    if axis == "rekopplung" and delta < 0:
        return "entkoppelnd"
    if axis == "strain" and delta < 0:
        return "entlastend"
    if axis == "strain" and delta > 0:
        return "belastend"
    if axis == "carry" and delta > 0:
        return "tragend_steigend"
    if axis == "carry" and delta < 0:
        return "tragend_fallend"
    return "stabil"


def _iter_world_rows(input_dir: Path) -> list[tuple[str, list[dict[str, str]]]]:
    worlds: list[tuple[str, list[dict[str, str]]]] = []
    for world_dir in sorted(input_dir.glob("world_*")):
        rows_path = world_dir / "reifespur_landkarte_rows.csv"
        if rows_path.exists():
            rows = _read_csv(rows_path)
            worlds.append((world_dir.name.removeprefix("world_"), rows))
    return worlds


def run(input_dir: Path, out_dir: Path) -> dict[str, object]:
    worlds = _iter_world_rows(input_dir)
    transitions: list[dict[str, object]] = []
    by_target_prev: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    by_target: dict[str, list[dict[str, object]]] = defaultdict(list)

    for world_label, rows in worlds:
        ordered = sorted(rows, key=lambda row: int(row.get("tick", 0) or 0))
        for prev, current in zip(ordered, ordered[1:]):
            prev_symbol = str(prev.get("nearest_reifespur_symbol", "-") or "-")
            current_symbol = str(current.get("nearest_reifespur_symbol", "-") or "-")
            if not current_symbol or current_symbol == "-":
                continue
            item = {
                "world_label": world_label,
                "tick": current.get("tick", "0"),
                "timestamp_ms": current.get("timestamp_ms", "0"),
                "prev_symbol": prev_symbol,
                "target_symbol": current_symbol,
                "transition_quality": _transition_quality(prev, current),
                "prev_effect": prev.get("effect_class", "-"),
                "target_effect": current.get("effect_class", "-"),
                "prev_landkarte_state": prev.get("landkarte_state", "-"),
                "target_landkarte_state": current.get("landkarte_state", "-"),
                "prev_carry": _as_float(prev, "mcm_carry_quality"),
                "target_carry": _as_float(current, "mcm_carry_quality"),
                "delta_carry": round(_as_float(current, "mcm_carry_quality") - _as_float(prev, "mcm_carry_quality"), 6),
                "prev_strain": _as_float(prev, "mcm_strain_quality"),
                "target_strain": _as_float(current, "mcm_strain_quality"),
                "delta_strain": round(_as_float(current, "mcm_strain_quality") - _as_float(prev, "mcm_strain_quality"), 6),
                "prev_rekopplung": _as_float(prev, "mcm_rekopplung_quality"),
                "target_rekopplung": _as_float(current, "mcm_rekopplung_quality"),
                "delta_rekopplung": round(_as_float(current, "mcm_rekopplung_quality") - _as_float(prev, "mcm_rekopplung_quality"), 6),
            }
            transitions.append(item)
            by_target_prev[(current_symbol, prev_symbol)].append(item)
            by_target[current_symbol].append(item)

    pair_rows: list[dict[str, object]] = []
    for (target_symbol, prev_symbol), items in sorted(by_target_prev.items(), key=lambda entry: len(entry[1]), reverse=True):
        quality = Counter(str(item["transition_quality"]) for item in items)
        worlds_seen = Counter(str(item["world_label"]) for item in items)
        count = len(items)
        target_total = len(by_target[target_symbol])
        pair_rows.append(
            {
                "target_symbol": target_symbol,
                "prev_symbol": prev_symbol,
                "count": count,
                "share_of_target": _share(count, target_total),
                "world_presence": len(worlds_seen),
                "dominant_transition_quality": _dominant(quality),
                "rekoppelnd_share": _share(quality.get("rekoppelnd", 0), count),
                "entlastend_share": _share(quality.get("entlastend", 0), count),
                "belastend_share": _share(quality.get("belastend", 0), count),
                "entkoppelnd_share": _share(quality.get("entkoppelnd", 0), count),
                "tragend_steigend_share": _share(quality.get("tragend_steigend", 0), count),
                "tragend_fallend_share": _share(quality.get("tragend_fallend", 0), count),
                "mean_delta_carry": _mean([float(item["delta_carry"]) for item in items]),
                "mean_delta_strain": _mean([float(item["delta_strain"]) for item in items]),
                "mean_delta_rekopplung": _mean([float(item["delta_rekopplung"]) for item in items]),
            }
        )

    target_rows: list[dict[str, object]] = []
    for target_symbol, items in sorted(by_target.items(), key=lambda entry: len(entry[1]), reverse=True):
        quality = Counter(str(item["transition_quality"]) for item in items)
        prevs = Counter(str(item["prev_symbol"]) for item in items)
        worlds_seen = Counter(str(item["world_label"]) for item in items)
        count = len(items)
        target_rows.append(
            {
                "target_symbol": target_symbol,
                "count": count,
                "world_presence": len(worlds_seen),
                "prev_symbol_count": len(prevs),
                "dominant_prev_symbol": _dominant(prevs),
                "dominant_transition_quality": _dominant(quality),
                "rekoppelnd_share": _share(quality.get("rekoppelnd", 0), count),
                "entlastend_share": _share(quality.get("entlastend", 0), count),
                "belastend_share": _share(quality.get("belastend", 0), count),
                "entkoppelnd_share": _share(quality.get("entkoppelnd", 0), count),
                "tragend_steigend_share": _share(quality.get("tragend_steigend", 0), count),
                "tragend_fallend_share": _share(quality.get("tragend_fallend", 0), count),
                "mean_delta_carry": _mean([float(item["delta_carry"]) for item in items]),
                "mean_delta_strain": _mean([float(item["delta_strain"]) for item in items]),
                "mean_delta_rekopplung": _mean([float(item["delta_rekopplung"]) for item in items]),
            }
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "target_access_dynamics_by_pair.csv",
        pair_rows,
        [
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
        out_dir / "target_access_dynamics_by_target.csv",
        target_rows,
        [
            "target_symbol",
            "count",
            "world_presence",
            "prev_symbol_count",
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
    _write_csv(
        out_dir / "target_access_dynamics_events_sample.csv",
        transitions[:2000],
        [
            "world_label",
            "tick",
            "timestamp_ms",
            "prev_symbol",
            "target_symbol",
            "transition_quality",
            "prev_effect",
            "target_effect",
            "prev_landkarte_state",
            "target_landkarte_state",
            "prev_carry",
            "target_carry",
            "delta_carry",
            "prev_strain",
            "target_strain",
            "delta_strain",
            "prev_rekopplung",
            "target_rekopplung",
            "delta_rekopplung",
        ],
    )
    summary = {
        "world_count": len(worlds),
        "transition_count": len(transitions),
        "target_count": len(target_rows),
        "pair_count": len(pair_rows),
        "top_targets": target_rows[:5],
        "interpretation": "passive_target_access_dynamics_built",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "target_access_dynamics_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Zielraum-Zugangsdynamik ueber mehrere Reifespuren")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_IN)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(json.dumps(run(args.input_dir, args.out_dir), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
