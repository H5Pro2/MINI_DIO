from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = befunde_root(ROOT) / "1573_SLEEP_KOMBI_VS_EINZEL_REKOPPLUNG_FELDMERKMALE.md"
DEFAULT_CSV = befunde_root(ROOT) / "1573_SLEEP_KOMBI_VS_EINZEL_REKOPPLUNG_FELDMERKMALE.csv"


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _load_summary(label: str) -> dict:
    path = ROOT / "debug" / "real_sleep_real" / label / "real_sleep_real_summary.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _metric(summary: dict, name: str, side: str = "real_a") -> float:
    metrics = dict(dict(summary.get("comparison", {}) or {}).get("metrics", {}) or {})
    item = dict(metrics.get(name, {}) or {})
    return _float(item.get(side))


def _classify(row: dict[str, object]) -> str:
    combos = _int(row.get("combination_trace_count"))
    roles = _int(row.get("touched_role_count"))
    if combos > 0 and roles >= 3:
        return "kombinationsfeld"
    if roles <= 1 and combos == 0:
        return "einzel_rekopplung"
    return "uebergang_oder_schwach_kombiniert"


def _row(label: str, group: str) -> dict[str, object]:
    summary = _load_summary(label)
    sleep = dict(summary.get("sleep_reorganization_memory", {}) or {})
    followup = dict(summary.get("sleep_reorganization_followup", {}) or {})
    comparison = dict(summary.get("comparison", {}) or {})
    real_a_states = dict(comparison.get("real_a_episode_states", {}) or {})
    real_a_effects = dict(comparison.get("real_a_effect_classes", {}) or {})
    episodes = max(1, _int(_metric(summary, "episodes")))
    row: dict[str, object] = {
        "label": label,
        "group_hint": group,
        "data_path": str(summary.get("data_path", "")),
        "follow_data_path": str(summary.get("follow_data_path", "")),
        "touched_role_count": _int(sleep.get("touched_role_count")),
        "combination_trace_count": _int(sleep.get("combination_trace_count")),
        "active_role_set_count": _int(sleep.get("active_role_set_count")),
        "avg_afterimage_abs": _float(sleep.get("avg_afterimage_abs")),
        "avg_signature_abs": _float(sleep.get("avg_signature_abs")),
        "sleep_unique_symbols": _int(sleep.get("sleep_unique_symbols")),
        "real_a_episode_memory": _int(_metric(summary, "episode_memory_written")),
        "real_a_mcm_field_episode": _int(_metric(summary, "mcm_field_episode_written")),
        "real_a_unique_symbols": _int(_metric(summary, "unique_symbols")),
        "real_a_rekopplung": _metric(summary, "avg_mcm_rekopplung_quality"),
        "real_a_carry": _metric(summary, "avg_mcm_carry_quality"),
        "real_a_strain": _metric(summary, "avg_mcm_strain_quality"),
        "real_a_sensory": _metric(summary, "avg_mcm_sensory_coupling"),
        "real_a_neuro_balance": _metric(summary, "avg_mini_neuro_balance"),
        "real_a_neuro_load": _metric(summary, "avg_mini_neuro_load"),
        "real_a_afterimage": _metric(summary, "avg_mini_afterimage"),
        "field_carried": _int(real_a_states.get("field_carried")),
        "field_strained": _int(real_a_states.get("field_strained")),
        "field_strained_ratio": _int(real_a_states.get("field_strained")) / episodes,
        "effect_stabil": _int(real_a_effects.get("stabil")),
        "effect_tragend_unruhig": _int(real_a_effects.get("tragend_unruhig")),
        "effect_kippend": _int(real_a_effects.get("kippend")),
        "effect_gespannt": _int(real_a_effects.get("gespannt")),
        "full_reactivated_combos": _int(followup.get("combination_fully_reactivated_count")),
        "partial_reactivated_combos": _int(followup.get("combination_partly_reactivated_count")),
    }
    row["actual_field_state"] = _classify(row)
    return row


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "label",
        "group_hint",
        "actual_field_state",
        "touched_role_count",
        "combination_trace_count",
        "active_role_set_count",
        "avg_afterimage_abs",
        "avg_signature_abs",
        "real_a_episode_memory",
        "real_a_mcm_field_episode",
        "real_a_unique_symbols",
        "real_a_rekopplung",
        "real_a_carry",
        "real_a_strain",
        "real_a_sensory",
        "real_a_neuro_balance",
        "real_a_neuro_load",
        "real_a_afterimage",
        "field_strained_ratio",
        "effect_stabil",
        "effect_tragend_unruhig",
        "effect_kippend",
        "effect_gespannt",
        "full_reactivated_combos",
        "partial_reactivated_combos",
        "data_path",
        "follow_data_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _avg(rows: list[dict[str, object]], key: str) -> float:
    if not rows:
        return 0.0
    return sum(_float(row.get(key)) for row in rows) / len(rows)


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    combo_rows = [row for row in rows if row["actual_field_state"] == "kombinationsfeld"]
    single_rows = [row for row in rows if row["actual_field_state"] == "einzel_rekopplung"]
    lines = [
        "# Sleep-Kombination vs Einzel-Rekopplung: Feldmerkmale",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese passive Diagnose vergleicht Welten, die Offline-Kombinationen bilden, mit Welten, die nur Einzel-Rekopplung bilden.",
        "",
        "Die Grundfrage lautet:",
        "",
        "```text",
        "Welche MCM-Feldmerkmale machen aus Rohwelt-Varianz mehrrollige Feldnaehe?",
        "```",
        "",
        "Die Diagnose erzeugt keine Handlung und keine neue MCM-Mechanik.",
        "",
        "## Einzelwelten",
        "",
        "| Label | Feldzustand | Rollen | Kombinationen | Episodenrollen | Afterimage | Rekopplung | Carry | Strain | Neuro-Balance |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["label"]),
                    str(row["actual_field_state"]),
                    str(row["touched_role_count"]),
                    str(row["combination_trace_count"]),
                    str(row["real_a_mcm_field_episode"]),
                    _fmt(row["real_a_afterimage"]),
                    _fmt(row["real_a_rekopplung"]),
                    _fmt(row["real_a_carry"]),
                    _fmt(row["real_a_strain"]),
                    _fmt(row["real_a_neuro_balance"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Gruppenmittel",
            "",
            "| Gruppe | Anzahl | Rollen | Kombinationen | Episodenrollen | Afterimage | Rekopplung | Carry | Strain | Neuro-Balance |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for name, group_rows in [("kombinationsfeld", combo_rows), ("einzel_rekopplung", single_rows)]:
        lines.append(
            "| "
            + " | ".join(
                [
                    name,
                    str(len(group_rows)),
                    _fmt(_avg(group_rows, "touched_role_count")),
                    _fmt(_avg(group_rows, "combination_trace_count")),
                    _fmt(_avg(group_rows, "real_a_mcm_field_episode")),
                    _fmt(_avg(group_rows, "real_a_afterimage")),
                    _fmt(_avg(group_rows, "real_a_rekopplung")),
                    _fmt(_avg(group_rows, "real_a_carry")),
                    _fmt(_avg(group_rows, "real_a_strain")),
                    _fmt(_avg(group_rows, "real_a_neuro_balance")),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "In den aktuellen Pruefwelten entsteht Kombinationsbildung nicht einfach aus hoher Rohweltbewegung.",
            "",
            "Auffaellig ist stattdessen:",
            "",
            "- Kombinationsfelder tragen mehrere MCM-Feldrollen gleichzeitig oder nahe genug.",
            "- Einzel-Rekopplungsfelder koennen rohweltlich aktiv sein, bleiben im MCM-Feld aber auf eine dominante Rolle gebunden.",
            "- Damit ist die entscheidende Trennlinie nicht Weltstaerke allein, sondern mehrrollige Feldnaehe.",
            "",
            "Kurz:",
            "",
            "```text",
            "Rohwelt-Varianz ist Material.",
            "MCM-Feldnaehe entscheidet, ob daraus Kombination wird.",
            "```",
            "",
            "## Grenze",
            "",
            "Die Stichprobe ist klein. Die Diagnose zeigt eine Arbeitsrichtung, keinen Beweis.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Vergleicht Sleep-Kombinationsfelder mit Einzel-Rekopplung.")
    parser.add_argument("--label", action="append", nargs=2, metavar=("GRUPPE", "LABEL"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    labels = args.label or [
        ("combo", "sol2024_soft_sleep_combo_same"),
        ("combo", "btc1000_soft_sleep_combo_same"),
        ("single", "paxg1000_soft_sleep_combo_same"),
        ("single", "kas1000_soft_sleep_combo_same"),
    ]
    rows = [_row(label, group) for group, label in labels]
    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    csv_path = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    _write_csv(rows, csv_path)
    _write_md(rows, out_path)


if __name__ == "__main__":
    main()
