from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from mini_dio.dio_syntax import make_role_movement_symbol


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


CLASS_RANK = {
    "-": 0,
    "schwacher_anschluss": 1,
    "schwacher_brueckenpfad": 1,
    "lokaler_anschlussanker": 2,
    "starker_anschlussanker": 3,
    "brueckenkern": 4,
}


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _clip01(value: object) -> float:
    return max(0.0, min(1.0, _safe_float(value)))


def _pressure(value: object, scale: float = 1.0) -> float:
    amount = max(0.0, _safe_float(value))
    return amount / (amount + max(0.000001, scale))


def _mean(*values: object) -> float:
    clean = [_clip01(value) for value in values]
    return sum(clean) / max(1, len(clean))


def _dominant_label(scores: dict[str, float], default: str) -> str:
    clean = {key: _clip01(value) for key, value in scores.items()}
    if not clean:
        return default
    return max(clean, key=clean.get)


def _split_sequence(value: object) -> list[str]:
    text = str(value or "").strip()
    if not text:
        return []
    return [part.strip() for part in text.split("->")]


def _rank_sequence(classes: list[str]) -> list[int]:
    return [CLASS_RANK.get(item, 0) for item in classes]


def _role_movement_quality(trend: str) -> str:
    if trend == "kernnah_gehalten":
        return "role_core_near_retained"
    if trend == "aufsteigende_verdichtung":
        return "role_condensing"
    if trend == "rollendrift":
        return "role_drifting"
    if trend == "absteigende_entlastung":
        return "role_releasing"
    if trend == "stabile_rolle":
        return "role_stable"
    return "role_open"


def _stability_quality(classes: list[str], weights: list[int]) -> str:
    ranks = _rank_sequence(classes)
    visible = [rank for rank in ranks if rank > 0]
    if not visible:
        return "not_visible"
    rank_span = max(ranks) - min(ranks)
    max_rank_pressure = _pressure(max(ranks), 3.0)
    stability_pressure = 1.0 - _pressure(rank_span, 1.0)
    retained_pressure = _mean(max_rank_pressure, _pressure(ranks[-1], 2.0))
    weight_gain = (weights[-1] - weights[0]) if weights else 0
    weight_gain_pressure = _pressure(weight_gain, 1.0)
    rank_gain_pressure = _pressure(ranks[-1] - ranks[0], 1.0)
    rank_loss_pressure = _pressure(ranks[0] - ranks[-1], 1.0)
    return _dominant_label(
        {
            "stable_core": _mean(stability_pressure, max_rank_pressure),
            "core_near_retained": retained_pressure,
            "stable_surface": _mean(stability_pressure, 1.0 - max_rank_pressure),
            "gaining_weight": _mean(weight_gain_pressure, rank_gain_pressure),
            "losing_role_weight": rank_loss_pressure,
            "variable_but_carried": _mean(1.0 - stability_pressure, retained_pressure),
        },
        default="variable_but_carried",
    )


def _drift_quality(classes: list[str], trend: str) -> str:
    ranks = _rank_sequence(classes)
    if trend == "rollendrift":
        return "explicit_role_drift"
    if trend == "absteigende_entlastung":
        return "role_releasing_or_fading"
    rank_span = max(ranks, default=0) - min(ranks, default=0)
    drift_pressure = _pressure(rank_span, 1.0)
    core_pressure = _pressure(max(ranks, default=0), 3.0)
    return _dominant_label(
        {
            "core_boundary_movement": _mean(drift_pressure, core_pressure),
            "surface_role_movement": _mean(drift_pressure, 1.0 - core_pressure),
            "low_drift": 1.0 - drift_pressure,
        },
        default="low_drift",
    )


def _memory_note(row: dict[str, str], classes: list[str]) -> str:
    trend = row.get("trend", "")
    if trend == "kernnah_gehalten":
        return "role stays near core while surface class may move"
    if trend == "aufsteigende_verdichtung":
        return "role gains density across landscapes"
    if trend == "rollendrift":
        return "role changes direction or loses temporary density"
    if trend == "absteigende_entlastung":
        return "role releases or fades across landscapes"
    if trend == "stabile_rolle":
        return "role remains stable across landscapes"
    if classes:
        return "role movement remains open"
    return "role not visible"


@dataclass
class RoleMovementRecord:
    short_token: str
    class_sequence: str
    weight_sequence: str
    world_span_sequence: str
    trend: str
    role_movement_quality: str
    stability_quality: str
    drift_quality: str
    role_symbol: str
    max_rank: int
    weight_delta_total: int
    memory_note: str

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "RoleMovementRecord":
        classes = _split_sequence(row.get("class_sequence", ""))
        weights = [_safe_int(part) for part in _split_sequence(row.get("weight_sequence", ""))]
        trend = str(row.get("trend", "") or "role_open")
        max_rank = max(_rank_sequence(classes), default=0)
        weight_delta_total = _safe_int(row.get("weight_delta_total", "0"))
        payload = {
            "short_token": row.get("short_token", ""),
            "class_sequence": row.get("class_sequence", ""),
            "trend": trend,
            "role_movement_quality": _role_movement_quality(trend),
            "stability_quality": _stability_quality(classes, weights),
            "drift_quality": _drift_quality(classes, trend),
            "max_rank": max_rank,
            "weight_delta_total": weight_delta_total,
        }
        return cls(
            short_token=str(row.get("short_token", "") or ""),
            class_sequence=str(row.get("class_sequence", "") or ""),
            weight_sequence=str(row.get("weight_sequence", "") or ""),
            world_span_sequence=str(row.get("world_span_sequence", "") or ""),
            trend=trend,
            role_movement_quality=str(payload["role_movement_quality"]),
            stability_quality=str(payload["stability_quality"]),
            drift_quality=str(payload["drift_quality"]),
            role_symbol=make_role_movement_symbol(payload),
            max_rank=max_rank,
            weight_delta_total=weight_delta_total,
            memory_note=_memory_note(row, classes),
        )

    def to_row(self) -> dict[str, object]:
        return {
            **PASSIVE_FLAGS,
            "role_symbol": self.role_symbol,
            "short_token": self.short_token,
            "class_sequence": self.class_sequence,
            "weight_sequence": self.weight_sequence,
            "world_span_sequence": self.world_span_sequence,
            "trend": self.trend,
            "role_movement_quality": self.role_movement_quality,
            "stability_quality": self.stability_quality,
            "drift_quality": self.drift_quality,
            "max_rank": self.max_rank,
            "weight_delta_total": self.weight_delta_total,
            "memory_note": self.memory_note,
        }


class MCMRoleMovementMemory:
    def __init__(self, records: list[RoleMovementRecord] | None = None) -> None:
        self.records = list(records or [])

    @classmethod
    def from_csv(cls, path: Path) -> "MCMRoleMovementMemory":
        with Path(path).open(newline="", encoding="utf-8") as handle:
            records = [RoleMovementRecord.from_row(row) for row in csv.DictReader(handle)]
        return cls(records)

    def to_rows(self) -> list[dict[str, object]]:
        return [record.to_row() for record in self.records]

    def quality_profile(self) -> dict[str, object]:
        movement = Counter(record.role_movement_quality for record in self.records)
        stability = Counter(record.stability_quality for record in self.records)
        drift = Counter(record.drift_quality for record in self.records)
        return {
            "records": len(self.records),
            "movement_quality": dict(movement.most_common()),
            "stability_quality": dict(stability.most_common()),
            "drift_quality": dict(drift.most_common()),
            **PASSIVE_FLAGS,
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
    "MCMRoleMovementMemory",
    "RoleMovementRecord",
]
