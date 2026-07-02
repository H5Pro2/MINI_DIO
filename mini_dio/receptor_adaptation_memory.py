from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field


@dataclass
class ReceptorAdaptationTrace:
    """Passive memory for field effects after receptor adaptation.

    It stores consequences of an intake posture. It does not decide, gate or
    act. The memory only says whether the posture tended to calm, shift or
    destabilize the MCM field order in observed worlds.
    """

    label: str
    worlds: int = 0
    known_ticks: int = 0
    applied_ticks: int = 0
    outcome_counts: Counter[str] = field(default_factory=Counter)
    delta_zentrum_sum: float = 0.0
    delta_rand_sum: float = 0.0
    delta_rekopplung_sum: float = 0.0
    delta_strain_sum: float = 0.0
    delta_raw_field_sum: float = 0.0
    delta_auditory_sum: float = 0.0
    delta_visual_sum: float = 0.0

    def observe(self, *, known_ticks: int, applied_ticks: int, deltas: dict[str, float]) -> None:
        self.worlds += 1
        self.known_ticks += max(0, int(known_ticks))
        self.applied_ticks += max(0, int(applied_ticks))
        outcome = classify_adaptation_outcome(deltas)
        self.outcome_counts[outcome] += 1
        self.delta_zentrum_sum += float(deltas.get("zentrum", 0.0))
        self.delta_rand_sum += float(deltas.get("rand", 0.0))
        self.delta_rekopplung_sum += float(deltas.get("rekopplung", 0.0))
        self.delta_strain_sum += float(deltas.get("strain", 0.0))
        self.delta_raw_field_sum += float(deltas.get("raw_field", 0.0))
        self.delta_auditory_sum += float(deltas.get("auditory", 0.0))
        self.delta_visual_sum += float(deltas.get("visual", 0.0))

    def _avg(self, value: float) -> float:
        return value / max(1, self.worlds)

    @property
    def dominant_outcome(self) -> str:
        if not self.outcome_counts:
            return "unknown"
        return self.outcome_counts.most_common(1)[0][0]

    @property
    def adaptation_quality(self) -> float:
        calm = self.outcome_counts.get("beruhigend", 0)
        stable = self.outcome_counts.get("stabil_leicht", 0)
        risky = self.outcome_counts.get("verschiebend", 0)
        neutral = self.outcome_counts.get("neutral", 0)
        score = (calm * 1.0) + (stable * 0.7) + (neutral * 0.35) - (risky * 0.8)
        return max(0.0, min(1.0, score / max(1, self.worlds)))

    def as_row(self) -> dict[str, object]:
        return {
            "adaptation_label": self.label,
            "worlds": self.worlds,
            "known_ticks": self.known_ticks,
            "applied_ticks": self.applied_ticks,
            "dominant_outcome": self.dominant_outcome,
            "adaptation_quality": round(self.adaptation_quality, 6),
            "avg_delta_zentrum": round(self._avg(self.delta_zentrum_sum), 6),
            "avg_delta_rand": round(self._avg(self.delta_rand_sum), 6),
            "avg_delta_rekopplung": round(self._avg(self.delta_rekopplung_sum), 6),
            "avg_delta_strain": round(self._avg(self.delta_strain_sum), 6),
            "avg_delta_raw_field": round(self._avg(self.delta_raw_field_sum), 6),
            "avg_delta_auditory": round(self._avg(self.delta_auditory_sum), 6),
            "avg_delta_visual": round(self._avg(self.delta_visual_sum), 6),
            "outcome_counts": ";".join(f"{key}:{value}" for key, value in self.outcome_counts.most_common()),
            "passive_only": 1,
            "influences_action": 0,
        }


class ReceptorAdaptationMemory:
    def __init__(self) -> None:
        self._traces: dict[str, ReceptorAdaptationTrace] = {}

    def observe_ab_pair(self, *, label: str, base: dict[str, object], adapted: dict[str, object]) -> None:
        trace = self._traces.setdefault(label, ReceptorAdaptationTrace(label=label))
        trace.observe(
            known_ticks=_to_int(adapted.get("known_signature_ticks", 0)),
            applied_ticks=_to_int(adapted.get("preference_applied_ticks", 0)),
            deltas={
                "zentrum": _to_float(adapted.get("zentrum_ratio")) - _to_float(base.get("zentrum_ratio")),
                "rand": _to_float(adapted.get("rand_ratio")) - _to_float(base.get("rand_ratio")),
                "rekopplung": _to_float(adapted.get("avg_rekopplung")) - _to_float(base.get("avg_rekopplung")),
                "strain": _to_float(adapted.get("avg_strain")) - _to_float(base.get("avg_strain")),
                "raw_field": _to_float(adapted.get("avg_raw_field")) - _to_float(base.get("avg_raw_field")),
                "auditory": _to_float(adapted.get("avg_auditory")) - _to_float(base.get("avg_auditory")),
                "visual": _to_float(adapted.get("avg_visual")) - _to_float(base.get("avg_visual")),
            },
        )

    def rows(self) -> list[dict[str, object]]:
        return [trace.as_row() for trace in sorted(self._traces.values(), key=lambda item: item.label)]


def classify_adaptation_outcome(deltas: dict[str, float]) -> str:
    delta_rand = float(deltas.get("rand", 0.0))
    delta_strain = float(deltas.get("strain", 0.0))
    delta_zentrum = float(deltas.get("zentrum", 0.0))
    delta_rekopplung = float(deltas.get("rekopplung", 0.0))

    calming = delta_rand < -0.001 and delta_strain < -0.0005
    preserving = delta_zentrum > -0.01 and delta_rekopplung > -0.002
    strong_shift = abs(delta_zentrum) > 0.04 or abs(delta_rekopplung) > 0.015

    if strong_shift:
        return "verschiebend"
    if calming and preserving and (delta_zentrum >= 0.003 or delta_rekopplung >= 0.0005):
        return "beruhigend"
    if calming and preserving:
        return "stabil_leicht"
    if delta_rand > 0.002 or delta_strain > 0.001:
        return "verschiebend"
    return "neutral"


def _to_float(value: object) -> float:
    try:
        number = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if number != number else number


def _to_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0
