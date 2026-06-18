from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "136_KURZSEGMENT_WERTEBEREICHE.md"


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


def _profile(name: str, reading: str, debug_root: Path, run: int) -> dict:
    summary = _read_summary(debug_root)
    rows = _read_episodes(debug_root, run)
    total = max(1, len(rows))
    memory_count = sum(1 for row in rows if row.get("episode_memory_symbol", "-") not in ("", "-"))
    return {
        "name": name,
        "reading": reading,
        "episodes": total,
        "memory_count": memory_count,
        "memory_ratio": memory_count / total,
        "avg_strain": _avg([_float(row.get("mcm_strain_quality")) for row in rows]),
        "avg_rekopplung": _avg([_float(row.get("mcm_rekopplung_quality")) for row in rows]),
        "avg_carry": _avg([_float(row.get("mcm_carry_quality")) for row in rows]),
        "avg_afterimage": _avg([_float(row.get("mini_afterimage")) for row in rows]),
        "avg_recurrence": _avg([_float(row.get("mini_recurrence_strength")) for row in rows]),
        "effect_transition_ratio": _transition_count(rows, "passive_mcm_effect_class") / total,
        "top_symbol_overlap": float((summary.get("top_symbol_overlap") or {}).get("ratio", 0.0) or 0.0),
        "top_family_overlap": float((summary.get("top_family_overlap") or {}).get("ratio", 0.0) or 0.0),
    }


def _range(values: list[float]) -> str:
    if not values:
        return "-"
    return f"{min(values):.6f} - {max(values):.6f}"


def _avg_text(values: list[float]) -> str:
    if not values:
        return "-"
    return f"{_avg(values):.6f}"


def write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    by_reading: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_reading[row["reading"]].append(row)

    lines = [
        "# Kurzsegment-Wertebereiche",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Datei verdichtet die bisherigen Kurzsegment-Befunde.",
        "Sie ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.",
        "",
        "Die Wertebereiche sind Arbeitsbefunde aus den bisher geprüften Segmenten.",
        "Sie dürfen nicht als harte Schwellwerte gelesen werden.",
        "",
        "## Hierarchie Der Prüfung",
        "",
        "1. Grundfrage: Trennen sich lokale Last und lokale Ruhe im MCM-Feld reproduzierbar?",
        "2. Unterprüfung: Welche Wertebereiche zeigen die bisherigen Segmenttypen?",
        "3. Folgeschritt: Weitere Jahre/Welten gegen diese Arbeitsbereiche prüfen.",
        "",
        "## Einzelsegmente",
        "",
        "| Segment | Lesung | Memory | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['name']} | "
            f"{row['reading']} | "
            f"{row['memory_count']} ({row['memory_ratio']:.3f}) | "
            f"{row['avg_strain']:.6f} | "
            f"{row['avg_rekopplung']:.6f} | "
            f"{row['avg_carry']:.6f} | "
            f"{row['effect_transition_ratio']:.3f} | "
            f"{row['avg_recurrence']:.6f} | "
            f"{row['avg_afterimage']:.6f} |"
        )

    lines.extend(
        [
            "",
            "## Verdichtete Wertebereiche",
            "",
            "| Lesung | Segmente | Memory-Quote | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for reading, group in sorted(by_reading.items()):
        lines.append(
            f"| {reading} | "
            f"{len(group)} | "
            f"{_range([row['memory_ratio'] for row in group])} | "
            f"{_range([row['avg_strain'] for row in group])} | "
            f"{_range([row['avg_rekopplung'] for row in group])} | "
            f"{_range([row['avg_carry'] for row in group])} | "
            f"{_range([row['effect_transition_ratio'] for row in group])} | "
            f"{_range([row['avg_recurrence'] for row in group])} | "
            f"{_range([row['avg_afterimage'] for row in group])} |"
        )

    lines.extend(
        [
            "",
            "## Mittelwerte Nach Lesung",
            "",
            "| Lesung | Memory-Quote | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for reading, group in sorted(by_reading.items()):
        lines.append(
            f"| {reading} | "
            f"{_avg_text([row['memory_ratio'] for row in group])} | "
            f"{_avg_text([row['avg_strain'] for row in group])} | "
            f"{_avg_text([row['avg_rekopplung'] for row in group])} | "
            f"{_avg_text([row['avg_carry'] for row in group])} | "
            f"{_avg_text([row['effect_transition_ratio'] for row in group])} | "
            f"{_avg_text([row['avg_recurrence'] for row in group])} | "
            f"{_avg_text([row['avg_afterimage'] for row in group])} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die bisherigen Kurzsegmente trennen sich in drei Arbeitsformen:",
            "",
            "- `lastnah`: hohe Memorylast, hoher Strain, schwächere Rekopplung.",
            "- `ruhig_feldzeitnah`: niedrige Memorylast, niedriger Strain, stärkere Rekopplung und leichte Feldzeitspur.",
            "- `last_feldzeitnah`: Last bleibt dominant, aber erste Wiederkehr/Nachhall-Spuren treten hinzu.",
            "",
            "Damit wird die passive MCM-Lesung präziser:",
            "",
            "```text",
            "Lokale Last ist nicht einfach Bewegung.",
            "Lokale Ruhe ist nicht einfach Stillstand.",
            "Feldzeit ist nicht automatisch Ruhe.",
            "```",
            "",
            "## Interpretation",
            "",
            "Die bisherige Trennung spricht dafür, dass MINI_DIO lokale Feldreaktionen ausbildet, die nicht direkt aus dem Dateinamen oder einer Einzelmetrik folgen.",
            "Die Lastseite zeigt eine belastete Innenfeldreaktion.",
            "Die Ruheseite zeigt eine tragfähigere Innenfeldreaktion.",
            "Feldzeit kann in beiden Richtungen eingebettet sein.",
            "",
            "Das stützt die Arbeitsthese, dass das MCM-Feld Gegenpole nicht als Modul braucht.",
            "Stress, Ruhe, Entlastung und Last werden als Feldwirkung lesbar.",
            "",
            "## Begrenzung",
            "",
            "Die Datenbasis ist noch klein.",
            "Die Wertebereiche sind keine Schwellwerte.",
            "Neue Segmente können die Bereiche bestätigen, verschieben oder neue Mischformen zeigen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte ein weiteres unabhängiges Jahr getestet werden.",
            "Ziel: Prüfen, ob `lastnah`, `ruhig_feldzeitnah` und `last_feldzeitnah` auch außerhalb der bisher verwendeten Welten entstehen.",
            "Wenn ja, wird die Kurzsegment-Lesung als passive Diagnoseebene deutlich belastbarer.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verdichtet Kurzsegment-Wertebereiche.")
    parser.add_argument("--segment", action="append", nargs=3, metavar=("NAME", "READING", "DEBUG_ROOT"), required=True)
    parser.add_argument("--run", type=int, default=2)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    rows = [_profile(name, reading, _path(debug_root), args.run) for name, reading, debug_root in args.segment]
    out_path = _path(args.out)
    write_markdown(rows, out_path)
    print(json.dumps({"segments": rows, "out": str(out_path)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
