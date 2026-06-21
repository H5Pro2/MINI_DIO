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


def _most_common(counter: Counter[str]) -> tuple[str, int]:
    if not counter:
        return "-", 0
    value, count = counter.most_common(1)[0]
    return value or "-", int(count)


@dataclass
class FieldMovementObservation:
    movement_key: str
    top_passive_quality: str = ""
    quality_profile: str = ""
    top_signature: str = ""
    drift_label: str = ""
    year: str = ""
    timeframe: str = ""
    asset: str = ""
    world_label: str = ""
    events: int = 0
    worlds: int = 0
    top_share: float = 0.0
    top_signature_share: float = 0.0
    pressure_delta: float = 0.0
    relaxation_delta: float = 0.0
    rekopplung_delta: float = 0.0
    strain_delta: float = 0.0
    sharpness_delta: float = 0.0
    loudness_delta: float = 0.0
    source: str = ""

    @classmethod
    def from_row(cls, row: dict[str, str], *, source: str = "") -> FieldMovementObservation:
        movement_key = _clean(
            row.get("movement_key")
            or row.get("pair")
            or row.get("transition")
            or row.get("movement")
            or row.get("direction"),
            "-",
        )
        return cls(
            movement_key=movement_key,
            top_passive_quality=_clean(
                row.get("top_passive_quality")
                or row.get("passive_regulation_quality")
                or row.get("passive_quality")
                or row.get("top_quality")
                or row.get("field_movement_quality")
                or row.get("interpretation")
            ),
            quality_profile=_clean(row.get("quality_profile")),
            top_signature=_clean(row.get("top_signature") or row.get("movement_signature")),
            drift_label=_clean(
                row.get("drift_label")
                or row.get("drift_quality")
                or row.get("reproduction")
            ),
            year=_clean(row.get("year")),
            timeframe=_clean(row.get("timeframe")),
            asset=_clean(row.get("asset") or row.get("symbol") or row.get("world_asset")),
            world_label=_clean(row.get("world") or row.get("world_label")),
            events=_safe_int(row.get("events") or row.get("count")),
            worlds=_safe_int(row.get("worlds")),
            top_share=_safe_float(row.get("top_share") or row.get("share")),
            top_signature_share=_safe_float(row.get("top_signature_share")),
            pressure_delta=_safe_float(row.get("pressure_delta") or row.get("d_pressure")),
            relaxation_delta=_safe_float(row.get("relaxation_delta") or row.get("d_relaxation")),
            rekopplung_delta=_safe_float(row.get("rekopplung_delta") or row.get("d_rekopplung")),
            strain_delta=_safe_float(row.get("strain_delta") or row.get("d_strain")),
            sharpness_delta=_safe_float(row.get("sharpness_delta") or row.get("d_sharpness")),
            loudness_delta=_safe_float(row.get("loudness_delta") or row.get("d_loudness")),
            source=source,
        )

    def movement_effect_quality(self) -> str:
        if (
            self.rekopplung_delta > 0.0
            and self.pressure_delta < 0.0
            and (
                self.strain_delta < 0.0
                or (self.strain_delta == 0.0 and self.loudness_delta <= 0.0)
            )
        ):
            return "rekoppelnd_entlastend"
        if (
            self.rekopplung_delta < 0.0
            and self.pressure_delta > 0.0
            and (
                self.strain_delta > 0.0
                or (self.strain_delta == 0.0 and self.loudness_delta >= 0.0)
            )
        ):
            return "oeffnend_belastend"
        if self.rekopplung_delta > 0.0 and self.relaxation_delta > 0.0:
            return "rekoppelnd"
        if self.pressure_delta > 0.0 or self.strain_delta > 0.0:
            return "spannungsnah"
        if any(
            value != 0.0
            for value in (
                self.pressure_delta,
                self.relaxation_delta,
                self.rekopplung_delta,
                self.strain_delta,
                self.sharpness_delta,
                self.loudness_delta,
            )
        ):
            return "bewegung_offen"
        return ""


@dataclass
class MCMFieldMovementRecord:
    movement_key: str
    seen_count: int = 0
    total_events: int = 0
    total_worlds_observed: int = 0
    quality_counts: Counter[str] = field(default_factory=Counter)
    drift_counts: Counter[str] = field(default_factory=Counter)
    signature_counts: Counter[str] = field(default_factory=Counter)
    timeframe_counts: Counter[str] = field(default_factory=Counter)
    asset_counts: Counter[str] = field(default_factory=Counter)
    year_counts: Counter[str] = field(default_factory=Counter)
    world_counts: Counter[str] = field(default_factory=Counter)
    source_counts: Counter[str] = field(default_factory=Counter)
    movement_effect_counts: Counter[str] = field(default_factory=Counter)
    top_share_sum: float = 0.0
    top_signature_share_sum: float = 0.0
    pressure_delta_sum: float = 0.0
    relaxation_delta_sum: float = 0.0
    rekopplung_delta_sum: float = 0.0
    strain_delta_sum: float = 0.0
    sharpness_delta_sum: float = 0.0
    loudness_delta_sum: float = 0.0

    def add(self, observation: FieldMovementObservation) -> None:
        self.seen_count += 1
        self.total_events += observation.events
        self.total_worlds_observed += observation.worlds
        self.top_share_sum += observation.top_share
        self.top_signature_share_sum += observation.top_signature_share
        self.pressure_delta_sum += observation.pressure_delta
        self.relaxation_delta_sum += observation.relaxation_delta
        self.rekopplung_delta_sum += observation.rekopplung_delta
        self.strain_delta_sum += observation.strain_delta
        self.sharpness_delta_sum += observation.sharpness_delta
        self.loudness_delta_sum += observation.loudness_delta

        if observation.top_passive_quality:
            self.quality_counts[observation.top_passive_quality] += 1
        if observation.drift_label:
            self.drift_counts[observation.drift_label] += 1
        if observation.top_signature:
            self.signature_counts[observation.top_signature] += 1
        if observation.timeframe:
            self.timeframe_counts[observation.timeframe] += 1
        if observation.asset:
            self.asset_counts[observation.asset] += 1
        if observation.year:
            self.year_counts[observation.year] += 1
        if observation.world_label:
            self.world_counts[observation.world_label] += 1
        if observation.source:
            self.source_counts[observation.source] += 1
        movement_effect = observation.movement_effect_quality()
        if movement_effect:
            self.movement_effect_counts[movement_effect] += 1

    @property
    def average_top_share(self) -> float:
        if self.seen_count <= 0:
            return 0.0
        return self.top_share_sum / self.seen_count

    @property
    def average_top_signature_share(self) -> float:
        if self.seen_count <= 0:
            return 0.0
        return self.top_signature_share_sum / self.seen_count

    def dominant_quality(self) -> str:
        return _most_common(self.quality_counts)[0]

    def dominant_drift_label(self) -> str:
        return _most_common(self.drift_counts)[0]

    def dominant_signature(self) -> str:
        return _most_common(self.signature_counts)[0]

    def dominant_movement_effect(self) -> str:
        return _most_common(self.movement_effect_counts)[0]

    def _average(self, value_sum: float) -> float:
        if self.seen_count <= 0:
            return 0.0
        return value_sum / self.seen_count

    def field_memory_quality(self) -> str:
        dominant_quality, dominant_count = _most_common(self.quality_counts)
        dominant_effect, effect_count = _most_common(self.movement_effect_counts)
        unique_qualities = len(self.quality_counts)
        recurrent_exposure = (
            self.seen_count > 1
            or self.total_worlds_observed > 1
            or self.total_events > 1
        )

        if not recurrent_exposure:
            return "young"
        if dominant_effect == "rekoppelnd_entlastend" and (effect_count > 1 or recurrent_exposure):
            return "recurrently_reconnecting"
        if dominant_effect == "oeffnend_belastend" and (effect_count > 1 or recurrent_exposure):
            return "recurrently_opening_strain"
        if unique_qualities > 1 and dominant_count <= 1:
            return "mixed_unstable"
        if dominant_quality in {
            "rekoppelnd_beruhigend_schaerfend",
            "rekoppelnd_entlastend",
        }:
            return "recurrently_reconnecting"
        if dominant_quality in {
            "oeffnend_lauter_strainnaeher",
            "oeffnend_belastend",
        }:
            return "recurrently_opening_strain"
        if dominant_quality == "eng_getragen":
            return "recurrently_carried"
        if dominant_quality == "fragmentiert":
            return "recurrently_fragmented"
        if dominant_quality in {"breit_driftend", "offen_driftend"}:
            return "open_drifting"
        if len(self.asset_counts) > 1 and unique_qualities > 1:
            return "asset_sensitive"
        if len(self.timeframe_counts) > 1 and unique_qualities > 1:
            return "timeframe_sensitive"
        return "mixed_unstable" if unique_qualities > 1 else "world_specific"

    def maturity_note(self) -> str:
        dominant_quality, dominant_count = _most_common(self.quality_counts)
        recurrent_exposure = (
            self.seen_count > 1
            or self.total_worlds_observed > 1
            or self.total_events > 1
        )
        if not recurrent_exposure:
            return "young_trace"
        if self.seen_count <= 1 and self.total_worlds_observed > 1:
            return "cross_world_condensed_trace"
        if self.seen_count <= 1 and self.total_events > 1:
            return "event_condensed_trace"
        if dominant_count == self.seen_count and dominant_quality != "-":
            return "consistent_top_quality"
        if len(self.source_counts) > 1 and dominant_count > 1:
            return "cross_source_recurrent"
        if len(self.timeframe_counts) > 1 and dominant_count > 1:
            return "timeframe_recurrent"
        if len(self.year_counts) > 1 and dominant_count > 1:
            return "year_recurrent"
        return "variable_trace"

    def to_row(self) -> dict[str, object]:
        return {
            "movement_key": self.movement_key,
            "seen_count": self.seen_count,
            "total_events": self.total_events,
            "total_worlds_observed": self.total_worlds_observed,
            "dominant_tragart": self.dominant_quality(),
            "field_memory_quality": self.field_memory_quality(),
            "maturity_note": self.maturity_note(),
            "dominant_field_position": self.dominant_signature(),
            "dominant_drift_label": self.dominant_drift_label(),
            "dominant_movement_effect": self.dominant_movement_effect(),
            "avg_pressure_delta": round(self._average(self.pressure_delta_sum), 6),
            "avg_relaxation_delta": round(self._average(self.relaxation_delta_sum), 6),
            "avg_rekopplung_delta": round(self._average(self.rekopplung_delta_sum), 6),
            "avg_strain_delta": round(self._average(self.strain_delta_sum), 6),
            "avg_sharpness_delta": round(self._average(self.sharpness_delta_sum), 6),
            "avg_loudness_delta": round(self._average(self.loudness_delta_sum), 6),
            "avg_top_share": round(self.average_top_share, 6),
            "avg_top_signature_share": round(self.average_top_signature_share, 6),
            "tragart_profile": _counter_text(self.quality_counts),
            "field_position_profile": _counter_text(self.signature_counts),
            "drift_profile": _counter_text(self.drift_counts),
            "movement_effect_profile": _counter_text(self.movement_effect_counts),
            "timeframes": _counter_text(self.timeframe_counts),
            "assets": _counter_text(self.asset_counts),
            "years": _counter_text(self.year_counts),
            "sources": _counter_text(self.source_counts),
            "caution_note": "passive_not_actionable",
        }


def _counter_text(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return "; ".join(f"{key}:{value}" for key, value in counter.most_common())


class MCMFieldMovementMemory:
    def __init__(self) -> None:
        self.records: dict[str, MCMFieldMovementRecord] = {}

    def update_from_observation(self, observation: FieldMovementObservation) -> None:
        if not observation.movement_key or observation.movement_key == "-":
            return
        record = self.records.setdefault(
            observation.movement_key,
            MCMFieldMovementRecord(movement_key=observation.movement_key),
        )
        record.add(observation)

    def update_many(self, observations: Iterable[FieldMovementObservation]) -> None:
        for observation in observations:
            self.update_from_observation(observation)

    @classmethod
    def from_csv_paths(cls, paths: Iterable[Path]) -> MCMFieldMovementMemory:
        memory = cls()
        for path in paths:
            with Path(path).open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                for row in reader:
                    memory.update_from_observation(
                        FieldMovementObservation.from_row(row, source=Path(path).name)
                    )
        return memory

    def to_rows(self) -> list[dict[str, object]]:
        return sorted(
            (record.to_row() for record in self.records.values()),
            key=lambda row: (str(row["movement_key"])),
        )

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
        path.write_text(
            json.dumps(self.to_rows(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
