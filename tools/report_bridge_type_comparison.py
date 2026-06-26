from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_fieldtime_controlled"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "818_BLOCK_K_BRUECKENTYPEN_VERGLEICH.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "818_BLOCK_K_BRUECKENTYPEN_VERGLEICH.md"
EDGE_FAMILY_DEFAULT = "dio_1un4"
BRIDGE_FAMILIES_DEFAULT = "dio_155c,dio_0m9z,dio_17ct,dio_0h9h,dio_1mwv,dio_0obq"


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


def _summarize_context(rows: list[dict[str, str]]) -> dict[str, object]:
    classes = Counter(str(row.get("passive_mcm_effect_class") or "-") for row in rows)
    return {
        "ticks": len(rows),
        "dominant_class": _dominant(classes),
        "stable_share": classes.get("stabil", 0) / max(1, len(rows)),
        "unrest_share": classes.get("tragend_unruhig", 0) / max(1, len(rows)),
        "avg_strain": _mean([_safe_float(row.get("mcm_strain_quality")) for row in rows]),
        "avg_trust": _mean([_safe_float(row.get("mini_temporal_trust_support")) for row in rows]),
        "avg_afterimage": _mean([_safe_float(row.get("mini_afterimage")) for row in rows]),
        "avg_rekopplung": _mean([_safe_float(row.get("mcm_rekopplung_quality")) for row in rows]),
        "avg_hearing_stimulation": _mean(
            [_safe_float(row.get("rezeptor_auditory_stimulation")) for row in rows]
        ),
        "fieldtime_embedding": _embedding(rows),
    }


def _classify_bridge(before_ticks: int, after_ticks: int, near: dict[str, object], normal: dict[str, object]) -> str:
    near_ticks = int(near["ticks"])
    if near_ticks <= 0:
        return "nicht_gekoppelt"
    stable_near = float(near["stable_share"])
    trust_delta = float(near["avg_trust"]) - float(normal["avg_trust"])
    strain_delta = float(near["avg_strain"]) - float(normal["avg_strain"])
    if before_ticks > 0 and after_ticks > 0 and stable_near >= 0.90 and trust_delta >= -0.03:
        if abs(strain_delta) <= 0.02:
            return "balancierte_bruecke"
        if strain_delta < -0.02:
            return "entlastende_bruecke"
        return "spannungsnahe_bruecke"
    if before_ticks > 0 and after_ticks == 0:
        return "vorfeld_anker"
    if before_ticks == 0 and after_ticks > 0:
        return "nachfeld_anker"
    if stable_near < 0.70:
        return "instabile_kontaktzone"
    return "offene_bruecke"


def summarize_family(debug_root: Path, family: str, edge_family: str) -> dict[str, object]:
    contexts: dict[str, list[dict[str, str]]] = defaultdict(list)
    total_rows: list[dict[str, str]] = []
    before_worlds = Counter()
    after_worlds = Counter()
    for path in _episode_paths(debug_root):
        world = path.parent.parent.name
        rows = _read_rows(path)
        for index, row in enumerate(rows):
            if str(row.get("symbol_family") or "") != family:
                continue
            total_rows.append(row)
            prev_family = str(rows[index - 1].get("symbol_family") or "-") if index > 0 else "-"
            next_family = str(rows[index + 1].get("symbol_family") or "-") if index + 1 < len(rows) else "-"
            if next_family == edge_family:
                contexts["before_edge"].append(row)
                contexts["near_edge"].append(row)
                before_worlds[world] += 1
            if prev_family == edge_family:
                contexts["after_edge"].append(row)
                contexts["near_edge"].append(row)
                after_worlds[world] += 1
            if prev_family != edge_family and next_family != edge_family:
                contexts["normal"].append(row)
    normal = _summarize_context(contexts["normal"])
    near = _summarize_context(contexts["near_edge"])
    before = _summarize_context(contexts["before_edge"])
    after = _summarize_context(contexts["after_edge"])
    all_summary = _summarize_context(total_rows)
    bridge_type = _classify_bridge(int(before["ticks"]), int(after["ticks"]), near, normal)
    return {
        "family": family,
        "bridge_type": bridge_type,
        "total_ticks": len(total_rows),
        "near_ticks": near["ticks"],
        "before_ticks": before["ticks"],
        "after_ticks": after["ticks"],
        "before_worlds": ",".join(f"{key}:{value}" for key, value in before_worlds.most_common()),
        "after_worlds": ",".join(f"{key}:{value}" for key, value in after_worlds.most_common()),
        "all_stable_share": all_summary["stable_share"],
        "all_unrest_share": all_summary["unrest_share"],
        "normal_stable_share": normal["stable_share"],
        "near_stable_share": near["stable_share"],
        "normal_strain": normal["avg_strain"],
        "near_strain": near["avg_strain"],
        "strain_delta": float(near["avg_strain"]) - float(normal["avg_strain"]),
        "normal_trust": normal["avg_trust"],
        "near_trust": near["avg_trust"],
        "trust_delta": float(near["avg_trust"]) - float(normal["avg_trust"]),
        "normal_afterimage": normal["avg_afterimage"],
        "near_afterimage": near["avg_afterimage"],
        "normal_embedding": normal["fieldtime_embedding"],
        "near_embedding": near["fieldtime_embedding"],
        "embedding_delta": float(near["fieldtime_embedding"]) - float(normal["fieldtime_embedding"]),
        "normal_hearing_stimulation": normal["avg_hearing_stimulation"],
        "near_hearing_stimulation": near["avg_hearing_stimulation"],
        "before_trust": before["avg_trust"],
        "after_trust": after["avg_trust"],
        "before_stable_share": before["stable_share"],
        "after_stable_share": after["stable_share"],
    }


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


def _write_markdown(path: Path, rows: list[dict[str, object]], edge_family: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# 818 - Block-K Brueckentypen-Vergleich zu {edge_family}",
        "",
        "## Fragestellung",
        "",
        f"Bilden die stabilen Nachbarfamilien von `{edge_family}` einen gemeinsamen Brueckentyp oder mehrere unterschiedliche Uebergangsarten?",
        "",
        "## Vergleich",
        "",
        "| Familie | Brueckentyp | Gesamt | Near | Vorher | Nachher | Stabil all | Stabil near | Strain Delta | Trust Delta | Einbettung Delta |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['family']} | {row['bridge_type']} | {row['total_ticks']} | {row['near_ticks']} | "
            f"{row['before_ticks']} | {row['after_ticks']} | {_fmt(row['all_stable_share'])} | "
            f"{_fmt(row['near_stable_share'])} | {_fmt(row['strain_delta'])} | "
            f"{_fmt(row['trust_delta'])} | {_fmt(row['embedding_delta'])} |"
        )
    bridge_counter = Counter(str(row["bridge_type"]) for row in rows)
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Die Brueckenfamilien um `{edge_family}` bilden keinen komplett einheitlichen Typ, aber sie teilen einen Kern: Randnaehe fuehrt nicht automatisch zu Kollaps.",
            "",
        ]
    )
    for key, value in bridge_counter.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "Gemeinsame Lesung:",
            "",
            "- stabile Bruecken behalten in Randnaehe ueberwiegend ihre Stabilitaet,",
            "- Vorher-/Nachher-Verteilung unterscheidet die Rolle: manche wirken als Vorfeldanker, andere als Nachfeldanker, einige als echte beidseitige Bruecke,",
            "- Trust-Delta und Strain-Delta zeigen, ob Randnaehe belastet, neutral bleibt oder entlastet,",
            "- damit wirkt die MCM-Topologie nicht wie eine einzelne Linie, sondern wie mehrere Uebergangsarten zwischen Randspannung und stabileren Bedeutungsraeumen.",
            "",
            "## Grenze",
            "",
            "Der Befund ist passiv. Er beschreibt Brueckentypen im Innenfeld, keine Handlung und keine Richtung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus diesen Brueckentypen eine kompakte MCM-Uebergangskarte gebaut werden: Randfamilie, Vorfeldanker, beidseitige Bruecke, Nachfeldanker, stabile Mitte.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--edge-family", default=EDGE_FAMILY_DEFAULT)
    parser.add_argument("--families", default=BRIDGE_FAMILIES_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    families = [item.strip() for item in args.families.split(",") if item.strip()]
    rows = [summarize_family(debug_root, family, args.edge_family) for family in families]
    _write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows, args.edge_family)
    print(f"edge_family={args.edge_family}")
    print(f"families={len(rows)}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in rows:
        print(
            f"{row['family']}: {row['bridge_type']} near={row['near_ticks']} "
            f"stable_near={float(row['near_stable_share']):.4f} "
            f"trust_delta={float(row['trust_delta']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
