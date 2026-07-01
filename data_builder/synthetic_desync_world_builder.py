from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


COMBINED_PHASES = (
    ("ruhige_form_leiser_ton", 900),
    ("ruhige_form_laute_wicks", 1200),
    ("klare_form_leiser_ton", 1100),
    ("gegenlaeufige_form_laut", 1200),
    ("stille_rekopplung", 1000),
    ("bruch_ohne_lautheit", 900),
    ("lauter_nachhall_ohne_form", 1200),
    ("schluss_rekopplung", 1000),
)

VISUAL_STABLE_HEARING_CHAOTIC_PHASES = (
    ("ruhige_form_leiser_ton", 900),
    ("ruhige_form_laute_wicks", 1600),
    ("stille_rekopplung", 900),
    ("lauter_nachhall_ohne_form", 1700),
    ("ruhige_form_laute_wicks", 1400),
    ("schluss_rekopplung", 900),
)

VISUAL_CHAOTIC_HEARING_STABLE_PHASES = (
    ("ruhige_form_leiser_ton", 700),
    ("klare_form_leiser_ton", 1300),
    ("bruch_ohne_lautheit", 1300),
    ("klare_form_leiser_ton", 1000),
    ("bruch_ohne_lautheit", 1200),
    ("stille_rekopplung", 900),
)

PURE_HEARING_PHASES = (
    ("ruhige_form_leiser_ton", 900),
    ("hoeren_steigend_form_stabil", 1400),
    ("hoeren_fallend_form_stabil", 1400),
    ("hoeren_pulsierend_form_stabil", 1600),
    ("hoeren_still_form_stabil", 1000),
    ("hoeren_doppelimpuls_form_stabil", 1200),
    ("schluss_rekopplung", 900),
)

VISUAL_BREAKS_STABLE_PULSE_PHASES = (
    ("ruhige_form_leiser_ton", 800),
    ("stabiler_puls_klare_form", 1200),
    ("formbruch_stabiler_puls", 1400),
    ("rekopplung_stabiler_puls", 900),
    ("zweiter_formbruch_stabiler_puls", 1400),
    ("stille_schlussrekopplung", 900),
)

VISUAL_RECOUPLING_CHAOTIC_TONE_PHASES = (
    ("ruhige_form_leiser_ton", 800),
    ("klare_rekopplung_chaostone", 1200),
    ("visuelle_rekopplung_lautimpuls", 1400),
    ("klare_form_chaotischer_nachhall", 900),
    ("zweite_rekopplung_chaostone", 1400),
    ("stille_schlussrekopplung", 900),
)

PHASE_PRESETS = {
    "combined": COMBINED_PHASES,
    "pure_hearing": PURE_HEARING_PHASES,
    "visual_recoupling_chaotic_tone": VISUAL_RECOUPLING_CHAOTIC_TONE_PHASES,
    "visual_breaks_stable_pulse": VISUAL_BREAKS_STABLE_PULSE_PHASES,
    "visual_stable_hearing_chaotic": VISUAL_STABLE_HEARING_CHAOTIC_PHASES,
    "visual_chaotic_hearing_stable": VISUAL_CHAOTIC_HEARING_STABLE_PHASES,
}


def _phase_at(index: int, phases: tuple[tuple[str, int], ...]) -> tuple[str, int, int]:
    offset = 0
    for name, length in phases:
        if index < offset + length:
            return name, length, index - offset
        offset += length
    name, length = phases[-1]
    return name, length, length - 1


def build_rows(rows: int, start_price: float, symbol: str, timeframe: str, variant: str) -> list[dict[str, object]]:
    phases = PHASE_PRESETS[variant]
    timestamp = 1_704_067_200_000
    step_ms = 300_000
    price = float(start_price)
    out: list[dict[str, object]] = []

    for index in range(rows):
        phase, phase_length, local_index = _phase_at(index, phases)
        t = local_index / max(1, phase_length - 1)
        slow = math.sin(t * math.tau)
        fast = math.sin((index * 0.173) + math.cos(index * 0.037))
        pulse = 1.0 if (index % 17 in {0, 1, 2}) else 0.0

        drift = 0.00002
        body_wave = 0.00010
        wick_scale = 0.0012
        volume_scale = 1.0

        if phase == "ruhige_form_laute_wicks":
            drift = 0.00000
            body_wave = 0.000035
            wick_scale = 0.0120 + (pulse * 0.0180)
            volume_scale = 6.5 + (pulse * 8.0)
        elif phase == "klare_form_leiser_ton":
            drift = 0.00034
            body_wave = 0.00022
            wick_scale = 0.0016
            volume_scale = 0.42
        elif phase == "gegenlaeufige_form_laut":
            drift = -0.00030
            body_wave = 0.00018
            wick_scale = 0.0100 + (abs(fast) * 0.0120)
            volume_scale = 5.8 + abs(fast) * 5.5
        elif phase == "stille_rekopplung":
            drift = 0.00009
            body_wave = 0.00008
            wick_scale = 0.0010
            volume_scale = 0.55
        elif phase == "bruch_ohne_lautheit":
            drift = -0.00072
            body_wave = 0.00030
            wick_scale = 0.0018
            volume_scale = 0.38
        elif phase == "lauter_nachhall_ohne_form":
            drift = 0.00000
            body_wave = 0.000025
            wick_scale = 0.0140 + (abs(slow) * 0.0140)
            volume_scale = 7.4 + abs(slow) * 7.5
        elif phase == "schluss_rekopplung":
            drift = 0.00010
            body_wave = 0.00007
            wick_scale = 0.0012
            volume_scale = 0.85
        elif phase == "hoeren_steigend_form_stabil":
            drift = 0.00003
            body_wave = 0.000035
            wick_scale = 0.0015 + (t * 0.0170)
            volume_scale = 0.65 + (t * 8.5)
        elif phase == "hoeren_fallend_form_stabil":
            drift = 0.00002
            body_wave = 0.000035
            wick_scale = 0.0180 - (t * 0.0165)
            volume_scale = 9.0 - (t * 8.2)
        elif phase == "hoeren_pulsierend_form_stabil":
            drift = 0.00000
            body_wave = 0.000025
            pulse_wave = 0.5 + (0.5 * math.sin(index * 0.51))
            wick_scale = 0.0015 + (pulse_wave * 0.0180)
            volume_scale = 0.70 + (pulse_wave * 9.2)
        elif phase == "hoeren_still_form_stabil":
            drift = 0.00002
            body_wave = 0.000030
            wick_scale = 0.0010
            volume_scale = 0.34
        elif phase == "hoeren_doppelimpuls_form_stabil":
            drift = 0.00001
            body_wave = 0.000025
            local_pulse = 1.0 if (index % 43 in {0, 1, 2, 21, 22}) else 0.0
            wick_scale = 0.0012 + (local_pulse * 0.0250)
            volume_scale = 0.62 + (local_pulse * 12.0)
        elif phase == "stabiler_puls_klare_form":
            drift = 0.00016
            body_wave = 0.00010
            pulse_wave = 0.5 + (0.5 * math.sin(index * 0.33))
            wick_scale = 0.0022 + (pulse_wave * 0.0040)
            volume_scale = 1.2 + (pulse_wave * 1.8)
        elif phase == "formbruch_stabiler_puls":
            drift = -0.00042
            body_wave = 0.00058
            pulse_wave = 0.5 + (0.5 * math.sin(index * 0.33))
            wick_scale = 0.0024 + (pulse_wave * 0.0040)
            volume_scale = 1.2 + (pulse_wave * 1.8)
        elif phase == "rekopplung_stabiler_puls":
            drift = 0.00008
            body_wave = 0.00008
            pulse_wave = 0.5 + (0.5 * math.sin(index * 0.33))
            wick_scale = 0.0020 + (pulse_wave * 0.0035)
            volume_scale = 1.0 + (pulse_wave * 1.4)
        elif phase == "zweiter_formbruch_stabiler_puls":
            drift = 0.00038
            body_wave = 0.00054
            pulse_wave = 0.5 + (0.5 * math.sin(index * 0.33))
            wick_scale = 0.0024 + (pulse_wave * 0.0040)
            volume_scale = 1.2 + (pulse_wave * 1.8)
        elif phase == "stille_schlussrekopplung":
            drift = 0.00005
            body_wave = 0.00005
            wick_scale = 0.0010
            volume_scale = 0.45
        elif phase == "klare_rekopplung_chaostone":
            drift = 0.00012
            body_wave = 0.00007
            chaotic_tone = 0.5 + (0.5 * abs(math.sin(index * 0.79) + math.sin(index * 0.17)) / 2.0)
            wick_scale = 0.0020 + (chaotic_tone * 0.0160)
            volume_scale = 0.9 + (chaotic_tone * 8.5)
        elif phase == "visuelle_rekopplung_lautimpuls":
            drift = 0.00016
            body_wave = 0.00008
            local_pulse = 1.0 if (index % 31 in {0, 1, 2, 14, 15, 16}) else 0.0
            wick_scale = 0.0018 + (local_pulse * 0.0260)
            volume_scale = 0.8 + (local_pulse * 13.0)
        elif phase == "klare_form_chaotischer_nachhall":
            drift = 0.00010
            body_wave = 0.00006
            chaotic_tone = abs(math.sin(index * 0.41) * math.cos(index * 0.113))
            wick_scale = 0.0020 + (chaotic_tone * 0.0220)
            volume_scale = 1.0 + (chaotic_tone * 10.0)
        elif phase == "zweite_rekopplung_chaostone":
            drift = 0.00012
            body_wave = 0.00007
            local_pulse = 1.0 if (index % 47 in {0, 1, 2, 23, 24}) else 0.0
            wick_scale = 0.0018 + (local_pulse * 0.0200)
            volume_scale = 0.85 + (local_pulse * 10.0)

        ret = drift + (slow * body_wave) + (fast * body_wave * 0.35)
        open_price = price
        close = max(0.01, open_price * (1.0 + ret))
        body = abs(close - open_price)
        wick = max(open_price * wick_scale, body * 1.8, open_price * 0.0005)
        high = max(open_price, close) + wick * (0.55 + 0.35 * abs(fast))
        low = max(0.01, min(open_price, close) - wick * (0.55 + 0.35 * (1.0 - abs(fast))))
        volume = 100_000.0 * volume_scale * (1.0 + abs(fast) * 0.22 + abs(slow) * 0.12)

        out.append(
            {
                "timestamp_ms": timestamp + (index * step_ms),
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
    parser.add_argument("--variant", choices=sorted(PHASE_PRESETS), default="combined")
    parser.add_argument("--rows", type=int, default=0)
    parser.add_argument("--start-price", type=float, default=100.0)
    parser.add_argument("--symbol", default="SYN_DESYNC")
    parser.add_argument("--timeframe", default="5m")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    row_count = args.rows or sum(length for _, length in PHASE_PRESETS[args.variant])
    rows = build_rows(row_count, args.start_price, args.symbol, args.timeframe, args.variant)
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
