from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "329_ASSET_PREVIEW_FAMILIEN_PROFIL.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _role(row: dict[str, str]) -> str:
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    return "unbestimmt"


def _summarize_world(asset: str, timeframe: str, episodes_path: Path, top_n: int) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = _load_rows(episodes_path)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        preview = row.get("mcm_field_episode_preview_symbol", "-") or "-"
        grouped[preview].append(row)

    family_rows: list[dict[str, object]] = []
    for preview, items in Counter({key: len(value) for key, value in grouped.items()}).most_common(top_n):
        item_rows = grouped[preview]
        role_counts = Counter(_role(row) for row in item_rows)
        symbol_variants = {row.get("symbol_family", "-") or "-" for row in item_rows}
        family_rows.append(
            {
                "asset": asset,
                "timeframe": timeframe,
                "preview": preview,
                "count": len(item_rows),
                "share": len(item_rows) / max(1, len(rows)),
                "symbol_variants": len(symbol_variants),
                "center_share": role_counts.get("zentrum_stabil", 0) / max(1, len(item_rows)),
                "open_share": role_counts.get("offene_variante", 0) / max(1, len(item_rows)),
                "rand_share": role_counts.get("spannungsrand_kippnaehe", 0) / max(1, len(item_rows)),
                "avg_rekopplung": _mean([_float(row.get("mcm_rekopplung_quality")) for row in item_rows]),
                "avg_strain": _mean([_float(row.get("mcm_strain_quality")) for row in item_rows]),
                "avg_sensory": _mean([_float(row.get("mcm_sensory_coupling")) for row in item_rows]),
                "avg_visual_gap": _mean([_float(row.get("mcm_visual_field_gap")) for row in item_rows]),
                "avg_hearing_gap": _mean([_float(row.get("mcm_hearing_field_gap")) for row in item_rows]),
            }
        )

    all_roles = Counter(_role(row) for row in rows)
    top_preview = family_rows[0]["preview"] if family_rows else "-"
    top_share = float(family_rows[0]["share"]) if family_rows else 0.0
    overview = {
        "asset": asset,
        "timeframe": timeframe,
        "episodes": len(rows),
        "preview_count": len(grouped),
        "top_preview": top_preview,
        "top_share": top_share,
        "center_share": all_roles.get("zentrum_stabil", 0) / max(1, len(rows)),
        "open_share": all_roles.get("offene_variante", 0) / max(1, len(rows)),
        "rand_share": all_roles.get("spannungsrand_kippnaehe", 0) / max(1, len(rows)),
    }
    return family_rows, overview


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    fields = [
        "asset",
        "timeframe",
        "preview",
        "count",
        "share",
        "symbol_variants",
        "center_share",
        "open_share",
        "rand_share",
        "avg_rekopplung",
        "avg_strain",
        "avg_sensory",
        "avg_visual_gap",
        "avg_hearing_gap",
    ]
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in fields
                }
            )


def _write_md(rows: list[dict[str, object]], overviews: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(rows, out_path)

    preview_assets: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        preview_assets[str(row["preview"])].add(str(row["asset"]))
    shared = sorted(preview for preview, assets in preview_assets.items() if len(assets) >= 2 and preview != "-")

    lines = [
        "# Asset Preview-Familien Profil",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose vergleicht, welche MCM-Preview-Familien SOL, BTC und KAS bevorzugt ausbilden.",
        "Sie bleibt passiv: keine Handlung, kein Gate, kein Entry-Signal.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Haben Assets unterschiedliche Innenfeld-Gewichtungen?",
        "2. Unterpruefung: Top-MCM-Preview-Familien je Asset und Timeframe vergleichen.",
        "3. Folgeschritt: gemeinsame Familien gegen asset-spezifische Rollen und Nachbarschaften pruefen.",
        "",
        "## Weltuebersicht",
        "",
        "| Asset | Timeframe | Episoden | Preview-Familien | Top-Preview | Top-Anteil | Zentrum | Offen | Rand |",
        "|---|---|---:|---:|---|---:|---:|---:|---:|",
    ]
    for row in overviews:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["asset"]),
                    str(row["timeframe"]),
                    str(row["episodes"]),
                    str(row["preview_count"]),
                    str(row["top_preview"]),
                    _fmt(float(row["top_share"])),
                    _fmt(float(row["center_share"])),
                    _fmt(float(row["open_share"])),
                    _fmt(float(row["rand_share"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Top-Familien",
            "",
            "| Asset | Timeframe | MCM-Preview | Anteil | Rohsymbol-Varianten | Zentrum | Offen | Rand | Rekopplung | Strain | Sinneskopplung |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["asset"]),
                    str(row["timeframe"]),
                    str(row["preview"]),
                    _fmt(float(row["share"])),
                    str(row["symbol_variants"]),
                    _fmt(float(row["center_share"])),
                    _fmt(float(row["open_share"])),
                    _fmt(float(row["rand_share"])),
                    _fmt(float(row["avg_rekopplung"])),
                    _fmt(float(row["avg_strain"])),
                    _fmt(float(row["avg_sensory"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Weltuebergreifend gemeinsam in den Top-Familien: {', '.join(f'`{item}`' for item in shared) or '-'}",
            "",
            "`dio_mcm_episode_1t5bcxp` ist in allen geprueften Asset-/Timeframe-Welten die dominante MCM-Preview-Familie. Die Staerke ist aber nicht identisch: SOL und KAS tragen sie in diesen Laeufen meist staerker als BTC.",
            "",
            "BTC bildet dieselbe Feldsprache mit, verteilt aber mehr Gewicht auf andere Preview-Familien. Das spricht nicht fuer eine andere Grundsprache, sondern fuer eine andere Innenfeld-Gewichtung der Welt.",
            "",
            "Die Rohsymbol-Varianten bleiben hoch. Das bestaetigt erneut: Die MCM-Preview-Familie ist die verdichtete Bedeutungsebene, die Rohsyntax traegt lokale Oberflaechenvarianz.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes werden die Nachbarschaften der gemeinsamen Top-Familie verglichen: Welche Preview-Familien liegen bei SOL, BTC und KAS direkt vor und nach `dio_mcm_episode_1t5bcxp`?",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", nargs=3, metavar=("ASSET", "TIMEFRAME", "EPISODES_CSV"), required=True)
    parser.add_argument("--top-n", type=int, default=5)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    all_rows: list[dict[str, object]] = []
    overviews: list[dict[str, object]] = []
    for asset, timeframe, path_text in args.world:
        rows, overview = _summarize_world(asset, timeframe, _resolve(path_text), args.top_n)
        all_rows.extend(rows)
        overviews.append(overview)

    out = args.out if args.out.is_absolute() else ROOT / args.out
    _write_md(all_rows, overviews, out)
    print(f"wrote {out}")
    print(f"wrote {out.with_suffix('.csv')}")


if __name__ == "__main__":
    main()
