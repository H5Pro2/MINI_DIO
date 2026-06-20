from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DEBUG_ROOT = ROOT / "debug" / "_codex_sensesplit_worldcheck"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "402_LOKALE_SINNESACHSEN_EPISODENKARTE.csv"
DEFAULT_MD = ROOT / "docs" / "befunde" / "402_LOKALE_SINNESACHSEN_EPISODENKARTE.md"

AXIS_FIELDS = {
    "sehen_fokus": "perception_visual_focus_tendency",
    "sehen_abstand": "perception_visual_distance_tendency",
    "hoeren_hin": "perception_auditory_listen_tendency",
    "hoeren_leise": "perception_auditory_softening_tendency",
    "fuehlen_abstand": "perception_felt_distance_tendency",
    "feldinput": "rezeptor_field_intake_pressure",
}

SUMMARY_FIELDS = [
    "mcm_rekopplung_quality",
    "mcm_strain_quality",
    "mcm_carry_quality",
    "rezeptor_field_intake_pressure",
    "perception_adaptation_potential",
    "perception_visual_focus_tendency",
    "perception_visual_distance_tendency",
    "perception_auditory_listen_tendency",
    "perception_auditory_softening_tendency",
    "perception_felt_distance_tendency",
]


def _float(value: object) -> float:
    try:
        value = float(value or 0.0)
    except Exception:
        value = 0.0
    if value != value:
        return 0.0
    return value


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _stdev(values: list[float], mean: float) -> float:
    if len(values) < 2:
        return 0.0
    return math.sqrt(sum((item - mean) ** 2 for item in values) / (len(values) - 1))


def _axis_stats(rows: list[dict[str, str]]) -> dict[str, tuple[float, float]]:
    stats: dict[str, tuple[float, float]] = {}
    for key, field in AXIS_FIELDS.items():
        values = [_float(row.get(field)) for row in rows]
        mean = _mean(values)
        stats[key] = (mean, max(1e-9, _stdev(values, mean)))
    return stats


def _classify_axis(row: dict[str, str], stats: dict[str, tuple[float, float]]) -> tuple[str, float]:
    scores: dict[str, float] = {}
    for key, field in AXIS_FIELDS.items():
        mean, stdev = stats[key]
        scores[key] = (_float(row.get(field)) - mean) / stdev
    axis, score = max(scores.items(), key=lambda item: item[1])
    if score < 0.35:
        return "ausgeglichen", score
    return axis, score


def _iter_episode_paths(debug_root: Path) -> list[Path]:
    if debug_root.is_file():
        return [debug_root]
    paths = sorted(debug_root.glob("*/dio_mini_lauf_1/episodes.csv"))
    if not paths:
        paths = sorted(debug_root.glob("**/episodes.csv"))
    return paths


def build_axis_map(debug_root: Path) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for path in _iter_episode_paths(debug_root):
        rows = _read_rows(path)
        if not rows:
            continue
        world = rows[0].get("passive_world_label") or path.parents[1].name
        stats = _axis_stats(rows)
        grouped: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            axis, score = _classify_axis(row, stats)
            row = dict(row)
            row["_local_axis"] = axis
            row["_local_axis_z"] = f"{score:.6f}"
            effect_state = row.get("passive_inner_effect_awareness_state") or row.get("passive_mcm_effect_class") or "-"
            preview = row.get("mcm_field_episode_preview_symbol") or "-"
            grouped[(axis, effect_state, preview)].append(row)

        total = max(1, len(rows))
        for (axis, effect_state, preview), items in grouped.items():
            result: dict[str, object] = {
                "world": world,
                "axis": axis,
                "inner_effect_state": effect_state,
                "mcm_preview_symbol": preview,
                "count": len(items),
                "ratio": len(items) / total,
                "avg_axis_z": _mean([_float(item.get("_local_axis_z")) for item in items]),
            }
            for field in SUMMARY_FIELDS:
                result[f"avg_{field}"] = _mean([_float(item.get(field)) for item in items])
            output.append(result)
    output.sort(key=lambda row: (str(row["world"]), -float(row["count"]), str(row["axis"])))
    return output


def _fmt(value: object, digits: int = 4) -> str:
    if isinstance(value, int):
        return str(value)
    try:
        return f"{float(value):.{digits}f}"
    except Exception:
        return str(value)


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "axis",
        "inner_effect_state",
        "mcm_preview_symbol",
        "count",
        "ratio",
        "avg_axis_z",
        *[f"avg_{field}" for field in SUMMARY_FIELDS],
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, object]], path: Path, source_root: Path, csv_path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_world: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_world[str(row["world"])].append(row)

    lines = [
        "# Lokale Sinnesachsen-Episodenkarte",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        "Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?",
        "",
        "Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.",
        "",
        "## Quelle",
        "",
        f"- Debug-Wurzel: `{source_root.relative_to(ROOT) if source_root.is_relative_to(ROOT) else source_root}`",
        f"- CSV: `{csv_path.relative_to(ROOT) if csv_path.is_relative_to(ROOT) else csv_path}`",
        "",
        "## Methode",
        "",
        "Pro Welt werden die Achsen weltrelativ normalisiert. Eine Achse gilt lokal dominant, wenn sie in dieser Welt deutlich ueber ihrem eigenen Durchschnitt liegt.",
        "",
        "Gelesene Achsen:",
        "",
        "- `sehen_fokus`",
        "- `sehen_abstand`",
        "- `hoeren_hin`",
        "- `hoeren_leise`",
        "- `fuehlen_abstand`",
        "- `feldinput`",
        "- `ausgeglichen`",
        "",
        "## Top-Befunde je Welt",
        "",
    ]

    for world, world_rows in sorted(by_world.items()):
        lines.extend([f"### {world}", ""])
        lines.append("| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |")
        lines.append("|---|---|---|---:|---:|---:|---:|---:|")
        for row in sorted(world_rows, key=lambda item: -float(item["count"]))[:10]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(row["axis"]),
                        str(row["inner_effect_state"]),
                        str(row["mcm_preview_symbol"]),
                        _fmt(row["ratio"]),
                        _fmt(row["count"], 0),
                        _fmt(row["avg_mcm_rekopplung_quality"]),
                        _fmt(row["avg_mcm_strain_quality"]),
                        _fmt(row["avg_rezeptor_field_intake_pressure"]),
                    ]
                )
                + " |"
            )
        lines.append("")

    lines.extend(
        [
            "## Erste Lesart",
            "",
            "Die Weltmittelwerte waren eng. Lokal entstehen aber unterscheidbare Achsenlagen. Entscheidend ist nicht, dass eine Welt insgesamt lauter oder visueller ist, sondern welche Achse in konkreten Episoden hervorsticht und ob diese Episode rekoppelt oder belastet.",
            "",
            "Damit verschiebt sich die naechste Pruefung von globaler Regulation zu episodischer Kopplung:",
            "",
            "```text",
            "Welche Achsenlage wurde vom Feld getragen?",
            "Welche Achsenlage erzeugte Strain?",
            "Welche Achsenlage blieb nur offen oder ausgeglichen?",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird aus dieser Karte eine kleine Rekopplungsanalyse abgeleitet: Welche Achsenlage hat pro Welt die beste Rekopplung bei niedriger Belastung?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", default=str(DEFAULT_DEBUG_ROOT))
    parser.add_argument("--out-csv", default=str(DEFAULT_CSV))
    parser.add_argument("--out-md", default=str(DEFAULT_MD))
    args = parser.parse_args()

    debug_root = _resolve(args.debug_root)
    out_csv = _resolve(args.out_csv)
    out_md = _resolve(args.out_md)

    rows = build_axis_map(debug_root)
    if not rows:
        raise SystemExit(f"Keine episodes.csv unter {debug_root}")
    write_csv(rows, out_csv)
    write_markdown(rows, out_md, debug_root, out_csv)
    print(f"wrote {out_csv}")
    print(f"wrote {out_md}")
    print(f"rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
