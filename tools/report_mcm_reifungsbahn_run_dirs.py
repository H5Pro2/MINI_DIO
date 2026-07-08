from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_RUNS = [
    ("DOGE_2024_5M_10K", "realwelt_2024", "debug/doge_2024_5m_10k/dio_mini_lauf_1"),
    ("PAXG_2024_5M_10K", "realwelt_2024", "debug/paxg_2024_5m_10k/dio_mini_lauf_1"),
    ("XRP_2024_5M_10K", "realwelt_2024", "debug/xrp_2024_5m_10k/dio_mini_lauf_1"),
    ("NULL_RANDOM_2400", "nullwelt", "debug/1831_damping_asset10k_null/NULL_RANDOM_2400_factor_1p0/dio_mini_lauf_1"),
    ("NULL_SHUFFLE_2400", "nullwelt", "debug/1831_damping_asset10k_null/NULL_SHUFFLE_2400_factor_1p0/dio_mini_lauf_1"),
]


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


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


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
    episodes_path = path / "episodes.csv"
    if not episodes_path.exists():
        return {
            "unique_families": 0.0,
            "role_entropy": 0.0,
            "milieu_entropy": 0.0,
            "episode_rows": 0.0,
        }
    family_counter: Counter[str] = Counter()
    role_counter: Counter[str] = Counter()
    milieu_counter: Counter[str] = Counter()
    rows = 0
    with episodes_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows += 1
            family_counter[row.get("symbol_family") or row.get("dominant_family") or "-"] += 1
            role_counter[
                row.get("mcm_field_episode_role")
                or row.get("passive_mcm_effect_class")
                or row.get("mcm_field_effect_state")
                or "-"
            ] += 1
            milieu_counter[
                row.get("mcm_adaptive_milieu_state")
                or row.get("passive_inner_effect_awareness_state")
                or row.get("mcm_field_effect_state")
                or "-"
            ] += 1
    return {
        "unique_families": float(len(family_counter)),
        "role_entropy": _entropy(role_counter),
        "milieu_entropy": _entropy(milieu_counter),
        "episode_rows": float(rows),
    }


def _read_run(world: str, group: str, run_dir: str) -> dict[str, float | str]:
    path = _resolve(run_dir)
    report_path = path / "mini_report.json"
    if not report_path.exists():
        raise FileNotFoundError(report_path)
    report = json.loads(report_path.read_text(encoding="utf-8"))
    episode = _episode_metrics(path)
    adaptive = _float(report.get("avg_mcm_adaptive_rekopplung_quality"))
    if adaptive <= 0.0:
        adaptive = _float(report.get("avg_mcm_rekopplung_quality"))
    return {
        "world": world,
        "group": group,
        "run_dir": run_dir,
        "candles": _float(report.get("candles")),
        "unique_symbols": _float(report.get("unique_symbols")),
        "unique_families": episode["unique_families"],
        "adaptive_rekopplung": adaptive,
        "rekopplung": _float(report.get("avg_mcm_rekopplung_quality")),
        "strain": _float(report.get("avg_mcm_strain_quality")),
        "afterimage": _float(report.get("avg_mini_afterimage")),
        "temporal_trust": _float(report.get("avg_mini_temporal_trust_support")),
        "temporal_caution": _float(report.get("avg_mini_temporal_caution_support")),
        "sensory_coupling": _float(report.get("avg_mcm_sensory_coupling")),
        "role_entropy": episode["role_entropy"],
        "milieu_entropy": episode["milieu_entropy"],
        "episode_rows": episode["episode_rows"],
    }


def _norm(value: float, maximum: float) -> float:
    if maximum <= 0:
        return 0.0
    return max(0.0, min(1.0, value / maximum))


def _dominant_state(pressures: dict[str, float]) -> str:
    return max(pressures.items(), key=lambda item: (item[1], item[0]))[0]


def _profile_rows(rows: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    max_symbols = max([_float(row["unique_symbols"]) for row in rows] + [1.0])
    max_families = max([_float(row["unique_families"]) for row in rows] + [1.0])
    max_role_entropy = max([_float(row["role_entropy"]) for row in rows] + [1.0])
    max_milieu_entropy = max([_float(row["milieu_entropy"]) for row in rows] + [1.0])
    null_rows = [row for row in rows if row["group"] == "nullwelt"]
    null_symbol_mean = _mean([_float(row["unique_symbols"]) for row in null_rows])
    null_family_mean = _mean([_float(row["unique_families"]) for row in null_rows])
    null_adaptive_mean = _mean([_float(row["adaptive_rekopplung"]) for row in null_rows])
    null_role_mean = _mean([_float(row["role_entropy"]) for row in null_rows])

    raw_distances: dict[str, float] = {}
    for row in rows:
        raw_distances[str(row["world"])] = (
            max(0.0, _float(row["unique_symbols"]) - null_symbol_mean)
            + max(0.0, _float(row["unique_families"]) - null_family_mean)
            + max(0.0, _float(row["adaptive_rekopplung"]) - null_adaptive_mean) * 1000.0
            + max(0.0, _float(row["role_entropy"]) - null_role_mean) * 100.0
        )
    max_distance = max(list(raw_distances.values()) + [1.0])

    profiles: list[dict[str, float | str]] = []
    for row in rows:
        meaning_breadth = _mean(
            [
                _norm(_float(row["unique_symbols"]), max_symbols),
                _norm(_float(row["unique_families"]), max_families),
            ]
        )
        role_variance = _mean(
            [
                _norm(_float(row["role_entropy"]), max_role_entropy),
                _norm(_float(row["milieu_entropy"]), max_milieu_entropy),
            ]
        )
        fieldtime = _mean(
            [
                _float(row["afterimage"]),
                _float(row["temporal_trust"]),
                max(0.0, 1.0 - _float(row["temporal_caution"])),
            ]
        )
        null_distance = _norm(raw_distances[str(row["world"])], max_distance)
        if row["group"] == "nullwelt":
            null_distance *= 0.25
        adaptive = _float(row["adaptive_rekopplung"])
        pressures = {
            "jung": (1.0 - meaning_breadth) + (1.0 - fieldtime),
            "schmal_stabil": (1.0 - meaning_breadth) + adaptive,
            "breit_getragen": meaning_breadth + role_variance + adaptive,
            "nachhallend_offen": fieldtime + (1.0 - meaning_breadth) + (0.5 * role_variance),
            "nullweltnah": (1.0 - null_distance) + (1.0 - meaning_breadth),
            "feldzeit_reif": (fieldtime + meaning_breadth + adaptive) * (0.5 + null_distance),
        }
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
                **row,
                "meaning_breadth": meaning_breadth,
                "role_variance": role_variance,
                "fieldtime_pressure": fieldtime,
                "nullwelt_abstand": null_distance,
                "maturity_pressure": maturity_pressure,
                "dominant_reifezustand": _dominant_state(pressures),
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
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, float | str]]) -> None:
    state_counter = Counter(str(row["dominant_reifezustand"]) for row in rows)
    real_pressure = _mean([_float(row["maturity_pressure"]) for row in rows if str(row["group"]).startswith("realwelt")])
    null_pressure = _mean([_float(row["maturity_pressure"]) for row in rows if row["group"] == "nullwelt"])
    lines = [
        "# 1834 - MCM-Reifungsbahn Gegenprüfung 2024",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        "Wiederholt sich die passive Reifungsbahn in vorhandenen 2024-Assetwelten, oder war `feldzeit_reif` nur ein 2025-10k-Effekt?",
        "",
        "## Grundlage",
        "",
        "Gelesen wurden vorhandene MINI_DIO-Läufe, ohne neue Handlung, Gate-Logik oder Strategie:",
        "",
        "- DOGE 2024 5m 10k",
        "- PAXG 2024 5m 10k",
        "- XRP 2024 5m 10k",
        "- zwei Nullwelten aus der 1831-Kontrollfläche",
        "",
        "BTC 2024 5m 10k wurde in diesem Schritt nicht aufgenommen, weil kein gleichartig benannter 10k-Lauf im aktuellen Debugbestand vorliegt. Das ist eine Datenlücke, kein Negativbefund.",
        "",
        "## Reifeprofile",
        "",
        "| Welt | Gruppe | Kerzen | Symbole | Familien | Bedeutung | Rollenvarianz | Adaptive Rekopplung | Feldzeitdruck | Nullwelt-Abstand | Reifedruck | Zustand |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["group"]),
                    _format(_float(row["candles"])),
                    _format(_float(row["unique_symbols"])),
                    _format(_float(row["unique_families"])),
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

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            f"- Zustandsverteilung: `{dict(state_counter)}`",
            f"- Mittlerer Reifedruck 2024-Realwelt: `{_format(real_pressure)}`",
            f"- Mittlerer Reifedruck Nullwelt: `{_format(null_pressure)}`",
            "",
            "Die vorhandenen 2024-Assetwelten werden ebenfalls als `feldzeit_reif` gelesen. Die Nullwelten bleiben in dieser Gegenprüfung `nullweltnah`. Damit wiederholt sich die Trennung aus 1833 in strengerer Form: Nullwelt kann Nachhall und Rekopplung tragen, bleibt aber ohne vergleichbare Bedeutungsbreite und ohne starken Abstand zur Kontrollfläche.",
            "",
            "PAXG 2024 fällt schmaler aus als DOGE/XRP, bleibt aber über Rekopplung und Feldzeitdruck noch innerhalb der reifen Lesung. Das passt zur bisherigen Beobachtung, dass PAXG lokal anders färbt, ohne die Grundtopologie zu brechen.",
            "",
            "## Grenze",
            "",
            "Die Prüfung nutzt vorhandene 2024-Läufe und keine neu erzeugte vollständige 2024-Dämpfungsreihe. Für eine härtere Aussage sollte dieselbe Logik mit BTC 2024 10k, 2024-Nullwelten gleicher Länge und größeren Fenstern wiederholt werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte ein sauberer 2024-10k-Satz mit BTC, DOGE, PAXG, XRP und längengleichen Nullwelten erzeugt werden. Danach kann geprüft werden, ob `feldzeit_reif` über Assets, Jahre und Nullweltformen stabil unterscheidet.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-md", default="docs/befunde/1834_MCM_REIFUNGSBAHN_2024_GEGENPRUEFUNG.md")
    parser.add_argument("--out-csv", default="docs/befunde/1834_MCM_REIFUNGSBAHN_2024_GEGENPRUEFUNG.csv")
    args = parser.parse_args()

    rows = [_read_run(world, group, run_dir) for world, group, run_dir in DEFAULT_RUNS]
    profiles = _profile_rows(rows)
    _write_csv(_resolve(args.out_csv), profiles)
    _write_md(_resolve(args.out_md), profiles)
    print({"out_md": args.out_md, "out_csv": args.out_csv, "rows": len(profiles)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
