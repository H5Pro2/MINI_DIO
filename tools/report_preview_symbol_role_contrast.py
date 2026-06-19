from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs" / "befunde" / "243_MEHRWELT_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "246_PREVIEW_SYMBOL_ROLLENKONTRAST.md"
DEFAULT_SYMBOL = "dio_mcm_episode_02xikfk"


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _load_rows(path: Path, symbol: str) -> list[dict]:
    rows: list[dict] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            if (raw.get("field_symbol", "") or "") != symbol:
                continue
            rows.append(
                {
                    "name": raw.get("name", "-") or "-",
                    "run": int(_float(raw.get("run"))),
                    "ticks": f"{raw.get('tick_start', '-')}-{raw.get('tick_end', '-')}",
                    "local_role": raw.get("local_role", "-") or "-",
                    "effect_class": raw.get("effect_class", "-") or "-",
                    "awareness_state": raw.get("awareness_state", "-") or "-",
                    "field_symbol_share": _float(raw.get("field_symbol_share")),
                    "effect_share": _float(raw.get("effect_share")),
                    "awareness_share": _float(raw.get("awareness_share")),
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


def _write_markdown(rows: list[dict], symbol: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    role_groups: dict[str, list[dict]] = defaultdict(list)
    world_groups: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        role_groups[row["local_role"]].append(row)
        world_groups[row["name"]].append(row)

    lines = [
        "# Preview-Symbol Rollen-Kontrast",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        f"Diese Diagnose isoliert `{symbol}` und prueft, ob dasselbe Feldsymbol je nach lokaler Rolle eine andere Innenfeldwirkung traegt.",
        "",
        "Wichtig: Das ist eine passive Lesung, keine Handlung, kein Gate und keine Runtime-Regel.",
        "",
        "## Gesamtbild",
        "",
        f"- Symbol: `{symbol}`",
        f"- Fenster: `{len(rows)}`",
        f"- Welten: {', '.join(f'`{name}` ({len(items)})' for name, items in sorted(world_groups.items()))}",
        f"- Rollen: {', '.join(f'`{role}` ({len(items)})' for role, items in sorted(role_groups.items()))}",
        "",
        "## Rollenvergleich",
        "",
        "| Rolle | Fenster | Effekt | Awareness | Symbolanteil | Rekopplung | Entlastung | Kipp | Felddruck | Syntaxkonz. |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]

    for role, items in sorted(role_groups.items()):
        lines.append(
            "| "
            + " | ".join(
                [
                    role,
                    str(len(items)),
                    _dominant(items, "effect_class"),
                    _dominant(items, "awareness_state"),
                    _fmt(_avg(items, "field_symbol_share")),
                    _fmt(_avg(items, "rekopplung")),
                    _fmt(_avg(items, "relief")),
                    _fmt(_avg(items, "kipp_pressure")),
                    _fmt(_avg(items, "field_pressure")),
                    _fmt(_avg(items, "syntax_concentration")),
                ]
            )
            + " |"
        )

    strongest = sorted(rows, key=lambda row: row["field_symbol_share"], reverse=True)[:12]
    lines.extend(
        [
            "",
            "## Staerkste Einzelfenster",
            "",
            "| Welt | Lauf | Ticks | Rolle | Anteil | Effekt | Awareness | Kipp | Entlastung |",
            "|---|---:|---|---|---:|---|---|---:|---:|",
        ]
    )
    for row in strongest:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    str(row["run"]),
                    row["ticks"],
                    row["local_role"],
                    _fmt(row["field_symbol_share"]),
                    row["effect_class"],
                    row["awareness_state"],
                    _fmt(row["kipp_pressure"]),
                    _fmt(row["relief"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            f"`{symbol}` ist kein eindimensionaler Wert.",
            "Das Symbol traegt eine gemeinsame Feldnaehe, aber seine Bedeutung wird erst durch Rolle und Innenfeldwirkung konkret.",
            "",
            "Wenn es in `lokal_rekoppelnd` erscheint, liegt der Schwerpunkt auf Stabilisierung und Entlastung.",
            "Wenn es in `lokale_multisensorische_kippnaehe` erscheint, bleibt dieselbe Feldnaehe vorhanden, aber mit groesserer Beweglichkeit und Kippnaehe.",
            "",
            "Damit zeigt die passive Regulation nicht nur ein Symbol, sondern eine Kopplung:",
            "",
            "```text",
            "Feldsymbol + lokale Rolle + Innenfeldwirkung = regulative Lesart",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird geprueft, ob die weniger haeufigen Kippvarianten eine eigene Rand-/Spannungsfamilie bilden.",
            "Dazu werden `dio_mcm_episode_037i64j`, `dio_mcm_episode_0e9ekzq`, `dio_mcm_episode_0eje6op` und `dio_mcm_episode_182yyt2` gemeinsam gegen die Rekopplungsfamilie gestellt.",
            "",
        ]
    )

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--symbol", default=DEFAULT_SYMBOL)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    input_path = args.input if args.input.is_absolute() else ROOT / args.input
    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    rows = _load_rows(input_path, args.symbol)
    _write_markdown(rows, args.symbol, out_path)


if __name__ == "__main__":
    main()
