from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MATRIX = ROOT / "debug" / "dio_mini_passive_mcm_topology_matrix_20260618" / "passive_mcm_topology_matrix.csv"
DEFAULT_WORLD_DIR = ROOT / "debug" / "dio_mini_passive_topology_year_hardtest_worlds_20260618"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_center_phase_dynamics_20260618"
TARGET_ROLE = "zentrum"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _as_float(value: object) -> float:
    return float(value or 0.0)


def _mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 6) if values else 0.0


def _dominant(counter: Counter[str]) -> str:
    return counter.most_common(1)[0][0] if counter else "-"


def _iter_worlds(input_dir: Path) -> list[tuple[str, list[dict[str, str]]]]:
    worlds: list[tuple[str, list[dict[str, str]]]] = []
    for world_dir in sorted(input_dir.glob("world_*")):
        path = world_dir / "reifespur_landkarte_rows.csv"
        if path.exists():
            rows = sorted(_read_csv(path), key=lambda row: int(float(row.get("tick", 0) or 0)))
            worlds.append((world_dir.name.removeprefix("world_"), rows))
    return worlds


def _features(signature: str) -> list[str]:
    return [part.strip() for part in str(signature or "").split("|") if part.strip()]


def _role_for(row: dict[str, str], matrix: dict[str, str]) -> str:
    return matrix.get(row.get("nearest_reifespur_symbol", "-"), "unmapped")


def _segment_class(length: int) -> str:
    if length == 1:
        return "kurzer_zentrumskontakt"
    if length <= 3:
        return "zentrum_haelt_kurz"
    if length <= 8:
        return "zentrumslauf"
    return "langes_zentrum"


def run(matrix_path: Path, input_dir: Path, out_dir: Path, radius: int = 3) -> dict[str, object]:
    matrix = {
        row["reifespur_symbol"]: row["matrix_interpretation"]
        for row in _read_csv(matrix_path)
        if row.get("reifespur_symbol")
    }
    worlds = _iter_worlds(input_dir)

    event_counter = 0
    offset_role_counts: dict[int, Counter[str]] = defaultdict(Counter)
    offset_values: dict[int, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    transition_counts: Counter[tuple[str, str]] = Counter()
    feature_counts: Counter[str] = Counter()
    segment_rows: list[dict[str, object]] = []

    for world_label, rows in worlds:
        roles = [_role_for(row, matrix) for row in rows]
        for idx, role in enumerate(roles):
            if role != TARGET_ROLE:
                continue
            event_counter += 1
            before = roles[idx - 1] if idx > 0 else "world_start"
            after = roles[idx + 1] if idx + 1 < len(roles) else "world_end"
            transition_counts[(before, after)] += 1
            for feature in _features(rows[idx].get("current_multisense_signature", "")):
                feature_counts[feature] += 1
            for offset in range(-radius, radius + 1):
                pos = idx + offset
                if pos < 0 or pos >= len(rows):
                    continue
                offset_role_counts[offset][roles[pos]] += 1
                offset_values[offset]["carry"].append(_as_float(rows[pos].get("mcm_carry_quality", 0.0)))
                offset_values[offset]["strain"].append(_as_float(rows[pos].get("mcm_strain_quality", 0.0)))
                offset_values[offset]["rekopplung"].append(_as_float(rows[pos].get("mcm_rekopplung_quality", 0.0)))

        start = 0
        while start < len(roles):
            role = roles[start]
            end = start
            while end + 1 < len(roles) and roles[end + 1] == role:
                end += 1
            if role == TARGET_ROLE:
                before = roles[start - 1] if start > 0 else "world_start"
                after = roles[end + 1] if end + 1 < len(roles) else "world_end"
                segment_slice = rows[start : end + 1]
                length = end - start + 1
                segment_rows.append(
                    {
                        "world_label": world_label,
                        "start_tick": rows[start].get("tick", 0),
                        "end_tick": rows[end].get("tick", 0),
                        "length": length,
                        "segment_class": _segment_class(length),
                        "before_role": before,
                        "after_role": after,
                        "mean_carry": _mean([_as_float(row.get("mcm_carry_quality", 0.0)) for row in segment_slice]),
                        "mean_strain": _mean([_as_float(row.get("mcm_strain_quality", 0.0)) for row in segment_slice]),
                        "mean_rekopplung": _mean(
                            [_as_float(row.get("mcm_rekopplung_quality", 0.0)) for row in segment_slice]
                        ),
                        "passive_only": 1,
                        "influences_action": 0,
                        "is_gate": 0,
                        "is_entry_signal": 0,
                    }
                )
            start = end + 1

    offset_rows: list[dict[str, object]] = []
    for offset, role_counter in sorted(offset_role_counts.items()):
        total = sum(role_counter.values())
        offset_rows.append(
            {
                "target_role": TARGET_ROLE,
                "offset": offset,
                "rows": total,
                "dominant_role": _dominant(role_counter),
                "zentrum_share": round(role_counter.get("zentrum", 0) / total, 6) if total else 0.0,
                "selbstnahe_drift_share": round(role_counter.get("selbstnahe_drift", 0) / total, 6) if total else 0.0,
                "uebergangszone_share": round(role_counter.get("uebergangszone", 0) / total, 6) if total else 0.0,
                "tragende_bruecke_share": round(role_counter.get("tragende_bruecke", 0) / total, 6) if total else 0.0,
                "entlastende_bruecke_share": round(role_counter.get("entlastende_bruecke", 0) / total, 6) if total else 0.0,
                "offene_varianz_share": round(
                    role_counter.get("entlastende_bruecke_mit_offener_varianz", 0) / total, 6
                )
                if total
                else 0.0,
                "mean_carry": _mean(offset_values[offset]["carry"]),
                "mean_strain": _mean(offset_values[offset]["strain"]),
                "mean_rekopplung": _mean(offset_values[offset]["rekopplung"]),
                "passive_only": 1,
                "influences_action": 0,
                "is_gate": 0,
                "is_entry_signal": 0,
            }
        )

    transition_rows = [
        {
            "before_role": before,
            "after_role": after,
            "count": count,
            "share_in_center": round(count / event_counter, 6) if event_counter else 0.0,
            "passive_only": 1,
            "influences_action": 0,
            "is_gate": 0,
            "is_entry_signal": 0,
        }
        for (before, after), count in transition_counts.most_common()
    ]

    class_counts = Counter(str(row["segment_class"]) for row in segment_rows)
    before_counts = Counter(str(row["before_role"]) for row in segment_rows)
    after_counts = Counter(str(row["after_role"]) for row in segment_rows)
    lengths = [_as_float(row["length"]) for row in segment_rows]
    segment_summary_rows = [
        {
            "segment_count": len(segment_rows),
            "mean_length": _mean(lengths),
            "max_length": int(max(lengths)) if lengths else 0,
            "dominant_before_role": _dominant(before_counts),
            "dominant_after_role": _dominant(after_counts),
            "kurzer_zentrumskontakt_count": class_counts.get("kurzer_zentrumskontakt", 0),
            "zentrum_haelt_kurz_count": class_counts.get("zentrum_haelt_kurz", 0),
            "zentrumslauf_count": class_counts.get("zentrumslauf", 0),
            "langes_zentrum_count": class_counts.get("langes_zentrum", 0),
            "mean_carry": _mean([_as_float(row["mean_carry"]) for row in segment_rows]),
            "mean_strain": _mean([_as_float(row["mean_strain"]) for row in segment_rows]),
            "mean_rekopplung": _mean([_as_float(row["mean_rekopplung"]) for row in segment_rows]),
            "passive_only": 1,
            "influences_action": 0,
            "is_gate": 0,
            "is_entry_signal": 0,
        }
    ]

    feature_rows = [
        {
            "feature": feature,
            "count": count,
            "share_in_center": round(count / event_counter, 6) if event_counter else 0.0,
            "passive_only": 1,
            "influences_action": 0,
            "is_gate": 0,
            "is_entry_signal": 0,
        }
        for feature, count in feature_counts.most_common()
    ]

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "center_phase_offset_profile.csv",
        offset_rows,
        [
            "target_role",
            "offset",
            "rows",
            "dominant_role",
            "zentrum_share",
            "selbstnahe_drift_share",
            "uebergangszone_share",
            "tragende_bruecke_share",
            "entlastende_bruecke_share",
            "offene_varianz_share",
            "mean_carry",
            "mean_strain",
            "mean_rekopplung",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    _write_csv(
        out_dir / "center_phase_transition_pairs.csv",
        transition_rows,
        [
            "before_role",
            "after_role",
            "count",
            "share_in_center",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    _write_csv(
        out_dir / "center_phase_segments.csv",
        segment_rows,
        [
            "world_label",
            "start_tick",
            "end_tick",
            "length",
            "segment_class",
            "before_role",
            "after_role",
            "mean_carry",
            "mean_strain",
            "mean_rekopplung",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    _write_csv(
        out_dir / "center_phase_segment_summary.csv",
        segment_summary_rows,
        [
            "segment_count",
            "mean_length",
            "max_length",
            "dominant_before_role",
            "dominant_after_role",
            "kurzer_zentrumskontakt_count",
            "zentrum_haelt_kurz_count",
            "zentrumslauf_count",
            "langes_zentrum_count",
            "mean_carry",
            "mean_strain",
            "mean_rekopplung",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    _write_csv(
        out_dir / "center_phase_features.csv",
        feature_rows,
        ["feature", "count", "share_in_center", "passive_only", "influences_action", "is_gate", "is_entry_signal"],
    )

    summary = {
        "world_count": len(worlds),
        "center_event_count": event_counter,
        "segment_summary": segment_summary_rows[0] if segment_summary_rows else {},
        "top_transition_pairs": transition_rows[:12],
        "top_center_features": feature_rows[:12],
        "radius": radius,
        "interpretation": "passive_center_phase_dynamics",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "center_phase_dynamics_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Zentrum-Phasendynamik pruefen")
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_WORLD_DIR)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--radius", type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(run(args.matrix, args.input_dir, args.out_dir, args.radius), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
