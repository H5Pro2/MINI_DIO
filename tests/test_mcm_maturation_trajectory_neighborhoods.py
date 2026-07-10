from __future__ import annotations

import unittest

from tools.run_mcm_maturation_trajectory_neighborhoods import (
    _mutual_nearest_edges,
    _rank_maturity,
    _raw_fingerprint,
)


class MCMMaturationTrajectoryNeighborhoodTest(unittest.TestCase):
    def test_rank_maturity_preserves_ties_without_threshold(self) -> None:
        self.assertEqual(
            _rank_maturity([3.0, 1.0, 3.0], higher_is_stronger=True),
            [0.75, 0.0, 0.75],
        )
        self.assertEqual(
            _rank_maturity([1.0, 3.0, 1.0], higher_is_stronger=False),
            [0.75, 0.0, 0.75],
        )

    def test_only_mutual_nearest_trajectories_form_an_edge(self) -> None:
        edges, zero_edges = _mutual_nearest_edges(
            {(10, 20): {"a": [0.0], "b": [1.0], "c": [10.0]}}
        )

        self.assertEqual(edges, {("a", "b")})
        self.assertEqual(zero_edges, set())

    def test_exact_ties_remain_visible_instead_of_being_broken(self) -> None:
        edges, zero_edges = _mutual_nearest_edges(
            {(10, 20): {"a": [0.0], "b": [0.0], "c": [0.0]}}
        )

        expected = {("a", "b"), ("a", "c"), ("b", "c")}
        self.assertEqual(edges, expected)
        self.assertEqual(zero_edges, expected)

    def test_raw_fingerprint_contains_only_observed_integer_changes(self) -> None:
        history = [
            {
                "pareto_depth": "5",
                "world_pair_count": "3",
                "world_count": "2",
                "growth_seen_count": "1",
            },
            {
                "pareto_depth": "3",
                "world_pair_count": "8",
                "world_count": "4",
                "growth_seen_count": "3",
            },
        ]

        self.assertEqual(_raw_fingerprint(history), (-2, 5, 2, 2))


if __name__ == "__main__":
    unittest.main()
