from __future__ import annotations

import random
import unittest
from collections import Counter

from tools.run_mcm_collective_renewal_configuration_topology import (
    _collision_pairs,
    _configuration_counter,
    _degree_preserving_rewire,
    _renewal_configurations,
)
from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import ClosedRankEpisode


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


class MCMCollectiveRenewalConfigurationTopologyTest(unittest.TestCase):
    def test_simultaneous_pair_replacements_form_one_configuration(self) -> None:
        episodes = [
            _episode(1, 1, 7),
            _episode(3, 0, 6),
            _episode(5, 0, 1, 6, 7),
            _episode(7, 1, 7),
        ]

        self.assertEqual(_renewal_configurations(episodes), ((0, 1),))

    def test_other_pair_or_unequal_frequency_is_not_forced_into_config(self) -> None:
        episodes = [
            _episode(1, 6),
            _episode(3, 0),
            _episode(5, 0, 6),
            _episode(7, 6),
        ]

        self.assertEqual(_renewal_configurations(episodes), ())

    def test_degree_swap_preserves_widths_and_pair_frequencies(self) -> None:
        path = ((0, 1), (0, 2), (1, 3), (2, 3))
        before_frequency = Counter(pair for row in path for pair in row)

        rewired, accepted, _ = _degree_preserving_rewire(
            path, random.Random(2120)
        )
        after_frequency = Counter(pair for row in rewired for pair in row)

        self.assertGreater(accepted, 0)
        self.assertEqual([len(row) for row in rewired], [2, 2, 2, 2])
        self.assertEqual(after_frequency, before_frequency)

    def test_singleton_path_has_no_artificial_swap(self) -> None:
        path = ((0,),)

        rewired, accepted, _ = _degree_preserving_rewire(
            path, random.Random(2120)
        )

        self.assertEqual(rewired, path)
        self.assertEqual(accepted, 0)

    def test_collision_count_uses_every_repeat_without_threshold(self) -> None:
        self.assertEqual(_collision_pairs(Counter({(0, 1): 3, (1, 2): 1})), 3)

    def test_collective_counter_excludes_single_pair_moments(self) -> None:
        paths = [((0,), (0, 1), (0, 1))]

        self.assertEqual(_configuration_counter(paths), Counter({(0, 1): 2}))


if __name__ == "__main__":
    unittest.main()
