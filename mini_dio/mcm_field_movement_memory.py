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
        rek_up = _pressure(self.rekopplung_delta, 0.02)
        rek_down = _pressure(-self.rekopplung_delta, 0.02)
        pressure_up = _pressure(self.pressure_delta, 0.02)
        pressure_down = _pressure(-self.pressure_delta, 0.02)
        strain_up = _pressure(self.strain_delta, 0.02)
        strain_down = _pressure(-self.strain_delta, 0.02)
        relaxation_up = _pressure(self.relaxation_delta, 0.02)
        loud_up = _pressure(self.loudness_delta, 0.04)
        loud_down = _pressure(-self.loudness_delta, 0.04)
        sharpness_motion = _pressure(abs(self.sharpness_delta), 0.02)
        any_motion = _mean(
            _pressure(abs(self.pressure_delta), 0.02),
            _pressure(abs(self.relaxation_delta), 0.02),
            _pressure(abs(self.rekopplung_delta), 0.02),
            _pressure(abs(self.strain_delta), 0.02),
            sharpness_motion,
            _pressure(abs(self.loudness_delta), 0.04),
        )
        return _dominant_label(
            {
                "rekoppelnd_entlastend": _mean(rek_up, pressure_down, strain_down, loud_down),
                "oeffnend_belastend": _mean(rek_down, pressure_up, strain_up, loud_up),
                "rekoppelnd": _mean(rek_up, relaxation_up, 1.0 - pressure_up),
                "spannungsnah": _mean(pressure_up, strain_up, loud_up),
                "bewegung_offen": _mean(any_motion, 1.0 - max(rek_up, rek_down), sharpness_motion),
            },
            default="bewegung_offen",
        ) if any_motion > 0.0 else ""


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
        exposure_pressure = _mean(
            _pressure(self.seen_count, 1.0),
            _pressure(self.total_worlds_observed, 1.0),
            _pressure(self.total_events, 1.0),
        )
        dominant_pressure = _pressure(dominant_count, max(1.0, float(self.seen_count)))
        effect_pressure = _pressure(effect_count, max(1.0, float(self.seen_count)))
        variety_pressure = _pressure(unique_qualities, 1.0)
        asset_pressure = _pressure(len(self.asset_counts), 1.0)
        timeframe_pressure = _pressure(len(self.timeframe_counts), 1.0)
        reconnect_label = 1.0 if dominant_effect == "rekoppelnd_entlastend" or dominant_quality in {
            "rekoppelnd_beruhigend_schaerfend",
            "rekoppelnd_entlastend",
        } else 0.0
        opening_label = 1.0 if dominant_effect == "oeffnend_belastend" or dominant_quality in {
            "oeffnend_lauter_strainnaeher",
            "oeffnend_belastend",
        } else 0.0
        carried_label = 1.0 if dominant_quality == "eng_getragen" else 0.0
        fragmented_label = 1.0 if dominant_quality == "fragmentiert" else 0.0
        drifting_label = 1.0 if dominant_quality in {"breit_driftend", "offen_driftend"} else 0.0
        return _dominant_label(
            {
                "young": 1.0 - exposure_pressure,
                "recurrently_reconnecting": _mean(exposure_pressure, reconnect_label, effect_pressure),
                "recurrently_opening_strain": _mean(exposure_pressure, opening_label, effect_pressure),
                "mixed_unstable": _mean(variety_pressure, 1.0 - dominant_pressure),
                "recurrently_carried": _mean(exposure_pressure, carried_label, dominant_pressure),
                "recurrently_fragmented": _mean(exposure_pressure, fragmented_label, dominant_pressure),
                "open_drifting": _mean(exposure_pressure, drifting_label, variety_pressure),
                "asset_sensitive": _mean(asset_pressure, variety_pressure),
                "timeframe_sensitive": _mean(timeframe_pressure, variety_pressure),
                "world_specific": _mean(exposure_pressure, dominant_pressure, 1.0 - variety_pressure),
            },
            default="world_specific",
        )

    def maturity_note(self) -> str:
        dominant_quality, dominant_count = _most_common(self.quality_counts)
        exposure_pressure = _mean(
            _pressure(self.seen_count, 1.0),
            _pressure(self.total_worlds_observed, 1.0),
            _pressure(self.total_events, 1.0),
        )
        seen_pressure = _pressure(self.seen_count, 1.0)
        world_pressure = _pressure(self.total_worlds_observed, 1.0)
        event_pressure = _pressure(self.total_events, 1.0)
        dominant_pressure = _pressure(dominant_count, max(1.0, float(self.seen_count)))
        named_quality = 1.0 if dominant_quality != "-" else 0.0
        return _dominant_label(
            {
                "young_trace": 1.0 - exposure_pressure,
                "cross_world_condensed_trace": _mean(1.0 - seen_pressure, world_pressure),
                "event_condensed_trace": _mean(1.0 - seen_pressure, event_pressure),
                "consistent_top_quality": _mean(dominant_pressure, named_quality),
                "cross_source_recurrent": _mean(_pressure(len(self.source_counts), 1.0), dominant_pressure),
                "timeframe_recurrent": _mean(_pressure(len(self.timeframe_counts), 1.0), dominant_pressure),
                "year_recurrent": _mean(_pressure(len(self.year_counts), 1.0), dominant_pressure),
                "variable_trace": _mean(exposure_pressure, 1.0 - dominant_pressure),
            },
            default="variable_trace",
        )

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
