from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "124_FELDZEIT_DIAGNOSE.md"

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


def _float(row: dict, key: str) -> float:
    try:
        return float(row.get(key) or 0.0)
    except Exception:
        return 0.0


def _read_summary(debug_root: Path) -> dict:
    path = debug_root / "research_chain_summary.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _read_episodes(debug_root: Path, run: int) -> list[dict]:
    path = debug_root / f"dio_mini_lauf_{run}" / "episodes.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _transition_count(rows: list[dict], key: str) -> int:
    changes = 0
    previous = None
    for row in rows:
        value = row.get(key, "-")
        if previous is not None and value != previous:
            changes += 1
        previous = value
    return changes


def _dominant(counter: Counter) -> tuple[str, int, float]:
    total = max(1, sum(counter.values()))
    if not counter:
        return "-", 0, 0.0
    key, count = counter.most_common(1)[0]
    return str(key), int(count), count / total


def _segment_metrics(rows: list[dict], start: int, end: int, index: int) -> dict:
    segment = rows[start:end]
    total = max(1, len(segment))
    temporal_counts = Counter(row.get("mini_temporal_state", "-") for row in segment)
    effect_counts = Counter(row.get("passive_mcm_effect_class", "-") for row in segment)
    symbol_counts = Counter(row.get("symbol_family", "-") for row in segment)
    dominant_temporal, temporal_count, temporal_ratio = _dominant(temporal_counts)
    dominant_effect, effect_count, effect_ratio = _dominant(effect_counts)
    dominant_symbol, symbol_count, symbol_ratio = _dominant(symbol_counts)
    memory_count = sum(1 for row in segment if row.get("episode_memory_symbol", "-") not in ("", "-"))

    return {
        "segment": index,
        "start": start,
        "end": end,
        "dominant_temporal": dominant_temporal,
        "dominant_temporal_count": temporal_count,
        "dominant_temporal_ratio": temporal_ratio,
        "dominant_effect": dominant_effect,
        "dominant_effect_count": effect_count,
        "dominant_effect_ratio": effect_ratio,
        "dominant_symbol": dominant_symbol,
        "dominant_symbol_count": symbol_count,
        "dominant_symbol_ratio": symbol_ratio,
        "avg_afterimage": sum(_float(row, "mini_afterimage") for row in segment) / total,
        "max_afterimage": max((_float(row, "mini_afterimage") for row in segment), default=0.0),
        "avg_recurrence": sum(_float(row, "mini_recurrence_strength") for row in segment) / total,
        "max_recurrence": max((_float(row, "mini_recurrence_strength") for row in segment), default=0.0),
        "avg_rekopplung": sum(_float(row, "mcm_rekopplung_quality") for row in segment) / total,
        "avg_carry": sum(_float(row, "mcm_carry_quality") for row in segment) / total,
        "avg_strain": sum(_float(row, "mcm_strain_quality") for row in segment) / total,
        "memory_count": memory_count,
        "memory_ratio": memory_count / total,
        "effect_transition_count": _transition_count(segment, "passive_mcm_effect_class"),
        "temporal_transition_count": _transition_count(segment, "mini_temporal_state"),
    }


def analyze_world(name: str, debug_root: Path, segments: int, run: int) -> dict:
    summary = _read_summary(debug_root)
    rows = _read_episodes(debug_root, run)
    total = max(1, len(rows))
    temporal_counts = Counter(row.get("mini_temporal_state", "-") for row in rows)
    effect_counts = Counter(row.get("passive_mcm_effect_class", "-") for row in rows)
    segment_size = max(1, total // segments)
    segment_rows = []
    for index in range(segments):
        start = index * segment_size
        end = min(start + segment_size, total)
        if index == segments - 1:
            end = total
        if start >= total:
            break
        segment_rows.append(_segment_metrics(rows, start, end, index + 1))

    afterimage_rank = sorted(segment_rows, key=lambda row: row["max_afterimage"], reverse=True)[:3]
    recurrence_rank = sorted(segment_rows, key=lambda row: row["avg_recurrence"], reverse=True)[:3]
    memory_rank = sorted(segment_rows, key=lambda row: row["memory_ratio"], reverse=True)[:3]

    return {
        "name": name,
        "debug_root": str(debug_root.relative_to(ROOT)),
        "data_path": str(summary.get("data_path", "")),
        "episodes": total,
        "temporal_counts": dict(temporal_counts),
        "effect_counts": dict(effect_counts),
        "avg_afterimage": sum(_float(row, "mini_afterimage") for row in rows) / total,
        "max_afterimage": max((_float(row, "mini_afterimage") for row in rows), default=0.0),
        "avg_recurrence": sum(_float(row, "mini_recurrence_strength") for row in rows) / total,
        "max_recurrence": max((_float(row, "mini_recurrence_strength") for row in rows), default=0.0),
        "avg_rekopplung": sum(_float(row, "mcm_rekopplung_quality") for row in rows) / total,
        "avg_carry": sum(_float(row, "mcm_carry_quality") for row in rows) / total,
        "avg_strain": sum(_float(row, "mcm_strain_quality") for row in rows) / total,
        "episode_memory_count": sum(1 for row in rows if row.get("episode_memory_symbol", "-") not in ("", "-")),
        "effect_transition_count": _transition_count(rows, "passive_mcm_effect_class"),
        "temporal_transition_count": _transition_count(rows, "mini_temporal_state"),
        "segments": segment_rows,
        "afterimage_rank": afterimage_rank,
        "recurrence_rank": recurrence_rank,
        "memory_rank": memory_rank,
    }


def _format_counter(counter: dict) -> str:
    if not counter:
        return "`-`"
    parts = [f"`{key}` `{value}`" for key, value in sorted(counter.items(), key=lambda item: item[1], reverse=True)]
    return ", ".join(parts)


def write_markdown(results: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Feldzeit-Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prüft passiv, ob MINI_DIO zeitliche Tiefe bereits aus dem Feldverhalten bildet.",
        "Es geht nicht um eine externe Uhr und nicht um eine neue Runtime-Regel.",
        "",
        "Hierarchie der Prüfung:",
        "",
        "1. Grundfrage: Entsteht im MCM-Feld eine eigene zeitliche Tiefe?",
        "2. Unterprüfung: Wo erscheinen Nachhall, Wiederkehr, Drift, Verblassen und Rekopplung über Zeit?",
        "3. Folgeschritt: Prüfen, ob diese Feldzeit bei neuen Welten stabil bleibt oder neue Zeittöne bildet.",
        "",
        "## Ergebnisübersicht",
        "",
        "| Welt | Episoden | Nachhall avg/max | Wiederkehr avg/max | Rekopplung | Tragqualität | Strain | Episodenmemory | Feldübergänge | Zeitübergänge |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for result in results:
        lines.append(
            f"| {result['name']} | "
            f"{result['episodes']} | "
            f"{result['avg_afterimage']:.6f}/{result['max_afterimage']:.6f} | "
            f"{result['avg_recurrence']:.6f}/{result['max_recurrence']:.6f} | "
            f"{result['avg_rekopplung']:.6f} | "
            f"{result['avg_carry']:.6f} | "
            f"{result['avg_strain']:.6f} | "
            f"{result['episode_memory_count']} | "
            f"{result['effect_transition_count']} | "
            f"{result['temporal_transition_count']} |"
        )

    lines.extend(["", "## Weltprofile", ""])

    for result in results:
        lines.extend(
            [
                f"### {result['name']}",
                "",
                f"- Datenwelt: `{result['data_path']}`",
                f"- Debug: `{result['debug_root']}`",
                f"- Zeitstatus: {_format_counter(result['temporal_counts'])}",
                f"- Feldwirkung: {_format_counter(result['effect_counts'])}",
                "",
                "Stärkste Nachhallabschnitte:",
                "",
            ]
        )
        for segment in result["afterimage_rank"]:
            lines.append(
                f"- Abschnitt `{segment['segment']}` (`{segment['start']}`-`{segment['end']}`): "
                f"max_afterimage `{segment['max_afterimage']:.6f}`, "
                f"avg_recurrence `{segment['avg_recurrence']:.6f}`, "
                f"dominante Wirkung `{segment['dominant_effect']}`, "
                f"Memory `{segment['memory_count']}`"
            )
        lines.extend(["", "Stärkste Wiederkehrabschnitte:", ""])
        for segment in result["recurrence_rank"]:
            lines.append(
                f"- Abschnitt `{segment['segment']}` (`{segment['start']}`-`{segment['end']}`): "
                f"avg_recurrence `{segment['avg_recurrence']:.6f}`, "
                f"max_recurrence `{segment['max_recurrence']:.6f}`, "
                f"dominante Zeitlage `{segment['dominant_temporal']}`, "
                f"dominante Formfamilie `{segment['dominant_symbol']}` (`{segment['dominant_symbol_ratio']:.3f}`)"
            )
        lines.extend(["", "Stärkste Memoryabschnitte:", ""])
        for segment in result["memory_rank"]:
            lines.append(
                f"- Abschnitt `{segment['segment']}` (`{segment['start']}`-`{segment['end']}`): "
                f"memory_ratio `{segment['memory_ratio']:.3f}`, "
                f"Rekopplung `{segment['avg_rekopplung']:.6f}`, "
                f"Tragqualität `{segment['avg_carry']:.6f}`, "
                f"Strain `{segment['avg_strain']:.6f}`"
            )
        lines.append("")

    lines.extend(
        [
            "## Befund",
            "",
            "Feldzeit ist in den bisherigen Daten nicht als starke externe Uhr sichtbar.",
            "Sie erscheint eher als innere Zeitspur: Wiederkehr einzelner Formfamilien, kurze Nachhallspitzen, wechselnde Rekopplung und unterschiedlich dichte Episodenmemory.",
            "",
            "Wichtig ist die Trennung:",
            "",
            "- `mini_afterimage` zeigt Restwirkung einer vorherigen Lage.",
            "- `mini_recurrence_strength` zeigt Wiederkehr oder erneute Nähe.",
            "- `episode_memory_count` zeigt, dass bestimmte Abschnitte mehr innere Verarbeitung tragen.",
            "- `effect_transition_count` zeigt, wie oft die Feldwirkung wechselt.",
            "- `temporal_transition_count` zeigt, ob die Zeitlage selbst wechselt oder weitgehend gleich bleibt.",
            "",
            "Damit wirkt Feldzeit aktuell nicht wie programmierte Mehrdimensionalzeit, sondern wie eine passive Tiefe des Feldes: etwas war da, wirkt nach, kehrt wieder oder verliert seine Nähe.",
            "",
            "## Interpretation",
            "",
            "Das passt zur aktuellen Forschungsrichtung: MINI_DIO muss Zeit nicht als harte Mechanik bekommen, solange das Feld selbst zeitliche Qualitäten lesbar bildet.",
            "Die Diagnose darf aber nicht überdehnt werden. Die meisten Episoden bleiben `temporal_first_contact`; Wiederkehr und Nachhall sind noch dünne, aber messbare Spuren.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte die Feldzeit gegen die bestehenden Feldklassen gehalten werden.",
            "Konkrete Unterprüfung: Entsteht mehr Nachhall/Wiederkehr in der ruhigen Nähegruppe oder im Stress-Gegenpol?",
            "Erst danach entscheiden wir, ob eine eigene Feldzeit-Karte notwendig ist oder ob die vorhandene Topologie-Karte reicht.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Erzeuge eine passive Feldzeit-Diagnose.")
    parser.add_argument("--world", action="append", nargs=2, metavar=("NAME", "DEBUG_ROOT"))
    parser.add_argument("--segments", type=int, default=10)
    parser.add_argument("--run", type=int, default=2)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    worlds = args.world or DEFAULT_WORLDS
    results = [analyze_world(name, _path(debug_root), args.segments, args.run) for name, debug_root in worlds]
    out_path = _path(args.out)
    write_markdown(results, out_path)
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
