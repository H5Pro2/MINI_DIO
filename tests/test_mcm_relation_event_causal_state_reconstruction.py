from __future__ import annotations

import unittest

from mini_dio.mcm_neighborhood_event_memory import EVENT_FIELDS
from tools.run_mcm_relation_event_causal_state_reconstruction import (
    _causal_reconstruction,
)


def _event(symbol: str, index: int, finalization: int) -> dict[str, str]:
    values = {
        "finalization_index": finalization,
        "world_pair_count": index,
        "world_count": index,
        "growth_seen_count": index,
        "field_core_raw": index,
        "field_full_raw": index,
        "field_full_plus_duration_standardized": index,
    }
    return {
        "neighborhood_symbol": symbol,
        "event_index": str(index),
        **{field: str(values[field]) for field in EVENT_FIELDS},
    }


class MCMRelationEventCausalStateReconstructionTest(unittest.TestCase):
    def test_future_event_does_not_change_earlier_prefix(self) -> None:
        events = [_event("a", 1, 1), _event("a", 2, 3)]
        order = [
            {"position": str(index), "world_label": f"W{index}"}
            for index in range(1, 4)
        ]

        result = _causal_reconstruction(events, [], order)
        snapshots = result["snapshots"]

        self.assertEqual(snapshots[0]["active_relations"], 1)
        self.assertEqual(snapshots[1]["event_state_changed"], 0)
        self.assertEqual(
            snapshots[0]["event_prefix_fingerprint"],
            snapshots[1]["event_prefix_fingerprint"],
        )
        self.assertEqual(snapshots[2]["event_state_changed"], 1)
        self.assertEqual(result["integrity"]["future_event_reads"], 0)

    def test_two_equal_age_relations_reconstruct_lifecycle_observation(self) -> None:
        events = [
            _event("a", 1, 1),
            _event("b", 1, 1),
            _event("a", 2, 2),
            _event("b", 2, 2),
        ]
        lifecycle = [
            {
                "left_relation": "a",
                "right_relation": "b",
                "finalization_index": "2",
                "relation_age": "2",
            }
        ]
        order = [
            {"position": "1", "world_label": "W1"},
            {"position": "2", "world_label": "W2"},
        ]

        result = _causal_reconstruction(events, lifecycle, order)

        self.assertEqual(result["integrity"]["lifecycle_exact"], 1)
        self.assertEqual(result["integrity"]["synchrony_exact"], 1)
        self.assertEqual(result["integrity"]["lifecycle_prefixes_exact"], 2)


if __name__ == "__main__":
    unittest.main()
