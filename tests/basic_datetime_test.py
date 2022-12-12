import unittest
# from datetime import datetime
import datetime
from fixedcal.core.date import FixedDate

class TestBasicDateInit(unittest.TestCase):
    def test_date_init_january_first(self):
        fixed_date = FixedDate(date=datetime.date(2022, 1, 1))
        self.assertEqual(fixed_date.date, datetime.date(2022, 1, 1))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 1)
        self.assertEqual(fixed_date.day_of_month, 1)
        self.assertEqual(fixed_date.day_of_year, 1)
        self.assertEqual(fixed_date.week_of_month, 1)
        self.assertEqual(fixed_date.weekday, 1)
        self.assertEqual(fixed_date.week_of_year, 1)
        self.assertEqual(fixed_date.year_quarter, 1)

    def test_date_init_february_last(self):
        fixed_date = FixedDate(date=datetime.date(2022, 2, 25))
        self.assertEqual(fixed_date.date, datetime.date(2022, 2, 25))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 2)
        self.assertEqual(fixed_date.day_of_month, 28)
        self.assertEqual(fixed_date.day_of_year, 56)
        self.assertEqual(fixed_date.week_of_month, 4)
        self.assertEqual(fixed_date.weekday, 7)
        self.assertEqual(fixed_date.week_of_year, 8)
        self.assertEqual(fixed_date.year_quarter, 1)

    def test_date_init_sol_month(self):
        fixed_date = FixedDate(date=datetime.date(2022, 6, 20))
        self.assertEqual(fixed_date.date, datetime.date(2022, 6, 20))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 7)
        self.assertEqual(fixed_date.day_of_month, 3)
        self.assertEqual(fixed_date.day_of_year, 171)
        self.assertEqual(fixed_date.week_of_month, 1)
        self.assertEqual(fixed_date.weekday, 3)
        self.assertEqual(fixed_date.week_of_year, 25)
        self.assertEqual(fixed_date.year_quarter, 2)

    def test_date_init_middle_of_september(self):
        fixed_date = FixedDate(date=datetime.date(2022, 9, 15))
        self.assertEqual(fixed_date.date, datetime.date(2022, 9, 15))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 10)
        self.assertEqual(fixed_date.day_of_month, 6)
        self.assertEqual(fixed_date.day_of_year, 258)
        self.assertEqual(fixed_date.week_of_month, 1)
        self.assertEqual(fixed_date.weekday, 6)
        self.assertEqual(fixed_date.week_of_year, 37)
        self.assertEqual(fixed_date.year_quarter, 3)

    def test_date_init_december_last(self):
        fixed_date = FixedDate(date=datetime.date(2022, 12, 30))
        self.assertEqual(fixed_date.date, datetime.date(2022, 12, 30))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 13)
        self.assertEqual(fixed_date.day_of_month, 28)
        self.assertFalse(fixed_date.is_year_day)
        self.assertEqual(fixed_date.day_of_year, 364)
        self.assertEqual(fixed_date.week_of_month, 4)
        self.assertEqual(fixed_date.weekday, 7)
        self.assertEqual(fixed_date.week_of_year, 52)
        self.assertEqual(fixed_date.year_quarter, 4)

    def test_date_init_year_day(self):
        fixed_date = FixedDate(date=datetime.date(2022, 12, 31))
        self.assertEqual(fixed_date.date, datetime.date(2022, 12, 31))
        self.assertEqual(fixed_date.year, 2022)
        self.assertEqual(fixed_date.month, 13)
        self.assertEqual(fixed_date.day_of_month, 29)
        self.assertTrue(fixed_date.is_year_day)
        self.assertEqual(fixed_date.day_of_year, 365)
        self.assertEqual(fixed_date.week_of_month, 4)
        self.assertIsNone(fixed_date.weekday)
        self.assertEqual(fixed_date.week_of_year, 52)
        self.assertEqual(fixed_date.year_quarter, 4)

    def test_today(self):
        fixed_date_datetime = FixedDate.today().date
        self.assertEqual(fixed_date_datetime, datetime.date.today())
