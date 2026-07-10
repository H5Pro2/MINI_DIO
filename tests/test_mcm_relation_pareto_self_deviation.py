from __future__ import annotations

import random
import unittest

from mini_dio.mcm_neighborhood_consolidation import SUPPORT_AXES, pareto_depths
from tools.run_mcm_relation_pareto_self_deviation import (
    _phase_summary,
    _pareto_depths_fast,
    _permute_timing_within_event_count,
    _reorganization_rows,
    _support_trajectory_signature,
    _timing_age_signature,
)


def _event(finalization: int, values: tuple[int, int, int]) -> dict[str, int]:
    return {
        "finalization_index": finalization,
        **{axis: value for axis, value in zip(SUPPORT_AXES, values)},
    }


class MCMRelationParetoSelfDeviationTest(unittest.TestCase):
    def test_fast_pareto_depth_matches_existing_weightless_depth(self) -> None:
        state = {
            "a": (3, 3, 3),
            "b": (2, 2, 2),
            "c": (3, 1, 4),
            "d": (3, 3, 3),
            "e": (1, 4, 1),
        }
        rows = [
            {"pair_key": symbol, **dict(zip(SUPPORT_AXES, values))}
            for symbol, values in state.items()
        ]

        self.assertEqual(_pareto_depths_fast(state), pareto_depths(rows))

    def test_null_preserves_event_age_activity_and_support_trajectories(self) -> None:
        trajectories = {
            "a": [_event(1, (1, 2, 1)), _event(3, (2, 3, 2))],
            "b": [_event(2, (2, 2, 1)), _event(4, (3, 4, 2))],
            "c": [_event(3, (1, 2, 1))],
            "d": [_event(4, (4, 5, 1))],
        }

        permuted = _permute_timing_within_event_count(
            trajectories, random.Random(2102)
        )

        self.assertEqual(
            _timing_age_signature(permuted), _timing_age_signature(trajectories)
        )
        self.assertEqual(
            _support_trajectory_signature(permuted),
            _support_trajectory_signature(trajectories),
        )

    def test_reorganization_uses_only_current_and_prior_prefix(self) -> None:
        base = {
            "a": [_event(1, (1, 2, 1)), _event(2, (3, 3, 2))],
            "b": [_event(1, (2, 2, 1))],
        }
        with_future = {
            **base,
            "c": [_event(3, (9, 9, 1))],
        }

        base_rows = _reorganization_rows(base, 3)
        future_rows = _reorganization_rows(with_future, 3)

        self.assertEqual(base_rows[:2], future_rows[:2])
        self.assertEqual(base_rows[1]["depth_change_count"], 2)
        self.assertEqual(base_rows[1]["moved_shallower"], 1)
        self.assertEqual(base_rows[1]["moved_deeper"], 1)
        self.assertEqual(base_rows[1]["future_event_reads"], 0)

        summary = _phase_summary(base_rows, "all")
        self.assertEqual(summary["depth_change_share"], 0.5)
        self.assertEqual(summary["mean_world_depth_change_share"], 0.5)


if __name__ == "__main__":
    unittest.main()
