from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["timestamp_ms", "symbol", "timeframe", "open", "high", "low", "close", "volume"]


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _read_raw_kline_rows(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        for raw in reader:
            if len(raw) < 6:
                continue
            rows.append(
                {
                    "timestamp_ms": raw[0],
                    "open": raw[1],
                    "high": raw[2],
                    "low": raw[3],
                    "close": raw[4],
                    "volume": raw[5],
                }
            )
    return rows


def build_world(sources: list[Path], target: Path, symbol: str, timeframe: str, rows: int) -> dict[str, object]:
    target.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    with target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for source in sources:
            for row in _read_raw_kline_rows(source):
                if written >= rows:
                    break
                writer.writerow(
                    {
                        "timestamp_ms": row["timestamp_ms"],
                        "symbol": symbol,
                        "timeframe": timeframe,
                        "open": row["open"],
                        "high": row["high"],
                        "low": row["low"],
                        "close": row["close"],
                        "volume": row["volume"],
                    }
                )
                written += 1
            if written >= rows:
                break
    return {
        "sources": [str(source) for source in sources],
        "target": str(target),
        "symbol": symbol,
        "timeframe": timeframe,
        "rows_requested": rows,
        "rows_written": written,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalisiert rohe Binance-Kline-CSV-Dateien zu MINI_DIO-Weltspuren.")
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--timeframe", required=True)
    parser.add_argument("--rows", type=int, default=17000)
    args = parser.parse_args()
    result = build_world(
        sources=[_resolve(source) for source in args.source],
        target=_resolve(args.target),
        symbol=args.symbol,
        timeframe=args.timeframe,
        rows=args.rows,
    )
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
