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


RECOUPLING_WIDTH_PHASES = (
    ("ruhig_basis", 700, 0.00002, 0.0025, 0.0010, 0.95),
    ("oeffnung_a", 650, 0.00038, 0.0080, 0.0044, 1.55),
    ("rekopplung_a", 850, 0.00022, 0.0060, 0.0028, 1.25),
    ("oeffnung_b", 650, -0.00018, 0.0090, 0.0048, 1.70),
    ("rekopplung_b", 850, 0.00026, 0.0064, 0.0030, 1.30),
    ("gegenpol_weich", 600, 0.00078, 0.0115, 0.0065, 2.05),
    ("rekopplung_c", 900, 0.00018, 0.0058, 0.0026, 1.20),
    ("randimpuls_kurz", 360, -0.00048, 0.0135, 0.0072, 2.25),
    ("rekopplung_d", 900, 0.00024, 0.0062, 0.0029, 1.28),
    ("ruhe_nachhall", 700, 0.00001, 0.0030, 0.0014, 1.02),
)


RECOUPLING_CONTRAST_PHASES = (
    ("ruhe_start", 700, 0.00002, 0.0024, 0.0010, 0.95),
    ("klare_oeffnung", 1300, 0.00055, 0.0115, 0.0068, 1.95),
    ("offene_varianz", 900, -0.00010, 0.0125, 0.0078, 2.10),
    ("lange_rekopplung", 1800, 0.00020, 0.0060, 0.0026, 1.22),
    ("unruhiger_nachhall", 900, 0.00002, 0.0070, 0.0045, 1.45),
    ("zweite_rekopplung", 1400, 0.00024, 0.0056, 0.0024, 1.18),
    ("ruhe_rueckbindung", 900, 0.00001, 0.0030, 0.0013, 1.00),
)


RECOUPLING_PACKET_PHASES = (
    ("ruhe_start", 650, 0.00002, 0.0024, 0.0010, 0.95),
    ("paket_a_oeffnung", 900, 0.00055, 0.0115, 0.0068, 1.95),
    ("paket_a_varianz", 650, -0.00010, 0.0125, 0.0078, 2.10),
    ("paket_a_rekopplung", 950, 0.00020, 0.0060, 0.0026, 1.22),
    ("ruhe_abstand_a", 600, 0.00001, 0.0030, 0.0013, 1.00),
    ("paket_b_oeffnung", 900, -0.00045, 0.0120, 0.0072, 2.00),
    ("paket_b_varianz", 650, 0.00016, 0.0130, 0.0080, 2.15),
    ("paket_b_rekopplung", 950, 0.00023, 0.0058, 0.0025, 1.20),
    ("unruhiger_nachhall", 700, 0.00002, 0.0070, 0.0045, 1.45),
    ("paket_c_oeffnung", 900, 0.00062, 0.0110, 0.0065, 1.90),
    ("paket_c_varianz", 650, -0.00022, 0.0128, 0.0078, 2.10),
    ("paket_c_rekopplung", 950, 0.00019, 0.0056, 0.0024, 1.18),
    ("ruhe_rueckbindung", 700, 0.00001, 0.0030, 0.0013, 1.00),
)


RECOUPLING_OFFSET_PHASES = (
    ("ruhe_start", 650, 0.00002, 0.0022, 0.0010, 0.94),
    ("tragendes_paket_oeffnung", 950, 0.00050, 0.0105, 0.0058, 1.75),
    ("tragendes_paket_rekopplung", 1050, 0.00024, 0.0054, 0.0022, 1.14),
    ("abstand_nachhall", 650, 0.00001, 0.0034, 0.0015, 1.02),
    ("drift_paket_oeffnung", 900, -0.00055, 0.0138, 0.0088, 2.25),
    ("drift_paket_varianz", 850, 0.00008, 0.0150, 0.0100, 2.45),
    ("drift_paket_offen", 750, -0.00018, 0.0125, 0.0082, 2.05),
    ("verzoegerter_nachhall", 850, 0.00000, 0.0068, 0.0048, 1.48),
    ("spaete_rekopplung_anstieg", 900, 0.00026, 0.0060, 0.0028, 1.22),
    ("spaete_rekopplung_bindung", 1100, 0.00018, 0.0048, 0.0020, 1.08),
    ("ruhe_rueckbindung", 800, 0.00001, 0.0028, 0.0012, 0.98),
)


RECOUPLING_COACTIVE_PHASES = (
    ("ruhe_start", 600, 0.00002, 0.0022, 0.0010, 0.94),
    ("zentrum_puls", 850, 0.00034, 0.0065, 0.0028, 1.18),
    ("offene_ueberlagerung", 1150, 0.00005, 0.0145, 0.0095, 2.35),
    ("gegenpol_ueberlagerung", 1000, -0.00018, 0.0155, 0.0105, 2.55),
    ("koaktive_beruehrung", 1200, 0.00008, 0.0135, 0.0090, 2.20),
    ("versetzte_rekopplung", 1200, 0.00020, 0.0068, 0.0034, 1.28),
    ("zweite_koaktive_beruehrung", 1100, -0.00006, 0.0125, 0.0080, 2.05),
    ("spaete_bindung", 1100, 0.00018, 0.0052, 0.0023, 1.10),
    ("ruhe_rueckbindung", 800, 0.00001, 0.0028, 0.0012, 0.98),
)


RECOUPLING_FINE_MILIEU_PHASES = (
    ("ruhe_feinbasis", 900, 0.00001, 0.0014, 0.00055, 0.90),
    ("feine_annaherung", 1000, 0.00006, 0.0018, 0.00065, 0.94),
    ("leiser_gegenzug", 900, -0.00004, 0.0019, 0.00072, 0.96),
    ("feine_driftbindung", 1200, 0.00003, 0.0017, 0.00060, 0.93),
    ("ruhige_rollennaehe", 1300, 0.00005, 0.0019, 0.00066, 0.95),
    ("sanfte_rekopplung", 1500, 0.00008, 0.0016, 0.00052, 0.91),
    ("nachhallbindung", 1200, 0.00002, 0.0015, 0.00050, 0.90),
    ("zweite_feinbindung", 1200, 0.00007, 0.0017, 0.00058, 0.92),
    ("ruhe_rueckbindung", 900, 0.00001, 0.0013, 0.00048, 0.88),
)


RECOUPLING_FINE_DIFFERENCE_PHASES = (
    ("ruhe_feinbasis", 800, 0.00001, 0.0014, 0.00055, 0.90),
    ("mikro_impuls_links", 900, 0.00011, 0.0023, 0.00090, 1.02),
    ("leiser_gegenzug", 850, -0.00007, 0.0022, 0.00086, 1.00),
    ("feine_driftbindung", 1100, 0.00003, 0.0018, 0.00062, 0.94),
    ("range_puls_kurz", 700, 0.00002, 0.0032, 0.00115, 1.12),
    ("ruhige_rollennaehe", 1100, 0.00006, 0.0021, 0.00076, 0.97),
    ("mikro_impuls_rechts", 900, -0.00009, 0.0025, 0.00095, 1.04),
    ("sanfte_rekopplung", 1300, 0.00008, 0.0017, 0.00055, 0.92),
    ("nachhallbindung", 1000, 0.00002, 0.0015, 0.00050, 0.90),
    ("zweite_feinbindung", 1000, 0.00007, 0.0019, 0.00066, 0.94),
    ("ruhe_rueckbindung", 800, 0.00001, 0.0013, 0.00048, 0.88),
)


PRESETS = {
    "harmonic": HARMONIC_PHASES,
    "bruch_rand": BREAK_RAND_PHASES,
    "rand_dominanz": RAND_DOMINANCE_PHASES,
    "rekopplungsbreite_koaktiv": RECOUPLING_COACTIVE_PHASES,
    "rekopplungsbreite_feindifferenz": RECOUPLING_FINE_DIFFERENCE_PHASES,
    "rekopplungsbreite_feinmilieu": RECOUPLING_FINE_MILIEU_PHASES,
    "rekopplungsbreite_versatz": RECOUPLING_OFFSET_PHASES,
    "rekopplungsbreite_pakete": RECOUPLING_PACKET_PHASES,
    "rekopplungsbreite_kontrast": RECOUPLING_CONTRAST_PHASES,
    "rekopplungsbreite": RECOUPLING_WIDTH_PHASES,
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


def _order_phases(
    phases: tuple[tuple[str, int, float, float, float, float], ...],
    phase_order: str,
) -> tuple[tuple[str, int, float, float, float, float], ...]:
    if not str(phase_order or "").strip():
        return phases
    phase_by_name = {name: phase for phase in phases for name in [phase[0]]}
    ordered_names = [item.strip() for item in str(phase_order).split(",") if item.strip()]
    missing = [name for name in ordered_names if name not in phase_by_name]
    if missing:
        raise ValueError(f"unknown phase names: {', '.join(missing)}")
    if len(set(ordered_names)) != len(ordered_names):
        raise ValueError("phase-order contains duplicate phase names")
    remaining = [phase for phase in phases if phase[0] not in set(ordered_names)]
    return tuple(phase_by_name[name] for name in ordered_names) + tuple(remaining)


def _override_phase_lengths(
    phases: tuple[tuple[str, int, float, float, float, float], ...],
    phase_lengths: str,
) -> tuple[tuple[str, int, float, float, float, float], ...]:
    if not str(phase_lengths or "").strip():
        return phases
    overrides: dict[str, int] = {}
    for item in str(phase_lengths).split(","):
        if not item.strip():
            continue
        if "=" not in item:
            raise ValueError("phase-lengths entries must use name=length")
        name, raw_length = item.split("=", 1)
        name = name.strip()
        if not name:
            raise ValueError("phase-lengths contains an empty phase name")
        overrides[name] = max(1, int(float(raw_length.strip())))
    known = {phase[0] for phase in phases}
    missing = [name for name in overrides if name not in known]
    if missing:
        raise ValueError(f"unknown phase names: {', '.join(missing)}")
    return tuple(
        (name, overrides.get(name, length), drift, wave, noise, volume_scale)
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


def _phase_family(phase_name: str) -> str:
    if phase_name in {"mikro_impuls_links", "mikro_impuls_rechts", "range_puls_kurz"}:
        return "feindifferenz"
    if phase_name in {"feine_annaherung", "leiser_gegenzug", "feine_driftbindung", "ruhige_rollennaehe", "zweite_feinbindung"}:
        return "feinmilieu"
    if phase_name in {"sanfte_rekopplung", "nachhallbindung"}:
        return "feinrekopplung"
    if phase_name in {"offene_ueberlagerung", "gegenpol_ueberlagerung", "koaktive_beruehrung", "zweite_koaktive_beruehrung"}:
        return "koaktiv"
    if phase_name in {"zentrum_puls", "versetzte_rekopplung", "spaete_bindung"}:
        return "rekopplung"
    if phase_name.startswith("tragendes_paket"):
        return "tragendes_paket"
    if phase_name.startswith("drift_paket"):
        return "drift_paket"
    if phase_name.startswith("spaete_rekopplung"):
        return "rekopplung"
    if phase_name == "verzoegerter_nachhall":
        return "verzoegerter_nachhall"
    if "_oeffnung" in phase_name:
        return "oeffnung"
    if "_varianz" in phase_name:
        return "oeffnung"
    if "_rekopplung" in phase_name:
        return "rekopplung"
    if phase_name.startswith("oeffnung_"):
        return "oeffnung"
    if phase_name.startswith("rekopplung_"):
        return "rekopplung"
    if phase_name in {"lange_rekopplung", "zweite_rekopplung", "ruhe_rueckbindung"}:
        return "rekopplung"
    if phase_name in {"klare_oeffnung", "offene_varianz"}:
        return "oeffnung"
    if phase_name == "unruhiger_nachhall":
        return "unruhiger_nachhall"
    if phase_name.startswith("randimpuls_"):
        return "randimpuls"
    return phase_name


def build_rows(
    rows: int,
    start_price: float,
    symbol: str,
    timeframe: str,
    preset: str,
    phase_scale: float = 1.0,
    phase_order: str = "",
    phase_lengths: str = "",
) -> list[dict[str, object]]:
    phases = _override_phase_lengths(_order_phases(_scale_phases(PRESETS[preset], phase_scale), phase_order), phase_lengths)
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
        phase_family = _phase_family(phase_name)
        if phase_family == "kippnaehe":
            ret += -abs(fast) * noise * 0.09
        if phase_family in {"bruch_impuls", "zweiter_kippimpuls"}:
            ret += -abs(fast) * noise * 0.20
        if phase_family in {"asymmetrischer_bruch", "zweiter_randstoss"}:
            ret += -abs(fast) * noise * 0.32
        if phase_family == "laute_randphase":
            ret += math.sin(i * 1.37) * noise * 0.30
        if phase_family == "randflackern":
            ret += math.sin(i * 0.91) * noise * 0.18
        if phase_family in {"gegenpol", "gegenzerrung", "gegenpol_weich"}:
            ret += abs(fast) * noise * 0.12
        if phase_family == "ueberreizter_nachhall":
            ret += math.sin(i * 0.53) * noise * 0.14
        if phase_family == "rekopplung":
            ret += (0.5 - abs(local_t - 0.5)) * wave * 0.08
        if phase_family == "zweite_rekopplung":
            ret += (0.5 - abs(local_t - 0.5)) * wave * 0.10
        if phase_family == "oeffnung":
            ret += math.sin(i * 0.43) * noise * 0.06
        if phase_family == "unruhiger_nachhall":
            ret += math.sin(i * 0.31) * noise * 0.08 + math.cos(i * 0.097) * noise * 0.05
        if phase_family == "tragendes_paket":
            ret += (0.5 - abs(local_t - 0.5)) * wave * 0.09 + math.sin(i * 0.19) * noise * 0.025
        if phase_family == "drift_paket":
            ret += math.sin(i * 0.37) * noise * 0.11 - abs(math.sin(i * 0.11)) * noise * 0.055
        if phase_family == "verzoegerter_nachhall":
            ret += math.sin(i * 0.17) * noise * 0.10 + math.cos(i * 0.061) * noise * 0.06
        if phase_family == "koaktiv":
            ret += math.sin(i * 0.29) * noise * 0.13
            ret += math.cos(i * 0.071) * wave * 0.075
            ret += math.sin(local_t * math.tau * 2.0) * wave * 0.055
        if phase_family == "feinmilieu":
            ret += math.sin(i * 0.041) * wave * 0.045
            ret += math.cos(i * 0.067) * noise * 0.035
            ret += (0.5 - abs(local_t - 0.5)) * wave * 0.030
        if phase_family == "feindifferenz":
            ret += math.sin(i * 0.113) * wave * 0.080
            ret += math.cos(i * 0.181) * noise * 0.060
            ret += math.sin(local_t * math.tau * 3.0) * wave * 0.050
        if phase_family == "feinrekopplung":
            ret += (0.5 - abs(local_t - 0.5)) * wave * 0.075
            ret += math.sin(i * 0.029) * noise * 0.020
        if phase_family == "randimpuls":
            ret += -abs(fast) * noise * 0.11 + math.sin(i * 0.77) * noise * 0.07

        open_price = price
        close = max(0.01, open_price * (1.0 + ret))
        body = abs(close - open_price)
        phase_range = max(open_price * (wave + noise) * 0.20, body * 1.8, open_price * 0.0008)
        wick_bias = 0.5 + 0.5 * math.sin(i * 0.071)
        high = max(open_price, close) + phase_range * (0.45 + 0.35 * wick_bias)
        low = min(open_price, close) - phase_range * (0.45 + 0.35 * (1.0 - wick_bias))
        low = max(0.01, low)
        range_boost = 1.0
        if phase_family in {
            "bruch_impuls",
            "randflackern",
            "zweiter_kippimpuls",
            "druckaufbau",
            "laute_randphase",
            "asymmetrischer_bruch",
            "gegenzerrung",
            "ueberreizter_nachhall",
            "unruhiger_nachhall",
            "verzoegerter_nachhall",
            "drift_paket",
            "koaktiv",
            "zweiter_randstoss",
            "randimpuls",
        }:
            range_boost = 1.65
        if phase_family in {"laute_randphase", "zweiter_randstoss"}:
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
    parser.add_argument(
        "--phase-order",
        default="",
        help="Optional comma-separated phase order. Missing phases keep their original order after the listed phases.",
    )
    parser.add_argument(
        "--phase-lengths",
        default="",
        help="Optional comma-separated length overrides, for example rekopplung=1400,randflackern=700.",
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = build_rows(
        args.rows,
        args.start_price,
        args.symbol,
        args.timeframe,
        args.preset,
        args.phase_scale,
        args.phase_order,
        args.phase_lengths,
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
