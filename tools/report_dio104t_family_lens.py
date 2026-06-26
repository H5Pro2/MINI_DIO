from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_fieldtime_controlled"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "813_BLOCK_K_DIO104T_FAMILIEN_LUPE.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "813_BLOCK_K_DIO104T_FAMILIEN_LUPE.md"
TARGET_FAMILY_DEFAULT = "dio_104t"


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


def _group_from_path(path: Path) -> str:
    try:
        return path.relative_to(DEBUG_DEFAULT).parts[0]
    except Exception:
        return path.parts[-4]


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return counter.most_common(1)[0][0]


def _first_meaningful(row: dict[str, str], *keys: str) -> str:
    for key in keys:
        value = str(row.get(key, "") or "")
        if value and value != "-":
            return value
    return "-"


def summarize_world(path: Path, target_family: str) -> dict[str, object]:
    rows = _read_rows(path)
    target_rows = [row for row in rows if str(row.get("symbol_family", "")) == target_family]
    total = len(rows)
    target_total = len(target_rows)
    mcm_episodes = Counter(
        _first_meaningful(row, "mcm_field_episode_symbol", "mcm_field_episode_preview_symbol")
        for row in target_rows
    )
    field_states = Counter(str(row.get("mcm_field_effect_state") or "-") for row in target_rows)
    mcm_classes = Counter(str(row.get("passive_mcm_effect_class") or "-") for row in target_rows)
    inner_states = Counter(str(row.get("passive_inner_effect_awareness_state") or "-") for row in target_rows)
    symbols = Counter(str(row.get("symbol") or "-") for row in target_rows)
    group = _group_from_path(path)
    world = path.parent.parent.name
    field_episode_unique = len(mcm_episodes)
    family_share = target_total / max(1, total)
    family_symbol_reuse = 1.0 - (len(symbols) / max(1, target_total))
    avg_mcm_carry = _mean([_safe_float(row.get("mcm_carry_quality")) for row in target_rows])
    avg_mcm_rekopplung = _mean([_safe_float(row.get("mcm_rekopplung_quality")) for row in target_rows])
    avg_mcm_strain = _mean([_safe_float(row.get("mcm_strain_quality")) for row in target_rows])
    avg_afterimage = _mean([_safe_float(row.get("mini_afterimage")) for row in target_rows])
    avg_temporal_trust = _mean([_safe_float(row.get("mini_temporal_trust_support")) for row in target_rows])
    dominant_episode_share = 0.0
    if target_total > 0 and mcm_episodes:
        dominant_episode_share = mcm_episodes.most_common(1)[0][1] / target_total
    # Diagnostic only: tightness of one family around one dominant field episode.
    family_concentration_score = (
        family_share * 0.25
        + dominant_episode_share * 0.25
        + avg_mcm_rekopplung * 0.20
        + avg_temporal_trust * 0.15
        + max(0.0, 1.0 - avg_mcm_strain) * 0.15
    )
    # Diagnostic only: broad fieldtime embedding without rewarding one-episode narrowing.
    family_fieldtime_embedding_score = (
        family_symbol_reuse * 0.25
        + avg_temporal_trust * 0.25
        + avg_afterimage * 0.15
        + avg_mcm_rekopplung * 0.20
        + max(0.0, 1.0 - avg_mcm_strain) * 0.15
    )
    return {
        "type": "detail",
        "group": group,
        "world": world,
        "target_family": target_family,
        "ticks": total,
        "family_ticks": target_total,
        "family_share": family_share,
        "family_unique_symbols": len(symbols),
        "family_symbol_reuse": family_symbol_reuse,
        "dominant_symbol": _dominant(symbols),
        "dominant_mcm_episode": _dominant(mcm_episodes),
        "dominant_mcm_episode_share": dominant_episode_share,
        "unique_mcm_episodes": field_episode_unique,
        "dominant_field_state": _dominant(field_states),
        "dominant_mcm_class": _dominant(mcm_classes),
        "dominant_inner_state": _dominant(inner_states),
        "avg_mcm_carry": avg_mcm_carry,
        "avg_mcm_rekopplung": avg_mcm_rekopplung,
        "avg_mcm_strain": avg_mcm_strain,
        "avg_sensory_coupling": _mean([_safe_float(row.get("mcm_sensory_coupling")) for row in target_rows]),
        "avg_visual_field_gap": _mean([_safe_float(row.get("mcm_visual_field_gap")) for row in target_rows]),
        "avg_hearing_field_gap": _mean([_safe_float(row.get("mcm_hearing_field_gap")) for row in target_rows]),
        "avg_visual_salience": _mean([_safe_float(row.get("rezeptor_visual_form_salience")) for row in target_rows]),
        "avg_memory_recall": _mean([_safe_float(row.get("rezeptor_visual_memory_recall")) for row in target_rows]),
        "avg_auditory_stimulation": _mean([_safe_float(row.get("rezeptor_auditory_stimulation")) for row in target_rows]),
        "avg_direct_contact_pressure": _mean(
            [_safe_float(row.get("rezeptor_direct_contact_pressure")) for row in target_rows]
        ),
        "avg_field_intake_pressure": _mean(
            [_safe_float(row.get("rezeptor_field_intake_pressure")) for row in target_rows]
        ),
        "avg_mcm_coherence": _mean([_safe_float(row.get("mcm_feldwirkung_mcm_coherence")) for row in target_rows]),
        "avg_mcm_tension": _mean([_safe_float(row.get("mcm_feldwirkung_mcm_tension")) for row in target_rows]),
        "avg_mcm_asymmetry": _mean([_safe_float(row.get("mcm_feldwirkung_mcm_asymmetry")) for row in target_rows]),
        "avg_afterimage": avg_afterimage,
        "avg_temporal_trust": avg_temporal_trust,
        "avg_temporal_caution": _mean([_safe_float(row.get("mini_temporal_caution_support")) for row in target_rows]),
        "family_concentration_score": family_concentration_score,
        "family_fieldtime_embedding_score": family_fieldtime_embedding_score,
        "source": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
    }


def summarize_groups(details: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in details:
        grouped[str(row["group"])].append(row)
    summaries: list[dict[str, object]] = []
    for group, rows in grouped.items():
        mcm_episodes = Counter(str(row["dominant_mcm_episode"]) for row in rows)
        field_states = Counter(str(row["dominant_field_state"]) for row in rows)
        mcm_classes = Counter(str(row["dominant_mcm_class"]) for row in rows)
        inner_states = Counter(str(row["dominant_inner_state"]) for row in rows)
        summaries.append(
            {
                "type": "summary",
                "group": group,
                "world": "GROUP",
                "target_family": rows[0]["target_family"] if rows else TARGET_FAMILY_DEFAULT,
                "ticks": _mean([_safe_float(row["ticks"]) for row in rows]),
                "family_ticks": _mean([_safe_float(row["family_ticks"]) for row in rows]),
                "family_share": _mean([_safe_float(row["family_share"]) for row in rows]),
                "family_unique_symbols": _mean([_safe_float(row["family_unique_symbols"]) for row in rows]),
                "family_symbol_reuse": _mean([_safe_float(row["family_symbol_reuse"]) for row in rows]),
                "dominant_symbol": "-",
                "dominant_mcm_episode": _dominant(mcm_episodes),
                "dominant_mcm_episode_share": _mean(
                    [_safe_float(row["dominant_mcm_episode_share"]) for row in rows]
                ),
                "unique_mcm_episodes": _mean([_safe_float(row["unique_mcm_episodes"]) for row in rows]),
                "dominant_field_state": _dominant(field_states),
                "dominant_mcm_class": _dominant(mcm_classes),
                "dominant_inner_state": _dominant(inner_states),
                "avg_mcm_carry": _mean([_safe_float(row["avg_mcm_carry"]) for row in rows]),
                "avg_mcm_rekopplung": _mean([_safe_float(row["avg_mcm_rekopplung"]) for row in rows]),
                "avg_mcm_strain": _mean([_safe_float(row["avg_mcm_strain"]) for row in rows]),
                "avg_sensory_coupling": _mean([_safe_float(row["avg_sensory_coupling"]) for row in rows]),
                "avg_visual_field_gap": _mean([_safe_float(row["avg_visual_field_gap"]) for row in rows]),
                "avg_hearing_field_gap": _mean([_safe_float(row["avg_hearing_field_gap"]) for row in rows]),
                "avg_visual_salience": _mean([_safe_float(row["avg_visual_salience"]) for row in rows]),
                "avg_memory_recall": _mean([_safe_float(row["avg_memory_recall"]) for row in rows]),
                "avg_auditory_stimulation": _mean(
                    [_safe_float(row["avg_auditory_stimulation"]) for row in rows]
                ),
                "avg_direct_contact_pressure": _mean(
                    [_safe_float(row["avg_direct_contact_pressure"]) for row in rows]
                ),
                "avg_field_intake_pressure": _mean(
                    [_safe_float(row["avg_field_intake_pressure"]) for row in rows]
                ),
                "avg_mcm_coherence": _mean([_safe_float(row["avg_mcm_coherence"]) for row in rows]),
                "avg_mcm_tension": _mean([_safe_float(row["avg_mcm_tension"]) for row in rows]),
                "avg_mcm_asymmetry": _mean([_safe_float(row["avg_mcm_asymmetry"]) for row in rows]),
                "avg_afterimage": _mean([_safe_float(row["avg_afterimage"]) for row in rows]),
                "avg_temporal_trust": _mean([_safe_float(row["avg_temporal_trust"]) for row in rows]),
                "avg_temporal_caution": _mean([_safe_float(row["avg_temporal_caution"]) for row in rows]),
                "family_concentration_score": _mean(
                    [_safe_float(row["family_concentration_score"]) for row in rows]
                ),
                "family_fieldtime_embedding_score": _mean(
                    [_safe_float(row["family_fieldtime_embedding_score"]) for row in rows]
                ),
                "source": "-",
            }
        )
    return summaries


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


def _write_markdown(path: Path, summaries: list[dict[str, object]], details: list[dict[str, object]], target_family: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_group = {str(row["group"]): row for row in summaries}
    lines = [
        f"# 813 - Block-K Familien-Lupe {target_family}",
        "",
        "## Fragestellung",
        "",
        f"Welche Feldlage, Sinnesachsen und Weltkontakte tragen die stabile Top-Familie `{target_family}` in 2k und 10k?",
        "",
        "## Gruppensynthese",
        "",
        "| Gruppe | Anteil | Symbol-Reuse | MCM-Episoden | domin. Episode | Episode-Anteil | Feldklasse | Innenzustand | Rekopplung | Carry | Strain | Sehen-Gap | Hoeren-Gap | Feldzeit/Trust | Nachhall | Konzentration | Einbettung |",
        "|---|---:|---:|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for group in ["kurz_2k", "asset_mixed_2k", "lang_10k"]:
        row = by_group.get(group)
        if not row:
            continue
        lines.append(
            f"| {row['group']} | {_fmt(row['family_share'])} | {_fmt(row['family_symbol_reuse'])} | "
            f"{_fmt(row['unique_mcm_episodes'])} | {row['dominant_mcm_episode']} | "
            f"{_fmt(row['dominant_mcm_episode_share'])} | {row['dominant_mcm_class']} | "
            f"{row['dominant_inner_state']} | {_fmt(row['avg_mcm_rekopplung'])} | "
            f"{_fmt(row['avg_mcm_carry'])} | {_fmt(row['avg_mcm_strain'])} | "
            f"{_fmt(row['avg_visual_field_gap'])} | {_fmt(row['avg_hearing_field_gap'])} | "
            f"{_fmt(row['avg_temporal_trust'])} | {_fmt(row['avg_afterimage'])} | "
            f"{_fmt(row['family_concentration_score'])} | "
            f"{_fmt(row['family_fieldtime_embedding_score'])} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{target_family}` ist keine beliebige Einzelmarke, sondern eine wiederkehrende Traegerfamilie. Sie bleibt in allen Gruppen dominant, veraendert aber ihre Einbettung:",
            "",
            "- in kurzen Welten ist sie sichtbar, aber auf weniger Feldzeit eingebettet,",
            "- in asset-gemischten 2k-Welten bleibt sie trotz Asset-Varianz tragend,",
            "- in 10k-Welten steigt vor allem Feldzeit/Trust und Nachhall,",
            "- die Konzentration auf eine einzelne MCM-Episode sinkt in 10k, weil die Familie breiter ueber Feldzeit verteilt wird,",
            "- die MCM-Klasse bleibt ueberwiegend stabil/tragend, ohne motorische oder Gate-Funktion.",
            "",
            f"Damit ist `{target_family}` eher eine passive Bedeutungsfamilie des Innenfeldes als eine Handlungsregel. Sie wirkt wie ein wiederverwendeter semantischer Traeger, der in laengerer Feldzeit tiefer eingebettet wird.",
            "",
            "Wichtig: Konzentration und Einbettung sind hier getrennt. Konzentration meint die Enge um eine dominante MCM-Episode. Einbettung meint, ob die Familie ueber laengere Feldzeit stabil wiederverwendet und getragen bleibt.",
            "",
            "## Detailauszug",
            "",
            "| Gruppe | Welt | Anteil | Symbol-Reuse | MCM-Episode | Episode-Anteil | Rekopplung | Carry | Strain | Feldzeit/Trust | Nachhall |",
            "|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in details:
        lines.append(
            f"| {row['group']} | {row['world']} | {_fmt(row['family_share'])} | "
            f"{_fmt(row['family_symbol_reuse'])} | {row['dominant_mcm_episode']} | "
            f"{_fmt(row['dominant_mcm_episode_share'])} | {_fmt(row['avg_mcm_rekopplung'])} | "
            f"{_fmt(row['avg_mcm_carry'])} | {_fmt(row['avg_mcm_strain'])} | "
            f"{_fmt(row['avg_temporal_trust'])} | {_fmt(row['avg_afterimage'])} |"
        )
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "Diese Lupe beschreibt eine passive Bedeutungsfamilie. Sie ist keine Handlungsauswertung, keine Strategie und keine Aussage darueber, was MINI_DIO tun soll.",
            "",
            "## Wie es weitergeht",
            "",
            f"Als naechstes sollte `{target_family}` gegen eine Rand- oder Bruchfamilie verglichen werden. Dann sehen wir, ob stabile Familien und gespannte Randfamilien unterschiedliche Sinnes-/Feldprofile tragen.",
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
    episode_paths = sorted(debug_root.glob("*/*/dio_mini_lauf_1/episodes.csv"))
    if not episode_paths:
        raise FileNotFoundError(f"no episodes.csv files found under {debug_root}")
    details = [summarize_world(path, args.family) for path in episode_paths]
    summaries = summarize_groups(details)
    _write_csv(args.csv_out, summaries + details)
    _write_markdown(args.md_out, summaries, details, args.family)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in summaries:
        print(
            f"{row['group']}: share={float(row['family_share']):.4f} "
            f"trust={float(row['avg_temporal_trust']):.4f} "
            f"concentration={float(row['family_concentration_score']):.4f} "
            f"embedding={float(row['family_fieldtime_embedding_score']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
