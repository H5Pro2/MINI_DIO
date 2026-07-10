from __future__ import annotations

import unittest

from tools.run_mcm_relation_lifecycle_integration import (
    _baseline_payload,
    _expected_observations,
)
from tools.run_mcm_breadth_data_holdout import _order_rows, _world_specs
from tools.run_mcm_neighborhood_relation_event_time import _csv_bytes


def _relation(symbol: str, second_pairs: int, second_worlds: int) -> dict:
    return {
        "neighborhood_symbol": symbol,
        "unobserved_prior_events": 0,
        "events": [
            {
                "event_index": 1,
                "finalization_index": 1,
                "world_pair_count": 1,
                "world_count": 1,
                "growth_seen_count": 1,
                "field_core_raw": 1,
                "field_full_raw": 1,
                "field_full_plus_duration_standardized": 1,
            },
            {
                "event_index": 2,
                "finalization_index": 2,
                "world_pair_count": second_pairs,
                "world_count": second_worlds,
                "growth_seen_count": 2,
                "field_core_raw": 2,
                "field_full_raw": 2,
                "field_full_plus_duration_standardized": 2,
            },
        ],
    }


class MCMRelationLifecycleIntegrationTest(unittest.TestCase):
    def test_replay_order_is_byte_equal_to_2089(self) -> None:
        self.assertEqual(
            _csv_bytes(_order_rows(_world_specs())),
            _baseline_payload("holdout_order.csv"),
        )

    def test_offline_reconstruction_finds_mutual_breadth_neighbors(self) -> None:
        relations = {
            "relation_a": _relation("relation_a", 2, 2),
            "relation_b": _relation("relation_b", 2, 2),
            "relation_c": _relation("relation_c", 11, 11),
            "relation_d": _relation("relation_d", 12, 12),
        }

        self.assertEqual(
            _expected_observations(relations),
            {
                ("relation_a", "relation_b", 2, 2),
                ("relation_c", "relation_d", 2, 2),
            },
        )


if __name__ == "__main__":
    unittest.main()
