import unittest
# from datetime import datetime, timedelta
import datetime
from fixedcal.core.date import FixedDate

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.fixed1 = FixedDate(date=datetime.date(2022, 12, 5))
        self.fixed2 = FixedDate(date=datetime.date(2022, 12, 6))

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

    def test_subtration_of_two_dates(self):
        self.assertEqual(self.fixed2-self.fixed1, datetime.timedelta(1))

    def test_subtration_of_two_dates_with_smaller_first(self):
        self.assertEqual(self.fixed1-self.fixed2, datetime.timedelta(-1))

    def test_subtration_of_two_same_dates(self):
        self.assertEqual(self.fixed1-self.fixed1, datetime.timedelta(0))

    def test_subtraction_of_timedelta(self):
        result = self.fixed1 - datetime.timedelta(7)
        self.assertEqual(result, FixedDate(date=datetime.date(2022, 11, 28)))

    def test_subtraction_of_negative_timedelta(self):
        result = self.fixed1 - datetime.timedelta(-2)
        self.assertEqual(result, FixedDate(date=datetime.date(2022, 12, 7)))

    def test_subtraction_of_invalid_type(self):
        self.assertRaises(ValueError, lambda : self.fixed1 - 3)

    def test_addition_of_timedelta(self):
        result = self.fixed1 + datetime.timedelta(3)
        self.assertEqual(result, FixedDate(date=datetime.date(2022, 12, 8)))

    def test_addition_of_negative_timedelta(self):
        result = self.fixed1 + datetime.timedelta(-3)
        self.assertEqual(result, FixedDate(date=datetime.date(2022, 12, 2)))

    def test_addition_does_not_modify(self):
        _ = self.fixed1 + datetime.timedelta(2)
        self.assertEqual(self.fixed1.date, datetime.date(2022, 12, 5))
