from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = ROOT / "debug" / "dio_mini_passive_topology_year_hardtest_worlds_20260618"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_nu25d5_kippzonen_zeitlupe_20260618"
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


def _mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def _dominant(counter: Counter[str]) -> str:
    return counter.most_common(1)[0][0] if counter else "-"


def _quality(row: dict[str, str]) -> str:
    effect = str(row.get("effect_class", "-") or "-")
    carry = _as_float(row, "mcm_carry_quality")
    strain = _as_float(row, "mcm_strain_quality")
    rekopplung = _as_float(row, "mcm_rekopplung_quality")
    if effect in {"gespannt", "kippend"} or strain >= 0.26:
        return "randspannung"
    if effect in {"tragend_unruhig", "stabil"} and carry >= 0.28 and strain <= 0.20:
        return "brueckenfaehig"
    if effect == "rekoppelnd" or rekopplung >= 0.66:
        return "rekoppelnd"
    if strain <= 0.16:
        return "entlastend"
    return "gemischt"


def _window(rows: list[dict[str, str]], index: int, radius: int) -> list[dict[str, str]]:
    start = max(0, index - radius)
    end = min(len(rows), index + radius + 1)
    return rows[start:end]


def _summarize_window(world_label: str, center: dict[str, str], rows: list[dict[str, str]], phase: str) -> dict[str, object]:
    qualities = Counter(_quality(row) for row in rows)
    effects = Counter(str(row.get("effect_class", "-") or "-") for row in rows)
    symbols = Counter(str(row.get("nearest_reifespur_symbol", "-") or "-") for row in rows)
    return {
        "world_label": world_label,
        "center_tick": center.get("tick", "0"),
        "center_timestamp_ms": center.get("timestamp_ms", "0"),
        "phase": phase,
        "window_size": len(rows),
        "dominant_quality": _dominant(qualities),
        "dominant_effect": _dominant(effects),
        "target_share_in_window": round(symbols.get(TARGET, 0) / len(rows), 6) if rows else 0.0,
        "randspannung_share": round(qualities.get("randspannung", 0) / len(rows), 6) if rows else 0.0,
        "brueckenfaehig_share": round(qualities.get("brueckenfaehig", 0) / len(rows), 6) if rows else 0.0,
        "entlastend_share": round(qualities.get("entlastend", 0) / len(rows), 6) if rows else 0.0,
        "rekoppelnd_share": round(qualities.get("rekoppelnd", 0) / len(rows), 6) if rows else 0.0,
        "mean_carry": _mean([_as_float(row, "mcm_carry_quality") for row in rows]),
        "mean_strain": _mean([_as_float(row, "mcm_strain_quality") for row in rows]),
        "mean_rekopplung": _mean([_as_float(row, "mcm_rekopplung_quality") for row in rows]),
    }


def _iter_worlds(input_dir: Path) -> list[tuple[str, list[dict[str, str]]]]:
    worlds: list[tuple[str, list[dict[str, str]]]] = []
    for world_dir in sorted(input_dir.glob("world_*")):
        path = world_dir / "reifespur_landkarte_rows.csv"
        if not path.exists():
            continue
        rows = sorted(_read_csv(path), key=lambda row: int(row.get("tick", 0) or 0))
        worlds.append((world_dir.name.removeprefix("world_"), rows))
    return worlds


def run(input_dir: Path, out_dir: Path, radius: int) -> dict[str, object]:
    worlds = _iter_worlds(input_dir)
    event_rows: list[dict[str, object]] = []
    window_rows: list[dict[str, object]] = []
    world_rows: list[dict[str, object]] = []

    for world_label, rows in worlds:
        target_indices = [idx for idx, row in enumerate(rows) if row.get("nearest_reifespur_symbol") == TARGET]
        kipp_events = 0
        world_quality = Counter()
        for idx in target_indices:
            current = rows[idx]
            prev = rows[idx - 1] if idx > 0 else current
            nxt = rows[idx + 1] if idx + 1 < len(rows) else current
            prev_q = _quality(prev)
            current_q = _quality(current)
            next_q = _quality(nxt)
            world_quality[current_q] += 1
            if prev_q == "randspannung" and current_q in {"brueckenfaehig", "entlastend", "rekoppelnd"}:
                event_type = "randspannung_zu_bruecke"
            elif current_q == "randspannung" and next_q in {"brueckenfaehig", "entlastend", "rekoppelnd"}:
                event_type = "kippvorfeld_randspannung"
            elif prev_q in {"brueckenfaehig", "entlastend", "rekoppelnd"} and current_q == "randspannung":
                event_type = "bruecke_zu_randspannung"
            else:
                event_type = "kein_kippereignis"
            if event_type != "kein_kippereignis":
                kipp_events += 1
                event_rows.append(
                    {
                        "world_label": world_label,
                        "tick": current.get("tick", "0"),
                        "timestamp_ms": current.get("timestamp_ms", "0"),
                        "event_type": event_type,
                        "prev_quality": prev_q,
                        "current_quality": current_q,
                        "next_quality": next_q,
                        "current_effect": current.get("effect_class", "-"),
                        "current_similarity": current.get("nearest_similarity", "0"),
                        "current_carry": _as_float(current, "mcm_carry_quality"),
                        "current_strain": _as_float(current, "mcm_strain_quality"),
                        "current_rekopplung": _as_float(current, "mcm_rekopplung_quality"),
                    }
                )
                before = _window(rows, max(0, idx - radius), radius)
                center = _window(rows, idx, radius)
                after = _window(rows, min(len(rows) - 1, idx + radius), radius)
                window_rows.append(_summarize_window(world_label, current, before, "vorfeld"))
                window_rows.append(_summarize_window(world_label, current, center, "kippbereich"))
                window_rows.append(_summarize_window(world_label, current, after, "nachfeld"))

        world_rows.append(
            {
                "world_label": world_label,
                "rows": len(rows),
                "nu25d5_hits": len(target_indices),
                "kipp_events": kipp_events,
                "kipp_event_share_of_nu25d5": round(kipp_events / len(target_indices), 6) if target_indices else 0.0,
                "dominant_nu25d5_quality": _dominant(world_quality),
                "nu25d5_randspannung_share": round(world_quality.get("randspannung", 0) / len(target_indices), 6) if target_indices else 0.0,
                "nu25d5_brueckenfaehig_share": round(world_quality.get("brueckenfaehig", 0) / len(target_indices), 6) if target_indices else 0.0,
                "nu25d5_entlastend_share": round(world_quality.get("entlastend", 0) / len(target_indices), 6) if target_indices else 0.0,
                "nu25d5_rekoppelnd_share": round(world_quality.get("rekoppelnd", 0) / len(target_indices), 6) if target_indices else 0.0,
            }
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "nu25d5_kippzonen_events.csv",
        event_rows,
        [
            "world_label",
            "tick",
            "timestamp_ms",
            "event_type",
            "prev_quality",
            "current_quality",
            "next_quality",
            "current_effect",
            "current_similarity",
            "current_carry",
            "current_strain",
            "current_rekopplung",
        ],
    )
    _write_csv(
        out_dir / "nu25d5_kippzonen_windows.csv",
        window_rows,
        [
            "world_label",
            "center_tick",
            "center_timestamp_ms",
            "phase",
            "window_size",
            "dominant_quality",
            "dominant_effect",
            "target_share_in_window",
            "randspannung_share",
            "brueckenfaehig_share",
            "entlastend_share",
            "rekoppelnd_share",
            "mean_carry",
            "mean_strain",
            "mean_rekopplung",
        ],
    )
    _write_csv(
        out_dir / "nu25d5_kippzonen_by_world.csv",
        world_rows,
        [
            "world_label",
            "rows",
            "nu25d5_hits",
            "kipp_events",
            "kipp_event_share_of_nu25d5",
            "dominant_nu25d5_quality",
            "nu25d5_randspannung_share",
            "nu25d5_brueckenfaehig_share",
            "nu25d5_entlastend_share",
            "nu25d5_rekoppelnd_share",
        ],
    )
    event_counter = Counter(str(row["event_type"]) for row in event_rows)
    summary = {
        "world_count": len(worlds),
        "event_count": len(event_rows),
        "event_type_counts": dict(event_counter),
        "worlds": world_rows,
        "interpretation": "nu25d5_kippzonen_zeitlupe_built",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "nu25d5_kippzonen_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive nu25d5 Kippzonen-Zeitlupe")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_IN)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--radius", type=int, default=6)
    args = parser.parse_args()
    print(json.dumps(run(args.input_dir, args.out_dir, args.radius), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
