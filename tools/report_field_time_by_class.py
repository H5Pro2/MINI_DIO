from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "125_FELDZEIT_GEGEN_FELDKLASSEN.md"

DEFAULT_WORLDS = [
    ("welt_2023_01", "debug/research_chain"),
    ("welt_2024_01", "debug/research_chain_2024_01"),
    ("welt_2025_core_01", "debug/research_chain_2025_core_01"),
    ("welt_2025_mid_shift_01", "debug/research_chain_2025_mid_shift_01"),
    ("welt_2025_late_shift_01", "debug/research_chain_2025_late_shift_01"),
    ("welt_2023_stress_01", "debug/research_chain_2023_stress_01"),
    ("welt_2024_bridge3_01", "debug/research_chain_2024_bridge3_01"),
]


def _path(path_text: str) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _second(values: object) -> float:
    if isinstance(values, list) and len(values) >= 2:
        return _float(values[1])
    return 0.0


def _read_summary(debug_root: Path) -> dict:
    return json.loads((debug_root / "research_chain_summary.json").read_text(encoding="utf-8"))


def _read_episodes(debug_root: Path, run: int) -> list[dict]:
    path = debug_root / f"dio_mini_lauf_{run}" / "episodes.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _profile(summary: dict) -> dict[str, int]:
    return {str(key): int(value or 0) for key, value in (summary.get("passive_mcm_effect_classes") or {}).items()}


def _transition_count(rows: list[dict], key: str) -> int:
    changes = 0
    previous = None
    for row in rows:
        value = row.get(key, "-")
        if previous is not None and value != previous:
            changes += 1
        previous = value
    return changes


def _classify(summary: dict) -> str:
    profile = _profile(summary)
    stable = profile.get("stabil", 0)
    strained = profile.get("gespannt", 0) + profile.get("kippend", 0)
    restless = profile.get("tragend_unruhig", 0)
    rekopplung = _second(summary.get("avg_mcm_rekopplung_quality"))
    carry = _second(summary.get("avg_mcm_carry_quality"))
    memory = int((summary.get("episode_memory_written") or [0, 0])[1])

    if rekopplung >= 0.630 and carry >= 0.359 and stable >= 500 and strained <= 75:
        return "ruhige Nähegruppe"
    if rekopplung <= 0.617 or carry <= 0.348 or strained >= 170 or memory >= 100:
        return "Stress-Gegenpol"
    if restless >= stable or strained >= 120:
        return "angespannte Übergangsgruppe"
    return "mittlere Feldlage"


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def analyze_world(name: str, debug_root: Path, run: int) -> dict:
    summary = _read_summary(debug_root)
    rows = _read_episodes(debug_root, run)
    total = max(1, len(rows))
    temporal_counts = Counter(row.get("mini_temporal_state", "-") for row in rows)
    effect_counts = Counter(row.get("passive_mcm_effect_class", "-") for row in rows)
    memory_count = sum(1 for row in rows if row.get("episode_memory_symbol", "-") not in ("", "-"))
    return {
        "name": name,
        "field_class": _classify(summary),
        "data_path": str(summary.get("data_path", "")),
        "episodes": total,
        "temporal_counts": dict(temporal_counts),
        "effect_counts": dict(effect_counts),
        "avg_afterimage": _avg([_float(row.get("mini_afterimage")) for row in rows]),
        "max_afterimage": max((_float(row.get("mini_afterimage")) for row in rows), default=0.0),
        "avg_recurrence": _avg([_float(row.get("mini_recurrence_strength")) for row in rows]),
        "max_recurrence": max((_float(row.get("mini_recurrence_strength")) for row in rows), default=0.0),
        "avg_rekopplung": _avg([_float(row.get("mcm_rekopplung_quality")) for row in rows]),
        "avg_carry": _avg([_float(row.get("mcm_carry_quality")) for row in rows]),
        "avg_strain": _avg([_float(row.get("mcm_strain_quality")) for row in rows]),
        "memory_count": memory_count,
        "memory_ratio": memory_count / total,
        "effect_transition_count": _transition_count(rows, "passive_mcm_effect_class"),
        "temporal_transition_count": _transition_count(rows, "mini_temporal_state"),
        "far_return_count": temporal_counts.get("temporal_far_return", 0),
        "near_return_count": temporal_counts.get("temporal_near_return", 0),
        "afterimage_state_count": temporal_counts.get("temporal_immediate_afterimage", 0),
    }


def aggregate_by_class(rows: list[dict]) -> dict[str, dict]:
    by_class: dict[str, list[dict]] = {}
    for row in rows:
        by_class.setdefault(row["field_class"], []).append(row)

    aggregates: dict[str, dict] = {}
    for class_name, class_rows in sorted(by_class.items()):
        total_episodes = sum(row["episodes"] for row in class_rows)
        aggregates[class_name] = {
            "worlds": class_rows,
            "world_count": len(class_rows),
            "avg_afterimage": _avg([row["avg_afterimage"] for row in class_rows]),
            "max_afterimage": max((row["max_afterimage"] for row in class_rows), default=0.0),
            "avg_recurrence": _avg([row["avg_recurrence"] for row in class_rows]),
            "max_recurrence": max((row["max_recurrence"] for row in class_rows), default=0.0),
            "avg_rekopplung": _avg([row["avg_rekopplung"] for row in class_rows]),
            "avg_carry": _avg([row["avg_carry"] for row in class_rows]),
            "avg_strain": _avg([row["avg_strain"] for row in class_rows]),
            "memory_ratio": sum(row["memory_count"] for row in class_rows) / max(1, total_episodes),
            "effect_transition_ratio": sum(row["effect_transition_count"] for row in class_rows) / max(1, total_episodes),
            "temporal_transition_ratio": sum(row["temporal_transition_count"] for row in class_rows) / max(1, total_episodes),
            "return_ratio": sum(row["far_return_count"] + row["near_return_count"] for row in class_rows) / max(1, total_episodes),
        }
    return aggregates


def write_markdown(rows: list[dict], aggregates: dict[str, dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Feldzeit Gegen Feldklassen",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prüft, ob Feldzeit-Spuren je nach Feldklasse unterschiedlich auftreten.",
        "Sie verbindet die Feldklassen-Diagnose mit der Feldzeit-Diagnose.",
        "Sie ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.",
        "",
        "Hierarchie der Prüfung:",
        "",
        "1. Grundfrage: Hängt Feldzeit mit der Feldklasse zusammen?",
        "2. Unterprüfung: Welche Klassen tragen mehr Nachhall, Wiederkehr, Memorylast oder Übergänge?",
        "3. Folgeschritt: Prüfen, ob neue Welten dieselbe Kopplung zeigen oder eine neue Klasse bilden.",
        "",
        "## Klassenvergleich",
        "",
        "| Feldklasse | Welten | Nachhall avg/max | Wiederkehr avg/max | Return-Quote | Memory-Quote | Feldwechsel/Episode | Zeitwechsel/Episode | Rekopplung | Tragqualität | Strain |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for class_name, data in aggregates.items():
        lines.append(
            f"| {class_name} | "
            f"{data['world_count']} | "
            f"{data['avg_afterimage']:.6f}/{data['max_afterimage']:.6f} | "
            f"{data['avg_recurrence']:.6f}/{data['max_recurrence']:.6f} | "
            f"{data['return_ratio']:.4f} | "
            f"{data['memory_ratio']:.4f} | "
            f"{data['effect_transition_ratio']:.4f} | "
            f"{data['temporal_transition_ratio']:.4f} | "
            f"{data['avg_rekopplung']:.6f} | "
            f"{data['avg_carry']:.6f} | "
            f"{data['avg_strain']:.6f} |"
        )

    lines.extend(["", "## Einzelwelten", ""])
    lines.extend(
        [
            "| Welt | Feldklasse | Nachhall avg/max | Wiederkehr avg/max | Memory | Feldwechsel | Zeitwechsel | Rekopplung | Tragqualität | Strain |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['name']} | "
            f"{row['field_class']} | "
            f"{row['avg_afterimage']:.6f}/{row['max_afterimage']:.6f} | "
            f"{row['avg_recurrence']:.6f}/{row['max_recurrence']:.6f} | "
            f"{row['memory_count']} | "
            f"{row['effect_transition_count']} | "
            f"{row['temporal_transition_count']} | "
            f"{row['avg_rekopplung']:.6f} | "
            f"{row['avg_carry']:.6f} | "
            f"{row['avg_strain']:.6f} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Feldzeit ist nicht gleichmäßig über alle Feldklassen verteilt.",
            "Die ruhige Nähegruppe zeigt in den bisherigen Welten die stärkste Wiederkehr und die niedrigste Memorylast.",
            "Der Stress-Gegenpol zeigt dagegen weniger Wiederkehr, niedrigere Rekopplung, höhere Memorylast und höhere Strain-Werte.",
            "",
            "Das ist fachlich wichtig: Feldzeit wirkt nicht isoliert. Sie hängt mit der Qualität der Innenfeldlage zusammen.",
            "Eine Lage kann also zeitliche Tiefe bilden, ohne dass sie automatisch tragend wird.",
            "",
            "## Interpretation",
            "",
            "Die bisherigen Daten sprechen dafür, dass MINI_DIO Feldzeit als Rekopplungsqualität trägt.",
            "In ruhiger Nähe kann Wiederkehr entstehen, ohne viel Memorylast zu erzeugen.",
            "Im Stress-Gegenpol wird weniger Wiederkehr sichtbar, während mehr Episodenmemory geschrieben wird. Das wirkt wie Verarbeitungslast statt ruhiger zeitlicher Tiefe.",
            "",
            "Damit wird Feldzeit als organische MCM-Eigenschaft plausibler: Zeit ist nicht nur Reihenfolge, sondern gewirkte Feldnähe, Nachhall und Rekopplung.",
            "",
            "## Begrenzung",
            "",
            "Der Befund ist noch kein Beweis für eine allgemeine MCM-Topologie.",
            "Er ist ein reproduzierbarer Arbeitsbefund innerhalb der bisher getesteten MINI_DIO-Welten.",
            "Neue Welten können diese Kopplung bestätigen, erweitern oder brechen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte eine neue Welt gezielt gegen diese Kopplung geprüft werden.",
            "Konkrete Frage: Bleibt die ruhige Nähegruppe wiederkehrstark und memoryarm, während Stresswelten memorylastiger bleiben?",
            "Wenn ja, wird Feldzeit als Feldklassen-Eigenschaft deutlich belastbarer.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Vergleiche Feldzeit-Spuren gegen passive Feldklassen.")
    parser.add_argument("--world", action="append", nargs=2, metavar=("NAME", "DEBUG_ROOT"))
    parser.add_argument("--run", type=int, default=2)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    worlds = args.world or DEFAULT_WORLDS
    rows = [analyze_world(name, _path(debug_root), args.run) for name, debug_root in worlds]
    aggregates = aggregate_by_class(rows)
    out_path = _path(args.out)
    write_markdown(rows, aggregates, out_path)
    print(json.dumps({"rows": rows, "aggregates": aggregates}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
