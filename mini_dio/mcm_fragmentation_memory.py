from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from mini_dio.dio_syntax import make_fragmentation_symbol


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


def _load_csv(path: Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _avg(rows: list[dict[str, str]], key: str) -> float:
    if not rows:
        return 0.0
    return sum(_safe_float(row.get(key)) for row in rows) / len(rows)


def _classify_fragmentation(
    zones_total: int,
    young_spur_count: int,
    class_counts: Counter[str],
) -> str:
    young_share = young_spur_count / max(1, zones_total)
    open_share = class_counts.get("nichtbruecke_offen", 0) / max(1, zones_total)
    rand_share = class_counts.get("nichtbruecke_randspannung", 0) / max(1, zones_total)
    weak_center_share = class_counts.get("nichtbruecke_zentrum_schwach", 0) / max(1, zones_total)
    rekopplung_share = class_counts.get("nichtbruecke_rekopplungsfeld", 0) / max(1, zones_total)

    if young_share >= 0.75 and open_share >= 0.35 and rand_share >= 0.20:
        return "fragmentierung_offen_randnah_jung"
    if young_share >= 0.70 and weak_center_share >= 0.20:
        return "fragmentierung_jung_mit_schwachem_zentrum"
    if rand_share >= 0.35:
        return "fragmentierung_randlastig"
    if open_share >= 0.45:
        return "fragmentierung_offene_oberflaeche"
    if rekopplung_share >= 0.10:
        return "fragmentierung_mit_rekopplungsresten"
    if young_share >= 0.60:
        return "fragmentierung_jung"
    return "fragmentierung_gemischt"


def _note(fragmentation_class: str) -> str:
    notes = {
        "fragmentierung_offen_randnah_jung": "Viele junge Spuren, offene Oberflaeche und Randspannung zugleich.",
        "fragmentierung_jung_mit_schwachem_zentrum": "Junge Spuren dominieren, aber schwache Zentrumsordnung bleibt vorhanden.",
        "fragmentierung_randlastig": "Randspannung dominiert die Oberflaeche.",
        "fragmentierung_offene_oberflaeche": "Offene Oberflaeche dominiert ohne starke Bindung.",
        "fragmentierung_mit_rekopplungsresten": "Fragmentierung bleibt mit Rekopplungsresten verbunden.",
        "fragmentierung_jung": "Junge Spuren dominieren ohne klare Rollenbindung.",
    }
    return notes.get(fragmentation_class, "Gemischte Fragmentierungsoberflaeche.")


@dataclass
class FragmentationRecord:
    world_label: str
    fragmentation_symbol: str
    fragmentation_class: str
    zones_total: int
    young_spur_count: int
    dominant_surface_class: str
    secondary_surface_class: str
    open_count: int
    rand_count: int
    weak_center_count: int
    rekopplung_count: int
    drift_count: int
    avg_strain: float
    avg_sensory: float
    avg_rekopplung: float
    memory_note: str

    @classmethod
    def from_rows(cls, world_label: str, nonbridge_rows: list[dict[str, str]], zone_rows: list[dict[str, str]]) -> "FragmentationRecord":
        class_counts = Counter(row.get("nonbridge_class", "-") for row in nonbridge_rows)
        zone_counts = Counter(row.get("condensation_zone", "-") for row in zone_rows)
        zones_total = len(nonbridge_rows)
        young_spur_count = zone_counts.get("junge_spur", 0)
        ranked = class_counts.most_common()
        dominant = ranked[0][0] if ranked else "-"
        secondary = ranked[1][0] if len(ranked) > 1 else "-"
        fragmentation_class = _classify_fragmentation(zones_total, young_spur_count, class_counts)
        payload = {
            "world_label": world_label,
            "fragmentation_class": fragmentation_class,
            "dominant_surface_class": dominant,
            "secondary_surface_class": secondary,
            "zones_total": zones_total,
            "young_spur_count": young_spur_count,
            "open_count": class_counts.get("nichtbruecke_offen", 0),
            "rand_count": class_counts.get("nichtbruecke_randspannung", 0),
            "weak_center_count": class_counts.get("nichtbruecke_zentrum_schwach", 0),
            "rekopplung_count": class_counts.get("nichtbruecke_rekopplungsfeld", 0),
            "avg_strain": _avg(nonbridge_rows, "avg_strain"),
            "avg_sensory": _avg(nonbridge_rows, "avg_sensory"),
            "avg_rekopplung": _avg(nonbridge_rows, "avg_rekopplung"),
        }
        return cls(
            world_label=world_label,
            fragmentation_symbol=make_fragmentation_symbol(payload),
            fragmentation_class=fragmentation_class,
            zones_total=zones_total,
            young_spur_count=young_spur_count,
            dominant_surface_class=dominant,
            secondary_surface_class=secondary,
            open_count=int(payload["open_count"]),
            rand_count=int(payload["rand_count"]),
            weak_center_count=int(payload["weak_center_count"]),
            rekopplung_count=int(payload["rekopplung_count"]),
            drift_count=class_counts.get("nichtbruecke_driftfeld", 0),
            avg_strain=float(payload["avg_strain"]),
            avg_sensory=float(payload["avg_sensory"]),
            avg_rekopplung=float(payload["avg_rekopplung"]),
            memory_note=_note(fragmentation_class),
        )

    def to_row(self) -> dict[str, object]:
        return {
            **PASSIVE_FLAGS,
            "fragmentation_symbol": self.fragmentation_symbol,
            "world_label": self.world_label,
            "fragmentation_class": self.fragmentation_class,
            "zones_total": self.zones_total,
            "young_spur_count": self.young_spur_count,
            "dominant_surface_class": self.dominant_surface_class,
            "secondary_surface_class": self.secondary_surface_class,
            "open_count": self.open_count,
            "rand_count": self.rand_count,
            "weak_center_count": self.weak_center_count,
            "rekopplung_count": self.rekopplung_count,
            "drift_count": self.drift_count,
            "avg_strain": round(self.avg_strain, 6),
            "avg_sensory": round(self.avg_sensory, 6),
            "avg_rekopplung": round(self.avg_rekopplung, 6),
            "memory_note": self.memory_note,
        }


class MCMFragmentationMemory:
    def __init__(self, records: list[FragmentationRecord] | None = None) -> None:
        self.records = list(records or [])

    @classmethod
    def from_csvs(cls, world_label: str, nonbridge_path: Path, zones_path: Path) -> "MCMFragmentationMemory":
        return cls([FragmentationRecord.from_rows(world_label, _load_csv(nonbridge_path), _load_csv(zones_path))])

    def to_rows(self) -> list[dict[str, object]]:
        return [record.to_row() for record in self.records]

    def quality_profile(self) -> dict[str, object]:
        return {
            "records": len(self.records),
            "fragmentation_class": dict(Counter(record.fragmentation_class for record in self.records).most_common()),
            "dominant_surface_class": dict(Counter(record.dominant_surface_class for record in self.records).most_common()),
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
    "FragmentationRecord",
    "MCMFragmentationMemory",
]
