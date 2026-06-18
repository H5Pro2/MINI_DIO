from __future__ import annotations


class Config:
    """Local defaults for the standalone MINI_DIO research project."""

    DIO_MINI_MCM_NEURON_COUNT = 12
    DIO_MINI_EPISODE_MEMORY_MAX_TICKS = 2048
    DIO_MINI_MAX_EPISODES = 4096

    DIO_MINI_CONTROLLED_WORLD_PATH = "data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv"
    DIO_MINI_EPISODIC_MEMORY_PATH = "memory/dio_mini_semantic_memory.json"
