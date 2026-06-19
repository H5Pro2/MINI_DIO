from __future__ import annotations

import argparse
import csv
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_OUT = ROOT / "docs" / "befunde" / "269_WELTRELATIVE_TOPOLOGIE_MATRIX.md"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "269_WELTRELATIVE_TOPOLOGIE_MATRIX.csv"

DEFAULT_WORLDS = [
    (
        "SOL_2024_5M_2K",
        "debug/verify_world_relative_sol_2024_5m_01/dio_mini_lauf_2/episodes.csv",
    ),
    (
        "SOL_2024_1H_2K",
        "debug/verify_world_relative_sol_2024_1h_01/dio_mini_lauf_2/episodes.csv",
    ),
    (
        "BTC_2024_5M_2K",
        "debug/verify_world_relative_btc_2024_5m_01/dio_mini_lauf_2/episodes.csv",
    ),
    (
        "BTC_2024_1H_2K",
        "debug/verify_world_relative_btc_2024_1h_01/dio_mini_lauf_2/episodes.csv",
    ),
]


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(_float(item) for item in values)
    index = (len(ordered) - 1) * q
    lower = int(index)
    upper = min(len(ordered) - 1, lower + 1)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] * (upper - index) + ordered[upper] * (index - lower)


def _dominant(values: list[str]) -> str:
    cleaned = [str(value or "-") for value in values if str(value or "-") != "-"]
    if not cleaned:
        return "-"
    return Counter(cleaned).most_common(1)[0][0]


def _primary_topology_role(row: dict[str, str]) -> str:
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    strain_quality = _float(row.get("mcm_strain_quality"))
    rekopplung_quality = _float(row.get("mcm_rekopplung_quality"))
    sensory_coupling = _float(row.get("mcm_sensory_coupling"))

    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    if rekopplung_quality >= 0.58 and strain_quality <= 0.26 and sensory_coupling >= 0.70:
        return "rekopplungsnaehe"
    if strain_quality >= 0.28:
        return "spannungsrand_kippnaehe"
    return "unbestimmt"


def _load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _summarize_world(name: str, rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], dict[str, object]]:
    if not rows:
        return [], {
            "world": name,
            "episodes": 0,
            "topology_state": "keine_daten",
            "center_share": 0.0,
            "open_share": 0.0,
            "rand_share": 0.0,
            "rekopplung_overlay_share": 0.0,
        }

    for row in rows:
        row["_topology_role"] = _primary_topology_role(row)

    rekopplung_values = [_float(row.get("mcm_rekopplung_quality")) for row in rows]
    carry_values = [_float(row.get("mcm_carry_quality")) for row in rows]
    strain_values = [_float(row.get("mcm_strain_quality")) for row in rows]
    rekopplung_top = _percentile(rekopplung_values, 0.75)
    carry_top = _percentile(carry_values, 0.75)
    strain_top = _percentile(strain_values, 0.75)

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("_topology_role", "unbestimmt"))].append(row)

    role_rows: list[dict[str, object]] = []
    total = len(rows)
    for role in [
        "zentrum_stabil",
        "rekopplungsnaehe",
        "offene_variante",
        "spannungsrand_kippnaehe",
        "unbestimmt",
    ]:
        items = grouped.get(role, [])
        if not items:
            continue
        role_rows.append(
            {
                "world": name,
                "role": role,
                "count": len(items),
                "share": len(items) / max(1, total),
                "avg_rekopplung": _mean([_float(item.get("mcm_rekopplung_quality")) for item in items]),
                "avg_carry": _mean([_float(item.get("mcm_carry_quality")) for item in items]),
                "avg_strain": _mean([_float(item.get("mcm_strain_quality")) for item in items]),
                "avg_sensory": _mean([_float(item.get("mcm_sensory_coupling")) for item in items]),
                "avg_visual_gap": _mean([_float(item.get("mcm_visual_field_gap")) for item in items]),
                "avg_hearing_gap": _mean([_float(item.get("mcm_hearing_field_gap")) for item in items]),
                "rekopplung_top_share": sum(
                    1 for item in items if _float(item.get("mcm_rekopplung_quality")) >= rekopplung_top
                )
                / max(1, len(items)),
                "carry_top_share": sum(1 for item in items if _float(item.get("mcm_carry_quality")) >= carry_top)
                / max(1, len(items)),
                "strain_top_share": sum(1 for item in items if _float(item.get("mcm_strain_quality")) >= strain_top)
                / max(1, len(items)),
                "dominant_effect_class": _dominant([item.get("passive_mcm_effect_class", "-") for item in items]),
                "dominant_awareness": _dominant(
                    [item.get("passive_inner_effect_awareness_state", "-") for item in items]
                ),
                "dominant_preview_symbol": _dominant(
                    [item.get("mcm_field_episode_preview_symbol", "-") for item in items]
                ),
                "dominant_symbol_family": _dominant([item.get("symbol_family", "-") for item in items]),
            }
        )

    center_share = sum(1 for row in rows if row.get("_topology_role") == "zentrum_stabil") / max(1, total)
    open_share = sum(1 for row in rows if row.get("_topology_role") == "offene_variante") / max(1, total)
    rand_share = sum(1 for row in rows if row.get("_topology_role") == "spannungsrand_kippnaehe") / max(1, total)
    rekopplung_overlay_share = sum(
        1
        for row in rows
        if _float(row.get("mcm_rekopplung_quality")) >= rekopplung_top
        and _float(row.get("mcm_strain_quality")) <= strain_top
    ) / max(1, total)

    if center_share >= 0.70 and rand_share >= 0.02 and open_share >= 0.05:
        topology_state = "zentrum_mit_rand_und_uebergang"
    elif center_share >= 0.80 and rand_share < 0.02:
        topology_state = "stark_zentriert_wenig_rand"
    elif rand_share >= 0.25:
        topology_state = "randlastig_angespannt"
    else:
        topology_state = "gemischte_rollenordnung"

    summary = {
        "world": name,
        "episodes": total,
        "topology_state": topology_state,
        "center_share": center_share,
        "open_share": open_share,
        "rand_share": rand_share,
        "rekopplung_overlay_share": rekopplung_overlay_share,
        "avg_rekopplung": _mean(rekopplung_values),
        "avg_carry": _mean(carry_values),
        "avg_strain": _mean(strain_values),
        "avg_sensory": _mean([_float(row.get("mcm_sensory_coupling")) for row in rows]),
    }
    return role_rows, summary


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "role",
        "count",
        "share",
        "avg_rekopplung",
        "avg_carry",
        "avg_strain",
        "avg_sensory",
        "avg_visual_gap",
        "avg_hearing_gap",
        "rekopplung_top_share",
        "carry_top_share",
        "strain_top_share",
        "dominant_effect_class",
        "dominant_awareness",
        "dominant_preview_symbol",
        "dominant_symbol_family",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(role_rows: list[dict[str, object]], summaries: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Weltrelative Topologie-Matrix",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob MINI_DIO unter `world_relative` weiterhin eine passive Topologie ausbildet.",
        "Die Topologie wird nicht ueber feste `dio_*`-Namen gelesen.",
        "Gelesen werden Rollenqualitaeten aus Innenfeldwirkung, Rekopplung, Carry, Strain und Sinnes-MCM-Kopplung.",
        "",
        "Die Diagnose erzeugt keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Bleibt eine Rollen-Topologie sichtbar, wenn die Sinnesaufnahme weltrelativ wird?",
        "2. Unterpruefung: Welche Rollenanteile tragen Zentrum, Rand/Kippnaehe, offene Variante und Rekopplungsnaehe?",
        "3. Folgeschritt: Vergleich gegen ruhigere, laengere und staerker gespannte Welten.",
        "",
        "## Kurzbefund",
        "",
        "| Welt | Episoden | Topologiezustand | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for summary in summaries:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(summary["world"]),
                    str(summary["episodes"]),
                    str(summary["topology_state"]),
                    _fmt(_float(summary["center_share"])),
                    _fmt(_float(summary["open_share"])),
                    _fmt(_float(summary["rand_share"])),
                    _fmt(_float(summary["rekopplung_overlay_share"])),
                    _fmt(_float(summary["avg_rekopplung"])),
                    _fmt(_float(summary["avg_carry"])),
                    _fmt(_float(summary["avg_strain"])),
                    _fmt(_float(summary["avg_sensory"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Rollenmatrix",
            "",
            "| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
        ]
    )
    for row in role_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["role"]),
                    _fmt(_float(row["share"])),
                    _fmt(_float(row["avg_rekopplung"])),
                    _fmt(_float(row["avg_carry"])),
                    _fmt(_float(row["avg_strain"])),
                    _fmt(_float(row["avg_sensory"])),
                    _fmt(_float(row["rekopplung_top_share"])),
                    _fmt(_float(row["strain_top_share"])),
                    str(row["dominant_preview_symbol"]),
                    str(row["dominant_symbol_family"]),
                ]
            )
            + " |"
        )

    center_worlds = sum(1 for item in summaries if str(item["topology_state"]).startswith("zentrum"))
    mixed_worlds = sum(1 for item in summaries if item["topology_state"] == "gemischte_rollenordnung")
    rand_worlds = sum(1 for item in summaries if item["topology_state"] == "randlastig_angespannt")
    lines.extend(
        [
            "",
            "## Lesart",
            "",
            f"Zentrumsnahe Welten: {center_worlds}",
            f"Gemischte Rollenordnung: {mixed_worlds}",
            f"Randlastige Welten: {rand_worlds}",
            "",
            "Die aktuelle Matrix spricht fuer eine Rollen-Topologie, nicht fuer eine starre geometrische Form.",
            "",
            "```text",
            "Zentrum      = stabile Innenfeldwirkung",
            "Rand/Kipp    = lokale Spannung und Bruchnaehe",
            "Offen        = tragende, aber noch nicht fest gereifte Variante",
            "Rekopplung   = Qualitaet, die Zentrum und Uebergang stabilisiert",
            "```",
            "",
            "Wichtig: Die numerischen Einteilungen sind Diagnosehilfen.",
            "Sie sind keine Regeln fuer MINI_DIO und keine universellen MCM-Grenzen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieselbe Matrix auf lange ruhige Welten, Stresswelten und Expansionswelten gelegt werden.",
            "Ziel ist zu pruefen, ob `zentrum_mit_rand_und_uebergang` stabil bleibt, ob Randspannung bei Stress sichtbar zunimmt oder ob neue Mischklassen entstehen.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--world",
        action="append",
        nargs=2,
        metavar=("NAME", "EPISODES_CSV"),
        help="World label and matching world_relative episodes csv.",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    worlds = args.world or DEFAULT_WORLDS
    all_role_rows: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []
    for name, raw_path in worlds:
        path = Path(raw_path)
        if not path.is_absolute():
            path = ROOT / path
        role_rows, summary = _summarize_world(name, _load_rows(path))
        all_role_rows.extend(role_rows)
        summaries.append(summary)

    out = args.out if args.out.is_absolute() else ROOT / args.out
    csv_out = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    _write_csv(all_role_rows, csv_out)
    _write_md(all_role_rows, summaries, out)
    print(f"wrote {out}")
    print(f"wrote {csv_out}")


if __name__ == "__main__":
    main()
