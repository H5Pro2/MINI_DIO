from __future__ import annotations

import copy
import unittest

from mini_dio.mcm_neighborhood_event_memory import (
    EVENT_FORMAT,
    PASSIVE_EVENT_BOUNDARY,
    observe_passive_mcm_neighborhood_growth_event,
    passive_mcm_neighborhood_event_profile,
    passive_mcm_neighborhood_event_relations,
)


def _neighborhood(
    *,
    world_pairs: int,
    worlds: int,
    growth: int,
    core: int,
    full: int,
    duration: int,
) -> dict:
    return {
        "neighborhood_symbol": "n_a",
        "left_node": "episode_a",
        "right_node": "episode_b",
        "current_world_pair_count": world_pairs,
        "current_world_count": worlds,
        "growth_seen_count": growth,
        "current_scope_support": {
            "field_core_raw": core,
            "field_full_raw": full,
            "field_full_plus_duration_standardized": duration,
        },
    }


class MCMNeighborhoodEventMemoryTest(unittest.TestCase):
    def test_growth_events_are_stored_as_exact_relation_internal_deltas(self) -> None:
        data: dict = {}
        first = _neighborhood(
            world_pairs=3,
            worlds=2,
            growth=1,
            core=5,
            full=4,
            duration=3,
        )
        second = _neighborhood(
            world_pairs=8,
            worlds=4,
            growth=2,
            core=9,
            full=7,
            duration=6,
        )
        source_before = copy.deepcopy(first)

        observe_passive_mcm_neighborhood_growth_event(
            data, first, finalization_index=2
        )
        observe_passive_mcm_neighborhood_growth_event(
            data, second, finalization_index=5
        )

        self.assertEqual(first, source_before)
        raw = data["passive_mcm_neighborhood_event_memory"]["relations"]["n_a"]
        self.assertEqual(
            raw["event_deltas"],
            [[2, 3, 2, 1, 5, 4, 3], [3, 5, 2, 1, 4, 3, 3]],
        )
        events = passive_mcm_neighborhood_event_relations(data)["n_a"]["events"]
        self.assertEqual(events[0]["finalization_index"], 2)
        self.assertEqual(events[1]["world_pair_count"], 8)
        self.assertEqual(events[1]["field_full_raw"], 7)
        self.assertEqual(
            passive_mcm_neighborhood_event_relations(data)["n_a"][
                "unobserved_prior_events"
            ],
            0,
        )

    def test_same_finalization_is_idempotent(self) -> None:
        data: dict = {}
        record = _neighborhood(
            world_pairs=3,
            worlds=2,
            growth=1,
            core=5,
            full=4,
            duration=3,
        )

        first = observe_passive_mcm_neighborhood_growth_event(
            data, record, finalization_index=2
        )
        repeated = observe_passive_mcm_neighborhood_growth_event(
            data, record, finalization_index=2
        )

        self.assertEqual(first, repeated)
        self.assertEqual(passive_mcm_neighborhood_event_profile(data)["events"], 1)

    def test_boundary_and_profile_remain_passive(self) -> None:
        data: dict = {}
        observe_passive_mcm_neighborhood_growth_event(
            data,
            _neighborhood(
                world_pairs=3,
                worlds=2,
                growth=1,
                core=5,
                full=4,
                duration=3,
            ),
            finalization_index=2,
        )

        profile = passive_mcm_neighborhood_event_profile(data)
        relation = passive_mcm_neighborhood_event_relations(data)["n_a"]
        self.assertEqual(profile["format"], EVENT_FORMAT)
        self.assertEqual(profile["relations"], 1)
        self.assertEqual(profile["events"], 1)
        for key, value in PASSIVE_EVENT_BOUNDARY.items():
            self.assertEqual(profile[key], value)
            self.assertEqual(relation[key], value)

    def test_existing_growth_is_marked_unobserved_instead_of_backfilled(self) -> None:
        data: dict = {}
        observe_passive_mcm_neighborhood_growth_event(
            data,
            _neighborhood(
                world_pairs=12,
                worlds=6,
                growth=4,
                core=14,
                full=12,
                duration=10,
            ),
            finalization_index=20,
        )

        relation = passive_mcm_neighborhood_event_relations(data)["n_a"]
        profile = passive_mcm_neighborhood_event_profile(data)
        self.assertEqual(relation["event_count"], 1)
        self.assertEqual(relation["unobserved_prior_events"], 3)
        self.assertEqual(relation["total_growth_event_count"], 4)
        self.assertEqual(profile["events"], 1)
        self.assertEqual(profile["legacy_unobserved_events"], 3)
        self.assertEqual(profile["total_growth_events"], 4)


if __name__ == "__main__":
    unittest.main()
