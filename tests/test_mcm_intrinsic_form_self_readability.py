from __future__ import annotations

import unittest

from tools.run_mcm_intrinsic_form_self_readability import (
    FINGERPRINT_SIZE,
    NEURON_COUNT,
    _mutual_nearest_edges,
    _record_relation_transitions,
)


class MCMIntrinsicFormSelfReadabilityTest(unittest.TestCase):
    def test_intrinsic_transition_uses_only_consecutive_rank_relations(self) -> None:
        previous = tuple(float(index) for index in range(NEURON_COUNT))
        current = tuple(reversed(previous))
        counts = [0] * FINGERPRINT_SIZE
        changed = _record_relation_transitions(previous, current, counts)
        self.assertEqual(changed, NEURON_COUNT * (NEURON_COUNT - 1) // 2)
        self.assertEqual(sum(counts), changed)

    def test_equal_consecutive_relations_create_no_observation(self) -> None:
        values = tuple(float(index) for index in range(NEURON_COUNT))
        counts = [0] * FINGERPRINT_SIZE
        self.assertEqual(_record_relation_transitions(values, values, counts), 0)
        self.assertEqual(sum(counts), 0)

    def test_mutual_nearest_excludes_one_sided_neighbor(self) -> None:
        self.assertEqual(
            _mutual_nearest_edges([[0.0, 1.0], [0.5, 1.0]]),
            [(0, 0)],
        )

    def test_mutual_nearest_preserves_exact_ties(self) -> None:
        self.assertEqual(
            _mutual_nearest_edges([[1.0, 1.0], [1.0, 1.0]]),
            [(0, 0), (0, 1), (1, 0), (1, 1)],
        )


if __name__ == "__main__":
    unittest.main()
