import os
import csv
import io
import zipfile
import argparse
import requests
import numpy as np

# ==========================================================
# OHLCV DB BUILDER
# ==========================================================
# Ziel:
# - Binance Monatsdaten laden
# - JEDE Kerze 1:1 speichern
# - NUR: timestamp, OHLCV
# - KEINE Ableitungen
# ==========================================================

COIN = "SOL"
QUOTE = "USDT"
TIMEFRAME = "5m"

START_YEAR = 2026
START_MONTH = 3
MONTHS = 2

DATA_DIR = "data"
STRIDE = 1
LIMIT = 0
OUTPUT = ""
MARKET = "spot"

# --------------------------------------------------
# Hilfsfunktionen Datum
# --------------------------------------------------
def get_year_month(start_year: int, start_month: int, offset: int):
    month = start_month + offset
    year = start_year + (month - 1) // 12
    month = ((month - 1) % 12) + 1
    return year, month

# --------------------------------------------------
# Binance Monatsdaten laden
# --------------------------------------------------
def download_month_csv(symbol: str, tf: str, date_yyyy_mm: str, data_dir: str, market: str = "spot"):
    os.makedirs(data_dir, exist_ok=True)
    csv_path = os.path.join(data_dir, f"{market}_{symbol}_{tf}_{date_yyyy_mm}.csv")

    if os.path.exists(csv_path):
        return csv_path

    if market == "futures_um":
        url = (
            "https://data.binance.vision/data/futures/um/monthly/klines/"
            f"{symbol}/{tf}/{symbol}-{tf}-{date_yyyy_mm}.zip"
        )
    else:
        url = (
            "https://data.binance.vision/data/spot/monthly/klines/"
            f"{symbol}/{tf}/{symbol}-{tf}-{date_yyyy_mm}.zip"
        )

    r = requests.get(url, timeout=60)
    if r.status_code != 200:
        print(f"[SKIP] Monat nicht verfügbar: {date_yyyy_mm}")
        return None

    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        name = z.namelist()[0]
        with z.open(name) as f_in, open(csv_path, "wb") as f_out:
            f_out.write(f_in.read())

    return csv_path

def load_month_candles(symbol: str, tf: str, date_yyyy_mm: str, data_dir: str, market: str = "spot") -> np.ndarray:
    csv_path = download_month_csv(symbol, tf, date_yyyy_mm, data_dir, market=market)
    if csv_path is None:
        return np.empty((0, 6))

    candles = []
    with open(csv_path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or str(row[0]).strip().lower() in ("open_time", "timestamp", "timestamp_ms"):
                continue
            candles.append([
                int(row[0]),    # timestamp_ms
                float(row[1]),  # open
                float(row[2]),  # high
                float(row[3]),  # low
                float(row[4]),  # close
                float(row[5]),  # volume
            ])

    return np.array(candles, dtype=np.float64)

# --------------------------------------------------
# CSV Writer
# --------------------------------------------------
def year_db_path(symbol: str, tf: str, year: int, data_dir: str) -> str:
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, f"{START_MONTH}-{MONTHS+START_MONTH-1}_{year}_{tf}_{symbol}.csv")

def append_rows(path: str, rows):
    file_exists = os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        if not file_exists:
            w.writerow([
                "timestamp_ms",
                "symbol",
                "timeframe",
                "open",
                "high",
                "low",
                "close",
                "volume",
            ])
        for r in rows:
            w.writerow(r)

# --------------------------------------------------
# Runner
# --------------------------------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="Build OHLCV CSV worlds from Binance monthly spot klines.")
    parser.add_argument("--coin", default=COIN)
    parser.add_argument("--quote", default=QUOTE)
    parser.add_argument("--timeframe", default=TIMEFRAME)
    parser.add_argument("--start-year", type=int, default=START_YEAR)
    parser.add_argument("--start-month", type=int, default=START_MONTH)
    parser.add_argument("--months", type=int, default=MONTHS)
    parser.add_argument("--data-dir", default=DATA_DIR)
    parser.add_argument("--stride", type=int, default=STRIDE)
    parser.add_argument("--limit", type=int, default=LIMIT, help="Maximum output rows; 0 means all rows.")
    parser.add_argument("--output", default=OUTPUT, help="Optional output CSV path.")
    parser.add_argument("--market", choices=("spot", "futures_um"), default=MARKET)
    return parser.parse_args()


def run(args=None):
    global COIN, QUOTE, TIMEFRAME, START_YEAR, START_MONTH, MONTHS, DATA_DIR, STRIDE, LIMIT, OUTPUT, MARKET
    args = args if args is not None else parse_args()
    COIN = str(args.coin).upper()
    QUOTE = str(args.quote).upper()
    TIMEFRAME = str(args.timeframe)
    START_YEAR = int(args.start_year)
    START_MONTH = int(args.start_month)
    MONTHS = int(args.months)
    DATA_DIR = str(args.data_dir)
    STRIDE = max(1, int(args.stride))
    LIMIT = max(0, int(args.limit))
    OUTPUT = str(args.output or "")
    MARKET = str(args.market or "spot")
    symbol = f"{COIN}{QUOTE}"
    year_rows = {}
    all_rows = []

    for m in range(MONTHS):
        y, mo = get_year_month(START_YEAR, START_MONTH, m)
        date = f"{y}-{mo:02d}"

        candles = load_month_candles(symbol, TIMEFRAME, date, DATA_DIR, market=MARKET)
        if len(candles) == 0:
            continue

        rows = []
        for i in range(0, len(candles), STRIDE):
            ts, o, h, l, c, v = candles[i]
            rows.append([
                int(ts),
                symbol,
                TIMEFRAME,
                float(o),
                float(h),
                float(l),
                float(c),
                float(v),
            ])

        if OUTPUT:
            all_rows.extend(rows)
            if LIMIT and len(all_rows) >= LIMIT:
                all_rows = all_rows[:LIMIT]
                break
        else:
            year_rows.setdefault(y, []).extend(rows)
            if LIMIT:
                year_rows[y] = year_rows[y][:LIMIT]
                break

    if OUTPUT:
        if os.path.exists(OUTPUT):
            os.remove(OUTPUT)
        append_rows(OUTPUT, all_rows)
        print(f"[DONE] wrote {OUTPUT} rows={len(all_rows)}")
        return

    for y in sorted(year_rows.keys()):
        out_path = year_db_path(symbol, TIMEFRAME, y, DATA_DIR)
        if os.path.exists(out_path):
            os.remove(out_path)
        append_rows(out_path, year_rows[y])

    print("[DONE] OHLCV database build complete")

# --------------------------------------------------
# ENTRYPOINT
# --------------------------------------------------
if __name__ == "__main__":
    run()
