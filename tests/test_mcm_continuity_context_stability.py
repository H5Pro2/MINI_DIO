from __future__ import annotations

import unittest
from pathlib import Path

from tools.run_mcm_continuity_context_stability import (
    World,
    _balanced_partitions,
    _candidate_score_block,
)


def _world(index: int) -> World:
    return World("test", "asset", 2026, Path("source.csv"), index)


class MCMContinuityContextStabilityTest(unittest.TestCase):
    def test_all_balanced_complementary_partitions_are_kept_once(self) -> None:
        targets = tuple(_world(index) for index in range(8))
        partitions = _balanced_partitions(targets)
        self.assertEqual(len(partitions), 35)
        seen = set()
        for left, right in partitions:
            self.assertEqual(len(left), 4)
            self.assertEqual(len(right), 4)
            self.assertFalse(set(left) & set(right))
            self.assertEqual(set(left) | set(right), set(targets))
            signature = frozenset(
                (frozenset(world.key for world in left), frozenset(world.key for world in right))
            )
            self.assertNotIn(signature, seen)
            seen.add(signature)

    def test_candidate_scores_preserve_ties_without_forced_identity(self) -> None:
        block = _candidate_score_block(
            "group",
            [[1.0, 1.0], [2.0, 2.0]],
            ["a", "b"],
        )
        self.assertEqual(block.auc_scores, ((0.5, 0.5), (0.5, 0.5)))
        self.assertEqual(block.unique_scores, ((0, 0), (0, 0)))
        self.assertEqual(block.nearest_tie_scores, ((1, 1), (1, 1)))

    def test_partition_requires_exactly_eight_targets(self) -> None:
        with self.assertRaises(ValueError):
            _balanced_partitions(tuple(_world(index) for index in range(7)))


if __name__ == "__main__":
    unittest.main()
