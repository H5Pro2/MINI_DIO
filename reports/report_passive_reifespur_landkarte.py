from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.report_passive_reifespur_reproduction import _signature, _state_rows


DEFAULT_MEMORY = ROOT / "bot_memory" / "dio_mini_passive_reifespur_memory.json"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_reifespur_landkarte_20260618"


def _load_memory(path: Path) -> list[dict]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    boundary = dict(payload.get("boundary", {}) or {})
    if not bool(boundary.get("passive_only", False)):
        return []
    if bool(boundary.get("influences_action", True)):
        return []
    if bool(boundary.get("is_gate", True)) or bool(boundary.get("is_entry_signal", True)):
        return []
    return [dict(item) for item in payload.get("entries", []) or [] if isinstance(item, dict)]


def _parts(signature: str) -> list[str]:
    return [part.strip() for part in str(signature or "").split("|") if part.strip()]


def _similarity(a: str, b: str) -> tuple[float, int, int]:
    a_parts = _parts(a)
    b_parts = _parts(b)
    total = max(len(a_parts), len(b_parts), 1)
    same = sum(1 for left, right in zip(a_parts, b_parts) if left == right)
    return round(same / total, 6), same, total


def _landkarte_state(best: dict | None, similarity: float, exact: bool) -> str:
    if best is None:
        return "keine_reifespur_nahe"
    kind = str(best.get("candidate_kind", "") or "")
    if exact and kind == "reifekandidat":
        return "reifespur_exakt_erkannt"
    if exact and kind == "spannungskandidat":
        return "spannungsspur_exakt_erkannt"
    if exact:
        return "tragspur_exakt_erkannt"
    if similarity >= 0.875 and kind == "reifekandidat":
        return "reifespur_nahe"
    if similarity >= 0.875 and kind == "spannungskandidat":
        return "spannungsspur_nahe"
    if similarity >= 0.875:
        return "tragspur_nahe"
    if similarity >= 0.625:
        return "offene_spurnahe"
    return "keine_reifespur_nahe"


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def run(data_path: Path, memory_path: Path, out_dir: Path, world_label: str) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    memory_entries = _load_memory(memory_path)
    states = _state_rows(data_path)
    rows: list[dict[str, object]] = []
    state_counts: Counter[str] = Counter()
    exact_counts: Counter[str] = Counter()
    best_symbol_counts: Counter[str] = Counter()

    for current, nxt in zip(states, states[1:]):
        signature = _signature(dict(current["senses"]), dict(current["effect"]), dict(nxt["effect"]))
        best = None
        best_similarity = -1.0
        best_same = 0
        best_total = 0
        for entry in memory_entries:
            sim, same, total = _similarity(signature, str(entry.get("multisense_signature", "") or ""))
            if sim > best_similarity:
                best = entry
                best_similarity = sim
                best_same = same
                best_total = total
        exact = bool(best and best_similarity >= 1.0)
        landkarte_state = _landkarte_state(best, best_similarity, exact)
        state_counts[landkarte_state] += 1
        if exact and best:
            exact_counts[str(best.get("candidate_kind", "") or "-")] += 1
        if best:
            best_symbol_counts[str(best.get("reifespur_symbol", "") or "-")] += 1
        effect = dict(current["effect"])
        rows.append(
            {
                "world_label": world_label,
                "data_path": str(data_path),
                "tick": current["tick"],
                "timestamp_ms": current["timestamp_ms"],
                "current_multisense_signature": signature,
                "landkarte_state": landkarte_state,
                "nearest_reifespur_symbol": str(best.get("reifespur_symbol", "") if best else ""),
                "nearest_candidate_kind": str(best.get("candidate_kind", "") if best else ""),
                "nearest_reference_status": str(best.get("reference_follow_status", "") if best else ""),
                "nearest_memory_state": str(best.get("passive_reifespur_memory_state", "") if best else ""),
                "nearest_similarity": best_similarity if best else 0.0,
                "nearest_equal_parts": best_same,
                "nearest_total_parts": best_total,
                "exact_reifespur_match": 1 if exact else 0,
                "effect_class": current["effect_class"],
                "mcm_carry_quality": round(float(effect.get("mcm_carry_quality", 0.0) or 0.0), 6),
                "mcm_strain_quality": round(float(effect.get("mcm_strain_quality", 0.0) or 0.0), 6),
                "mcm_rekopplung_quality": round(float(effect.get("mcm_rekopplung_quality", 0.0) or 0.0), 6),
                "passive_only": 1,
                "influences_action": 0,
                "is_gate": 0,
                "is_entry_signal": 0,
            }
        )

    _write_csv(
        out_dir / "reifespur_landkarte_rows.csv",
        rows,
        [
            "world_label",
            "data_path",
            "tick",
            "timestamp_ms",
            "current_multisense_signature",
            "landkarte_state",
            "nearest_reifespur_symbol",
            "nearest_candidate_kind",
            "nearest_reference_status",
            "nearest_memory_state",
            "nearest_similarity",
            "nearest_equal_parts",
            "nearest_total_parts",
            "exact_reifespur_match",
            "effect_class",
            "mcm_carry_quality",
            "mcm_strain_quality",
            "mcm_rekopplung_quality",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )

    summary_rows = []
    for symbol, count in best_symbol_counts.most_common():
        entry = next((item for item in memory_entries if item.get("reifespur_symbol") == symbol), {})
        summary_rows.append(
            {
                "reifespur_symbol": symbol,
                "candidate_kind": str(entry.get("candidate_kind", "") or ""),
                "memory_state": str(entry.get("passive_reifespur_memory_state", "") or ""),
                "reference_status": str(entry.get("reference_follow_status", "") or ""),
                "nearest_count": count,
            }
        )
    _write_csv(
        out_dir / "reifespur_landkarte_by_memory_symbol.csv",
        summary_rows,
        ["reifespur_symbol", "candidate_kind", "memory_state", "reference_status", "nearest_count"],
    )

    summary = {
        "world_label": world_label,
        "data_path": str(data_path),
        "memory_path": str(memory_path),
        "ticks": len(states),
        "rows": len(rows),
        "memory_entries": len(memory_entries),
        "landkarte_state_counts": dict(state_counts),
        "exact_candidate_kind_counts": dict(exact_counts),
        "nearest_symbol_counts": dict(best_symbol_counts.most_common()),
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "reifespur_landkarte_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Mini-DIO reifespur landkarte")
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--memory", type=Path, default=DEFAULT_MEMORY)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--world-label", default="")
    args = parser.parse_args()
    world_label = args.world_label or args.data.stem
    summary = run(args.data, args.memory, args.out_dir, world_label)
    print(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
