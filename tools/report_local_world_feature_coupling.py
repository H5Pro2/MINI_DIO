from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path

from report_recoupling_quality import _load_json, _resolve
from report_recoupling_quality import _row as recoupling_row


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "216_LOKALE_WELTMERKMALE_REKOPPLUNG_DIAGNOSE.md"


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _group_label(name: str) -> str:
    lowered = name.lower()
    if "quiet" in lowered or "ruhe" in lowered:
        return "ruhe"
    if "stress" in lowered:
        return "stress"
    return "sonstige"


def _read_candles(path_text: str) -> list[dict[str, float]]:
    path = _resolve(path_text)
    if not path.exists():
        return []
    rows: list[dict[str, float]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(
                {
                    "open": _float(row.get("open")),
                    "high": _float(row.get("high")),
                    "low": _float(row.get("low")),
                    "close": _float(row.get("close")),
                    "volume": _float(row.get("volume")),
                }
            )
    return rows


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    index = (len(values) - 1) * q
    lower = int(index)
    upper = min(lower + 1, len(values) - 1)
    if lower == upper:
        return values[lower]
    return values[lower] * (upper - index) + values[upper] * (index - lower)


def _world_features(candles: list[dict[str, float]]) -> dict[str, float]:
    if len(candles) < 2:
        return {
            "candles": float(len(candles)),
            "drift": 0.0,
            "abs_drift": 0.0,
            "avg_abs_return": 0.0,
            "p95_abs_return": 0.0,
            "avg_range": 0.0,
            "p95_range": 0.0,
            "avg_volume_change": 0.0,
            "direction_change_ratio": 0.0,
            "direction_persistence": 0.0,
            "world_compaction": 0.0,
        }

    closes = [row["close"] for row in candles]
    highs = [row["high"] for row in candles]
    lows = [row["low"] for row in candles]
    volumes = [row["volume"] for row in candles]
    returns = [
        (closes[index] - closes[index - 1]) / closes[index - 1]
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
    abs_returns = [abs(value) for value in returns]
    ranges = [
        max(0.0, high - low) / close
        for high, low, close in zip(highs, lows, closes)
        if close
    ]
    volume_changes = [
        abs((volumes[index] - volumes[index - 1]) / volumes[index - 1])
        for index in range(1, len(volumes))
        if volumes[index - 1]
    ]
    direction_changes = sum(
        1
        for index in range(1, len(returns))
        if returns[index] * returns[index - 1] < 0
    )
    direction_change_ratio = direction_changes / max(1, len(returns) - 1)
    drift = ((closes[-1] - closes[0]) / closes[0]) if closes[0] else 0.0
    avg_abs_return = sum(abs_returns) / max(1, len(abs_returns))
    avg_range = sum(ranges) / max(1, len(ranges))
    avg_volume_change = sum(volume_changes) / max(1, len(volume_changes))
    p95_abs_return = _percentile(abs_returns, 0.95)
    p95_range = _percentile(ranges, 0.95)
    direction_persistence = max(0.0, 1.0 - direction_change_ratio)
    # Passive Verdichtung: starke Bewegung + Range + Persistenz. Kein Signal,
    # nur eine Lesegroesse fuer lokale Weltspannung.
    world_compaction = (
        (avg_abs_return * 1000.0 * 0.28)
        + (p95_abs_return * 1000.0 * 0.22)
        + (avg_range * 1000.0 * 0.22)
        + (p95_range * 1000.0 * 0.18)
        + (min(avg_volume_change, 5.0) * 0.04)
        + (direction_persistence * 0.06)
    )
    return {
        "candles": float(len(candles)),
        "drift": drift,
        "abs_drift": abs(drift),
        "avg_abs_return": avg_abs_return,
        "p95_abs_return": p95_abs_return,
        "avg_range": avg_range,
        "p95_range": p95_range,
        "avg_volume_change": avg_volume_change,
        "direction_change_ratio": direction_change_ratio,
        "direction_persistence": direction_persistence,
        "world_compaction": world_compaction,
    }


def _contrast(row: dict) -> float:
    return float(row["binding_sum"]) - float(row["reiz_aktiv_rekoppelnd"])


def _write_csv(rows: list[dict], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    fieldnames = [
        "name",
        "group",
        "role",
        "contrast",
        "field_strain",
        "memory_load",
        "rekopplung",
        "world_compaction",
        "drift",
        "abs_drift",
        "avg_abs_return",
        "p95_abs_return",
        "avg_range",
        "p95_range",
        "avg_volume_change",
        "direction_change_ratio",
        "direction_persistence",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _fmt(row[key], 6) if isinstance(row.get(key), float) else row.get(key) for key in fieldnames})


def _avg(rows: list[dict], key: str) -> float:
    return sum(float(row[key]) for row in rows) / max(1, len(rows))


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"]))
    _write_csv(rows, out_path)
    stress_rows = [row for row in rows if row["group"] == "stress"]
    quiet_rows = [row for row in rows if row["group"] == "ruhe"]
    strongest_binding = sorted(rows, key=lambda row: row["contrast"], reverse=True)[:5]
    strongest_compaction = sorted(rows, key=lambda row: row["world_compaction"], reverse=True)[:5]

    lines = [
        "# Lokale Weltmerkmale und Rekopplung - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt Rohweltmerkmale neben lokale Rekopplungsrollen.",
        "Sie prueft, welche Weltmerkmale den Uebergang von aktiv-rekoppelnd zu bindend begleiten.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Welche Weltmerkmale erzeugen oder begleiten Rekopplungsbindung?",
        "2. Unterpruefung: Drift, Range, Volumenrhythmus, Richtungswechsel und Verdichtung gegen Feldlast/Memory/Rekopplung legen.",
        "3. Folgeschritt: Bewerten, ob Bindung eher aus Weltstruktur, Nachhall oder Feldzustand entsteht.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | Gruppe | Rolle | Kontrast | Feldlast | Memorylast | Rekopplung | Verdichtung | Drift | avg Range | p95 Range | Richtungswechsel | Persistenz |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["group"],
                    row["role"],
                    _fmt(row["contrast"], 4),
                    _fmt(row["field_strain"], 4),
                    _fmt(row["memory_load"], 4),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["world_compaction"], 4),
                    _fmt(row["drift"], 4),
                    _fmt(row["avg_range"], 6),
                    _fmt(row["p95_range"], 6),
                    _fmt(row["direction_change_ratio"], 4),
                    _fmt(row["direction_persistence"], 4),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Gruppenmittel", ""])
    if stress_rows:
        lines.extend(
            [
                "### Stress",
                "",
                f"- Kontrast Bindung-Aktiv: `{_fmt(_avg(stress_rows, 'contrast'), 4)}`",
                f"- Feldlast: `{_fmt(_avg(stress_rows, 'field_strain'), 4)}`",
                f"- Memorylast: `{_fmt(_avg(stress_rows, 'memory_load'), 4)}`",
                f"- Weltverdichtung: `{_fmt(_avg(stress_rows, 'world_compaction'), 4)}`",
                f"- Richtungswechsel: `{_fmt(_avg(stress_rows, 'direction_change_ratio'), 4)}`",
                "",
            ]
        )
    if quiet_rows:
        lines.extend(
            [
                "### Ruhe",
                "",
                f"- Kontrast Bindung-Aktiv: `{_fmt(_avg(quiet_rows, 'contrast'), 4)}`",
                f"- Feldlast: `{_fmt(_avg(quiet_rows, 'field_strain'), 4)}`",
                f"- Memorylast: `{_fmt(_avg(quiet_rows, 'memory_load'), 4)}`",
                f"- Weltverdichtung: `{_fmt(_avg(quiet_rows, 'world_compaction'), 4)}`",
                f"- Richtungswechsel: `{_fmt(_avg(quiet_rows, 'direction_change_ratio'), 4)}`",
                "",
            ]
        )

    lines.extend(["## Staerkste Bindung", ""])
    for row in strongest_binding:
        lines.append(
            f"- `{row['name']}`: Kontrast `{_fmt(row['contrast'], 4)}`, Verdichtung `{_fmt(row['world_compaction'], 4)}`, "
            f"Range `{_fmt(row['avg_range'], 6)}`, Richtungswechsel `{_fmt(row['direction_change_ratio'], 4)}`"
        )

    lines.extend(["", "## Staerkste Rohweltverdichtung", ""])
    for row in strongest_compaction:
        lines.append(
            f"- `{row['name']}`: Verdichtung `{_fmt(row['world_compaction'], 4)}`, Rolle `{row['role']}`, "
            f"Kontrast `{_fmt(row['contrast'], 4)}`"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Diese Diagnose ist noch keine Erklaerung, sondern eine Kopplungskarte.",
            "Sie zeigt, ob lokale Bindung mit Rohweltmerkmalen zusammenfaellt oder ob Feldzustand und Memory staerker erklaeren.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Dabei wird bewertet, ob lokale Bindung vor allem durch Verdichtung, Richtungswechsel, Range oder bereits vorhandene Feld-/Memorylage entsteht.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Verbindet lokale Weltmerkmale mit Rekopplungsrollen.")
    parser.add_argument("--summary", nargs=2, action="append", metavar=("NAME", "PATH"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = []
    for name, path_text in args.summary:
        summary = _load_json(_resolve(path_text))
        row = recoupling_row(name, summary)
        features = _world_features(_read_candles(str(summary.get("data_path", ""))))
        rows.append(
            {
                "name": name,
                "group": _group_label(name),
                "role": row["dominant_role"],
                "contrast": _contrast(row),
                "field_strain": row["field_strain"],
                "memory_load": row["memory_load"],
                "rekopplung": row["rekopplung"],
                **features,
            }
        )
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
