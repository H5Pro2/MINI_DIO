from __future__ import annotations

import unittest

from tools.run_mcm_continuous_field_instance import NEURON_COUNT
from tools.run_mcm_endogenous_rank_cycle_closure import (
    _endogenous_cycle_episode,
)


class _Neuron:
    def __init__(self, activation: float):
        self.activation = activation


class _Field:
    def __init__(self, initial: tuple[float, ...], states: list[tuple[float, ...]]):
        self.neurons = [_Neuron(value) for value in initial]
        self._states = iter(states)

    def step(self, senses: dict) -> dict:
        values = next(self._states)
        for neuron, value in zip(self.neurons, values):
            neuron.activation = value
        return {"activations": list(values)}


def _ascending() -> tuple[float, ...]:
    return tuple(float(index) for index in range(NEURON_COUNT))


class MCMEndogenousRankCycleClosureTest(unittest.TestCase):
    def test_episode_opens_on_change_and_closes_on_first_exact_return(self) -> None:
        ascending = _ascending()
        descending = tuple(reversed(ascending))
        field = _Field(ascending, [descending, ascending])
        episode = _endogenous_cycle_episode(field, ({}, {}))
        self.assertEqual(episode.opened_tick, 1)
        self.assertEqual(episode.closure_tick, 2)
        self.assertEqual(episode.repeated_from_tick, 0)
        self.assertEqual(episode.cycle_span, 2)
        self.assertEqual(episode.closed, 1)

    def test_episode_does_not_close_before_it_has_opened(self) -> None:
        ascending = _ascending()
        descending = tuple(reversed(ascending))
        field = _Field(ascending, [ascending, descending])
        episode = _endogenous_cycle_episode(field, ({}, {}))
        self.assertEqual(episode.opened_tick, 2)
        self.assertEqual(episode.closed, 0)

    def test_repeated_open_order_closes_without_fixed_duration(self) -> None:
        ascending = _ascending()
        descending = tuple(reversed(ascending))
        field = _Field(ascending, [descending, descending])
        episode = _endogenous_cycle_episode(field, ({}, {}))
        self.assertEqual(episode.closure_tick, 2)
        self.assertEqual(episode.repeated_from_tick, 1)
        self.assertEqual(episode.cycle_span, 1)


if __name__ == "__main__":
    unittest.main()
