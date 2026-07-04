from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def _phase_value(index: int, phase: str, block_size: int) -> float:
    if phase == "rest":
        return math.sin(index * 0.11) * 0.18
    if phase == "wave_up":
        return max(0.0, math.sin(index * 0.18)) * 0.95 + math.sin(index * 0.04) * 0.15
    if phase == "wave_down":
        return -max(0.0, math.sin(index * 0.18)) * 0.95 + math.cos(index * 0.04) * 0.15
    if phase == "regular":
        return 1.0 if index % 2 == 0 else -1.0
    if phase == "block":
        return 1.0 if (index // max(1, block_size)) % 2 == 0 else -1.0
    if phase == "irregular":
        value = math.sin(index * 1.731) + math.sin(index * 0.417) * 0.55 + math.cos(index * 0.113) * 0.25
        return 1.0 if value >= 0.0 else -1.0
    raise ValueError(f"unknown melody phase: {phase}")


def _parse_phases(value: str) -> list[str]:
    phases = [part.strip() for part in value.split(",") if part.strip()]
    allowed = {"rest", "wave_up", "wave_down", "regular", "block", "irregular"}
    unknown = [phase for phase in phases if phase not in allowed]
    if unknown:
        raise ValueError(f"unknown phases: {', '.join(unknown)}")
    if not phases:
        raise ValueError("at least one phase is required")
    return phases


def build_rows(
    rows: int,
    start_price: float,
    symbol: str,
    timeframe: str,
    phases: list[str],
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
    phase_len = max(1, rows // len(phases))

    for i in range(rows):
        phase_index = min(len(phases) - 1, i // phase_len)
        phase = phases[phase_index]
        local_index = i - (phase_index * phase_len)
        base = _phase_value(local_index, phase, block_size)
        tremor = math.sin(i * 0.37) * 0.10 + math.cos(i * 0.071) * 0.08
        ret = drift + (base + tremor) * amplitude

        open_price = price
        close = max(0.01, open_price * (1.0 + ret))
        body = abs(close - open_price)
        wick_phase = 0.5 + 0.5 * math.sin(i * 0.29)
        wick = max(open_price * range_scale, body * 1.55)
        high = max(open_price, close) + wick * (0.25 + 0.22 * wick_phase)
        low = min(open_price, close) - wick * (0.25 + 0.22 * (1.0 - wick_phase))
        low = max(0.01, low)
        volume = 100_000.0 * volume_scale * (1.0 + abs(base) * 0.06 + abs(tremor) * 0.05)

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
                "melody_phase": phase,
            }
        )
        price = close
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Erzeuge synthetische Melodie-Welten aus mehreren Rhythmusphasen.")
    parser.add_argument("--rows", type=int, default=1200)
    parser.add_argument("--start-price", type=float, default=100.0)
    parser.add_argument("--symbol", default="SYN_MELODY")
    parser.add_argument("--timeframe", default="5m")
    parser.add_argument("--phases", default="rest,wave_up,block,wave_down,regular,rest")
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
        phases=_parse_phases(args.phases),
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
            fieldnames=[
                "timestamp_ms",
                "symbol",
                "timeframe",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "melody_phase",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"[DONE] wrote {path} rows={len(rows)} phases={args.phases}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
