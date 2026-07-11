from __future__ import annotations

import unittest

from mini_dio.mcm_neuron import MiniMCMField
from tools.run_mcm_neighbor_coupling_observer_coordination import (
    _neuron_trace_digest,
    _trace_without_neighbor_signal,
    _weights_digest,
)
from tools.run_mcm_passive_observer_boundary import _trace


SENSES = (
    {
        "mcm_feldwirkung": {
            "mcm_coherence": 0.7,
            "mcm_tension": -0.2,
            "mcm_asymmetry": 0.4,
        }
    },
    {
        "mcm_feldwirkung": {
            "mcm_coherence": -0.3,
            "mcm_tension": 0.8,
            "mcm_asymmetry": 0.1,
        }
    },
)


class MCMNeighborCouplingObserverCoordinationTest(unittest.TestCase):
    def test_control_keeps_weights_and_first_neuron_trace_exact(self) -> None:
        coupled = MiniMCMField(neuron_count=4)
        control = MiniMCMField(neuron_count=4)

        coupled_trace = _trace(coupled, SENSES)
        control_trace = _trace_without_neighbor_signal(control, SENSES)

        self.assertEqual(_weights_digest(coupled), _weights_digest(control))
        self.assertEqual(
            _neuron_trace_digest(coupled_trace, 0),
            _neuron_trace_digest(control_trace, 0),
        )

    def test_control_removes_only_downstream_neighbor_signal(self) -> None:
        coupled = MiniMCMField(neuron_count=4)
        control = MiniMCMField(neuron_count=4)

        coupled_trace = _trace(coupled, SENSES)
        control_trace = _trace_without_neighbor_signal(control, SENSES)

        self.assertNotEqual(
            _neuron_trace_digest(coupled_trace, 1),
            _neuron_trace_digest(control_trace, 1),
        )
        self.assertEqual(_weights_digest(coupled), _weights_digest(control))


if __name__ == "__main__":
    unittest.main()
