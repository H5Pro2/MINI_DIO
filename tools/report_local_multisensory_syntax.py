from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

from report_auditory_regulation import DEFAULT_SUMMARIES
from report_auditory_regulation import _fmt
from report_recoupling_quality import _resolve


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCAL_WINDOWS = ROOT / "docs" / "befunde" / "234_LOKALE_MULTISENSORISCHE_KOPPLUNG_DIAGNOSE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "236_LOKALE_MULTISENSORISCHE_SYNTAX_DIAGNOSE.md"


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _episode_file(summary_path: Path, run_index: int) -> Path:
    files = sorted(summary_path.parent.glob("dio_mini_lauf_*/episodes.csv"))
    if run_index < 1 or run_index > len(files):
        raise FileNotFoundError(f"Kein episodes.csv fuer Lauf {run_index} in {summary_path.parent}")
    return files[run_index - 1]


def _load_windows(path: Path, roles: set[str]) -> list[dict]:
    rows: list[dict] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            if raw.get("local_role") not in roles:
                continue
            rows.append(
                {
                    "name": raw.get("name", ""),
                    "group": raw.get("group", ""),
                    "run": int(_float(raw.get("run"))),
                    "tick_start": int(_float(raw.get("tick_start"))),
                    "tick_end": int(_float(raw.get("tick_end"))),
                    "local_role": raw.get("local_role", ""),
                    "kipp_pressure": _float(raw.get("kipp_pressure")),
                    "relief": _float(raw.get("relief")),
                    "rekopplung": _float(raw.get("rekopplung")),
                    "field_pressure": _float(raw.get("field_pressure")),
                }
            )
    return rows


def _dominant(counter: Counter[str]) -> tuple[str, float, int]:
    total = sum(counter.values())
    if not total:
        return "-", 0.0, 0
    value, count = counter.most_common(1)[0]
    return value or "-", count / total, total


def _window_syntax(window: dict, summary_map: dict[str, Path]) -> dict:
    episode_path = _episode_file(summary_map[window["name"]], window["run"])
    symbol_counter: Counter[str] = Counter()
    family_counter: Counter[str] = Counter()
    field_symbol_counter: Counter[str] = Counter()
    effect_counter: Counter[str] = Counter()
    awareness_counter: Counter[str] = Counter()
    rows_seen = 0

    with episode_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            tick = int(_float(raw.get("tick")))
            if tick < window["tick_start"] or tick > window["tick_end"]:
                continue
            rows_seen += 1
            symbol_counter[raw.get("symbol", "-") or "-"] += 1
            family_counter[raw.get("symbol_family", "-") or "-"] += 1
            field_symbol = raw.get("mcm_field_episode_preview_symbol", "") or raw.get("mcm_field_episode_symbol", "-") or "-"
            field_symbol_counter[field_symbol] += 1
            effect_counter[raw.get("passive_mcm_effect_class", "-") or "-"] += 1
            awareness_counter[raw.get("passive_inner_effect_awareness_state", "-") or "-"] += 1

    symbol, symbol_share, _ = _dominant(symbol_counter)
    family, family_share, _ = _dominant(family_counter)
    field_symbol, field_symbol_share, _ = _dominant(field_symbol_counter)
    effect, effect_share, _ = _dominant(effect_counter)
    awareness, awareness_share, _ = _dominant(awareness_counter)
    syntax_concentration = (symbol_share * 0.26) + (family_share * 0.24) + (field_symbol_share * 0.24) + (effect_share * 0.14) + (awareness_share * 0.12)

    return {
        **window,
        "rows": rows_seen,
        "symbol": symbol,
        "symbol_share": symbol_share,
        "symbol_family": family,
        "symbol_family_share": family_share,
        "field_symbol": field_symbol,
        "field_symbol_share": field_symbol_share,
        "effect_class": effect,
        "effect_share": effect_share,
        "awareness_state": awareness,
        "awareness_share": awareness_share,
        "syntax_concentration": syntax_concentration,
    }


def _write_csv(rows: list[dict], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "name",
                "group",
                "run",
                "tick_start",
                "tick_end",
                "local_role",
                "rows",
                "symbol",
                "symbol_share",
                "symbol_family",
                "symbol_family_share",
                "field_symbol",
                "field_symbol_share",
                "effect_class",
                "effect_share",
                "awareness_state",
                "awareness_share",
                "syntax_concentration",
                "kipp_pressure",
                "relief",
                "rekopplung",
                "field_pressure",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in writer.fieldnames})


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["local_role"], row["name"], row["run"], row["tick_start"]))
    _write_csv(rows, out_path)

    role_counts: dict[str, Counter[str]] = {}
    family_by_role: dict[str, Counter[str]] = {}
    field_symbol_by_role: dict[str, Counter[str]] = {}
    for row in rows:
        role_counts.setdefault(row["local_role"], Counter())[row["name"]] += 1
        family_by_role.setdefault(row["local_role"], Counter())[row["symbol_family"]] += 1
        field_symbol_by_role.setdefault(row["local_role"], Counter())[row["field_symbol"]] += 1

    strongest = sorted(rows, key=lambda row: row["syntax_concentration"], reverse=True)[:16]

    lines = [
        "# Lokale multisensorische Syntax - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt lokale multisensorische Kipp- und Rekopplungsfenster gegen MINI_DIOs eigene Syntax.",
        "Sie prueft, ob lokale Sinnesinnenlagen wiederkehrende Zeichen, Familien oder Feld-Episodensymbole tragen.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Werden lokale multisensorische Innenlagen semantisch wiedererkannt?",
        "2. Unterpruefung: Top-Kippfenster und Top-Rekopplungsfenster gegen Symbol, Symbolfamilie und MCM-Feldsymbol legen.",
        "3. Folgeschritt: Nur bei wiederkehrender Syntax von lokalen Bedeutungsinseln sprechen.",
        "",
        "## Rollen und dominante Familien",
        "",
    ]
    for role in sorted(family_by_role):
        families = ", ".join(f"`{name}` ({count})" for name, count in family_by_role[role].most_common(6))
        field_symbols = ", ".join(f"`{name}` ({count})" for name, count in field_symbol_by_role[role].most_common(6))
        lines.append(f"- `{role}` Familien: {families}")
        lines.append(f"- `{role}` Feldsymbole: {field_symbols}")

    lines.extend(
        [
            "",
            "## Staerkste Syntax-Konzentration",
            "",
            "| Welt | Lauf | Ticks | Rolle | Familie | Anteil | Feldsymbol | Anteil | Effekt | Awareness | Syntaxkonz. | Kipp | Entlastung |",
            "|---|---:|---|---|---|---:|---|---:|---|---|---:|---:|---:|",
        ]
    )
    for row in strongest:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    str(row["run"]),
                    f"{row['tick_start']}-{row['tick_end']}",
                    row["local_role"],
                    row["symbol_family"],
                    _fmt(row["symbol_family_share"], 4),
                    row["field_symbol"],
                    _fmt(row["field_symbol_share"], 4),
                    row["effect_class"],
                    row["awareness_state"],
                    _fmt(row["syntax_concentration"], 4),
                    _fmt(row["kipp_pressure"], 4),
                    _fmt(row["relief"], 4),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Welt-/Rollenverteilung", ""])
    for role in sorted(role_counts):
        values = ", ".join(f"`{name}` ({count})" for name, count in role_counts[role].most_common())
        lines.append(f"- `{role}`: {values}")

    lines.extend(
        [
            "",
            "## Vorlaeufige Lesart",
            "",
            "Eine lokale multisensorische Innenlage wird erst dann als Bedeutungsinsel interessant, wenn sie nicht nur hohe Kipp- oder Rekopplungswerte zeigt, sondern auch eigene wiederkehrende Syntax traegt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Darin wird bewertet, ob lokale Kipp- und Rekopplungsfenster semantisch getrennte Innenfeldinseln bilden oder nur dieselbe allgemeine Feldsprache wiederholen.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prueft lokale multisensorische Fenster gegen MINI_DIO-Syntax.")
    parser.add_argument("--local-windows", type=Path, default=DEFAULT_LOCAL_WINDOWS)
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--role", action="append", default=["lokale_multisensorische_kippnaehe", "lokal_rekoppelnd"])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    summary_map = {name: _resolve(path_text) for name, path_text, _group in specs}
    windows = _load_windows(_resolve(args.local_windows), set(args.role))
    rows = [_window_syntax(window, summary_map) for window in windows if window["name"] in summary_map]
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
