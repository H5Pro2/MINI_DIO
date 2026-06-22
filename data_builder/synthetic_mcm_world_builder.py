from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


HARMONIC_PHASES = (
    ("ruhig", 900, 0.00004, 0.0020, 0.0008, 0.92),
    ("expansion", 900, 0.00055, 0.0048, 0.0022, 1.45),
    ("unruhe", 900, -0.00008, 0.0090, 0.0048, 1.90),
    ("kippnaehe", 900, -0.00042, 0.0125, 0.0066, 2.35),
    ("rekopplung", 900, 0.00018, 0.0060, 0.0028, 1.30),
    ("ruhe_rueckkehr", 900, 0.00002, 0.0024, 0.0010, 0.98),
)


BREAK_RAND_PHASES = (
    ("ruhig_vorlast", 700, 0.00002, 0.0025, 0.0010, 0.95),
    ("oeffnung", 700, 0.00040, 0.0085, 0.0048, 1.70),
    ("bruch_impuls", 700, -0.00120, 0.0180, 0.0120, 3.20),
    ("randflackern", 700, 0.00005, 0.0220, 0.0160, 3.85),
    ("gegenpol", 700, 0.00105, 0.0170, 0.0100, 2.90),
    ("rekopplung", 700, 0.00025, 0.0070, 0.0035, 1.55),
    ("ruhe_nachhall", 700, 0.00001, 0.0030, 0.0014, 1.05),
    ("zweiter_kippimpuls", 500, -0.00085, 0.0150, 0.0110, 3.10),
    ("zweite_rekopplung", 400, 0.00030, 0.0060, 0.0030, 1.35),
)


RAND_DOMINANCE_PHASES = (
    ("ruhig_basis", 600, 0.00001, 0.0020, 0.0010, 0.90),
    ("druckaufbau", 600, -0.00035, 0.0140, 0.0100, 2.60),
    ("laute_randphase", 800, 0.00000, 0.0400, 0.0350, 6.50),
    ("asymmetrischer_bruch", 700, -0.00220, 0.0300, 0.0260, 5.80),
    ("gegenzerrung", 700, 0.00180, 0.0300, 0.0240, 5.20),
    ("ueberreizter_nachhall", 700, -0.00005, 0.0260, 0.0220, 4.60),
    ("rekopplungsversuch", 700, 0.00035, 0.0110, 0.0060, 2.20),
    ("ruhe_restspannung", 600, 0.00002, 0.0050, 0.0030, 1.30),
    ("zweiter_randstoss", 600, -0.00160, 0.0350, 0.0300, 6.10),
    ("schluss_rekopplung", 600, 0.00040, 0.0090, 0.0050, 1.85),
)


PRESETS = {
    "harmonic": HARMONIC_PHASES,
    "bruch_rand": BREAK_RAND_PHASES,
    "rand_dominanz": RAND_DOMINANCE_PHASES,
}


def _scale_phases(
    phases: tuple[tuple[str, int, float, float, float, float], ...],
    phase_scale: float,
) -> tuple[tuple[str, int, float, float, float, float], ...]:
    scale = max(0.05, float(phase_scale or 1.0))
    return tuple(
        (name, max(1, int(round(length * scale))), drift, wave, noise, volume_scale)
        for name, length, drift, wave, noise, volume_scale in phases
    )


def _phase_at(index: int, phases: tuple[tuple[str, int, float, float, float, float], ...]) -> tuple[str, int, float, float, float, float, int]:
    offset = 0
    for phase in phases:
        name, length, drift, wave, noise, volume_scale = phase
        if index < offset + length:
            return name, length, drift, wave, noise, volume_scale, index - offset
        offset += length
    name, length, drift, wave, noise, volume_scale = phases[-1]
    return name, length, drift, wave, noise, volume_scale, length - 1


def build_rows(
    rows: int,
    start_price: float,
    symbol: str,
    timeframe: str,
    preset: str,
    phase_scale: float = 1.0,
) -> list[dict[str, object]]:
    phases = _scale_phases(PRESETS[preset], phase_scale)
    timestamp = 1_704_067_200_000
    step_ms = 300_000
    price = start_price
    out: list[dict[str, object]] = []
    for i in range(rows):
        phase_name, phase_len, drift, wave, noise, volume_scale, local_i = _phase_at(i, phases)
        local_t = local_i / max(1, phase_len - 1)
        slow = math.sin(local_t * math.tau)
        fast = math.sin((local_t * 7.0 + i * 0.013) * math.tau)
        micro = math.sin((i * 0.173) + math.cos(i * 0.019))
        ret = drift + (slow * wave * 0.12) + (fast * noise * 0.06) + (micro * noise * 0.035)
        if phase_name == "kippnaehe":
            ret += -abs(fast) * noise * 0.09
        if phase_name in {"bruch_impuls", "zweiter_kippimpuls"}:
            ret += -abs(fast) * noise * 0.20
        if phase_name in {"asymmetrischer_bruch", "zweiter_randstoss"}:
            ret += -abs(fast) * noise * 0.32
        if phase_name == "laute_randphase":
            ret += math.sin(i * 1.37) * noise * 0.30
        if phase_name == "randflackern":
            ret += math.sin(i * 0.91) * noise * 0.18
        if phase_name in {"gegenpol", "gegenzerrung"}:
            ret += abs(fast) * noise * 0.12
        if phase_name == "ueberreizter_nachhall":
            ret += math.sin(i * 0.53) * noise * 0.14
        if phase_name == "rekopplung":
            ret += (0.5 - abs(local_t - 0.5)) * wave * 0.08
        if phase_name == "zweite_rekopplung":
            ret += (0.5 - abs(local_t - 0.5)) * wave * 0.10

        open_price = price
        close = max(0.01, open_price * (1.0 + ret))
        body = abs(close - open_price)
        phase_range = max(open_price * (wave + noise) * 0.20, body * 1.8, open_price * 0.0008)
        wick_bias = 0.5 + 0.5 * math.sin(i * 0.071)
        high = max(open_price, close) + phase_range * (0.45 + 0.35 * wick_bias)
        low = min(open_price, close) - phase_range * (0.45 + 0.35 * (1.0 - wick_bias))
        low = max(0.01, low)
        range_boost = 1.0
        if phase_name in {
            "bruch_impuls",
            "randflackern",
            "zweiter_kippimpuls",
            "druckaufbau",
            "laute_randphase",
            "asymmetrischer_bruch",
            "gegenzerrung",
            "ueberreizter_nachhall",
            "zweiter_randstoss",
        }:
            range_boost = 1.65
        if phase_name in {"laute_randphase", "zweiter_randstoss"}:
            range_boost = 2.45
        high = max(open_price, close) + (high - max(open_price, close)) * range_boost
        low = min(open_price, close) - (min(open_price, close) - low) * range_boost
        low = max(0.01, low)
        volume = 100_000.0 * volume_scale * (1.0 + abs(fast) * 0.55 + abs(slow) * 0.24)

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
    parser.add_argument("--rows", type=int, default=5400)
    parser.add_argument("--start-price", type=float, default=100.0)
    parser.add_argument("--symbol", default="SYNMCM")
    parser.add_argument("--timeframe", default="5m")
    parser.add_argument("--preset", choices=sorted(PRESETS), default="harmonic")
    parser.add_argument(
        "--phase-scale",
        type=float,
        default=1.0,
        help="Scale only phase lengths. Use this to build compact/stretched versions of the same form sequence.",
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = build_rows(args.rows, args.start_price, args.symbol, args.timeframe, args.preset, args.phase_scale)
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
