from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from mini_dio.mcm_topological_memory import (
    PASSIVE_BOUNDARY,
    passive_mcm_topology_profile,
    store_passive_mcm_topology_episode,
)
from mini_dio.semantic_memory import SemanticMemory


def _episode(state: str, previous: str, next_state: str, carry: float) -> dict:
    return {
        "episode_state": state,
        "base_field_effect_state": state.replace("field_", "", 1),
        "passive_mcm_effect_class": state.replace("field_", "", 1),
        "previous_state": previous,
        "next_state": next_state,
        "transition": f"{previous}->{state}",
        "start_tick": 10,
        "end_tick": 14,
        "duration": 5,
        "dominant_family": "dio_inner_family",
        "avg_mcm_carry_quality": carry,
        "avg_mcm_strain_quality": 1.0 - carry,
        "avg_mcm_rekopplung_quality": 0.7,
        "avg_mcm_adaptive_rekopplung_quality": 0.72,
        "avg_sensory_coupling": 0.8,
        "avg_visual_field_gap": 0.1,
        "avg_hearing_field_gap": 0.2,
    }


class MCMTopologicalMemoryTest(unittest.TestCase):
    def test_world_context_does_not_change_node_identity(self) -> None:
        data: dict = {}
        payload = _episode("field_carried", "start", "field_open", 0.8)

        first = store_passive_mcm_topology_episode(data, payload, world="WORLD_A", run_index=1)
        second = store_passive_mcm_topology_episode(data, payload, world="WORLD_B", run_index=2)

        self.assertEqual(first["node_symbol"], second["node_symbol"])
        topology = data["passive_mcm_topology"]
        self.assertEqual(len(topology["nodes"]), 1)
        node = topology["nodes"][first["node_symbol"]]
        self.assertEqual(node["seen_count"], 2)
        self.assertEqual(node["world_count"], 2)
        self.assertEqual(set(node["world_observations"]), {"WORLD_A", "WORLD_B"})
        self.assertNotIn("WORLD_A", first["node_symbol"])
        self.assertEqual(passive_mcm_topology_profile(data)["node_return_observations"], 1)

    def test_directed_order_creates_distinct_edges(self) -> None:
        data: dict = {}
        episode_a = _episode("field_carried", "start", "field_open", 0.8)
        episode_b = _episode("field_open", "field_carried", "field_carried", 0.6)
        node_a = store_passive_mcm_topology_episode(data, episode_a)["node_symbol"]
        observation_ab = store_passive_mcm_topology_episode(
            data, episode_b, previous_node_symbol=node_a
        )
        node_b = observation_ab["node_symbol"]
        observation_ba = store_passive_mcm_topology_episode(
            data, episode_a, previous_node_symbol=node_b
        )

        self.assertNotEqual(observation_ab["edge_symbol"], observation_ba["edge_symbol"])
        edges = data["passive_mcm_topology"]["edges"]
        self.assertEqual(len(edges), 2)
        self.assertEqual(edges[observation_ab["edge_symbol"]]["source_node"], node_a)
        self.assertEqual(edges[observation_ab["edge_symbol"]]["target_node"], node_b)
        self.assertEqual(edges[observation_ba["edge_symbol"]]["source_node"], node_b)
        self.assertEqual(edges[observation_ba["edge_symbol"]]["target_node"], node_a)

    def test_recurrence_accumulates_on_existing_edge(self) -> None:
        data: dict = {}
        episode_a = _episode("field_carried", "start", "field_open", 0.8)
        episode_b = _episode("field_open", "field_carried", "field_carried", 0.6)
        node_a = store_passive_mcm_topology_episode(data, episode_a)["node_symbol"]
        first = store_passive_mcm_topology_episode(data, episode_b, previous_node_symbol=node_a)
        second = store_passive_mcm_topology_episode(data, episode_b, previous_node_symbol=node_a)

        self.assertEqual(first["edge_symbol"], second["edge_symbol"])
        edge = data["passive_mcm_topology"]["edges"][first["edge_symbol"]]
        self.assertEqual(edge["seen_count"], 2)
        self.assertEqual(passive_mcm_topology_profile(data)["edge_return_observations"], 1)

    def test_boundary_is_passive_and_survives_reload(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "memory.json"
            memory = SemanticMemory(path)
            observation = memory.store_passive_mcm_topology_episode(
                _episode("field_carried", "start", "field_open", 0.8),
                world="WORLD_A",
                run_index=1,
            )
            memory.save()

            loaded = SemanticMemory(path)
            loaded.load()
            node = loaded.data["passive_mcm_topology"]["nodes"][observation["node_symbol"]]
            for key, value in PASSIVE_BOUNDARY.items():
                self.assertEqual(node[key], value)
            self.assertEqual(loaded.passive_mcm_topology_profile()["nodes"], 1)


if __name__ == "__main__":
    unittest.main()
