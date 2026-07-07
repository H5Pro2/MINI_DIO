from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
START_TS = 1704067200000
STEP_MS = 300_000


def _phase_pressure(index: int, cycle: int = 720) -> float:
    position = index % cycle
    if 220 <= position < 420:
        center = 320.0
        width = 100.0
        return max(0.0, 1.0 - (abs(position - center) / width))
    return 0.0


def _base_return(index: int) -> float:
    slow = math.sin(index / 83.0) * 0.00055
    medium = math.sin(index / 19.0) * 0.00028
    micro = math.sin(index / 5.0) * 0.00010
    return slow + medium + micro


def _row(index: int, price: float, mode: str) -> tuple[dict[str, object], float]:
    pressure = _phase_pressure(index)
    sign = 1.0 if index % 2 == 0 else -1.0
    ret = _base_return(index)
    base_range = 0.00115 + (abs(math.sin(index / 31.0)) * 0.00042)
    base_volume = 92_000.0 + (math.sin(index / 47.0) * 8_500.0) + (math.sin(index / 9.0) * 3_500.0)

    if mode in {"range_hearing", "range_tension"}:
        base_range *= 1.0 + (pressure * 3.2)
    if mode in {"range_hearing", "hearing_tension"}:
        base_volume *= 1.0 + (pressure * 2.6) + (abs(math.sin(index / 3.0)) * pressure * 0.85)
    if mode in {"range_tension", "hearing_tension"}:
        ret += sign * pressure * 0.00125

    open_ = price
    close = max(1e-9, open_ * (1.0 + ret))
    center = (open_ + close) * 0.5
    candle_range = max(1e-9, center * base_range)
    high = max(open_, close) + (candle_range * 0.50)
    low = min(open_, close) - (candle_range * 0.50)
    next_price = close
    symbol = {
        "range_hearing": "SYN_PAIR_RANGE_HEARING",
        "range_tension": "SYN_PAIR_RANGE_TENSION",
        "hearing_tension": "SYN_PAIR_HEARING_TENSION",
    }[mode]
    return (
        {
            "timestamp_ms": START_TS + (index * STEP_MS),
            "symbol": symbol,
            "timeframe": "5m",
            "open": round(open_, 8),
            "high": round(high, 8),
            "low": round(low, 8),
            "close": round(close, 8),
            "volume": round(max(1.0, base_volume), 4),
        },
        next_price,
    )


def build(mode: str, rows: int) -> list[dict[str, object]]:
    price = 100.0
    out: list[dict[str, object]] = []
    for index in range(rows):
        item, price = _row(index, price, mode)
        out.append(item)
    return out


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["timestamp_ms", "symbol", "timeframe", "open", "high", "low", "close", "volume"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Baut synthetische Zweierkopplungs-Welten fuer dio_0ly7.")
    parser.add_argument("--rows", type=int, default=8500)
    parser.add_argument("--out-dir", default="data")
    args = parser.parse_args()

    out_dir = ROOT / args.out_dir
    rows = max(32, int(args.rows or 8500))
    outputs = {
        "range_hearing": out_dir / f"synthetic_1716_pair_range_hearing_{rows}_5m.csv",
        "range_tension": out_dir / f"synthetic_1716_pair_range_tension_{rows}_5m.csv",
        "hearing_tension": out_dir / f"synthetic_1716_pair_hearing_tension_{rows}_5m.csv",
    }
    for mode, path in outputs.items():
        write_csv(path, build(mode, rows=rows))
        print(f"{mode}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
