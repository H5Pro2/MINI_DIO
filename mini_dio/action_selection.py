"""Active action selection compatibility for Mini-DIO.

The passive research core should stay separable from active action selection.
This module keeps the current soft action pressure path intact while making the
dependency explicit.
"""

from __future__ import annotations

from mini_dio.mcm_neuron import ACTION_NAMES


def _clip(value: float, lo: float = -1.0, hi: float = 1.0) -> float:
    try:
        value = float(value)
    except Exception:
        value = 0.0
    if value != value:
        value = 0.0
    return max(lo, min(hi, value))


def _positive_band(value: float) -> float:
    """Map an internal -1..1 state to a soft 0..1 support band."""

    return _clip((float(value or 0.0) + 1.0) * 0.5, 0.0, 1.0)


def organic_action_pressure(action: str, base: float, bias: float, readiness: dict) -> dict:
    """Return soft action pressure without fixed accept/reject thresholds."""

    raw_trade_signal = abs(float(base or 0.0) + float(bias or 0.0))
    best_trade_readiness = max(float(readiness["LONG"]), float(readiness["SHORT"]))
    trade_support = _positive_band(best_trade_readiness)
    wait_bias = 0.0
    trade_caution = 0.0
    memory_support_pressure = 0.0
    signal_diffusion_pressure = 0.0
    if action == "WAIT":
        wait_bias = (1.0 - trade_support) * 0.045
    elif action in ("LONG", "SHORT"):
        action_support = _positive_band(float(readiness[action]))
        signal_support = _clip(raw_trade_signal / (raw_trade_signal + 0.12), 0.0, 1.0)
        memory_support_pressure = (1.0 - action_support) * 0.040
        signal_diffusion_pressure = (1.0 - signal_support) * 0.030
        trade_caution = memory_support_pressure + signal_diffusion_pressure
    return {
        "raw_trade_signal": raw_trade_signal,
        "wait_bias": wait_bias,
        "trade_caution": trade_caution,
        "memory_support_pressure": memory_support_pressure,
        "signal_diffusion_pressure": signal_diffusion_pressure,
    }


def choose_action(action_scores: dict, memory: object, symbol: str, vector: list[float]) -> tuple[str, dict, dict]:
    """Choose the current active action using existing compatibility memory."""

    scores = {}
    diagnostics = {
        action: memory.action_diagnostics(symbol, action, vector=vector)
        for action in ACTION_NAMES
    }
    readiness = {
        action: float(diagnostics[action].get("readiness", 0.0) or 0.0)
        for action in ACTION_NAMES
    }
    for action in ACTION_NAMES:
        base = float(action_scores.get(action, 0.0) or 0.0)
        bias = float(diagnostics[action].get("action_bias", 0.0) or 0.0)
        pressure = organic_action_pressure(action, base, bias, readiness)
        wait_bias = float(pressure["wait_bias"])
        raw_trade_signal = float(pressure["raw_trade_signal"])
        trade_caution = float(pressure["trade_caution"])
        scores[action] = base + bias + wait_bias - trade_caution
        diagnostics[action]["base_score"] = base
        diagnostics[action]["wait_bias"] = wait_bias
        diagnostics[action]["raw_trade_signal"] = raw_trade_signal
        diagnostics[action]["immature_memory_pressure"] = float(pressure["memory_support_pressure"])
        diagnostics[action]["weak_signal_pressure"] = float(pressure["signal_diffusion_pressure"])
        diagnostics[action]["memory_support_pressure"] = float(pressure["memory_support_pressure"])
        diagnostics[action]["signal_diffusion_pressure"] = float(pressure["signal_diffusion_pressure"])
        diagnostics[action]["trade_caution"] = trade_caution
        diagnostics[action]["final_score"] = scores[action]
    action = max(scores, key=scores.get)
    return action, scores, diagnostics
