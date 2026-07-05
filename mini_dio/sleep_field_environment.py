"""Passive sleep field environment for MINI_DIO.

The environment does not replay a fixed sequence. It offers stored MCM-field
episodes as a resonance space and lets the current field state determine which
episode qualities become active.
"""

from __future__ import annotations

import json
from pathlib import Path

from mini_dio.mini_world import _empty_senses


def _clip(value: float, lo: float = -1.0, hi: float = 1.0) -> float:
    try:
        value = float(value)
    except Exception:
        value = 0.0
    if value != value:
        value = 0.0
    return max(lo, min(hi, value))


def _clip01(value: float) -> float:
    return _clip(value, 0.0, 1.0)


def load_mcm_episode_roles(memory_path: Path, limit: int = 24) -> list[dict]:
    """Load passive MCM episode roles from a MINI_DIO memory JSON file."""

    memory_path = Path(memory_path)
    if not memory_path.exists():
        raise FileNotFoundError(str(memory_path))
    data = json.loads(memory_path.read_text(encoding="utf-8"))
    episodes = list(dict(data.get("mcm_field_episode_memory", {}) or {}).values())
    roles: list[dict] = []
    for item in episodes:
        if not isinstance(item, dict):
            continue
        symbol = str(item.get("mcm_field_episode_symbol", "") or "")
        if not symbol:
            continue
        carry = _clip01(item.get("avg_mcm_carry_quality", 0.0))
        strain = _clip01(item.get("avg_mcm_strain_quality", 0.0))
        rekopplung = _clip01(item.get("avg_mcm_rekopplung_quality", 0.0))
        coupling = _clip01(item.get("avg_sensory_coupling", 0.0))
        visual_gap = _clip01(item.get("avg_visual_field_gap", 0.0))
        hearing_gap = _clip01(item.get("avg_hearing_field_gap", 0.0))
        seen_count = int(item.get("seen_count", 0) or 0)
        duration = int(item.get("duration", 0) or 0)
        signature_proxy = _clip((carry - strain) * 0.72 + (rekopplung - 0.5) * 0.28)
        tension_proxy = _clip01((strain * 0.62) + ((1.0 - rekopplung) * 0.24) + ((1.0 - coupling) * 0.14))
        asymmetry_proxy = _clip((visual_gap - hearing_gap) * 0.62 + (strain - carry) * 0.20)
        base_weight = (
            (seen_count * 0.18)
            + (min(duration, 240) / 240.0 * 0.34)
            + (rekopplung * 0.22)
            + (carry * 0.18)
            + ((1.0 - strain) * 0.08)
        )
        roles.append(
            {
                "symbol": symbol,
                "episode_state": str(item.get("episode_state", "") or ""),
                "transition": str(item.get("transition", "") or ""),
                "seen_count": seen_count,
                "duration": duration,
                "carry": carry,
                "strain": strain,
                "rekopplung": rekopplung,
                "coupling": coupling,
                "visual_gap": visual_gap,
                "hearing_gap": hearing_gap,
                "signature_proxy": signature_proxy,
                "tension_proxy": tension_proxy,
                "asymmetry_proxy": asymmetry_proxy,
                "base_weight": max(0.0001, base_weight),
            }
        )
    roles.sort(key=lambda role: float(role["base_weight"]), reverse=True)
    return roles[: max(1, int(limit))]


def _role_resonance(role: dict, current_signature: float, tick: int) -> float:
    """Return field-state dependent resonance for one stored episode role."""

    signature_distance = abs(float(current_signature) - float(role.get("signature_proxy", 0.0) or 0.0))
    proximity = max(0.0, 1.0 - min(1.0, signature_distance))
    # Gentle, deterministic role breathing keeps this a milieu, not a fixed order.
    symbol = str(role.get("symbol", "") or "")
    phase_seed = sum((index + 1) * ord(char) for index, char in enumerate(symbol)) % 29
    slow_phase = ((tick + phase_seed) % 11) / 10.0
    fast_phase = ((tick * 3 + phase_seed) % 7) / 6.0
    breathing = 0.72 + (slow_phase * 0.20) + (fast_phase * 0.08)
    field_fit = 1.0 - min(1.0, abs(float(role.get("tension_proxy", 0.0) or 0.0) - abs(float(current_signature))))
    return float(role.get("base_weight", 0.0) or 0.0) * proximity * field_fit * breathing


def build_sleep_environment_senses(
    roles: list[dict],
    current_signature: float,
    tick: int,
    intensity: float = 0.42,
    max_active_roles: int = 5,
    activation_floor: float = 0.82,
) -> tuple[dict, list[dict]]:
    """Build passive MCM-field senses from resonating episode roles."""

    if not roles:
        return _empty_senses(), []
    scored = []
    for role in roles:
        score = _role_resonance(role, current_signature=current_signature, tick=tick)
        if score > 0.0:
            scored.append((score, role))
    scored.sort(key=lambda item: item[0], reverse=True)
    top_score = scored[0][0] if scored else 0.0
    floor = max(0.0, min(0.99, float(activation_floor)))
    active = [
        (score, role)
        for score, role in scored[: max(1, int(max_active_roles))]
        if top_score <= 0.0 or score >= top_score * floor
    ]
    if not active and scored:
        active = [scored[0]]
    total = sum(score for score, _role in active) or 1.0
    coherence = sum((score / total) * float(role["signature_proxy"]) for score, role in active)
    tension = sum((score / total) * float(role["tension_proxy"]) for score, role in active)
    asymmetry = sum((score / total) * float(role["asymmetry_proxy"]) for score, role in active)
    coupling = sum((score / total) * float(role["coupling"]) for score, role in active)
    visual_gap = sum((score / total) * float(role["visual_gap"]) for score, role in active)
    hearing_gap = sum((score / total) * float(role["hearing_gap"]) for score, role in active)
    scale = _clip01(intensity)
    senses = _empty_senses()
    senses["mcm_feldwirkung"] = {
        "mcm_coherence": _clip(coherence * scale),
        "mcm_tension": _clip01(tension * scale),
        "mcm_asymmetry": _clip(asymmetry * scale),
    }
    senses["fuehlen"] = dict(senses["mcm_feldwirkung"])
    senses["rezeptoren"].update(
        {
            "field_intake_pressure": _clip01(tension * scale),
            "contact_alignment": _clip01(coupling),
            "visual_form_salience": _clip01((1.0 - visual_gap) * scale),
            "auditory_stimulation": _clip01((1.0 - hearing_gap) * scale),
            "passive_only": True,
            "influences_action": False,
        }
    )
    active_roles = [
        {
            "symbol": str(role.get("symbol", "") or ""),
            "resonance": score / total,
            "episode_state": str(role.get("episode_state", "") or ""),
            "transition": str(role.get("transition", "") or ""),
        }
        for score, role in active
    ]
    return senses, active_roles


__all__ = [
    "build_sleep_environment_senses",
    "load_mcm_episode_roles",
]
