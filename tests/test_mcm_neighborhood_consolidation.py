from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from mini_dio.mcm_neighborhood_consolidation import (
    CONSOLIDATION_FORMAT,
    PASSIVE_CONSOLIDATION_BOUNDARY,
)
from mini_dio.semantic_memory import SemanticMemory


def _neighborhood(
    symbol: str,
    left: str,
    right: str,
    world_pairs: int,
    worlds: int,
    growth: int,
) -> dict:
    return {
        "active": 1,
        "neighborhood_symbol": symbol,
        "left_node": left,
        "right_node": right,
        "current_world_pair_count": world_pairs,
        "current_world_count": worlds,
        "growth_seen_count": growth,
    }


def _seed(memory: SemanticMemory) -> None:
    memory.data["passive_mcm_neighborhood_memory"] = {
        "world_profiles": {},
        "neighborhoods": {
            "n_a": _neighborhood("n_a", "a", "b", 5, 3, 2),
            "n_b": _neighborhood("n_b", "c", "d", 4, 2, 1),
            "n_c": _neighborhood("n_c", "e", "f", 5, 2, 4),
        },
    }


class MCMNeighborhoodConsolidationTest(unittest.TestCase):
    def test_consolidation_is_passive_idempotent_and_preserves_source(self) -> None:
        memory = SemanticMemory("unused.json")
        _seed(memory)
        source_before = copy.deepcopy(memory.data["passive_mcm_neighborhood_memory"])

        first = memory.consolidate_passive_mcm_neighborhood_layers(
            checkpoint_label="world_10", run_index=10
        )
        repeated = memory.consolidate_passive_mcm_neighborhood_layers(
            checkpoint_label="world_10", run_index=10
        )

        self.assertEqual(memory.data["passive_mcm_neighborhood_memory"], source_before)
        self.assertEqual(first, repeated)
        self.assertEqual(first["checkpoints"], 1)
        self.assertEqual(first["history_entries"], 3)
        self.assertEqual(first["latest_layer_one_count"], 2)
        store = memory.data["passive_mcm_neighborhood_consolidation"]
        for key, value in PASSIVE_CONSOLIDATION_BOUNDARY.items():
            self.assertEqual(store[key], value)
        self.assertEqual(store["format"], CONSOLIDATION_FORMAT)
        self.assertNotIn("history", store["relations"]["n_b"])
        self.assertNotIn("latest_pareto_depth", store["relations"]["n_b"])
        self.assertEqual(store["relations"]["n_b"]["history_deltas"], [[1, 2, 4, 2, 1]])
        self.assertEqual(
            memory.passive_mcm_neighborhood_consolidation_relations()["n_b"][
                "latest_pareto_depth"
            ],
            2,
        )

    def test_later_checkpoint_appends_without_rewriting_history(self) -> None:
        memory = SemanticMemory("unused.json")
        _seed(memory)
        memory.consolidate_passive_mcm_neighborhood_layers(
            checkpoint_label="world_10", run_index=10
        )
        first_history = copy.deepcopy(
            memory.passive_mcm_neighborhood_consolidation_relations()["n_b"]["history"]
        )
        memory.data["passive_mcm_neighborhood_memory"]["neighborhoods"]["n_b"].update(
            {
                "current_world_pair_count": 7,
                "current_world_count": 4,
                "growth_seen_count": 3,
            }
        )

        profile = memory.consolidate_passive_mcm_neighborhood_layers(
            checkpoint_label="world_20", run_index=20
        )
        history = memory.passive_mcm_neighborhood_consolidation_relations()["n_b"][
            "history"
        ]

        self.assertEqual(profile["checkpoints"], 2)
        self.assertEqual(history[:-1], first_history)
        self.assertEqual(history[-1]["world_pair_count"], 7)
        self.assertEqual(history[-1]["checkpoint_index"], 2)
        self.assertEqual(
            memory.data["passive_mcm_neighborhood_consolidation"]["relations"]["n_b"][
                "history_deltas"
            ],
            [[1, 2, 4, 2, 1], [1, -1, 3, 2, 2]],
        )

    def test_verbose_history_is_migrated_without_information_loss(self) -> None:
        memory = SemanticMemory("unused.json")
        _seed(memory)
        memory.data["passive_mcm_neighborhood_consolidation"] = {
            "checkpoints": [
                {
                    "checkpoint_symbol": "legacy_1",
                    "checkpoint_index": 1,
                    "checkpoint_label": "world_10",
                    "run_index": 10,
                    "relation_count": 1,
                    "max_pareto_depth": 2,
                    "layer_one_count": 0,
                    "layer_counts": {"2": 1},
                }
            ],
            "relations": {
                "n_b": {
                    **PASSIVE_CONSOLIDATION_BOUNDARY,
                    "neighborhood_symbol": "n_b",
                    "left_node": "c",
                    "right_node": "d",
                    "latest_pareto_depth": 2,
                    "history": [
                        {
                            "checkpoint_symbol": "legacy_1",
                            "checkpoint_index": 1,
                            "checkpoint_label": "world_10",
                            "run_index": 10,
                            "pareto_depth": 2,
                            "max_pareto_depth": 2,
                            "normalized_depth": 1.0,
                            "world_pair_count": 4,
                            "world_count": 2,
                            "growth_seen_count": 1,
                        }
                    ],
                }
            },
        }
        self.assertEqual(
            memory.passive_mcm_neighborhood_consolidation_profile()["format"],
            "verbose_v1",
        )

        memory.consolidate_passive_mcm_neighborhood_layers(
            checkpoint_label="world_20", run_index=20
        )
        raw = memory.data["passive_mcm_neighborhood_consolidation"]["relations"]["n_b"]
        expanded = memory.passive_mcm_neighborhood_consolidation_relations()["n_b"]

        self.assertNotIn("history", raw)
        self.assertEqual(
            memory.data["passive_mcm_neighborhood_consolidation"]["format"],
            CONSOLIDATION_FORMAT,
        )
        self.assertEqual(raw["history_deltas"], [[1, 2, 4, 2, 1], [1, 0, 0, 0, 0]])
        self.assertEqual(expanded["history"][0]["checkpoint_symbol"], "legacy_1")
        self.assertEqual(expanded["history"][0]["normalized_depth"], 1.0)
        self.assertEqual(expanded["history"][1]["checkpoint_label"], "world_20")

    def test_boundary_and_history_survive_save_and_load(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "memory.json"
            memory = SemanticMemory(path)
            _seed(memory)
            memory.consolidate_passive_mcm_neighborhood_layers(
                checkpoint_label="world_10", run_index=10
            )
            memory.save()

            loaded = SemanticMemory(path)
            loaded.load()
            profile = loaded.passive_mcm_neighborhood_consolidation_profile()
            top = loaded.top_passive_mcm_neighborhood_consolidation(3)

            self.assertEqual(profile["checkpoints"], 1)
            self.assertEqual(profile["history_entries"], 3)
            self.assertEqual(profile["format"], CONSOLIDATION_FORMAT)
            self.assertEqual(
                [record["neighborhood_symbol"] for record in top],
                ["n_a", "n_c", "n_b"],
            )
            for key, value in PASSIVE_CONSOLIDATION_BOUNDARY.items():
                self.assertEqual(top[0][key], value)


if __name__ == "__main__":
    unittest.main()
