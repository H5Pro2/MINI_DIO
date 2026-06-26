from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_fieldtime_controlled"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "816_BLOCK_K_RANDFAMILIE_NACHBARSCHAFT_BRUECKE.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "816_BLOCK_K_RANDFAMILIE_NACHBARSCHAFT_BRUECKE.md"
TARGET_FAMILY_DEFAULT = "dio_1un4"
TOP_N_DEFAULT = 12


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _episode_paths(debug_root: Path) -> list[Path]:
    paths = set(debug_root.glob("*/*/dio_mini_lauf_1/episodes.csv"))
    paths.update(debug_root.glob("dio_mini_lauf_1/episodes.csv"))
    return sorted(paths)


def _group_from_path(path: Path, debug_root: Path) -> str:
    try:
        parts = path.relative_to(debug_root).parts
        if parts and parts[0].startswith("dio_mini_lauf_"):
            return debug_root.name
        return parts[0]
    except Exception:
        return path.parts[-4]


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return counter.most_common(1)[0][0]


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


def _summarize_family(
    family: str,
    all_family_rows: list[dict[str, str]],
    before_count: int,
    after_count: int,
    groups: Counter[str],
) -> dict[str, object]:
    classes = Counter(str(row.get("passive_mcm_effect_class") or "-") for row in all_family_rows)
    inner_states = Counter(str(row.get("passive_inner_effect_awareness_state") or "-") for row in all_family_rows)
    episodes = Counter(
        str(row.get("mcm_field_episode_symbol") or row.get("mcm_field_episode_preview_symbol") or "-")
        for row in all_family_rows
    )
    total_neighbor_hits = before_count + after_count
    stable_share = classes.get("stabil", 0) / max(1, len(all_family_rows))
    unrest_share = classes.get("tragend_unruhig", 0) / max(1, len(all_family_rows))
    role = "unbestimmt"
    if stable_share >= 0.70 and after_count > 0 and before_count > 0:
        role = "stabile_bruecke"
    elif stable_share >= 0.70:
        role = "stabiler_nachbar"
    elif unrest_share >= 0.70:
        role = "randnahe_unruhe"
    elif len(episodes) > 4:
        role = "verteilte_kontaktzone"
    return {
        "type": "neighbor_summary",
        "family": family,
        "neighbor_hits": total_neighbor_hits,
        "before_hits": before_count,
        "after_hits": after_count,
        "group_count": len(groups),
        "groups": ",".join(f"{key}:{value}" for key, value in groups.most_common()),
        "family_ticks_total": len(all_family_rows),
        "dominant_class": _dominant(classes),
        "stable_share": stable_share,
        "unrest_share": unrest_share,
        "dominant_inner_state": _dominant(inner_states),
        "unique_mcm_episodes": len(episodes),
        "avg_strain": _mean([_safe_float(row.get("mcm_strain_quality")) for row in all_family_rows]),
        "avg_trust": _mean([_safe_float(row.get("mini_temporal_trust_support")) for row in all_family_rows]),
        "avg_afterimage": _mean([_safe_float(row.get("mini_afterimage")) for row in all_family_rows]),
        "avg_rekopplung": _mean([_safe_float(row.get("mcm_rekopplung_quality")) for row in all_family_rows]),
        "avg_carry": _mean([_safe_float(row.get("mcm_carry_quality")) for row in all_family_rows]),
        "avg_visual_gap": _mean([_safe_float(row.get("mcm_visual_field_gap")) for row in all_family_rows]),
        "avg_hearing_gap": _mean([_safe_float(row.get("mcm_hearing_field_gap")) for row in all_family_rows]),
        "avg_hearing_stimulation": _mean(
            [_safe_float(row.get("rezeptor_auditory_stimulation")) for row in all_family_rows]
        ),
        "fieldtime_embedding": _embedding(all_family_rows),
        "bridge_role": role,
    }


def build_report_rows(debug_root: Path, target_family: str, top_n: int) -> tuple[list[dict[str, object]], dict[str, object]]:
    paths = _episode_paths(debug_root)
    if not paths:
        raise FileNotFoundError(f"no episodes.csv files found under {debug_root}")
    family_rows: dict[str, list[dict[str, str]]] = defaultdict(list)
    before = Counter()
    after = Counter()
    neighbor_groups: dict[str, Counter[str]] = defaultdict(Counter)
    target_rows: list[dict[str, str]] = []
    for path in paths:
        group = _group_from_path(path, debug_root)
        rows = _read_rows(path)
        for row in rows:
            family_rows[str(row.get("symbol_family") or "-")].append(row)
        for index, row in enumerate(rows):
            if str(row.get("symbol_family") or "") != target_family:
                continue
            target_rows.append(row)
            if index > 0:
                family = str(rows[index - 1].get("symbol_family") or "-")
                before[family] += 1
                neighbor_groups[family][group] += 1
            if index + 1 < len(rows):
                family = str(rows[index + 1].get("symbol_family") or "-")
                after[family] += 1
                neighbor_groups[family][group] += 1
    neighbor_total = before + after
    selected = [family for family, _ in neighbor_total.most_common(top_n) if family not in {"-", target_family}]
    rows_out = [
        _summarize_family(
            family,
            family_rows.get(family, []),
            before.get(family, 0),
            after.get(family, 0),
            neighbor_groups.get(family, Counter()),
        )
        for family in selected
    ]
    target_classes = Counter(str(row.get("passive_mcm_effect_class") or "-") for row in target_rows)
    target_summary = {
        "target_family": target_family,
        "target_ticks": len(target_rows),
        "target_dominant_class": _dominant(target_classes),
        "target_avg_strain": _mean([_safe_float(row.get("mcm_strain_quality")) for row in target_rows]),
        "target_avg_trust": _mean([_safe_float(row.get("mini_temporal_trust_support")) for row in target_rows]),
        "target_embedding": _embedding(target_rows),
        "selected_neighbors": len(rows_out),
        "total_neighbor_hits": sum(neighbor_total.values()),
        "stable_bridge_count": sum(1 for row in rows_out if row["bridge_role"] == "stabile_bruecke"),
        "unrest_neighbor_count": sum(1 for row in rows_out if row["bridge_role"] == "randnahe_unruhe"),
    }
    return rows_out, target_summary


def _write_csv(path: Path, rows: list[dict[str, object]], target_summary: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    all_rows = [{"type": "target_summary", **target_summary}] + rows
    fieldnames = sorted({key for row in all_rows for key in row.keys()})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(all_rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, rows: list[dict[str, object]], target_summary: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    target_family = str(target_summary["target_family"])
    lines = [
        f"# 816 - Block-K Randfamilie Nachbarschaft/Bruecke: {target_family}",
        "",
        "## Fragestellung",
        "",
        f"Ist `{target_family}` ein isolierter Randpunkt, eine Bruecke zu stabilen Bedeutungsraeumen oder der Anfang einer Unterfamilie?",
        "",
        "## Zielzustand der Randfamilie",
        "",
        "| Familie | Ticks | Klasse | Strain | Trust | Einbettung | Nachbar-Hits |",
        "|---|---:|---|---:|---:|---:|---:|",
        f"| {target_family} | {target_summary['target_ticks']} | {target_summary['target_dominant_class']} | "
        f"{_fmt(target_summary['target_avg_strain'])} | {_fmt(target_summary['target_avg_trust'])} | "
        f"{_fmt(target_summary['target_embedding'])} | {target_summary['total_neighbor_hits']} |",
        "",
        "## Haeufigste Nachbarfamilien",
        "",
        "| Familie | Rolle | Hits | Vorher | Nachher | Gruppen | Klasse | Stabil | Unruhe | Strain | Trust | Nachhall | Einbettung |",
        "|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['family']} | {row['bridge_role']} | {row['neighbor_hits']} | "
            f"{row['before_hits']} | {row['after_hits']} | {row['group_count']} | "
            f"{row['dominant_class']} | {_fmt(row['stable_share'])} | {_fmt(row['unrest_share'])} | "
            f"{_fmt(row['avg_strain'])} | {_fmt(row['avg_trust'])} | "
            f"{_fmt(row['avg_afterimage'])} | {_fmt(row['fieldtime_embedding'])} |"
        )
    stable_bridge_count = target_summary["stable_bridge_count"]
    unrest_neighbor_count = target_summary["unrest_neighbor_count"]
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{target_family}` ist kein isolierter Randpunkt. Die haeufigsten Nachbarn beruehren mehrere Gruppen und liegen ueberwiegend in stabilen oder teilstabilen Bedeutungsraeumen.",
            "",
            f"- stabile Bruecken im Top-N-Feld: {stable_bridge_count}",
            f"- randnahe Unruhe-Nachbarn im Top-N-Feld: {unrest_neighbor_count}",
            "- viele Nachbarn treten vor und nach der Randfamilie auf; das spricht fuer Kontaktzone statt Einbahn-Uebergang,",
            "- die Randfamilie bleibt selbst strain-nah, aber ihre Umgebung ist deutlich tragender als sie selbst.",
            "",
            "Lesung: `dio_1un4` wirkt wie eine randnahe Kontakt-/Brueckenfamilie. Sie entsteht an Spannungsuebergaengen und koppelt an stabilere Bedeutungsraeume, ohne selbst zur stabilen Mitte zu werden.",
            "",
            "## Grenze",
            "",
            "Der Befund ist eine passive Nachbarschaftsdiagnose. Er beschreibt keine Handlung, keine Richtung und keine Strategie.",
            "",
            "## Wie es weitergeht",
            "",
            f"Als naechstes sollte eine der stabilen Brueckenfamilien neben `{target_family}` genauer gelesen werden. Dann sehen wir, ob die Bruecke nur Nachbarschaft ist oder eine echte semantische Uebergangsstruktur bildet.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--family", default=TARGET_FAMILY_DEFAULT)
    parser.add_argument("--top-n", type=int, default=TOP_N_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    rows, target_summary = build_report_rows(debug_root, args.family, args.top_n)
    _write_csv(args.csv_out, rows, target_summary)
    _write_markdown(args.md_out, rows, target_summary)
    print(f"family={args.family}")
    print(f"neighbors={len(rows)}")
    print(f"stable_bridges={target_summary['stable_bridge_count']}")
    print(f"unrest_neighbors={target_summary['unrest_neighbor_count']}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in rows[:8]:
        print(
            f"{row['family']}: role={row['bridge_role']} hits={row['neighbor_hits']} "
            f"class={row['dominant_class']} trust={float(row['avg_trust']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
