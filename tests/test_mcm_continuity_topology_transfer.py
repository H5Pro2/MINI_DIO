from __future__ import annotations

import unittest

from tools.run_mcm_continuity_topology_transfer import (
    _activation_order,
    _path_difference,
    _path_profile,
    _rank_pair_disagreements,
)


class MCMContinuityTopologyTransferTest(unittest.TestCase):
    def test_activation_order_preserves_exact_ties_without_threshold(self) -> None:
        self.assertEqual(
            _activation_order((0.2, 0.7, 0.2, -0.1)),
            ((1,), (0, 2), (3,)),
        )

    def test_rank_disagreement_counts_changed_pair_relations(self) -> None:
        self.assertEqual(
            _rank_pair_disagreements((0.3, 0.2, 0.1), (0.1, 0.2, 0.3)),
            3,
        )
        self.assertEqual(
            _rank_pair_disagreements((0.3, 0.2, 0.1), (0.3, 0.2, 0.1)),
            0,
        )

    def test_path_profile_compresses_only_consecutive_equal_states(self) -> None:
        profile = _path_profile(["a", "a", "b", "a", "a"])
        self.assertEqual(profile["episodes"], ("a", "b", "a"))
        self.assertEqual(profile["boundaries"], frozenset({3, 4}))
        self.assertEqual(profile["edge_counts"][("a", "b")], 1)
        self.assertEqual(profile["edge_counts"][("b", "a")], 1)

    def test_path_difference_keeps_equal_paths_exact(self) -> None:
        difference = _path_difference(["a", "a", "b"], ["a", "a", "b"])
        changed_values = [
            value
            for key, value in difference.items()
            if "left_" not in key and "right_" not in key
        ]
        self.assertTrue(all(value == 0 for value in changed_values))


if __name__ == "__main__":
    unittest.main()
