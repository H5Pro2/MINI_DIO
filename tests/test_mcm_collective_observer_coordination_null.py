from __future__ import annotations

import unittest

from tools.run_mcm_collective_observer_coordination_null import (
    _neuron_shifts,
    _shift_neuron_pairs,
    _synchrony_excess,
)
from tools.run_mcm_passive_observer_boundary import FieldFrame


class MCMCollectiveObserverCoordinationNullTest(unittest.TestCase):
    def test_shift_preserves_each_local_activation_afterimage_pair(self) -> None:
        trace = tuple(
            FieldFrame(
                activations=(tick + 0.1, tick + 0.2, tick + 0.3),
                afterimages=(tick + 10.1, tick + 10.2, tick + 10.3),
            )
            for tick in range(4)
        )
        shifted = _shift_neuron_pairs(trace, (0, 1, 3))

        for neuron in range(3):
            original_pairs = sorted(
                (frame.activations[neuron], frame.afterimages[neuron])
                for frame in trace
            )
            shifted_pairs = sorted(
                (frame.activations[neuron], frame.afterimages[neuron])
                for frame in shifted
            )
            self.assertEqual(shifted_pairs, original_pairs)

    def test_independent_shift_is_deterministic_and_not_collective(self) -> None:
        left = _neuron_shifts("2123-test", 17, 12)
        right = _neuron_shifts("2123-test", 17, 12)

        self.assertEqual(left, right)
        self.assertGreater(len(set(left)), 1)

    def test_synchrony_excess_removes_own_cadence_expectation(self) -> None:
        self.assertEqual(_synchrony_excess((1, 4), (1, 4), 5), 1.5)
        self.assertEqual(_synchrony_excess((1, 4), (2, 5), 5), -1.0)


if __name__ == "__main__":
    unittest.main()
