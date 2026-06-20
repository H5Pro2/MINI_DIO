"""Controlled market world and senses for mini DIO."""

from __future__ import annotations

import csv
import math
from pathlib import Path


def _clip(value: float, lo: float = -1.0, hi: float = 1.0) -> float:
    try:
        value = float(value)
    except Exception:
        value = 0.0
    if value != value:
        value = 0.0
    return max(lo, min(hi, value))


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    values = sorted(float(item) for item in values)
    index = (len(values) - 1) * q
    lower = int(index)
    upper = min(len(values) - 1, lower + 1)
    if lower == upper:
        return values[lower]
    return values[lower] * (upper - index) + values[upper] * (index - lower)


def _robust_scale(values: list[float], fallback: float = 1.0) -> float:
    abs_values = [abs(float(item or 0.0)) for item in values if item == item]
    if not abs_values:
        return max(1e-9, fallback)
    scale = _percentile(abs_values, 0.95)
    if scale <= 1e-9:
        scale = _percentile(abs_values, 0.75)
    return max(1e-9, scale, fallback)


def _soft_signed(value: float, scale: float, gain: float = 0.62) -> float:
    """Soft sensory compression around a world-relative scale."""

    scale = max(1e-9, float(scale or 0.0))
    return math.tanh((float(value or 0.0) / scale) * gain)


def _empty_senses() -> dict:
    mcm_feldwirkung = {"mcm_coherence": 0.0, "mcm_tension": 0.0, "mcm_asymmetry": 0.0}
    perception_regulation_state = {
        "focus_strength": 0.0,
        "distance_need": 0.0,
        "auditory_loudness": 0.0,
        "auditory_softening": 0.0,
        "visual_sharpness": 0.0,
        "visual_blur": 0.0,
        "felt_pressure": 0.0,
        "felt_relaxation": 0.0,
        "visual_focus_tendency": 0.0,
        "visual_distance_tendency": 0.0,
        "auditory_listen_tendency": 0.0,
        "auditory_softening_tendency": 0.0,
        "felt_contact_tendency": 0.0,
        "felt_distance_tendency": 0.0,
        "raw_field_intake_pressure": 0.0,
        "adaptation_potential": 0.0,
        "adapted_field_intake_pressure": 0.0,
        "regulation_damping": 0.0,
        "passive_only": True,
        "influences_action": False,
    }
    return {
        "sehen": {"form_flow": 0.0, "form_stability": 0.0, "form_change": 0.0},
        "hoeren": {"energy_tone": 0.0, "energy_shift": 0.0},
        "perception_regulation_state": dict(perception_regulation_state),
        "organism_adaptation_state": dict(perception_regulation_state),
        "rezeptoren": {
            "visual_form_salience": 0.0,
            "visual_memory_recall": 0.0,
            "auditory_stimulation": 0.0,
            "direct_contact_pressure": 0.0,
            "field_intake_pressure": 0.0,
            "visual_contact": 0.0,
            "auditory_contact": 0.0,
            "contact_pressure": 0.0,
            "contact_alignment": 0.0,
            "contact_asymmetry": 0.0,
            **perception_regulation_state,
            "passive_only": True,
            "influences_action": False,
        },
        "mcm_feldwirkung": dict(mcm_feldwirkung),
        "fuehlen": dict(mcm_feldwirkung),
    }


def _build_receptor_senses(sehen: dict, hoeren: dict) -> dict:
    """Translate sensory intake into MCM field effect.

    Seeing does not directly touch the field. It provides form salience and can
    later couple to memory. Hearing is tonal/energetic stimulation. Direct
    contact is a separate receptor path and is currently empty for chart worlds.
    Compatibility keys keep older reports readable.
    """

    form_flow = _clip(sehen.get("form_flow", 0.0))
    form_stability = _clip(sehen.get("form_stability", 0.0))
    form_change = _clip(sehen.get("form_change", 0.0))
    energy_tone = _clip(hoeren.get("energy_tone", 0.0))
    energy_shift = _clip(hoeren.get("energy_shift", 0.0))

    stability_band = max(0.0, min(1.0, (form_stability + 1.0) * 0.5))
    visual_form_salience = _clip(
        (abs(form_flow) * 0.32)
        + ((1.0 - stability_band) * 0.28)
        + (abs(form_change) * 0.28)
        + (abs(form_flow - form_change) * 0.12),
        0.0,
        1.0,
    )
    visual_memory_recall = 0.0
    auditory_stimulation = _clip((abs(energy_tone) * 0.58) + (abs(energy_shift) * 0.42), 0.0, 1.0)
    direct_contact_pressure = 0.0
    visual_sharpness = _clip(
        (stability_band * 0.48)
        + ((1.0 - abs(form_change)) * 0.24)
        + ((1.0 - abs(form_flow - form_change)) * 0.16)
        + ((1.0 - auditory_stimulation) * 0.12),
        0.0,
        1.0,
    )
    visual_blur = _clip(1.0 - visual_sharpness, 0.0, 1.0)
    auditory_loudness = auditory_stimulation
    auditory_softening = _clip(
        (auditory_loudness * 0.52)
        + (abs(energy_shift) * 0.22)
        + (visual_blur * 0.16)
        + (max(0.0, 0.40 - stability_band) * 0.10),
        0.0,
        1.0,
    )
    contact_alignment = _clip(
        1.0
        - (abs(visual_form_salience - auditory_stimulation) * 0.42)
        - (abs(form_flow - energy_shift) * 0.20),
        0.0,
        1.0,
    )
    raw_field_intake_pressure = _clip(
        (auditory_stimulation * 0.54)
        + (direct_contact_pressure * 0.30)
        + (visual_memory_recall * 0.10)
        + (abs(visual_form_salience - auditory_stimulation) * 0.06)
        + (max(0.0, 0.45 - stability_band) * 0.12),
        0.0,
        1.0,
    )
    distance_need = _clip(
        (raw_field_intake_pressure * 0.34)
        + ((1.0 - contact_alignment) * 0.28)
        + (visual_blur * 0.20)
        + (auditory_softening * 0.18),
        0.0,
        1.0,
    )
    focus_strength = _clip(
        (visual_form_salience * 0.28)
        + (visual_sharpness * 0.26)
        + (contact_alignment * 0.24)
        + ((1.0 - distance_need) * 0.22),
        0.0,
        1.0,
    )
    felt_pressure = _clip(
        (raw_field_intake_pressure * 0.46)
        + (distance_need * 0.24)
        + (direct_contact_pressure * 0.18)
        + ((1.0 - contact_alignment) * 0.12),
        0.0,
        1.0,
    )
    felt_relaxation = _clip(
        (contact_alignment * 0.34)
        + ((1.0 - felt_pressure) * 0.28)
        + (focus_strength * 0.20)
        + (visual_sharpness * 0.18),
        0.0,
        1.0,
    )
    adaptation_potential = _clip(
        (distance_need * 0.18)
        + (auditory_softening * 0.12)
        + (visual_blur * 0.08)
        + (felt_relaxation * 0.06),
        0.0,
        0.42,
    )
    # This is diagnostic only: the MCM field receives receptor intake, while
    # organism adaptation stays observable as an ability state.
    adapted_field_intake_pressure = _clip(raw_field_intake_pressure * (1.0 - adaptation_potential), 0.0, 1.0)
    field_intake_pressure = raw_field_intake_pressure
    contact_asymmetry = _clip(
        (form_flow * 0.40)
        + (form_change * 0.22)
        + (energy_shift * 0.22)
        + (energy_tone * 0.16)
    )
    mcm_coherence = _clip(
        (((contact_alignment * 2.0) - 1.0) * 0.55)
        + (form_stability * 0.25)
        + ((1.0 - field_intake_pressure) * 0.20)
    )

    mcm_feldwirkung = {
        "mcm_coherence": mcm_coherence,
        "mcm_tension": field_intake_pressure,
        "mcm_asymmetry": contact_asymmetry,
    }
    perception_regulation_state = {
        "focus_strength": focus_strength,
        "distance_need": distance_need,
        "auditory_loudness": auditory_loudness,
        "auditory_softening": auditory_softening,
        "visual_sharpness": visual_sharpness,
        "visual_blur": visual_blur,
        "felt_pressure": felt_pressure,
        "felt_relaxation": felt_relaxation,
        "visual_focus_tendency": focus_strength,
        "visual_distance_tendency": visual_blur,
        "auditory_listen_tendency": _clip(1.0 - auditory_softening, 0.0, 1.0),
        "auditory_softening_tendency": auditory_softening,
        "felt_contact_tendency": direct_contact_pressure,
        "felt_distance_tendency": distance_need,
        "raw_field_intake_pressure": raw_field_intake_pressure,
        "adaptation_potential": adaptation_potential,
        "adapted_field_intake_pressure": adapted_field_intake_pressure,
        "regulation_damping": adaptation_potential,
        "passive_only": True,
        "influences_action": False,
    }
    return {
        "sehen": dict(sehen),
        "hoeren": dict(hoeren),
        "perception_regulation_state": dict(perception_regulation_state),
        "organism_adaptation_state": dict(perception_regulation_state),
        "rezeptoren": {
            "visual_form_salience": visual_form_salience,
            "visual_memory_recall": visual_memory_recall,
            "auditory_stimulation": auditory_stimulation,
            "direct_contact_pressure": direct_contact_pressure,
            "field_intake_pressure": field_intake_pressure,
            "visual_contact": visual_form_salience,
            "auditory_contact": auditory_stimulation,
            "contact_pressure": field_intake_pressure,
            "contact_alignment": contact_alignment,
            "contact_asymmetry": contact_asymmetry,
            **perception_regulation_state,
            "passive_only": True,
            "influences_action": False,
        },
        "mcm_feldwirkung": dict(mcm_feldwirkung),
        "fuehlen": dict(mcm_feldwirkung),
    }


def load_candles(path: str | Path) -> list[dict]:
    candles = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            candles.append(
                {
                    "timestamp_ms": int(float(row["timestamp_ms"])),
                    "open": float(row["open"]),
                    "high": float(row["high"]),
                    "low": float(row["low"]),
                    "close": float(row["close"]),
                    "volume": float(row["volume"]),
                }
            )
    return candles


def _sample_primitives(sample: list[dict]) -> dict:
    closes = [item["close"] for item in sample]
    ranges = [max(1e-9, item["high"] - item["low"]) for item in sample]
    volumes = [item["volume"] for item in sample]
    returns = [(closes[i] - closes[i - 1]) / max(1e-9, closes[i - 1]) for i in range(1, len(closes))]
    direction = (closes[-1] - closes[0]) / max(1e-9, closes[0])
    previous_mean = sum(returns[:-1]) / max(1, len(returns) - 1) if len(returns) > 1 else 0.0
    change = returns[-1] - previous_mean if returns else 0.0
    range_base = sum(ranges) / max(1, len(ranges))
    range_shift = ranges[-1] / max(1e-9, range_base) - 1.0
    volume_base = sum(volumes) / max(1, len(volumes))
    volume_shift = volumes[-1] / max(1e-9, volume_base) - 1.0
    energy_shift = (ranges[-1] - ranges[-2]) / max(1e-9, range_base) if len(ranges) > 1 else 0.0
    signed_sum = sum(returns)
    abs_sum = sum(abs(item) for item in returns)
    directional_consistency = abs(signed_sum) / max(1e-9, abs_sum)
    positive = sum(1 for item in returns if item > 0)
    negative = sum(1 for item in returns if item < 0)
    agreement = abs(positive - negative) / max(1, len(returns))
    return {
        "returns": returns,
        "direction": direction,
        "change": change,
        "range_shift": range_shift,
        "volume_shift": volume_shift,
        "energy_shift": energy_shift,
        "agreement": agreement,
        "directional_consistency": directional_consistency,
    }


def build_sensory_profile(candles: list[dict], window: int = 5) -> dict:
    """Build a passive world-relative profile for sensory intake.

    This profile is a research adapter. It keeps different worlds comparable by
    reading movement, change and tone relative to the world's own distribution.
    It does not create actions, gates or direction rules.
    """

    directions: list[float] = []
    changes: list[float] = []
    range_shifts: list[float] = []
    volume_shifts: list[float] = []
    energy_shifts: list[float] = []
    for index in range(len(candles)):
        start = max(0, index - window + 1)
        sample = candles[start : index + 1]
        if len(sample) < 2:
            continue
        primitives = _sample_primitives(sample)
        directions.append(primitives["direction"])
        changes.append(primitives["change"])
        range_shifts.append(primitives["range_shift"])
        volume_shifts.append(primitives["volume_shift"])
        energy_shifts.append(primitives["energy_shift"])

    return {
        "direction_scale": _robust_scale(directions, fallback=0.003),
        "change_scale": _robust_scale(changes, fallback=0.002),
        "range_shift_scale": _robust_scale(range_shifts, fallback=0.35),
        "volume_shift_scale": _robust_scale(volume_shifts, fallback=0.50),
        "energy_shift_scale": _robust_scale(energy_shifts, fallback=0.35),
        "sample_count": len(directions),
        "passive_only": True,
        "influences_action": False,
        "is_gate": False,
        "is_motoric": False,
        "is_entry_signal": False,
        "is_direction_signal": False,
    }


def build_senses(candles: list[dict], index: int, window: int = 5) -> dict:
    start = max(0, index - window + 1)
    sample = candles[start : index + 1]
    if len(sample) < 2:
        return _empty_senses()
    closes = [item["close"] for item in sample]
    ranges = [max(1e-9, item["high"] - item["low"]) for item in sample]
    volumes = [item["volume"] for item in sample]
    returns = [(closes[i] - closes[i - 1]) / max(1e-9, closes[i - 1]) for i in range(1, len(closes))]
    avg_abs_return = sum(abs(item) for item in returns) / max(1, len(returns))
    direction = (closes[-1] - closes[0]) / max(1e-9, closes[0])
    positive = sum(1 for item in returns if item > 0)
    negative = sum(1 for item in returns if item < 0)
    agreement = abs(positive - negative) / max(1, len(returns))
    change = returns[-1] - (sum(returns[:-1]) / max(1, len(returns) - 1) if len(returns) > 1 else 0.0)
    range_base = sum(ranges) / max(1, len(ranges))
    range_shift = ranges[-1] / max(1e-9, range_base) - 1.0
    volume_base = sum(volumes) / max(1, len(volumes))
    volume_shift = volumes[-1] / max(1e-9, volume_base) - 1.0

    form_flow = _clip(direction / 0.018)
    form_stability = _clip((agreement * 2.0) - 1.0)
    form_change = _clip(change / 0.009)
    energy_tone = _clip(((range_shift * 0.62) + (volume_shift * 0.38)) / 1.4)
    energy_shift = _clip((ranges[-1] - ranges[-2]) / max(1e-9, range_base))
    sehen = {
        "form_flow": form_flow,
        "form_stability": form_stability,
        "form_change": form_change,
    }
    hoeren = {
        "energy_tone": energy_tone,
        "energy_shift": energy_shift,
    }
    return _build_receptor_senses(sehen, hoeren)


def build_senses_world_relative(candles: list[dict], index: int, window: int = 5, profile: dict | None = None) -> dict:
    """Build senses with a world-relative intake adapter.

    The adapter keeps the same output shape as ``build_senses`` but avoids
    fixed absolute divisors. It reads each world against its own rhythm and
    amplitude first, then maps the result into the Mini-DIO sensory space.
    """

    start = max(0, index - window + 1)
    sample = candles[start : index + 1]
    if len(sample) < 2:
        return _empty_senses()
    profile = dict(profile or build_sensory_profile(candles, window=window))
    primitives = _sample_primitives(sample)

    direction_scale = float(profile.get("direction_scale", 0.003) or 0.003)
    change_scale = float(profile.get("change_scale", 0.002) or 0.002)
    range_shift_scale = float(profile.get("range_shift_scale", 0.35) or 0.35)
    volume_shift_scale = float(profile.get("volume_shift_scale", 0.50) or 0.50)
    energy_shift_scale = float(profile.get("energy_shift_scale", 0.35) or 0.35)

    form_flow = _soft_signed(primitives["direction"], direction_scale)
    directional_energy = abs(form_flow)
    form_stability = _clip(((primitives["directional_consistency"] * 2.0) - 1.0) * (0.35 + (directional_energy * 0.65)))
    form_change = _soft_signed(primitives["change"], change_scale)

    range_component = _soft_signed(primitives["range_shift"], range_shift_scale)
    volume_component = _soft_signed(primitives["volume_shift"], volume_shift_scale)
    energy_tone = _clip((range_component * 0.62) + (volume_component * 0.38))
    energy_shift = _soft_signed(primitives["energy_shift"], energy_shift_scale)
    sehen = {
        "form_flow": form_flow,
        "form_stability": form_stability,
        "form_change": form_change,
    }
    hoeren = {
        "energy_tone": energy_tone,
        "energy_shift": energy_shift,
    }
    return _build_receptor_senses(sehen, hoeren)


def evaluate_future(candles: list[dict], index: int, action: str, horizon: int = 5, cost: float = 0.0012) -> dict:
    current = candles[index]
    entry = float(current["close"])
    future = candles[index + 1 : min(len(candles), index + 1 + horizon)]
    if not future:
        return {"reward": 0.0, "raw_return": 0.0, "better_entry": entry}
    if action == "LONG":
        exit_price = future[-1]["close"]
        raw_return = (exit_price - entry) / max(1e-9, entry)
        better_entry = min(item["low"] for item in future)
    elif action == "SHORT":
        exit_price = future[-1]["close"]
        raw_return = (entry - exit_price) / max(1e-9, entry)
        better_entry = max(item["high"] for item in future)
    else:
        raw_return = 0.0
        better_entry = entry
    reward = _clip((raw_return - (cost if action in ("LONG", "SHORT") else 0.0)) / 0.012, -2.0, 2.0)
    return {"reward": reward, "raw_return": raw_return, "better_entry": better_entry}


def _local_trade_distance(candles: list[dict], index: int, window: int = 5) -> float:
    start = max(0, index - window + 1)
    sample = candles[start : index + 1]
    if not sample:
        return 0.0
    ranges = [max(0.0, float(item["high"]) - float(item["low"])) for item in sample]
    entry = float(candles[index]["close"])
    avg_range = sum(ranges) / max(1, len(ranges))
    return max(avg_range, entry * 0.001)


def evaluate_trade_event(candles: list[dict], index: int, action: str, horizon: int = 5) -> dict:
    """Evaluate a tiny TP/SL consequence event for mini DIO.

    The distance is derived from recent local candle range. This is not the
    large bot order engine; it is a compact consequence reader for controlled
    Mini-DIO learning.
    """
    action = str(action or "WAIT").upper()
    current = candles[index]
    entry = float(current["close"])
    distance = _local_trade_distance(candles, index)
    if action not in ("LONG", "SHORT") or distance <= 0.0:
        return {
            "outcome_event": "NO_TRADE",
            "event_reward": 0.0,
            "event_raw_return": 0.0,
            "tp_price": entry,
            "sl_price": entry,
            "exit_price": entry,
            "bars_held": 0,
        }

    if action == "LONG":
        tp_price = entry + distance
        sl_price = entry - distance
    else:
        tp_price = entry - distance
        sl_price = entry + distance

    future = candles[index + 1 : min(len(candles), index + 1 + horizon)]
    exit_price = float(future[-1]["close"]) if future else entry
    outcome_event = "TIMEOUT"
    bars_held = len(future)

    for offset, candle in enumerate(future, start=1):
        high = float(candle["high"])
        low = float(candle["low"])
        if action == "LONG":
            tp_touched = high >= tp_price
            sl_touched = low <= sl_price
        else:
            tp_touched = low <= tp_price
            sl_touched = high >= sl_price
        if tp_touched and sl_touched:
            outcome_event = "BOTH_TOUCHED"
            exit_price = entry
            bars_held = offset
            break
        if tp_touched:
            outcome_event = "TP"
            exit_price = tp_price
            bars_held = offset
            break
        if sl_touched:
            outcome_event = "SL"
            exit_price = sl_price
            bars_held = offset
            break

    if action == "LONG":
        raw_return = (exit_price - entry) / max(1e-9, entry)
    else:
        raw_return = (entry - exit_price) / max(1e-9, entry)
    risk_return = distance / max(1e-9, entry)

    if outcome_event == "TP":
        event_reward = 1.0
    elif outcome_event == "SL":
        event_reward = -1.0
    elif outcome_event == "BOTH_TOUCHED":
        event_reward = 0.0
    else:
        event_reward = _clip(raw_return / max(1e-9, risk_return), -1.0, 1.0)

    return {
        "outcome_event": outcome_event,
        "event_reward": event_reward,
        "event_raw_return": raw_return,
        "tp_price": tp_price,
        "sl_price": sl_price,
        "exit_price": exit_price,
        "bars_held": bars_held,
    }


def best_future_action(candles: list[dict], index: int, horizon: int = 5) -> tuple[str, float]:
    long_reward = evaluate_trade_event(candles, index, "LONG", horizon=horizon)["event_reward"]
    short_reward = evaluate_trade_event(candles, index, "SHORT", horizon=horizon)["event_reward"]
    if long_reward <= 0.0 and short_reward <= 0.0:
        return "WAIT", 0.0
    if long_reward >= short_reward:
        return "LONG", long_reward
    return "SHORT", short_reward
