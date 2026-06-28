from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from mini_dio.dio_syntax import make_role_maturation_symbol


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
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


def _load_csv(path: Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _segment_by_short(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        token = str(row.get("token", "") or "")
        short = token.replace("dio_mcm_episode_", "")
        if short:
            out[short] = row
    return out


def _maturation_quality(follow_state: str, previous_axis_profile: str, segment: dict[str, str] | None) -> str:
    if follow_state == "reift_weiter":
        return "maturation_reifung"
    if follow_state == "jung_gehalten":
        return "maturation_jung_gehalten"
    if follow_state == "rolle_gehalten":
        if previous_axis_profile == "rekopplung_verliert_unschaerfe_steigt":
            return "maturation_reorganisationsbruecke_gehalten"
        return "maturation_rolle_gehalten"
    if follow_state == "verschwindet":
        return "maturation_verschwindet"
    if segment is None:
        return "maturation_offen"
    return "maturation_offen"


def _segment_quality(segment: dict[str, str] | None) -> str:
    if segment is None:
        return "segment_nicht_gelesen"
    segments = _safe_int(segment.get("segments"))
    worlds = _safe_int(segment.get("worlds"))
    duration = _safe_float(segment.get("duration_avg"))
    if segments >= 80 and worlds >= 5 and duration >= 10.0:
        return "lange_mehrweltphase"
    if segments >= 20 and worlds >= 4:
        return "mehrwelt_segmentbruecke"
    if segments >= 4 and worlds >= 3:
        return "kurze_mehrweltspur"
    if segments > 0:
        return "kurze_einzelspur"
    return "segment_nicht_gelesen"


def _field_quality(segment: dict[str, str] | None) -> str:
    if segment is None:
        return "feld_unguelesen"
    within_rek = _safe_float(segment.get("within_rekopplung_delta"))
    exit_rek = _safe_float(segment.get("exit_rekopplung_delta"))
    within_strain = _safe_float(segment.get("within_strain_delta"))
    exit_strain = _safe_float(segment.get("exit_strain_delta"))
    within_blur = _safe_float(segment.get("within_blur_delta"))
    exit_blur = _safe_float(segment.get("exit_blur_delta"))
    exit_loud = _safe_float(segment.get("exit_loudness_delta"))
    exit_tension = _safe_float(segment.get("exit_tension_delta"))

    if within_rek > 0.0 and within_strain < 0.0 and within_blur < 0.0 and exit_rek >= 0.0:
        return "feld_rekoppelnd_schaerfend"
    if within_rek > 0.0 and within_strain < 0.0 and exit_blur > 0.05:
        return "feld_jung_instabiler_austritt"
    if exit_strain > 0.02 or exit_loud > 0.08 or exit_tension > 0.05:
        return "feld_belastete_kernnaehe"
    if within_rek >= 0.0 and within_strain <= 0.0:
        return "feld_leicht_stabilisierend"
    if exit_rek < 0.0 and exit_strain > 0.0:
        return "feld_austritt_belastet"
    return "feld_gemischt"


def _memory_note(maturation_quality: str, segment_quality: str, field_quality: str) -> str:
    if maturation_quality == "maturation_reifung" and field_quality == "feld_rekoppelnd_schaerfend":
        return "young trace matures with coherent recoupling"
    if maturation_quality == "maturation_reifung":
        return "young trace becomes more central but needs follow-up"
    if maturation_quality == "maturation_reorganisationsbruecke_gehalten":
        return "reorganization bridge remains carried across follow world"
    if field_quality == "feld_belastete_kernnaehe":
        return "central proximity is carried but loaded"
    if maturation_quality == "maturation_verschwindet":
        return "trace fades from visible role space"
    if segment_quality == "kurze_mehrweltspur":
        return "short multiworld seed remains visible"
    return "maturation remains passive and open"


@dataclass
class RoleMaturationRecord:
    short_token: str
    previous_axis_profile: str
    previous_status: str
    previous_class: str
    follow_class: str
    follow_state: str
    follow_weight: int
    follow_world_span: int
    segments: int
    worlds: int
    segment_quality: str
    field_quality: str
    maturation_quality: str
    maturation_symbol: str
    memory_note: str

    @classmethod
    def from_rows(cls, follow_row: dict[str, str], segment_row: dict[str, str] | None) -> "RoleMaturationRecord":
        segment_quality = _segment_quality(segment_row)
        field_quality = _field_quality(segment_row)
        maturation_quality = _maturation_quality(
            str(follow_row.get("follow_state", "") or ""),
            str(follow_row.get("previous_axis_profile", "") or ""),
            segment_row,
        )
        payload = {
            "short_token": follow_row.get("short_token", ""),
            "previous_axis_profile": follow_row.get("previous_axis_profile", ""),
            "follow_state": follow_row.get("follow_state", ""),
            "maturation_quality": maturation_quality,
            "segment_quality": segment_quality,
            "field_quality": field_quality,
            "previous_class": follow_row.get("previous_class", ""),
            "follow_class": follow_row.get("follow_class", ""),
            "segments": _safe_int((segment_row or {}).get("segments")),
            "worlds": _safe_int((segment_row or {}).get("worlds")),
            "follow_weight": _safe_int(follow_row.get("follow_weight")),
        }
        return cls(
            short_token=str(payload["short_token"]),
            previous_axis_profile=str(payload["previous_axis_profile"]),
            previous_status=str(follow_row.get("previous_status", "") or ""),
            previous_class=str(payload["previous_class"]),
            follow_class=str(payload["follow_class"]),
            follow_state=str(payload["follow_state"]),
            follow_weight=_safe_int(payload["follow_weight"]),
            follow_world_span=_safe_int(follow_row.get("follow_world_span")),
            segments=_safe_int(payload["segments"]),
            worlds=_safe_int(payload["worlds"]),
            segment_quality=segment_quality,
            field_quality=field_quality,
            maturation_quality=maturation_quality,
            maturation_symbol=make_role_maturation_symbol(payload),
            memory_note=_memory_note(maturation_quality, segment_quality, field_quality),
        )

    def to_row(self) -> dict[str, object]:
        return {
            **PASSIVE_FLAGS,
            "maturation_symbol": self.maturation_symbol,
            "short_token": self.short_token,
            "previous_status": self.previous_status,
            "previous_axis_profile": self.previous_axis_profile,
            "previous_class": self.previous_class,
            "follow_class": self.follow_class,
            "follow_state": self.follow_state,
            "follow_weight": self.follow_weight,
            "follow_world_span": self.follow_world_span,
            "segments": self.segments,
            "worlds": self.worlds,
            "segment_quality": self.segment_quality,
            "field_quality": self.field_quality,
            "maturation_quality": self.maturation_quality,
            "memory_note": self.memory_note,
        }


class MCMRoleMaturationMemory:
    def __init__(self, records: list[RoleMaturationRecord] | None = None) -> None:
        self.records = list(records or [])

    @classmethod
    def from_csvs(cls, follow_path: Path, segment_path: Path) -> "MCMRoleMaturationMemory":
        segments = _segment_by_short(_load_csv(segment_path))
        records = [RoleMaturationRecord.from_rows(row, segments.get(str(row.get("short_token", "") or ""))) for row in _load_csv(follow_path)]
        return cls(records)

    def to_rows(self) -> list[dict[str, object]]:
        return [record.to_row() for record in self.records]

    def quality_profile(self) -> dict[str, object]:
        maturation = Counter(record.maturation_quality for record in self.records)
        segment = Counter(record.segment_quality for record in self.records)
        field = Counter(record.field_quality for record in self.records)
        return {
            "records": len(self.records),
            "maturation_quality": dict(maturation.most_common()),
            "segment_quality": dict(segment.most_common()),
            "field_quality": dict(field.most_common()),
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
    "MCMRoleMaturationMemory",
    "RoleMaturationRecord",
]
