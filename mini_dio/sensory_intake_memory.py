from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _clean(value: object, fallback: str = "") -> str:
    text = str(value or "").strip()
    return text or fallback


def _counter_text(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return "; ".join(f"{key}:{value}" for key, value in counter.most_common())


def _most_common(counter: Counter[str]) -> tuple[str, int]:
    if not counter:
        return "-", 0
    value, count = counter.most_common(1)[0]
    return value or "-", int(count)


def _clip01(value: object) -> float:
    return max(0.0, min(1.0, _safe_float(value)))


def _mean(*values: object) -> float:
    clean = [_clip01(value) for value in values]
    return sum(clean) / max(1, len(clean))


def _pressure(value: object, scale: float = 1.0) -> float:
    amount = max(0.0, _safe_float(value))
    return amount / (amount + max(0.000001, scale))


def _dominant_label(scores: dict[str, float], default: str) -> str:
    clean = {key: _clip01(value) for key, value in scores.items()}
    if not clean:
        return default
    return max(clean, key=clean.get)


@dataclass
class SensoryIntakeObservation:
    axis: str
    inner_effect_state: str
    mcm_preview_symbol: str
    signature_label: str = ""
    worlds: str = ""
    world_count: int = 0
    total_count: int = 0
    recoupling_balance: float = 0.0
    recoupling_stdev: float = 0.0
    rekopplung_quality: float = 0.0
    strain_quality: float = 0.0
    carry_quality: float = 0.0
    field_intake_pressure: float = 0.0
    source: str = ""

    @property
    def intake_key(self) -> str:
        return f"{self.axis}|{self.inner_effect_state}|{self.mcm_preview_symbol}"

    @classmethod
    def from_row(cls, row: dict[str, str], *, source: str = "") -> SensoryIntakeObservation:
        return cls(
            axis=_clean(row.get("axis"), "-"),
            inner_effect_state=_clean(row.get("inner_effect_state"), "-"),
            mcm_preview_symbol=_clean(row.get("mcm_preview_symbol"), "-"),
            signature_label=_clean(row.get("signature_label")),
            worlds=_clean(row.get("worlds")),
            world_count=_safe_int(row.get("world_count")),
            total_count=_safe_int(row.get("total_count")),
            recoupling_balance=_safe_float(row.get("recoupling_balance")),
            recoupling_stdev=_safe_float(row.get("stdev_recoupling_balance")),
            rekopplung_quality=_safe_float(row.get("avg_mcm_rekopplung_quality")),
            strain_quality=_safe_float(row.get("avg_mcm_strain_quality")),
            carry_quality=_safe_float(row.get("avg_mcm_carry_quality")),
            field_intake_pressure=_safe_float(row.get("avg_rezeptor_field_intake_pressure")),
            source=source,
        )


@dataclass
class SensoryIntakeRecord:
    intake_key: str
    axis: str
    inner_effect_state: str
    mcm_preview_symbol: str
    seen_count: int = 0
    total_events: int = 0
    max_world_count: int = 0
    world_counts: Counter[str] = field(default_factory=Counter)
    label_counts: Counter[str] = field(default_factory=Counter)
    source_counts: Counter[str] = field(default_factory=Counter)
    balance_sum: float = 0.0
    stdev_sum: float = 0.0
    rekopplung_sum: float = 0.0
    strain_sum: float = 0.0
    carry_sum: float = 0.0
    field_input_sum: float = 0.0

    def add(self, observation: SensoryIntakeObservation) -> None:
        self.seen_count += 1
        self.total_events += observation.total_count
        self.max_world_count = max(self.max_world_count, observation.world_count)
        self.balance_sum += observation.recoupling_balance
        self.stdev_sum += observation.recoupling_stdev
        self.rekopplung_sum += observation.rekopplung_quality
        self.strain_sum += observation.strain_quality
        self.carry_sum += observation.carry_quality
        self.field_input_sum += observation.field_intake_pressure
        if observation.signature_label:
            self.label_counts[observation.signature_label] += 1
        if observation.worlds:
            for world in observation.worlds.split(","):
                if world.strip():
                    self.world_counts[world.strip()] += 1
        if observation.source:
            self.source_counts[observation.source] += 1

    def _avg(self, value: float) -> float:
        return value / max(1, self.seen_count)

    def dominant_label(self) -> str:
        return _most_common(self.label_counts)[0]

    def intake_memory_quality(self) -> str:
        label = self.dominant_label()
        avg_balance = self._avg(self.balance_sum)
        avg_strain = self._avg(self.strain_sum)
        avg_field_input = self._avg(self.field_input_sum)
        avg_stdev = self._avg(self.stdev_sum)
        world_pressure = _pressure(self.max_world_count, 2.0)
        event_pressure = _pressure(self.total_events, 60.0)
        balance_pressure = _clip01(avg_balance)
        strain_pressure = _clip01(avg_strain)
        field_pressure = _clip01(avg_field_input)
        drift_pressure = _pressure(avg_stdev, 0.02)
        quiet_label = 1.0 if label == "reproduzierte_ruhige_aufnahme" else 0.0
        carried_label = 1.0 if label == "wiederkehrend_tragend" else 0.0
        loaded_label = 1.0 if label == "wiederkehrend_kontaktlastig" else 0.0
        return _dominant_label(
            {
                "reproduced_quiet_intake": _mean(quiet_label, world_pressure, 1.0 - strain_pressure, balance_pressure),
                "recurrently_carried_intake": _mean(carried_label, balance_pressure, world_pressure),
                "contact_loaded_intake": _mean(loaded_label, field_pressure, event_pressure),
                "strained_intake": _mean(strain_pressure, 1.0 - balance_pressure, field_pressure),
                "drifting_intake": _mean(drift_pressure, world_pressure, 1.0 - balance_pressure),
                "open_recurrent_intake": _mean(world_pressure, event_pressure, 1.0 - max(strain_pressure, field_pressure)),
                "young_intake_trace": _mean(1.0 - world_pressure, 1.0 - event_pressure),
            },
            default="young_intake_trace",
        )

    def maturity_note(self) -> str:
        world_pressure = _pressure(self.max_world_count, 2.0)
        event_pressure = _pressure(self.total_events, 60.0)
        seen_pressure = _pressure(self.seen_count, 1.0)
        return _dominant_label(
            {
                "multi_world_recurrent": _mean(world_pressure, event_pressure),
                "cross_world_visible": world_pressure,
                "single_observation": 1.0 - seen_pressure,
                "weak_recurrence": _mean(seen_pressure, 1.0 - world_pressure),
            },
            default="weak_recurrence",
        )

    def to_row(self) -> dict[str, object]:
        return {
            "intake_key": self.intake_key,
            "axis": self.axis,
            "inner_effect_state": self.inner_effect_state,
            "mcm_preview_symbol": self.mcm_preview_symbol,
            "seen_count": self.seen_count,
            "total_events": self.total_events,
            "max_world_count": self.max_world_count,
            "dominant_signature_label": self.dominant_label(),
            "intake_memory_quality": self.intake_memory_quality(),
            "maturity_note": self.maturity_note(),
            "avg_recoupling_balance": round(self._avg(self.balance_sum), 6),
            "avg_balance_stdev": round(self._avg(self.stdev_sum), 6),
            "avg_rekopplung_quality": round(self._avg(self.rekopplung_sum), 6),
            "avg_strain_quality": round(self._avg(self.strain_sum), 6),
            "avg_carry_quality": round(self._avg(self.carry_sum), 6),
            "avg_field_intake_pressure": round(self._avg(self.field_input_sum), 6),
            "label_profile": _counter_text(self.label_counts),
            "world_profile": _counter_text(self.world_counts),
            "sources": _counter_text(self.source_counts),
            "caution_note": "passive_not_actionable",
        }


class SensoryIntakeMemory:
    def __init__(self) -> None:
        self.records: dict[str, SensoryIntakeRecord] = {}

    def update_from_observation(self, observation: SensoryIntakeObservation) -> None:
        if observation.intake_key == "-|-|-":
            return
        record = self.records.setdefault(
            observation.intake_key,
            SensoryIntakeRecord(
                intake_key=observation.intake_key,
                axis=observation.axis,
                inner_effect_state=observation.inner_effect_state,
                mcm_preview_symbol=observation.mcm_preview_symbol,
            ),
        )
        record.add(observation)

    def update_many(self, observations: Iterable[SensoryIntakeObservation]) -> None:
        for observation in observations:
            self.update_from_observation(observation)

    @classmethod
    def from_csv_paths(cls, paths: Iterable[Path]) -> SensoryIntakeMemory:
        memory = cls()
        for path in paths:
            with Path(path).open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle, delimiter=";")
                for row in reader:
                    memory.update_from_observation(
                        SensoryIntakeObservation.from_row(row, source=Path(path).name)
                    )
        return memory

    def to_rows(self) -> list[dict[str, object]]:
        return sorted(
            (record.to_row() for record in self.records.values()),
            key=lambda row: (
                -int(row["max_world_count"]),
                -int(row["total_events"]),
                str(row["axis"]),
                str(row["inner_effect_state"]),
            ),
        )

    def write_csv(self, path: Path) -> None:
        rows = self.to_rows()
        path.parent.mkdir(parents=True, exist_ok=True)
        if not rows:
            path.write_text("", encoding="utf-8")
            return
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter=";")
            writer.writeheader()
            writer.writerows(rows)

    def write_json(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_rows(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
