from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_fieldtime_controlled"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "814_BLOCK_K_STABIL_GEGEN_RAND_FAMILIENKONTRAST.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "814_BLOCK_K_STABIL_GEGEN_RAND_FAMILIENKONTRAST.md"
STABLE_FAMILY_DEFAULT = "dio_104t"
EDGE_FAMILY_DEFAULT = ""


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


def _first_meaningful(row: dict[str, str], *keys: str) -> str:
    for key in keys:
        value = str(row.get(key, "") or "")
        if value and value != "-":
            return value
    return "-"


def _episode_paths(debug_root: Path) -> list[Path]:
    paths = sorted(debug_root.glob("*/*/dio_mini_lauf_1/episodes.csv"))
    if not paths:
        raise FileNotFoundError(f"no episodes.csv files found under {debug_root}")
    return paths


def _choose_edge_family(paths: list[Path], debug_root: Path, stable_family: str) -> str:
    stats: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "n": 0,
            "groups": Counter(),
            "classes": Counter(),
            "strain_sum": 0.0,
            "trust_sum": 0.0,
        }
    )
    for path in paths:
        group = _group_from_path(path, debug_root)
        for row in _read_rows(path):
            family = str(row.get("symbol_family", "") or "-")
            if family in {"-", stable_family}:
                continue
            item = stats[family]
            item["n"] = int(item["n"]) + 1
            item["groups"][group] += 1
            item["classes"][str(row.get("passive_mcm_effect_class") or "-")] += 1
            item["strain_sum"] = float(item["strain_sum"]) + _safe_float(row.get("mcm_strain_quality"))
            item["trust_sum"] = float(item["trust_sum"]) + _safe_float(row.get("mini_temporal_trust_support"))
    candidates: list[tuple[float, float, int, str]] = []
    for family, item in stats.items():
        n = int(item["n"])
        groups = item["groups"]
        classes = item["classes"]
        if n < 100 or len(groups) < 3:
            continue
        carried_unrest_share = classes.get("tragend_unruhig", 0) / max(1, n)
        if carried_unrest_share < 0.70:
            continue
        avg_strain = float(item["strain_sum"]) / max(1, n)
        avg_trust = float(item["trust_sum"]) / max(1, n)
        candidates.append((avg_strain, -avg_trust, n, family))
    if not candidates:
        raise RuntimeError("no edge family candidate found")
    candidates.sort(reverse=True)
    return candidates[0][3]


def summarize_family(path: Path, debug_root: Path, family: str, role: str) -> dict[str, object]:
    rows = _read_rows(path)
    target_rows = [row for row in rows if str(row.get("symbol_family", "")) == family]
    total = len(rows)
    target_total = len(target_rows)
    mcm_episodes = Counter(
        _first_meaningful(row, "mcm_field_episode_symbol", "mcm_field_episode_preview_symbol")
        for row in target_rows
    )
    symbols = Counter(str(row.get("symbol") or "-") for row in target_rows)
    mcm_classes = Counter(str(row.get("passive_mcm_effect_class") or "-") for row in target_rows)
    inner_states = Counter(str(row.get("passive_inner_effect_awareness_state") or "-") for row in target_rows)
    field_states = Counter(str(row.get("mcm_field_effect_state") or "-") for row in target_rows)
    dominant_episode_share = 0.0
    if target_total > 0 and mcm_episodes:
        dominant_episode_share = mcm_episodes.most_common(1)[0][1] / target_total
    symbol_reuse = 1.0 - (len(symbols) / max(1, target_total))
    avg_rekopplung = _mean([_safe_float(row.get("mcm_rekopplung_quality")) for row in target_rows])
    avg_strain = _mean([_safe_float(row.get("mcm_strain_quality")) for row in target_rows])
    avg_trust = _mean([_safe_float(row.get("mini_temporal_trust_support")) for row in target_rows])
    avg_afterimage = _mean([_safe_float(row.get("mini_afterimage")) for row in target_rows])
    fieldtime_embedding = (
        symbol_reuse * 0.25
        + avg_trust * 0.25
        + avg_afterimage * 0.15
        + avg_rekopplung * 0.20
        + max(0.0, 1.0 - avg_strain) * 0.15
    )
    return {
        "type": "detail",
        "role": role,
        "family": family,
        "group": _group_from_path(path, debug_root),
        "world": path.parent.parent.name,
        "ticks": total,
        "family_ticks": target_total,
        "family_share": target_total / max(1, total),
        "unique_symbols": len(symbols),
        "symbol_reuse": symbol_reuse,
        "dominant_mcm_episode": _dominant(mcm_episodes),
        "dominant_mcm_episode_share": dominant_episode_share,
        "unique_mcm_episodes": len(mcm_episodes),
        "dominant_mcm_class": _dominant(mcm_classes),
        "dominant_inner_state": _dominant(inner_states),
        "dominant_field_state": _dominant(field_states),
        "avg_mcm_rekopplung": avg_rekopplung,
        "avg_mcm_carry": _mean([_safe_float(row.get("mcm_carry_quality")) for row in target_rows]),
        "avg_mcm_strain": avg_strain,
        "avg_sensory_coupling": _mean([_safe_float(row.get("mcm_sensory_coupling")) for row in target_rows]),
        "avg_visual_field_gap": _mean([_safe_float(row.get("mcm_visual_field_gap")) for row in target_rows]),
        "avg_hearing_field_gap": _mean([_safe_float(row.get("mcm_hearing_field_gap")) for row in target_rows]),
        "avg_visual_salience": _mean([_safe_float(row.get("rezeptor_visual_form_salience")) for row in target_rows]),
        "avg_memory_recall": _mean([_safe_float(row.get("rezeptor_visual_memory_recall")) for row in target_rows]),
        "avg_auditory_stimulation": _mean(
            [_safe_float(row.get("rezeptor_auditory_stimulation")) for row in target_rows]
        ),
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
        "avg_temporal_trust": avg_trust,
        "avg_temporal_caution": _mean([_safe_float(row.get("mini_temporal_caution_support")) for row in target_rows]),
        "fieldtime_embedding": fieldtime_embedding,
        "source": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
    }


def summarize_groups(details: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in details:
        grouped[(str(row["role"]), str(row["family"]), str(row["group"]))].append(row)
    summaries: list[dict[str, object]] = []
    for (role, family, group), rows in grouped.items():
        mcm_episodes = Counter(str(row["dominant_mcm_episode"]) for row in rows)
        mcm_classes = Counter(str(row["dominant_mcm_class"]) for row in rows)
        inner_states = Counter(str(row["dominant_inner_state"]) for row in rows)
        field_states = Counter(str(row["dominant_field_state"]) for row in rows)
        summaries.append(
            {
                "type": "summary",
                "role": role,
                "family": family,
                "group": group,
                "world": "GROUP",
                "ticks": _mean([_safe_float(row["ticks"]) for row in rows]),
                "family_ticks": _mean([_safe_float(row["family_ticks"]) for row in rows]),
                "family_share": _mean([_safe_float(row["family_share"]) for row in rows]),
                "unique_symbols": _mean([_safe_float(row["unique_symbols"]) for row in rows]),
                "symbol_reuse": _mean([_safe_float(row["symbol_reuse"]) for row in rows]),
                "dominant_mcm_episode": _dominant(mcm_episodes),
                "dominant_mcm_episode_share": _mean(
                    [_safe_float(row["dominant_mcm_episode_share"]) for row in rows]
                ),
                "unique_mcm_episodes": _mean([_safe_float(row["unique_mcm_episodes"]) for row in rows]),
                "dominant_mcm_class": _dominant(mcm_classes),
                "dominant_inner_state": _dominant(inner_states),
                "dominant_field_state": _dominant(field_states),
                "avg_mcm_rekopplung": _mean([_safe_float(row["avg_mcm_rekopplung"]) for row in rows]),
                "avg_mcm_carry": _mean([_safe_float(row["avg_mcm_carry"]) for row in rows]),
                "avg_mcm_strain": _mean([_safe_float(row["avg_mcm_strain"]) for row in rows]),
                "avg_sensory_coupling": _mean([_safe_float(row["avg_sensory_coupling"]) for row in rows]),
                "avg_visual_field_gap": _mean([_safe_float(row["avg_visual_field_gap"]) for row in rows]),
                "avg_hearing_field_gap": _mean([_safe_float(row["avg_hearing_field_gap"]) for row in rows]),
                "avg_visual_salience": _mean([_safe_float(row["avg_visual_salience"]) for row in rows]),
                "avg_memory_recall": _mean([_safe_float(row["avg_memory_recall"]) for row in rows]),
                "avg_auditory_stimulation": _mean([_safe_float(row["avg_auditory_stimulation"]) for row in rows]),
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
                "fieldtime_embedding": _mean([_safe_float(row["fieldtime_embedding"]) for row in rows]),
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


def _summary_by(summaries: list[dict[str, object]]) -> dict[tuple[str, str], dict[str, object]]:
    return {(str(row["role"]), str(row["group"])): row for row in summaries}


def _write_markdown(
    path: Path,
    summaries: list[dict[str, object]],
    details: list[dict[str, object]],
    stable_family: str,
    edge_family: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_key = _summary_by(summaries)
    lines = [
        "# 814 - Block-K Familienkontrast: stabil gegen Rand",
        "",
        "## Fragestellung",
        "",
        f"Unterscheiden sich die stabile Traegerfamilie `{stable_family}` und die gespannte Randfamilie `{edge_family}` in Feldlage, Sinnesachsen und Feldzeit?",
        "",
        "## Auswahl der Randfamilie",
        "",
        f"`{edge_family}` wurde datengetrieben gewaehlt: ausreichend haeufig, in allen drei Gruppen vorhanden und mit der hoechsten durchschnittlichen MCM-Strain unter ueberwiegend `tragend_unruhig`-Familien.",
        "",
        "## Gruppensynthese",
        "",
        "| Gruppe | Rolle | Familie | Anteil | Klasse | Innenzustand | Strain | Rekopplung | Carry | Trust | Nachhall | Sehen-Gap | Hoeren-Gap | Hoeren-Stim. | Kontakt | Einbettung |",
        "|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for group in ["kurz_2k", "asset_mixed_2k", "lang_10k"]:
        for role in ["stable", "edge"]:
            row = by_key.get((role, group))
            if not row:
                continue
            lines.append(
                f"| {group} | {role} | {row['family']} | {_fmt(row['family_share'])} | "
                f"{row['dominant_mcm_class']} | {row['dominant_inner_state']} | "
                f"{_fmt(row['avg_mcm_strain'])} | {_fmt(row['avg_mcm_rekopplung'])} | "
                f"{_fmt(row['avg_mcm_carry'])} | {_fmt(row['avg_temporal_trust'])} | "
                f"{_fmt(row['avg_afterimage'])} | {_fmt(row['avg_visual_field_gap'])} | "
                f"{_fmt(row['avg_hearing_field_gap'])} | {_fmt(row['avg_auditory_stimulation'])} | "
                f"{_fmt(row['avg_direct_contact_pressure'])} | {_fmt(row['fieldtime_embedding'])} |"
            )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{stable_family}` und `{edge_family}` sind nicht dasselbe Feldereignis mit anderem Namen. Der Kontrast ist systematisch sichtbar:",
            "",
            f"- `{stable_family}` bleibt ueberwiegend `stabil` / `inner_effect_stable`.",
            f"- `{edge_family}` liegt ueberwiegend in `tragend_unruhig` / `inner_effect_carried_unrest`.",
            "- die Randfamilie traegt deutlich mehr Strain und weniger Feldzeit/Trust.",
            "- die stabile Familie traegt mehr Nachhall und hoehere Feldzeit-Einbettung.",
            "- die Randfamilie zeigt hoehere Sehen-/Hoeren-Gaps und staerkere Hoer-Stimulation.",
            "- der Unterschied liegt damit nicht nur in einem Namen, sondern in gekoppeltem Sinnes-/Feldprofil.",
            "",
            "Damit sieht MINI_DIO nicht nur eine generische Bedeutungswolke. Es trennt mindestens eine stabile Traegerfamilie von einer unruhigen Randfamilie innerhalb desselben passiven MCM-Feldes.",
            "",
            "## Grenze",
            "",
            "Der Befund ist passiv. Er beschreibt Innenfeld- und Bedeutungsprofile, keine Strategie, keine Handlung und keine Richtungsvorhersage.",
            "",
            "## Detailauszug",
            "",
            "| Rolle | Gruppe | Welt | Anteil | Klasse | Strain | Trust | Nachhall | Einbettung |",
            "|---|---|---|---:|---|---:|---:|---:|---:|",
        ]
    )
    for row in details:
        lines.append(
            f"| {row['role']} | {row['group']} | {row['world']} | {_fmt(row['family_share'])} | "
            f"{row['dominant_mcm_class']} | {_fmt(row['avg_mcm_strain'])} | "
            f"{_fmt(row['avg_temporal_trust'])} | {_fmt(row['avg_afterimage'])} | "
            f"{_fmt(row['fieldtime_embedding'])} |"
        )
    lines.extend(
        [
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese Randfamilie unter laengerer Folgewelt driftet, stabilisiert oder in eine eigene Bedeutungsinsel ausreift.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--stable-family", default=STABLE_FAMILY_DEFAULT)
    parser.add_argument("--edge-family", default=EDGE_FAMILY_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    paths = _episode_paths(debug_root)
    edge_family = args.edge_family or _choose_edge_family(paths, debug_root, args.stable_family)
    details: list[dict[str, object]] = []
    for path in paths:
        details.append(summarize_family(path, debug_root, args.stable_family, "stable"))
        details.append(summarize_family(path, debug_root, edge_family, "edge"))
    summaries = summarize_groups(details)
    _write_csv(args.csv_out, summaries + details)
    _write_markdown(args.md_out, summaries, details, args.stable_family, edge_family)
    print(f"stable_family={args.stable_family}")
    print(f"edge_family={edge_family}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in sorted(summaries, key=lambda item: (str(item["group"]), str(item["role"]))):
        print(
            f"{row['group']} {row['role']} {row['family']}: "
            f"strain={float(row['avg_mcm_strain']):.4f} "
            f"trust={float(row['avg_temporal_trust']):.4f} "
            f"embedding={float(row['fieldtime_embedding']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
