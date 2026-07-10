from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from mini_dio.mcm_neighborhood_memory import (
    PASSIVE_NEIGHBOR_BOUNDARY,
    finalize_passive_mcm_neighborhood_world,
    observe_passive_mcm_neighborhood_episode,
    passive_mcm_neighborhood_profile,
    top_passive_mcm_neighborhoods,
)
from mini_dio.semantic_memory import SemanticMemory


def _episode(state: str, carry: float, duration: int = 5) -> dict:
    return {
        "episode_state": state,
        "base_field_effect_state": state,
        "passive_mcm_effect_class": state,
        "previous_state": f"before_{state}",
        "next_state": f"after_{state}",
        "transition": f"before_{state}->{state}",
        "start_tick": 10,
        "end_tick": 10 + duration - 1,
        "duration": duration,
        "dominant_family": "dio_inner_family",
        "avg_mcm_carry_quality": carry,
        "avg_mcm_strain_quality": 1.0 - carry,
        "avg_mcm_rekopplung_quality": 0.2 + (carry * 0.6),
        "avg_mcm_adaptive_rekopplung_quality": 0.25 + (carry * 0.5),
        "avg_sensory_coupling": 0.3 + (carry * 0.4),
        "avg_visual_field_gap": 0.7 - (carry * 0.5),
        "avg_hearing_field_gap": 0.15 + (carry * 0.35),
    }


def _observe_world(data: dict, world: str, run_index: int, episodes: list[dict]) -> list[str]:
    symbols = []
    for episode in episodes:
        symbols.append(
            observe_passive_mcm_neighborhood_episode(
                data,
                episode,
                world=world,
                run_index=run_index,
            )["node_symbol"]
        )
    finalize_passive_mcm_neighborhood_world(data, world=world, run_index=run_index)
    return symbols


class MCMNeighborhoodMemoryTest(unittest.TestCase):
    def test_mutual_neighborhoods_emerge_without_predefined_pairs(self) -> None:
        data: dict = {}
        first = _observe_world(
            data,
            "WORLD_A",
            1,
            [_episode("field_a", 0.10), _episode("field_c", 0.90)],
        )
        second = _observe_world(
            data,
            "WORLD_B",
            2,
            [_episode("field_b", 0.12), _episode("field_d", 0.88)],
        )

        active_pairs = {
            frozenset((record["left_node"], record["right_node"])): record
            for record in top_passive_mcm_neighborhoods(data, limit=8)
        }
        self.assertIn(frozenset((first[0], second[0])), active_pairs)
        self.assertIn(frozenset((first[1], second[1])), active_pairs)
        self.assertEqual(active_pairs[frozenset((first[0], second[0]))]["current_scope_count"], 3)

    def test_mutual_rank_has_no_fixed_distance_threshold(self) -> None:
        data: dict = {}
        first = _observe_world(data, "WORLD_A", 1, [_episode("field_low", 0.0)])
        second = _observe_world(data, "WORLD_B", 2, [_episode("field_high", 1.0)])

        records = top_passive_mcm_neighborhoods(data, limit=4)
        self.assertEqual(len(records), 1)
        self.assertEqual(
            {records[0]["left_node"], records[0]["right_node"]},
            {first[0], second[0]},
        )
        self.assertGreater(records[0]["current_avg_distance"]["field_core_raw"], 0.0)

    def test_final_graph_is_independent_of_world_arrival_order(self) -> None:
        worlds = {
            "WORLD_A": (1, [_episode("field_a", 0.15), _episode("field_c", 0.85)]),
            "WORLD_B": (2, [_episode("field_b", 0.20), _episode("field_d", 0.80)]),
            "WORLD_C": (3, [_episode("field_e", 0.25), _episode("field_f", 0.75)]),
        }

        def build(order: list[str]) -> dict[str, tuple[int, int]]:
            data: dict = {}
            for world in order:
                run_index, episodes = worlds[world]
                _observe_world(data, world, run_index, episodes)
            return {
                record["neighborhood_symbol"]: (
                    record["current_scope_count"],
                    record["current_world_pair_count"],
                )
                for record in top_passive_mcm_neighborhoods(data, limit=64)
            }

        self.assertEqual(
            build(["WORLD_A", "WORLD_B", "WORLD_C"]),
            build(["WORLD_C", "WORLD_B", "WORLD_A"]),
        )

    def test_boundary_is_passive_and_survives_reload(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "memory.json"
            memory = SemanticMemory(path)
            memory.observe_passive_mcm_neighborhood_episode(
                _episode("field_a", 0.2), world="WORLD_A", run_index=1
            )
            memory.finalize_passive_mcm_neighborhood_world(world="WORLD_A", run_index=1)
            memory.observe_passive_mcm_neighborhood_episode(
                _episode("field_b", 0.8), world="WORLD_B", run_index=2
            )
            memory.finalize_passive_mcm_neighborhood_world(world="WORLD_B", run_index=2)
            memory.save()

            loaded = SemanticMemory(path)
            loaded.load()
            profile = loaded.passive_mcm_neighborhood_profile()
            self.assertEqual(profile["world_profiles"], 2)
            self.assertEqual(profile["active_neighborhoods"], 1)
            record = loaded.top_passive_mcm_neighborhoods(1)[0]
            for key, value in PASSIVE_NEIGHBOR_BOUNDARY.items():
                self.assertEqual(record[key], value)


if __name__ == "__main__":
    unittest.main()
