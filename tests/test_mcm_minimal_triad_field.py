from __future__ import annotations

import unittest

from mini_dio.mcm_neuron import MiniMCMField
from tools.run_mcm_minimal_triad_field import (
    _joint_states,
    _local_sequences,
    _run_target_triad,
    _source_triads,
)
from tools.run_mcm_passive_observer_boundary import _trace_digest


SENSES = tuple(
    {
        "mcm_feldwirkung": {
            "mcm_coherence": value,
            "mcm_tension": -value / 2.0,
            "mcm_asymmetry": value / 3.0,
        }
    }
    for value in (0.2, 0.5, -0.3, 0.8)
)


class _Source:
    def __init__(self, key: str) -> None:
        self.key = key


class MCMMinimalTriadFieldTest(unittest.TestCase):
    def test_source_triads_cover_every_source(self) -> None:
        sources = [_Source(f"s{index}") for index in range(5)]
        triads = _source_triads(sources)

        self.assertEqual(len(triads), 2)
        self.assertEqual(
            {source.key for triad in triads for source in triad},
            {source.key for source in sources},
        )
        self.assertTrue(all(len(triad) == 3 for triad in triads))

    def test_identical_fields_remain_symmetric_without_programmed_center(self) -> None:
        fields = tuple(MiniMCMField(neuron_count=4) for _ in range(3))
        traces, _, _ = _run_target_triad(fields, SENSES, connected=True)

        self.assertEqual(_trace_digest(traces[0]), _trace_digest(traces[1]))
        self.assertEqual(_trace_digest(traces[1]), _trace_digest(traces[2]))

    def test_connected_triad_is_equivariant_to_field_permutation(self) -> None:
        fields = [MiniMCMField(neuron_count=4) for _ in range(3)]
        fields[0].step(SENSES[0])
        fields[1].step(SENSES[1])
        fields[2].step(SENSES[2])
        original, _, _ = _run_target_triad(tuple(fields), SENSES, connected=True)
        permutation = (2, 0, 1)
        permuted, _, _ = _run_target_triad(
            tuple(fields[index] for index in permutation),
            SENSES,
            connected=True,
        )

        self.assertEqual(
            sorted(_trace_digest(trace) for trace in original),
            sorted(_trace_digest(trace) for trace in permuted),
        )
        self.assertEqual(
            _joint_states(_local_sequences(original)),
            _joint_states(_local_sequences(permuted)),
        )


if __name__ == "__main__":
    unittest.main()
