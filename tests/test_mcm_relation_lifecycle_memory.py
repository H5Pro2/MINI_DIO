from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from mini_dio.mcm_neighborhood_event_memory import (
    observe_passive_mcm_neighborhood_growth_event,
)
from mini_dio.mcm_relation_lifecycle_memory import (
    PASSIVE_RELATION_LIFECYCLE_BOUNDARY,
    observe_passive_mcm_relation_lifecycle,
    passive_mcm_relation_lifecycle_edges,
    passive_mcm_relation_lifecycle_profile,
)
from mini_dio.semantic_memory import SemanticMemory


def _event(
    data: dict,
    symbol: str,
    *,
    finalization: int,
    age: int,
    world_pairs: int,
    worlds: int,
) -> None:
    observe_passive_mcm_neighborhood_growth_event(
        data,
        {
            "neighborhood_symbol": symbol,
            "left_node": f"{symbol}_left",
            "right_node": f"{symbol}_right",
            "current_world_pair_count": world_pairs,
            "current_world_count": worlds,
            "growth_seen_count": age,
            "current_scope_support": {
                "field_core_raw": age,
                "field_full_raw": age,
                "field_full_plus_duration_standardized": age,
            },
        },
        finalization_index=finalization,
    )


class MCMRelationLifecycleMemoryTest(unittest.TestCase):
    def test_equal_age_mutual_neighbors_emerge_without_fixed_members(self) -> None:
        data: dict = {}
        for symbol, second_pairs, second_worlds in (
            ("relation_a", 2, 2),
            ("relation_b", 2, 2),
            ("relation_c", 11, 11),
            ("relation_d", 12, 12),
        ):
            _event(
                data,
                symbol,
                finalization=1,
                age=1,
                world_pairs=1,
                worlds=1,
            )
            _event(
                data,
                symbol,
                finalization=2,
                age=2,
                world_pairs=second_pairs,
                worlds=second_worlds,
            )

        observe_passive_mcm_relation_lifecycle(
            data,
            finalization_index=2,
            changed_relations={
                "relation_a",
                "relation_b",
                "relation_c",
                "relation_d",
            },
        )

        edges = passive_mcm_relation_lifecycle_edges(data)
        pairs = {
            (edge["left_relation"], edge["right_relation"])
            for edge in edges.values()
        }
        self.assertEqual(
            pairs,
            {("relation_a", "relation_b"), ("relation_c", "relation_d")},
        )
        self.assertEqual(
            set(edges),
            {"relation_a|relation_b", "relation_c|relation_d"},
        )
        raw = data["passive_mcm_relation_lifecycle_memory"]
        self.assertNotIn("edges", raw)
        self.assertEqual(len(raw["symbols"]), 4)
        self.assertEqual(len(raw["observation_chunks"]), 1)
        self.assertEqual(raw["observation_count"], 2)

    def test_recurrence_follows_relation_age_and_is_idempotent(self) -> None:
        data: dict = {}
        for symbol in ("relation_a", "relation_b"):
            _event(
                data,
                symbol,
                finalization=1,
                age=1,
                world_pairs=1,
                worlds=1,
            )
            _event(
                data,
                symbol,
                finalization=2,
                age=2,
                world_pairs=2,
                worlds=2,
            )
        observe_passive_mcm_relation_lifecycle(
            data,
            finalization_index=2,
            changed_relations={"relation_a", "relation_b"},
        )
        for symbol in ("relation_a", "relation_b"):
            _event(
                data,
                symbol,
                finalization=3,
                age=3,
                world_pairs=3,
                worlds=3,
            )
        observe_passive_mcm_relation_lifecycle(
            data,
            finalization_index=3,
            changed_relations={"relation_a", "relation_b"},
        )
        observe_passive_mcm_relation_lifecycle(
            data,
            finalization_index=3,
            changed_relations={"relation_a", "relation_b"},
        )

        edge = next(iter(passive_mcm_relation_lifecycle_edges(data).values()))
        self.assertEqual(edge["observation_count"], 2)
        self.assertEqual(
            [item["relation_age"] for item in edge["observations"]], [2, 3]
        )
        profile = passive_mcm_relation_lifecycle_profile(data)
        self.assertEqual(profile["recurring_edges"], 1)
        self.assertEqual(profile["edges_reappearing_at_later_age"], 1)

    def test_boundary_and_non_backfill_survive_save_and_load(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "memory.json"
            memory = SemanticMemory(path)
            for symbol in ("relation_a", "relation_b"):
                _event(
                    memory.data,
                    symbol,
                    finalization=1,
                    age=1,
                    world_pairs=1,
                    worlds=1,
                )
                _event(
                    memory.data,
                    symbol,
                    finalization=2,
                    age=2,
                    world_pairs=2,
                    worlds=2,
                )
            observe_passive_mcm_relation_lifecycle(
                memory.data,
                finalization_index=2,
                changed_relations={"relation_a", "relation_b"},
            )
            memory.save()

            loaded = SemanticMemory(path)
            loaded.load()
            profile = loaded.passive_mcm_relation_lifecycle_profile()
            self.assertEqual(profile["source_events_before_start"], 2)
            self.assertEqual(profile["edges"], 1)
            for key, value in PASSIVE_RELATION_LIFECYCLE_BOUNDARY.items():
                self.assertEqual(profile[key], value)


if __name__ == "__main__":
    unittest.main()
