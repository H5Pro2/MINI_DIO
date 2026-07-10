from __future__ import annotations

import unittest

from tools.run_mcm_relation_lifecycle_provenance_balance import (
    _has_simultaneous_next_age,
    _opportunities,
    _records,
)


class MCMRelationLifecycleProvenanceBalanceTest(unittest.TestCase):
    def test_relation_that_already_advanced_has_no_equal_age_opportunity(self) -> None:
        finalizations = {
            "left": {4: 10, 5: 11},
            "right": {4: 12},
        }

        self.assertFalse(
            _has_simultaneous_next_age(("left", "right"), 3, 12, finalizations)
        )

    def test_later_next_age_event_assigns_opportunity_provenance(self) -> None:
        finalizations = {
            "left": {4: 10},
            "right": {4: 12},
        }
        edges = {2: set(), 3: {("left", "right")}, 4: {("left", "right")}}

        opportunities, counts = _opportunities(
            finalizations, edges, {10: "DOGE_2024", 12: "XRP_2025"}
        )

        self.assertEqual(len(opportunities), 1)
        self.assertEqual(opportunities[0]["source"], "XRP_2025")
        self.assertEqual(opportunities[0]["continued"], 1)
        self.assertEqual(counts["exact_new"], 1)

    def test_source_age_records_preserve_labels_and_continuations(self) -> None:
        opportunities = [
            {"source": "DOGE_2024", "relation_age": 3, "label": "carried", "continued": 1},
            {"source": "DOGE_2024", "relation_age": 3, "label": "new", "continued": 0},
        ]

        records = _records(opportunities, ("source", "relation_age"))

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["carried_edges"], 1)
        self.assertEqual(records[0]["new_edges"], 1)
        self.assertEqual(records[0]["future_current_edges"], 1)
        self.assertEqual(records[0]["informative"], 1)


if __name__ == "__main__":
    unittest.main()
