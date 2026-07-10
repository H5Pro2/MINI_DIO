from __future__ import annotations

import unittest
from collections import Counter

from tools.run_mcm_relation_gap_prequential_expectation import (
    _percentile_score,
    _prequential_rows,
)


class MCMRelationGapPrequentialExpectationTest(unittest.TestCase):
    def test_percentile_score_preserves_ties_without_smoothing(self) -> None:
        counts = Counter({1: 4, 2: 2, 3: 2, 4: 0})

        self.assertEqual(_percentile_score(counts, 1, {1, 2, 3, 4}), 1.0)
        self.assertEqual(_percentile_score(counts, 4, {1, 2, 3, 4}), 0.0)
        self.assertEqual(_percentile_score(counts, 2, {1, 2, 3, 4}), 0.5)

    def test_unknown_conditional_history_is_an_unweighted_tie(self) -> None:
        score = _percentile_score(Counter(), 3, {1, 2, 3})

        self.assertEqual(score, 0.5)

    def test_prequential_training_never_reads_target_future(self) -> None:
        rows, future_reads = _prequential_rows(
            {
                "a": [1, 2, 4, 7],
                "b": [1, 3, 5, 8],
            }
        )

        self.assertEqual(future_reads, 0)
        self.assertEqual(len(rows), 4)
        self.assertTrue(
            all(
                int(row["maximum_training_finalization"])
                == int(row["prediction_origin"])
                < int(row["target_event_finalization"])
                for row in rows
            )
        )


if __name__ == "__main__":
    unittest.main()
