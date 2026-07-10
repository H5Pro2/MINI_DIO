from __future__ import annotations

import unittest

from mini_dio.mcm_neighborhood_consolidation import pareto_depths


class MCMParetoDepthTest(unittest.TestCase):
    def test_non_dominated_layers_need_no_weights_or_thresholds(self) -> None:
        rows = [
            {
                "pair_key": "a",
                "world_pair_count": 3,
                "world_count": 3,
                "growth_seen_count": 3,
            },
            {
                "pair_key": "b",
                "world_pair_count": 2,
                "world_count": 2,
                "growth_seen_count": 2,
            },
            {
                "pair_key": "c",
                "world_pair_count": 3,
                "world_count": 1,
                "growth_seen_count": 4,
            },
        ]

        depths = pareto_depths(rows)

        self.assertEqual(depths, {"a": 1, "c": 1, "b": 2})

    def test_equal_relations_share_the_same_layer(self) -> None:
        rows = [
            {
                "pair_key": key,
                "world_pair_count": 4,
                "world_count": 3,
                "growth_seen_count": 2,
            }
            for key in ("a", "b")
        ]

        self.assertEqual(pareto_depths(rows), {"a": 1, "b": 1})


if __name__ == "__main__":
    unittest.main()
