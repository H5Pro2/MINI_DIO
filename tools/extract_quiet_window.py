from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _path(path_text: str) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(row: dict, key: str) -> float:
    try:
        return float(row.get(key) or 0.0)
    except Exception:
        return 0.0


def _read_rows(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def _window_metrics(rows: list[dict], start: int, size: int) -> dict[str, float]:
    window = rows[start : start + size]
    closes = [_float(row, "close") for row in window]
    highs = [_float(row, "high") for row in window]
    lows = [_float(row, "low") for row in window]
    volumes = [_float(row, "volume") for row in window]

    signed_returns = [
        (closes[index] - closes[index - 1]) / closes[index - 1]
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
    returns = [abs(value) for value in signed_returns]
    ranges = [(high - low) / close for high, low, close in zip(highs, lows, closes) if close]
    direction_changes = sum(
        1
        for index in range(2, len(closes))
        if (closes[index] - closes[index - 1]) * (closes[index - 1] - closes[index - 2]) < 0
    )
    drift = ((closes[-1] - closes[0]) / closes[0]) if len(closes) >= 2 and closes[0] else 0.0
    max_drawdown = 0.0
    peak = closes[0] if closes else 0.0
    for close in closes:
        peak = max(peak, close)
        if peak:
            max_drawdown = max(max_drawdown, (peak - close) / peak)

    avg_abs_return = sum(returns) / max(1, len(returns))
    max_abs_return = max(returns) if returns else 0.0
    avg_range = sum(ranges) / max(1, len(ranges))
    mean_signed = sum(signed_returns) / max(1, len(signed_returns))
    return_volatility = (
        sum((value - mean_signed) ** 2 for value in signed_returns) / max(1, len(signed_returns))
    ) ** 0.5
    avg_volume = sum(volumes) / max(1, len(volumes))

    quiet_score = (
        avg_abs_return * 42.0
        + max_abs_return * 8.0
        + avg_range * 24.0
        + return_volatility * 32.0
        + abs(drift) * 0.7
        + max_drawdown * 1.1
        + (direction_changes / max(1, size)) * 0.5
    )
    return {
        "start": float(start),
        "end": float(start + size),
        "avg_abs_return": avg_abs_return,
        "max_abs_return": max_abs_return,
        "avg_range": avg_range,
        "return_volatility": return_volatility,
        "drift": drift,
        "max_drawdown": max_drawdown,
        "direction_changes": float(direction_changes),
        "avg_volume": avg_volume,
        "quiet_score": quiet_score,
    }


def _write_rows(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extrahiere ein rohweltlich ruhiges Kontrollfenster.")
    parser.add_argument("--source", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--window-size", type=int, default=100)
    parser.add_argument("--step", type=int, default=25)
    parser.add_argument("--report", default="")
    args = parser.parse_args()

    source = _path(args.source)
    out = _path(args.out)
    report = _path(args.report) if args.report else None
    fieldnames, rows = _read_rows(source)
    if len(rows) < args.window_size:
        raise ValueError(f"source has only {len(rows)} rows, need {args.window_size}")

    metrics = []
    max_start = len(rows) - args.window_size
    for start in range(0, max_start + 1, max(1, args.step)):
        metrics.append(_window_metrics(rows, start, args.window_size))
    if metrics[-1]["start"] != float(max_start):
        metrics.append(_window_metrics(rows, max_start, args.window_size))

    best = min(metrics, key=lambda item: item["quiet_score"])
    start = int(best["start"])
    selected = rows[start : start + args.window_size]
    _write_rows(out, fieldnames, selected)

    payload = {
        "source": str(source.relative_to(ROOT) if source.is_relative_to(ROOT) else source),
        "out": str(out.relative_to(ROOT) if out.is_relative_to(ROOT) else out),
        "window_size": args.window_size,
        "step": args.step,
        "evaluated_windows": len(metrics),
        "best": best,
        "bottom_windows": sorted(metrics, key=lambda item: item["quiet_score"])[:10],
    }
    if report is not None:
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
