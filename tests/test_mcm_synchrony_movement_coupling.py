from __future__ import annotations

import unittest

from tools.run_mcm_synchrony_movement_coupling import (
    _coupling_records,
    _stats,
)


class MCMSynchronyMovementCouplingTest(unittest.TestCase):
    def test_coupling_uses_only_relations_present_at_both_ages(self) -> None:
        nodes = {2: {"a", "b", "c"}, 3: {"a", "b"}}
        synchrony = {
            2: {("a", "b"), ("a", "c")},
            3: {("a", "b")},
        }
        lifecycle = {2: {("a", "b"), ("a", "c")}}

        records = _coupling_records(nodes, synchrony, lifecycle)

        self.assertEqual(records, [])

    def test_selected_and_unselected_pairs_share_same_synchrony_opportunity(self) -> None:
        nodes = {2: {"a", "b", "c"}, 3: {"a", "b", "c"}}
        synchrony = {
            2: {("a", "b"), ("a", "c"), ("b", "c")},
            3: {("a", "b"), ("b", "c")},
        }
        lifecycle = {2: {("a", "b")}}

        records = _coupling_records(nodes, synchrony, lifecycle)

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["movement_selected_pairs"], 1)
        self.assertEqual(records[0]["movement_selected_retained"], 1)
        self.assertEqual(records[0]["not_selected_pairs"], 2)
        self.assertEqual(records[0]["not_selected_retained"], 1)

    def test_aggregate_stats_keep_age_strata_separate(self) -> None:
        records = [
            {
                "relation_age": 2,
                "synchrony_pairs": 4,
                "movement_selected_pairs": 2,
                "movement_selected_retained": 2,
                "not_selected_pairs": 2,
                "not_selected_retained": 1,
                "retained_current_pairs": 3,
            },
            {
                "relation_age": 3,
                "synchrony_pairs": 4,
                "movement_selected_pairs": 2,
                "movement_selected_retained": 1,
                "not_selected_pairs": 2,
                "not_selected_retained": 1,
                "retained_current_pairs": 2,
            },
        ]

        stats = _stats(records)

        self.assertEqual(stats["strata"], 2)
        self.assertEqual(stats["movement_selected_pairs"], 4)
        self.assertEqual(stats["movement_selected_retained"], 3)
        self.assertEqual(stats["not_selected_retained"], 2)


if __name__ == "__main__":
    unittest.main()
