import unittest
import datetime
from fixedcal.core.date import FixedDate

class TestInitWithFixedDate(unittest.TestCase):
    def test_january_first(self):
        fixed_date = FixedDate(day=1, month=1, year=2022)
        self.assertEqual(fixed_date.date, datetime.date(2022, 1, 1))
        self.assertEqual(fixed_date.day_of_year, 1)

    def test_non_leap_year_day(self):
        fixed_date = FixedDate(day=29, month=13, year=2022)
        self.assertEqual(fixed_date.date, datetime.date(2022, 12, 31))
        self.assertTrue(fixed_date.is_year_day)

    def test_leap_year_day(self):
        fixed_date = FixedDate(day=29, month=13, year=2024)
        self.assertEqual(fixed_date.date, datetime.date(2024, 12, 31))
        self.assertTrue(fixed_date.is_year_day)

    def test_leap_year_june_last(self):
        fixed_date = FixedDate(day=28, month=6, year=2024)
        self.assertEqual(fixed_date.date, datetime.date(2024, 6, 16))
        self.assertFalse(fixed_date.is_leap_day)

    def test_leap_year_leap_day(self):
        fixed_date = FixedDate(day=29, month=6, year=2024)
        self.assertEqual(fixed_date.date, datetime.date(2024, 6, 17))
        self.assertTrue(fixed_date.is_leap_day)

    def test_leap_year_sol_first(self):
        fixed_date = FixedDate(day=1, month=7, year=2024)
        self.assertEqual(fixed_date.date, datetime.date(2024, 6, 18))
        self.assertFalse(fixed_date.is_leap_day)

    def test_non_leap_year_sol_first(self):
        fixed_date = FixedDate(day=1, month=7, year=2022)
        self.assertEqual(fixed_date.date, datetime.date(2022, 6, 18))
        self.assertFalse(fixed_date.is_leap_day)

    def test_non_leap_year_leap_day_raises(self):
        self.assertRaises(ValueError, lambda : FixedDate(day=29, month=6, year=2022))

    def test_day_too_big_raises(self):
        self.assertRaises(ValueError, lambda : FixedDate(day=29, month=12, year=2022))

    def test_day_zero_raises(self):
        self.assertRaises(ValueError, lambda : FixedDate(day=0, month=3, year=2022))

    def test_month_zero_raises(self):
        self.assertRaises(ValueError, lambda : FixedDate(day=15, month=0, year=2022))

    def test_month_too_big_raises(self):
        self.assertRaises(ValueError, lambda : FixedDate(day=15, month=14, year=2022))
