from __future__ import annotations

import unittest

from mini_dio.mcm_neuron import MiniMCMField
from mini_dio.mini_world import _empty_senses
from tools.run_mcm_continuous_field_instance import (
    _blank_field_remains_fresh,
    _compare_target,
    _correlation,
    _directed_pairs,
    _dynamic_state,
    _reset_states,
    World,
)


def _senses(coherence: float, tension: float, asymmetry: float) -> dict:
    senses = _empty_senses()
    senses["mcm_feldwirkung"] = {
        "mcm_coherence": coherence,
        "mcm_tension": tension,
        "mcm_asymmetry": asymmetry,
    }
    senses["fuehlen"] = dict(senses["mcm_feldwirkung"])
    return senses


class MCMContinuousFieldInstanceTest(unittest.TestCase):
    def test_correlation_keeps_continuous_carrier_relation(self) -> None:
        self.assertAlmostEqual(_correlation([1.0, 2.0, 3.0], [2.0, 4.0, 6.0]), 1.0)

    def test_empty_ticks_do_not_create_state_in_fresh_field(self) -> None:
        self.assertTrue(_blank_field_remains_fresh(64))

    def test_continuous_field_reports_difference_without_forcing_convergence(self) -> None:
        source = tuple([_senses(0.8, 0.2, -0.1)] * 30)
        target = tuple([_senses(-0.2, 0.6, 0.3)] * 600)
        field = MiniMCMField(12)
        for item in source:
            field.step(item)

        result = _compare_target(field, target, _reset_states(target))

        self.assertGreater(result["first_signature_difference"], 0.0)
        self.assertEqual(result["exact_convergence_reached"], 0)
        self.assertEqual(result["continuity_affected_ticks"], len(target))
        self.assertGreater(result["final_signature_difference"], 0.0)

    def test_pair_builder_keeps_both_contact_directions(self) -> None:
        source = __file__
        worlds = [
            World("d", "A", 2024, source, start)
            for start in (0, 1000, 2000)
        ]

        pairs = _directed_pairs(worlds)

        self.assertEqual(len(pairs), 4)
        self.assertEqual([direction for direction, _, _ in pairs], [
            "forward",
            "reverse",
            "forward",
            "reverse",
        ])


if __name__ == "__main__":
    unittest.main()
