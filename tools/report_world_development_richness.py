from __future__ import annotations

import argparse
import csv
import math
import statistics
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1571_WELT_ENTWICKLUNGSREICHTUM_DIAGNOSE.md"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "1571_WELT_ENTWICKLUNGSREICHTUM_DIAGNOSE.csv"


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = (len(ordered) - 1) * q
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return ordered[int(index)]
    return ordered[lower] * (upper - index) + ordered[upper] * (index - lower)


def _std(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    return statistics.pstdev(values)


def _resolve(path_text: str) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_rows(path: Path) -> list[dict[str, float]]:
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


def _sign(value: float) -> int:
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def _analyze_world(name: str, path: Path) -> dict[str, object]:
    rows = _load_rows(path)
    closes = [row["close"] for row in rows]
    highs = [row["high"] for row in rows]
    lows = [row["low"] for row in rows]
    volumes = [row["volume"] for row in rows]

    returns = [
        (closes[index] - closes[index - 1]) / closes[index - 1]
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
    abs_returns = [abs(value) for value in returns]
    ranges = [
        (high - low) / close
        for high, low, close in zip(highs, lows, closes)
        if close
    ]
    volume_changes = [
        abs((volumes[index] - volumes[index - 1]) / volumes[index - 1])
        for index in range(1, len(volumes))
        if volumes[index - 1]
    ]
    directions = [_sign(value) for value in returns if _sign(value) != 0]
    direction_changes = sum(
        1
        for index in range(1, len(directions))
        if directions[index] != directions[index - 1]
    )
    direction_change_ratio = direction_changes / max(1, len(directions) - 1)
    drift = ((closes[-1] - closes[0]) / closes[0]) if closes and closes[0] else 0.0
    p95_return = _percentile(abs_returns, 0.95)
    p95_range = _percentile(ranges, 0.95)
    p95_volume_change = _percentile(volume_changes, 0.95)
    burst_ratio = (
        sum(1 for value in abs_returns if value >= p95_return) / max(1, len(abs_returns))
        if p95_return > 0
        else 0.0
    )
    range_burst_ratio = (
        sum(1 for value in ranges if value >= p95_range) / max(1, len(ranges))
        if p95_range > 0
        else 0.0
    )

    return {
        "world": name,
        "path": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
        "candles": len(rows),
        "avg_abs_return": statistics.fmean(abs_returns) if abs_returns else 0.0,
        "p95_abs_return": p95_return,
        "std_return": _std(returns),
        "avg_range": statistics.fmean(ranges) if ranges else 0.0,
        "p95_range": p95_range,
        "std_range": _std(ranges),
        "avg_volume_change": statistics.fmean(volume_changes) if volume_changes else 0.0,
        "p95_volume_change": p95_volume_change,
        "direction_change_ratio": direction_change_ratio,
        "abs_drift": abs(drift),
        "burst_ratio": burst_ratio,
        "range_burst_ratio": range_burst_ratio,
    }


def _relative_scores(rows: list[dict[str, object]]) -> None:
    features = [
        "avg_abs_return",
        "p95_abs_return",
        "std_return",
        "avg_range",
        "p95_range",
        "std_range",
        "avg_volume_change",
        "p95_volume_change",
        "direction_change_ratio",
        "abs_drift",
    ]
    for feature in features:
        values = [_float(row.get(feature)) for row in rows]
        min_value = min(values) if values else 0.0
        max_value = max(values) if values else 0.0
        span = max(max_value - min_value, 1e-12)
        for row in rows:
            row[f"{feature}_rel"] = (_float(row.get(feature)) - min_value) / span

    for row in rows:
        movement = (
            _float(row.get("avg_abs_return_rel")) * 0.16
            + _float(row.get("p95_abs_return_rel")) * 0.14
            + _float(row.get("std_return_rel")) * 0.10
        )
        range_energy = (
            _float(row.get("avg_range_rel")) * 0.12
            + _float(row.get("p95_range_rel")) * 0.10
            + _float(row.get("std_range_rel")) * 0.08
        )
        rhythm = (
            _float(row.get("direction_change_ratio_rel")) * 0.12
            + _float(row.get("avg_volume_change_rel")) * 0.08
            + _float(row.get("p95_volume_change_rel")) * 0.06
        )
        direction = _float(row.get("abs_drift_rel")) * 0.04
        score = movement + range_energy + rhythm + direction
        row["development_richness_score"] = score
        row["movement_component"] = movement
        row["range_component"] = range_energy
        row["rhythm_component"] = rhythm
        row["direction_component"] = direction

    ordered = sorted(rows, key=lambda item: _float(item.get("development_richness_score")), reverse=True)
    for rank, row in enumerate(ordered, start=1):
        row["development_rank"] = rank


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "path",
        "candles",
        "development_rank",
        "development_richness_score",
        "movement_component",
        "range_component",
        "rhythm_component",
        "direction_component",
        "avg_abs_return",
        "p95_abs_return",
        "std_return",
        "avg_range",
        "p95_range",
        "std_range",
        "avg_volume_change",
        "p95_volume_change",
        "direction_change_ratio",
        "abs_drift",
        "burst_ratio",
        "range_burst_ratio",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(rows, key=lambda item: int(item.get("development_rank", 999)))
    lines = [
        "# Welt-Entwicklungsreichtum Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese passive Diagnose prueft, wie viel Entwicklungsreichtum eine Welt vor der MCM-Feldbildung anbietet.",
        "",
        "Gemeint ist nicht, ob eine Welt gut oder schlecht ist.",
        "Gemeint ist, ob sie genug Bewegung, Spannungswechsel, Rhythmus, Bruch und Drift traegt, damit MINI_DIO mehrere Rollen oder Kombinationen bilden kann.",
        "",
        "Die Bewertung ist relativ zur geprueften Weltgruppe. Sie ist keine feste Regel.",
        "",
        "## Uebersicht",
        "",
        "| Rang | Welt | Score | Bewegung | Range | Rhythmus | Richtung | Richtungswechsel | Drift |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in ordered:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["development_rank"]),
                    str(row["world"]),
                    _fmt(row["development_richness_score"]),
                    _fmt(row["movement_component"]),
                    _fmt(row["range_component"]),
                    _fmt(row["rhythm_component"]),
                    _fmt(row["direction_component"]),
                    _fmt(row["direction_change_ratio"]),
                    _fmt(row["abs_drift"]),
                ]
            )
            + " |"
        )

    if ordered:
        top = ordered[0]
        bottom = ordered[-1]
    else:
        top = bottom = {}
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            f"Staerkste Entwicklungswelt in dieser Gruppe: `{top.get('world', '-')}`.",
            f"Schwaechste Entwicklungswelt in dieser Gruppe: `{bottom.get('world', '-')}`.",
            "",
            "Eine entwicklungsreiche Welt kann eher mehrere Feldrollen, Uebergaenge und Zwischenrollen ermoeglichen.",
            "Eine entwicklungsarme oder sehr glatte Welt kann dagegen als Einzel-Rekopplung erscheinen, ohne dass das MCM-Feld deswegen fehlerhaft ist.",
            "",
            "## Grenze",
            "",
            "Diese Diagnose misst nur die angebotene Weltqualitaet vor dem MCM-Feld.",
            "Sie beweist nicht, welche Topologie entsteht, und sie erzeugt keine Handlung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Rangfolge gegen die tatsaechliche Sleep-Kombinationsbildung gelegt werden: Welche Welten mit hohem Entwicklungsreichtum erzeugen wirklich mehrere Rollen, und welche bleiben trotzdem Einzel-Rekopplung?",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Passive Diagnose fuer Welt-Entwicklungsreichtum.")
    parser.add_argument(
        "--world",
        action="append",
        nargs=2,
        metavar=("NAME", "PATH"),
        help="Weltname und CSV-Pfad. Kann mehrfach genutzt werden.",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    worlds = args.world or [
        ("SOL2024_5M", "data/1-12_2024_5m_SOLUSDT.csv"),
        ("BTC1000_5M", "data/kontrolliert_btc2024_sleep_origin_1000_5m.csv"),
        ("PAXG1000_5M", "data/kontrolliert_paxg2024_sleep_origin_1000_5m.csv"),
        ("KAS1000_5M", "data/kontrolliert_kas2024_sleep_mosaic_1000_5m.csv"),
    ]

    rows = [_analyze_world(name, _resolve(path_text)) for name, path_text in worlds]
    _relative_scores(rows)

    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    csv_path = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    _write_csv(rows, csv_path)
    _write_md(rows, out_path)


if __name__ == "__main__":
    main()
