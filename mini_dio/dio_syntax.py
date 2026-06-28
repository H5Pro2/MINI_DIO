"""DIO-owned syntax helpers for MINI_DIO.

This module creates compact internal words from perception, episode and
MCM-field payloads. It stores nothing and it does not influence action.
"""

from __future__ import annotations


def _clip(value: float, lo: float = -1.0, hi: float = 1.0) -> float:
    try:
        value = float(value)
    except Exception:
        value = 0.0
    if value != value:
        value = 0.0
    return max(lo, min(hi, value))


def _base36(number: int) -> str:
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    number = abs(int(number))
    if number == 0:
        return "0"
    chars = []
    while number:
        number, rem = divmod(number, 36)
        chars.append(alphabet[rem])
    return "".join(reversed(chars))


def _mcm_feldwirkung(senses: dict) -> dict:
    return dict(senses.get("mcm_feldwirkung", {}) or senses.get("fuehlen", {}) or {})


def make_syntax_vector(senses: dict, field_signature: float) -> list[float]:
    """Return DIO's compact sensory vector."""

    feldwirkung = _mcm_feldwirkung(senses)
    rezeptoren = dict(senses.get("rezeptoren", {}) or {})
    return [
        _clip(value)
        for value in [
            rezeptoren.get("visual_form_salience", 0.0),
            rezeptoren.get("visual_memory_recall", 0.0),
            rezeptoren.get("auditory_stimulation", 0.0),
            rezeptoren.get("direct_contact_pressure", 0.0),
            rezeptoren.get("field_intake_pressure", 0.0),
            feldwirkung.get("mcm_coherence", 0.0),
            feldwirkung.get("mcm_tension", 0.0),
            feldwirkung.get("mcm_asymmetry", 0.0),
            field_signature,
        ]
    ]


def make_syntax_symbol(senses: dict, field_signature: float) -> str:
    """Create a compact internal word from sensed state."""

    values = make_syntax_vector(senses, field_signature)
    buckets = [int(round((_clip(v) + 1.0) * 8.0)) for v in values]
    hash_value = 2166136261
    for bucket in buckets:
        hash_value ^= bucket + 17
        hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_{_base36(hash_value).rjust(7, '0')}"


def make_contact_lage_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for a passive contact-lage."""

    state = str(payload.get("contact_lage_state", "") or "")
    values = [
        len(state),
        int(payload.get("runs", 0) or 0),
        int(payload.get("trades_total", 0) or 0),
        int(payload.get("direct_positive_action", 0) or 0),
        int(payload.get("observation_to_positive_action", 0) or 0),
        int(payload.get("held_observation", 0) or 0),
        int(round(float(payload.get("contact_reward_sum", 0.0) or 0.0) * 1000.0)),
    ]
    hash_value = 2166136261
    for value in values:
        hash_value ^= abs(int(value)) + 31
        hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_contact_{_base36(hash_value).rjust(7, '0')}"


def make_reflection_seed_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for a passive reflection seed."""

    family = str(payload.get("symbol_family", "") or "")
    state = str(payload.get("reflection_state", "") or "")
    values = [
        len(family),
        len(state),
        int(payload.get("prior_observation_count", 0) or 0),
        int(payload.get("prior_execution_count", 0) or 0),
        int(payload.get("followup_seen_count", 0) or 0),
        int(payload.get("followup_executed_aligned_count", 0) or 0),
        int(round(float(payload.get("prior_execution_reward_sum", 0.0) or 0.0) * 1000.0)),
        int(round(float(payload.get("followup_executed_reward", 0.0) or 0.0) * 1000.0)),
    ]
    hash_value = 2166136261
    for char in f"{family}|{state}":
        hash_value ^= ord(char) + 43
        hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    for value in values:
        hash_value ^= abs(int(value)) + 43
        hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_reflect_{_base36(hash_value).rjust(7, '0')}"


def make_reflection_map_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for a passive reflection-map snapshot."""

    family = str(payload.get("symbol_family", "") or "")
    state = str(payload.get("reflection_map_state", "") or "")
    reason = str(payload.get("reflection_map_reason", "") or "")
    source_probe = str(payload.get("source_probe", "") or "")
    values = [
        len(family),
        len(state),
        len(reason),
        len(source_probe),
        int(payload.get("seen_count", 0) or 0),
        int(payload.get("executed_count", 0) or 0),
        int(payload.get("observed_count", 0) or 0),
        int(round(float(payload.get("reward_sum", 0.0) or 0.0) * 1000.0)),
        int(round(float(payload.get("best_reward_sum", 0.0) or 0.0) * 1000.0)),
    ]
    hash_value = 2166136261
    for char in f"{family}|{state}|{reason}|{source_probe}":
        hash_value ^= ord(char) + 47
        hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    for value in values:
        hash_value ^= abs(int(value)) + 47
        hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_rmap_{_base36(hash_value).rjust(7, '0')}"


def make_episode_memory_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for a passive episode trace."""

    duration = int(payload.get("duration", 0) or 0)
    duration_band = min(5, max(0, duration // 3))
    values = [
        str(payload.get("episode_state", "") or ""),
        str(payload.get("previous_state", "") or ""),
        str(payload.get("next_state", "") or ""),
        str(payload.get("transition", "") or ""),
        str(payload.get("dominant_family", "") or ""),
        duration_band,
        int(round(float(payload.get("avg_mcm_carry_quality", 0.0) or 0.0) * 10.0)),
        int(round(float(payload.get("avg_mcm_strain_quality", 0.0) or 0.0) * 10.0)),
        int(round(float(payload.get("avg_mcm_rekopplung_quality", 0.0) or 0.0) * 10.0)),
        int(round(float(payload.get("avg_sensory_coupling", 0.0) or 0.0) * 10.0)),
    ]
    hash_value = 2166136261
    for value in values:
        for char in str(value):
            hash_value ^= ord(char) + 53
            hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_episode_{_base36(hash_value).rjust(7, '0')}"


def make_mcm_field_episode_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for passive MCM field-effect recurrence."""

    duration = int(payload.get("duration", 0) or 0)
    duration_band = min(5, max(0, duration // 3))
    values = [
        str(payload.get("episode_state", "") or ""),
        str(payload.get("previous_state", "") or ""),
        str(payload.get("next_state", "") or ""),
        str(payload.get("transition", "") or ""),
        duration_band,
        int(round(float(payload.get("avg_mcm_carry_quality", 0.0) or 0.0) * 10.0)),
        int(round(float(payload.get("avg_mcm_strain_quality", 0.0) or 0.0) * 10.0)),
        int(round(float(payload.get("avg_mcm_rekopplung_quality", 0.0) or 0.0) * 10.0)),
        int(round(float(payload.get("avg_sensory_coupling", 0.0) or 0.0) * 10.0)),
        int(round(float(payload.get("avg_visual_field_gap", 0.0) or 0.0) * 10.0)),
        int(round(float(payload.get("avg_hearing_field_gap", 0.0) or 0.0) * 10.0)),
    ]
    hash_value = 2166136261
    for value in values:
        for char in str(value):
            hash_value ^= ord(char) + 59
            hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_mcm_episode_{_base36(hash_value).rjust(7, '0')}"


def make_role_movement_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for passive role-movement memory."""

    values = [
        str(payload.get("short_token", "") or ""),
        str(payload.get("class_sequence", "") or ""),
        str(payload.get("trend", "") or ""),
        str(payload.get("role_movement_quality", "") or ""),
        str(payload.get("stability_quality", "") or ""),
        str(payload.get("drift_quality", "") or ""),
        int(payload.get("max_rank", 0) or 0),
        int(round(float(payload.get("weight_delta_total", 0.0) or 0.0))),
    ]
    hash_value = 2166136261
    for value in values:
        for char in str(value):
            hash_value ^= ord(char) + 67
            hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_role_{_base36(hash_value).rjust(7, '0')}"


def make_role_maturation_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for passive role-maturation memory."""

    values = [
        str(payload.get("short_token", "") or ""),
        str(payload.get("previous_axis_profile", "") or ""),
        str(payload.get("follow_state", "") or ""),
        str(payload.get("maturation_quality", "") or ""),
        str(payload.get("segment_quality", "") or ""),
        str(payload.get("field_quality", "") or ""),
        str(payload.get("previous_class", "") or ""),
        str(payload.get("follow_class", "") or ""),
        int(payload.get("segments", 0) or 0),
        int(payload.get("worlds", 0) or 0),
        int(round(float(payload.get("follow_weight", 0.0) or 0.0))),
    ]
    hash_value = 2166136261
    for value in values:
        for char in str(value):
            hash_value ^= ord(char) + 71
            hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_mature_{_base36(hash_value).rjust(7, '0')}"


def make_role_shift_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for passive role-shift memory."""

    values = [
        str(payload.get("short_token", "") or ""),
        str(payload.get("from_longterm_class", "") or ""),
        str(payload.get("from_role_class", "") or ""),
        str(payload.get("to_nonbridge_class", "") or ""),
        str(payload.get("to_zone", "") or ""),
        str(payload.get("to_dominant_role", "") or ""),
        str(payload.get("shift_quality", "") or ""),
        int(payload.get("observations", 0) or 0),
        int(payload.get("worlds", 0) or 0),
        int(round(float(payload.get("avg_rekopplung", 0.0) or 0.0) * 1000.0)),
        int(round(float(payload.get("avg_strain", 0.0) or 0.0) * 1000.0)),
    ]
    hash_value = 2166136261
    for value in values:
        for char in str(value):
            hash_value ^= ord(char) + 73
            hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_shift_{_base36(hash_value).rjust(7, '0')}"


def make_fragmentation_symbol(payload: dict) -> str:
    """Create DIO-owned syntax for passive field-fragmentation memory."""

    values = [
        str(payload.get("world_label", "") or ""),
        str(payload.get("fragmentation_class", "") or ""),
        str(payload.get("dominant_surface_class", "") or ""),
        str(payload.get("secondary_surface_class", "") or ""),
        int(payload.get("zones_total", 0) or 0),
        int(payload.get("young_spur_count", 0) or 0),
        int(payload.get("open_count", 0) or 0),
        int(payload.get("rand_count", 0) or 0),
        int(payload.get("weak_center_count", 0) or 0),
        int(payload.get("rekopplung_count", 0) or 0),
        int(round(float(payload.get("avg_strain", 0.0) or 0.0) * 1000.0)),
        int(round(float(payload.get("avg_sensory", 0.0) or 0.0) * 1000.0)),
        int(round(float(payload.get("avg_rekopplung", 0.0) or 0.0) * 1000.0)),
    ]
    hash_value = 2166136261
    for value in values:
        for char in str(value):
            hash_value ^= ord(char) + 79
            hash_value = (hash_value * 16777619) & 0xFFFFFFFF
    return f"dio_frag_{_base36(hash_value).rjust(7, '0')}"


__all__ = [
    "make_contact_lage_symbol",
    "make_episode_memory_symbol",
    "make_fragmentation_symbol",
    "make_mcm_field_episode_symbol",
    "make_role_maturation_symbol",
    "make_role_movement_symbol",
    "make_role_shift_symbol",
    "make_reflection_map_symbol",
    "make_reflection_seed_symbol",
    "make_syntax_symbol",
    "make_syntax_vector",
]
