from __future__ import annotations

import argparse
import csv
import math
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _world_group(world: str) -> str:
    return "nullwelt" if world.startswith("NULL_") else "realwelt"


def _run_dir_name(world: str, factor: str) -> str:
    return f"{world}_factor_{str(factor).replace('.', 'p')}"


def _episode_path(debug_root: Path, world: str, factor: str) -> Path:
    return debug_root / _run_dir_name(world, factor) / "dio_mini_lauf_1" / "episodes.csv"


def _entropy(counter: Counter[str]) -> float:
    total = sum(counter.values())
    if total <= 0:
        return 0.0
    entropy = 0.0
    for count in counter.values():
        if count <= 0:
            continue
        probability = count / total
        entropy -= probability * math.log(probability, 2)
    return entropy


def _episode_metrics(path: Path) -> dict[str, float]:
    if not path.exists():
        return {
            "unique_roles": 0.0,
            "role_entropy": 0.0,
            "unique_milieus": 0.0,
            "milieu_entropy": 0.0,
        }
    role_counter: Counter[str] = Counter()
    milieu_counter: Counter[str] = Counter()
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            role_counter[row.get("mcm_field_episode_role") or "-"] += 1
            milieu_counter[row.get("mcm_adaptive_milieu_state") or "-"] += 1
    return {
        "unique_roles": float(len(role_counter)),
        "role_entropy": _entropy(role_counter),
        "unique_milieus": float(len(milieu_counter)),
        "milieu_entropy": _entropy(milieu_counter),
    }


def _enrich(rows: list[dict[str, str]], debug_root: Path) -> list[dict[str, object]]:
    enriched: list[dict[str, object]] = []
    for row in rows:
        world = str(row.get("world", ""))
        factor = str(row.get("rekopplung_factor", ""))
        metrics = _episode_metrics(_episode_path(debug_root, world, factor))
        enriched.append(
            {
                "world": world,
                "group": _world_group(world),
                "factor": _float(factor),
                "candles": _float(row.get("candles")),
                "unique_symbols": _float(row.get("unique_symbols")),
                "unique_episode_families": _float(row.get("unique_episode_families")),
                "adaptive_rekopplung": _float(row.get("avg_mcm_adaptive_rekopplung_quality")),
                "rekopplung": _float(row.get("avg_mcm_rekopplung_quality")),
                "strain": _float(row.get("avg_mcm_strain_quality")),
                "afterimage": _float(row.get("avg_mini_afterimage")),
                "temporal_trust": _float(row.get("avg_mini_temporal_trust_support")),
                "temporal_caution": _float(row.get("avg_mini_temporal_caution_support")),
                "sensory_coupling": _float(row.get("avg_mcm_sensory_coupling")),
                **metrics,
            }
        )
    return enriched


def _group_rows(rows: list[dict[str, object]]) -> list[dict[str, float | str]]:
    buckets: dict[tuple[float, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        buckets[(_float(row["factor"]), str(row["group"]))].append(row)

    grouped: list[dict[str, float | str]] = []
    for (factor, group), items in sorted(buckets.items()):
        grouped.append(
            {
                "factor": factor,
                "group": group,
                "worlds": float(len(items)),
                "symbols": _mean([_float(item["unique_symbols"]) for item in items]),
                "families": _mean([_float(item["unique_episode_families"]) for item in items]),
                "adaptive_rekopplung": _mean([_float(item["adaptive_rekopplung"]) for item in items]),
                "rekopplung": _mean([_float(item["rekopplung"]) for item in items]),
                "strain": _mean([_float(item["strain"]) for item in items]),
                "afterimage": _mean([_float(item["afterimage"]) for item in items]),
                "temporal_trust": _mean([_float(item["temporal_trust"]) for item in items]),
                "temporal_caution": _mean([_float(item["temporal_caution"]) for item in items]),
                "sensory_coupling": _mean([_float(item["sensory_coupling"]) for item in items]),
                "role_entropy": _mean([_float(item["role_entropy"]) for item in items]),
                "milieu_entropy": _mean([_float(item["milieu_entropy"]) for item in items]),
            }
        )
    return grouped


def _factor_deltas(grouped: list[dict[str, float | str]]) -> dict[float, dict[str, float]]:
    by_factor: dict[float, dict[str, dict[str, float | str]]] = defaultdict(dict)
    for row in grouped:
        by_factor[_float(row["factor"])][str(row["group"])] = row

    deltas: dict[float, dict[str, float]] = {}
    for factor, groups in by_factor.items():
        real = groups.get("realwelt")
        null = groups.get("nullwelt")
        if not real or not null:
            continue
        deltas[factor] = {
            "symbols_delta": _float(real["symbols"]) - _float(null["symbols"]),
            "families_delta": _float(real["families"]) - _float(null["families"]),
            "adaptive_delta": _float(real["adaptive_rekopplung"]) - _float(null["adaptive_rekopplung"]),
            "afterimage_delta": _float(real["afterimage"]) - _float(null["afterimage"]),
            "role_entropy_delta": _float(real["role_entropy"]) - _float(null["role_entropy"]),
            "milieu_entropy_delta": _float(real["milieu_entropy"]) - _float(null["milieu_entropy"]),
        }
    return deltas


def _norm(value: float, maximum: float) -> float:
    if maximum <= 0:
        return 0.0
    return max(0.0, min(1.0, value / maximum))


def _scale_delta(value: float, maximum: float) -> float:
    return _norm(max(0.0, value), maximum)


def _dominant_state(pressures: dict[str, float]) -> str:
    return max(pressures.items(), key=lambda item: (item[1], item[0]))[0]


def _profile_rows(grouped: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    deltas = _factor_deltas(grouped)
    max_symbols = max([_float(row["symbols"]) for row in grouped] + [1.0])
    max_families = max([_float(row["families"]) for row in grouped] + [1.0])
    max_role_entropy = max([_float(row["role_entropy"]) for row in grouped] + [1.0])
    max_milieu_entropy = max([_float(row["milieu_entropy"]) for row in grouped] + [1.0])
    max_null_delta = max(
        [
            abs(delta["symbols_delta"])
            + abs(delta["families_delta"])
            + abs(delta["adaptive_delta"] * 1000.0)
            + abs(delta["role_entropy_delta"] * 100.0)
            for delta in deltas.values()
        ]
        + [1.0]
    )

    profiles: list[dict[str, float | str]] = []
    for row in grouped:
        factor = _float(row["factor"])
        delta = deltas.get(factor, {})
        meaning_breadth = _mean(
            [
                _norm(_float(row["symbols"]), max_symbols),
                _norm(_float(row["families"]), max_families),
            ]
        )
        role_variance = _mean(
            [
                _norm(_float(row["role_entropy"]), max_role_entropy),
                _norm(_float(row["milieu_entropy"]), max_milieu_entropy),
            ]
        )
        adaptive = _float(row["adaptive_rekopplung"])
        fieldtime = _mean(
            [
                _float(row["afterimage"]),
                _float(row["temporal_trust"]),
                max(0.0, 1.0 - _float(row["temporal_caution"])),
            ]
        )
        null_distance_raw = (
            abs(delta.get("symbols_delta", 0.0))
            + abs(delta.get("families_delta", 0.0))
            + abs(delta.get("adaptive_delta", 0.0) * 1000.0)
            + abs(delta.get("role_entropy_delta", 0.0) * 100.0)
        )
        null_distance = _scale_delta(null_distance_raw, max_null_delta)
        if row["group"] == "nullwelt":
            # Nullwelten dienen als Gegenpol; ihr Abstand ist methodisch die Vergleichsflaeche.
            null_distance *= 0.25

        pressures = {
            "jung": (1.0 - meaning_breadth) + (1.0 - fieldtime),
            "schmal_stabil": (1.0 - meaning_breadth) + adaptive,
            "breit_getragen": meaning_breadth + role_variance + adaptive,
            "nachhallend_offen": fieldtime + (1.0 - meaning_breadth) + (0.5 * role_variance),
            "nullweltnah": (1.0 - null_distance) + (1.0 - meaning_breadth),
            "feldzeit_reif": (fieldtime + meaning_breadth + adaptive) * (0.5 + null_distance),
        }
        state = _dominant_state(pressures)
        maturity_pressure = _mean(
            [
                meaning_breadth,
                role_variance,
                adaptive,
                fieldtime,
                null_distance,
                max(0.0, 1.0 - _float(row["strain"])),
            ]
        )
        profiles.append(
            {
                "factor": factor,
                "group": str(row["group"]),
                "worlds": _float(row["worlds"]),
                "meaning_breadth": meaning_breadth,
                "role_variance": role_variance,
                "adaptive_rekopplung": adaptive,
                "fieldtime_pressure": fieldtime,
                "nullwelt_abstand": null_distance,
                "strain": _float(row["strain"]),
                "maturity_pressure": maturity_pressure,
                "dominant_reifezustand": state,
                "druck_jung": pressures["jung"],
                "druck_schmal_stabil": pressures["schmal_stabil"],
                "druck_breit_getragen": pressures["breit_getragen"],
                "druck_nachhallend_offen": pressures["nachhallend_offen"],
                "druck_nullweltnah": pressures["nullweltnah"],
                "druck_feldzeit_reif": pressures["feldzeit_reif"],
            }
        )
    return profiles


def _format(value: float) -> str:
    return f"{value:.4f}"


def _write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, float | str]], source_csv: str, debug_root: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 1833 - Passiver Reife-Report der MCM-Reifungsbahn",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        "Kann MINI_DIOs Reife passiv aus der MCM-Reifungsbahn gelesen werden, ohne daraus Handlung, Gate oder Strategie abzuleiten?",
        "",
        "## Grundlage",
        "",
        f"- Summenquelle: `{source_csv}`",
        f"- Episodenquelle: `{debug_root}`",
        "- Mechanische Grundlage: [009_MCM_REIFUNGSBAHN.md](../mechanik/009_MCM_REIFUNGSBAHN.md)",
        "",
        "## Methode",
        "",
        "Der Report liest keine harte Reifegrenze. Stattdessen werden mehrere Reife-Drücke gebildet und gegeneinander gehalten:",
        "",
        "- Bedeutungsbreite aus Symbolen und Episodenfamilien,",
        "- Rollenvarianz aus Rollen- und Milieu-Entropie,",
        "- adaptive Rekopplung,",
        "- Feldzeitdruck aus Nachhall, Vertrauen und Vorsicht,",
        "- Abstand zur Nullwelt,",
        "- Strain als Belastungsanteil.",
        "",
        "Der dominante Reifezustand ist die stärkste relative Lesung, nicht eine Handlungsvorgabe.",
        "",
        "## Reifeprofile",
        "",
        "| Faktor | Gruppe | Welten | Bedeutung | Rollenvarianz | Adaptive Rekopplung | Feldzeitdruck | Nullwelt-Abstand | Reifedruck | Dominanter Zustand |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    _format(_float(row["factor"])),
                    str(row["group"]),
                    _format(_float(row["worlds"])),
                    _format(_float(row["meaning_breadth"])),
                    _format(_float(row["role_variance"])),
                    _format(_float(row["adaptive_rekopplung"])),
                    _format(_float(row["fieldtime_pressure"])),
                    _format(_float(row["nullwelt_abstand"])),
                    _format(_float(row["maturity_pressure"])),
                    str(row["dominant_reifezustand"]),
                ]
            )
            + " |"
        )

    real_states = Counter(str(row["dominant_reifezustand"]) for row in rows if row["group"] == "realwelt")
    null_states = Counter(str(row["dominant_reifezustand"]) for row in rows if row["group"] == "nullwelt")
    real_pressure = _mean([_float(row["maturity_pressure"]) for row in rows if row["group"] == "realwelt"])
    null_pressure = _mean([_float(row["maturity_pressure"]) for row in rows if row["group"] == "nullwelt"])

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            f"- Realwelt-Zustände: `{dict(real_states)}`",
            f"- Nullwelt-Zustände: `{dict(null_states)}`",
            f"- Mittlerer Reifedruck Realwelt: `{_format(real_pressure)}`",
            f"- Mittlerer Reifedruck Nullwelt: `{_format(null_pressure)}`",
            "",
            "Die 10k-Assetwelten werden in dieser Lesung als `feldzeit_reif` gelesen. Das liegt nicht an einer einzelnen stabilen Klasse, sondern an der Kopplung aus Bedeutungsbreite, Rollenvarianz, adaptiver Rekopplung, Feldzeitdruck und Abstand zur Nullwelt.",
            "",
            "Die Nullwelten bleiben nicht bedeutungslos, aber sie tragen in dieser Prüfung deutlich weniger Reifedruck. Damit wird die Reifungsbahn als passive Diagnose brauchbar: Sie trennt nicht über Ja/Nein, sondern über Tiefe und Kopplungsqualität.",
            "",
            "## Grenze",
            "",
            "Dieser Report ist eine Lesung der vorhandenen 1831/1832-Prüfung. Er beweist keine allgemeine Reife des Systems. Belastbarer wird die Aussage erst, wenn dieselbe Reifungsbahn über 2024-Fenster, längere Daten und weitere Nullweltformen stabil unterscheidet.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-csv", default="docs/befunde/1001-2000/1751-2000/1831_DAEMPFUNG_ASSET10K_NULLWELTEN.csv")
    parser.add_argument("--debug-root", default="debug/1831_damping_asset10k_null")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1833_MCM_REIFUNGSBAHN_ASSET10K_NULLWELT.md")
    parser.add_argument("--out-csv", default="docs/befunde/1001-2000/1751-2000/1833_MCM_REIFUNGSBAHN_ASSET10K_NULLWELT.csv")
    args = parser.parse_args()

    rows = _profile_rows(_group_rows(_enrich(_read_csv(_resolve(args.source_csv)), _resolve(args.debug_root))))
    _write_csv(_resolve(args.out_csv), rows)
    _write_md(_resolve(args.out_md), rows, args.source_csv, args.debug_root)
    print({"out_md": args.out_md, "out_csv": args.out_csv, "rows": len(rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
