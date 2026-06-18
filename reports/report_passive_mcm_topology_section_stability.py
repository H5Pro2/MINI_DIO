from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MATRIX = ROOT / "debug" / "dio_mini_passive_mcm_topology_matrix_20260618" / "passive_mcm_topology_matrix.csv"
DEFAULT_WORLD_DIR = ROOT / "debug" / "dio_mini_passive_topology_year_hardtest_worlds_20260618"
DEFAULT_OUT = ROOT / "debug" / "dio_mini_passive_mcm_topology_section_stability_20260618"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _as_int(value: str) -> int:
    return int(float(value or 0))


def _as_float(value: object) -> float:
    return float(value or 0.0)


def _section_for_tick(tick: int, max_tick: int) -> str:
    if max_tick <= 0:
        return "early"
    ratio = tick / max_tick
    if ratio < 1.0 / 3.0:
        return "early"
    if ratio < 2.0 / 3.0:
        return "middle"
    return "late"


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return counter.most_common(1)[0][0]


def _iter_world_rows(input_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for world_dir in sorted(input_dir.glob("world_*")):
        path = world_dir / "reifespur_landkarte_rows.csv"
        if not path.exists():
            continue
        rows.extend(_read_csv(path))
    return rows


def _row_quality(row: dict[str, str]) -> str:
    return str(row.get("uebergangsqualitaet") or row.get("effect_class") or "-")


def run(matrix_path: Path, input_dir: Path, out_dir: Path, rows_path: Path | None = None) -> dict[str, object]:
    matrix_rows = _read_csv(matrix_path)
    matrix_by_symbol = {row["reifespur_symbol"]: row for row in matrix_rows}
    rows = _read_csv(rows_path) if rows_path else _iter_world_rows(input_dir)

    max_tick_by_world: dict[str, int] = defaultdict(int)
    for row in rows:
        world = row.get("world_label", "-")
        max_tick_by_world[world] = max(max_tick_by_world[world], _as_int(row.get("tick", "0")))

    bucket_counts: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    bucket_quality: dict[tuple[str, str, str], Counter[str]] = defaultdict(Counter)
    bucket_total: Counter[tuple[str, str]] = Counter()

    for row in rows:
        world = row.get("world_label", "-")
        section = _section_for_tick(_as_int(row.get("tick", "0")), max_tick_by_world[world])
        symbol = row.get("nearest_reifespur_symbol", "-")
        quality = _row_quality(row)
        bucket = (world, section)
        bucket_counts[bucket][symbol] += 1
        bucket_quality[(world, section, symbol)][quality] += 1
        bucket_total[bucket] += 1

    section_rows: list[dict[str, object]] = []
    for (world, section), counts in sorted(bucket_counts.items()):
        total = bucket_total[(world, section)]
        for symbol, count in counts.most_common():
            matrix = matrix_by_symbol.get(symbol, {})
            section_rows.append(
                {
                    "world_label": world,
                    "section": section,
                    "reifespur_symbol": symbol,
                    "section_count": count,
                    "section_share": round(count / total, 6) if total else 0.0,
                    "matrix_interpretation": matrix.get("matrix_interpretation", "-"),
                    "year_role": matrix.get("year_role", "-"),
                    "dominant_section_quality": _dominant(bucket_quality[(world, section, symbol)]),
                    "passive_only": 1,
                    "influences_action": 0,
                    "is_gate": 0,
                    "is_entry_signal": 0,
                }
            )

    interpretation_presence: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    for row in section_rows:
        interpretation_presence[(str(row["world_label"]), str(row["section"]))][str(row["matrix_interpretation"])] += _as_float(
            row["section_share"]
        )

    section_summary_rows: list[dict[str, object]] = []
    for (world, section), interpretations in sorted(interpretation_presence.items()):
        section_summary_rows.append(
            {
                "world_label": world,
                "section": section,
                "dominant_matrix_interpretation": _dominant(interpretations),
                "zentrum_share": round(interpretations.get("zentrum", 0.0), 6),
                "tragende_bruecke_share": round(interpretations.get("tragende_bruecke", 0.0), 6),
                "entlastende_bruecke_share": round(interpretations.get("entlastende_bruecke", 0.0), 6),
                "entlastende_bruecke_mit_offener_varianz_share": round(
                    interpretations.get("entlastende_bruecke_mit_offener_varianz", 0.0), 6
                ),
                "selbstnahe_drift_share": round(interpretations.get("selbstnahe_drift", 0.0), 6),
                "uebergangszone_share": round(interpretations.get("uebergangszone", 0.0), 6),
                "passive_only": 1,
                "influences_action": 0,
                "is_gate": 0,
                "is_entry_signal": 0,
            }
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(
        out_dir / "topology_section_by_symbol.csv",
        section_rows,
        [
            "world_label",
            "section",
            "reifespur_symbol",
            "section_count",
            "section_share",
            "matrix_interpretation",
            "year_role",
            "dominant_section_quality",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )
    _write_csv(
        out_dir / "topology_section_summary.csv",
        section_summary_rows,
        [
            "world_label",
            "section",
            "dominant_matrix_interpretation",
            "zentrum_share",
            "tragende_bruecke_share",
            "entlastende_bruecke_share",
            "entlastende_bruecke_mit_offener_varianz_share",
            "selbstnahe_drift_share",
            "uebergangszone_share",
            "passive_only",
            "influences_action",
            "is_gate",
            "is_entry_signal",
        ],
    )

    dominant_by_section = Counter(row["dominant_matrix_interpretation"] for row in section_summary_rows)
    max_transition = max((_as_float(row["uebergangszone_share"]) for row in section_summary_rows), default=0.0)
    max_center = max((_as_float(row["zentrum_share"]) for row in section_summary_rows), default=0.0)
    summary = {
        "row_count": len(rows),
        "world_section_count": len(section_summary_rows),
        "dominant_matrix_interpretation_counts": dict(dominant_by_section),
        "max_uebergangszone_share": round(max_transition, 6),
        "max_zentrum_share": round(max_center, 6),
        "interpretation": "passive_topology_section_stability",
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_entry_signal": False,
    }
    (out_dir / "topology_section_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive MCM-Topologie abschnittsweise pruefen")
    parser.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_WORLD_DIR)
    parser.add_argument("--rows", type=Path, default=None)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    print(json.dumps(run(args.matrix, args.input_dir, args.out_dir, args.rows), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
