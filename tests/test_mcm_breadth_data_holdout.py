from __future__ import annotations

import unittest

from tools.run_mcm_breadth_data_holdout import ROWS, SOURCES, STARTS, _world_specs


class MCMBreadthDataHoldoutTest(unittest.TestCase):
    def test_worlds_are_complete_unique_and_hash_sorted(self) -> None:
        specs = _world_specs()

        self.assertEqual(len(specs), 64)
        self.assertEqual([spec.position for spec in specs], list(range(1, 65)))
        self.assertEqual(
            [spec.order_digest for spec in specs],
            sorted(spec.order_digest for spec in specs),
        )
        self.assertEqual(
            len({(spec.source, spec.start) for spec in specs}),
            len(specs),
        )

    def test_windows_are_non_overlapping_and_fit_every_source(self) -> None:
        self.assertEqual(STARTS, tuple(range(0, 16000, ROWS)))
        for _, _, source in SOURCES:
            self.assertTrue(source.exists())
        for left, right in zip(STARTS, STARTS[1:]):
            self.assertEqual(left + ROWS, right)

    def test_sources_are_real_30m_data_outside_prior_holdout_timeframes(self) -> None:
        self.assertEqual({asset for asset, _, _ in SOURCES}, {"BTC", "SOL"})
        self.assertEqual({year for _, year, _ in SOURCES}, {2024, 2025})
        self.assertTrue(all("30m" in source.name for _, _, source in SOURCES))
        self.assertTrue(all("synthetic" not in source.name for _, _, source in SOURCES))


if __name__ == "__main__":
    unittest.main()
