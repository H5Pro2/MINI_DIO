from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def build_rows(
    rows: int,
    start_price: float,
    symbol: str,
    timeframe: str,
    drift: float,
    wave: float,
    noise: float,
    volume_scale: float,
) -> list[dict[str, object]]:
    timestamp = 1_704_067_200_000
    step_ms = 300_000
    price = start_price
    out: list[dict[str, object]] = []
    for i in range(rows):
        t = i / max(1, rows - 1)
        slow = math.sin(t * math.tau)
        micro = math.sin(i * 0.137 + math.cos(i * 0.021))
        ret = drift + (slow * wave * 0.10) + (micro * noise * 0.04)

        open_price = price
        close = max(0.01, open_price * (1.0 + ret))
        body = abs(close - open_price)
        phase_range = max(open_price * (wave + noise) * 0.18, body * 1.55, open_price * 0.0007)
        wick_bias = 0.5 + 0.5 * math.sin(i * 0.061)
        high = max(open_price, close) + phase_range * (0.40 + 0.28 * wick_bias)
        low = min(open_price, close) - phase_range * (0.40 + 0.28 * (1.0 - wick_bias))
        low = max(0.01, low)
        volume = 100_000.0 * volume_scale * (1.0 + abs(slow) * 0.18 + abs(micro) * 0.12)

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=1000)
    parser.add_argument("--start-price", type=float, default=100.0)
    parser.add_argument("--symbol", default="SYN_QUIET_DRIFT")
    parser.add_argument("--timeframe", default="5m")
    parser.add_argument("--drift", type=float, default=0.00009)
    parser.add_argument("--wave", type=float, default=0.0022)
    parser.add_argument("--noise", type=float, default=0.0011)
    parser.add_argument("--volume-scale", type=float, default=1.0)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = build_rows(
        rows=args.rows,
        start_price=args.start_price,
        symbol=args.symbol,
        timeframe=args.timeframe,
        drift=args.drift,
        wave=args.wave,
        noise=args.noise,
        volume_scale=args.volume_scale,
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
    print(f"[DONE] wrote {path} rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
