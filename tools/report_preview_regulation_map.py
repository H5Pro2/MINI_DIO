from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs" / "befunde" / "243_MEHRWELT_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "245_PASSIVE_PREVIEW_REGULATIONSKARTE.md"


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
            rows.append(
                {
                    "name": raw.get("name", "-") or "-",
                    "run": int(_float(raw.get("run"))),
                    "ticks": f"{raw.get('tick_start', '-')}-{raw.get('tick_end', '-')}",
                    "local_role": raw.get("local_role", "-") or "-",
                    "field_symbol": raw.get("field_symbol", "-") or "-",
                    "field_symbol_share": _float(raw.get("field_symbol_share")),
                    "effect_class": raw.get("effect_class", "-") or "-",
                    "effect_share": _float(raw.get("effect_share")),
                    "awareness_state": raw.get("awareness_state", "-") or "-",
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


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    value, count = counter.most_common(1)[0]
    total = sum(counter.values()) or 1
    return f"{value} ({count}/{total})"


def _regulation_reading(rows: list[dict]) -> str:
    effect_counter = Counter(row["effect_class"] for row in rows)
    role_counter = Counter(row["local_role"] for row in rows)
    avg_relief = _avg(rows, "relief")
    avg_kipp = _avg(rows, "kipp_pressure")
    avg_field_pressure = _avg(rows, "field_pressure")
    dominant_effect = effect_counter.most_common(1)[0][0] if effect_counter else "-"
    dominant_role = role_counter.most_common(1)[0][0] if role_counter else "-"

    if dominant_effect == "stabil" and dominant_role == "lokal_rekoppelnd" and avg_relief >= avg_kipp:
        return "rekoppelnd_stabilisierend"
    if dominant_effect == "tragend_unruhig" and avg_kipp >= avg_relief * 0.30:
        return "tragend_unruhig"
    if dominant_effect in {"gespannt", "kippend"} or avg_field_pressure > 0.24:
        return "spannungsnah"
    if dominant_role == "lokale_multisensorische_kippnaehe":
        return "kippnah_variant"
    return "offen_uneindeutig"


def _write_csv(symbol_rows: list[dict], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "field_symbol",
                "count",
                "worlds",
                "roles",
                "dominant_role",
                "dominant_effect",
                "dominant_awareness",
                "avg_field_symbol_share",
                "avg_syntax_concentration",
                "avg_rekopplung",
                "avg_relief",
                "avg_kipp_pressure",
                "avg_field_pressure",
                "regulation_reading",
            ],
        )
        writer.writeheader()
        for row in symbol_rows:
            writer.writerow(row)


def _summarize(rows: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row["field_symbol"]].append(row)

    symbol_rows: list[dict] = []
    for symbol, items in grouped.items():
        role_counter = Counter(item["local_role"] for item in items)
        effect_counter = Counter(item["effect_class"] for item in items)
        awareness_counter = Counter(item["awareness_state"] for item in items)
        worlds = sorted({item["name"] for item in items})
        symbol_rows.append(
            {
                "field_symbol": symbol,
                "count": len(items),
                "worlds": ", ".join(worlds),
                "roles": ", ".join(f"{role}:{count}" for role, count in role_counter.most_common()),
                "dominant_role": _dominant(role_counter),
                "dominant_effect": _dominant(effect_counter),
                "dominant_awareness": _dominant(awareness_counter),
                "avg_field_symbol_share": _fmt(_avg(items, "field_symbol_share")),
                "avg_syntax_concentration": _fmt(_avg(items, "syntax_concentration")),
                "avg_rekopplung": _fmt(_avg(items, "rekopplung")),
                "avg_relief": _fmt(_avg(items, "relief")),
                "avg_kipp_pressure": _fmt(_avg(items, "kipp_pressure")),
                "avg_field_pressure": _fmt(_avg(items, "field_pressure")),
                "regulation_reading": _regulation_reading(items),
            }
        )
    return sorted(symbol_rows, key=lambda row: (int(row["count"]), float(row["avg_field_symbol_share"])), reverse=True)


def _write_markdown(rows: list[dict], symbol_rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(symbol_rows, out_path)

    role_counter = Counter(row["local_role"] for row in rows)
    reading_counter = Counter(row["regulation_reading"] for row in symbol_rows)
    top = symbol_rows[:12]

    lines = [
        "# Passive Preview-Regulationskarte",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die lokalen Feld-Episoden-Vorschau-Symbole als passive Regulationskarte.",
        "Sie fragt nicht, was MINI_DIO tun soll, sondern welche Vorschau-Feldlagen mit Stabilisierung, Unruhe, Kippnaehe oder Rekopplung gekoppelt sind.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate, kein Entry-Signal und keine Runtime-Regel.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Welche Feldsymbole tragen regulative Innenfeldwirkung?",
        "2. Unterpruefung: Feldsymbol gegen lokale Rolle, Effektklasse, Awareness, Rekopplung, Entlastung und Kippnaehe legen.",
        "3. Folgeschritt: Wiederkehrende Feldsymbole spaeter gegen weitere Welten pruefen.",
        "",
        "## Datenbasis",
        "",
        f"- Fenster gesamt: `{len(rows)}`",
        f"- Feldsymbole: `{len(symbol_rows)}`",
        f"- Rollen: {', '.join(f'`{role}` ({count})' for role, count in role_counter.most_common())}",
        f"- Regulationslesarten: {', '.join(f'`{reading}` ({count})' for reading, count in reading_counter.most_common())}",
        "",
        "## Staerkste Feldsymbole",
        "",
        "| Feldsymbol | Fenster | Welten | Rolle | Effekt | Awareness | Rekopplung | Entlastung | Kipp | Felddruck | Lesart |",
        "|---|---:|---|---|---|---|---:|---:|---:|---:|---|",
    ]

    for row in top:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["field_symbol"],
                    str(row["count"]),
                    row["worlds"],
                    row["dominant_role"],
                    row["dominant_effect"],
                    row["dominant_awareness"],
                    row["avg_rekopplung"],
                    row["avg_relief"],
                    row["avg_kipp_pressure"],
                    row["avg_field_pressure"],
                    row["regulation_reading"],
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Vorlaeufige Lesart",
            "",
            "`dio_mcm_episode_02xikfk` ist derzeit die wichtigste gemeinsame Vorschau-Feldlage.",
            "Sie tritt in mehreren Welten und besonders in lokalen Rekopplungsfenstern auf.",
            "Das spricht fuer eine passive rekoppelnd-stabilisierende Innenfeldnaehe.",
            "",
            "Kippnahe und weltbezogene Varianten bleiben beweglicher.",
            "Dort ist nicht allein das Feldsymbol entscheidend, sondern seine Kopplung an Rolle, Weltspannung und aktuelle Innenfeldwirkung.",
            "",
            "## Grenze",
            "",
            "Diese Karte beschreibt Regulation nur als beobachtete Feldorganisation.",
            "Sie darf nicht als aktives Kontrollsystem, Handlungsvorgabe oder Beweis fuer eine fertige Bedeutungsstruktur gelesen werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird `dio_mcm_episode_02xikfk` isoliert.",
            "Dabei werden Rekopplungsfenster mit diesem Symbol gegen Kippfenster mit demselben Symbol verglichen.",
            "Ziel ist zu pruefen, ob dasselbe Feldsymbol je nach Rolle eine andere Innenfeldwirkung traegt.",
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
    symbol_rows = _summarize(rows)
    _write_markdown(rows, symbol_rows, out_path)


if __name__ == "__main__":
    main()
