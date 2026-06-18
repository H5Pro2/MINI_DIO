from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MATRIX = ROOT / "debug" / "dio_mini_passive_mcm_topology_matrix_20260618" / "passive_mcm_topology_matrix.csv"
DEFAULT_WORLD_DIR = ROOT / "debug" / "dio_mini_passive_topology_year_hardtest_worlds_20260618"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_drift_transition_feature_proximity_20260618"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _as_float(value: str | object) -> float:
    return float(value or 0.0)


def _mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def _iter_world_rows(input_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for world_dir in sorted(input_dir.glob("world_*")):
        path = world_dir / "reifespur_landkarte_rows.csv"
        if path.exists():
            rows.extend(_read_csv(path))
    return rows


def _features(signature: str) -> list[str]:
    return [part.strip() for part in str(signature or "").split("|") if part.strip()]


def _family(feature: str) -> str:
    if feature.startswith("sehen_"):
        return "sehen"
    if feature.startswith("hoeren_"):
        return "hoeren"
    if feature.startswith("feld_"):
        return "feld"
    if feature.startswith("folge_"):
        return "folge"
    return "sonstige"


def _dominant(counter: Counter[str]) -> str:
    return counter.most_common(1)[0][0] if counter else "-"


def _role_feature_rows(
    role_counts: Counter[str],
    role_feature_counts: dict[str, Counter[str]],
    baseline_features: Counter[str],
    baseline_total: int,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for role, role_total in sorted(role_counts.items()):
        for feature, count in role_feature_counts[role].most_common():
            role_share = count / role_total if role_total else 0.0
            baseline_share = baseline_features[feature] / baseline_total if baseline_total else 0.0
            rows.append(
                {
                    "matrix_interpretation": role,
                    "feature": feature,
                    "feature_family": _family(feature),
                    "count": count,
                    "role_rows": role_total,
                    "role_share": round(role_share, 6),
                    "baseline_share": round(baseline_share, 6),
                    "enrichment": round(role_share - baseline_share, 6),
                    "passive_only": 1,
                    "influences_action": 0,
                    "is_gate": 0,
                    "is_entry_signal": 0,
                }
            )
    rows.sort(key=lambda row: (str(row["matrix_interpretation"]), -abs(_as_float(row["enrichment"])), str(row["feature"])))
    return rows


def run(matrix_path: Path, input_dir: Path, out_dir: Path) -> dict[str, object]:
    matrix = {row["reifespur_symbol"]: row for row in _read_csv(matrix_path)}
    rows = _iter_world_rows(input_dir)

    baseline_features: Counter[str] = Counter()
    role_counts: Counter[str] = Counter()
    role_feature_counts: dict[str, Counter[str]] = defaultdict(Counter)
    role_world_counts: dict[str, Counter[str]] = defaultdict(Counter)
    role_effect_counts: dict[str, Counter[str]] = defaultdict(Counter)
    role_values: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))

    for row in rows:
        symbol = row.get("nearest_reifespur_symbol", "-")
        role = matrix.get(symbol, {}).get("matrix_interpretation", "unmapped")
        role_counts[role] += 1
        role_world_counts[role][row.get("world_label", "-")] += 1
        role_effect_counts[role][row.get("effect_class", "-")] += 1
        role_values[role]["carry"].append(_as_float(row.get("mcm_carry_quality", 0.0)))
        role_values[role]["strain"].append(_as_float(row.get("mcm_strain_quality", 0.0)))
        role_values[role]["rekopplung"].append(_as_float(row.get("mcm_rekopplung_quality", 0.0)))
        for feature in _features(row.get("current_multisense_signature", "")):
            baseline_features[feature] += 1
            role_feature_counts[role][feature] += 1

    baseline_total = sum(role_counts.values())
    feature_rows = _role_feature_rows(role_counts, role_feature_counts, baseline_features, baseline_total)

    role_profile_rows: list[dict[str, object]] = []
    for role, count in sorted(role_counts.items()):
        world_counter = role_world_counts[role]
        effect_counter = role_effect_counts[role]
        role_profile_rows.append(
            {
                "matrix_interpretation": role,
                "rows": count,
                "share": round(count / baseline_total, 6) if baseline_total else 0.0,
                "dominant_world": _dominant(world_counter),
                "dominant_effect_class": _dominant(effect_counter),
                "mean_carry": _mean(role_values[role]["carry"]),
                "mean_strain": _mean(role_values[role]["strain"]),
                "mean_rekopplung": _mean(role_values[role]["rekopplung"]),
                "top_feature_1": role_feature_counts[role].most_common(1)[0][0] if role_feature_counts[role] else "-",
                "top_feature_2": role_feature_counts[role].most_common(2)[1][0]
                if len(role_feature_counts[role]) > 1
                else "-",
                "top_feature_3": role_feature_counts[role].most_common(3)[2][0]
                if len(role_feature_counts[role]) > 2
                else "-",
                "passive_only": 1,
                "influences_action": 0,
                "is_gate": 0,
                "is_entry_signal": 0,
            }
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "matrix_role_feature_enrichment.csv",
        feature_rows,
        [
            "matrix_interpretation",
            "feature",
            "feature_family",
            "count",
            "role_rows",
            "role_share",
            "baseline_share",
            "enrichment",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    _write_csv(
        out_dir / "matrix_role_profile.csv",
        role_profile_rows,
        [
            "matrix_interpretation",
            "rows",
            "share",
            "dominant_world",
            "dominant_effect_class",
            "mean_carry",
            "mean_strain",
            "mean_rekopplung",
            "top_feature_1",
            "top_feature_2",
            "top_feature_3",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )

    focused = [row for row in feature_rows if row["matrix_interpretation"] in {"selbstnahe_drift", "uebergangszone"}]
    summary = {
        "row_count": baseline_total,
        "role_counts": dict(role_counts),
        "role_profile_count": len(role_profile_rows),
        "focused_roles": ["selbstnahe_drift", "uebergangszone"],
        "top_focused_enrichments": focused[:12],
        "interpretation": "passive_drift_transition_feature_proximity",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "drift_transition_feature_proximity_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Merkmalsnaehe fuer Drift und Uebergang pruefen")
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_WORLD_DIR)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(json.dumps(run(args.matrix, args.input_dir, args.out_dir), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
