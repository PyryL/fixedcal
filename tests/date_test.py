import unittest
from datetime import datetime
from fixedcal.core.date import FixedDate

class TestDate(unittest.TestCase):
    def setUp(self):
        pass

    def test_datetime_init_january_first(self):
        fixed_date = FixedDate(date=datetime(2022, 1, 1))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 1)
        self.assertEqual(fixed_date.day_of_month, 1)

    def test_datetime_init_february_last(self):
        fixed_date = FixedDate(date=datetime(2022, 2, 25))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 2)
        self.assertEqual(fixed_date.day_of_month, 28)

    def test_datetime_init_sol_month(self):
        fixed_date = FixedDate(date=datetime(2022, 6, 20))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 7)
        self.assertEqual(fixed_date.day_of_month, 3)

    def test_datetime_init_december_last(self):
        fixed_date = FixedDate(date=datetime(2022, 12, 30))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 13)
        self.assertEqual(fixed_date.day_of_month, 28)
        self.assertFalse(fixed_date.is_year_day)

    def test_datetime_init_year_day(self):
        fixed_date = FixedDate(date=datetime(2022, 12, 31))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 14)
        self.assertEqual(fixed_date.day_of_month, 1)
        self.assertTrue(fixed_date.is_year_day)
