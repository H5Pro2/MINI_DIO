from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path

from mini_dio.dio_syntax import (
    make_role_family_response_evidence_symbol,
    make_role_family_response_symbol,
)


PASSIVE_RESPONSE_FLAGS = {
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


@dataclass(frozen=True)
class ResponseEvidenceSource:
    evidence_id: str
    summary_path: Path
    world_year_profile: str
    timeframe_profile: str
    asset_profile: str
    overall_real_worlds: int
    subgroup_real_worlds: int
    phase_offsets: str = "17;83;251"

    def context(self, group: str) -> dict[str, object]:
        year_profile = self.world_year_profile
        timeframe_profile = self.timeframe_profile
        asset_profile = self.asset_profile
        real_worlds = self.overall_real_worlds
        if group.startswith("year:"):
            year_profile = group.split(":", 1)[1]
            real_worlds = self.subgroup_real_worlds
        elif group.startswith("timeframe:"):
            timeframe_profile = group.split(":", 1)[1]
            real_worlds = self.subgroup_real_worlds
        elif group.startswith("asset:"):
            asset_profile = group.split(":", 1)[1]
            real_worlds = self.subgroup_real_worlds
        return {
            "world_year_profile": year_profile,
            "timeframe_profile": timeframe_profile,
            "asset_profile": asset_profile,
            "real_worlds": real_worlds,
            "control_worlds": real_worlds * 3,
        }


@dataclass
class RoleFamilyComponentResponseRecord:
    response_symbol: str
    observation_symbol: str
    family_symbol: str
    role_family: str
    component: str
    members: int
    member_symbols: str
    evidence_id: str
    evidence_path: str
    context_group: str
    world_year_profile: str
    timeframe_profile: str
    asset_profile: str
    real_worlds: int
    control_worlds: int
    phase_offsets: str
    delta_continuity: float
    delta_event_share: float
    delta_member_coverage: float
    pseudo_mean_delta_continuity: float
    pseudo_mean_delta_event_share: float
    pseudo_mean_delta_member_coverage: float
    percentile_continuity: float
    percentile_event_share: float
    percentile_member_coverage: float
    mean_match_distance: float
    median_source_event_ratio: float

    @classmethod
    def from_summary_row(
        cls,
        row: dict[str, str],
        family: dict[str, str],
        source: ResponseEvidenceSource,
        evidence_path: str,
    ) -> "RoleFamilyComponentResponseRecord":
        role_family = str(row.get("role_family", "") or "")
        component = str(row.get("component", "") or "")
        context_group = str(row.get("group", "") or "overall")
        member_symbols = str(family.get("member_symbols", "") or "")
        context = source.context(context_group)
        response_symbol = make_role_family_response_symbol(
            {
                "role_family": role_family,
                "component": component,
                "member_symbols": member_symbols,
            }
        )
        values: dict[str, object] = {
            "response_symbol": response_symbol,
            "family_symbol": str(family.get("family_symbol", "") or ""),
            "role_family": role_family,
            "component": component,
            "members": _safe_int(family.get("members")),
            "member_symbols": member_symbols,
            "evidence_id": source.evidence_id,
            "evidence_path": evidence_path,
            "context_group": context_group,
            "world_year_profile": str(context["world_year_profile"]),
            "timeframe_profile": str(context["timeframe_profile"]),
            "asset_profile": str(context["asset_profile"]),
            "real_worlds": int(context["real_worlds"]),
            "control_worlds": int(context["control_worlds"]),
            "phase_offsets": source.phase_offsets,
            "delta_continuity": _safe_float(
                row.get("observed_control_minus_real_family_continuity_score")
            ),
            "delta_event_share": _safe_float(
                row.get("observed_control_minus_real_mean_family_event_share")
            ),
            "delta_member_coverage": _safe_float(
                row.get("observed_control_minus_real_mean_member_coverage")
            ),
            "pseudo_mean_delta_continuity": _safe_float(
                row.get("pseudo_mean_control_minus_real_family_continuity_score")
            ),
            "pseudo_mean_delta_event_share": _safe_float(
                row.get("pseudo_mean_control_minus_real_mean_family_event_share")
            ),
            "pseudo_mean_delta_member_coverage": _safe_float(
                row.get("pseudo_mean_control_minus_real_mean_member_coverage")
            ),
            "percentile_continuity": _safe_float(
                row.get("observed_percentile_control_minus_real_family_continuity_score")
            ),
            "percentile_event_share": _safe_float(
                row.get("observed_percentile_control_minus_real_mean_family_event_share")
            ),
            "percentile_member_coverage": _safe_float(
                row.get("observed_percentile_control_minus_real_mean_member_coverage")
            ),
            "mean_match_distance": _safe_float(row.get("mean_match_distance")),
            "median_source_event_ratio": _safe_float(
                row.get("median_source_event_ratio")
            ),
        }
        observation_symbol = make_role_family_response_evidence_symbol(values)
        return cls(observation_symbol=observation_symbol, **values)

    def to_row(self) -> dict[str, object]:
        return {
            **PASSIVE_RESPONSE_FLAGS,
            "response_symbol": self.response_symbol,
            "observation_symbol": self.observation_symbol,
            "family_symbol": self.family_symbol,
            "role_family": self.role_family,
            "component": self.component,
            "members": self.members,
            "member_symbols": self.member_symbols,
            "evidence_id": self.evidence_id,
            "evidence_path": self.evidence_path,
            "context_group": self.context_group,
            "world_year_profile": self.world_year_profile,
            "timeframe_profile": self.timeframe_profile,
            "asset_profile": self.asset_profile,
            "real_worlds": self.real_worlds,
            "control_worlds": self.control_worlds,
            "phase_offsets": self.phase_offsets,
            "delta_continuity": round(self.delta_continuity, 6),
            "delta_event_share": round(self.delta_event_share, 6),
            "delta_member_coverage": round(self.delta_member_coverage, 6),
            "pseudo_mean_delta_continuity": round(
                self.pseudo_mean_delta_continuity, 6
            ),
            "pseudo_mean_delta_event_share": round(
                self.pseudo_mean_delta_event_share, 6
            ),
            "pseudo_mean_delta_member_coverage": round(
                self.pseudo_mean_delta_member_coverage, 6
            ),
            "percentile_continuity": round(self.percentile_continuity, 6),
            "percentile_event_share": round(self.percentile_event_share, 6),
            "percentile_member_coverage": round(self.percentile_member_coverage, 6),
            "mean_match_distance": round(self.mean_match_distance, 6),
            "median_source_event_ratio": round(self.median_source_event_ratio, 6),
            "caution_note": "passive_numeric_family_component_response_not_actionable",
        }


class MCMRoleFamilyResponseMemory:
    def __init__(
        self,
        records: list[RoleFamilyComponentResponseRecord] | None = None,
    ) -> None:
        self.records = list(records or [])

    def append(self, record: RoleFamilyComponentResponseRecord) -> bool:
        if any(
            existing.observation_symbol == record.observation_symbol
            for existing in self.records
        ):
            return False
        self.records.append(record)
        self.records.sort(
            key=lambda item: (
                item.role_family,
                item.component,
                item.evidence_id,
                item.context_group,
            )
        )
        return True

    @classmethod
    def from_sources(
        cls,
        family_memory_path: Path,
        sources: list[ResponseEvidenceSource],
        root: Path | None = None,
    ) -> "MCMRoleFamilyResponseMemory":
        families = {
            str(row.get("role_family", "") or ""): row
            for row in _load_csv(family_memory_path)
        }
        memory = cls()
        for source in sources:
            try:
                evidence_path = source.summary_path.resolve().relative_to(root.resolve()).as_posix() if root else str(source.summary_path)
            except ValueError:
                evidence_path = str(source.summary_path.resolve())
            for row in _load_csv(source.summary_path):
                role_family = str(row.get("role_family", "") or "")
                family = families.get(role_family)
                if family is None:
                    raise ValueError(
                        f"Rollenfamilie aus {source.summary_path} fehlt in Memory: {role_family}"
                    )
                memory.append(
                    RoleFamilyComponentResponseRecord.from_summary_row(
                        row,
                        family,
                        source,
                        evidence_path,
                    )
                )
        return memory

    def to_rows(self) -> list[dict[str, object]]:
        return [record.to_row() for record in self.records]

    def quality_profile(self) -> dict[str, object]:
        rows = self.to_rows()
        return {
            "records": len(rows),
            "response_identities": len({row["response_symbol"] for row in rows}),
            "observation_identities": len({row["observation_symbol"] for row in rows}),
            "families": len({row["role_family"] for row in rows}),
            "components": len({row["component"] for row in rows}),
            "evidence_sources": len({row["evidence_id"] for row in rows}),
            "contexts": len(
                {
                    (
                        row["world_year_profile"],
                        row["timeframe_profile"],
                        row["asset_profile"],
                        row["context_group"],
                    )
                    for row in rows
                }
            ),
            "mean_percentile_continuity": _mean(
                [_safe_float(row["percentile_continuity"]) for row in rows]
            ),
            "mean_percentile_event_share": _mean(
                [_safe_float(row["percentile_event_share"]) for row in rows]
            ),
            "mean_percentile_member_coverage": _mean(
                [_safe_float(row["percentile_member_coverage"]) for row in rows]
            ),
            **PASSIVE_RESPONSE_FLAGS,
        }

    def validate(self) -> list[str]:
        rows = self.to_rows()
        errors: list[str] = []
        forbidden_fields = {
            "observed_relation",
            "expected_relation",
            "response_class",
            "meaning",
            "confirmed",
            "prediction",
        }
        for field in forbidden_fields:
            if any(field in row for row in rows):
                errors.append(f"forbidden_field:{field}")
        if len({row["observation_symbol"] for row in rows}) != len(rows):
            errors.append("observation_symbols_not_unique")
        for row in rows:
            for flag, expected in PASSIVE_RESPONSE_FLAGS.items():
                if _safe_int(row.get(flag)) != expected:
                    errors.append(f"passive_flag:{row['observation_symbol']}:{flag}")
            for field in (
                "percentile_continuity",
                "percentile_event_share",
                "percentile_member_coverage",
            ):
                value = _safe_float(row.get(field))
                if not 0.0 <= value <= 1.0:
                    errors.append(
                        f"percentile_out_of_range:{row['observation_symbol']}:{field}"
                    )
        return errors

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
        path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )


__all__ = [
    "MCMRoleFamilyResponseMemory",
    "PASSIVE_RESPONSE_FLAGS",
    "ResponseEvidenceSource",
    "RoleFamilyComponentResponseRecord",
]
