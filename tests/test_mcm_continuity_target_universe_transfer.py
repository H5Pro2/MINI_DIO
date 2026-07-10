from __future__ import annotations

import unittest
from pathlib import Path

from tools.run_mcm_continuity_target_universe_transfer import (
    World,
    _comparison_groups,
    _universe_split,
)


def _world(index: int, asset: str = "asset") -> World:
    return World("test", asset, 2026, Path("source.csv"), index)


class MCMContinuityTargetUniverseTransferTest(unittest.TestCase):
    def test_universe_split_is_deterministic_disjoint_and_complete(self) -> None:
        worlds = [_world(index) for index in range(20)]
        first = _universe_split(worlds)
        second = _universe_split(list(reversed(worlds)))
        self.assertEqual(first, second)
        sources, universe_a, universe_b = first
        self.assertEqual(len(sources), 4)
        self.assertEqual(len(universe_a), 8)
        self.assertEqual(len(universe_b), 8)
        self.assertFalse(set(universe_a) & set(universe_b))
        self.assertFalse(set(sources) & (set(universe_a) | set(universe_b)))
        self.assertEqual(
            set(worlds), set(sources) | set(universe_a) | set(universe_b)
        )

    def test_within_asset_year_groups_keep_only_matching_sources(self) -> None:
        sources = [_world(1, "a"), _world(2, "a"), _world(3, "b")]
        groups = _comparison_groups(sources, "within_asset_year")
        self.assertEqual(sorted(len(group) for group in groups), [1, 2])

    def test_universe_split_requires_sources_outside_both_targets(self) -> None:
        with self.assertRaises(ValueError):
            _universe_split([_world(index) for index in range(16)])


if __name__ == "__main__":
    unittest.main()
