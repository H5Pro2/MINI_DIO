from __future__ import annotations

import unittest

from tools.run_mcm_relation_lifecycle_independent_holdout import (
    ROWS,
    SOURCES,
    STARTS,
    _edge_sets_from_rows,
    _world_specs,
)


class MCMRelationLifecycleIndependentHoldoutTest(unittest.TestCase):
    def test_worlds_are_complete_unique_and_hash_sorted(self) -> None:
        specs = _world_specs()

        self.assertEqual(len(specs), 60)
        self.assertEqual([spec.position for spec in specs], list(range(1, 61)))
        self.assertEqual(
            [spec.order_digest for spec in specs],
            sorted(spec.order_digest for spec in specs),
        )
        self.assertEqual(
            len({(spec.source, spec.start) for spec in specs}), len(specs)
        )

    def test_sources_are_independent_real_five_minute_worlds(self) -> None:
        self.assertEqual({asset for asset, _, _ in SOURCES}, {"DOGE", "PAXG", "XRP"})
        self.assertEqual({year for _, year, _ in SOURCES}, {2024, 2025})
        self.assertTrue(all("5m" in source.name for _, _, source in SOURCES))
        self.assertTrue(all("synthetic" not in source.name for _, _, source in SOURCES))
        self.assertTrue(all(source.exists() for _, _, source in SOURCES))
        self.assertEqual(STARTS, tuple(range(0, 10000, ROWS)))

    def test_lifecycle_rows_form_age_specific_edge_sets(self) -> None:
        rows = [
            {"left_relation": "b", "right_relation": "a", "relation_age": 2},
            {"left_relation": "a", "right_relation": "b", "relation_age": 2},
            {"left_relation": "a", "right_relation": "c", "relation_age": 3},
        ]

        self.assertEqual(
            _edge_sets_from_rows(rows),
            {2: {("a", "b")}, 3: {("a", "c")}},
        )


if __name__ == "__main__":
    unittest.main()
