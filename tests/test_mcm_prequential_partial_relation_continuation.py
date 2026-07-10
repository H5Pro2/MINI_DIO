from __future__ import annotations

import unittest

from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import ClosedRankEpisode
from tools.run_mcm_prequential_partial_relation_continuation import (
    _binomial_lower_p,
    _binomial_upper_p,
    _matched_continuation,
)


def _values(*slots: int) -> tuple[int, ...]:
    values = [0] * FINGERPRINT_SIZE
    for slot in slots:
        values[slot] = 1
    return tuple(values)


def _episode(tick: int, *slots: int) -> ClosedRankEpisode:
    values = _values(*slots)
    return ClosedRankEpisode(
        values=values,
        opened_tick=tick,
        closure_tick=tick + 1,
        repeated_from_tick=tick - 1,
        cycle_span=2,
        unique_rank_orders=2,
        transition_observations=sum(values),
    )


class MCMPrequentialPartialRelationContinuationTest(unittest.TestCase):
    def test_same_pair_and_frequency_match_uses_only_past_for_groups(self) -> None:
        episodes = [
            _episode(1, 1),
            _episode(3, 0),
            _episode(5, 0, 1),
            _episode(7, 0),
        ]

        result = _matched_continuation(episodes, same_neuron_pair=True)

        self.assertEqual(result.pairs, 1)
        self.assertEqual(result.wins, 1)
        self.assertEqual(result.losses, 0)
        self.assertEqual(result.auc, 1.0)

    def test_strict_match_rejects_equal_frequency_from_other_pair(self) -> None:
        episodes = [
            _episode(1, 6),
            _episode(3, 0),
            _episode(5, 0, 6),
            _episode(7, 0),
        ]

        broad = _matched_continuation(episodes, same_neuron_pair=False)
        strict = _matched_continuation(episodes, same_neuron_pair=True)

        self.assertEqual(broad.pairs, 1)
        self.assertEqual(strict.pairs, 0)

    def test_future_changes_outcome_but_not_matched_opportunity(self) -> None:
        prefix = [_episode(1, 1), _episode(3, 0), _episode(5, 0, 1)]
        carried_continues = _matched_continuation(
            prefix + [_episode(7, 0)],
            same_neuron_pair=True,
        )
        neither_continues = _matched_continuation(
            prefix + [_episode(7)],
            same_neuron_pair=True,
        )

        self.assertEqual(carried_continues.pairs, neither_continues.pairs)
        self.assertEqual(carried_continues.matched_steps, neither_continues.matched_steps)
        self.assertNotEqual(carried_continues.auc, neither_continues.auc)

    def test_binomial_upper_tail_is_exact(self) -> None:
        self.assertEqual(_binomial_upper_p(3, 0), 0.125)
        self.assertEqual(_binomial_lower_p(0, 3), 0.125)
        self.assertEqual(_binomial_upper_p(0, 0), 1.0)
        self.assertEqual(_binomial_lower_p(0, 0), 1.0)


if __name__ == "__main__":
    unittest.main()
