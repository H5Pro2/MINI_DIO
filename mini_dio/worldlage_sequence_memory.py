from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from mini_dio.worldlage_classifier import classify_adaptation_delta


@dataclass
class WorldlageSequenceTrace:
    sequence: str
    occurrences: int = 0
    outcome_counts: Counter[str] = field(default_factory=Counter)
    delta_zentrum_sum: float = 0.0
    delta_rand_sum: float = 0.0
    delta_rekopplung_sum: float = 0.0
    delta_strain_sum: float = 0.0

    def observe(self, base: dict[str, object], adapted: dict[str, object]) -> None:
        deltas = classify_adaptation_delta(base, adapted)
        self.occurrences += 1
        self.outcome_counts[str(deltas["adaptation_outcome"])] += 1
        self.delta_zentrum_sum += float(deltas["delta_zentrum"])
        self.delta_rand_sum += float(deltas["delta_rand"])
        self.delta_rekopplung_sum += float(deltas["delta_rekopplung"])
        self.delta_strain_sum += float(deltas["delta_strain"])

    @property
    def dominant_outcome(self) -> str:
        if not self.outcome_counts:
            return "unknown"
        return self.outcome_counts.most_common(1)[0][0]

    def _avg(self, value: float) -> float:
        return value / max(1, self.occurrences)

    def as_row(self) -> dict[str, object]:
        return {
            "worldlage_sequence": self.sequence,
            "occurrences": self.occurrences,
            "dominant_outcome": self.dominant_outcome,
            "outcome_counts": ";".join(f"{key}:{value}" for key, value in self.outcome_counts.most_common()),
            "avg_delta_zentrum": round(self._avg(self.delta_zentrum_sum), 6),
            "avg_delta_rand": round(self._avg(self.delta_rand_sum), 6),
            "avg_delta_rekopplung": round(self._avg(self.delta_rekopplung_sum), 6),
            "avg_delta_strain": round(self._avg(self.delta_strain_sum), 6),
            "passive_only": 1,
            "influences_action": 0,
        }


class WorldlageSequenceMemory:
    def __init__(self) -> None:
        self._traces: dict[str, WorldlageSequenceTrace] = {}

    def observe(self, *, previous_lage: str, current_lage: str, base: dict[str, object], adapted: dict[str, object]) -> None:
        sequence = f"{previous_lage}->{current_lage}"
        trace = self._traces.setdefault(sequence, WorldlageSequenceTrace(sequence=sequence))
        trace.observe(base, adapted)

    def rows(self) -> list[dict[str, object]]:
        return [
            trace.as_row()
            for trace in sorted(self._traces.values(), key=lambda item: (-item.occurrences, item.sequence))
        ]
