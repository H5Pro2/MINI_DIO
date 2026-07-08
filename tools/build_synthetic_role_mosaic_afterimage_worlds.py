from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
START_TS = 1704067200000
STEP_MS = 300_000
FIELDS = ["timestamp_ms", "symbol", "timeframe", "open", "high", "low", "close", "volume"]


def _segment(index: int, rows: int) -> tuple[int, float]:
    segments = 6
    size = rows / segments
    seg = min(segments - 1, int(index / size))
    pos = (index - seg * size) / max(1.0, size)
    return seg, pos


def _smooth(pos: float) -> float:
    return 0.5 - 0.5 * math.cos(max(0.0, min(1.0, pos)) * math.pi)


def _profile(index: int, rows: int, mode: str) -> tuple[float, float, float, float]:
    seg, pos = _segment(index, rows)
    p = _smooth(pos)
    # drift, range, volume, chop
    profiles = [
        (0.00018, 0.0010, 70_000, 0.10),   # ruhiger Aufbau
        (0.00072, 0.0024, 170_000, 0.22),  # Expansion
        (-0.00022, 0.0048, 230_000, 0.75), # breiter Spannungsraum
        (0.00005, 0.0014, 95_000, 0.18),   # Kompression
        (-0.00065, 0.0038, 210_000, 0.52), # Bruch/Gegenlauf
        (0.00034, 0.0020, 140_000, 0.28),  # Rekopplungsversuch
    ]
    nxt = profiles[min(len(profiles) - 1, seg + 1)]
    cur = profiles[seg]
    if mode == "follow":
        p = min(1.0, p + 0.18)
    elif mode == "shuffle":
        # Segmentfolge bleibt energetisch ähnlich, aber zeitliche Ordnung driftet.
        seg = [2, 0, 4, 1, 5, 3][seg]
        cur = profiles[seg]
        nxt = profiles[min(len(profiles) - 1, (seg + 2) % len(profiles))]
        p = 0.5 + 0.5 * math.sin(index / 29.0)
    drift = cur[0] * (1.0 - p) + nxt[0] * p
    range_scale = cur[1] * (1.0 - p) + nxt[1] * p
    volume = cur[2] * (1.0 - p) + nxt[2] * p
    chop = cur[3] * (1.0 - p) + nxt[3] * p
    return drift, range_scale, volume, chop


def _row(index: int, price: float, rows: int, mode: str) -> tuple[dict[str, object], float]:
    drift, range_scale, volume, chop = _profile(index, rows, mode)
    slow = math.sin(index / 47.0) * 0.00042
    medium = math.sin(index / 11.0) * 0.00024
    fast = math.sin(index / 3.0) * 0.00018 * chop
    alternation = (1.0 if index % 2 == 0 else -1.0) * 0.00022 * chop
    ret = drift + slow + medium + fast + alternation
    if mode == "follow":
        # leichte Nachhallbindung: nicht Kopie, aber Anschlussnaehe.
        ret = ret * 0.86 + math.sin((index - 13) / 47.0) * 0.00016
        range_scale *= 0.94
        volume *= 0.96
    elif mode == "shuffle":
        ret = ret * 1.08 + math.sin(index / 5.0) * 0.00030
        range_scale *= 1.08
        volume *= 1.03

    open_ = price
    close = max(1e-9, open_ * (1.0 + ret))
    mid = (open_ + close) * 0.5
    candle_range = max(1e-9, mid * range_scale)
    wick_bias = 0.45 + min(0.35, chop * 0.35)
    high = max(open_, close) + candle_range * wick_bias
    low = min(open_, close) - candle_range * wick_bias
    symbol = {
        "base": "SYN_ROLE_MOSAIC_AFTERIMAGE_BASE",
        "follow": "SYN_ROLE_MOSAIC_AFTERIMAGE_FOLLOW",
        "shuffle": "SYN_ROLE_MOSAIC_AFTERIMAGE_SHUFFLE",
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
            "volume": round(max(1.0, volume + abs(math.sin(index / 4.0)) * volume * 0.18 * chop), 4),
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
    parser = argparse.ArgumentParser(description="Baut synthetische Rollen-Mosaik-Nachhallwelten.")
    parser.add_argument("--rows", type=int, default=3600)
    parser.add_argument("--out-dir", default="data")
    args = parser.parse_args()

    rows = max(900, int(args.rows or 3600))
    out_dir = ROOT / args.out_dir
    outputs = {
        "base": out_dir / f"synthetic_1788_role_mosaic_afterimage_base_{rows}_5m.csv",
        "follow": out_dir / f"synthetic_1788_role_mosaic_afterimage_follow_{rows}_5m.csv",
        "shuffle": out_dir / f"synthetic_1788_role_mosaic_afterimage_shuffle_{rows}_5m.csv",
    }
    for mode, path in outputs.items():
        write(path, build(rows, mode))
        print(f"{mode}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
