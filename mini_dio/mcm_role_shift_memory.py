from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from mini_dio.dio_syntax import make_role_shift_symbol


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


def _shift_quality(row: dict[str, str]) -> str:
    read_state = str(row.get("read_state", "") or "")
    nonbridge_class = str(row.get("nonbridge_class", "") or "")
    longterm_class = str(row.get("longterm_class", "") or "")

    if nonbridge_class == "-":
        return "shift_nicht_sichtbar"
    if read_state == "reifung_bleibt_als_nichtbruecke_getragen":
        return "shift_bruecke_zu_zentrum_getragen"
    if read_state == "belastete_reifung_bleibt_sichtbar":
        return "shift_belastete_reifung_zu_zentrum"
    if read_state == "weltabhaengige_reifung_sichtbar":
        return "shift_weltabhaengig_zu_rekopplung"
    if read_state == "verlorene_reifung_taucht_umorganisiert_auf":
        return "shift_verlust_zu_randspur"
    if read_state == "oberflaeche_taucht_umorganisiert_auf":
        return "shift_oberflaeche_zu_offen"
    if read_state == "verschwindung_widersprochen_durch_nichtbruecke":
        if nonbridge_class in {"nichtbruecke_zentrum_getragen", "nichtbruecke_zentrum_schwach"}:
            return "shift_verschwinden_zu_zentrum"
        return "shift_verschwinden_widersprochen"
    if longterm_class == "kurzfristige_oberflaeche":
        return "shift_oberflaeche_offen"
    return "shift_offen"


def _shift_note(quality: str) -> str:
    notes = {
        "shift_bruecke_zu_zentrum_getragen": "Brueckenreifung bleibt als zentrumsnahe Feldform sichtbar.",
        "shift_belastete_reifung_zu_zentrum": "Belastete Reifung bleibt sichtbar, verliert aber die Brueckenrolle.",
        "shift_weltabhaengig_zu_rekopplung": "Weltabhaengige Reifung koppelt als Rekopplungsfeld wieder an.",
        "shift_verlust_zu_randspur": "Vorher verlorene Reifung taucht als Randspannung wieder auf.",
        "shift_oberflaeche_zu_offen": "Kurzfristige Oberflaeche bleibt als offene Form sichtbar.",
        "shift_verschwinden_zu_zentrum": "Verschwinden in Brueckenlogik war kein vollstaendiger Feldverlust.",
        "shift_verschwinden_widersprochen": "Verschwinden wird durch andere Feldform widersprochen.",
        "shift_nicht_sichtbar": "Zeichen bleibt in dieser Lesung unsichtbar.",
    }
    return notes.get(quality, "Rollenwechsel bleibt passiv offen.")


@dataclass
class RoleShiftRecord:
    short_token: str
    maturation_symbol: str
    shift_symbol: str
    from_longterm_class: str
    from_role_class: str
    to_nonbridge_class: str
    to_zone: str
    to_dominant_role: str
    observations: int
    worlds: int
    avg_rekopplung: float
    avg_strain: float
    read_state: str
    shift_quality: str
    shift_note: str

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "RoleShiftRecord":
        shift_quality = _shift_quality(row)
        payload = {
            "short_token": row.get("short_token", ""),
            "from_longterm_class": row.get("longterm_class", ""),
            "from_role_class": row.get("memory_follow_class", ""),
            "to_nonbridge_class": row.get("nonbridge_class", ""),
            "to_zone": row.get("condensation_zone", ""),
            "to_dominant_role": row.get("dominant_role", ""),
            "shift_quality": shift_quality,
            "observations": _safe_int(row.get("observations")),
            "worlds": _safe_int(row.get("worlds")),
            "avg_rekopplung": _safe_float(row.get("avg_rekopplung")),
            "avg_strain": _safe_float(row.get("avg_strain")),
        }
        return cls(
            short_token=str(payload["short_token"]),
            maturation_symbol=str(row.get("maturation_symbol", "") or ""),
            shift_symbol=make_role_shift_symbol(payload),
            from_longterm_class=str(payload["from_longterm_class"]),
            from_role_class=str(payload["from_role_class"]),
            to_nonbridge_class=str(payload["to_nonbridge_class"]),
            to_zone=str(payload["to_zone"]),
            to_dominant_role=str(payload["to_dominant_role"]),
            observations=_safe_int(payload["observations"]),
            worlds=_safe_int(payload["worlds"]),
            avg_rekopplung=_safe_float(payload["avg_rekopplung"]),
            avg_strain=_safe_float(payload["avg_strain"]),
            read_state=str(row.get("read_state", "") or ""),
            shift_quality=shift_quality,
            shift_note=_shift_note(shift_quality),
        )

    def to_row(self) -> dict[str, object]:
        return {
            **PASSIVE_FLAGS,
            "shift_symbol": self.shift_symbol,
            "maturation_symbol": self.maturation_symbol,
            "short_token": self.short_token,
            "from_longterm_class": self.from_longterm_class,
            "from_role_class": self.from_role_class,
            "to_nonbridge_class": self.to_nonbridge_class,
            "to_zone": self.to_zone,
            "to_dominant_role": self.to_dominant_role,
            "observations": self.observations,
            "worlds": self.worlds,
            "avg_rekopplung": round(self.avg_rekopplung, 6),
            "avg_strain": round(self.avg_strain, 6),
            "read_state": self.read_state,
            "shift_quality": self.shift_quality,
            "shift_note": self.shift_note,
        }


class MCMRoleShiftMemory:
    def __init__(self, records: list[RoleShiftRecord] | None = None) -> None:
        self.records = list(records or [])

    @classmethod
    def from_csv(cls, path: Path) -> "MCMRoleShiftMemory":
        return cls([RoleShiftRecord.from_row(row) for row in _load_csv(path)])

    def to_rows(self) -> list[dict[str, object]]:
        return [record.to_row() for record in self.records]

    def quality_profile(self) -> dict[str, object]:
        return {
            "records": len(self.records),
            "shift_quality": dict(Counter(record.shift_quality for record in self.records).most_common()),
            "to_nonbridge_class": dict(Counter(record.to_nonbridge_class for record in self.records).most_common()),
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
    "MCMRoleShiftMemory",
    "RoleShiftRecord",
]
