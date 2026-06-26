from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_fieldtime_controlled"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "815_BLOCK_K_RANDFAMILIE_FOLGEWELT_REIFUNG.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "815_BLOCK_K_RANDFAMILIE_FOLGEWELT_REIFUNG.md"
TARGET_FAMILY_DEFAULT = "dio_1un4"


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _safe_int(value: object, default: int = 0) -> int:
    try:
        return int(float(value))
    except Exception:
        return default


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _group_from_path(path: Path, debug_root: Path) -> str:
    try:
        return path.relative_to(debug_root).parts[0]
    except Exception:
        return path.parts[-4]


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return counter.most_common(1)[0][0]


def _top(counter: Counter[str], limit: int = 3) -> str:
    if not counter:
        return "-"
    return ", ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _embedding(rows: list[dict[str, str]]) -> float:
    symbols = Counter(str(row.get("symbol") or "-") for row in rows)
    symbol_reuse = 1.0 - (len(symbols) / max(1, len(rows)))
    avg_trust = _mean([_safe_float(row.get("mini_temporal_trust_support")) for row in rows])
    avg_afterimage = _mean([_safe_float(row.get("mini_afterimage")) for row in rows])
    avg_rekopplung = _mean([_safe_float(row.get("mcm_rekopplung_quality")) for row in rows])
    avg_strain = _mean([_safe_float(row.get("mcm_strain_quality")) for row in rows])
    return (
        symbol_reuse * 0.25
        + avg_trust * 0.25
        + avg_afterimage * 0.15
        + avg_rekopplung * 0.20
        + max(0.0, 1.0 - avg_strain) * 0.15
    )


def _summarize_rows(
    rows: list[dict[str, str]],
    *,
    row_type: str,
    group: str,
    world: str,
    segment: str,
    target_family: str,
) -> dict[str, object]:
    total = len(rows)
    classes = Counter(str(row.get("passive_mcm_effect_class") or "-") for row in rows)
    inner_states = Counter(str(row.get("passive_inner_effect_awareness_state") or "-") for row in rows)
    episodes = Counter(
        str(row.get("mcm_field_episode_symbol") or row.get("mcm_field_episode_preview_symbol") or "-")
        for row in rows
    )
    return {
        "type": row_type,
        "group": group,
        "world": world,
        "segment": segment,
        "target_family": target_family,
        "family_ticks": total,
        "dominant_class": _dominant(classes),
        "dominant_inner_state": _dominant(inner_states),
        "dominant_episode": _dominant(episodes),
        "unique_episodes": len(episodes),
        "avg_strain": _mean([_safe_float(row.get("mcm_strain_quality")) for row in rows]),
        "avg_trust": _mean([_safe_float(row.get("mini_temporal_trust_support")) for row in rows]),
        "avg_afterimage": _mean([_safe_float(row.get("mini_afterimage")) for row in rows]),
        "avg_rekopplung": _mean([_safe_float(row.get("mcm_rekopplung_quality")) for row in rows]),
        "avg_carry": _mean([_safe_float(row.get("mcm_carry_quality")) for row in rows]),
        "avg_visual_gap": _mean([_safe_float(row.get("mcm_visual_field_gap")) for row in rows]),
        "avg_hearing_gap": _mean([_safe_float(row.get("mcm_hearing_field_gap")) for row in rows]),
        "avg_hearing_stimulation": _mean([_safe_float(row.get("rezeptor_auditory_stimulation")) for row in rows]),
        "avg_field_intake": _mean([_safe_float(row.get("rezeptor_field_intake_pressure")) for row in rows]),
        "avg_temporal_caution": _mean([_safe_float(row.get("mini_temporal_caution_support")) for row in rows]),
        "fieldtime_embedding": _embedding(rows),
        "class_mix": _top(classes),
    }


def _segment_for_tick(tick: int, max_tick: int) -> str:
    if max_tick <= 0:
        return "q1"
    ratio = tick / max_tick
    if ratio < 0.25:
        return "q1"
    if ratio < 0.50:
        return "q2"
    if ratio < 0.75:
        return "q3"
    return "q4"


def summarize_world(path: Path, debug_root: Path, target_family: str) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = _read_rows(path)
    group = _group_from_path(path, debug_root)
    world = path.parent.parent.name
    max_tick = max((_safe_int(row.get("tick")) for row in rows), default=0)
    target_indices = [index for index, row in enumerate(rows) if str(row.get("symbol_family") or "") == target_family]
    target_rows = [rows[index] for index in target_indices]
    result_rows: list[dict[str, object]] = []
    result_rows.append(
        {
            **_summarize_rows(
                target_rows,
                row_type="world",
                group=group,
                world=world,
                segment="all",
                target_family=target_family,
            ),
            "world_ticks": len(rows),
            "family_share": len(target_rows) / max(1, len(rows)),
        }
    )
    if group == "lang_10k":
        by_segment: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in target_rows:
            by_segment[_segment_for_tick(_safe_int(row.get("tick")), max_tick)].append(row)
        for segment in ["q1", "q2", "q3", "q4"]:
            segment_rows = by_segment.get(segment, [])
            summary = _summarize_rows(
                segment_rows,
                row_type="segment",
                group=group,
                world=world,
                segment=segment,
                target_family=target_family,
            )
            summary["world_ticks"] = len(rows)
            summary["family_share"] = len(segment_rows) / max(1, len(rows) / 4)
            result_rows.append(summary)
    before = Counter()
    after = Counter()
    before_classes = Counter()
    after_classes = Counter()
    for index in target_indices:
        if index > 0:
            prev = rows[index - 1]
            before[str(prev.get("symbol_family") or "-")] += 1
            before_classes[str(prev.get("passive_mcm_effect_class") or "-")] += 1
        if index + 1 < len(rows):
            nxt = rows[index + 1]
            after[str(nxt.get("symbol_family") or "-")] += 1
            after_classes[str(nxt.get("passive_mcm_effect_class") or "-")] += 1
    neighbor_row = {
        "type": "neighbor",
        "group": group,
        "world": world,
        "segment": "neighbors",
        "target_family": target_family,
        "family_ticks": len(target_rows),
        "before_top": _top(before),
        "after_top": _top(after),
        "before_class_top": _top(before_classes),
        "after_class_top": _top(after_classes),
    }
    return result_rows, neighbor_row


def summarize_group(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        if row["type"] == "world":
            grouped[(str(row["group"]), "all")].append(row)
        if row["type"] == "segment":
            grouped[(str(row["group"]), str(row["segment"]))].append(row)
    out: list[dict[str, object]] = []
    for (group, segment), items in grouped.items():
        classes = Counter(str(row["dominant_class"]) for row in items)
        inner = Counter(str(row["dominant_inner_state"]) for row in items)
        out.append(
            {
                "type": "group_summary",
                "group": group,
                "world": "GROUP",
                "segment": segment,
                "target_family": items[0]["target_family"],
                "family_ticks": _mean([_safe_float(row["family_ticks"]) for row in items]),
                "world_ticks": _mean([_safe_float(row["world_ticks"]) for row in items]),
                "family_share": _mean([_safe_float(row["family_share"]) for row in items]),
                "dominant_class": _dominant(classes),
                "dominant_inner_state": _dominant(inner),
                "avg_strain": _mean([_safe_float(row["avg_strain"]) for row in items]),
                "avg_trust": _mean([_safe_float(row["avg_trust"]) for row in items]),
                "avg_afterimage": _mean([_safe_float(row["avg_afterimage"]) for row in items]),
                "avg_rekopplung": _mean([_safe_float(row["avg_rekopplung"]) for row in items]),
                "avg_carry": _mean([_safe_float(row["avg_carry"]) for row in items]),
                "avg_visual_gap": _mean([_safe_float(row["avg_visual_gap"]) for row in items]),
                "avg_hearing_gap": _mean([_safe_float(row["avg_hearing_gap"]) for row in items]),
                "avg_hearing_stimulation": _mean([_safe_float(row["avg_hearing_stimulation"]) for row in items]),
                "avg_field_intake": _mean([_safe_float(row["avg_field_intake"]) for row in items]),
                "avg_temporal_caution": _mean([_safe_float(row["avg_temporal_caution"]) for row in items]),
                "fieldtime_embedding": _mean([_safe_float(row["fieldtime_embedding"]) for row in items]),
            }
        )
    return out


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(
    path: Path,
    group_rows: list[dict[str, object]],
    detail_rows: list[dict[str, object]],
    neighbor_rows: list[dict[str, object]],
    target_family: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    groups = {(str(row["group"]), str(row["segment"])): row for row in group_rows}
    lines = [
        f"# 815 - Block-K Randfamilie Folgewelt/Reifung: {target_family}",
        "",
        "## Fragestellung",
        "",
        f"Bleibt `{target_family}` eine Randspannung, reift sie ueber laengere Feldzeit nach, driftet sie oder bildet sie Nachbarschaften?",
        "",
        "## Gruppensynthese",
        "",
        "| Gruppe | Anteil | Klasse | Innenzustand | Strain | Trust | Nachhall | Rekopplung | Carry | Hoeren-Stim. | Einbettung |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for group in ["kurz_2k", "asset_mixed_2k", "lang_10k"]:
        row = groups.get((group, "all"))
        if not row:
            continue
        lines.append(
            f"| {group} | {_fmt(row['family_share'])} | {row['dominant_class']} | "
            f"{row['dominant_inner_state']} | {_fmt(row['avg_strain'])} | "
            f"{_fmt(row['avg_trust'])} | {_fmt(row['avg_afterimage'])} | "
            f"{_fmt(row['avg_rekopplung'])} | {_fmt(row['avg_carry'])} | "
            f"{_fmt(row['avg_hearing_stimulation'])} | {_fmt(row['fieldtime_embedding'])} |"
        )
    lines.extend(
        [
            "",
            "## 10k-Verlauf",
            "",
            "| Segment | Anteil | Klasse | Strain | Trust | Nachhall | Einbettung |",
            "|---|---:|---|---:|---:|---:|---:|",
        ]
    )
    for segment in ["q1", "q2", "q3", "q4"]:
        row = groups.get(("lang_10k", segment))
        if not row:
            continue
        lines.append(
            f"| {segment} | {_fmt(row['family_share'])} | {row['dominant_class']} | "
            f"{_fmt(row['avg_strain'])} | {_fmt(row['avg_trust'])} | "
            f"{_fmt(row['avg_afterimage'])} | {_fmt(row['fieldtime_embedding'])} |"
        )
    lines.extend(
        [
            "",
            "## Nachbarschaften",
            "",
            "| Gruppe | Welt | Vorher | Nachher | Vorher-Klasse | Nachher-Klasse |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in neighbor_rows:
        lines.append(
            f"| {row['group']} | {row['world']} | {row['before_top']} | {row['after_top']} | "
            f"{row['before_class_top']} | {row['after_class_top']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{target_family}` bleibt in allen Gruppen eine Rand-/Unruhefamilie, aber sie ist kein reines Rauschen.",
            "",
            "- in kurzen und asset-gemischten 2k-Welten ist Trust niedrig und Nachhall fast nicht ausgebildet,",
            "- in 10k steigt Trust und Feldzeit-Einbettung deutlich,",
            "- im 10k-Verlauf beginnt q1 noch schwach getragen; q2 bis q4 zeigen deutlich hoeheren Trust,",
            "- Strain bleibt ab q2 trotzdem hoch; die Familie kippt also nicht einfach in eine stabile Mitte,",
            "- q3 wirkt am staerksten eingebettet, q4 bleibt vertrauensnaeher, aber nicht voll stabilisiert,",
            "- die Nachbarschaften sind ueberwiegend stabil; die Randfamilie ist also eher Bruecken-/Kontaktzone als isoliertes Rauschen.",
            "",
            "Damit ist die wahrscheinlichste Lesung: `dio_1un4` ist eine randnahe Spannungsbedeutung, die durch laengere Feldzeit teilweise nachreifen kann, aber ihre Randqualitaet nicht verliert.",
            "",
            "## Grenze",
            "",
            "Der Befund beschreibt passive Innenfeldreifung. Er ist keine Handlungsauswertung und keine Richtungslogik.",
            "",
            "## Wie es weitergeht",
            "",
            f"Als naechstes sollte `{target_family}` gegen seine haeufigsten Nachbarfamilien gelesen werden. Dann wird sichtbar, ob daraus eine Bruecke, eine Unterfamilie oder ein isolierter Randpunkt entsteht.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--family", default=TARGET_FAMILY_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    paths = sorted(debug_root.glob("*/*/dio_mini_lauf_1/episodes.csv"))
    if not paths:
        raise FileNotFoundError(f"no episodes.csv files found under {debug_root}")
    detail_rows: list[dict[str, object]] = []
    neighbor_rows: list[dict[str, object]] = []
    for path in paths:
        world_rows, neighbor_row = summarize_world(path, debug_root, args.family)
        detail_rows.extend(world_rows)
        neighbor_rows.append(neighbor_row)
    group_rows = summarize_group(detail_rows)
    _write_csv(args.csv_out, group_rows + detail_rows + neighbor_rows)
    _write_markdown(args.md_out, group_rows, detail_rows, neighbor_rows, args.family)
    print(f"family={args.family}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in sorted(group_rows, key=lambda item: (str(item["group"]), str(item["segment"]))):
        if row["segment"] != "all":
            continue
        print(
            f"{row['group']}: share={float(row['family_share']):.4f} "
            f"strain={float(row['avg_strain']):.4f} trust={float(row['avg_trust']):.4f} "
            f"embedding={float(row['fieldtime_embedding']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
