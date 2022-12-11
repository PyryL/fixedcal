import unittest
from datetime import datetime, timedelta
from fixedcal.core.date import FixedDate

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.fixed1 = FixedDate(date=datetime(2022, 12, 5))
        self.fixed2 = FixedDate(date=datetime(2022, 12, 6))

    def test_equal_with_two_same(self):
        self.assertTrue(self.fixed1 == self.fixed1)

    def test_equal_with_two_different(self):
        self.assertFalse(self.fixed1 == self.fixed2)

    def test_greather_than_with_true_expected(self):
        self.assertTrue(self.fixed2 > self.fixed1)

    def test_greather_than_with_false_expected(self):
        self.assertFalse(self.fixed1 > self.fixed2)

    def test_greather_than_with_two_same(self):
        self.assertFalse(self.fixed1 > self.fixed1)

    def test_less_than_with_true_expected(self):
        self.assertTrue(self.fixed1 < self.fixed2)

    def test_subtration_with_two_different(self):
        self.assertEqual(self.fixed2-self.fixed1, timedelta(1))

    def test_subtration_with_smaller_first(self):
        self.assertEqual(self.fixed1-self.fixed2, timedelta(-1))

    def test_subtration_with_two_same(self):
        self.assertEqual(self.fixed1-self.fixed1, timedelta(0))
