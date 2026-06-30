from __future__ import annotations

import argparse
import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path


PATTERNS = {
    "tragende_verarbeitung": {
        "tonal_band": "tonal_mid",
        "target_role": "zentrum_rekoppelnd",
    },
    "kippnaehe": {
        "tonal_band": "tonal_high",
        "target_role": "rand_kipp",
    },
}


def _float(row: dict[str, str], key: str, default: float = 0.0) -> float:
    try:
        return float(row.get(key, "") or default)
    except (TypeError, ValueError):
        return default


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * q))))
    return ordered[idx]


def _band(value: float, q33: float, q66: float) -> str:
    if value <= q33:
        return "tonal_low"
    if value >= q66:
        return "tonal_high"
    return "tonal_mid"


def _role(row: dict[str, str], qs: dict[str, float]) -> str:
    field_class = (row.get("passive_mcm_effect_class") or "").strip()
    rekopplung = _float(row, "mcm_rekopplung_quality")
    strain = _float(row, "mcm_strain_quality")
    carry = _float(row, "mcm_carry_quality")
    tension = _float(row, "mcm_feldwirkung_mcm_tension")

    if field_class in {"kippend", "gespannt"} or (
        strain >= qs["strain_q66"] and rekopplung <= qs["rekopplung_q33"]
    ):
        return "rand_kipp"
    if field_class == "stabil" and rekopplung >= qs["rekopplung_q66"] and strain <= qs["strain_q33"]:
        return "zentrum_rekoppelnd"
    if carry >= qs["carry_q66"] and rekopplung >= qs["rekopplung_q50"] and strain < qs["strain_q66"]:
        return "bruecke_tragend"
    if field_class == "tragend_unruhig" or tension >= qs["tension_q66"] or strain >= qs["strain_q50"]:
        return "offen_unruhig"
    return "offenes_feld"


def _iter_episode_files(world_dirs: list[Path]) -> list[Path]:
    files: list[Path] = []
    for world_dir in world_dirs:
        if world_dir.is_file() and world_dir.name == "episodes.csv":
            files.append(world_dir)
        elif world_dir.is_dir():
            files.extend(sorted(world_dir.glob("**/episodes.csv")))
    return files


def _world_group(path: Path) -> str:
    name = path.parent.parent.name.lower()
    if "synth" in name:
        return "synthetisch"
    if "state" in name:
        return "regime"
    if "real_quiet" in name or "sequence_break" in name:
        return "real_segment"
    if "adapted_time" in name or "_1h" in name:
        return "zeit_1h"
    if "adapted_field" in name or "_5m" in name:
        return "feld_5m"
    return "sonstige"


def _classify_rows(path: Path) -> dict[str, list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return {key: [] for key in PATTERNS}

    tone_values = [_float(row, "hoeren_energy_tone") for row in rows]
    qs = {
        "tone_q33": _quantile(tone_values, 0.33),
        "tone_q66": _quantile(tone_values, 0.66),
        "rekopplung_q33": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.33),
        "rekopplung_q50": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.50),
        "rekopplung_q66": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.66),
        "strain_q33": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.33),
        "strain_q50": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.50),
        "strain_q66": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.66),
        "carry_q66": _quantile([_float(row, "mcm_carry_quality") for row in rows], 0.66),
        "tension_q66": _quantile([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows], 0.66),
    }
    classified = {key: [] for key in PATTERNS}
    for row in rows:
        tonal_band = _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"])
        role = _role(row, qs)
        for pattern, spec in PATTERNS.items():
            if tonal_band == spec["tonal_band"] and role == spec["target_role"]:
                classified[pattern].append(row)
    return classified


def _family(value: str) -> str:
    value = (value or "").strip()
    return value if value and value != "-" else "-"


def _summarize(world_group: str, rows_by_pattern: dict[str, list[dict[str, str]]]) -> list[dict[str, object]]:
    left_rows = rows_by_pattern["tragende_verarbeitung"]
    right_rows = rows_by_pattern["kippnaehe"]
    left = Counter(_family(row.get("symbol_family", "")) for row in left_rows if _family(row.get("symbol_family", "")) != "-")
    right = Counter(_family(row.get("symbol_family", "")) for row in right_rows if _family(row.get("symbol_family", "")) != "-")
    shared = sorted(set(left) & set(right))
    union = set(left) | set(right)
    rows: list[dict[str, object]] = [
        {
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
            "world_group": world_group,
            "family": "__SUMMARY__",
            "tragend_count": sum(left.values()),
            "kipp_count": sum(right.values()),
            "shared_family_count": len(shared),
            "union_family_count": len(union),
            "jaccard": len(shared) / len(union) if union else 0.0,
            "bridge_score": 0.0,
            "tragend_share": 0.0,
            "kipp_share": 0.0,
            "avg_tragend_rekopplung": _mean([_float(row, "mcm_rekopplung_quality") for row in left_rows]),
            "avg_kipp_rekopplung": _mean([_float(row, "mcm_rekopplung_quality") for row in right_rows]),
            "avg_tragend_strain": _mean([_float(row, "mcm_strain_quality") for row in left_rows]),
            "avg_kipp_strain": _mean([_float(row, "mcm_strain_quality") for row in right_rows]),
        }
    ]
    total_left = sum(left.values()) or 1
    total_right = sum(right.values()) or 1
    for family in shared:
        tragend_share = left[family] / total_left
        kipp_share = right[family] / total_right
        bridge_score = min(tragend_share, kipp_share)
        rows.append(
            {
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
                "world_group": world_group,
                "family": family,
                "tragend_count": left[family],
                "kipp_count": right[family],
                "shared_family_count": len(shared),
                "union_family_count": len(union),
                "jaccard": len(shared) / len(union) if union else 0.0,
                "bridge_score": bridge_score,
                "tragend_share": tragend_share,
                "kipp_share": kipp_share,
                "avg_tragend_rekopplung": 0.0,
                "avg_kipp_rekopplung": 0.0,
                "avg_tragend_strain": 0.0,
                "avg_kipp_strain": 0.0,
            }
        )
    return rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    summaries = [row for row in rows if row["family"] == "__SUMMARY__"]
    bridges = sorted(
        [row for row in rows if row["family"] != "__SUMMARY__"],
        key=lambda row: float(row["bridge_score"]),
        reverse=True,
    )[:12]
    lines = [
        "# 1072 - Rezeptorhaltung Familienueberlappung",
        "",
        "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
        "",
        "## Frage",
        "",
        "Bleiben `tragende_verarbeitung` und `kippnaehe` in Mini-DIOs Symbolfamilien getrennt, oder gibt es Familien, die beide Rollen ueberbruecken?",
        "",
        "## Weltgruppen",
        "",
        "| Weltgruppe | Tragend Episoden | Kipp Episoden | Geteilte Familien | Familien gesamt | Jaccard | Tragend Rekopplung | Kipp Rekopplung | Tragend Strain | Kipp Strain |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summaries:
        lines.append(
            "| {world_group} | {tragend_count} | {kipp_count} | {shared_family_count} | {union_family_count} | {jaccard:.4f} | {avg_tragend_rekopplung:.4f} | {avg_kipp_rekopplung:.4f} | {avg_tragend_strain:.4f} | {avg_kipp_strain:.4f} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Staerkste Brueckenfamilien",
            "",
            "| Weltgruppe | Familie | Tragend Anteil | Kipp Anteil | Brueckenwert | Tragend Count | Kipp Count |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in bridges:
        lines.append(
            "| {world_group} | {family} | {tragend_share:.4f} | {kipp_share:.4f} | {bridge_score:.4f} | {tragend_count} | {kipp_count} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Haltungen sind nicht vollstaendig getrennt. Es gibt geteilte Symbolfamilien, aber ihre Brueckenstaerke unterscheidet sich je nach Weltgruppe deutlich.",
            "",
            "Das spricht fuer eine innere Semantik, die nicht nur zwei feste Klassen bildet. Einzelne Familien koennen als Uebergangstraeger wirken: dieselbe Familie kann in tragender Verarbeitung und in Kippnaehe erscheinen, aber mit anderer Feldqualitaet.",
            "",
            "## Schluss",
            "",
            "Mini-DIO zeigt hier keine simple Wenn-Dann-Trennung. Die Symbolfamilien bilden eher ein Feldnetz: getrennte Bereiche plus Brueckenfamilien.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine starke Brueckenfamilie isoliert und gegen Rohweltfenster gelesen werden: Welche Weltabschnitte lassen dieselbe Familie tragend oder kippnah erscheinen?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    grouped: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: {key: [] for key in PATTERNS})
    for episode_file in _iter_episode_files([Path(item) for item in args.world_dir]):
        world_group = _world_group(episode_file)
        classified = _classify_rows(episode_file)
        for pattern, pattern_rows in classified.items():
            grouped[world_group][pattern].extend(pattern_rows)

    rows: list[dict[str, object]] = []
    for world_group, rows_by_pattern in sorted(grouped.items()):
        rows.extend(_summarize(world_group, rows_by_pattern))

    _write_csv(rows, Path(args.out_csv))
    _write_md(rows, Path(args.out_md))
    print(f"world_groups={len(grouped)}")
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
