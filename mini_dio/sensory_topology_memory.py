from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field


@dataclass
class SensoryTopologyTrace:
    signature: str
    role_counts: Counter[str] = field(default_factory=Counter)
    source_counts: Counter[str] = field(default_factory=Counter)
    segments: int = 0
    duration: int = 0
    rekopplung_sum: float = 0.0
    strain_sum: float = 0.0
    raw_field_sum: float = 0.0

    def observe(
        self,
        *,
        role: str,
        source: str,
        segments: int,
        duration: int,
        rekopplung: float,
        strain: float,
        raw_field: float,
    ) -> None:
        self.role_counts[str(role)] += int(max(0, segments))
        self.source_counts[str(source)] += int(max(0, segments))
        self.segments += int(max(0, segments))
        self.duration += int(max(0, duration))
        weight = max(1, int(duration))
        self.rekopplung_sum += float(rekopplung) * weight
        self.strain_sum += float(strain) * weight
        self.raw_field_sum += float(raw_field) * weight

    @property
    def dominant_role(self) -> str:
        if not self.role_counts:
            return "unknown"
        return self.role_counts.most_common(1)[0][0]

    @property
    def avg_rekopplung(self) -> float:
        return self.rekopplung_sum / max(1, self.duration)

    @property
    def avg_strain(self) -> float:
        return self.strain_sum / max(1, self.duration)

    @property
    def avg_raw_field(self) -> float:
        return self.raw_field_sum / max(1, self.duration)

    @property
    def carrying_quality(self) -> float:
        return max(0.0, min(1.0, (self.avg_rekopplung * 0.68) + ((1.0 - self.avg_strain) * 0.32)))

    @property
    def receptor_adaptation_preference(self) -> dict[str, str]:
        return _axis_preferences(
            signature=self.signature,
            role=self.dominant_role,
            carrying_quality=self.carrying_quality,
            strain=self.avg_strain,
            raw_field=self.avg_raw_field,
        )

    def as_row(self) -> dict[str, object]:
        preferences = self.receptor_adaptation_preference
        return {
            "sensory_signature": self.signature,
            "dominant_role": self.dominant_role,
            "segments": self.segments,
            "duration": self.duration,
            "avg_rekopplung": round(self.avg_rekopplung, 6),
            "avg_strain": round(self.avg_strain, 6),
            "avg_raw_field": round(self.avg_raw_field, 6),
            "carrying_quality": round(self.carrying_quality, 6),
            "hearing_preference": preferences["hearing"],
            "vision_preference": preferences["vision"],
            "feeling_preference": preferences["feeling"],
            "adaptation_reason": preferences["reason"],
            "role_counts": ";".join(f"{key}:{value}" for key, value in self.role_counts.most_common()),
            "source_counts": ";".join(f"{key}:{value}" for key, value in self.source_counts.most_common()),
            "passive_only": 1,
            "influences_action": 0,
        }


class SensoryTopologyMemory:
    def __init__(self) -> None:
        self._traces: dict[str, SensoryTopologyTrace] = {}

    def observe_row(self, row: dict[str, object]) -> None:
        signature = str(row.get("sensory_signature", "") or "unknown")
        trace = self._traces.setdefault(signature, SensoryTopologyTrace(signature=signature))
        trace.observe(
            role=str(row.get("role", "") or "unknown"),
            source=str(row.get("source", "") or "unknown"),
            segments=_to_int(row.get("segments", 0)),
            duration=_to_int(row.get("duration", 0)),
            rekopplung=_to_float(row.get("avg_rekopplung", 0.0)),
            strain=_to_float(row.get("avg_strain", 0.0)),
            raw_field=_to_float(row.get("avg_raw_field_intake", 0.0)),
        )

    def rows(self) -> list[dict[str, object]]:
        return [trace.as_row() for trace in sorted(self._traces.values(), key=lambda item: (-item.segments, item.signature))]

    def role_index(self) -> dict[str, list[str]]:
        index: dict[str, list[str]] = defaultdict(list)
        for trace in self._traces.values():
            index[trace.dominant_role].append(trace.signature)
        return {key: sorted(values) for key, values in sorted(index.items())}


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


def _axis_preferences(
    *,
    signature: str,
    role: str,
    carrying_quality: float,
    strain: float,
    raw_field: float,
) -> dict[str, str]:
    """Derive passive, axis-specific receptor tendencies.

    This is not a gate and not an action rule. It only reads whether a repeated
    sensory signature suggests more intake, less intake or stable intake per
    sense axis.
    """

    tokens = set(str(signature).split("_"))
    overloaded = role == "spannungsrand_kippnaehe" or strain >= 0.24 or raw_field >= 0.34
    thin = "feldduenn" in tokens or raw_field <= 0.08
    carried = carrying_quality >= 0.74 and not overloaded
    open_state = role == "offene_variante"

    hearing = "hold"
    vision = "hold"
    feeling = "hold"
    reason = "tragende_aufnahme_halten"

    if overloaded:
        if "laut" in tokens:
            hearing = "down"
        if "unscharf" in tokens:
            vision = "up"
        elif "scharf" in tokens and raw_field >= 0.42:
            vision = "soften"
        if "feldstark" in tokens:
            feeling = "down"
        reason = "ueberlastung_achsenweise_daempfen"
    elif thin and not carried:
        if "leise" in tokens:
            hearing = "up"
        if "unscharf" in tokens:
            vision = "up"
        if "feldduenn" in tokens:
            feeling = "up"
        reason = "aufnahme_zu_duenn_achsenweise_verstaerken"
    elif open_state:
        if "laut" in tokens:
            hearing = "down"
        if "unscharf" in tokens:
            vision = "up"
        if "feldstark" in tokens:
            feeling = "soften"
        elif "feldmittel" in tokens:
            feeling = "hold"
        reason = "offene_lage_feiner_ausrichten"
    elif carried:
        reason = "tragende_sinneshaltung_stabilisieren"

    return {
        "hearing": hearing,
        "vision": vision,
        "feeling": feeling,
        "reason": reason,
    }
