from __future__ import annotations

import unittest

from mini_dio.mcm_neighborhood_consolidation import SUPPORT_AXES
from tools.run_mcm_relation_pareto_indirect_redistribution import (
    _redistribution_rows,
)


def _event(finalization: int, values: tuple[int, int, int]) -> dict[str, int]:
    return {
        "finalization_index": finalization,
        **{axis: value for axis, value in zip(SUPPORT_AXES, values)},
    }


class MCMRelationParetoIndirectRedistributionTest(unittest.TestCase):
    def test_direct_and_indirect_layer_moves_are_kept_separate(self) -> None:
        trajectories = {
            "a": [_event(1, (1, 2, 1)), _event(2, (3, 3, 2))],
            "b": [_event(1, (2, 2, 1))],
        }

        row = _redistribution_rows(trajectories, 2)[1]

        self.assertEqual(row["direct_relations"], 1)
        self.assertEqual(row["direct_depth_changes"], 1)
        self.assertEqual(row["direct_moved_shallower"], 1)
        self.assertEqual(row["indirect_relations"], 1)
        self.assertEqual(row["indirect_depth_changes"], 1)
        self.assertEqual(row["indirect_moved_deeper"], 1)

    def test_future_relation_does_not_change_earlier_redistribution(self) -> None:
        base = {
            "a": [_event(1, (1, 2, 1)), _event(2, (3, 3, 2))],
            "b": [_event(1, (2, 2, 1))],
        }
        with_future = {**base, "c": [_event(3, (9, 9, 1))]}

        self.assertEqual(
            _redistribution_rows(base, 3)[:2],
            _redistribution_rows(with_future, 3)[:2],
        )


if __name__ == "__main__":
    unittest.main()
