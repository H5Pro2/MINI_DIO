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


def _mcm_feldwirkung(senses: dict) -> dict:
    return dict(senses.get("mcm_feldwirkung", {}) or senses.get("fuehlen", {}) or {})


def _weighted_episode_average(episodes: list[dict], key: str) -> float:
    weighted_sum = 0.0
    total_weight = 0.0
    for item in episodes:
        seen = max(1.0, float(item.get("seen_count", 1.0) or 1.0))
        weighted_sum += _clip(item.get(key, 0.0)) * seen
        total_weight += seen
    if total_weight <= 0.0:
        return 0.0
    return _clip(weighted_sum / total_weight)


def _seen_sum(episodes: list[dict]) -> float:
    return sum(max(1.0, float(item.get("seen_count", 1.0) or 1.0)) for item in episodes)


def _blend_memory(global_value: float, role_value: float, path_value: float, role_experience: float, path_experience: float) -> float:
    role_weight = role_experience * 0.38
    path_weight = path_experience * 0.24
    global_weight = max(0.20, 1.0 - role_weight - path_weight)
    total = global_weight + role_weight + path_weight
    return _clip(((global_value * global_weight) + (role_value * role_weight) + (path_value * path_weight)) / total)


def _dominant_label(items: dict[str, float]) -> str:
    clean = {key: _clip(value) for key, value in items.items()}
    if not clean:
        return "unknown"
    return max(clean, key=clean.get)


def build_adaptive_rekopplung_state(
    field_effect: dict,
    memory_data: dict | None,
    symbol_family: str = "",
    field_role: str = "",
    field_transition: str = "",
) -> dict:
    """Build a passive experience-weighted recoupling reading.

    The original ``mcm_rekopplung_quality`` stays as the stable reference. This
    adaptive reading lets previous passive episode traces shift how carry,
    alignment, strain relief and sensory coupling are weighted.
    """

    episodes = list(dict((memory_data or {}).get("episode_memory", {}) or {}).values())
    same_family = [
        dict(item or {})
        for item in episodes
        if symbol_family and str((item or {}).get("dominant_family", "") or "") == symbol_family
    ]
    candidates = same_family or [dict(item or {}) for item in episodes]
    role_candidates = [
        dict(item or {})
        for item in candidates
        if field_role
        and (
            str((item or {}).get("episode_state", "") or "") == field_role
            or str((item or {}).get("passive_mcm_effect_class", "") or "") == field_role.replace("field_", "", 1)
        )
    ]
    path_candidates = [
        dict(item or {})
        for item in candidates
        if field_transition and str((item or {}).get("transition", "") or "") == field_transition
    ]
    if not candidates:
        return {
            "mcm_adaptive_rekopplung_quality": _clip(field_effect.get("mcm_rekopplung_quality", 0.0)),
            "mcm_adaptive_rekopplung_state": "adaptive_untrained",
            "mcm_adaptive_rekopplung_experience": 0.0,
            "mcm_adaptive_role_experience": 0.0,
            "mcm_adaptive_path_experience": 0.0,
            "mcm_adaptive_milieu_state": "milieu_untrained",
            "mcm_adaptive_weight_carry": 0.42,
            "mcm_adaptive_weight_alignment": 0.24,
            "mcm_adaptive_weight_strain_relief": 0.20,
            "mcm_adaptive_weight_sensory": 0.14,
        }

    total_seen = _seen_sum(candidates)
    experience = _clip(total_seen / 18.0)
    role_experience = _clip(_seen_sum(role_candidates) / 12.0) if role_candidates else 0.0
    path_experience = _clip(_seen_sum(path_candidates) / 8.0) if path_candidates else 0.0
    carry_memory = _weighted_episode_average(candidates, "avg_mcm_carry_quality")
    strain_memory = _weighted_episode_average(candidates, "avg_mcm_strain_quality")
    rekopplung_memory = _weighted_episode_average(candidates, "avg_mcm_rekopplung_quality")
    sensory_memory = _weighted_episode_average(candidates, "avg_sensory_coupling")
    role_carry_memory = _weighted_episode_average(role_candidates or candidates, "avg_mcm_carry_quality")
    role_strain_memory = _weighted_episode_average(role_candidates or candidates, "avg_mcm_strain_quality")
    role_rekopplung_memory = _weighted_episode_average(role_candidates or candidates, "avg_mcm_rekopplung_quality")
    role_sensory_memory = _weighted_episode_average(role_candidates or candidates, "avg_sensory_coupling")
    path_carry_memory = _weighted_episode_average(path_candidates or candidates, "avg_mcm_carry_quality")
    path_strain_memory = _weighted_episode_average(path_candidates or candidates, "avg_mcm_strain_quality")
    path_rekopplung_memory = _weighted_episode_average(path_candidates or candidates, "avg_mcm_rekopplung_quality")
    path_sensory_memory = _weighted_episode_average(path_candidates or candidates, "avg_sensory_coupling")
    carry_memory = _blend_memory(carry_memory, role_carry_memory, path_carry_memory, role_experience, path_experience)
    strain_memory = _blend_memory(strain_memory, role_strain_memory, path_strain_memory, role_experience, path_experience)
    rekopplung_memory = _blend_memory(
        rekopplung_memory,
        role_rekopplung_memory,
        path_rekopplung_memory,
        role_experience,
        path_experience,
    )
    sensory_memory = _blend_memory(
        sensory_memory,
        role_sensory_memory,
        path_sensory_memory,
        role_experience,
        path_experience,
    )

    raw_weights = {
        "carry": 0.24 + (carry_memory * 0.30) + (rekopplung_memory * 0.10),
        "alignment": 0.16 + (rekopplung_memory * 0.26),
        "strain_relief": 0.14 + ((1.0 - strain_memory) * 0.34),
        "sensory": 0.10 + (sensory_memory * 0.28),
    }
    total = sum(raw_weights.values()) or 1.0
    weights = {key: _clip(value / total) for key, value in raw_weights.items()}
    adaptive = _clip(
        (_clip(field_effect.get("mcm_carry_quality", 0.0)) * weights["carry"])
        + (_clip(field_effect.get("reflection_alignment", 0.0)) * weights["alignment"])
        + ((1.0 - _clip(field_effect.get("mcm_strain_quality", 0.0))) * weights["strain_relief"])
        + (_clip(field_effect.get("sensory_coupling", 0.0)) * weights["sensory"])
    )
    static = _clip(field_effect.get("mcm_rekopplung_quality", 0.0))
    delta = adaptive - static
    state = _dominant_label(
        {
            "adaptive_jung": 1.0 - experience,
            "adaptive_rekopplung_angehoben": _clip(delta, 0.0, 1.0) * experience,
            "adaptive_rekopplung_gedaempft": _clip(-delta, 0.0, 1.0) * experience,
            "adaptive_rekopplung_nahe_statisch": (1.0 - _clip(abs(delta), 0.0, 1.0)) * experience,
        }
    )
    milieu_state = _dominant_label(
        {
            "milieu_rolle_und_pfad_getragen": role_experience * path_experience,
            "milieu_rollennah": role_experience * (1.0 - path_experience),
            "milieu_pfadnah": path_experience * (1.0 - role_experience),
            "milieu_offen": (1.0 - role_experience) * (1.0 - path_experience),
        }
    )
    return {
        "mcm_adaptive_rekopplung_quality": adaptive,
        "mcm_adaptive_rekopplung_state": state,
        "mcm_adaptive_rekopplung_experience": experience,
        "mcm_adaptive_role_experience": role_experience,
        "mcm_adaptive_path_experience": path_experience,
        "mcm_adaptive_milieu_state": milieu_state,
        "mcm_adaptive_weight_carry": weights["carry"],
        "mcm_adaptive_weight_alignment": weights["alignment"],
        "mcm_adaptive_weight_strain_relief": weights["strain_relief"],
        "mcm_adaptive_weight_sensory": weights["sensory"],
    }


def build_mcm_field_effect(
    senses: dict,
    reflection_context: dict,
    temporal_state: dict,
    neuro_state: dict,
    rekopplung_factor: float = 1.0,
) -> dict:
    """Return a compact passive MCM-field effect.

    The values describe how current perception appears to affect the inner
    field. They are diagnostic only; no entry, gate or motoric code reads them.
    """

    rezeptoren = dict(senses.get("rezeptoren", {}) or {})
    feldwirkung = _mcm_feldwirkung(senses)
    visual_salience = _clip(rezeptoren.get("visual_form_salience", 0.0))
    auditory_stimulation = _clip(rezeptoren.get("auditory_stimulation", 0.0))
    direct_contact = _clip(rezeptoren.get("direct_contact_pressure", 0.0))
    intake_pressure = _clip(rezeptoren.get("field_intake_pressure", 0.0))
    coherence = _signed_clip(feldwirkung.get("mcm_coherence", 0.0))
    tension = _clip(feldwirkung.get("mcm_tension", 0.0))
    asymmetry = _signed_clip(feldwirkung.get("mcm_asymmetry", 0.0))
    reflection_carry = _clip(reflection_context.get("reflection_context_carry", 0.0))
    reflection_strain = _clip(reflection_context.get("reflection_context_strain", 0.0))
    reflection_alignment = _clip(reflection_context.get("reflection_context_alignment", 0.0))
    afterimage = _clip(temporal_state.get("mini_afterimage", 0.0))
    recurrence = _clip(temporal_state.get("mini_recurrence_strength", 0.0))
    neuro_support = _clip(neuro_state.get("mini_neuro_support", 0.0))
    neuro_load = _clip(neuro_state.get("mini_neuro_load", 0.0))
    visual_field_gap = _clip(abs(visual_salience - abs(asymmetry)), 0.0, 1.0)
    hearing_field_gap = _clip(abs(auditory_stimulation - tension), 0.0, 1.0)
    contact_field_gap = _clip(abs(direct_contact - intake_pressure), 0.0, 1.0)
    sensory_coupling = _clip(
        ((1.0 - visual_field_gap) * 0.28)
        + ((1.0 - hearing_field_gap) * 0.26)
        + ((1.0 - contact_field_gap) * 0.10)
        + (((coherence + 1.0) * 0.5) * 0.20)
        + (reflection_alignment * 0.16)
    )
    mcm_carry_quality = _clip(
        (reflection_carry * 0.34)
        + (sensory_coupling * 0.28)
        + (neuro_support * 0.18)
        + ((1.0 - intake_pressure) * 0.12)
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
    base_rekopplung_quality = _clip(
        (mcm_carry_quality * 0.42)
        + (reflection_alignment * 0.24)
        + ((1.0 - mcm_strain_quality) * 0.20)
        + (sensory_coupling * 0.14)
    )
    rekopplung_factor = _clip(rekopplung_factor, 0.0, 2.0)
    rekopplung_quality = _clip(base_rekopplung_quality * rekopplung_factor)
    field_effect_state = _dominant_label(
        {
            "field_carried": _clip((mcm_carry_quality * 0.46) + (sensory_coupling * 0.34) + ((1.0 - mcm_strain_quality) * 0.20)),
            "field_fragmented": _clip((mcm_strain_quality * 0.42) + ((1.0 - sensory_coupling) * 0.34) + (visual_field_gap * 0.12) + (hearing_field_gap * 0.12)),
            "field_strained": _clip((mcm_strain_quality * 0.52) + (tension * 0.22) + (neuro_load * 0.16) + ((1.0 - mcm_carry_quality) * 0.10)),
            "field_mixed": _clip((1.0 - abs(mcm_carry_quality - mcm_strain_quality)) * 0.48 + (1.0 - abs(sensory_coupling - 0.5)) * 0.32 + (recurrence * 0.20)),
        }
    )
    return {
        "field_effect_state": field_effect_state,
        "mcm_carry_quality": mcm_carry_quality,
        "mcm_strain_quality": mcm_strain_quality,
        "mcm_rekopplung_quality": rekopplung_quality,
        "mcm_base_rekopplung_quality": base_rekopplung_quality,
        "mcm_rekopplung_factor": rekopplung_factor,
        "sensory_coupling": sensory_coupling,
        "reflection_alignment": reflection_alignment,
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
            "mcm_adaptive_rekopplung_quality": 0.0,
            "mcm_adaptive_rekopplung_experience": 0.0,
            "mcm_adaptive_role_experience": 0.0,
            "mcm_adaptive_path_experience": 0.0,
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
            "base_field_effect_state": str(self.sums.get("base_field_effect_state", "") or ""),
            "passive_mcm_effect_class": str(self.sums.get("passive_mcm_effect_class", "") or ""),
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
            "avg_mcm_adaptive_rekopplung_quality": self.sums["mcm_adaptive_rekopplung_quality"] / denom,
            "avg_mcm_adaptive_rekopplung_experience": self.sums["mcm_adaptive_rekopplung_experience"] / denom,
            "avg_mcm_adaptive_role_experience": self.sums["mcm_adaptive_role_experience"] / denom,
            "avg_mcm_adaptive_path_experience": self.sums["mcm_adaptive_path_experience"] / denom,
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
        state = str(effect.get("field_episode_role", "") or effect.get("field_effect_state", "") or "field_mixed")
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
            if key in {"base_field_effect_state", "passive_mcm_effect_class"}:
                continue
            self.sums[key] += float(effect.get(key, 0.0) or 0.0)
        self.sums["base_field_effect_state"] = str(effect.get("field_effect_state", "") or "")
        self.sums["passive_mcm_effect_class"] = str(effect.get("passive_mcm_effect_class", "") or "")
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
