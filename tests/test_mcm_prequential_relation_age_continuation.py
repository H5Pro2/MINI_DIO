from __future__ import annotations

import unittest

from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import ClosedRankEpisode
from tools.run_mcm_prequential_relation_age_continuation import (
    _matched_age_continuation,
)


def _episode(tick: int, *slots: int) -> ClosedRankEpisode:
    values = [0] * FINGERPRINT_SIZE
    for slot in slots:
        values[slot] = 1
    return ClosedRankEpisode(
        values=tuple(values),
        opened_tick=tick,
        closure_tick=tick + 1,
        repeated_from_tick=tick - 1,
        cycle_span=2,
        unique_rank_orders=2,
        transition_observations=len(slots),
    )


class MCMPrequentialRelationAgeContinuationTest(unittest.TestCase):
    def test_older_slot_is_compared_at_equal_pair_and_frequency(self) -> None:
        episodes = [
            _episode(1, 1),
            _episode(3, 0),
            _episode(5, 0, 1),
            _episode(7, 0, 1),
            _episode(9, 1),
        ]

        result = _matched_age_continuation(episodes)

        self.assertEqual(result.pairs, 2)
        self.assertEqual(result.losses, 1)
        self.assertEqual(result.ties, 1)
        self.assertEqual(result.outcomes[-1].younger_age, 2)
        self.assertEqual(result.outcomes[-1].older_age, 3)

    def test_equal_ages_are_not_forced_into_an_order(self) -> None:
        episodes = [
            _episode(1, 0, 1),
            _episode(3, 0, 1),
            _episode(5, 0, 1),
        ]

        self.assertEqual(_matched_age_continuation(episodes).pairs, 0)

    def test_other_neuron_pair_is_not_a_match(self) -> None:
        episodes = [
            _episode(1, 6),
            _episode(3, 0),
            _episode(5, 0, 6),
            _episode(7, 0, 6),
            _episode(9, 6),
        ]

        self.assertEqual(_matched_age_continuation(episodes).pairs, 0)

    def test_future_changes_outcome_not_age_matching(self) -> None:
        prefix = [
            _episode(1, 1),
            _episode(3, 0),
            _episode(5, 0, 1),
            _episode(7, 0, 1),
        ]
        older_ends = _matched_age_continuation(prefix + [_episode(9, 1)])
        younger_ends = _matched_age_continuation(prefix + [_episode(9, 0)])

        self.assertEqual(older_ends.pairs, younger_ends.pairs)
        self.assertEqual(older_ends.matched_steps, younger_ends.matched_steps)
        self.assertNotEqual(older_ends.auc, younger_ends.auc)

    def test_carried_only_view_uses_exact_ages_without_bins(self) -> None:
        episodes = [
            _episode(1, 1),
            _episode(3, 0),
            _episode(5, 0, 1),
            _episode(7, 0, 1),
            _episode(9, 1),
        ]

        result = _matched_age_continuation(episodes)

        self.assertEqual(result.where(minimum_younger_age=2).pairs, 1)
        self.assertEqual(result.where(minimum_younger_age=3).pairs, 0)


if __name__ == "__main__":
    unittest.main()
