from __future__ import annotations

import unittest
from collections import Counter

from tools.run_mcm_collective_gap_cumulative_experience import (
    _combined_counts,
    _cumulative_rows,
    _one_sided_sign_p,
)


class MCMCollectiveGapCumulativeExperienceTest(unittest.TestCase):
    def test_combined_counts_add_every_observation_without_weight(self) -> None:
        source = Counter({1: 4, 2: 2})
        target = Counter({1: 1, 3: 3})

        combined = _combined_counts(source, target)

        self.assertEqual(combined, Counter({1: 5, 3: 3, 2: 2}))
        self.assertEqual(source, Counter({1: 4, 2: 2}))

    def test_sign_test_uses_only_nontied_comparisons(self) -> None:
        self.assertAlmostEqual(_one_sided_sign_p(3, 1), 5 / 16)
        self.assertEqual(_one_sided_sign_p(0, 0), 1.0)

    def test_cumulative_transfer_uses_no_future_target_gap(self) -> None:
        source = {"source": [1, 2, 4, 7]}
        target = {"target": [1, 3, 6]}
        order = [
            {
                "position": str(index),
                "world_label": f"W{index}",
                "asset": "TEST",
                "year": "2026",
            }
            for index in range(1, 7)
        ]

        rows, future_reads = _cumulative_rows(source, target, order)

        self.assertEqual(future_reads, 0)
        self.assertEqual(len(rows), 2)
        self.assertTrue(
            all(
                int(row["maximum_target_training_finalization"])
                == int(row["prediction_origin"])
                < int(row["target_event_finalization"])
                for row in rows
            )
        )


if __name__ == "__main__":
    unittest.main()
