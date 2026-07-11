from __future__ import annotations

import unittest
from dataclasses import dataclass

from tools.run_mcm_passive_triad_relational_mobility import (
    _medoid_centers,
    _mutual_nearest_pairs,
    _shift_sequences,
    _source_triads,
    _trace_metrics,
)


@dataclass(frozen=True)
class _Source:
    key: str


class MCMPassiveTriadRelationalMobilityTest(unittest.TestCase):
    def test_equal_distances_preserve_multiple_relations(self) -> None:
        self.assertEqual(
            _mutual_nearest_pairs((2, 2, 2)),
            ((0, 1), (0, 2), (1, 2)),
        )
        self.assertEqual(_medoid_centers((2, 2, 2)), (0, 1, 2))

    def test_nearest_pair_and_center_are_not_fixed(self) -> None:
        self.assertEqual(_mutual_nearest_pairs((-5, 1, 2)), ((1, 2),))
        self.assertEqual(_medoid_centers((-5, 1, 2)), (1,))
        self.assertEqual(_mutual_nearest_pairs((4, -3, 5)), ((0, 2),))
        self.assertEqual(_medoid_centers((4, -3, 5)), (0,))

    def test_hash_triads_cover_sources_without_duplicate_members(self) -> None:
        sources = [_Source(f"source_{index}") for index in range(5)]
        triads = _source_triads(sources)
        self.assertEqual(len(triads), 2)
        self.assertTrue(set(sources).issubset({source for triad in triads for source in triad}))
        self.assertTrue(all(len(set(triad)) == 3 for triad in triads))

    def test_independent_shift_preserves_each_event_sequence(self) -> None:
        sequences = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        shifted = _shift_sequences(sequences, (1, 2, 0))
        self.assertEqual(shifted, ((2, 3, 1), (6, 4, 5), (7, 8, 9)))
        self.assertEqual(
            [sorted(sequence) for sequence in shifted],
            [sorted(sequence) for sequence in sequences],
        )

    def test_strict_view_excludes_every_delta_tie(self) -> None:
        metrics = _trace_metrics(((0, 0, 3), (0, 1, 1), (2, 2, 3)))
        self.assertEqual(metrics["strict_distinct_ticks"], 1)
        self.assertEqual(sum(metrics["strict_edge_support"]), 1)
        self.assertEqual(sum(metrics["strict_center_support"]), 1)
        self.assertEqual(metrics["strict_edge_collision_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
