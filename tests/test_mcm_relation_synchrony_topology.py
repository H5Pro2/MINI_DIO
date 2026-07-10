from __future__ import annotations

import random
import unittest

from tools.run_mcm_relation_synchrony_topology import (
    _overlap_edges,
    _shuffled_gaps,
    _synchrony_graphs,
)


class MCMRelationSynchronyTopologyTest(unittest.TestCase):
    def test_touching_interval_boundaries_are_not_simultaneous(self) -> None:
        intervals = [
            ("a", 2, 5),
            ("b", 4, 7),
            ("c", 5, 8),
        ]

        self.assertEqual(_overlap_edges(intervals), {("a", "b"), ("b", "c")})

    def test_gap_shuffle_preserves_birth_end_and_gap_multiset(self) -> None:
        source = {"relation": [3, 5, 9, 10]}

        shuffled = _shuffled_gaps(source, random.Random(2094))["relation"]

        self.assertEqual(shuffled[0], source["relation"][0])
        self.assertEqual(shuffled[-1], source["relation"][-1])
        self.assertEqual(
            sorted(right - left for left, right in zip(shuffled, shuffled[1:])),
            [1, 2, 4],
        )

    def test_synchrony_graph_uses_equal_relation_age(self) -> None:
        finalizations = {
            "a": [1, 3, 6],
            "b": [2, 4, 7],
            "c": [1, 6, 8],
        }

        nodes, edges = _synchrony_graphs(finalizations, worlds=8)

        self.assertEqual(nodes[2], {"a", "b", "c"})
        self.assertEqual(edges[2], {("a", "b"), ("b", "c")})
        self.assertEqual(edges[3], {("a", "b"), ("a", "c"), ("b", "c")})


if __name__ == "__main__":
    unittest.main()
