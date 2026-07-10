from __future__ import annotations

import unittest

from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import ClosedRankEpisode
from tools.run_mcm_multi_episode_exact_recurrence import (
    _canonical_episode_form,
    _stream_form_profiles,
)


def _values(first: int, second: int = 0) -> tuple[int, ...]:
    values = [0] * FINGERPRINT_SIZE
    values[0] = first
    values[1] = second
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


class MCMMultiEpisodeExactRecurrenceTest(unittest.TestCase):
    def test_canonical_form_removes_only_common_integer_strength(self) -> None:
        self.assertEqual(
            _canonical_episode_form(_values(2, 4)),
            _canonical_episode_form(_values(1, 2)),
        )

    def test_only_observations_after_first_exact_form_recur(self) -> None:
        form_a = _values(1, 2)
        form_b = _values(0, 1)
        profiles = _stream_form_profiles(
            [
                _episode(form_a, 1),
                _episode(form_a, 3),
                _episode(form_b, 5),
                _episode(form_a, 7),
            ]
        )

        self.assertEqual(profiles.recurrent_form_classes, 1)
        self.assertEqual(profiles.recurrence_observations, 2)
        self.assertEqual(profiles.recurrence_values[0], 2)
        self.assertEqual(profiles.recurrence_values[1], 4)

    def test_unique_forms_create_no_recurrence_profile(self) -> None:
        profiles = _stream_form_profiles(
            [_episode(_values(1, 0), 1), _episode(_values(0, 1), 3)]
        )

        self.assertEqual(profiles.recurrence_observations, 0)
        self.assertEqual(sum(profiles.recurrence_values), 0)


if __name__ == "__main__":
    unittest.main()
