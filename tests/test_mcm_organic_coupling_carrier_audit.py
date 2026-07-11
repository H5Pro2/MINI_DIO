from __future__ import annotations

import unittest

from tools.run_mcm_organic_coupling_carrier_audit import (
    REQUIREMENTS,
    _candidates,
    _matrix_rows,
    _summary_rows,
)


class MCMOrganicCouplingCarrierAuditTest(unittest.TestCase):
    def test_candidates_and_requirements_are_unique(self) -> None:
        candidates = _candidates()

        self.assertEqual(
            len({candidate.candidate_id for candidate in candidates}),
            len(candidates),
        )
        self.assertEqual(len(set(REQUIREMENTS)), len(REQUIREMENTS))

    def test_no_candidate_is_silently_promoted_to_field_coupling(self) -> None:
        matrix = _matrix_rows()
        summary = _summary_rows(matrix)[0]

        self.assertEqual(summary["ready_for_field_coupling"], 0)
        self.assertTrue(all(row["unmet_requirements"] for row in matrix))
        self.assertTrue(all(row["passive_no_action"] == 1 for row in matrix))

    def test_audit_localizes_two_complementary_carriers(self) -> None:
        matrix = {row["candidate_id"]: row for row in _matrix_rows()}
        lifecycle = matrix["relation_lifecycle_neighborhood"]
        field_local = matrix["intrinsic_rank_form_and_cycle"]

        self.assertEqual(
            lifecycle["unmet_requirements"],
            "within_contact_available|architecture_independent",
        )
        self.assertEqual(field_local["within_contact_available"], 1)
        self.assertEqual(field_local["architecture_independent"], 0)
        self.assertEqual(field_local["no_fixed_direction_or_order"], 0)


if __name__ == "__main__":
    unittest.main()
