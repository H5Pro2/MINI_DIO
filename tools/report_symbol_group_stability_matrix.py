from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BEFORE = ROOT / "docs" / "befunde" / "256_PASSIVE_SYMBOLGRUPPEN_ROLLENKARTE.csv"
DEFAULT_AFTER = ROOT / "docs" / "befunde" / "259_SYMBOLGRUPPEN_NEUE_WELT_ROLLENKARTE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "261_SYMBOLGRUPPEN_STABILITAETSMATRIX.md"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "261_SYMBOLGRUPPEN_STABILITAETSMATRIX.csv"

NUMERIC_FIELDS = [
    "windows",
    "world_count",
    "symbol_count",
    "avg_rekopplung",
    "avg_relief",
    "avg_kipp_pressure",
    "avg_field_pressure",
    "avg_symbol_share",
    "avg_syntax_concentration",
]


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _load(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["symbol_group"]: row for row in csv.DictReader(handle)}


def _stability_state(row: dict[str, object]) -> str:
    kipp_delta = abs(_float(row["delta_avg_kipp_pressure"]))
    rek_delta = abs(_float(row["delta_avg_rekopplung"]))
    field_delta = abs(_float(row["delta_avg_field_pressure"]))
    if kipp_delta <= 0.01 and rek_delta <= 0.01 and field_delta <= 0.01:
        return "stabil"
    if kipp_delta <= 0.025 and rek_delta <= 0.025 and field_delta <= 0.025:
        return "leicht_verschoben"
    return "deutlich_verschoben"


def _matrix(before: dict[str, dict[str, str]], after: dict[str, dict[str, str]]) -> list[dict[str, object]]:
    groups = sorted(set(before) | set(after))
    rows: list[dict[str, object]] = []
    for group in groups:
        left = before.get(group, {})
        right = after.get(group, {})
        row: dict[str, object] = {"symbol_group": group}
        for field in NUMERIC_FIELDS:
            before_value = _float(left.get(field))
            after_value = _float(right.get(field))
            row[f"before_{field}"] = before_value
            row[f"after_{field}"] = after_value
            row[f"delta_{field}"] = after_value - before_value
        row["before_dominant_role"] = left.get("dominant_role", "-")
        row["after_dominant_role"] = right.get("dominant_role", "-")
        row["before_dominant_effect"] = left.get("dominant_effect", "-")
        row["after_dominant_effect"] = right.get("dominant_effect", "-")
        row["before_dominant_awareness"] = left.get("dominant_awareness", "-")
        row["after_dominant_awareness"] = right.get("dominant_awareness", "-")
        row["stability_state"] = _stability_state(row)
        rows.append(row)
    return rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["symbol_group", "stability_state"]
    for field in NUMERIC_FIELDS:
        fields.extend([f"before_{field}", f"after_{field}", f"delta_{field}"])
    fields.extend(
        [
            "before_dominant_role",
            "after_dominant_role",
            "before_dominant_effect",
            "after_dominant_effect",
            "before_dominant_awareness",
            "after_dominant_awareness",
        ]
    )
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Symbolgruppen-Stabilitaetsmatrix",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose vergleicht die passive Rollenkarte vor und nach einer neuen Welt.",
        "Sie prueft nicht Einzelzeichen, sondern ob Rollengruppen in ihrer Innenfeldwirkung stabil bleiben.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und keine Runtime-Regel.",
        "",
        "## Matrix",
        "",
        "| Symbolgruppe | Zustand | Fenster | Welten | Rekopplung | Entlastung | Kipp | Felddruck | Dominanter Effekt |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["symbol_group"]),
                    str(row["stability_state"]),
                    f"{int(_float(row['before_windows']))}->{int(_float(row['after_windows']))} ({_fmt(_float(row['delta_windows']), 0)})",
                    f"{int(_float(row['before_world_count']))}->{int(_float(row['after_world_count']))} ({_fmt(_float(row['delta_world_count']), 0)})",
                    _fmt(_float(row["delta_avg_rekopplung"])),
                    _fmt(_float(row["delta_avg_relief"])),
                    _fmt(_float(row["delta_avg_kipp_pressure"])),
                    _fmt(_float(row["delta_avg_field_pressure"])),
                    f"{row['before_dominant_effect']} -> {row['after_dominant_effect']}",
                ]
            )
            + " |"
        )

    stable = [row for row in rows if row["stability_state"] == "stabil"]
    shifted = [row for row in rows if row["stability_state"] != "stabil"]
    lines.extend(
        [
            "",
            "## Lesart",
            "",
            f"Stabile Gruppen: {', '.join(str(row['symbol_group']) for row in stable) or '-'}",
            f"Verschobene Gruppen: {', '.join(str(row['symbol_group']) for row in shifted) or '-'}",
            "",
            "Die neue Welt wirkt bisher nicht als Ordnungsbruch.",
            "Sie erweitert die Rekopplungsnaehe und fuegt eine schwache offene Variante hinzu, ohne Randspannung oder Rekopplungsnaehe in ihrer Grundwirkung zu drehen.",
            "",
            "## Grenze",
            "",
            "Die Matrix beschreibt nur passive Stabilitaet der Rollenrelation.",
            "Sie darf nicht als Beweis einer universellen Topologie gelesen werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine weitere andersartige Welt gegen dieselbe Matrix gelegt werden. Grundfrage: bleibt die Rollenrelation auch unter staerkerer Weltspannung stabil?",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before", type=Path, default=DEFAULT_BEFORE)
    parser.add_argument("--after", type=Path, default=DEFAULT_AFTER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    before = args.before if args.before.is_absolute() else ROOT / args.before
    after = args.after if args.after.is_absolute() else ROOT / args.after
    out = args.out if args.out.is_absolute() else ROOT / args.out
    csv_out = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out

    rows = _matrix(_load(before), _load(after))
    _write_csv(rows, csv_out)
    _write_md(rows, out)


if __name__ == "__main__":
    main()
