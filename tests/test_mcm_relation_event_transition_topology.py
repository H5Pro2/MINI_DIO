from __future__ import annotations

import random
import unittest
from collections import Counter

from tools.run_mcm_relation_event_transition_topology import (
    _activity_preserving_rewire,
    _collision_pairs,
    _gap_order_shuffle,
    _topology_counters,
)


class MCMRelationEventTransitionTopologyTest(unittest.TestCase):
    def test_consecutive_relation_events_form_edges_and_two_step_paths(self) -> None:
        edges, paths = _topology_counters(
            {"a": [1, 3, 5], "b": [1, 3, 6]}
        )

        self.assertEqual(edges[(1, 3)], 2)
        self.assertEqual(edges[(3, 5)], 1)
        self.assertEqual(paths[(1, 3, 5)], 1)
        self.assertEqual(paths[(1, 3, 6)], 1)

    def test_collision_count_has_no_support_threshold(self) -> None:
        counter = Counter({("a", "b"): 3, ("b", "c"): 1})

        self.assertEqual(_collision_pairs(counter), 3)

    def test_gap_shuffle_preserves_endpoints_and_gap_multiset(self) -> None:
        source = {"a": [2, 4, 7, 11]}

        shuffled = _gap_order_shuffle(source, random.Random(2097))["a"]

        self.assertEqual(shuffled[0], 2)
        self.assertEqual(shuffled[-1], 11)
        self.assertEqual(
            sorted(right - left for left, right in zip(shuffled, shuffled[1:])),
            [2, 3, 4],
        )

    def test_activity_rewire_preserves_relations_world_activity_and_bounds(self) -> None:
        source = {
            "a": [1, 2, 4, 6],
            "b": [1, 3, 5, 6],
            "c": [1, 2, 5, 6],
        }
        before_activity = Counter(
            finalization
            for sequence in source.values()
            for finalization in sequence
        )

        rewired, _, _ = _activity_preserving_rewire(
            source, random.Random(2098)
        )
        after_activity = Counter(
            finalization
            for sequence in rewired.values()
            for finalization in sequence
        )

        self.assertEqual(after_activity, before_activity)
        self.assertEqual(set(rewired), set(source))
        for symbol in source:
            self.assertEqual(len(rewired[symbol]), len(source[symbol]))
            self.assertEqual(rewired[symbol][0], source[symbol][0])
            self.assertEqual(rewired[symbol][-1], source[symbol][-1])
            self.assertEqual(len(rewired[symbol]), len(set(rewired[symbol])))


if __name__ == "__main__":
    unittest.main()
