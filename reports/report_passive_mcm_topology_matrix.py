from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_YEAR_ROLE = ROOT / "debug" / "dio_mini_passive_target_role_map_year_hardtest_20260618" / "target_role_map.csv"
DEFAULT_STABILITY = ROOT / "debug" / "dio_mini_passive_role_stability_transition_map_20260618" / "role_stability_transition_map.csv"
DEFAULT_TRANSITION = ROOT / "debug" / "dio_mini_passive_transition_quality_landkarte_20260618" / "transition_quality_by_symbol.csv"
DEFAULT_VARIANCE = ROOT / "debug" / "dio_mini_passive_topology_year_hardtest_worlds_20260618" / "reifespur_matrix_extension_by_symbol.csv"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_mcm_topology_matrix_20260618"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _index(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    return {row[key]: row for row in rows if row.get(key)}


def _as_float(row: dict[str, str], key: str) -> float:
    return float(row.get(key, 0.0) or 0.0)


def _as_int(row: dict[str, str], key: str) -> int:
    return int(float(row.get(key, 0) or 0))


def _matrix_interpretation(role: str, stability: str, transition_hint: str, soft_kip: float, mixed: float) -> str:
    if stability == "jahresdrift_rolle" or transition_hint != "kein_uebergangsverdacht":
        return "uebergangszone"
    if role == "zentrum_nahe_stabilisierung":
        return "zentrum"
    if role == "selbstnah_driftend":
        return "selbstnahe_drift"
    if role == "offene_bruecke_tragend":
        return "tragende_bruecke"
    if role == "offene_bruecke_entlastend":
        if soft_kip >= 0.05 or mixed >= 0.20:
            return "entlastende_bruecke_mit_offener_varianz"
        return "entlastende_bruecke"
    return "offener_feldbereich"


def run(
    year_role_path: Path,
    stability_path: Path,
    transition_path: Path,
    variance_path: Path,
    out_dir: Path,
) -> dict[str, object]:
    year_roles = _index(_read_csv(year_role_path), "target_symbol")
    stability = _index(_read_csv(stability_path), "target_symbol")
    transitions = _index(_read_csv(transition_path), "nearest_reifespur_symbol")
    variance = _index(_read_csv(variance_path), "reifespur_symbol")
    symbols = sorted(set(year_roles) | set(stability) | set(transitions) | set(variance))

    rows: list[dict[str, object]] = []
    for symbol in symbols:
        role = year_roles.get(symbol, {})
        stable = stability.get(symbol, {})
        trans = transitions.get(symbol, {})
        var = variance.get(symbol, {})
        target_role = role.get("target_role", "-")
        stability_class = stable.get("stability_class", "-")
        transition_hint = stable.get("transition_hint", "-")
        soft_kip = _as_float(trans, "weich_kippend_share")
        mixed = _as_float(trans, "offen_gemischt_share")
        item = {
            "reifespur_symbol": symbol,
            "matrix_interpretation": _matrix_interpretation(target_role, stability_class, transition_hint, soft_kip, mixed),
            "year_role": target_role,
            "base_role": stable.get("base_role", "-"),
            "follow_role": stable.get("follow_role", "-"),
            "stability_class": stability_class,
            "transition_hint": transition_hint,
            "dominant_access_quality": role.get("dominant_transition_quality", "-"),
            "dominant_prev_symbol": role.get("dominant_prev_symbol", "-"),
            "self_share": _as_float(role, "self_share"),
            "world_presence": _as_int(role, "world_presence"),
            "prev_symbol_count": _as_int(role, "prev_symbol_count"),
            "count": _as_int(role, "count"),
            "variance_inside_count": _as_int(var, "innerhalb_bisheriger_varianz"),
            "variance_above_count": _as_int(var, "oberhalb_bisheriger_varianz"),
            "variance_below_count": _as_int(var, "unter_bisheriger_varianz"),
            "dominant_uebergangsqualitaet": trans.get("dominant_uebergangsqualitaet", "-"),
            "brueckenfaehig_share": _as_float(trans, "brueckenfaehig_share"),
            "randspannungsnah_share": _as_float(trans, "randspannungsnah_share"),
            "weich_kippend_share": soft_kip,
            "uebergang_entlastend_share": _as_float(trans, "uebergang_entlastend_share"),
            "uebergang_belastend_share": _as_float(trans, "uebergang_belastend_share"),
            "offen_gemischt_share": mixed,
            "mean_delta_carry": _as_float(role, "mean_delta_carry"),
            "mean_delta_strain": _as_float(role, "mean_delta_strain"),
            "mean_delta_rekopplung": _as_float(role, "mean_delta_rekopplung"),
            "passive_only": 1,
            "influences_action": 0,
            "is_gate": 0,
            "is_entry_signal": 0,
        }
        rows.append(item)

    rows.sort(key=lambda row: str(row["matrix_interpretation"]))
    interpretation_counts = Counter(str(row["matrix_interpretation"]) for row in rows)
    stability_counts = Counter(str(row["stability_class"]) for row in rows)

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "passive_mcm_topology_matrix.csv",
        rows,
        [
            "reifespur_symbol",
            "matrix_interpretation",
            "year_role",
            "base_role",
            "follow_role",
            "stability_class",
            "transition_hint",
            "dominant_access_quality",
            "dominant_prev_symbol",
            "self_share",
            "world_presence",
            "prev_symbol_count",
            "count",
            "variance_inside_count",
            "variance_above_count",
            "variance_below_count",
            "dominant_uebergangsqualitaet",
            "brueckenfaehig_share",
            "randspannungsnah_share",
            "weich_kippend_share",
            "uebergang_entlastend_share",
            "uebergang_belastend_share",
            "offen_gemischt_share",
            "mean_delta_carry",
            "mean_delta_strain",
            "mean_delta_rekopplung",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    summary = {
        "symbol_count": len(rows),
        "matrix_interpretation_counts": dict(interpretation_counts),
        "stability_class_counts": dict(stability_counts),
        "transition_zone_symbols": [
            row["reifespur_symbol"] for row in rows if row["matrix_interpretation"] == "uebergangszone"
        ],
        "interpretation": "passive_mcm_topology_matrix_consolidated",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "passive_mcm_topology_matrix_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive MCM-Topologie-Matrix konsolidieren")
    parser.add_argument("--year-role", type=Path, default=DEFAULT_YEAR_ROLE)
    parser.add_argument("--stability", type=Path, default=DEFAULT_STABILITY)
    parser.add_argument("--transition", type=Path, default=DEFAULT_TRANSITION)
    parser.add_argument("--variance", type=Path, default=DEFAULT_VARIANCE)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(
        json.dumps(
            run(args.year_role, args.stability, args.transition, args.variance, args.out_dir),
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
