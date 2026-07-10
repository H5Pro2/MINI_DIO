from __future__ import annotations

import random
import unittest
from collections import Counter

from tools.run_mcm_collective_gap_cadence_transfer import (
    _permuted_counts,
    _transfer_rows,
)


class MCMCollectiveGapCadenceTransferTest(unittest.TestCase):
    def test_label_permutation_preserves_frequency_multiset(self) -> None:
        source = Counter({1: 10, 2: 5, 3: 1})
        candidates = {1, 2, 3, 4}

        permuted = _permuted_counts(
            source, candidates, random.Random(2099)
        )

        self.assertEqual(
            sorted(permuted[value] for value in candidates),
            [0, 1, 5, 10],
        )

    def test_transfer_uses_no_future_target_gap(self) -> None:
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

        rows, future_reads = _transfer_rows(source, target, order)

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

    def test_target_universe_is_shared_by_frozen_and_online_scores(self) -> None:
        source = {"source": [1, 2, 4]}
        target = {"target": [1, 3]}
        order = [
            {
                "position": str(index),
                "world_label": f"W{index}",
                "asset": "TEST",
                "year": "2026",
            }
            for index in range(1, 5)
        ]

        rows, _ = _transfer_rows(source, target, order)

        self.assertEqual(len(rows), 1)
        self.assertIn("frozen_source_score", rows[0])
        self.assertIn("target_online_score", rows[0])


if __name__ == "__main__":
    unittest.main()
