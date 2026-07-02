from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _clean(value: object, fallback: str = "-") -> str:
    text = str(value or "").strip()
    return text or fallback


def _phase_effect(from_role: str, current_role: str, next_role: str) -> str:
    sequence = (from_role, current_role, next_role)
    if sequence == ("zentrum_stabil", "spannungsrand_kippnaehe", "offene_variante"):
        return "zentrumsbruch_in_offenheit"
    if current_role == "spannungsrand_kippnaehe" and next_role == "offene_variante":
        return "rand_entlastet_in_offenheit"
    if from_role == "offene_variante" and current_role == "spannungsrand_kippnaehe":
        return "offenheit_geraet_in_kippnaehe"
    if current_role == "rekopplungsnaehe" and next_role == "zentrum_stabil":
        return "rekopplung_findet_zentrum"
    if current_role == "zentrum_stabil" and next_role == "rekopplungsnaehe":
        return "zentrum_oeffnet_rekopplung"
    if current_role == next_role:
        return "phase_bleibt_gehalten"
    return "phase_offen"


@dataclass
class FieldPhaseObservation:
    world: str
    previous_role: str
    current_role: str
    next_role: str
    start_tick: int
    previous_duration: int
    current_duration: int
    next_duration: int
    current_raw_field_intake: float
    current_rekopplung: float
    current_strain: float
    next_raw_field_intake: float
    next_rekopplung: float
    next_strain: float
    source: str = ""

    @property
    def phase_key(self) -> str:
        return f"{self.previous_role}->{self.current_role}->{self.next_role}"

    @property
    def transition_key(self) -> str:
        return f"{self.previous_role}->{self.current_role}"

    @property
    def next_transition_key(self) -> str:
        return f"{self.current_role}->{self.next_role}"

    @property
    def rekopplung_delta_to_next(self) -> float:
        return self.next_rekopplung - self.current_rekopplung

    @property
    def strain_delta_to_next(self) -> float:
        return self.next_strain - self.current_strain

    @property
    def intake_delta_to_next(self) -> float:
        return self.next_raw_field_intake - self.current_raw_field_intake


@dataclass
class FieldPhaseRecord:
    phase_key: str
    seen_count: int = 0
    total_previous_duration: int = 0
    total_current_duration: int = 0
    total_next_duration: int = 0
    world_counts: Counter[str] = field(default_factory=Counter)
    source_counts: Counter[str] = field(default_factory=Counter)
    effect_counts: Counter[str] = field(default_factory=Counter)
    current_intake_sum: float = 0.0
    current_rekopplung_sum: float = 0.0
    current_strain_sum: float = 0.0
    next_intake_sum: float = 0.0
    next_rekopplung_sum: float = 0.0
    next_strain_sum: float = 0.0
    rekopplung_delta_sum: float = 0.0
    strain_delta_sum: float = 0.0
    intake_delta_sum: float = 0.0

    def add(self, observation: FieldPhaseObservation) -> None:
        self.seen_count += 1
        self.total_previous_duration += observation.previous_duration
        self.total_current_duration += observation.current_duration
        self.total_next_duration += observation.next_duration
        self.world_counts[observation.world] += 1
        if observation.source:
            self.source_counts[observation.source] += 1
        self.effect_counts[
            _phase_effect(
                observation.previous_role,
                observation.current_role,
                observation.next_role,
            )
        ] += 1
        self.current_intake_sum += observation.current_raw_field_intake
        self.current_rekopplung_sum += observation.current_rekopplung
        self.current_strain_sum += observation.current_strain
        self.next_intake_sum += observation.next_raw_field_intake
        self.next_rekopplung_sum += observation.next_rekopplung
        self.next_strain_sum += observation.next_strain
        self.rekopplung_delta_sum += observation.rekopplung_delta_to_next
        self.strain_delta_sum += observation.strain_delta_to_next
        self.intake_delta_sum += observation.intake_delta_to_next

    def _avg(self, value: float) -> float:
        if self.seen_count <= 0:
            return 0.0
        return value / self.seen_count

    def dominant_effect(self) -> str:
        if not self.effect_counts:
            return "-"
        return self.effect_counts.most_common(1)[0][0]

    def phase_memory_quality(self) -> str:
        if self.seen_count <= 1:
            return "young_phase_trace"
        if len(self.world_counts) > 1 and self.seen_count >= 3:
            if self.dominant_effect() in {
                "rand_entlastet_in_offenheit",
                "zentrumsbruch_in_offenheit",
                "rekopplung_findet_zentrum",
            }:
                return "cross_world_phase_family"
            return "cross_world_open_phase"
        if self.seen_count >= 3:
            return "recurrent_world_phase"
        return "local_phase_trace"

    def phase_note(self) -> str:
        effect = self.dominant_effect()
        if effect == "zentrumsbruch_in_offenheit":
            return "zentrumsnahe Ordnung bricht kurz und entlastet in offenen Neuordnungsraum"
        if effect == "rand_entlastet_in_offenheit":
            return "Randspannung bleibt nicht stehen, sondern entlastet in Offenheit"
        if effect == "offenheit_geraet_in_kippnaehe":
            return "offener Bewegungsraum geraet kurz in Kippnaehe"
        if effect == "rekopplung_findet_zentrum":
            return "Rekopplungsnaehe findet Zentrum"
        if effect == "phase_bleibt_gehalten":
            return "Feldphase bleibt ueber Folgezustand gehalten"
        return "Feldphase bleibt offen lesbar"

    def to_row(self) -> dict[str, object]:
        previous_role, current_role, next_role = self.phase_key.split("->", 2)
        return {
            **PASSIVE_FLAGS,
            "phase_key": self.phase_key,
            "previous_role": previous_role,
            "current_role": current_role,
            "next_role": next_role,
            "seen_count": self.seen_count,
            "world_count": len(self.world_counts),
            "dominant_effect": self.dominant_effect(),
            "phase_memory_quality": self.phase_memory_quality(),
            "phase_note": self.phase_note(),
            "avg_previous_duration": round(self._avg(self.total_previous_duration), 6),
            "avg_current_duration": round(self._avg(self.total_current_duration), 6),
            "avg_next_duration": round(self._avg(self.total_next_duration), 6),
            "avg_current_intake": round(self._avg(self.current_intake_sum), 6),
            "avg_current_rekopplung": round(self._avg(self.current_rekopplung_sum), 6),
            "avg_current_strain": round(self._avg(self.current_strain_sum), 6),
            "avg_next_intake": round(self._avg(self.next_intake_sum), 6),
            "avg_next_rekopplung": round(self._avg(self.next_rekopplung_sum), 6),
            "avg_next_strain": round(self._avg(self.next_strain_sum), 6),
            "avg_rekopplung_delta_to_next": round(self._avg(self.rekopplung_delta_sum), 6),
            "avg_strain_delta_to_next": round(self._avg(self.strain_delta_sum), 6),
            "avg_intake_delta_to_next": round(self._avg(self.intake_delta_sum), 6),
            "worlds": _counter_text(self.world_counts),
            "sources": _counter_text(self.source_counts),
            "caution_note": "passive_not_actionable",
        }


def _counter_text(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return "; ".join(f"{key}:{value}" for key, value in counter.most_common())


def _rows_from_transition_csv(path: Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def observations_from_transition_csv(path: Path) -> list[FieldPhaseObservation]:
    rows = _rows_from_transition_csv(path)
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(_clean(row.get("world")), []).append(row)

    observations: list[FieldPhaseObservation] = []
    for world, world_rows in grouped.items():
        ordered = sorted(world_rows, key=lambda item: _safe_int(item.get("start_tick")))
        for index, row in enumerate(ordered[:-1]):
            next_row = ordered[index + 1]
            previous_role = _clean(row.get("from_role"))
            current_role = _clean(row.get("to_role"))
            next_role = _clean(next_row.get("to_role"))
            if "-" in {previous_role, current_role, next_role}:
                continue
            observations.append(
                FieldPhaseObservation(
                    world=world,
                    previous_role=previous_role,
                    current_role=current_role,
                    next_role=next_role,
                    start_tick=_safe_int(row.get("start_tick")),
                    previous_duration=_safe_int(row.get("previous_duration")),
                    current_duration=_safe_int(row.get("current_duration")),
                    next_duration=_safe_int(next_row.get("current_duration")),
                    current_raw_field_intake=_safe_float(row.get("current_raw_field_intake")),
                    current_rekopplung=_safe_float(row.get("current_rekopplung")),
                    current_strain=_safe_float(row.get("current_strain")),
                    next_raw_field_intake=_safe_float(next_row.get("current_raw_field_intake")),
                    next_rekopplung=_safe_float(next_row.get("current_rekopplung")),
                    next_strain=_safe_float(next_row.get("current_strain")),
                    source=Path(path).name,
                )
            )
    return observations


class MCMFieldPhaseMemory:
    def __init__(self) -> None:
        self.records: dict[str, FieldPhaseRecord] = {}

    def update_from_observation(self, observation: FieldPhaseObservation) -> None:
        record = self.records.setdefault(
            observation.phase_key,
            FieldPhaseRecord(phase_key=observation.phase_key),
        )
        record.add(observation)

    def update_many(self, observations: Iterable[FieldPhaseObservation]) -> None:
        for observation in observations:
            self.update_from_observation(observation)

    @classmethod
    def from_transition_csv_paths(cls, paths: Iterable[Path]) -> MCMFieldPhaseMemory:
        memory = cls()
        for path in paths:
            memory.update_many(observations_from_transition_csv(Path(path)))
        return memory

    def to_rows(self) -> list[dict[str, object]]:
        return sorted(
            (record.to_row() for record in self.records.values()),
            key=lambda row: (-int(row["seen_count"]), str(row["phase_key"])),
        )

    def quality_profile(self) -> dict[str, object]:
        rows = self.to_rows()
        return {
            **PASSIVE_FLAGS,
            "records": len(rows),
            "phase_memory_quality": dict(
                Counter(str(row["phase_memory_quality"]) for row in rows).most_common()
            ),
            "dominant_effect": dict(Counter(str(row["dominant_effect"]) for row in rows).most_common()),
        }

    def write_csv(self, path: Path) -> None:
        rows = self.to_rows()
        path.parent.mkdir(parents=True, exist_ok=True)
        if not rows:
            path.write_text("", encoding="utf-8")
            return
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    def write_json(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "profile": self.quality_profile(),
            "records": self.to_rows(),
        }
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


__all__ = [
    "FieldPhaseObservation",
    "FieldPhaseRecord",
    "MCMFieldPhaseMemory",
    "observations_from_transition_csv",
]
