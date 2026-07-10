from __future__ import annotations

import unittest

from tools.run_mcm_multiplex_holdout import (
    _best_component_match,
    _internal_edge_count,
    _largest_overlap_component,
    _world_specs,
)


class MCMMultiplexHoldoutTest(unittest.TestCase):
    def test_holdout_order_is_complete_unique_and_hash_sorted(self) -> None:
        specs = _world_specs()

        self.assertEqual(len(specs), 81)
        self.assertEqual([spec.position for spec in specs], list(range(1, 82)))
        self.assertEqual(
            [spec.order_digest for spec in specs],
            sorted(spec.order_digest for spec in specs),
        )
        self.assertEqual(
            len({(spec.source_archive, spec.member) for spec in specs}),
            81,
        )

    def test_component_match_is_selected_only_by_post_discovery_overlap(self) -> None:
        reference = {"a", "b", "c"}
        components = [{"a", "x"}, {"a", "b", "c", "d"}, {"y", "z"}]

        self.assertEqual(
            _best_component_match(reference, components),
            (3, 4, 0.75),
        )

    def test_internal_edges_do_not_count_links_leaving_reference_set(self) -> None:
        edges = {("a", "b"), ("a", "c"), ("b", "d")}

        self.assertEqual(_internal_edge_count(edges, {"a", "b", "d"}), 2)

    def test_largest_overlap_is_separate_from_best_jaccard(self) -> None:
        reference = {"a", "b", "c", "d"}
        components = [{"a", "b", *{f"x{i}" for i in range(18)}}, {"c", "y"}]

        self.assertEqual(
            _largest_overlap_component(reference, components),
            (2, 20, 2 / 22),
        )
        self.assertEqual(_best_component_match(reference, components), (1, 2, 0.2))


if __name__ == "__main__":
    unittest.main()
