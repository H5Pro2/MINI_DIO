from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path

from mini_dio.dio_syntax import (
    make_role_family_evidence_symbol,
    make_role_family_memory_symbol,
)


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


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _load_csv(path: Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _member_list(value: object) -> list[str]:
    text = str(value or "").strip()
    if not text or text == "-":
        return []
    return [part.strip() for part in text.split(";") if part.strip()]


def _member_profile_symbols(value: object) -> list[str]:
    return [item.split(":", 1)[0].strip() for item in _member_list(value) if item]


def _by_role(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        role_family = str(row.get("role_family", "") or "")
        if role_family and role_family not in out:
            out[role_family] = row
    return out


@dataclass
class RoleFamilyMemoryRecord:
    role_family: str
    family_symbol: str
    evidence_symbol: str
    members: int
    member_symbols: str
    found_member_symbols: str
    has_cohesion_evidence: int
    has_legacy_follow_evidence: int
    has_same_basis_follow_evidence: int
    evidence_layers: str
    cohesion_total_events: int
    cohesion_event_concentration: float
    cohesion_shared_label_count: int
    cohesion_majority_label_count: int
    cohesion_mean_label_jaccard: float
    cohesion_min_label_jaccard: float
    cohesion_max_mcm_distance: float
    cohesion_mean_mcm_distance: float
    cohesion_avg_carry: float
    cohesion_avg_strain: float
    cohesion_avg_rekopplung: float
    cohesion_shared_labels: str
    cohesion_majority_labels: str
    legacy_found_members: int
    legacy_member_coverage: float
    legacy_real_follow_rows: int
    legacy_total_follow_events: int
    legacy_asset_profile: str
    legacy_member_event_profile: str
    legacy_mean_rekopplung_spaet: float
    legacy_mean_strain_spaet: float
    legacy_mean_afterimage_delta: float
    legacy_mean_temporal_delta: float
    same_basis_global_found_members: int
    same_basis_global_member_coverage: float
    same_basis_worlds: int
    same_basis_worlds_present: int
    same_basis_world_presence_ratio: float
    same_basis_whole_family_worlds: int
    same_basis_whole_family_ratio: float
    same_basis_partial_family_worlds: int
    same_basis_missing_worlds: int
    same_basis_assets_present: int
    same_basis_mean_member_coverage: float
    same_basis_total_follow_events: int
    same_basis_source_total_events: int
    same_basis_source_event_concentration: float
    same_basis_family_event_concentration: float
    same_basis_family_event_balance: float
    same_basis_source_member_event_profile: str
    same_basis_member_event_profile: str
    same_basis_mean_family_event_share: float
    same_basis_mean_phase_complete_ratio: float
    same_basis_mean_rekopplung_spaet: float
    same_basis_mean_strain_spaet: float
    same_basis_mean_afterimage_delta: float
    same_basis_mean_temporal_delta: float
    member_distribution_drift: float

    @classmethod
    def from_rows(
        cls,
        cohesion: dict[str, str],
        legacy_follow: dict[str, str] | None,
        same_basis_follow: dict[str, str] | None = None,
    ) -> "RoleFamilyMemoryRecord":
        role_family = str(cohesion.get("role_family", "") or "")
        members = _member_profile_symbols(cohesion.get("member_symbols"))
        family_symbol = make_role_family_memory_symbol(
            {
                "role_family": role_family,
                "member_symbols": ";".join(members),
            }
        )
        layers = ["cohesion"]
        if legacy_follow is not None:
            layers.append("legacy_follow")
        if same_basis_follow is not None:
            layers.append("same_basis_follow")

        values: dict[str, object] = {
            "role_family": role_family,
            "family_symbol": family_symbol,
            "members": _safe_int(cohesion.get("members")),
            "member_symbols": ";".join(members),
            "found_member_symbols": ";".join(
                _member_profile_symbols((legacy_follow or {}).get("member_profile"))
            ),
            "has_cohesion_evidence": 1,
            "has_legacy_follow_evidence": int(legacy_follow is not None),
            "has_same_basis_follow_evidence": int(same_basis_follow is not None),
            "evidence_layers": ";".join(layers),
            "cohesion_total_events": _safe_int(cohesion.get("total_follow_events")),
            "cohesion_event_concentration": _safe_float(cohesion.get("event_concentration")),
            "cohesion_shared_label_count": _safe_int(cohesion.get("shared_label_count")),
            "cohesion_majority_label_count": _safe_int(cohesion.get("majority_label_count")),
            "cohesion_mean_label_jaccard": _safe_float(cohesion.get("mean_label_jaccard")),
            "cohesion_min_label_jaccard": _safe_float(cohesion.get("min_label_jaccard")),
            "cohesion_max_mcm_distance": _safe_float(cohesion.get("max_mcm_distance")),
            "cohesion_mean_mcm_distance": _safe_float(cohesion.get("mean_mcm_distance")),
            "cohesion_avg_carry": _safe_float(cohesion.get("avg_carry")),
            "cohesion_avg_strain": _safe_float(cohesion.get("avg_strain")),
            "cohesion_avg_rekopplung": _safe_float(cohesion.get("avg_rekopplung")),
            "cohesion_shared_labels": str(cohesion.get("shared_labels", "") or ""),
            "cohesion_majority_labels": str(cohesion.get("majority_labels", "") or ""),
            "legacy_found_members": _safe_int((legacy_follow or {}).get("found_members")),
            "legacy_member_coverage": _safe_float((legacy_follow or {}).get("member_coverage")),
            "legacy_real_follow_rows": _safe_int((legacy_follow or {}).get("real_follow_rows")),
            "legacy_total_follow_events": _safe_int((legacy_follow or {}).get("total_follow_count")),
            "legacy_asset_profile": str((legacy_follow or {}).get("asset_profile", "") or ""),
            "legacy_member_event_profile": str((legacy_follow or {}).get("member_profile", "") or ""),
            "legacy_mean_rekopplung_spaet": _safe_float((legacy_follow or {}).get("mean_rekopplung_spaet")),
            "legacy_mean_strain_spaet": _safe_float((legacy_follow or {}).get("mean_strain_spaet")),
            "legacy_mean_afterimage_delta": _safe_float((legacy_follow or {}).get("mean_afterimage_delta")),
            "legacy_mean_temporal_delta": _safe_float((legacy_follow or {}).get("mean_temporal_delta")),
            "same_basis_global_found_members": _safe_int((same_basis_follow or {}).get("global_found_members")),
            "same_basis_global_member_coverage": _safe_float((same_basis_follow or {}).get("global_member_coverage")),
            "same_basis_worlds": _safe_int((same_basis_follow or {}).get("worlds")),
            "same_basis_worlds_present": _safe_int((same_basis_follow or {}).get("worlds_present")),
            "same_basis_world_presence_ratio": _safe_float((same_basis_follow or {}).get("world_presence_ratio")),
            "same_basis_whole_family_worlds": _safe_int((same_basis_follow or {}).get("whole_family_worlds")),
            "same_basis_whole_family_ratio": _safe_float((same_basis_follow or {}).get("whole_family_ratio")),
            "same_basis_partial_family_worlds": _safe_int((same_basis_follow or {}).get("partial_family_worlds")),
            "same_basis_missing_worlds": _safe_int((same_basis_follow or {}).get("missing_worlds")),
            "same_basis_assets_present": _safe_int((same_basis_follow or {}).get("assets_present")),
            "same_basis_mean_member_coverage": _safe_float((same_basis_follow or {}).get("mean_member_coverage")),
            "same_basis_total_follow_events": _safe_int((same_basis_follow or {}).get("total_follow_events")),
            "same_basis_source_total_events": _safe_int((same_basis_follow or {}).get("source_total_events")),
            "same_basis_source_event_concentration": _safe_float((same_basis_follow or {}).get("source_event_concentration")),
            "same_basis_family_event_concentration": _safe_float((same_basis_follow or {}).get("family_event_concentration")),
            "same_basis_family_event_balance": _safe_float((same_basis_follow or {}).get("family_event_balance")),
            "same_basis_source_member_event_profile": str((same_basis_follow or {}).get("source_member_event_profile", "") or ""),
            "same_basis_member_event_profile": str((same_basis_follow or {}).get("member_event_profile", "") or ""),
            "same_basis_mean_family_event_share": _safe_float((same_basis_follow or {}).get("mean_family_event_share")),
            "same_basis_mean_phase_complete_ratio": _safe_float((same_basis_follow or {}).get("mean_phase_complete_ratio")),
            "same_basis_mean_rekopplung_spaet": _safe_float((same_basis_follow or {}).get("mean_rekopplung_spaet")),
            "same_basis_mean_strain_spaet": _safe_float((same_basis_follow or {}).get("mean_strain_spaet")),
            "same_basis_mean_afterimage_delta": _safe_float((same_basis_follow or {}).get("mean_afterimage_delta")),
            "same_basis_mean_temporal_delta": _safe_float((same_basis_follow or {}).get("mean_temporal_delta")),
            "member_distribution_drift": _safe_float((same_basis_follow or {}).get("member_distribution_drift")),
        }
        evidence_symbol = make_role_family_evidence_symbol(values)
        return cls(evidence_symbol=evidence_symbol, **values)

    def to_row(self) -> dict[str, object]:
        return {
            **PASSIVE_FLAGS,
            "family_symbol": self.family_symbol,
            "evidence_symbol": self.evidence_symbol,
            "role_family": self.role_family,
            "members": self.members,
            "member_symbols": self.member_symbols,
            "found_member_symbols": self.found_member_symbols,
            "has_cohesion_evidence": self.has_cohesion_evidence,
            "has_legacy_follow_evidence": self.has_legacy_follow_evidence,
            "has_same_basis_follow_evidence": self.has_same_basis_follow_evidence,
            "evidence_layers": self.evidence_layers,
            "cohesion_total_events": self.cohesion_total_events,
            "cohesion_event_concentration": round(self.cohesion_event_concentration, 6),
            "cohesion_shared_label_count": self.cohesion_shared_label_count,
            "cohesion_majority_label_count": self.cohesion_majority_label_count,
            "cohesion_mean_label_jaccard": round(self.cohesion_mean_label_jaccard, 6),
            "cohesion_min_label_jaccard": round(self.cohesion_min_label_jaccard, 6),
            "cohesion_max_mcm_distance": round(self.cohesion_max_mcm_distance, 6),
            "cohesion_mean_mcm_distance": round(self.cohesion_mean_mcm_distance, 6),
            "cohesion_avg_carry": round(self.cohesion_avg_carry, 6),
            "cohesion_avg_strain": round(self.cohesion_avg_strain, 6),
            "cohesion_avg_rekopplung": round(self.cohesion_avg_rekopplung, 6),
            "cohesion_shared_labels": self.cohesion_shared_labels,
            "cohesion_majority_labels": self.cohesion_majority_labels,
            "legacy_found_members": self.legacy_found_members,
            "legacy_member_coverage": round(self.legacy_member_coverage, 6),
            "legacy_real_follow_rows": self.legacy_real_follow_rows,
            "legacy_total_follow_events": self.legacy_total_follow_events,
            "legacy_asset_profile": self.legacy_asset_profile,
            "legacy_member_event_profile": self.legacy_member_event_profile,
            "legacy_mean_rekopplung_spaet": round(self.legacy_mean_rekopplung_spaet, 6),
            "legacy_mean_strain_spaet": round(self.legacy_mean_strain_spaet, 6),
            "legacy_mean_afterimage_delta": round(self.legacy_mean_afterimage_delta, 6),
            "legacy_mean_temporal_delta": round(self.legacy_mean_temporal_delta, 6),
            "same_basis_global_found_members": self.same_basis_global_found_members,
            "same_basis_global_member_coverage": round(self.same_basis_global_member_coverage, 6),
            "same_basis_worlds": self.same_basis_worlds,
            "same_basis_worlds_present": self.same_basis_worlds_present,
            "same_basis_world_presence_ratio": round(self.same_basis_world_presence_ratio, 6),
            "same_basis_whole_family_worlds": self.same_basis_whole_family_worlds,
            "same_basis_whole_family_ratio": round(self.same_basis_whole_family_ratio, 6),
            "same_basis_partial_family_worlds": self.same_basis_partial_family_worlds,
            "same_basis_missing_worlds": self.same_basis_missing_worlds,
            "same_basis_assets_present": self.same_basis_assets_present,
            "same_basis_mean_member_coverage": round(self.same_basis_mean_member_coverage, 6),
            "same_basis_total_follow_events": self.same_basis_total_follow_events,
            "same_basis_source_total_events": self.same_basis_source_total_events,
            "same_basis_source_event_concentration": round(self.same_basis_source_event_concentration, 6),
            "same_basis_family_event_concentration": round(self.same_basis_family_event_concentration, 6),
            "same_basis_family_event_balance": round(self.same_basis_family_event_balance, 6),
            "same_basis_source_member_event_profile": self.same_basis_source_member_event_profile,
            "same_basis_member_event_profile": self.same_basis_member_event_profile,
            "same_basis_mean_family_event_share": round(self.same_basis_mean_family_event_share, 6),
            "same_basis_mean_phase_complete_ratio": round(self.same_basis_mean_phase_complete_ratio, 6),
            "same_basis_mean_rekopplung_spaet": round(self.same_basis_mean_rekopplung_spaet, 6),
            "same_basis_mean_strain_spaet": round(self.same_basis_mean_strain_spaet, 6),
            "same_basis_mean_afterimage_delta": round(self.same_basis_mean_afterimage_delta, 6),
            "same_basis_mean_temporal_delta": round(self.same_basis_mean_temporal_delta, 6),
            "member_distribution_drift": round(self.member_distribution_drift, 6),
            "caution_note": "passive_numeric_role_family_evidence_not_actionable",
        }


class MCMRoleFamilyMemory:
    def __init__(self, records: list[RoleFamilyMemoryRecord] | None = None) -> None:
        self.records = list(records or [])

    @classmethod
    def from_csvs(
        cls,
        cohesion_path: Path,
        connected_path: Path,
        same_basis_path: Path | None = None,
    ) -> "MCMRoleFamilyMemory":
        legacy = _by_role(_load_csv(connected_path))
        same_basis = _by_role(_load_csv(same_basis_path)) if same_basis_path else {}
        records = [
            RoleFamilyMemoryRecord.from_rows(
                row,
                legacy.get(str(row.get("role_family", "") or "")),
                same_basis.get(str(row.get("role_family", "") or "")),
            )
            for row in _load_csv(cohesion_path)
        ]
        return cls(records)

    def to_rows(self) -> list[dict[str, object]]:
        return [record.to_row() for record in self.records]

    def quality_profile(self) -> dict[str, object]:
        same_basis = [record for record in self.records if record.has_same_basis_follow_evidence]
        return {
            "records": len(self.records),
            "total_members": sum(record.members for record in self.records),
            "with_cohesion_evidence": sum(record.has_cohesion_evidence for record in self.records),
            "with_legacy_follow_evidence": sum(record.has_legacy_follow_evidence for record in self.records),
            "with_same_basis_follow_evidence": sum(record.has_same_basis_follow_evidence for record in self.records),
            "cohesion_events": sum(record.cohesion_total_events for record in self.records),
            "legacy_follow_events": sum(record.legacy_total_follow_events for record in self.records),
            "same_basis_follow_events": sum(record.same_basis_total_follow_events for record in self.records),
            "mean_same_basis_member_coverage": _mean(
                [record.same_basis_mean_member_coverage for record in same_basis]
            ),
            "mean_member_distribution_drift": _mean(
                [record.member_distribution_drift for record in same_basis]
            ),
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
    "MCMRoleFamilyMemory",
    "RoleFamilyMemoryRecord",
]
