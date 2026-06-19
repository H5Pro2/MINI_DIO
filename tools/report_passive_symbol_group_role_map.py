from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs" / "befunde" / "253_182Y_FOLGEWELTEN_PREVIEW_SYNTAX_DIAGNOSE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "256_PASSIVE_SYMBOLGRUPPEN_ROLLENKARTE.md"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "256_PASSIVE_SYMBOLGRUPPEN_ROLLENKARTE.csv"

RECOUPLING_SYMBOLS = {
    "dio_mcm_episode_02xikfk",
    "dio_mcm_episode_1t5bcxp",
    "dio_mcm_episode_1r7e52w",
}
EDGE_TENSION_SYMBOLS = {
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


def _group_for(symbol: str) -> str:
    if symbol in RECOUPLING_SYMBOLS:
        return "rekopplungsnaehe"
    if symbol in EDGE_TENSION_SYMBOLS:
        return "randspannung"
    return "offene_variante"


def _dominant(rows: list[dict], key: str) -> str:
    counter = Counter(str(row.get(key, "-") or "-") for row in rows)
    if not counter:
        return "-"
    value, count = counter.most_common(1)[0]
    return f"{value} ({count}/{len(rows)})"


def _avg(rows: list[dict], key: str) -> float:
    if not rows:
        return 0.0
    return sum(_float(row.get(key)) for row in rows) / len(rows)


def _load(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            symbol = raw.get("field_symbol", "-") or "-"
            rows.append(
                {
                    "name": raw.get("name", "-") or "-",
                    "run": raw.get("run", "-") or "-",
                    "tick_start": raw.get("tick_start", "-") or "-",
                    "tick_end": raw.get("tick_end", "-") or "-",
                    "local_role": raw.get("local_role", "-") or "-",
                    "field_symbol": symbol,
                    "symbol_group": _group_for(symbol),
                    "field_symbol_share": _float(raw.get("field_symbol_share")),
                    "effect_class": raw.get("effect_class", "-") or "-",
                    "awareness_state": raw.get("awareness_state", "-") or "-",
                    "syntax_concentration": _float(raw.get("syntax_concentration")),
                    "kipp_pressure": _float(raw.get("kipp_pressure")),
                    "relief": _float(raw.get("relief")),
                    "rekopplung": _float(raw.get("rekopplung")),
                    "field_pressure": _float(raw.get("field_pressure")),
                }
            )
    return rows


def _summaries(rows: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row["symbol_group"]].append(row)

    result: list[dict] = []
    for group, items in sorted(grouped.items()):
        symbols = sorted({row["field_symbol"] for row in items})
        worlds = sorted({row["name"] for row in items})
        result.append(
            {
                "symbol_group": group,
                "windows": len(items),
                "world_count": len(worlds),
                "worlds": ", ".join(worlds),
                "symbol_count": len(symbols),
                "symbols": ", ".join(symbols),
                "dominant_role": _dominant(items, "local_role"),
                "dominant_effect": _dominant(items, "effect_class"),
                "dominant_awareness": _dominant(items, "awareness_state"),
                "avg_rekopplung": _avg(items, "rekopplung"),
                "avg_relief": _avg(items, "relief"),
                "avg_kipp_pressure": _avg(items, "kipp_pressure"),
                "avg_field_pressure": _avg(items, "field_pressure"),
                "avg_symbol_share": _avg(items, "field_symbol_share"),
                "avg_syntax_concentration": _avg(items, "syntax_concentration"),
            }
        )
    return result


def _write_csv(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "symbol_group",
        "windows",
        "world_count",
        "worlds",
        "symbol_count",
        "symbols",
        "dominant_role",
        "dominant_effect",
        "dominant_awareness",
        "avg_rekopplung",
        "avg_relief",
        "avg_kipp_pressure",
        "avg_field_pressure",
        "avg_symbol_share",
        "avg_syntax_concentration",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_md(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Passive Symbolgruppen-Rollenkarte",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose fasst Feld-Episoden-Preview-Symbole nicht als Einzelzeichen, sondern als passive Rollenfamilien zusammen.",
        "Sie prueft, ob Rekopplungsnaehe, Randspannung und offene Varianten getrennte Innenfeldrollen tragen.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und keine Runtime-Regel.",
        "",
        "## Hierarchie",
        "",
        "1. Allgemeine Grundfrage: Welche Rollenfamilien bildet die Feld-Episoden-Syntax?",
        "2. Konkrete Unterpruefung: Wie unterscheiden sich diese Familien in Rekopplung, Entlastung, Kippnaehe und Felddruck?",
        "3. Folgeschritt: Nur stabile Unterschiede weiter beobachten; keine Einzelzeichen mechanisch ueberbewerten.",
        "",
        "## Rollenkarte",
        "",
        "| Symbolgruppe | Fenster | Welten | Zeichen | Dominante Rolle | Effekt | Awareness | Rekopplung | Entlastung | Kipp | Felddruck | Zeichenanteil | Syntaxkonzentration |",
        "|---|---:|---:|---:|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]

    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["symbol_group"]),
                    str(row["windows"]),
                    str(row["world_count"]),
                    str(row["symbol_count"]),
                    str(row["dominant_role"]),
                    str(row["dominant_effect"]),
                    str(row["dominant_awareness"]),
                    _fmt(_float(row["avg_rekopplung"])),
                    _fmt(_float(row["avg_relief"])),
                    _fmt(_float(row["avg_kipp_pressure"])),
                    _fmt(_float(row["avg_field_pressure"])),
                    _fmt(_float(row["avg_symbol_share"])),
                    _fmt(_float(row["avg_syntax_concentration"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "Die bisherige Preview-Syntax trennt sich passiv in Rollenfamilien:",
            "",
            "- `rekopplungsnaehe` ist breit, weltuebergreifend und stabilisierender.",
            "- `randspannung` ist schmaler, kippnaeher und felddruckstaerker.",
            "- `offene_variante` bleibt Beobachtungsraum fuer Zeichen, die noch keiner tragenden Familie zugeordnet sind.",
            "",
            "Damit wird die Forschung weniger fragmentiert: Nicht jedes neue Zeichen ist sofort eine neue Richtung. Zuerst wird es einer Rollenfamilie oder einem offenen Variantenraum zugeordnet.",
            "",
            "## Grenze",
            "",
            "Die Rollenkarte beschreibt nur passive Innenfeldordnung.",
            "Sie beweist keine universelle Topologie und erzeugt keine aktive Regulation.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Rollenkarte gegen eine neue Welt gelegt werden. Grundfrage: bleiben die Gruppenrelationen erhalten, auch wenn die Einzelzeichen wechseln?",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else ROOT / args.input
    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    csv_path = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out

    summaries = _summaries(_load(input_path))
    _write_csv(summaries, csv_path)
    _write_md(summaries, out_path)


if __name__ == "__main__":
    main()
