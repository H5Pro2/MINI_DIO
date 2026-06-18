from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE = ROOT / "debug" / "dio_mini_passive_target_role_map_20260618" / "target_role_map.csv"
DEFAULT_FOLLOW = ROOT / "debug" / "dio_mini_passive_target_role_map_reproduction_20260618" / "target_role_map.csv"
DEFAULT_YEAR = ROOT / "debug" / "dio_mini_passive_target_role_map_year_hardtest_20260618" / "target_role_map.csv"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_role_stability_transition_map_20260618"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _index(path: Path) -> dict[str, dict[str, str]]:
    return {row["target_symbol"]: row for row in _read_csv(path)}


def _as_float(row: dict[str, str], key: str) -> float:
    return float(row.get(key, 0.0) or 0.0)


def _stability_class(base_role: str, follow_role: str, year_role: str) -> str:
    if base_role == follow_role == year_role and base_role != "-":
        return "stabile_rolle"
    if base_role == follow_role and year_role != base_role:
        return "jahresdrift_rolle"
    if follow_role == year_role and base_role != follow_role:
        return "fruehe_abweichung_stabilisiert"
    return "wechselnde_rolle"


def _transition_hint(row: dict[str, object]) -> str:
    stability = str(row["stability_class"])
    base_role = str(row["base_role"])
    year_role = str(row["year_role"])
    if stability == "stabile_rolle":
        return "kein_uebergangsverdacht"
    if base_role == "spannungsrand_belastend" and "bruecke" in year_role:
        return "spannung_zu_bruecke_uebergang"
    if "bruecke" in base_role and "spannungsrand" in year_role:
        return "bruecke_zu_spannung_uebergang"
    return "rollen_drift_pruefen"


def run(base_path: Path, follow_path: Path, year_path: Path, out_dir: Path) -> dict[str, object]:
    base = _index(base_path)
    follow = _index(follow_path)
    year = _index(year_path)
    symbols = sorted(set(base) | set(follow) | set(year))
    rows: list[dict[str, object]] = []
    for symbol in symbols:
        b = base.get(symbol, {})
        f = follow.get(symbol, {})
        y = year.get(symbol, {})
        base_role = b.get("target_role", "-")
        follow_role = f.get("target_role", "-")
        year_role = y.get("target_role", "-")
        item: dict[str, object] = {
            "target_symbol": symbol,
            "base_role": base_role,
            "follow_role": follow_role,
            "year_role": year_role,
            "stability_class": _stability_class(base_role, follow_role, year_role),
            "base_quality": b.get("dominant_transition_quality", "-"),
            "follow_quality": f.get("dominant_transition_quality", "-"),
            "year_quality": y.get("dominant_transition_quality", "-"),
            "quality_stable_all": int(
                b.get("dominant_transition_quality", "-")
                == f.get("dominant_transition_quality", "-")
                == y.get("dominant_transition_quality", "-")
                and b.get("dominant_transition_quality", "-") != "-"
            ),
            "base_self_share": _as_float(b, "self_share"),
            "follow_self_share": _as_float(f, "self_share"),
            "year_self_share": _as_float(y, "self_share"),
            "delta_follow_self_share": round(_as_float(f, "self_share") - _as_float(b, "self_share"), 6),
            "delta_year_self_share": round(_as_float(y, "self_share") - _as_float(b, "self_share"), 6),
            "base_belastend_share": _as_float(b, "belastend_share"),
            "follow_belastend_share": _as_float(f, "belastend_share"),
            "year_belastend_share": _as_float(y, "belastend_share"),
            "delta_year_belastend_share": round(_as_float(y, "belastend_share") - _as_float(b, "belastend_share"), 6),
            "base_entlastend_share": _as_float(b, "entlastend_share"),
            "follow_entlastend_share": _as_float(f, "entlastend_share"),
            "year_entlastend_share": _as_float(y, "entlastend_share"),
            "delta_year_entlastend_share": round(_as_float(y, "entlastend_share") - _as_float(b, "entlastend_share"), 6),
        }
        item["transition_hint"] = _transition_hint(item)
        rows.append(item)

    rows.sort(key=lambda row: (str(row["stability_class"]), str(row["target_symbol"])))
    counts: dict[str, int] = {}
    hints: dict[str, int] = {}
    for row in rows:
        counts[str(row["stability_class"])] = counts.get(str(row["stability_class"]), 0) + 1
        hints[str(row["transition_hint"])] = hints.get(str(row["transition_hint"]), 0) + 1

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "role_stability_transition_map.csv",
        rows,
        [
            "target_symbol",
            "base_role",
            "follow_role",
            "year_role",
            "stability_class",
            "transition_hint",
            "base_quality",
            "follow_quality",
            "year_quality",
            "quality_stable_all",
            "base_self_share",
            "follow_self_share",
            "year_self_share",
            "delta_follow_self_share",
            "delta_year_self_share",
            "base_belastend_share",
            "follow_belastend_share",
            "year_belastend_share",
            "delta_year_belastend_share",
            "base_entlastend_share",
            "follow_entlastend_share",
            "year_entlastend_share",
            "delta_year_entlastend_share",
        ],
    )
    summary = {
        "symbol_count": len(rows),
        "stability_class_counts": counts,
        "transition_hint_counts": hints,
        "stable_role_count": counts.get("stabile_rolle", 0),
        "transition_zone_count": sum(count for hint, count in hints.items() if hint != "kein_uebergangsverdacht"),
        "interpretation": "role_stability_transition_map_built",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "role_stability_transition_map_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Rollenstabilitaets- und Uebergangszonenkarte")
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--follow", type=Path, default=DEFAULT_FOLLOW)
    parser.add_argument("--year", type=Path, default=DEFAULT_YEAR)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(json.dumps(run(args.base, args.follow, args.year, args.out_dir), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
