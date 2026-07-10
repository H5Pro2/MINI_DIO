from __future__ import annotations

import unittest
from pathlib import Path

from tools.run_mcm_continuity_source_identity import (
    World,
    _identity_observations,
    _shape_vector,
    _source_and_target_worlds,
    _transition_slot,
)


def _world(index: int) -> World:
    return World("test", "asset", 2026, Path("source.csv"), index)


class MCMContinuitySourceIdentityTest(unittest.TestCase):
    def test_world_split_is_deterministic_disjoint_and_complete(self) -> None:
        worlds = [_world(index) for index in range(12)]
        first = _source_and_target_worlds(worlds)
        second = _source_and_target_worlds(list(reversed(worlds)))
        self.assertEqual(first, second)
        sources, cohort_a, cohort_b = first
        self.assertEqual(len(sources), 4)
        self.assertEqual(len(cohort_a), 4)
        self.assertEqual(len(cohort_b), 4)
        self.assertEqual(
            {world.key for world in worlds},
            {world.key for world in sources + list(cohort_a) + list(cohort_b)},
        )

    def test_transition_slots_keep_pair_and_direction_separate(self) -> None:
        self.assertNotEqual(_transition_slot(0, -1, 1), _transition_slot(0, 1, -1))
        self.assertNotEqual(_transition_slot(0, -1, 1), _transition_slot(1, -1, 1))
        with self.assertRaises(ValueError):
            _transition_slot(0, 1, 1)

    def test_shape_vector_removes_total_strength_only(self) -> None:
        self.assertEqual(_shape_vector((1, 3)), (0.25, 0.75))
        self.assertEqual(_shape_vector((2, 6)), (0.25, 0.75))
        self.assertEqual(_shape_vector((0, 0)), (0.0, 0.0))

    def test_identity_ranking_preserves_nearest_ties(self) -> None:
        left = {"a": (0.0,), "b": (2.0,)}
        right = {"a": (1.0,), "b": (1.0,)}
        observations, _, _ = _identity_observations(left, right)
        self.assertTrue(all(row["identity_in_nearest_tie"] == 1 for row in observations))
        self.assertTrue(all(row["identity_unique_nearest"] == 0 for row in observations))


if __name__ == "__main__":
    unittest.main()
