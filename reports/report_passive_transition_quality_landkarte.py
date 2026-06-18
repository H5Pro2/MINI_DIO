from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = ROOT / "debug" / "dio_mini_passive_topology_year_hardtest_worlds_20260618"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_transition_quality_landkarte_20260618"


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


def _field_quality(row: dict[str, str]) -> str:
    effect = str(row.get("effect_class", "-") or "-")
    carry = _as_float(row, "mcm_carry_quality")
    strain = _as_float(row, "mcm_strain_quality")
    rekopplung = _as_float(row, "mcm_rekopplung_quality")
    if effect in {"gespannt", "kippend"} or strain >= 0.26:
        return "randspannungsnah"
    if effect in {"tragend_unruhig", "stabil"} and carry >= 0.28 and strain <= 0.20:
        return "brueckenfaehig"
    if effect == "rekoppelnd" or rekopplung >= 0.66:
        return "rekoppelnd"
    if strain <= 0.16:
        return "stabil_entlastet"
    return "gemischt"


def _transition_quality(prev: dict[str, str], current: dict[str, str], nxt: dict[str, str]) -> str:
    prev_q = _field_quality(prev)
    current_q = _field_quality(current)
    next_q = _field_quality(nxt)
    if current_q == "randspannungsnah" and next_q in {"brueckenfaehig", "stabil_entlastet", "rekoppelnd"}:
        return "weich_kippend"
    if prev_q == "randspannungsnah" and current_q in {"brueckenfaehig", "stabil_entlastet", "rekoppelnd"}:
        return "uebergang_entlastend"
    if prev_q in {"brueckenfaehig", "stabil_entlastet", "rekoppelnd"} and current_q == "randspannungsnah":
        return "uebergang_belastend"
    if current_q == "brueckenfaehig":
        return "brueckenfaehig"
    if current_q == "randspannungsnah":
        return "randspannungsnah"
    if current_q == "stabil_entlastet":
        return "stabil"
    return "offen_gemischt"


def _iter_worlds(input_dir: Path) -> list[tuple[str, Path]]:
    worlds: list[tuple[str, Path]] = []
    for world_dir in sorted(input_dir.glob("world_*")):
        rows_path = world_dir / "reifespur_landkarte_rows.csv"
        if rows_path.exists():
            worlds.append((world_dir.name.removeprefix("world_"), rows_path))
    return worlds


def run(input_dir: Path, out_dir: Path) -> dict[str, object]:
    worlds = _iter_worlds(input_dir)
    all_rows: list[dict[str, object]] = []
    by_world_rows: list[dict[str, object]] = []
    by_symbol_rows: list[dict[str, object]] = []
    symbol_quality: dict[str, Counter[str]] = defaultdict(Counter)
    symbol_counts: Counter[str] = Counter()

    for world_label, rows_path in worlds:
        rows = sorted(_read_csv(rows_path), key=lambda row: int(row.get("tick", 0) or 0))
        world_counter: Counter[str] = Counter()
        for idx, current in enumerate(rows):
            prev = rows[idx - 1] if idx > 0 else current
            nxt = rows[idx + 1] if idx + 1 < len(rows) else current
            transition_quality = _transition_quality(prev, current, nxt)
            field_quality = _field_quality(current)
            symbol = str(current.get("nearest_reifespur_symbol", "-") or "-")
            world_counter[transition_quality] += 1
            symbol_quality[symbol][transition_quality] += 1
            symbol_counts[symbol] += 1
            all_rows.append(
                {
                    "world_label": world_label,
                    "tick": current.get("tick", "0"),
                    "timestamp_ms": current.get("timestamp_ms", "0"),
                    "nearest_reifespur_symbol": symbol,
                    "landkarte_state": current.get("landkarte_state", "-"),
                    "effect_class": current.get("effect_class", "-"),
                    "field_quality": field_quality,
                    "uebergangsqualitaet": transition_quality,
                    "mcm_carry_quality": _as_float(current, "mcm_carry_quality"),
                    "mcm_strain_quality": _as_float(current, "mcm_strain_quality"),
                    "mcm_rekopplung_quality": _as_float(current, "mcm_rekopplung_quality"),
                    "passive_only": 1,
                    "influences_action": 0,
                    "is_gate": 0,
                    "is_entry_signal": 0,
                }
            )
        total = sum(world_counter.values())
        by_world_rows.append(
            {
                "world_label": world_label,
                "rows": total,
                "dominant_uebergangsqualitaet": _dominant(world_counter),
                "stabil_share": round(world_counter.get("stabil", 0) / total, 6) if total else 0.0,
                "brueckenfaehig_share": round(world_counter.get("brueckenfaehig", 0) / total, 6) if total else 0.0,
                "randspannungsnah_share": round(world_counter.get("randspannungsnah", 0) / total, 6) if total else 0.0,
                "weich_kippend_share": round(world_counter.get("weich_kippend", 0) / total, 6) if total else 0.0,
                "uebergang_entlastend_share": round(world_counter.get("uebergang_entlastend", 0) / total, 6) if total else 0.0,
                "uebergang_belastend_share": round(world_counter.get("uebergang_belastend", 0) / total, 6) if total else 0.0,
                "offen_gemischt_share": round(world_counter.get("offen_gemischt", 0) / total, 6) if total else 0.0,
            }
        )

    for symbol, counter in sorted(symbol_quality.items()):
        total = symbol_counts[symbol]
        by_symbol_rows.append(
            {
                "nearest_reifespur_symbol": symbol,
                "rows": total,
                "dominant_uebergangsqualitaet": _dominant(counter),
                "stabil_share": round(counter.get("stabil", 0) / total, 6) if total else 0.0,
                "brueckenfaehig_share": round(counter.get("brueckenfaehig", 0) / total, 6) if total else 0.0,
                "randspannungsnah_share": round(counter.get("randspannungsnah", 0) / total, 6) if total else 0.0,
                "weich_kippend_share": round(counter.get("weich_kippend", 0) / total, 6) if total else 0.0,
                "uebergang_entlastend_share": round(counter.get("uebergang_entlastend", 0) / total, 6) if total else 0.0,
                "uebergang_belastend_share": round(counter.get("uebergang_belastend", 0) / total, 6) if total else 0.0,
                "offen_gemischt_share": round(counter.get("offen_gemischt", 0) / total, 6) if total else 0.0,
            }
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "transition_quality_landkarte_rows_sample.csv",
        all_rows[:20000],
        [
            "world_label",
            "tick",
            "timestamp_ms",
            "nearest_reifespur_symbol",
            "landkarte_state",
            "effect_class",
            "field_quality",
            "uebergangsqualitaet",
            "mcm_carry_quality",
            "mcm_strain_quality",
            "mcm_rekopplung_quality",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    _write_csv(
        out_dir / "transition_quality_by_world.csv",
        by_world_rows,
        [
            "world_label",
            "rows",
            "dominant_uebergangsqualitaet",
            "stabil_share",
            "brueckenfaehig_share",
            "randspannungsnah_share",
            "weich_kippend_share",
            "uebergang_entlastend_share",
            "uebergang_belastend_share",
            "offen_gemischt_share",
        ],
    )
    _write_csv(
        out_dir / "transition_quality_by_symbol.csv",
        by_symbol_rows,
        [
            "nearest_reifespur_symbol",
            "rows",
            "dominant_uebergangsqualitaet",
            "stabil_share",
            "brueckenfaehig_share",
            "randspannungsnah_share",
            "weich_kippend_share",
            "uebergang_entlastend_share",
            "uebergang_belastend_share",
            "offen_gemischt_share",
        ],
    )

    total_counter = Counter(str(row["uebergangsqualitaet"]) for row in all_rows)
    total = sum(total_counter.values())
    summary = {
        "world_count": len(worlds),
        "rows": total,
        "transition_quality_counts": dict(total_counter),
        "transition_quality_shares": {key: round(value / total, 6) for key, value in total_counter.items()} if total else {},
        "dominant_transition_quality": _dominant(total_counter),
        "symbol_count": len(by_symbol_rows),
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
        "interpretation": "passive_transition_quality_landkarte_built",
    }
    (out_dir / "transition_quality_landkarte_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Uebergangsqualitaet fuer Mini-DIO-Landkarte")
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_IN)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(json.dumps(run(args.input_dir, args.out_dir), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
