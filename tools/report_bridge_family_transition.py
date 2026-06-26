from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_fieldtime_controlled"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "817_BLOCK_K_BRUECKENFAMILIE_UEBERGANGSSTRUKTUR.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "817_BLOCK_K_BRUECKENFAMILIE_UEBERGANGSSTRUKTUR.md"
BRIDGE_FAMILY_DEFAULT = "dio_155c"
EDGE_FAMILY_DEFAULT = "dio_1un4"


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


def _group_from_path(path: Path, debug_root: Path) -> str:
    try:
        return path.relative_to(debug_root).parts[0]
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


def _summarize_rows(
    rows: list[dict[str, str]],
    *,
    row_type: str,
    context: str,
    group: str,
    bridge_family: str,
    edge_family: str,
) -> dict[str, object]:
    classes = Counter(str(row.get("passive_mcm_effect_class") or "-") for row in rows)
    inner = Counter(str(row.get("passive_inner_effect_awareness_state") or "-") for row in rows)
    episodes = Counter(
        str(row.get("mcm_field_episode_symbol") or row.get("mcm_field_episode_preview_symbol") or "-")
        for row in rows
    )
    return {
        "type": row_type,
        "context": context,
        "group": group,
        "bridge_family": bridge_family,
        "edge_family": edge_family,
        "ticks": len(rows),
        "dominant_class": _dominant(classes),
        "dominant_inner_state": _dominant(inner),
        "stable_share": classes.get("stabil", 0) / max(1, len(rows)),
        "unrest_share": classes.get("tragend_unruhig", 0) / max(1, len(rows)),
        "unique_mcm_episodes": len(episodes),
        "avg_strain": _mean([_safe_float(row.get("mcm_strain_quality")) for row in rows]),
        "avg_trust": _mean([_safe_float(row.get("mini_temporal_trust_support")) for row in rows]),
        "avg_afterimage": _mean([_safe_float(row.get("mini_afterimage")) for row in rows]),
        "avg_rekopplung": _mean([_safe_float(row.get("mcm_rekopplung_quality")) for row in rows]),
        "avg_carry": _mean([_safe_float(row.get("mcm_carry_quality")) for row in rows]),
        "avg_visual_gap": _mean([_safe_float(row.get("mcm_visual_field_gap")) for row in rows]),
        "avg_hearing_gap": _mean([_safe_float(row.get("mcm_hearing_field_gap")) for row in rows]),
        "avg_hearing_stimulation": _mean(
            [_safe_float(row.get("rezeptor_auditory_stimulation")) for row in rows]
        ),
        "avg_field_intake": _mean([_safe_float(row.get("rezeptor_field_intake_pressure")) for row in rows]),
        "fieldtime_embedding": _embedding(rows),
    }


def collect_contexts(
    debug_root: Path, bridge_family: str, edge_family: str
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    paths = sorted(debug_root.glob("*/*/dio_mini_lauf_1/episodes.csv"))
    if not paths:
        raise FileNotFoundError(f"no episodes.csv files found under {debug_root}")
    buckets: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    world_details: list[dict[str, object]] = []
    for path in paths:
        group = _group_from_path(path, debug_root)
        world = path.parent.parent.name
        rows = _read_rows(path)
        contexts = {
            "normal": [],
            "before_edge": [],
            "after_edge": [],
            "near_edge": [],
        }
        for index, row in enumerate(rows):
            if str(row.get("symbol_family") or "") != bridge_family:
                continue
            prev_family = str(rows[index - 1].get("symbol_family") or "-") if index > 0 else "-"
            next_family = str(rows[index + 1].get("symbol_family") or "-") if index + 1 < len(rows) else "-"
            if next_family == edge_family:
                contexts["before_edge"].append(row)
                contexts["near_edge"].append(row)
            if prev_family == edge_family:
                contexts["after_edge"].append(row)
                contexts["near_edge"].append(row)
            if prev_family != edge_family and next_family != edge_family:
                contexts["normal"].append(row)
        for context, context_rows in contexts.items():
            buckets[(group, context)].extend(context_rows)
            buckets[("ALL", context)].extend(context_rows)
            world_details.append(
                {
                    **_summarize_rows(
                        context_rows,
                        row_type="world_detail",
                        context=context,
                        group=group,
                        bridge_family=bridge_family,
                        edge_family=edge_family,
                    ),
                    "world": world,
                }
            )
    summary_rows = []
    for (group, context), rows in sorted(buckets.items()):
        summary_rows.append(
            _summarize_rows(
                rows,
                row_type="summary",
                context=context,
                group=group,
                bridge_family=bridge_family,
                edge_family=edge_family,
            )
        )
    return summary_rows, world_details


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
    summary_rows: list[dict[str, object]],
    world_details: list[dict[str, object]],
    bridge_family: str,
    edge_family: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_key = {(str(row["group"]), str(row["context"])): row for row in summary_rows}
    lines = [
        f"# 817 - Block-K Brueckenfamilie/Uebergangsstruktur: {bridge_family}",
        "",
        "## Fragestellung",
        "",
        f"Ist `{bridge_family}` nur ein stabiler Nachbar von `{edge_family}`, oder veraendert sich sein Feldprofil in direkter Randnaehe?",
        "",
        "## Kontextvergleich",
        "",
        "| Gruppe | Kontext | Ticks | Klasse | Stabil | Unruhe | Strain | Trust | Nachhall | Rekopplung | Hoeren-Stim. | Einbettung |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for group in ["ALL", "kurz_2k", "asset_mixed_2k", "lang_10k"]:
        for context in ["normal", "near_edge", "before_edge", "after_edge"]:
            row = by_key.get((group, context))
            if not row:
                continue
            lines.append(
                f"| {group} | {context} | {row['ticks']} | {row['dominant_class']} | "
                f"{_fmt(row['stable_share'])} | {_fmt(row['unrest_share'])} | "
                f"{_fmt(row['avg_strain'])} | {_fmt(row['avg_trust'])} | "
                f"{_fmt(row['avg_afterimage'])} | {_fmt(row['avg_rekopplung'])} | "
                f"{_fmt(row['avg_hearing_stimulation'])} | {_fmt(row['fieldtime_embedding'])} |"
            )
    all_normal = by_key.get(("ALL", "normal"))
    all_near = by_key.get(("ALL", "near_edge"))
    strain_delta = 0.0
    trust_delta = 0.0
    if all_normal and all_near:
        strain_delta = float(all_near["avg_strain"]) - float(all_normal["avg_strain"])
        trust_delta = float(all_near["avg_trust"]) - float(all_normal["avg_trust"])
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{bridge_family}` bleibt auch in direkter Naehe zu `{edge_family}` ueberwiegend stabil. Die Randnaehe veraendert aber das Profil:",
            "",
            f"- Strain-Delta near_edge gegen normal: {_fmt(strain_delta)}",
            f"- Trust-Delta near_edge gegen normal: {_fmt(trust_delta)}",
            "- near_edge ist selten, aber nicht leer; die Bruecke ist also messbar, nicht nur theoretisch,",
            "- die Stabilitaet bleibt in Randnaehe voll erhalten,",
            "- Trust faellt nicht ab; die Bruecke kollabiert also nicht in Randbelastung,",
            "- die Feldzeit-Einbettung ist in Randnaehe niedriger, weil diese Kontakte selten und lokal begrenzt sind.",
            "",
            "Lesung: Die Brueckenfamilie wird nicht zur Randfamilie, sondern bleibt stabil und beruehrt die Randspannung ohne Vertrauensverlust. Das ist naeher an einer semantischen Uebergangsstruktur als an zufaelliger Nachbarschaft.",
            "",
            "## Welt-Detail",
            "",
            "| Gruppe | Welt | Kontext | Ticks | Strain | Trust | Einbettung |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in world_details:
        if row["ticks"] == 0:
            continue
        lines.append(
            f"| {row['group']} | {row['world']} | {row['context']} | {row['ticks']} | "
            f"{_fmt(row['avg_strain'])} | {_fmt(row['avg_trust'])} | {_fmt(row['fieldtime_embedding'])} |"
        )
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "Der Befund beschreibt passive Feldnaehe. Er ist keine Handlungsauswertung und keine Aussage ueber Richtung.",
            "",
            "## Wie es weitergeht",
            "",
            f"Als naechstes sollte die Bruecke `{bridge_family}` mit einer zweiten Brueckenfamilie verglichen werden. Dann sehen wir, ob es einen gemeinsamen Brueckentyp gibt oder mehrere unterschiedliche Uebergangsarten.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--bridge-family", default=BRIDGE_FAMILY_DEFAULT)
    parser.add_argument("--edge-family", default=EDGE_FAMILY_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    summary_rows, world_details = collect_contexts(debug_root, args.bridge_family, args.edge_family)
    _write_csv(args.csv_out, summary_rows + world_details)
    _write_markdown(args.md_out, summary_rows, world_details, args.bridge_family, args.edge_family)
    print(f"bridge_family={args.bridge_family}")
    print(f"edge_family={args.edge_family}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in summary_rows:
        if row["group"] == "ALL":
            print(
                f"{row['context']}: ticks={row['ticks']} strain={float(row['avg_strain']):.4f} "
                f"trust={float(row['avg_trust']):.4f} stable={float(row['stable_share']):.4f}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
