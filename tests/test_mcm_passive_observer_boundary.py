from __future__ import annotations

import unittest

from tools.run_mcm_passive_observer_boundary import (
    FieldFrame,
    PROJECTIONS,
    RecurrenceObserver,
    _observe_all,
    _nonzero_shift_expected,
    _shifted_overlap,
    _trace_digest,
)


def _frame(*values: float) -> FieldFrame:
    return FieldFrame(
        activations=tuple(values),
        afterimages=tuple(reversed(values)),
    )


class MCMPassiveObserverBoundaryTest(unittest.TestCase):
    def test_recurrence_closes_only_after_a_state_change(self) -> None:
        observer = RecurrenceObserver((0, 1))

        self.assertIsNone(observer.observe((0, 1), 1))
        self.assertIsNone(observer.observe((1, 0), 2))
        event = observer.observe((0, 1), 3)

        self.assertIsNotNone(event)
        self.assertEqual((event.opened_tick, event.closure_tick), (2, 3))

    def test_projection_order_does_not_change_trace_or_results(self) -> None:
        trace = (
            _frame(0.1, 0.2, 0.3),
            _frame(0.2, 0.3, 0.1),
            _frame(0.1, 0.2, 0.3),
            _frame(0.3, 0.1, 0.2),
            _frame(0.1, 0.2, 0.3),
        )
        before = _trace_digest(trace)
        order = tuple(PROJECTIONS)
        forward = _observe_all(trace, 0, order)
        reverse = _observe_all(trace, 0, tuple(reversed(order)))

        self.assertEqual(forward, reverse)
        self.assertEqual(_trace_digest(trace), before)

    def test_circular_null_preserves_event_count_and_wraps(self) -> None:
        left = (1, 4)
        right = (1, 4)

        self.assertEqual(_shifted_overlap(left, right, 5, 0), 2)
        self.assertEqual(_shifted_overlap(left, right, 5, 1), 0)
        self.assertEqual(_shifted_overlap(left, right, 5, 2), 1)

    def test_expected_value_excludes_identity_shift(self) -> None:
        left = (1, 4)
        right = (1, 4)

        overlaps = [
            _shifted_overlap(left, right, 5, shift)
            for shift in range(1, 5)
        ]

        self.assertEqual(_nonzero_shift_expected(left, right, 5), 0.5)
        self.assertEqual(sum(overlaps) / len(overlaps), 0.5)


if __name__ == "__main__":
    unittest.main()
