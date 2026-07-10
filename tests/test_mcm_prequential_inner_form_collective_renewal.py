from __future__ import annotations

import random
import unittest
from collections import Counter

from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import ClosedRankEpisode
from tools.run_mcm_multi_episode_exact_recurrence import _canonical_episode_form
from tools.run_mcm_prequential_inner_form_collective_renewal import (
    _collision_pairs,
    _context_configuration_counter,
    _contextual_renewal_observations,
    _shuffle_configurations_within_width,
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


class MCMPrequentialInnerFormCollectiveRenewalTest(unittest.TestCase):
    def test_closed_current_form_precedes_collective_renewal_outcome(self) -> None:
        current = _episode(5, 0, 1, 6, 7)
        episodes = [
            _episode(1, 1, 7),
            _episode(3, 0, 6),
            current,
            _episode(7, 1, 7),
        ]

        observations = _contextual_renewal_observations(episodes)

        self.assertEqual(observations, ((_canonical_episode_form(current.values), (0, 1)),))

    def test_future_changes_outcome_not_preceding_context(self) -> None:
        prefix = [
            _episode(1, 1, 7),
            _episode(3, 0, 6),
            _episode(5, 0, 1, 6, 7),
        ]
        pair_zero = _contextual_renewal_observations(
            prefix + [_episode(7, 1, 6)]
        )
        pair_one = _contextual_renewal_observations(
            prefix + [_episode(7, 0, 7)]
        )

        self.assertEqual(pair_zero[0][0], pair_one[0][0])
        self.assertEqual(pair_zero[0][1], (0,))
        self.assertEqual(pair_one[0][1], (1,))

    def test_shuffle_preserves_context_width_and_configuration_multiset(self) -> None:
        context_a = (1, 0)
        context_b = (0, 1)
        path = (
            (context_a, (0, 1)),
            (context_b, (2, 3)),
            (context_a, (4,)),
            (context_b, (5,)),
        )

        shuffled = _shuffle_configurations_within_width(
            path, random.Random(2121)
        )

        self.assertEqual([item[0] for item in shuffled], [item[0] for item in path])
        self.assertEqual(
            [len(item[1]) for item in shuffled],
            [len(item[1]) for item in path],
        )
        self.assertEqual(
            Counter(item[1] for item in shuffled),
            Counter(item[1] for item in path),
        )

    def test_context_counter_excludes_single_pair_outcomes(self) -> None:
        context = (1, 0)
        paths = [((context, (0,)), (context, (0, 1)), (context, (0, 1)))]

        self.assertEqual(
            _context_configuration_counter(paths),
            Counter({(context, (0, 1)): 2}),
        )

    def test_collision_uses_every_repeat_without_threshold(self) -> None:
        self.assertEqual(_collision_pairs(Counter({"a": 3, "b": 1})), 3)


if __name__ == "__main__":
    unittest.main()
