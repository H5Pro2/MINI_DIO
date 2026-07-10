from __future__ import annotations

import unittest

from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import ClosedRankEpisode
from tools.run_mcm_episode_relational_salience import (
    _midrank_percentile,
    _splitmix_index,
    _stream_salience,
)


def _values(slot: int) -> tuple[int, ...]:
    values = [0] * FINGERPRINT_SIZE
    values[slot] = 1
    return tuple(values)


def _episode(slot: int, opened: int, closed: int) -> ClosedRankEpisode:
    return ClosedRankEpisode(
        values=_values(slot),
        opened_tick=opened,
        closure_tick=closed,
        repeated_from_tick=opened - 1,
        cycle_span=closed - opened + 1,
        unique_rank_orders=2,
        transition_observations=1,
    )


class MCMEpisodeRelationalSalienceTest(unittest.TestCase):
    def test_midrank_percentile_preserves_exact_ties(self) -> None:
        self.assertEqual(_midrank_percentile(2.0, [1.0, 2.0, 2.0, 3.0]), 0.5)

    def test_candidate_is_first_strict_episode_transition(self) -> None:
        episodes = [
            _episode(0, 1, 2),
            _episode(1, 3, 4),
            _episode(2, 5, 12),
            _episode(3, 13, 16),
            _episode(4, 17, 20),
        ]

        salience = _stream_salience(episodes, boundary_tick=10)

        self.assertEqual(salience.candidate_left_crosses_boundary, 1)
        self.assertEqual(salience.candidate_right_open_delay, 3)
        self.assertEqual(salience.candidate_right_closure_delay, 6)
        self.assertEqual(salience.all_transition_count, 4)

    def test_position_null_index_is_deterministic_and_bounded(self) -> None:
        indexes = [_splitmix_index(123, permutation, 17) for permutation in range(32)]
        self.assertEqual(
            indexes,
            [_splitmix_index(123, permutation, 17) for permutation in range(32)],
        )
        self.assertTrue(all(0 <= index < 17 for index in indexes))
        self.assertGreater(len(set(indexes)), 1)


if __name__ == "__main__":
    unittest.main()
