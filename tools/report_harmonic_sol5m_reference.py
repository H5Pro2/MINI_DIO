from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from report_duration_load_decomposition import _row as duration_row
from report_local_world_feature_coupling import _read_candles, _world_features
from report_recoupling_quality import _load_json, _resolve
from report_recoupling_quality import _row as recoupling_row
from report_sensory_adaptation import _row as sensory_row


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "220_SOL5M_HARMONISCHE_REFERENZ_DIAGNOSE.md"


DEFAULT_SUMMARIES = [
    ("SOL_2024_5M", "debug/research_chain_sol_2024_5m_2k/research_chain_summary.json", "referenz"),
    ("SOL_2025_5M", "debug/research_chain_sol_2025_5m_2k/research_chain_summary.json", "referenz"),
    ("SOL_2024_30M", "debug/research_chain_sol_2024_30m_2k/research_chain_summary.json", "vergleich"),
    ("SOL_2025_30M", "debug/research_chain_sol_2025_30m_2k/research_chain_summary.json", "vergleich"),
    ("SOL_2024_1H", "debug/research_chain_sol_2024_1h_2k/research_chain_summary.json", "vergleich"),
    ("SOL_2025_1H", "debug/research_chain_sol_2025_1h_2k/research_chain_summary.json", "vergleich"),
    ("STRESS_2023_TEST4", "debug/research_chain_stress_segment_2023_test4_01/research_chain_summary.json", "stress"),
    ("STRESS_2024_REAL", "debug/research_chain_stress_segment_2024_real_test1_01/research_chain_summary.json", "stress"),
    ("STRESS_2025_STRESS", "debug/research_chain_stress_segment_2025_stress_01/research_chain_summary.json", "stress"),
]


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _avg(rows: list[dict], key: str) -> float:
    return sum(_float(row.get(key)) for row in rows) / max(1, len(rows))


def _row(name: str, path_text: str, group: str) -> dict:
    summary = _load_json(_resolve(path_text))
    rec = recoupling_row(name, summary)
    dur = duration_row(name, summary)
    sen = sensory_row(name, summary)
    world = _world_features(_read_candles(str(summary.get("data_path", ""))))
    sensory_metrics = sen["metrics"]

    field_load = _float(dur["field_strain_load"])
    memory_load = _float(dur["memory_load"])
    recoupling_loss = _float(dur["recoupling_loss"])
    duration_load = _float(dur["mcm_duration_load"])
    adapted_load = _float(sensory_metrics["adapted_load"])
    homeostasis = _float(sensory_metrics["homeostatic_balance"])
    attention = _float(sensory_metrics["attention_salience"])
    afterimage = _float(dur["afterimage_load"])
    compaction = _float(world["world_compaction"])

    harmonic_index = max(
        0.0,
        min(
            1.0,
            (homeostasis * 0.30)
            + (_float(rec["rekopplung"]) * 0.24)
            + ((1.0 - min(1.0, duration_load * 3.0)) * 0.18)
            + ((1.0 - min(1.0, memory_load * 3.0)) * 0.12)
            + ((1.0 - min(1.0, field_load * 3.0)) * 0.10)
            + ((1.0 - min(1.0, recoupling_loss * 6.0)) * 0.06),
        ),
    )
    overbinding_risk = max(
        0.0,
        min(
            1.0,
            (field_load * 0.30)
            + (memory_load * 0.24)
            + (recoupling_loss * 2.2 * 0.18)
            + (afterimage * 0.16)
            + (max(0.0, adapted_load - 1.0) * 0.12),
        ),
    )

    return {
        "name": name,
        "group": group,
        "role": rec["dominant_role"],
        "harmonic_index": harmonic_index,
        "overbinding_risk": overbinding_risk,
        "rekopplung": _float(rec["rekopplung"]),
        "field_load": field_load,
        "memory_load": memory_load,
        "duration_load": duration_load,
        "recoupling_loss": recoupling_loss,
        "afterimage": afterimage,
        "attention": attention,
        "adapted_load": adapted_load,
        "homeostasis": homeostasis,
        "world_compaction": compaction,
        "avg_range": _float(world["avg_range"]),
        "direction_change_ratio": _float(world["direction_change_ratio"]),
    }


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"]))
    reference = [row for row in rows if row["group"] == "referenz"]
    comparisons = [row for row in rows if row["group"] != "referenz"]

    ref_harmonic = _avg(reference, "harmonic_index")
    ref_risk = _avg(reference, "overbinding_risk")
    ref_duration = _avg(reference, "duration_load")
    ref_memory = _avg(reference, "memory_load")
    ref_field = _avg(reference, "field_load")
    ref_rec = _avg(reference, "rekopplung")

    lines = [
        "# SOL 5m als harmonische Referenz - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt SOL 5m als harmonische Referenz gegen groebere SOL-Aufloesungen und lokale Stresssegmente.",
        "Sie prueft passiv, welche Feldmerkmale die 5m-Welt tragfaehiger machen.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Warum wirkt SOL 5m im bisherigen Lauf harmonischer als groebere oder stressnahe Welten?",
        "2. Unterpruefung: Rekopplung, Dauerlast, Feldlast, Memorylast, Nachhall, Reizadaptation und Weltverdichtung vergleichen.",
        "3. Folgeschritt: Aus den stabilisierenden Merkmalen eine passive Feldhygiene ableiten, keine Handlung und kein Gate.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | Gruppe | Rolle | Harmonie | Ueberbindung | Rekopplung | Dauerlast | Feldlast | Memorylast | Nachhall | Adaptierte Last | Homoestase | Verdichtung | Richtungswechsel |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["group"],
                    row["role"],
                    _fmt(row["harmonic_index"], 4),
                    _fmt(row["overbinding_risk"], 4),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["duration_load"], 4),
                    _fmt(row["field_load"], 4),
                    _fmt(row["memory_load"], 4),
                    _fmt(row["afterimage"], 4),
                    _fmt(row["adapted_load"], 4),
                    _fmt(row["homeostasis"], 4),
                    _fmt(row["world_compaction"], 4),
                    _fmt(row["direction_change_ratio"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Referenzmittel SOL 5m",
            "",
            f"- Harmonieindex: `{_fmt(ref_harmonic, 4)}`",
            f"- Ueberbindungsrisiko: `{_fmt(ref_risk, 4)}`",
            f"- Rekopplung: `{_fmt(ref_rec, 6)}`",
            f"- Dauerlast: `{_fmt(ref_duration, 4)}`",
            f"- Feldlast: `{_fmt(ref_field, 4)}`",
            f"- Memorylast: `{_fmt(ref_memory, 4)}`",
            "",
            "## Abweichung gegen SOL 5m",
            "",
            "| Welt | Rolle | Harmonie-Abstand | Risiko-Abstand | Dauerlast-Abstand | Memory-Abstand | Feldlast-Abstand |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in sorted(comparisons, key=lambda item: item["harmonic_index"]):
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["role"],
                    _fmt(ref_harmonic - row["harmonic_index"], 4),
                    _fmt(row["overbinding_risk"] - ref_risk, 4),
                    _fmt(row["duration_load"] - ref_duration, 4),
                    _fmt(row["memory_load"] - ref_memory, 4),
                    _fmt(row["field_load"] - ref_field, 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Diagnose-Lesart",
            "",
            "- Eine harmonische Welt ist hier nicht reizarm, sondern gut rekoppelbar.",
            "- SOL 5m gilt nur als aktuelle Referenz, nicht als Regel fuer alle Daten.",
            "- Groebere Aufloesungen koennen weniger Ticks liefern, aber pro Kontakt mehr Feldwirkung tragen.",
            "- Wenn Memorylast und Feldlast steigen, wird Wahrnehmung eher zu gebundener Feldhistorie.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Dort wird festgehalten, welche Merkmalskombination SOL 5m tragfaehiger macht und welche Schutzrichtung daraus fuer MINI_DIO folgt.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Vergleicht SOL 5m als harmonische Referenz gegen groebere/stressnahe Welten.")
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    rows = [_row(name, path_text, group) for name, path_text, group in specs]
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
