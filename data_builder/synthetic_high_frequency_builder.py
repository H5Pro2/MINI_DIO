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
    amplitude: float,
    drift: float,
    range_scale: float,
    volume_scale: float,
    switch_rate: float,
) -> list[dict[str, object]]:
    timestamp = 1_704_067_200_000
    step_ms = 300_000
    price = start_price
    out: list[dict[str, object]] = []
    direction = 1.0
    switch_rate = max(0.0, min(1.0, switch_rate))
    for i in range(rows):
        phase = (i * 0.61803398875) % 1.0
        if i == 0:
            direction = 1.0
        elif phase < switch_rate:
            direction *= -1.0
        fast = direction
        tremor = math.sin(i * 0.91) * 0.32 + math.sin(i * 0.37) * 0.18
        slow_bias = math.sin(i / max(1, rows) * math.tau * 2.0) * 0.18
        ret = drift + (fast + tremor + slow_bias) * amplitude

        open_price = price
        close = max(0.01, open_price * (1.0 + ret))
        body = abs(close - open_price)
        wick_phase = 0.5 + 0.5 * math.sin(i * 0.73)
        wick = max(open_price * range_scale, body * 1.8)
        high = max(open_price, close) + wick * (0.30 + 0.30 * wick_phase)
        low = min(open_price, close) - wick * (0.30 + 0.30 * (1.0 - wick_phase))
        low = max(0.01, low)
        volume = 100_000.0 * volume_scale * (1.0 + abs(ret / max(amplitude, 1e-9)) * 0.08 + abs(tremor) * 0.08)

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
    parser = argparse.ArgumentParser(description="Erzeuge eine synthetische hochfrequente Wechselwelt.")
    parser.add_argument("--rows", type=int, default=1000)
    parser.add_argument("--start-price", type=float, default=100.0)
    parser.add_argument("--symbol", default="SYN_HIGH_FREQ_SWITCH")
    parser.add_argument("--timeframe", default="5m")
    parser.add_argument("--amplitude", type=float, default=0.0011)
    parser.add_argument("--drift", type=float, default=0.0)
    parser.add_argument("--range-scale", type=float, default=0.0048)
    parser.add_argument("--volume-scale", type=float, default=2.2)
    parser.add_argument("--switch-rate", type=float, default=1.0)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = build_rows(
        rows=args.rows,
        start_price=args.start_price,
        symbol=args.symbol,
        timeframe=args.timeframe,
        amplitude=args.amplitude,
        drift=args.drift,
        range_scale=args.range_scale,
        volume_scale=args.volume_scale,
        switch_rate=args.switch_rate,
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
