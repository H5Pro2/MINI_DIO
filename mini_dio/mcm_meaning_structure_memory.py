from __future__ import annotations

from dataclasses import dataclass


def _safe_float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def _quality_band(value: float, *, low: float, high: float) -> str:
    if value <= low:
        return "niedrig"
    if value >= high:
        return "hoch"
    return "mittel"


@dataclass(frozen=True)
class MCMMeaningStructure:
    meaning_key: str
    field_form: str
    asset_coloring: str
    dominant_sequence: str
    raw_profile: str
    scale_profile: str
    sensory_profile: str
    windows: int
    avg_auditory: float
    avg_visual_sharpness: float
    avg_field_pressure: float
    avg_range_pct: float

    def as_row(self) -> dict[str, object]:
        return {
            "meaning_key": self.meaning_key,
            "field_form": self.field_form,
            "asset_coloring": self.asset_coloring,
            "dominant_sequence": self.dominant_sequence,
            "raw_profile": self.raw_profile,
            "scale_profile": self.scale_profile,
            "sensory_profile": self.sensory_profile,
            "windows": self.windows,
            "avg_auditory": round(self.avg_auditory, 6),
            "avg_visual_sharpness": round(self.avg_visual_sharpness, 6),
            "avg_field_pressure": round(self.avg_field_pressure, 6),
            "avg_range_pct": round(self.avg_range_pct, 6),
            "passive_only": 1,
            "influences_action": 0,
            "is_gate": 0,
            "is_direction_signal": 0,
        }


def build_meaning_structure_from_asset_row(row: dict[str, object]) -> MCMMeaningStructure:
    asset = str(row.get("group", "UNKNOWN") or "UNKNOWN")
    raw_profile = str(row.get("dominant_raw_class", "unknown") or "unknown")
    sequence = str(row.get("dominant_sequence", "unknown") or "unknown")
    auditory = _safe_float(row.get("avg_auditory"))
    visual = _safe_float(row.get("avg_visual_sharpness"))
    pressure = _safe_float(row.get("avg_field_pressure"))
    range_pct = _safe_float(row.get("avg_range_pct"))
    auditory_band = _quality_band(auditory, low=0.22, high=0.50)
    visual_band = _quality_band(visual, low=0.62, high=0.72)
    pressure_band = _quality_band(pressure, low=0.08, high=0.18)
    range_band = _quality_band(range_pct, low=0.15, high=0.45)
    field_form = f"zwischenlage_{raw_profile}"
    asset_coloring = f"{asset.lower()}_{sequence.replace('->', '_zu_')}"
    scale_profile = str(row.get("scale_counts", "unknown") or "unknown")
    sensory_profile = (
        f"hoeren_{auditory_band}|sehen_{visual_band}|"
        f"felddruck_{pressure_band}|range_{range_band}"
    )
    meaning_key = f"mcm_meaning_{field_form}_{asset.lower()}"
    return MCMMeaningStructure(
        meaning_key=meaning_key,
        field_form=field_form,
        asset_coloring=asset_coloring,
        dominant_sequence=sequence,
        raw_profile=raw_profile,
        scale_profile=scale_profile,
        sensory_profile=sensory_profile,
        windows=_safe_int(row.get("count")),
        avg_auditory=auditory,
        avg_visual_sharpness=visual,
        avg_field_pressure=pressure,
        avg_range_pct=range_pct,
    )


class MCMMeaningStructureMemory:
    def __init__(self) -> None:
        self._items: list[MCMMeaningStructure] = []

    def observe_asset_row(self, row: dict[str, object]) -> None:
        self._items.append(build_meaning_structure_from_asset_row(row))

    def rows(self) -> list[dict[str, object]]:
        return [item.as_row() for item in self._items]

