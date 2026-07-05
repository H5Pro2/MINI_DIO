from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path


def create_slice(source: Path, target: Path, start: int, rows: int) -> dict[str, object]:
    target.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    with source.open(newline="", encoding="utf-8") as src, target.open("w", newline="", encoding="utf-8") as dst:
        reader = csv.DictReader(src)
        fieldnames = list(reader.fieldnames or [])
        writer = csv.DictWriter(dst, fieldnames=fieldnames)
        writer.writeheader()
        for index, row in enumerate(reader):
            if index < start:
                continue
            if written >= rows:
                break
            writer.writerow(row)
            written += 1
    return {
        "source": str(source),
        "target": str(target),
        "start": int(start),
        "rows_requested": int(rows),
        "rows_written": int(written),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Erzeugt einen kontrollierten CSV-Ausschnitt mit Header.")
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--rows", type=int, default=1000)
    args = parser.parse_args()
    result = create_slice(_path(args.source), _path(args.target), args.start, args.rows)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
