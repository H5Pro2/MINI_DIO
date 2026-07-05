"""Passive sleep/offline afterimage test for MINI_DIO.

The test runs a normal sensory contact phase, then stops new world input and
keeps the same MCM field alive with empty senses. It measures whether the field
re-couples toward center, drifts, or keeps residual load.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from mini_dio.config import Config
from mini_dio.dio_syntax import make_syntax_symbol
from mini_dio.mcm_neuron import MiniMCMField
from mini_dio.mini_world import _empty_senses, build_senses, build_senses_world_relative, build_sensory_profile, load_candles


def _mean(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _mean_abs(values: list[float]) -> float:
    return _mean([abs(float(item or 0.0)) for item in values])


def _afterimages(field: MiniMCMField) -> list[float]:
    return [float(neuron.afterimage) for neuron in field.neurons]


def _scale_senses(value, scale: float):
    if isinstance(value, dict):
        return {key: _scale_senses(item, scale) for key, item in value.items()}
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return float(value) * scale
    return value


def _state_from_afterimage(afterimage_abs: float, signature_abs: float, drift: float) -> str:
    if afterimage_abs < 0.012 and signature_abs < 0.010:
        return "offline_center_quiet"
    if afterimage_abs < 0.045 and drift < 0.010:
        return "offline_center_rekopplung"
    if afterimage_abs >= 0.12 and drift < 0.018:
        return "offline_residual_unrest"
    if drift >= 0.035:
        return "offline_drift"
    return "offline_afterimage"


def run_sleep_test(
    data_path: Path,
    second_data_path: Path | None,
    contact_ticks: int,
    second_contact_ticks: int,
    sleep_ticks: int,
    sense_mode: str,
    label: str,
    offline_mode: str,
    sleep_decay: float,
    sleep_intensity: float,
    cycle_ticks: int,
    memory_rest_multiplier: float,
) -> tuple[dict, list[dict]]:
    candles = load_candles(data_path)
    if not candles:
        raise ValueError(f"no candles loaded: {data_path}")
    second_candles = load_candles(second_data_path) if second_data_path else []

    field = MiniMCMField(neuron_count=getattr(Config, "DIO_MINI_MCM_NEURON_COUNT", 12))
    contact_limit = min(max(1, int(contact_ticks)), max(1, len(candles) - 1))
    second_contact_limit = (
        min(max(1, int(second_contact_ticks)), max(1, len(second_candles) - 1)) if second_candles else 0
    )
    sense_mode = str(sense_mode or "world_relative").strip().lower()
    profile = build_sensory_profile(candles) if sense_mode == "world_relative" else {}
    second_profile = build_sensory_profile(second_candles) if second_candles and sense_mode == "world_relative" else {}
    contact_symbols: Counter[str] = Counter()
    second_contact_symbols: Counter[str] = Counter()
    contact_signatures: list[float] = []
    contact_afterimages: list[float] = []
    last_senses = _empty_senses()
    first_last_senses = _empty_senses()

    for index in range(1, contact_limit + 1):
        if sense_mode == "world_relative":
            senses = build_senses_world_relative(candles, index, profile=profile)
        else:
            senses = build_senses(candles, index)
        last_senses = senses
        field_state = field.step(senses)
        symbol = make_syntax_symbol(senses, float(field_state["signature"]))
        contact_symbols[symbol] += 1
        contact_signatures.append(float(field_state["signature"]))
        contact_afterimages.append(_mean_abs(_afterimages(field)))
    first_last_senses = last_senses

    for index in range(1, second_contact_limit + 1):
        if sense_mode == "world_relative":
            senses = build_senses_world_relative(second_candles, index, profile=second_profile)
        else:
            senses = build_senses(second_candles, index)
        last_senses = senses
        field_state = field.step(senses)
        symbol = make_syntax_symbol(senses, float(field_state["signature"]))
        second_contact_symbols[symbol] += 1
        contact_signatures.append(float(field_state["signature"]))
        contact_afterimages.append(_mean_abs(_afterimages(field)))

    sleep_rows: list[dict] = []
    sleep_symbols: Counter[str] = Counter()
    previous_signature = float(field.last_signature)
    previous_afterimage = _mean_abs(_afterimages(field))
    first_sleep_afterimage = previous_afterimage
    first_sleep_signature = previous_signature
    empty_senses = _empty_senses()
    offline_mode = str(offline_mode or "empty").strip().lower()

    for sleep_tick in range(1, max(1, int(sleep_ticks)) + 1):
        if offline_mode == "damped":
            rest_scale = max(0.0, float(sleep_intensity)) * (max(0.0, float(sleep_decay)) ** (sleep_tick - 1))
            sleep_senses = _scale_senses(last_senses, rest_scale)
            offline_phase = "restreiz"
        elif offline_mode == "cyclic":
            cycle = max(4, int(cycle_ticks))
            quarter = max(1, cycle // 4)
            phase_tick = (sleep_tick - 1) % cycle
            phase_index = phase_tick % quarter
            if phase_tick < quarter:
                offline_phase = "restreiz"
                rest_scale = max(0.0, float(sleep_intensity)) * (max(0.0, float(sleep_decay)) ** phase_index)
                sleep_senses = _scale_senses(last_senses, rest_scale)
            elif phase_tick < quarter * 2:
                offline_phase = "leerphase"
                rest_scale = 0.0
                sleep_senses = empty_senses
            elif phase_tick < quarter * 3:
                offline_phase = "memory_restreiz"
                rest_scale = (
                    max(0.0, float(sleep_intensity))
                    * max(0.0, float(memory_rest_multiplier))
                    * (max(0.0, float(sleep_decay)) ** phase_index)
                )
                memory_source = first_last_senses if second_candles else last_senses
                sleep_senses = _scale_senses(memory_source, rest_scale)
            else:
                offline_phase = "leer_rekopplung"
                rest_scale = 0.0
                sleep_senses = empty_senses
        else:
            rest_scale = 0.0
            sleep_senses = empty_senses
            offline_phase = "leer"
        field_state = field.step(sleep_senses)
        signature = float(field_state["signature"])
        signature_abs = abs(signature)
        afterimage_abs = _mean_abs(_afterimages(field))
        drift = abs(signature - previous_signature)
        afterimage_delta = afterimage_abs - previous_afterimage
        state = _state_from_afterimage(afterimage_abs, signature_abs, drift)
        symbol = make_syntax_symbol(empty_senses, signature)
        sleep_symbols[symbol] += 1
        sleep_rows.append(
            {
                "label": label,
                "source_file": str(data_path),
                "second_source_file": str(second_data_path or ""),
                "sleep_tick": sleep_tick,
                "signature": f"{signature:.9f}",
                "signature_abs": f"{signature_abs:.9f}",
                "afterimage_abs": f"{afterimage_abs:.9f}",
                "signature_drift": f"{drift:.9f}",
                "afterimage_delta": f"{afterimage_delta:.9f}",
                "offline_mode": offline_mode,
                "offline_phase": offline_phase,
                "rest_scale": f"{rest_scale:.9f}",
                "sleep_state": state,
                "sleep_symbol": symbol,
            }
        )
        previous_signature = signature
        previous_afterimage = afterimage_abs

    state_counter = Counter(row["sleep_state"] for row in sleep_rows)
    phase_counter = Counter(row["offline_phase"] for row in sleep_rows)
    final_afterimage = float(sleep_rows[-1]["afterimage_abs"])
    final_signature = float(sleep_rows[-1]["signature"])
    final_signature_abs = abs(final_signature)
    avg_drift = _mean([float(row["signature_drift"]) for row in sleep_rows])
    center_ticks = sum(1 for row in sleep_rows if row["sleep_state"] in {"offline_center_quiet", "offline_center_rekopplung"})
    residual_ticks = sum(1 for row in sleep_rows if row["sleep_state"] in {"offline_residual_unrest", "offline_drift"})
    summary = {
        "label": label,
        "source_file": str(data_path),
        "second_source_file": str(second_data_path or ""),
        "contact_ticks": contact_limit,
        "second_contact_ticks": second_contact_limit,
        "sleep_ticks": len(sleep_rows),
        "sense_mode": sense_mode,
        "offline_mode": offline_mode,
        "sleep_decay": float(sleep_decay),
        "sleep_intensity": float(sleep_intensity),
        "cycle_ticks": int(cycle_ticks),
        "memory_rest_multiplier": float(memory_rest_multiplier),
        "contact_unique_symbols": len(contact_symbols),
        "contact_top_symbol": contact_symbols.most_common(1)[0][0] if contact_symbols else "-",
        "contact_top_symbol_count": contact_symbols.most_common(1)[0][1] if contact_symbols else 0,
        "second_contact_unique_symbols": len(second_contact_symbols),
        "second_contact_top_symbol": second_contact_symbols.most_common(1)[0][0] if second_contact_symbols else "-",
        "second_contact_top_symbol_count": second_contact_symbols.most_common(1)[0][1] if second_contact_symbols else 0,
        "contact_signature_mean": _mean(contact_signatures),
        "contact_afterimage_mean": _mean(contact_afterimages),
        "sleep_unique_symbols": len(sleep_symbols),
        "sleep_top_symbol": sleep_symbols.most_common(1)[0][0] if sleep_symbols else "-",
        "sleep_top_symbol_count": sleep_symbols.most_common(1)[0][1] if sleep_symbols else 0,
        "first_sleep_signature": first_sleep_signature,
        "final_sleep_signature": final_signature,
        "first_sleep_afterimage_abs": first_sleep_afterimage,
        "final_sleep_afterimage_abs": final_afterimage,
        "afterimage_release_ratio": 1.0 - (final_afterimage / max(1e-9, first_sleep_afterimage)),
        "final_signature_abs": final_signature_abs,
        "avg_sleep_signature_drift": avg_drift,
        "center_rekopplung_ratio": center_ticks / max(1, len(sleep_rows)),
        "residual_unrest_ratio": residual_ticks / max(1, len(sleep_rows)),
        "sleep_state_counts": dict(state_counter),
        "offline_phase_counts": dict(phase_counter),
    }
    return summary, sleep_rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Run passive MINI_DIO sleep/offline afterimage diagnostics.")
    parser.add_argument("--data", action="append", required=True, help="CSV world path. Can be supplied multiple times.")
    parser.add_argument("--second-data", action="append", help="Optional second contact world per --data.")
    parser.add_argument("--label", action="append", help="Optional label per --data.")
    parser.add_argument("--contact-ticks", type=int, default=2000)
    parser.add_argument("--second-contact-ticks", type=int, default=1000)
    parser.add_argument("--sleep-ticks", type=int, default=300)
    parser.add_argument("--sense-mode", choices=("fixed", "world_relative"), default="world_relative")
    parser.add_argument("--offline-mode", choices=("empty", "damped", "cyclic"), default="empty")
    parser.add_argument("--sleep-decay", type=float, default=0.92)
    parser.add_argument("--sleep-intensity", type=float, default=0.35)
    parser.add_argument("--cycle-ticks", type=int, default=80)
    parser.add_argument("--memory-rest-multiplier", type=float, default=0.55)
    parser.add_argument("--out-dir", default="debug/sleep_offline_test")
    args = parser.parse_args()

    root = Path.cwd()
    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    labels = list(args.label or [])
    second_items = list(args.second_data or [])
    summaries: list[dict] = []
    rows: list[dict] = []
    for index, item in enumerate(args.data):
        data_path = Path(item)
        if not data_path.is_absolute():
            data_path = root / data_path
        second_data_path = None
        if index < len(second_items):
            second_data_path = Path(second_items[index])
            if not second_data_path.is_absolute():
                second_data_path = root / second_data_path
        label = labels[index] if index < len(labels) else data_path.stem
        summary, sleep_rows = run_sleep_test(
            data_path=data_path,
            second_data_path=second_data_path,
            contact_ticks=args.contact_ticks,
            second_contact_ticks=args.second_contact_ticks,
            sleep_ticks=args.sleep_ticks,
            sense_mode=args.sense_mode,
            label=label,
            offline_mode=args.offline_mode,
            sleep_decay=args.sleep_decay,
            sleep_intensity=args.sleep_intensity,
            cycle_ticks=args.cycle_ticks,
            memory_rest_multiplier=args.memory_rest_multiplier,
        )
        summaries.append(summary)
        rows.extend(sleep_rows)

    summary_path = out_dir / "sleep_offline_summary.json"
    rows_path = out_dir / "sleep_offline_ticks.csv"
    summary_path.write_text(json.dumps(summaries, indent=2, ensure_ascii=False), encoding="utf-8")
    if rows:
        with rows_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(summaries, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
