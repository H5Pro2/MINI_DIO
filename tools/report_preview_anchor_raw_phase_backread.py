from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


TARGETS = [
    "dio_mcm_episode_0vcr3lw",
    "dio_mcm_episode_1rj8742",
    "dio_mcm_episode_0bsaqu1",
    "dio_mcm_episode_08g1nk4",
    "dio_mcm_episode_1eav7xq",
    "dio_mcm_episode_1qlxgj7",
]


def _float(value: object) -> float:
    try:
        result = float(value)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _phase(avg_visual_gap: float, avg_hearing_gap: float, avg_tension: float, avg_carry: float) -> str:
    if avg_tension >= 0.56 and avg_hearing_gap >= 0.16:
        return "spannung_hoerende_randnaehe"
    if avg_visual_gap >= 0.22 and avg_carry >= 0.50:
        return "sichtbare_uebergangsnaehe"
    if avg_carry >= 0.54 and avg_tension <= 0.48:
        return "ruhig_getragene_nahe"
    if avg_visual_gap >= 0.20 or avg_hearing_gap >= 0.18:
        return "offene_sensorische_randnaehe"
    return "zentrumsnah_getragen"


def _iter_episode_files(debug_roots: list[Path]):
    for root in debug_roots:
        if root.is_file() and root.name == "episodes.csv":
            yield root
        elif root.exists():
            yield from sorted(root.glob("dio_mini_lauf_*/episodes.csv"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    debug_roots = [Path(value) for value in args.debug_root]
    buckets: dict[str, dict[str, object]] = {
        target: {
            "count": 0,
            "worlds": Counter(),
            "states": Counter(),
            "effects": Counter(),
            "families": Counter(),
            "depth": [],
            "profile": [],
            "carry": [],
            "strain": [],
            "rekopplung": [],
            "sensory": [],
            "visual_gap": [],
            "hearing_gap": [],
            "coherence": [],
            "tension": [],
            "asymmetry": [],
            "visual_salience": [],
            "field_pressure": [],
        }
        for target in TARGETS
    }

    for episode_file in _iter_episode_files(debug_roots):
        with episode_file.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                symbol = row.get("mcm_field_episode_preview_symbol", "")
                if symbol not in buckets:
                    continue
                bucket = buckets[symbol]
                bucket["count"] = int(bucket["count"]) + 1
                bucket["worlds"][row.get("passive_world_label", "-") or "-"] += 1
                bucket["states"][row.get("mcm_preview_anchor_depth_state", "-") or "-"] += 1
                bucket["effects"][row.get("passive_mcm_effect_class", "-") or "-"] += 1
                bucket["families"][row.get("symbol_family", "-") or "-"] += 1
                bucket["depth"].append(_float(row.get("mcm_preview_anchor_depth_score")))
                bucket["profile"].append(_float(row.get("mcm_preview_anchor_profile_proximity")))
                bucket["carry"].append(_float(row.get("mcm_carry_quality")))
                bucket["strain"].append(_float(row.get("mcm_strain_quality")))
                bucket["rekopplung"].append(_float(row.get("mcm_rekopplung_quality")))
                bucket["sensory"].append(_float(row.get("mcm_sensory_coupling")))
                bucket["visual_gap"].append(_float(row.get("mcm_visual_field_gap")))
                bucket["hearing_gap"].append(_float(row.get("mcm_hearing_field_gap")))
                bucket["coherence"].append(_float(row.get("mcm_feldwirkung_mcm_coherence")))
                bucket["tension"].append(_float(row.get("mcm_feldwirkung_mcm_tension")))
                bucket["asymmetry"].append(_float(row.get("mcm_feldwirkung_mcm_asymmetry")))
                bucket["visual_salience"].append(_float(row.get("rezeptor_visual_form_salience")))
                bucket["field_pressure"].append(_float(row.get("rezeptor_field_intake_pressure")))

    rows = []
    for symbol, bucket in buckets.items():
        count = int(bucket["count"])
        avg_visual_gap = _avg(bucket["visual_gap"])
        avg_hearing_gap = _avg(bucket["hearing_gap"])
        avg_tension = _avg(bucket["tension"])
        avg_carry = _avg(bucket["carry"])
        rows.append(
            {
                "preview_symbol": symbol,
                "count": count,
                "world_count": len([world for world in bucket["worlds"] if world and world != "-"]),
                "top_worlds": ";".join(f"{key}:{value}" for key, value in bucket["worlds"].most_common(5)),
                "top_states": ";".join(f"{key}:{value}" for key, value in bucket["states"].most_common(5)),
                "top_effects": ";".join(f"{key}:{value}" for key, value in bucket["effects"].most_common(5)),
                "top_families": ";".join(f"{key}:{value}" for key, value in bucket["families"].most_common(5)),
                "avg_depth": round(_avg(bucket["depth"]), 6),
                "avg_profile": round(_avg(bucket["profile"]), 6),
                "avg_carry": round(avg_carry, 6),
                "avg_strain": round(_avg(bucket["strain"]), 6),
                "avg_rekopplung": round(_avg(bucket["rekopplung"]), 6),
                "avg_sensory": round(_avg(bucket["sensory"]), 6),
                "avg_visual_gap": round(avg_visual_gap, 6),
                "avg_hearing_gap": round(avg_hearing_gap, 6),
                "avg_coherence": round(_avg(bucket["coherence"]), 6),
                "avg_tension": round(avg_tension, 6),
                "avg_asymmetry": round(_avg(bucket["asymmetry"]), 6),
                "avg_visual_salience": round(_avg(bucket["visual_salience"]), 6),
                "avg_field_pressure": round(_avg(bucket["field_pressure"]), 6),
                "raw_phase_reading": _phase(avg_visual_gap, avg_hearing_gap, avg_tension, avg_carry),
            }
        )

    out = Path(args.out_csv)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
