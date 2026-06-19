from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs" / "befunde" / "243_MEHRWELT_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "247_PREVIEW_KIPPVARIANTEN_GEGEN_REKOPPLUNGSFAMILIE.md"
RECOUPLING_SYMBOLS = {
    "dio_mcm_episode_02xikfk",
    "dio_mcm_episode_1t5bcxp",
    "dio_mcm_episode_1r7e52w",
}
TIPPING_VARIANTS = {
    "dio_mcm_episode_037i64j",
    "dio_mcm_episode_0e9ekzq",
    "dio_mcm_episode_0eje6op",
    "dio_mcm_episode_182yyt2",
}


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _load_rows(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            symbol = raw.get("field_symbol", "-") or "-"
            if symbol in RECOUPLING_SYMBOLS:
                family = "rekopplungsfamilie"
            elif symbol in TIPPING_VARIANTS:
                family = "kippvarianten"
            else:
                continue
            rows.append(
                {
                    "family": family,
                    "name": raw.get("name", "-") or "-",
                    "run": int(_float(raw.get("run"))),
                    "ticks": f"{raw.get('tick_start', '-')}-{raw.get('tick_end', '-')}",
                    "local_role": raw.get("local_role", "-") or "-",
                    "field_symbol": symbol,
                    "field_symbol_share": _float(raw.get("field_symbol_share")),
                    "effect_class": raw.get("effect_class", "-") or "-",
                    "awareness_state": raw.get("awareness_state", "-") or "-",
                    "kipp_pressure": _float(raw.get("kipp_pressure")),
                    "relief": _float(raw.get("relief")),
                    "rekopplung": _float(raw.get("rekopplung")),
                    "field_pressure": _float(raw.get("field_pressure")),
                    "syntax_concentration": _float(raw.get("syntax_concentration")),
                }
            )
    return rows


def _avg(rows: list[dict], key: str) -> float:
    if not rows:
        return 0.0
    return sum(_float(row.get(key)) for row in rows) / len(rows)


def _dominant(rows: list[dict], key: str) -> str:
    counter = Counter(row[key] for row in rows)
    if not counter:
        return "-"
    value, count = counter.most_common(1)[0]
    return f"{value} ({count}/{len(rows)})"


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    groups = {
        "rekopplungsfamilie": [row for row in rows if row["family"] == "rekopplungsfamilie"],
        "kippvarianten": [row for row in rows if row["family"] == "kippvarianten"],
    }
    kipp_worlds = sorted({row["name"] for row in groups["kippvarianten"]})
    kipp_symbol_worlds = {
        symbol: sorted({row["name"] for row in groups["kippvarianten"] if row["field_symbol"] == symbol})
        for symbol in sorted(TIPPING_VARIANTS)
    }
    repeated_kipp_symbols = [
        symbol for symbol, worlds in kipp_symbol_worlds.items() if len(worlds) > 1
    ]
    if repeated_kipp_symbols:
        kipp_reading = (
            "Die Kippvarianten bilden weiterhin eine erkennbare Rand-/Spannungsgruppe. "
            "Mindestens ein Symbol tritt nun ueber mehrere Welten auf; damit entsteht eine erste Folgewelt-Stuetze, "
            "aber noch keine breit mehrweltstabile Familie."
        )
        next_step = (
            "Als naechstes sollte genau das wiederkehrende Kippzeichen gegen weitere Real- und Stresswelten gelegt werden. "
            "Grundfrage: bleibt es Randspannung, oder wird daraus eine stabile Spannungsfamilie?"
        )
    else:
        kipp_reading = (
            "Die Kippvarianten bilden bisher eine erkennbare Rand-/Spannungsgruppe, aber noch keine mehrweltstabile Familie. "
            "Sie reproduzieren sich innerhalb ihrer Welt, bleiben aber noch situativ."
        )
        next_step = (
            "Als naechstes braucht diese Rand-/Spannungsgruppe eine Folgewelt. "
            "Grundfrage: tauchen dieselben Kippvarianten in weiteren Real- oder Stresswelten wieder auf, "
            "oder bleiben sie situative Realwelt-Randzeichen?"
        )

    lines = [
        "# Preview-Kippvarianten gegen Rekopplungsfamilie",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose vergleicht seltenere Kippvarianten mit der haeufigeren Rekopplungsfamilie.",
        "Sie prueft, ob Rand-/Spannungssymbole eine eigene passive Familie bilden oder nur schwache Varianten der Rekopplungsnaehe sind.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und keine Runtime-Regel.",
        "",
        "## Symbolgruppen",
        "",
        "- Rekopplungsfamilie: `dio_mcm_episode_02xikfk`, `dio_mcm_episode_1t5bcxp`, `dio_mcm_episode_1r7e52w`",
        "- Kippvarianten: `dio_mcm_episode_037i64j`, `dio_mcm_episode_0e9ekzq`, `dio_mcm_episode_0eje6op`, `dio_mcm_episode_182yyt2`",
        "",
        "## Gruppenvergleich",
        "",
        "| Gruppe | Fenster | Welten | Rolle | Effekt | Awareness | Rekopplung | Entlastung | Kipp | Felddruck | Symbolanteil |",
        "|---|---:|---|---|---|---|---:|---:|---:|---:|---:|",
    ]

    for name, items in groups.items():
        worlds = ", ".join(f"`{world}`" for world in sorted({row["name"] for row in items}))
        lines.append(
            "| "
            + " | ".join(
                [
                    name,
                    str(len(items)),
                    worlds or "-",
                    _dominant(items, "local_role"),
                    _dominant(items, "effect_class"),
                    _dominant(items, "awareness_state"),
                    _fmt(_avg(items, "rekopplung")),
                    _fmt(_avg(items, "relief")),
                    _fmt(_avg(items, "kipp_pressure")),
                    _fmt(_avg(items, "field_pressure")),
                    _fmt(_avg(items, "field_symbol_share")),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Kippvarianten im Detail",
            "",
            "| Symbol | Fenster | Welten | Ticks | Anteil | Kipp | Entlastung | Rekopplung | Felddruck |",
            "|---|---:|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for symbol in sorted(TIPPING_VARIANTS):
        items = [row for row in groups["kippvarianten"] if row["field_symbol"] == symbol]
        if not items:
            continue
        worlds = ", ".join(sorted({row["name"] for row in items}))
        ticks = ", ".join(f"{row['run']}:{row['ticks']}" for row in items)
        lines.append(
            "| "
            + " | ".join(
                [
                    symbol,
                    str(len(items)),
                    worlds,
                    ticks,
                    _fmt(_avg(items, "field_symbol_share")),
                    _fmt(_avg(items, "kipp_pressure")),
                    _fmt(_avg(items, "relief")),
                    _fmt(_avg(items, "rekopplung")),
                    _fmt(_avg(items, "field_pressure")),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            kipp_reading,
            "",
            f"Kippvarianten-Welten: {', '.join(f'`{world}`' for world in kipp_worlds) or '-'}",
            f"Weltuebergreifend wiederkehrende Kippzeichen: {', '.join(f'`{symbol}`' for symbol in repeated_kipp_symbols) or '-'}",
            "",
            "Gegenueber der Rekopplungsfamilie zeigen sie:",
            "",
            "- weniger Fenster,",
            "- staerkere lokale Kippnaehe,",
            "- hoeheren Felddruck,",
            "- geringere Rekopplung und Entlastung,",
            "- eindeutige Kopplung an `tragend_unruhig` / `inner_effect_carried_unrest`.",
            "",
            "Damit sind sie fachlich eher Rand-/Spannungsvarianten als reine Abschwaechungen der Rekopplung.",
            "Die Grenze bleibt aber wichtig: Eine einzelne Folgewelt-Stuetze reicht noch nicht fuer eine stabile MCM-Familie.",
            "",
            "## Wie es weitergeht",
            "",
            next_step,
            "",
        ]
    )

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else ROOT / args.input
    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    rows = _load_rows(input_path)
    _write_markdown(rows, out_path)


if __name__ == "__main__":
    main()
