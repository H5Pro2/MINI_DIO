from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_neighborhood_memory import PASSIVE_NEIGHBOR_BOUNDARY
from mini_dio.mcm_relation_lifecycle_memory import (
    PASSIVE_RELATION_LIFECYCLE_BOUNDARY,
)
from mini_dio.mcm_role_family_memory import PASSIVE_FLAGS
from mini_dio.mcm_topological_memory import PASSIVE_BOUNDARY


FINDING_DIR = ROOT / "docs" / "befunde" / "2001-3000"
PREFIX = "2126_MCM_ORGANISCHER_KOPPLUNGSTRAEGER_AUDIT"

REQUIREMENTS = (
    "field_derived_identity",
    "no_fixed_members",
    "no_distance_threshold",
    "no_fixed_direction_or_order",
    "causal_prefix_only",
    "within_contact_available",
    "independent_data_reproduced",
    "architecture_independent",
    "passive_no_action",
)


@dataclass(frozen=True)
class CarrierCandidate:
    candidate_id: str
    findings: str
    layer: str
    identity_origin: str
    relation_formation: str
    time_basis: str
    evidence_boundary: str
    bridge_role: str
    field_derived_identity: int
    no_fixed_members: int
    no_distance_threshold: int
    no_fixed_direction_or_order: int
    causal_prefix_only: int
    within_contact_available: int
    independent_data_reproduced: int
    architecture_independent: int
    passive_no_action: int
    code_boundary_verified: int

    def unmet(self) -> tuple[str, ...]:
        return tuple(
            requirement
            for requirement in REQUIREMENTS
            if not int(getattr(self, requirement))
        )

    def to_row(self) -> dict[str, object]:
        unmet = self.unmet()
        return {
            "candidate_id": self.candidate_id,
            "findings": self.findings,
            "layer": self.layer,
            "identity_origin": self.identity_origin,
            "relation_formation": self.relation_formation,
            "time_basis": self.time_basis,
            "evidence_boundary": self.evidence_boundary,
            "bridge_role": self.bridge_role,
            **{
                requirement: int(getattr(self, requirement))
                for requirement in REQUIREMENTS
            },
            "code_boundary_verified": self.code_boundary_verified,
            "unmet_requirements": "|".join(unmet),
            "ready_for_field_coupling": int(not unmet),
            "memory_written": 0,
            "field_modified": 0,
            "influences_action": 0,
            "viranz_parameter_used": 0,
        }


def _boundary_is_passive(boundary: dict) -> bool:
    return (
        int(boundary.get("passive_only", 0)) == 1
        and int(boundary.get("influences_action", 1)) == 0
        and int(boundary.get("is_gate", 1)) == 0
        and int(boundary.get("is_direction_signal", 1)) == 0
    )


def _candidates() -> tuple[CarrierCandidate, ...]:
    topology_passive = int(_boundary_is_passive(PASSIVE_BOUNDARY))
    neighborhood_passive = int(_boundary_is_passive(PASSIVE_NEIGHBOR_BOUNDARY))
    lifecycle_passive = int(
        _boundary_is_passive(PASSIVE_RELATION_LIFECYCLE_BOUNDARY)
    )
    family_passive = int(_boundary_is_passive(PASSIVE_FLAGS))
    return (
        CarrierCandidate(
            "role_family_memory",
            "2069-2074",
            "imported passive role-family evidence",
            "offline discovered role families imported from report CSVs",
            "stored family records and follow-world evidence",
            "after completed analyses",
            "partial family transfer; rf_05 remains fragmentary",
            "context evidence only",
            0, 0, 0, 1, 0, 0, 0, 0, 1, family_passive,
        ),
        CarrierCandidate(
            "episode_sequence_topology",
            "2075",
            "directed completed-episode topology",
            "inner episode symbols generated from closed field episodes",
            "observed predecessor to successor sequence",
            "within run after episode closure",
            "single-world repeat smoke test; no independent data holdout",
            "field-local topology precursor",
            1, 1, 1, 1, 1, 1, 0, 0, 1, topology_passive,
        ),
        CarrierCandidate(
            "mutual_episode_neighborhood",
            "2079,2088,2089",
            "passive world-profile neighborhood",
            "episode identities observed in completed worlds",
            "mutual nearest profiles without fixed pairs or distance threshold",
            "world finalization against prior completed worlds",
            "broad layer reproduces; exact old members remain mobile",
            "middle-scale organic topology substrate",
            1, 1, 1, 1, 1, 0, 1, 0, 1, neighborhood_passive,
        ),
        CarrierCandidate(
            "pareto_neighborhood_maturity",
            "2080-2083",
            "derived neighborhood maturity order",
            "passive neighborhood evidence axes",
            "non-dominated layers without weights or threshold",
            "after accumulated world-finalization evidence",
            "reifung order reproduced; no active allocation or forgetting",
            "maturity description only",
            1, 1, 1, 1, 1, 0, 1, 0, 1, neighborhood_passive,
        ),
        CarrierCandidate(
            "relation_lifecycle_neighborhood",
            "2090-2101",
            "event-derived relation lifecycle",
            "relations with complete own event history and equal event age",
            "mutual nearest breadth movement without fixed members",
            "causal append-only relation-event prefix at world finalization",
            "formation process reproduces; exact persistent members do not",
            "organic relevance-process candidate",
            1, 1, 1, 1, 1, 0, 1, 0, 1, lifecycle_passive,
        ),
        CarrierCandidate(
            "relation_synchronization_view",
            "2094-2101",
            "derived event-time synchronization topology",
            "relations sharing event age and event time",
            "retrospective synchrony with strong partner change",
            "reconstructed from causal relation-event history",
            "real mobile synchrony; no forward expectation after controls",
            "retrospective self-order view",
            1, 1, 1, 1, 1, 0, 1, 0, 1, lifecycle_passive,
        ),
        CarrierCandidate(
            "intrinsic_rank_form_and_cycle",
            "2110-2117",
            "field-local relational form and endogenous cycle",
            "directed rank relations between fixed indexed neurons",
            "successive own states and exact rank recurrence",
            "within continuous field contact",
            "field-local form and renewal reproduce; relevance selection does not",
            "strongest field-local carrier candidate",
            1, 0, 1, 0, 1, 1, 1, 0, 1, 1,
        ),
        CarrierCandidate(
            "activation_afterimage_coordination",
            "2122-2125",
            "multi-projection field-time coordination",
            "relative activation and afterimage support of indexed neurons",
            "shared endogenous closure times",
            "within continuous field contact",
            "holdout reproduction but dominant fixed index-direction dependence",
            "architecture diagnostic only",
            1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
        ),
    )


def _matrix_rows() -> list[dict[str, object]]:
    return [candidate.to_row() for candidate in _candidates()]


def _summary_rows(matrix: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        {
            "candidates": len(matrix),
            "ready_for_field_coupling": sum(
                int(row["ready_for_field_coupling"]) for row in matrix
            ),
            "field_local_carrier_candidate": "intrinsic_rank_form_and_cycle",
            "organic_relevance_process_candidate": "relation_lifecycle_neighborhood",
            "missing_bridge": (
                "field_local_relation_lifecycle_without_fixed_neuron_identity_"
                "direction_or_world_finalization"
            ),
            "runtime_change_justified": 0,
            "new_memory_justified": 0,
            "field_readback_justified": 0,
            "action_readback_justified": 0,
            "branch_status": "carrier_gap_localized_no_integration",
            "memory_written": 0,
            "field_modified": 0,
            "influences_action": 0,
            "viranz_parameter_used": 0,
        }
    ]


def _write_csv(name: str, rows: list[dict[str, object]]) -> None:
    path = FINDING_DIR / f"{PREFIX}.{name}.csv"
    fieldnames = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    matrix = _matrix_rows()
    summary = _summary_rows(matrix)
    _write_csv("matrix", matrix)
    _write_csv("summary", summary)
    print(
        f"candidates={summary[0]['candidates']} "
        f"ready={summary[0]['ready_for_field_coupling']} "
        f"field_local={summary[0]['field_local_carrier_candidate']} "
        f"relevance_process={summary[0]['organic_relevance_process_candidate']}"
    )
    for row in matrix:
        print(
            f"candidate={row['candidate_id']} ready={row['ready_for_field_coupling']} "
            f"unmet={row['unmet_requirements']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
