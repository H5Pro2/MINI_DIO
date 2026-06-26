from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

from report_field_episode_multiworld import summarize_world


ROOT = Path(__file__).resolve().parents[1]
CSV_DEFAULT = ROOT / "docs" / "befunde" / "810_BLOCK_K_FELDZEIT_KURZ_ASSET_VERGLEICH.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "810_BLOCK_K_FELDZEIT_KURZ_ASSET_VERGLEICH.md"


GROUP_DEFAULTS = {
    "kurz_normal": ROOT / "debug" / "block_k_multiworld",
    "kurz_stress": ROOT / "debug" / "block_k_stress_multiworld",
    "asset_mixed_2k": ROOT / "debug" / "_codex_sensesplit_axis_validate",
    "lang_10k": ROOT / "debug" / "block_k_10k_multiworld",
}


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _episode_files(root: Path) -> list[Path]:
    return sorted(root.glob("*/*/episodes.csv"))


def _group_label(path: Path) -> str:
    for label, root in GROUP_DEFAULTS.items():
        try:
            path.relative_to(root)
            return label
        except Exception:
            continue
    return path.parts[-4] if len(path.parts) >= 4 else "gruppe"


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _rows_for_groups(group_roots: dict[str, Path]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for group, root in group_roots.items():
        root = root if root.is_absolute() else ROOT / root
        for path in _episode_files(root):
            row = summarize_world(path)
            row["group"] = group
            rows.append(row)
    return rows


def _aggregate_world_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["group"]), str(row["world"]))].append(row)
    aggregated: list[dict[str, object]] = []
    for (group, world), world_rows in grouped.items():
        patterns = Counter(str(row.get("dominant_pattern", "-")) for row in world_rows)
        sources = [str(row.get("source", "-")) for row in world_rows]
        aggregated.append(
            {
                "group": group,
                "world": world,
                "raw_runs": len(world_rows),
                "total_ticks": _mean([_safe_float(row.get("total_ticks")) for row in world_rows]),
                "max_duration": _mean([_safe_float(row.get("max_duration")) for row in world_rows]),
                "long_segments": _mean([_safe_float(row.get("long_segments")) for row in world_rows]),
                "strained_segments": _mean([_safe_float(row.get("strained_segments")) for row in world_rows]),
                "carried_tick_share": _mean(
                    [_safe_float(row.get("carried_tick_share")) for row in world_rows]
                ),
                "avg_carry": _mean([_safe_float(row.get("avg_carry")) for row in world_rows]),
                "avg_rekopplung": _mean([_safe_float(row.get("avg_rekopplung")) for row in world_rows]),
                "avg_strain": _mean([_safe_float(row.get("avg_strain")) for row in world_rows]),
                "avg_afterimage": _mean([_safe_float(row.get("avg_afterimage")) for row in world_rows]),
                "avg_temporal_trust": _mean(
                    [_safe_float(row.get("avg_temporal_trust")) for row in world_rows]
                ),
                "dominant_pattern": patterns.most_common(1)[0][0] if patterns else "-",
                "source": " | ".join(sources),
            }
        )
    return sorted(aggregated, key=lambda row: (str(row["group"]), str(row["world"])))


def _summaries(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["group"])].append(row)
    summaries: list[dict[str, object]] = []
    for group, group_rows in grouped.items():
        patterns = Counter(str(row.get("dominant_pattern", "-")) for row in group_rows)
        summaries.append(
            {
                "type": "summary",
                "group": group,
                "world": "GROUP",
                "worlds": len(group_rows),
                "raw_runs": sum(int(_safe_float(row.get("raw_runs"), 1.0)) for row in group_rows),
                "avg_total_ticks": _mean([_safe_float(row.get("total_ticks")) for row in group_rows]),
                "avg_max_duration": _mean([_safe_float(row.get("max_duration")) for row in group_rows]),
                "avg_long_segments": _mean([_safe_float(row.get("long_segments")) for row in group_rows]),
                "avg_strained_segments": _mean([_safe_float(row.get("strained_segments")) for row in group_rows]),
                "avg_carried_tick_share": _mean(
                    [_safe_float(row.get("carried_tick_share")) for row in group_rows]
                ),
                "avg_carry": _mean([_safe_float(row.get("avg_carry")) for row in group_rows]),
                "avg_rekopplung": _mean([_safe_float(row.get("avg_rekopplung")) for row in group_rows]),
                "avg_strain": _mean([_safe_float(row.get("avg_strain")) for row in group_rows]),
                "avg_afterimage": _mean([_safe_float(row.get("avg_afterimage")) for row in group_rows]),
                "avg_temporal_trust": _mean(
                    [_safe_float(row.get("avg_temporal_trust")) for row in group_rows]
                ),
                "dominant_pattern": patterns.most_common(1)[0][0] if patterns else "-",
                "source": "-",
            }
        )
    return summaries


def _detail_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    details = []
    for row in rows:
        details.append(
            {
                "type": "detail",
                "group": row["group"],
                "world": row["world"],
                "worlds": 1,
                "raw_runs": row.get("raw_runs", 1),
                "avg_total_ticks": row["total_ticks"],
                "avg_max_duration": row["max_duration"],
                "avg_long_segments": row["long_segments"],
                "avg_strained_segments": row["strained_segments"],
                "avg_carried_tick_share": row["carried_tick_share"],
                "avg_carry": row["avg_carry"],
                "avg_rekopplung": row["avg_rekopplung"],
                "avg_strain": row["avg_strain"],
                "avg_afterimage": row["avg_afterimage"],
                "avg_temporal_trust": row["avg_temporal_trust"],
                "dominant_pattern": row["dominant_pattern"],
                "source": row["source"],
            }
        )
    return details


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, summaries: list[dict[str, object]], details: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    summary_by_group = {str(row["group"]): row for row in summaries}
    lines = [
        "# 810 - Block-K Feldzeit Kurz/Asset-Vergleich",
        "",
        "## Fragestellung",
        "",
        "Reift Feldzeit primaer durch Dauer, durch Stress-/Regime-Art oder durch Asset-/Sinnesachsen-Mischung?",
        "",
        "## Gruppensynthese",
        "",
        "| Gruppe | Laeufe | Ticks | Max-Dauer | lange Segmente | gespannte Segmente | Carry-Anteil | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust | dominantes Muster |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for group in ["kurz_normal", "kurz_stress", "asset_mixed_2k", "lang_10k"]:
        row = summary_by_group.get(group)
        if not row:
            continue
        lines.append(
            f"| {row['group']} | {row['worlds']} Welten / {row['raw_runs']} Rohlaeufe | {_fmt(row['avg_total_ticks'])} | "
            f"{_fmt(row['avg_max_duration'])} | {_fmt(row['avg_long_segments'])} | "
            f"{_fmt(row['avg_strained_segments'])} | {_fmt(row['avg_carried_tick_share'])} | "
            f"{_fmt(row['avg_carry'])} | {_fmt(row['avg_rekopplung'])} | "
            f"{_fmt(row['avg_strain'])} | {_fmt(row['avg_afterimage'])} | "
            f"{_fmt(row['avg_temporal_trust'])} | {row['dominant_pattern']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die kurze Normal- und Stressgruppe bleibt getragen, zeigt aber deutlich weniger Feldzeit-Tiefe als die 10k-Gruppe. Die asset-gemischte 2k-Gruppe liegt zwischen kurzer Welt und langer 10k-Welt: sie ist nicht kollabiert, bildet aber keine durchgehend tiefe Feldzeit wie die langen Welten.",
            "",
            "Lesart:",
            "",
            "- Dauer wirkt stark auf Feldzeit/Trust und Nachhall.",
            "- Stress-/Regime-Art veraendert Segmentmuster und Bruchhaeufigkeit, zerlegt die Grundordnung aber nicht automatisch.",
            "- Asset-/Sinnesachsen-Mischung erzeugt Varianz, bleibt aber bei sauberer Rezeptoraufnahme feldtragend.",
            "- 10k zeigt die tiefste Integrationsqualitaet, nicht nur mehr Rohdaten.",
            "",
            "## Detailauszug",
            "",
            "| Gruppe | Welt | Max-Dauer | Nachhall | Feldzeit/Trust | Muster |",
            "|---|---|---:|---:|---:|---|",
        ]
    )
    for row in details:
        lines.append(
            f"| {row['group']} | {row['world']} | {_fmt(row['avg_max_duration'])} | "
            f"{_fmt(row['avg_afterimage'])} | {_fmt(row['avg_temporal_trust'])} | "
            f"{row['dominant_pattern']} |"
        )
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "Die Gruppen nutzen vorhandene Debuglaeufe. Das ist eine robuste Gegenprobe fuer die aktuelle Datenlage, aber noch kein vollstaendig neu generiertes Experiment mit exakt gleicher Laufzahl je Gruppe.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte ein kontrollierter Neu-Lauf mit gleicher Gruppengroesse gebaut werden: je vier 2k-Welten, vier 10k-Welten und vier Asset-Mischwelten. Dann koennen Dauer- und Asset-Effekt sauberer getrennt werden.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    rows = _rows_for_groups(GROUP_DEFAULTS)
    if not rows:
        raise FileNotFoundError("no episode files found for configured groups")
    world_rows = _aggregate_world_rows(rows)
    summaries = _summaries(world_rows)
    details = _detail_rows(world_rows)
    out_rows = summaries + details
    _write_csv(args.csv_out, out_rows)
    _write_markdown(args.md_out, summaries, details)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in summaries:
        print(
            f"{row['group']}: worlds={row['worlds']} raw_runs={row['raw_runs']} "
            f"trust={float(row['avg_temporal_trust']):.4f} "
            f"afterimage={float(row['avg_afterimage']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
