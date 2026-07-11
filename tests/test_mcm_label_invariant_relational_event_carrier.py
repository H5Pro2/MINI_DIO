from __future__ import annotations

import unittest

from mini_dio.mcm_neuron import MiniMCMField
from tools.run_mcm_continuous_field_instance import NEURON_COUNT, _contact_field
from tools.run_mcm_label_invariant_relational_event_carrier import (
    EVENT_COUNT_SIZE,
    PAIR_COUNT,
    _event_prefix_profiles,
    _permutation,
    _relabel,
    _profile_component,
    _relation_change_count,
    _source_state,
)


def _ascending() -> tuple[float, ...]:
    return tuple(float(index) for index in range(NEURON_COUNT))


class MCMLabelInvariantRelationalEventCarrierTest(unittest.TestCase):
    def test_relation_change_count_survives_neuron_relabeling(self) -> None:
        previous = _ascending()
        current = previous[3:] + previous[:3]
        expected = _relation_change_count(previous, current)
        for offset in range(NEURON_COUNT):
            self.assertEqual(
                _relation_change_count(
                    _relabel(previous, _permutation(offset)),
                    _relabel(current, _permutation(offset)),
                ),
                expected,
            )

        arbitrary = (5, 1, 10, 0, 8, 3, 11, 6, 2, 9, 4, 7)
        self.assertEqual(
            _relation_change_count(
                _relabel(previous, arbitrary),
                _relabel(current, arbitrary),
            ),
            expected,
        )

    def test_relation_change_count_has_natural_exact_bounds(self) -> None:
        ascending = _ascending()
        self.assertEqual(_relation_change_count(ascending, ascending), 0)
        self.assertEqual(
            _relation_change_count(ascending, tuple(reversed(ascending))),
            PAIR_COUNT,
        )

    def test_profile_records_event_and_signed_event_change(self) -> None:
        field = MiniMCMField(neuron_count=NEURON_COUNT)
        profiles, events, invariant = _event_prefix_profiles(
            field,
            0,
            tuple({} for _ in range(64)),
        )
        first_event = events[0]
        self.assertEqual(profiles[1][first_event], 1)
        self.assertEqual(
            profiles[1][EVENT_COUNT_SIZE + first_event + PAIR_COUNT],
            1,
        )
        self.assertEqual(invariant, 64)

    def test_profile_components_are_exact_nonoverlapping_views(self) -> None:
        values = tuple(range(EVENT_COUNT_SIZE + PAIR_COUNT * 2 + 1))
        count = _profile_component(values, "count")
        delta = _profile_component(values, "delta")
        self.assertEqual(count + delta, values)
        self.assertEqual(_profile_component(values, "combined"), values)

    def test_source_state_matches_existing_field_contact(self) -> None:
        senses = ({"x": 0.25}, {"x": -0.5}, {"x": 0.75})
        observed, _ = _source_state(senses)
        expected = _contact_field(senses)
        self.assertEqual(
            [neuron.activation for neuron in observed.neurons],
            [neuron.activation for neuron in expected.neurons],
        )
        self.assertEqual(observed.last_signature, expected.last_signature)


if __name__ == "__main__":
    unittest.main()
