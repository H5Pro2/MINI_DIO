from __future__ import annotations

import unittest

from tools.run_mcm_continuous_field_instance import NEURON_COUNT
from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import (
    ClosedRankEpisode,
    RankCycleSegmenter,
    _strict_postboundary_episodes,
)


def _ascending() -> tuple[float, ...]:
    return tuple(float(index) for index in range(NEURON_COUNT))


class MCMContinuousRankSelfSegmentationTest(unittest.TestCase):
    def test_segmenter_reopens_after_closure_without_reset(self) -> None:
        ascending = _ascending()
        descending = tuple(reversed(ascending))
        segmenter = RankCycleSegmenter(ascending)

        self.assertIsNone(segmenter.observe(descending, 1))
        first = segmenter.observe(ascending, 2)
        self.assertIsNotNone(first)
        self.assertEqual(first.opened_tick, 1)
        self.assertEqual(first.closure_tick, 2)

        self.assertIsNone(segmenter.observe(descending, 3))
        second = segmenter.observe(ascending, 4)
        self.assertIsNotNone(second)
        self.assertEqual(second.opened_tick, 3)
        self.assertEqual(second.closure_tick, 4)

    def test_open_episode_survives_an_unreported_boundary(self) -> None:
        ascending = _ascending()
        descending = tuple(reversed(ascending))
        rotated = ascending[1:] + ascending[:1]
        segmenter = RankCycleSegmenter(ascending)

        self.assertIsNone(segmenter.observe(descending, 1))
        self.assertIsNone(segmenter.observe(rotated, 2))
        episode = segmenter.observe(ascending, 3)

        self.assertIsNotNone(episode)
        self.assertEqual(episode.opened_tick, 1)
        self.assertEqual(episode.closure_tick, 3)
        self.assertGreater(episode.transition_observations, 0)

    def test_strict_profiles_exclude_boundary_crossing_episode(self) -> None:
        values = (0,) * FINGERPRINT_SIZE
        crossing = ClosedRankEpisode(values, 9, 12, 8, 4, 3, 1)
        strict = ClosedRankEpisode(values, 13, 15, 12, 3, 2, 1)

        selected = _strict_postboundary_episodes([crossing, strict], 10)

        self.assertEqual(selected, [strict])


if __name__ == "__main__":
    unittest.main()
