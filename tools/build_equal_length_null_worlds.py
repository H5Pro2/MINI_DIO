from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _resolve(value: str | Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _read_rows(path: Path, rows: int) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        data = []
        for index, row in enumerate(reader):
            if index >= rows:
                break
            data.append(dict(row))
    return fieldnames, data


def _write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: float) -> str:
    return f"{value:.8f}".rstrip("0").rstrip(".")


def _row_shape(row: dict[str, str]) -> dict[str, float]:
    open_price = _float(row.get("open"))
    high = _float(row.get("high"))
    low = _float(row.get("low"))
    close = _float(row.get("close"))
    base = open_price if abs(open_price) > 1e-12 else close
    if abs(base) <= 1e-12:
        base = 1.0
    return {
        "body": (close - open_price) / base,
        "upper": max(high, open_price, close) / base - 1.0,
        "lower": 1.0 - min(low, open_price, close) / base,
        "volume": _float(row.get("volume")),
    }


def _rebuild_from_shapes(
    template_rows: list[dict[str, str]],
    shapes: list[dict[str, float]],
    symbol: str,
    timeframe: str,
) -> list[dict[str, str]]:
    if not template_rows:
        return []
    current = _float(template_rows[0].get("open"), 1.0)
    rebuilt: list[dict[str, str]] = []
    for template, shape in zip(template_rows, shapes):
        open_price = max(current, 1e-12)
        close = max(open_price * (1.0 + shape["body"]), 1e-12)
        high = max(open_price, close, open_price * (1.0 + abs(shape["upper"])))
        low = max(min(open_price, close, open_price * (1.0 - abs(shape["lower"]))), 1e-12)
        rebuilt.append(
            {
                "timestamp_ms": template.get("timestamp_ms", ""),
                "symbol": symbol or template.get("symbol", ""),
                "timeframe": timeframe or template.get("timeframe", ""),
                "open": _fmt(open_price),
                "high": _fmt(high),
                "low": _fmt(low),
                "close": _fmt(close),
                "volume": _fmt(max(0.0, shape["volume"])),
            }
        )
        current = close
    return rebuilt


def build_null_worlds(source: Path, out_prefix: Path, rows: int, seed: int) -> dict[str, object]:
    fieldnames, data = _read_rows(source, rows)
    if not data:
        raise ValueError(f"Keine Daten in {source}")
    if not fieldnames:
        fieldnames = ["timestamp_ms", "symbol", "timeframe", "open", "high", "low", "close", "volume"]
    rng = random.Random(seed)
    symbol = str(data[0].get("symbol", "") or "")
    timeframe = str(data[0].get("timeframe", "") or "")
    shapes = [_row_shape(row) for row in data]

    shuffled_shapes = list(shapes)
    rng.shuffle(shuffled_shapes)

    random_sign_shapes = []
    for shape in shapes:
        sign = -1.0 if rng.random() < 0.5 else 1.0
        random_sign_shapes.append({**shape, "body": abs(shape["body"]) * sign})

    shuffle_path = out_prefix.with_name(f"{out_prefix.name}_shuffle_order_{len(data)}.csv")
    random_sign_path = out_prefix.with_name(f"{out_prefix.name}_random_sign_{len(data)}.csv")
    _write_rows(shuffle_path, fieldnames, _rebuild_from_shapes(data, shuffled_shapes, symbol, timeframe))
    _write_rows(random_sign_path, fieldnames, _rebuild_from_shapes(data, random_sign_shapes, symbol, timeframe))

    return {
        "source": str(source),
        "rows": len(data),
        "seed": seed,
        "shuffle_order": str(shuffle_path),
        "random_sign": str(random_sign_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Erzeugt gleichlange Nullwelten aus einer Realwelt.")
    parser.add_argument("--source", required=True)
    parser.add_argument("--out-prefix", required=True)
    parser.add_argument("--rows", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=1835)
    args = parser.parse_args()
    result = build_null_worlds(
        source=_resolve(args.source),
        out_prefix=_resolve(args.out_prefix),
        rows=args.rows,
        seed=args.seed,
    )
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
