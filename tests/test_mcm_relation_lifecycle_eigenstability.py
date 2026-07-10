from __future__ import annotations

import random
import unittest
from collections import Counter

from tools.run_mcm_relation_lifecycle_eigenstability import (
    _longest_consecutive_run,
    _permuted_edges,
    _transition_records,
)


class MCMRelationLifecycleEigenstabilityTest(unittest.TestCase):
    def test_transition_separates_labels_in_maximum_age_approximation(self) -> None:
        edges = {
            2: {("a", "b"), ("c", "d")},
            3: {("a", "b"), ("a", "c"), ("c", "d")},
            4: {("a", "b"), ("a", "c")},
        }
        records = _transition_records(edges, {symbol: 4 for symbol in "abcd"})

        self.assertEqual(len(records), 1)
        row = records[0]
        self.assertEqual(row["relation_age"], 3)
        self.assertEqual(row["carried_edges"], 2)
        self.assertEqual(row["carried_continued"], 1)
        self.assertEqual(row["new_edges"], 1)
        self.assertEqual(row["new_continued"], 1)

    def test_graph_permutation_preserves_edge_count_and_degree_multiset(self) -> None:
        edges = {("a", "b"), ("a", "c"), ("c", "d")}
        permuted = _permuted_edges(
            edges, ["a", "b", "c", "d"], random.Random(2091)
        )

        def degrees(graph: set[tuple[str, str]]) -> list[int]:
            counts = Counter(node for edge in graph for node in edge)
            return sorted(counts.values())

        self.assertEqual(len(permuted), len(edges))
        self.assertEqual(degrees(permuted), degrees(edges))

    def test_longest_consecutive_run_keeps_gaps_visible(self) -> None:
        self.assertEqual(_longest_consecutive_run({2, 3, 4, 7, 9, 10}), 3)
        self.assertEqual(_longest_consecutive_run({2, 4, 6}), 1)
        self.assertEqual(_longest_consecutive_run(set()), 0)


if __name__ == "__main__":
    unittest.main()
