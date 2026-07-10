from __future__ import annotations

import random
import unittest
from collections import Counter

from tools.run_mcm_continuity_source_identity import FINGERPRINT_SIZE
from tools.run_mcm_continuous_rank_self_segmentation import ClosedRankEpisode
from tools.run_mcm_prequential_renewal_replacement_topology import (
    ReplacementOpportunity,
    _collision_pairs,
    _cross_universe_matches,
    _observed_edges,
    _replacement_opportunities,
    _resampled_edges,
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


class MCMPrequentialRenewalReplacementTopologyTest(unittest.TestCase):
    def test_replacement_edge_uses_equal_frequency_and_same_pair(self) -> None:
        episodes = [
            _episode(1, 1),
            _episode(3, 0),
            _episode(5, 0, 1),
            _episode(7, 1),
        ]

        opportunities = _replacement_opportunities(episodes)

        self.assertEqual(len(opportunities), 1)
        self.assertEqual(_observed_edges(opportunities), Counter({(0, 1): 1}))
        self.assertEqual(opportunities[0].historical_frequency, 2)

    def test_future_changes_outcome_not_candidate_opportunity(self) -> None:
        prefix = [_episode(1, 1), _episode(3, 0), _episode(5, 0, 1)]
        replacement = _replacement_opportunities(prefix + [_episode(7, 1)])
        reverse = _replacement_opportunities(prefix + [_episode(7, 0)])

        self.assertEqual(replacement[0].carried_candidates, (0,))
        self.assertEqual(reverse[0].carried_candidates, (0,))
        self.assertEqual(replacement[0].new_candidates, (1,))
        self.assertEqual(reverse[0].new_candidates, (1,))
        self.assertNotEqual(_observed_edges(replacement), _observed_edges(reverse))

    def test_other_neuron_pair_creates_no_replacement_opportunity(self) -> None:
        episodes = [
            _episode(1, 6),
            _episode(3, 0),
            _episode(5, 0, 6),
            _episode(7, 6),
        ]

        self.assertEqual(_replacement_opportunities(episodes), ())

    def test_null_preserves_opportunity_and_edge_instance_count(self) -> None:
        opportunity = ReplacementOpportunity(
            neuron_pair=0,
            historical_frequency=3,
            carried_candidates=(0, 1, 2),
            new_candidates=(3, 4, 5),
            ending_carried=(0, 1),
            continuing_new=(3, 4),
        )

        edges = _resampled_edges([opportunity], random.Random(2119))

        self.assertEqual(sum(edges.values()), opportunity.edge_instances)
        self.assertTrue(all(left in (0, 1, 2) for left, _ in edges))
        self.assertTrue(all(right in (3, 4, 5) for _, right in edges))

    def test_forced_opportunity_is_not_changed_by_null(self) -> None:
        opportunity = ReplacementOpportunity(
            neuron_pair=0,
            historical_frequency=2,
            carried_candidates=(0,),
            new_candidates=(1,),
            ending_carried=(0,),
            continuing_new=(1,),
        )

        edges = _resampled_edges([opportunity], random.Random(2119))

        self.assertEqual(edges, Counter({(0, 1): 1}))

    def test_collision_and_cross_match_use_all_support_without_threshold(self) -> None:
        left = Counter({(0, 1): 3, (0, 2): 1})
        right = Counter({(0, 1): 2, (0, 3): 4})

        self.assertEqual(_collision_pairs(left), 3)
        self.assertEqual(_cross_universe_matches(left, right), 6)


if __name__ == "__main__":
    unittest.main()
