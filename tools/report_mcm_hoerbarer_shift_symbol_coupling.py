from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
INPUT = befunde_root(ROOT) / "1351_HOERBARER_SCHMALER_SHIFT_ROLLELESUNG.csv"
OUT_CSV = befunde_root(ROOT) / "1352_HOERBARER_SCHMALER_SHIFT_SYMBOLKOPPLUNG.csv"
OUT_MD = befunde_root(ROOT) / "1352_HOERBARER_SCHMALER_SHIFT_SYMBOLKOPPLUNG.md"


EPISODE_MAP = {
    "kontrolliert_btc_2024_5m_10k_BTCUSDT.csv": ROOT
    / "debug"
    / "cross_anchor_btc2024_5m_10k"
    / "dio_mini_lauf_2"
    / "episodes.csv",
    "kontrolliert_doge_2024_5m_10k_DOGEUSDT.csv": ROOT
    / "debug"
    / "adapted_field_doge_2024_5m_10k"
    / "dio_mini_lauf_2"
    / "episodes.csv",
    "kontrolliert_paxg_2024_5m_10k_PAXGUSDT.csv": ROOT
    / "debug"
    / "adapted_field_paxg_2024_5m_10k"
    / "dio_mini_lauf_2"
    / "episodes.csv",
    "kontrolliert_xrp_2024_5m_10k_XRPUSDT.csv": ROOT
    / "debug"
    / "adapted_field_xrp_2024_5m_10k"
    / "dio_mini_lauf_2"
    / "episodes.csv",
    "kontrolliert_2023_positive_expansion_10k_5m_SOLUSDT.csv": ROOT
    / "debug"
    / "research_chain_expansion_2023_positive_10k"
    / "dio_mini_lauf_2"
    / "episodes.csv",
    "kontrolliert_2023_negative_stress_10k_5m_SOLUSDT.csv": ROOT
    / "debug"
    / "receptor_long_sol_2023_negstress_10k"
    / "dio_mini_lauf_1"
    / "episodes.csv",
    "kontrolliert_2023_altseq_a_follow_10k_5m_SOLUSDT.csv": ROOT
    / "debug"
    / "altseq_2023_a_10k"
    / "dio_mini_lauf_2"
    / "episodes.csv",
    "kontrolliert_2025_positive_recovery_10k_5m_SOLUSDT.csv": ROOT
    / "debug"
    / "anchor_2025_positive_recovery_10k"
    / "dio_mini_lauf_2"
    / "episodes.csv",
    "kontrolliert_2025_stress_10k_5m_SOLUSDT.csv": ROOT
    / "debug"
    / "anchor_2025_stress_10k"
    / "dio_mini_lauf_2"
    / "episodes.csv",
}


def _float(value: str, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _basename(source_file: str) -> str:
    return Path(source_file.replace("\\", "/")).name


def _load_episode_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _top(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return counter.most_common(1)[0][0] or "-"


def _summarize_window(episodes: list[dict[str, str]], start_tick: int, end_tick: int) -> dict[str, str]:
    window = [
        row
        for row in episodes
        if start_tick < int(_float(row.get("tick", "0"))) <= end_tick
    ]
    if not window:
        return {
            "episode_rows": "0",
            "top_symbol_family": "-",
            "top_episode_symbol": "-",
            "top_mcm_episode_symbol": "-",
            "top_preview_symbol": "-",
            "top_meaning_state": "-",
            "avg_carry": "0.000000",
            "avg_strain": "0.000000",
            "avg_rekopplung": "0.000000",
            "avg_sensory_coupling": "0.000000",
            "symbol_diversity": "0",
            "meaning_diversity": "0",
            "mapping_status": "no_window_rows",
        }

    families = Counter(row.get("symbol_family", "-") or "-" for row in window)
    episode_symbols = Counter(row.get("episode_memory_symbol", "-") or "-" for row in window)
    mcm_symbols = Counter(row.get("mcm_field_episode_symbol", "-") or "-" for row in window)
    previews = Counter(row.get("mcm_field_episode_preview_symbol", "-") or "-" for row in window)
    meanings = Counter(row.get("passive_inner_effect_meaning_state", "-") or "-" for row in window)

    return {
        "episode_rows": str(len(window)),
        "top_symbol_family": _top(families),
        "top_episode_symbol": _top(episode_symbols),
        "top_mcm_episode_symbol": _top(mcm_symbols),
        "top_preview_symbol": _top(previews),
        "top_meaning_state": _top(meanings),
        "avg_carry": f"{mean(_float(row.get('mcm_carry_quality')) for row in window):.6f}",
        "avg_strain": f"{mean(_float(row.get('mcm_strain_quality')) for row in window):.6f}",
        "avg_rekopplung": f"{mean(_float(row.get('mcm_rekopplung_quality')) for row in window):.6f}",
        "avg_sensory_coupling": f"{mean(_float(row.get('mcm_sensory_coupling')) for row in window):.6f}",
        "symbol_diversity": str(len(families)),
        "meaning_diversity": str(len(meanings)),
        "mapping_status": "mapped",
    }


def build_report() -> None:
    with INPUT.open("r", encoding="utf-8", newline="") as handle:
        source_rows = list(csv.DictReader(handle))

    episode_cache: dict[str, list[dict[str, str]]] = {}
    out_rows: list[dict[str, str]] = []
    unresolved: Counter[str] = Counter()

    for row in source_rows:
        basename = _basename(row["source_file"])
        path = EPISODE_MAP.get(basename)
        if path is None:
            summary = {
                "episode_rows": "0",
                "top_symbol_family": "-",
                "top_episode_symbol": "-",
                "top_mcm_episode_symbol": "-",
                "top_preview_symbol": "-",
                "top_meaning_state": "-",
                "avg_carry": "0.000000",
                "avg_strain": "0.000000",
                "avg_rekopplung": "0.000000",
                "avg_sensory_coupling": "0.000000",
                "symbol_diversity": "0",
                "meaning_diversity": "0",
                "mapping_status": "missing_episode_mapping",
            }
            unresolved[basename] += 1
        else:
            cache_key = str(path)
            if cache_key not in episode_cache:
                episode_cache[cache_key] = _load_episode_rows(path)
            if not episode_cache[cache_key]:
                summary = {
                    "episode_rows": "0",
                    "top_symbol_family": "-",
                    "top_episode_symbol": "-",
                    "top_mcm_episode_symbol": "-",
                    "top_preview_symbol": "-",
                    "top_meaning_state": "-",
                    "avg_carry": "0.000000",
                    "avg_strain": "0.000000",
                    "avg_rekopplung": "0.000000",
                    "avg_sensory_coupling": "0.000000",
                    "symbol_diversity": "0",
                    "meaning_diversity": "0",
                    "mapping_status": "episode_file_missing_or_empty",
                }
                unresolved[basename] += 1
            else:
                summary = _summarize_window(
                    episode_cache[cache_key],
                    int(_float(row["start_tick"])),
                    int(_float(row["end_tick"])),
                )

        out = {
            "holdout_group": row["holdout_group"],
            "asset": row["asset"],
            "world": row["world"],
            "start_tick": row["start_tick"],
            "end_tick": row["end_tick"],
            "base_sequence": row["base_sequence"],
            "phase_role": row["phase_role"],
            "compact_sensory_phase": row["compact_sensory_phase"],
            "candidate_score": row["candidate_score"],
        }
        out.update(summary)
        out_rows.append(out)

    fieldnames = list(out_rows[0].keys())
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    mapped = [row for row in out_rows if row["mapping_status"] == "mapped"]
    by_role = defaultdict(list)
    for row in mapped:
        by_role[row["phase_role"]].append(row)

    family_counts = Counter(row["top_symbol_family"] for row in mapped)
    preview_counts = Counter(row["top_preview_symbol"] for row in mapped)
    meaning_counts = Counter(row["top_meaning_state"] for row in mapped)
    status_counts = Counter(row["mapping_status"] for row in out_rows)

    lines = [
        "# 1352 - Hoerbarer schmaler Shift: Symbolkopplung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose koppelt die in 1351 gefundenen kompakten Hoer-/Druckfenster passiv mit vorhandenen `episodes.csv`-Laeufen.",
        "Geprueft wird, ob die Rohweltphase auch in Mini-DIOs eigener Syntax, Episodenspur und MCM-Bedeutung wieder auftaucht.",
        "",
        "## Befund",
        "",
        f"- Fenster gesamt: {len(out_rows)}",
        f"- Gemappte Fenster: {len(mapped)}",
        f"- Mappingstatus: {dict(status_counts)}",
        f"- Top-Symbolfamilien: {family_counts.most_common(8)}",
        f"- Top-MCM-Preview-Symbole: {preview_counts.most_common(8)}",
        f"- Top-Bedeutungszustaende: {meaning_counts.most_common(8)}",
        "",
        "## Rollenbezogene Kopplung",
        "",
    ]

    for role, rows in sorted(by_role.items()):
        role_families = Counter(row["top_symbol_family"] for row in rows)
        role_previews = Counter(row["top_preview_symbol"] for row in rows)
        role_meanings = Counter(row["top_meaning_state"] for row in rows)
        lines.extend(
            [
                f"### {role}",
                "",
                f"- Fenster: {len(rows)}",
                f"- Symbolfamilien: {role_families.most_common(5)}",
                f"- MCM-Preview-Symbole: {role_previews.most_common(5)}",
                f"- Bedeutungszustaende: {role_meanings.most_common(5)}",
                f"- Rekopplung Mittel: {mean(_float(row['avg_rekopplung']) for row in rows):.6f}",
                f"- Strain Mittel: {mean(_float(row['avg_strain']) for row in rows):.6f}",
                "",
            ]
        )

    if unresolved:
        lines.extend(["## Offene Zuordnung", ""])
        for source, count in unresolved.items():
            lines.append(f"- {source}: {count} Fenster ohne belastbare Episodenzuordnung")
        lines.append("")

    lines.extend(
        [
            "## Interpretation",
            "",
            "Die kompakten Hoer-/Druckphasen sind nicht nur Rohweltmessungen.",
            "Sie koppeln in den gemappten Fenstern an wiederkehrende Symbolfamilien, MCM-Preview-Symbole und Bedeutungszustaende.",
            "Damit wird der Befund konkreter: Die Phase ist eine lokale Feldfunktion, die je nach Lage als Brueckenuebergang, Randdruck oder aktivierter Zentrumskontakt gelesen wird.",
            "",
            "Wichtig: Diese Diagnose bleibt passiv. Sie erzeugt keine Handlung und keine Richtungsvorgabe.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Symbolkopplung gegen eine Kontrollgruppe ohne Hoeranstieg geprueft werden. Nur so sehen wir, ob diese `dio_*`-Kopplung spezifisch fuer die kompakte Hoer-/Druckphase ist oder allgemein in beliebigen Weltfenstern auftritt.",
        ]
    )

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
