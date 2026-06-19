from __future__ import annotations

import argparse
import csv
import math
from collections import Counter
from datetime import datetime
from pathlib import Path

from report_auditory_regulation import DEFAULT_SUMMARIES
from report_auditory_regulation import _fmt
from report_recoupling_quality import _resolve


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "234_LOKALE_MULTISENSORISCHE_KOPPLUNG_DIAGNOSE.md"


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    index = (len(values) - 1) * q
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return values[int(index)]
    return values[lower] * (upper - index) + values[upper] * (index - lower)


def _episode_files(summary_path: Path) -> list[Path]:
    return sorted(summary_path.parent.glob("dio_mini_lauf_*/episodes.csv"))


def _read_episode_rows(summary_path: Path) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for path in _episode_files(summary_path):
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for raw in reader:
                rows.append(
                    {
                        "tick": _float(raw.get("tick")),
                        "hearing_tone": abs(_float(raw.get("hoeren_energy_tone"))),
                        "hearing_shift": abs(_float(raw.get("hoeren_energy_shift"))),
                        "hearing_gap": _float(raw.get("mcm_hearing_field_gap")),
                        "visual_flow": abs(_float(raw.get("sehen_form_flow"))),
                        "visual_stability": _float(raw.get("sehen_form_stability")),
                        "visual_change": abs(_float(raw.get("sehen_form_change"))),
                        "visual_gap": _float(raw.get("mcm_visual_field_gap")),
                        "field_carry": _float(raw.get("mcm_carry_quality")),
                        "field_strain": _float(raw.get("mcm_strain_quality")),
                        "rekopplung": _float(raw.get("mcm_rekopplung_quality")),
                        "sensory_coupling": _float(raw.get("mcm_sensory_coupling")),
                        "binding_pressure": _float(raw.get("episode_binding_pressure")),
                        "release_pressure": _float(raw.get("episode_release_pressure")),
                        "afterimage": _float(raw.get("mini_afterimage")),
                    }
                )
    return rows


def _avg(rows: list[dict[str, float]], key: str) -> float:
    if not rows:
        return 0.0
    return sum(row[key] for row in rows) / len(rows)


def _window_rows(rows: list[dict[str, float]], size: int, step: int) -> list[list[dict[str, float]]]:
    if not rows:
        return []
    if len(rows) <= size:
        return [rows]
    return [rows[index : index + size] for index in range(0, len(rows) - size + 1, step)]


def _score_window(name: str, group: str, run_index: int, window_index: int, rows: list[dict[str, float]]) -> dict:
    visual_stability = _clamp((_avg(rows, "visual_stability") + 1.0) * 0.5)
    hearing_load = _clamp(
        (_avg(rows, "hearing_tone") * 0.24)
        + (_avg(rows, "hearing_shift") * 0.34)
        + (_avg(rows, "hearing_gap") * 0.20)
        + (max(0.0, 0.64 - _avg(rows, "rekopplung")) * 0.22)
    )
    visual_load = _clamp(
        (_avg(rows, "visual_flow") * 0.22)
        + (_avg(rows, "visual_change") * 0.30)
        + (_avg(rows, "visual_gap") * 0.20)
        + ((1.0 - visual_stability) * 0.18)
        + (_avg(rows, "afterimage") * 0.10)
    )
    field_pressure = _clamp(
        (_avg(rows, "field_strain") * 0.34)
        + (max(0.0, 0.64 - _avg(rows, "rekopplung")) * 0.24)
        + (_avg(rows, "binding_pressure") * 0.22)
        + ((1.0 - _avg(rows, "field_carry")) * 0.20)
    )
    relief = _clamp(
        (_avg(rows, "rekopplung") * 0.34)
        + (_avg(rows, "sensory_coupling") * 0.24)
        + (_avg(rows, "field_carry") * 0.20)
        + (_avg(rows, "release_pressure") * 0.22)
    )
    sensory_conflict = _clamp(abs(hearing_load - visual_load) + abs(_avg(rows, "hearing_gap") - _avg(rows, "visual_gap")) * 0.35)
    kipp_pressure = _clamp((hearing_load * 0.24) + (visual_load * 0.24) + (field_pressure * 0.36) + (sensory_conflict * 0.16))
    fit = _clamp(1.0 - abs(((hearing_load + visual_load) * 0.5) - field_pressure))

    return {
        "name": name,
        "group": group,
        "run": run_index,
        "window": window_index,
        "tick_start": int(rows[0]["tick"]),
        "tick_end": int(rows[-1]["tick"]),
        "hearing_load": hearing_load,
        "visual_load": visual_load,
        "field_pressure": field_pressure,
        "relief": relief,
        "sensory_conflict": sensory_conflict,
        "kipp_pressure": kipp_pressure,
        "fit": fit,
        "rekopplung": _avg(rows, "rekopplung"),
        "field_strain": _avg(rows, "field_strain"),
        "field_carry": _avg(rows, "field_carry"),
        "afterimage": _avg(rows, "afterimage"),
    }


def _classify_windows(windows: list[dict]) -> list[dict]:
    if not windows:
        return []
    kipp_p80 = _percentile([row["kipp_pressure"] for row in windows], 0.80)
    conflict_p80 = _percentile([row["sensory_conflict"] for row in windows], 0.80)
    relief_p70 = _percentile([row["relief"] for row in windows], 0.70)
    field_mid = _percentile([row["field_pressure"] for row in windows], 0.50)
    for row in windows:
        if row["kipp_pressure"] >= kipp_p80 and row["field_pressure"] >= field_mid:
            role = "lokale_multisensorische_kippnaehe"
        elif row["sensory_conflict"] >= conflict_p80 and row["kipp_pressure"] >= kipp_p80:
            role = "lokales_sinnesreiben"
        elif row["relief"] >= relief_p70 and row["fit"] >= 0.90:
            role = "lokal_rekoppelnd"
        else:
            role = "lokal_offen"
        row["local_role"] = role
    return windows


def _rows_for_summary(name: str, path_text: str, group: str, window_size: int, step: int) -> list[dict]:
    summary_path = _resolve(path_text)
    scored: list[dict] = []
    for run_index, episode_path in enumerate(_episode_files(summary_path), start=1):
        rows: list[dict[str, float]] = []
        with episode_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for raw in reader:
                rows.append(
                    {
                        "tick": _float(raw.get("tick")),
                        "hearing_tone": abs(_float(raw.get("hoeren_energy_tone"))),
                        "hearing_shift": abs(_float(raw.get("hoeren_energy_shift"))),
                        "hearing_gap": _float(raw.get("mcm_hearing_field_gap")),
                        "visual_flow": abs(_float(raw.get("sehen_form_flow"))),
                        "visual_stability": _float(raw.get("sehen_form_stability")),
                        "visual_change": abs(_float(raw.get("sehen_form_change"))),
                        "visual_gap": _float(raw.get("mcm_visual_field_gap")),
                        "field_carry": _float(raw.get("mcm_carry_quality")),
                        "field_strain": _float(raw.get("mcm_strain_quality")),
                        "rekopplung": _float(raw.get("mcm_rekopplung_quality")),
                        "sensory_coupling": _float(raw.get("mcm_sensory_coupling")),
                        "binding_pressure": _float(raw.get("episode_binding_pressure")),
                        "release_pressure": _float(raw.get("episode_release_pressure")),
                        "afterimage": _float(raw.get("mini_afterimage")),
                    }
                )
        for window_index, window in enumerate(_window_rows(rows, window_size, step), start=1):
            scored.append(_score_window(name, group, run_index, window_index, window))
    return _classify_windows(scored)


def _write_csv(rows: list[dict], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "name",
                "group",
                "run",
                "window",
                "tick_start",
                "tick_end",
                "local_role",
                "hearing_load",
                "visual_load",
                "field_pressure",
                "relief",
                "sensory_conflict",
                "kipp_pressure",
                "fit",
                "rekopplung",
                "field_strain",
                "field_carry",
                "afterimage",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in writer.fieldnames})


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"], row["run"], row["window"]))
    _write_csv(rows, out_path)

    counts_by_world: dict[str, Counter] = {}
    for row in rows:
        counts_by_world.setdefault(row["name"], Counter())[row["local_role"]] += 1

    strongest_kipp = sorted(rows, key=lambda row: row["kipp_pressure"], reverse=True)[:12]
    strongest_relief = sorted(rows, key=lambda row: row["relief"], reverse=True)[:12]

    lines = [
        "# Lokale multisensorische Kopplung - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest kurze Abschnitte innerhalb einer Welt.",
        "Sie prueft, ob Hoeren, Sehen und MCM-Feldwirkung lokal gemeinsam kippen oder rekoppeln.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Gibt es gemeinsame Sinnesinnenlagen innerhalb einer Welt?",
        "2. Unterpruefung: Wo steigen Hoerlast, Sehlast und Felddruck lokal gemeinsam?",
        "3. Folgeschritt: Pruefen, ob lokale Kippnaehe nur kurz aufflammt oder wiederkehrende Innenfeldinseln bildet.",
        "",
        "## Rollen nach Welt",
        "",
        "| Welt | lokal offen | lokal rekoppelnd | Sinnesreiben | Kippnaehe |",
        "|---|---:|---:|---:|---:|",
    ]
    for world in sorted(counts_by_world):
        counter = counts_by_world[world]
        lines.append(
            f"| {world} | {counter.get('lokal_offen', 0)} | {counter.get('lokal_rekoppelnd', 0)} | "
            f"{counter.get('lokales_sinnesreiben', 0)} | {counter.get('lokale_multisensorische_kippnaehe', 0)} |"
        )

    lines.extend(
        [
            "",
            "## Staerkste lokale Kippnaehe",
            "",
            "| Welt | Lauf | Ticks | Rolle | Hoerlast | Sehlast | Felddruck | Entlastung | Konflikt | Kippnaehe | Rekopplung |",
            "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in strongest_kipp:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    str(row["run"]),
                    f"{row['tick_start']}-{row['tick_end']}",
                    row["local_role"],
                    _fmt(row["hearing_load"], 4),
                    _fmt(row["visual_load"], 4),
                    _fmt(row["field_pressure"], 4),
                    _fmt(row["relief"], 4),
                    _fmt(row["sensory_conflict"], 4),
                    _fmt(row["kipp_pressure"], 4),
                    _fmt(row["rekopplung"], 6),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Staerkste lokale Rekopplung / Entlastung",
            "",
            "| Welt | Lauf | Ticks | Rolle | Entlastung | Fit | Rekopplung | Feldlast | Nachhall |",
            "|---|---:|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in strongest_relief:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    str(row["run"]),
                    f"{row['tick_start']}-{row['tick_end']}",
                    row["local_role"],
                    _fmt(row["relief"], 4),
                    _fmt(row["fit"], 4),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["field_strain"], 4),
                    _fmt(row["afterimage"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Vorlaeufige Lesart",
            "",
            "Die Rollen werden relativ innerhalb der jeweiligen Welt gelesen.",
            "Eine lokale Kippnaehe ist also kein absoluter Grenzwert, sondern ein Abschnitt, der gegen seine eigene Welt deutlich hervortritt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Darin wird bewertet, ob lokale Kippnaehe nur Oberflaechenvarianz ist oder eine wiederkehrende multisensorische Innenfeldinsel bildet.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Liest lokale multisensorische Kopplung innerhalb einzelner Welten.")
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--window-size", type=int, default=80)
    parser.add_argument("--step", type=int, default=40)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    rows: list[dict] = []
    for name, path_text, group in specs:
        rows.extend(_rows_for_summary(name, path_text, group, args.window_size, args.step))
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
