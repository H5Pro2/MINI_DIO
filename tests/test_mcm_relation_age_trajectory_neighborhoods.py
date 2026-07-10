from __future__ import annotations

import unittest

from tools.run_mcm_relation_age_trajectory_neighborhoods import (
    _prefix_vector,
    _rank_vectors,
)
from tools.run_mcm_relation_age_edge_persistence import (
    _connected_components,
    _persistent_edges,
    _restricted_edges,
)


class MCMRelationAgeTrajectoryNeighborhoodTest(unittest.TestCase):
    def test_prefix_vector_uses_only_events_up_to_requested_age(self) -> None:
        history = [
            {
                "finalization_index": 2,
                "world_pair_count": 1,
                "world_count": 2,
                "field_core_raw": 3,
                "field_full_raw": 4,
                "field_full_plus_duration_standardized": 5,
            },
            {
                "finalization_index": 5,
                "world_pair_count": 4,
                "world_count": 3,
                "field_core_raw": 7,
                "field_full_raw": 9,
                "field_full_plus_duration_standardized": 11,
            },
            {
                "finalization_index": 9,
                "world_pair_count": 10,
                "world_count": 5,
                "field_core_raw": 13,
                "field_full_raw": 16,
                "field_full_plus_duration_standardized": 20,
            },
        ]

        self.assertEqual(_prefix_vector(history, 2), (3, 3, 1, 4, 5, 6))
        self.assertEqual(
            _prefix_vector(history, 3),
            (3, 3, 1, 4, 5, 6, 4, 6, 2, 6, 7, 9),
        )

    def test_rank_vectors_preserves_component_ties(self) -> None:
        vectors = {
            "a": (1, 10, 2, 20, 3, 30),
            "b": (1, 10, 4, 40, 5, 50),
            "c": (3, 30, 6, 60, 7, 70),
        }

        ranked = _rank_vectors(vectors, (0, 1))

        self.assertEqual(ranked["a"], ranked["b"])
        self.assertNotEqual(ranked["a"], ranked["c"])

    def test_edge_persistence_uses_only_relations_surviving_to_later_age(self) -> None:
        nodes = {"a", "b", "c"}
        age3 = {("a", "b"), ("b", "c"), ("c", "d")}
        age5 = {("a", "b"), ("a", "c"), ("c", "d")}
        age10 = {("a", "b"), ("b", "c")}

        self.assertEqual(
            _restricted_edges(age3, nodes),
            {("a", "b"), ("b", "c")},
        )
        self.assertEqual(
            _persistent_edges([age3, age5, age10], nodes),
            {("a", "b")},
        )

    def test_connected_components_keep_persistent_groups_separate(self) -> None:
        components = _connected_components(
            {("a", "b"), ("b", "c"), ("d", "e")}
        )

        self.assertEqual(components, [{"a", "b", "c"}, {"d", "e"}])


if __name__ == "__main__":
    unittest.main()
