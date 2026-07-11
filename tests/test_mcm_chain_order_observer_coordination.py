from __future__ import annotations

import unittest

from mini_dio.mcm_neuron import MiniMCMField
from tools.run_mcm_chain_order_observer_coordination import (
    _chain_orders,
    _trace_with_order,
)
from tools.run_mcm_passive_observer_boundary import _trace, _trace_digest


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


class MCMChainOrderObserverCoordinationTest(unittest.TestCase):
    def test_original_order_reproduces_production_trace(self) -> None:
        production = MiniMCMField(neuron_count=4)
        diagnostic = MiniMCMField(neuron_count=4)

        production_trace = _trace(production, SENSES)
        diagnostic_trace = _trace_with_order(diagnostic, SENSES, (0, 1, 2, 3))

        self.assertEqual(
            _trace_digest(diagnostic_trace),
            _trace_digest(production_trace),
        )

    def test_orders_cover_every_head_in_both_directions(self) -> None:
        orders = _chain_orders(4)

        self.assertEqual(len(orders), 8)
        self.assertEqual(len({order for _, order in orders}), 8)
        self.assertEqual(
            {order[0] for label, order in orders if label.startswith("reverse")},
            {0, 1, 2, 3},
        )
        self.assertEqual(
            {order[0] for label, order in orders if label.startswith("forward")}
            | {orders[0][1][0]},
            {0, 1, 2, 3},
        )
        self.assertEqual(
            sum(label.startswith("forward_rotation") for label, _ in orders),
            3,
        )
        self.assertEqual(
            sum(label.startswith("reverse_rotation") for label, _ in orders),
            4,
        )

    def test_alternative_order_changes_coupled_trace(self) -> None:
        original = MiniMCMField(neuron_count=4)
        reverse = MiniMCMField(neuron_count=4)

        original_trace = _trace_with_order(original, SENSES, (0, 1, 2, 3))
        reverse_trace = _trace_with_order(reverse, SENSES, (3, 2, 1, 0))

        self.assertNotEqual(
            _trace_digest(original_trace),
            _trace_digest(reverse_trace),
        )


if __name__ == "__main__":
    unittest.main()
