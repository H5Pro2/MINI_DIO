"""Passive episode memory primitives for Mini-DIO.

This module does not choose actions. It compresses the current sensory and
inner-field state into a passive episode trace so repeated development paths
can be inspected without turning them into gates or strategy rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def _clip(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    try:
        value = float(value)
    except Exception:
        value = 0.0
    if value != value:
        value = 0.0
    return max(lo, min(hi, value))


def _signed_clip(value: float) -> float:
    return max(-1.0, min(1.0, float(value or 0.0)))


def build_mcm_field_effect(senses: dict, reflection_context: dict, temporal_state: dict, neuro_state: dict) -> dict:
    """Return a compact passive MCM-field effect.

    The values describe how current perception appears to affect the inner
    field. They are diagnostic only; no entry, gate or motoric code reads them.
    """

    sehen = dict(senses.get("sehen", {}) or {})
    hoeren = dict(senses.get("hoeren", {}) or {})
    fuehlen = dict(senses.get("fuehlen", {}) or {})
    form_flow = _signed_clip(sehen.get("form_flow", 0.0))
    form_change = _signed_clip(sehen.get("form_change", 0.0))
    form_stability = _signed_clip(sehen.get("form_stability", 0.0))
    energy_tone = _signed_clip(hoeren.get("energy_tone", 0.0))
    energy_shift = _signed_clip(hoeren.get("energy_shift", 0.0))
    coherence = _signed_clip(fuehlen.get("mcm_coherence", 0.0))
    tension = _clip(fuehlen.get("mcm_tension", 0.0))
    asymmetry = _signed_clip(fuehlen.get("mcm_asymmetry", 0.0))
    reflection_carry = _clip(reflection_context.get("reflection_context_carry", 0.0))
    reflection_strain = _clip(reflection_context.get("reflection_context_strain", 0.0))
    reflection_alignment = _clip(reflection_context.get("reflection_context_alignment", 0.0))
    afterimage = _clip(temporal_state.get("mini_afterimage", 0.0))
    recurrence = _clip(temporal_state.get("mini_recurrence_strength", 0.0))
    neuro_support = _clip(neuro_state.get("mini_neuro_support", 0.0))
    neuro_load = _clip(neuro_state.get("mini_neuro_load", 0.0))
    visual_field_gap = _clip(abs(((form_flow * 0.65) + (form_change * 0.35)) - asymmetry), 0.0, 1.0)
    hearing_field_gap = _clip(abs(abs(energy_tone) - tension), 0.0, 1.0)
    sensory_coupling = _clip(
        ((1.0 - visual_field_gap) * 0.36)
        + ((1.0 - hearing_field_gap) * 0.28)
        + (((coherence + 1.0) * 0.5) * 0.20)
        + (reflection_alignment * 0.16)
    )
    mcm_carry_quality = _clip(
        (reflection_carry * 0.34)
        + (sensory_coupling * 0.28)
        + (neuro_support * 0.18)
        + (((form_stability + 1.0) * 0.5) * 0.12)
        + (recurrence * 0.08)
    )
    mcm_strain_quality = _clip(
        (reflection_strain * 0.30)
        + (tension * 0.24)
        + (neuro_load * 0.18)
        + (visual_field_gap * 0.14)
        + (hearing_field_gap * 0.10)
        + (afterimage * 0.04)
    )
    rekopplung_quality = _clip(
        (mcm_carry_quality * 0.42)
        + (reflection_alignment * 0.24)
        + ((1.0 - mcm_strain_quality) * 0.20)
        + (sensory_coupling * 0.14)
    )
    if mcm_carry_quality >= mcm_strain_quality and sensory_coupling >= (1.0 - sensory_coupling):
        field_effect_state = "field_carried"
    elif mcm_strain_quality > mcm_carry_quality and sensory_coupling < (1.0 - sensory_coupling):
        field_effect_state = "field_fragmented"
    elif mcm_strain_quality > mcm_carry_quality:
        field_effect_state = "field_strained"
    else:
        field_effect_state = "field_mixed"
    return {
        "field_effect_state": field_effect_state,
        "mcm_carry_quality": mcm_carry_quality,
        "mcm_strain_quality": mcm_strain_quality,
        "mcm_rekopplung_quality": rekopplung_quality,
        "sensory_coupling": sensory_coupling,
        "visual_field_gap": visual_field_gap,
        "hearing_field_gap": hearing_field_gap,
        "passive_only": True,
        "writes_runtime_memory": False,
        "read_by_mini_dio": False,
        "influences_action": False,
        "is_gate": False,
        "is_motoric": False,
        "is_entry_signal": False,
        "is_direction_signal": False,
    }


@dataclass
class PassiveEpisodeTracker:
    """Compress consecutive field-effect states into passive episode records."""

    max_ticks: int = 12
    active_state: str = ""
    started_at: int = 0
    last_tick: int = 0
    family_counts: dict[str, int] = field(default_factory=dict)
    sums: dict[str, float] = field(default_factory=dict)
    count: int = 0
    previous_state: str = ""

    def _reset(self, state: str, tick: int) -> None:
        self.active_state = state
        self.started_at = int(tick)
        self.last_tick = int(tick)
        self.family_counts = {}
        self.sums = {
            "mcm_carry_quality": 0.0,
            "mcm_strain_quality": 0.0,
            "mcm_rekopplung_quality": 0.0,
            "sensory_coupling": 0.0,
            "visual_field_gap": 0.0,
            "hearing_field_gap": 0.0,
        }
        self.count = 0

    def _record_payload(self, next_state: str = "") -> dict | None:
        if not self.active_state or self.count <= 0:
            return None
        dominant_family = "-"
        if self.family_counts:
            dominant_family = sorted(self.family_counts.items(), key=lambda item: item[1], reverse=True)[0][0]
        transition = f"{self.previous_state or 'start'}->{self.active_state}"
        if next_state:
            transition = f"{self.active_state}->{next_state}"
        denom = max(1, self.count)
        return {
            "episode_state": self.active_state,
            "previous_state": self.previous_state or "start",
            "next_state": next_state or "",
            "transition": transition,
            "start_tick": self.started_at,
            "end_tick": self.last_tick,
            "duration": self.count,
            "dominant_family": dominant_family,
            "family_count": len(self.family_counts),
            "avg_mcm_carry_quality": self.sums["mcm_carry_quality"] / denom,
            "avg_mcm_strain_quality": self.sums["mcm_strain_quality"] / denom,
            "avg_mcm_rekopplung_quality": self.sums["mcm_rekopplung_quality"] / denom,
            "avg_sensory_coupling": self.sums["sensory_coupling"] / denom,
            "avg_visual_field_gap": self.sums["visual_field_gap"] / denom,
            "avg_hearing_field_gap": self.sums["hearing_field_gap"] / denom,
            "passive_only": True,
            "writes_runtime_memory": False,
            "read_by_mini_dio": False,
            "influences_action": False,
            "is_gate": False,
            "is_motoric": False,
            "is_entry_signal": False,
            "is_direction_signal": False,
        }

    def step(self, tick: int, symbol_family: str, effect: dict) -> dict | None:
        state = str(effect.get("field_effect_state", "") or "field_mixed")
        tick = int(tick)
        if not self.active_state:
            self._reset(state, tick)
        should_roll = state != self.active_state or (self.count >= max(1, int(self.max_ticks)))
        payload = None
        if should_roll:
            payload = self._record_payload(next_state=state)
            self.previous_state = self.active_state
            self._reset(state, tick)
        self.last_tick = tick
        family = str(symbol_family or "-") or "-"
        self.family_counts[family] = int(self.family_counts.get(family, 0) or 0) + 1
        for key in self.sums:
            self.sums[key] += float(effect.get(key, 0.0) or 0.0)
        self.count += 1
        return payload

    def flush(self) -> dict | None:
        payload = self._record_payload()
        if self.active_state:
            self.previous_state = self.active_state
        self.active_state = ""
        return payload

    def preview(self) -> dict | None:
        """Return the currently forming passive episode without closing it.

        This is a read-only diagnostic view. It lets local analyses inspect the
        field-episode shape on every tick without writing memory or influencing
        action.
        """

        return self._record_payload()
