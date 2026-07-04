from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def _direction(index: int, mode: str, block_size: int) -> float:
    if mode == "regular":
        return 1.0 if index % 2 == 0 else -1.0
    if mode == "block":
        return 1.0 if (index // max(1, block_size)) % 2 == 0 else -1.0
    if mode == "irregular":
        value = math.sin(index * 1.731) + math.sin(index * 0.417) * 0.55 + math.cos(index * 0.113) * 0.25
        return 1.0 if value >= 0.0 else -1.0
    if mode == "wave":
        return math.sin(index * 0.19)
    raise ValueError(f"unknown rhythm mode: {mode}")


def build_rows(
    rows: int,
    start_price: float,
    symbol: str,
    timeframe: str,
    mode: str,
    amplitude: float,
    drift: float,
    range_scale: float,
    volume_scale: float,
    block_size: int,
) -> list[dict[str, object]]:
    timestamp = 1_704_067_200_000
    step_ms = 300_000
    price = start_price
    out: list[dict[str, object]] = []
    for i in range(rows):
        direction = _direction(i, mode, block_size)
        tremor = math.sin(i * 0.43) * 0.22 + math.cos(i * 0.077) * 0.12
        ret = drift + ((direction * 0.92) + tremor) * amplitude

        open_price = price
        close = max(0.01, open_price * (1.0 + ret))
        body = abs(close - open_price)
        wick_phase = 0.5 + 0.5 * math.sin(i * 0.31)
        wick = max(open_price * range_scale, body * 1.65)
        high = max(open_price, close) + wick * (0.28 + 0.26 * wick_phase)
        low = min(open_price, close) - wick * (0.28 + 0.26 * (1.0 - wick_phase))
        low = max(0.01, low)
        volume = 100_000.0 * volume_scale * (1.0 + abs(direction) * 0.05 + abs(tremor) * 0.08)

        out.append(
            {
                "timestamp_ms": timestamp + (i * step_ms),
                "symbol": symbol,
                "timeframe": timeframe,
                "open": round(open_price, 8),
                "high": round(high, 8),
                "low": round(low, 8),
                "close": round(close, 8),
                "volume": round(volume, 4),
            }
        )
        price = close
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Erzeuge synthetische Rhythmuswelten.")
    parser.add_argument("--rows", type=int, default=1000)
    parser.add_argument("--start-price", type=float, default=100.0)
    parser.add_argument("--symbol", default="SYN_RHYTHM")
    parser.add_argument("--timeframe", default="5m")
    parser.add_argument("--mode", choices=["regular", "block", "irregular", "wave"], required=True)
    parser.add_argument("--amplitude", type=float, default=0.00115)
    parser.add_argument("--drift", type=float, default=0.0)
    parser.add_argument("--range-scale", type=float, default=0.0048)
    parser.add_argument("--volume-scale", type=float, default=2.2)
    parser.add_argument("--block-size", type=int, default=8)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = build_rows(
        rows=args.rows,
        start_price=args.start_price,
        symbol=args.symbol,
        timeframe=args.timeframe,
        mode=args.mode,
        amplitude=args.amplitude,
        drift=args.drift,
        range_scale=args.range_scale,
        volume_scale=args.volume_scale,
        block_size=args.block_size,
    )
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["timestamp_ms", "symbol", "timeframe", "open", "high", "low", "close", "volume"],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"[DONE] wrote {path} rows={len(rows)} mode={args.mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
