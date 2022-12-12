import unittest
from fixedcal.core.date import FixedDate

class TestBasicDayOfYearInit(unittest.TestCase):
    def test_day_of_year_init_january_first(self):
        fixed_date = FixedDate(day_of_year=1, year=2022)
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 1)
        self.assertEqual(fixed_date.day_of_month, 1)

    def test_day_of_year_init_february_last(self):
        fixed_date = FixedDate(day_of_year=56, year=2022)      # 2022-02-25 Gregorian
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 2)
        self.assertEqual(fixed_date.day_of_month, 28)

    def test_day_of_year_init_sol_month(self):
        fixed_date = FixedDate(day_of_year=171, year=2022)      # 2022-06-20 Gregorian
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 7)
        self.assertEqual(fixed_date.day_of_month, 3)

    def test_day_of_year_init_december_last(self):
        fixed_date = FixedDate(day_of_year=364, year=2022)      # 2022-12-30 Gregorian
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 13)
        self.assertEqual(fixed_date.day_of_month, 28)
        self.assertFalse(fixed_date.is_year_day)

    def test_day_of_year_init_year_day(self):
        fixed_date = FixedDate(day_of_year=365, year=2022)      # 2022-12-31 Gregorian
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 13)
        self.assertEqual(fixed_date.day_of_month, 29)
        self.assertTrue(fixed_date.is_year_day)
