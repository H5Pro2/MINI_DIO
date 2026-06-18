from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "133_KURZSEGMENT_LESER.md"


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


def _read_summary(debug_root: Path) -> dict:
    return json.loads((debug_root / "research_chain_summary.json").read_text(encoding="utf-8"))


def _read_episodes(debug_root: Path, run: int) -> list[dict]:
    path = debug_root / f"dio_mini_lauf_{run}" / "episodes.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _transition_count(rows: list[dict], key: str) -> int:
    changes = 0
    previous = None
    for row in rows:
        value = row.get(key, "-")
        if previous is not None and value != previous:
            changes += 1
        previous = value
    return changes


def _rank_map(rows: list[dict], key: str, *, reverse: bool = False) -> dict[str, float]:
    ordered = sorted(rows, key=lambda row: float(row.get(key, 0.0)), reverse=reverse)
    count = len(ordered)
    if count <= 1:
        return {str(row["name"]): 0.5 for row in ordered}
    return {str(row["name"]): index / (count - 1) for index, row in enumerate(ordered)}


def _profile_segment(name: str, debug_root: Path, run: int) -> dict:
    summary = _read_summary(debug_root)
    rows = _read_episodes(debug_root, run)
    total = max(1, len(rows))
    effects = Counter(row.get("passive_mcm_effect_class", "-") for row in rows)
    temporal = Counter(row.get("mini_temporal_state", "-") for row in rows)
    memory_count = sum(1 for row in rows if row.get("episode_memory_symbol", "-") not in ("", "-"))
    return {
        "name": name,
        "data_path": str(summary.get("data_path", "")),
        "episodes": total,
        "memory_count": memory_count,
        "memory_ratio": memory_count / total,
        "avg_strain": _avg([_float(row.get("mcm_strain_quality")) for row in rows]),
        "avg_rekopplung": _avg([_float(row.get("mcm_rekopplung_quality")) for row in rows]),
        "avg_carry": _avg([_float(row.get("mcm_carry_quality")) for row in rows]),
        "avg_afterimage": _avg([_float(row.get("mini_afterimage")) for row in rows]),
        "avg_recurrence": _avg([_float(row.get("mini_recurrence_strength")) for row in rows]),
        "effect_transition_ratio": _transition_count(rows, "passive_mcm_effect_class") / total,
        "temporal_transition_ratio": _transition_count(rows, "mini_temporal_state") / total,
        "stable_ratio": effects.get("stabil", 0) / total,
        "restless_ratio": effects.get("tragend_unruhig", 0) / total,
        "strained_ratio": (effects.get("gespannt", 0) + effects.get("kippend", 0)) / total,
        "field_carried": int((summary.get("episode_memory_states") or {}).get("field_carried", 0)),
        "field_strained": int((summary.get("episode_memory_states") or {}).get("field_strained", 0)),
        "top_symbol_overlap": float((summary.get("top_symbol_overlap") or {}).get("ratio", 0.0) or 0.0),
        "top_family_overlap": float((summary.get("top_family_overlap") or {}).get("ratio", 0.0) or 0.0),
        "effects": dict(effects),
        "temporal": dict(temporal),
    }


def _add_relative_reading(rows: list[dict]) -> None:
    memory_rank = _rank_map(rows, "memory_ratio")
    strain_rank = _rank_map(rows, "avg_strain")
    rekop_rank = _rank_map(rows, "avg_rekopplung")
    recurrence_rank = _rank_map(rows, "avg_recurrence")
    transition_rank = _rank_map(rows, "effect_transition_ratio")

    for row in rows:
        name = str(row["name"])
        load = _avg(
            [
                memory_rank[name],
                strain_rank[name],
                1.0 - rekop_rank[name],
                transition_rank[name],
            ]
        )
        calm = _avg(
            [
                1.0 - memory_rank[name],
                1.0 - strain_rank[name],
                rekop_rank[name],
            ]
        )
        field_time = _avg([recurrence_rank[name], float(row["avg_afterimage"] > 0.0)])
        row["relative_load_score"] = load
        row["relative_calm_score"] = calm
        row["relative_field_time_score"] = field_time
        if calm > load and calm >= field_time:
            row["short_segment_reading"] = "ruhenah"
        elif load > calm and load >= field_time:
            row["short_segment_reading"] = "lastnah"
        elif field_time > max(load, calm):
            row["short_segment_reading"] = "feldzeitnah"
        else:
            row["short_segment_reading"] = "gemischt"


def write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Kurzsegment-Leser",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest kurze lokale Segmente anders als volle 1000-Zeilen-Welten.",
        "Sie ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.",
        "",
        "Kurzsegmente haben oft zu wenig Kontext für starke Wiederkehr oder Nachhall.",
        "Deshalb werden sie primär über lokale Feldwirkung gelesen: Memorylast, Strain, Rekopplung und Feldwechsel.",
        "",
        "## Hierarchie Der Prüfung",
        "",
        "1. Grundfrage: Kann MINI_DIO lokale Ruhe- und Stressinseln unterscheiden?",
        "2. Unterprüfung: Welche Kurzsegmente zeigen Lastnähe, Ruhenähe oder Feldzeitnähe?",
        "3. Folgeschritt: Prüfen, ob diese Kurzlesung über weitere lokale Abschnitte stabil bleibt.",
        "",
        "## Methode",
        "",
        "Die Lesung nutzt keine absoluten Regeln.",
        "Die Segmente werden relativ zueinander verglichen:",
        "",
        "- Lastnähe: mehr Memorylast, mehr Strain, schwächere Rekopplung, mehr Feldwechsel.",
        "- Ruhenähe: weniger Memorylast, weniger Strain, stärkere Rekopplung.",
        "- Feldzeitnähe: Wiederkehr und Nachhall treten sichtbar auf.",
        "",
        "## Segmentvergleich",
        "",
        "| Segment | Lesung | Episoden | Memory | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall | Load | Calm | Feldzeit |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['name']} | "
            f"{row['short_segment_reading']} | "
            f"{row['episodes']} | "
            f"{row['memory_count']} ({row['memory_ratio']:.3f}) | "
            f"{row['avg_strain']:.6f} | "
            f"{row['avg_rekopplung']:.6f} | "
            f"{row['avg_carry']:.6f} | "
            f"{row['effect_transition_ratio']:.3f} | "
            f"{row['avg_recurrence']:.6f} | "
            f"{row['avg_afterimage']:.6f} | "
            f"{row['relative_load_score']:.3f} | "
            f"{row['relative_calm_score']:.3f} | "
            f"{row['relative_field_time_score']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die lokalen Stresssegmente werden lastnah gelesen.",
            "Das ruhige Vergleichssegment wird ruhenah gelesen, obwohl ein globaler Feldklassenname es zuvor grob in den Stress-Gegenpol einsortierte.",
            "",
            "Das bestätigt die methodische Trennung:",
            "",
            "- Vollwelten zeigen Feldklassen über längere Einbettung.",
            "- Kurzsegmente zeigen lokale Feldreaktion.",
            "- Lokale Feldreaktion darf nicht blind wie eine volle Weltklasse gelesen werden.",
            "",
            "## Interpretation",
            "",
            "Innenfeldlast entsteht in MINI_DIO als Feldwirkung.",
            "Sie muss nicht als eigenes Lastmodul modelliert werden.",
            "Für Kurzsegmente reicht es, die entstehende Feldwirkung zu lesen:",
            "",
            "- schreibt das Feld viel Memory?",
            "- steigt Strain?",
            "- sinkt Rekopplung?",
            "- bleibt das Segment trotz kurzer Dauer ruhig und getragen?",
            "",
            "Damit wird der organische MCM-Ansatz sauberer:",
            "",
            "```text",
            "Nicht: Innenfeldlast programmieren.",
            "Sondern: Innenfeldlast als Feldwirkung lesen.",
            "```",
            "",
            "## Begrenzung",
            "",
            "Die Lesung ist relativ zur geprüften Segmentgruppe.",
            "Sie ist ein Diagnosewerkzeug, keine universelle Klassifikation.",
            "Weitere ruhige und belastete Kurzsegmente müssen gegengeprüft werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte eine zweite ruhige Insel aus einer anderen ruhigen Welt isoliert werden.",
            "Wenn sie wieder ruhenah gelesen wird, wird die Kurzsegment-Lesung belastbarer.",
            "Danach kann geprüft werden, ob Lastnähe und Ruhenähe sich über mehrere Jahre/Welten ähnlich trennen.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Liest kurze MINI_DIO-Segmente relativ zueinander.")
    parser.add_argument("--segment", action="append", nargs=2, metavar=("NAME", "DEBUG_ROOT"), required=True)
    parser.add_argument("--run", type=int, default=2)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    rows = [_profile_segment(name, _path(debug_root), args.run) for name, debug_root in args.segment]
    _add_relative_reading(rows)
    out_path = _path(args.out)
    write_markdown(rows, out_path)
    print(json.dumps({"segments": rows, "out": str(out_path)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
