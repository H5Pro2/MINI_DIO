from __future__ import annotations

import unittest

from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import ClosedRankEpisode
from tools.run_mcm_cross_cycle_partial_relations import (
    _partial_relation_profiles,
)


def _values(*slots: tuple[int, int]) -> tuple[int, ...]:
    values = [0] * FINGERPRINT_SIZE
    for index, strength in slots:
        values[index] = strength
    return tuple(values)


def _episode(values: tuple[int, ...], tick: int) -> ClosedRankEpisode:
    return ClosedRankEpisode(
        values=values,
        opened_tick=tick,
        closure_tick=tick + 1,
        repeated_from_tick=tick - 1,
        cycle_span=2,
        unique_rank_orders=2,
        transition_observations=sum(values),
    )


class MCMCrossCyclePartialRelationsTest(unittest.TestCase):
    def test_same_slot_in_consecutive_episodes_carries_once(self) -> None:
        profiles = _partial_relation_profiles(
            [_episode(_values((3, 1)), 1), _episode(_values((3, 9)), 3)]
        )

        self.assertEqual(profiles.carry_observations, 1)
        self.assertEqual(profiles.carry_values[3], 1)
        self.assertEqual(profiles.boundaries_with_carry, 1)

    def test_slot_return_after_gap_is_not_immediate_carry(self) -> None:
        profiles = _partial_relation_profiles(
            [
                _episode(_values((2, 1)), 1),
                _episode(_values((4, 1)), 3),
                _episode(_values((2, 1)), 5),
            ]
        )

        self.assertEqual(profiles.carry_values[2], 0)
        self.assertEqual(profiles.carry_observations, 0)

    def test_episode_strength_does_not_change_support_participation(self) -> None:
        profiles = _partial_relation_profiles(
            [_episode(_values((1, 1)), 1), _episode(_values((1, 7)), 3)]
        )

        self.assertEqual(profiles.participation_values[1], 2)
        self.assertEqual(profiles.carry_values[1], 1)


if __name__ == "__main__":
    unittest.main()
