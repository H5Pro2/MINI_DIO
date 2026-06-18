from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "121_PASSIVE_FELDKLASSEN_DIAGNOSE.md"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _second(values: object) -> float:
    if isinstance(values, list) and len(values) >= 2:
        return _float(values[1])
    return 0.0


def _profile(summary: dict) -> dict[str, int]:
    return {str(key): int(value or 0) for key, value in (summary.get("passive_mcm_effect_classes") or {}).items()}


def _dominant_effect(profile: dict[str, int]) -> tuple[str, float]:
    total = max(1, sum(profile.values()))
    if not profile:
        return "-", 0.0
    name, count = max(profile.items(), key=lambda item: item[1])
    return name, round(count / total, 4)


def _world_metrics(data_path_text: str) -> dict[str, float]:
    path = Path(data_path_text)
    if not path.is_absolute():
        path = ROOT / path
    closes: list[float] = []
    highs: list[float] = []
    lows: list[float] = []
    if not path.exists():
        return {
            "avg_abs_return": 0.0,
            "max_abs_return": 0.0,
            "avg_range": 0.0,
            "drift": 0.0,
            "direction_changes": 0.0,
        }
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            closes.append(float(row["close"]))
            highs.append(float(row["high"]))
            lows.append(float(row["low"]))
    returns = [
        abs((closes[index] - closes[index - 1]) / closes[index - 1])
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
    ranges = [(high - low) / close for high, low, close in zip(highs, lows, closes) if close]
    direction_changes = sum(
        1
        for index in range(2, len(closes))
        if (closes[index] - closes[index - 1]) * (closes[index - 1] - closes[index - 2]) < 0
    )
    drift = ((closes[-1] - closes[0]) / closes[0]) if closes else 0.0
    return {
        "avg_abs_return": round(sum(returns) / max(1, len(returns)), 6),
        "max_abs_return": round(max(returns) if returns else 0.0, 6),
        "avg_range": round(sum(ranges) / max(1, len(ranges)), 6),
        "drift": round(drift, 6),
        "direction_changes": float(direction_changes),
    }


def _classify(row: dict) -> str:
    profile = row["profile"]
    stable = profile.get("stabil", 0)
    strained = profile.get("gespannt", 0) + profile.get("kippend", 0)
    restless = profile.get("tragend_unruhig", 0)
    rekopplung = row["rekopplung"]
    carry = row["carry"]
    memory = row["episode_memory"]

    if rekopplung >= 0.630 and carry >= 0.359 and stable >= 500 and strained <= 75:
        return "ruhige Nähegruppe"
    if rekopplung <= 0.617 or carry <= 0.348 or strained >= 170 or memory >= 100:
        return "Stress-Gegenpol"
    if restless >= stable or strained >= 120:
        return "angespannte Übergangsgruppe"
    return "mittlere Feldlage"


def build_rows(summaries: list[tuple[str, dict]]) -> list[dict]:
    rows: list[dict] = []
    for name, summary in summaries:
        profile = _profile(summary)
        dominant, dominant_ratio = _dominant_effect(profile)
        data_path = str(summary.get("data_path", ""))
        metrics = _world_metrics(data_path)
        row = {
            "name": name,
            "data_path": data_path,
            "profile": profile,
            "dominant": dominant,
            "dominant_ratio": dominant_ratio,
            "rekopplung": _second(summary.get("avg_mcm_rekopplung_quality")),
            "carry": _second(summary.get("avg_mcm_carry_quality")),
            "sensory": _second(summary.get("avg_mcm_sensory_coupling")),
            "episode_memory": int((summary.get("episode_memory_written") or [0, 0])[1]),
            "unique_symbols": int((summary.get("unique_symbols") or [0, 0])[1]),
            "world_metrics": metrics,
        }
        row["field_class"] = _classify(row)
        rows.append(row)
    return rows


def write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    by_class: dict[str, list[dict]] = {}
    for row in rows:
        by_class.setdefault(row["field_class"], []).append(row)

    lines = [
        "# Passive Feldklassen-Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose ordnet mehrere passive MINI_DIO-Welten nach ihrer Innenfeldwirkung.",
        "Sie ersetzt keine Einzelanalyse. Sie prüft, ob aus den bisherigen Mehrweltläufen größere Feldklassen sichtbar werden.",
        "",
        "Hierarchie der Prüfung:",
        "",
        "1. Grundfrage: Bildet MINI_DIO über verschiedene Welten hinweg wiedererkennbare Innenfeldklassen?",
        "2. Unterprüfung: Welche Rohwelt-Merkmale und Feldwerte begleiten diese Klassen?",
        "3. Folgeschritt: Prüfen, ob die Klassen bei neuen Welten stabil bleiben oder driften.",
        "",
        "## Feldklassen",
        "",
    ]

    for class_name in sorted(by_class):
        class_rows = by_class[class_name]
        lines.extend([f"### {class_name}", ""])
        avg_rekopplung = sum(row["rekopplung"] for row in class_rows) / max(1, len(class_rows))
        avg_carry = sum(row["carry"] for row in class_rows) / max(1, len(class_rows))
        avg_strain = sum(
            row["profile"].get("gespannt", 0) + row["profile"].get("kippend", 0) for row in class_rows
        ) / max(1, len(class_rows))
        lines.extend(
            [
                f"- Welten: `{len(class_rows)}`",
                f"- mittlere Rekopplung: `{avg_rekopplung:.6f}`",
                f"- mittlere Tragqualität: `{avg_carry:.6f}`",
                f"- mittlere Spannungs-/Kippwirkung: `{avg_strain:.1f}`",
                "",
            ]
        )
        for row in class_rows:
            metrics = row["world_metrics"]
            profile = row["profile"]
            strain = profile.get("gespannt", 0) + profile.get("kippend", 0)
            lines.extend(
                [
                    f"#### {row['name']}",
                    "",
                    f"- Datenwelt: `{row['data_path']}`",
                    f"- dominante Feldwirkung: `{row['dominant']}` (`{row['dominant_ratio']}`)",
                    f"- Rekopplung: `{row['rekopplung']:.6f}`",
                    f"- Tragqualität: `{row['carry']:.6f}`",
                    f"- Sinnes-MCM-Kopplung: `{row['sensory']:.6f}`",
                    f"- Episodenmemory: `{row['episode_memory']}`",
                    f"- Unique Syntax: `{row['unique_symbols']}`",
                    f"- gespannte + kippende Wirkung: `{strain}`",
                    f"- Rohwelt avg_abs_return: `{metrics['avg_abs_return']}`",
                    f"- Rohwelt max_abs_return: `{metrics['max_abs_return']}`",
                    f"- Rohwelt avg_range: `{metrics['avg_range']}`",
                    f"- Rohwelt drift: `{metrics['drift']}`",
                    f"- Richtungswechsel: `{int(metrics['direction_changes'])}`",
                    "",
                ]
            )

    lines.extend(
        [
            "## Befund",
            "",
            "Die bisherigen Welten zeigen keine einheitliche Wortbildung, aber wiedererkennbare Feldklassen.",
            "Das ist wichtig: Die Syntax bleibt weltbezogen, während die Innenfeldwirkung über mehrere Welten hinweg ähnliche Klassen bilden kann.",
            "",
            "Die ruhige Nähegruppe wird aktuell vor allem von 2025-Welten getragen. Sie zeigt hohe Rekopplung, hohe Tragqualität, starke stabile Dominanz und wenig gespannte/kippende Wirkung.",
            "",
            "Der Stress-Gegenpol zeigt das Gegenteil: geringere Rekopplung, geringere Tragqualität, mehr Kipp- und Spannungswirkung und mehr Episodenmemory. Das wirkt wie stärkere innere Verarbeitungslast.",
            "",
            "Wichtig bleibt: Diese Klassen sind passive Beobachtungsklassen. Sie sind keine Gates, keine Handlungsregeln und keine Strategie.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte eine neue Welt nicht nur einzeln bewertet werden, sondern direkt gegen diese Feldklassen gehalten werden. Entscheidend ist, ob MINI_DIO eine neue Welt in eine bestehende Feldklasse einordnet oder ob eine neue Klasse entsteht.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Erzeuge eine passive Feldklassen-Diagnose.")
    parser.add_argument(
        "--summary",
        action="append",
        nargs=2,
        metavar=("NAME", "PATH"),
        help="Name und Pfad zu einer research_chain_summary.json",
    )
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    summary_args = args.summary or [
        ("welt_2023_01", "debug/research_chain/research_chain_summary.json"),
        ("welt_2024_01", "debug/research_chain_2024_01/research_chain_summary.json"),
        ("welt_2025_core_01", "debug/research_chain_2025_core_01/research_chain_summary.json"),
        ("welt_2025_mid_shift_01", "debug/research_chain_2025_mid_shift_01/research_chain_summary.json"),
        ("welt_2025_late_shift_01", "debug/research_chain_2025_late_shift_01/research_chain_summary.json"),
        ("welt_2023_stress_01", "debug/research_chain_2023_stress_01/research_chain_summary.json"),
    ]
    summaries = []
    for name, path_text in summary_args:
        path = Path(path_text)
        if not path.is_absolute():
            path = ROOT / path
        summaries.append((name, _load(path)))

    rows = build_rows(summaries)
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    write_markdown(rows, out_path)
    print(json.dumps(rows, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
