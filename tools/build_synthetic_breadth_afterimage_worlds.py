from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
START_TS = 1704067200000
STEP_MS = 300_000
FIELDS = ["timestamp_ms", "symbol", "timeframe", "open", "high", "low", "close", "volume"]


def _pulse(index: int, center: float, width: float) -> float:
    distance = abs(index - center)
    if distance >= width:
        return 0.0
    return 0.5 + 0.5 * math.cos(math.pi * distance / width)


def _field(index: int, rows: int, mode: str) -> float:
    # Mehrere versetzte Inseln erzeugen Rollenbreite; langsame Huelle erzeugt Nachhall.
    centers = [rows * 0.18, rows * 0.34, rows * 0.52, rows * 0.69, rows * 0.84]
    widths = [rows * 0.055, rows * 0.075, rows * 0.065, rows * 0.085, rows * 0.060]
    value = sum(_pulse(index, center, width) for center, width in zip(centers, widths))
    value /= max(1.0, len(centers) * 0.72)
    slow = 0.5 + 0.5 * math.sin(index / 173.0)
    if mode == "follow":
        value = (value * 0.78) + (slow * 0.22)
    elif mode == "shuffle_control":
        # Gleiche Energiegrundlage, aber fragmentierte Reihenfolge.
        value = (0.5 + 0.5 * math.sin((index * 37 % rows) / 41.0)) * 0.62
    else:
        value = (value * 0.88) + (slow * 0.12)
    return max(0.0, min(1.0, value))


def _row(index: int, price: float, rows: int, mode: str) -> tuple[dict[str, object], float]:
    field = _field(index, rows, mode)
    after = _field(max(0, index - 9), rows, mode)
    carry = (field * 0.72) + (after * 0.28)
    phase = math.sin(index / 23.0) + (0.45 * math.sin(index / 7.0))
    fine = math.sin(index / 3.0) * 0.00016
    drift = math.sin(index / 211.0) * 0.00018

    if mode == "follow":
        ret = (phase * 0.00033) + (carry * math.sin(index / 17.0) * 0.00052) + drift
        range_scale = 0.0012 + carry * 0.0022
        volume = 70_000 + carry * 120_000 + abs(math.sin(index / 5.0)) * carry * 38_000
    elif mode == "shuffle_control":
        ret = (phase * 0.00028) + (field * math.sin((index * 19) / 11.0) * 0.00050) + fine
        range_scale = 0.0010 + field * 0.0020
        volume = 70_000 + field * 115_000 + abs(math.sin((index * 13) / 4.0)) * field * 42_000
    else:
        ret = (phase * 0.00036) + (carry * math.sin(index / 13.0) * 0.00058) + fine + drift
        range_scale = 0.0011 + carry * 0.0025
        volume = 72_000 + carry * 130_000 + abs(math.sin(index / 4.0)) * carry * 45_000

    open_ = price
    close = max(1e-9, open_ * (1.0 + ret))
    mid = (open_ + close) * 0.5
    candle_range = max(1e-9, mid * range_scale)
    high = max(open_, close) + candle_range * (0.50 + carry * 0.18)
    low = min(open_, close) - candle_range * (0.50 + carry * 0.18)
    symbol = {
        "base": "SYN_BREADTH_AFTERIMAGE_BASE",
        "follow": "SYN_BREADTH_AFTERIMAGE_FOLLOW",
        "shuffle_control": "SYN_BREADTH_AFTERIMAGE_SHUFFLE",
    }[mode]
    return (
        {
            "timestamp_ms": START_TS + index * STEP_MS,
            "symbol": symbol,
            "timeframe": "5m",
            "open": round(open_, 8),
            "high": round(high, 8),
            "low": round(low, 8),
            "close": round(close, 8),
            "volume": round(max(1.0, volume), 4),
        },
        close,
    )


def build(rows: int, mode: str) -> list[dict[str, object]]:
    price = 100.0
    out: list[dict[str, object]] = []
    for index in range(rows):
        row, price = _row(index, price, rows, mode)
        out.append(row)
    return out


def write(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Baut synthetische Breite-plus-Nachhall-Kontrollwelten.")
    parser.add_argument("--rows", type=int, default=3000)
    parser.add_argument("--out-dir", default="data")
    args = parser.parse_args()

    rows = max(600, int(args.rows or 3000))
    out_dir = ROOT / args.out_dir
    outputs = {
        "base": out_dir / f"synthetic_1787_breadth_afterimage_base_{rows}_5m.csv",
        "follow": out_dir / f"synthetic_1787_breadth_afterimage_follow_{rows}_5m.csv",
        "shuffle_control": out_dir / f"synthetic_1787_breadth_afterimage_shuffle_{rows}_5m.csv",
    }
    for mode, path in outputs.items():
        write(path, build(rows, mode))
        print(f"{mode}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
