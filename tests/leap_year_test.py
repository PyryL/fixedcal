import unittest
import datetime
from fixedcal import FixedDate

class TestLeapYear(unittest.TestCase):
    def test_leap_year_detection_with_simple_noleap(self):
        # 2022 is not divisible of four -> not a leap year
        fixed_date = FixedDate(datetime.date(2022, 5, 4))
        self.assertFalse(fixed_date.is_leap_year)

    def test_leap_year_detection_with_complex_noleap(self):
        # 1900 is divisible of four but also by 100 and not by 400 -> not a leap year
        fixed_date = FixedDate(datetime.date(1900, 5, 4))
        self.assertFalse(fixed_date.is_leap_year)

    def test_leap_year_detection_with_common_leap_year(self):
        # 2024 is divisible of four but not by 100 -> leap year
        fixed_date = FixedDate(datetime.date(2024, 5, 4))
        self.assertTrue(fixed_date.is_leap_year)

    def test_leap_year_detection_with_centurial_leap_year(self):
        # 2000 is divisible of all four, 100 and 400 -> leap year
        fixed_date = FixedDate(datetime.date(2000, 5, 4))
        self.assertTrue(fixed_date.is_leap_year)


    def test_fixed_leap_day_properties(self):
        # June 17th is the leap day of fixed calendar system
        fixed_date = FixedDate(datetime.date(2024, 6, 17))
        self.assertEqual(fixed_date.day_of_month, 29)
        self.assertEqual(fixed_date.month, 6)
        self.assertIsNone(fixed_date.weekday)
        self.assertEqual(fixed_date.week_of_month, 4)
        self.assertEqual(fixed_date.week_of_year, 24)
        self.assertEqual(fixed_date.year_quarter, 2)

    def test_year_day_of_leap_year(self):
        fixed_date = FixedDate(day_of_year=366, year=2024)
        self.assertTrue(fixed_date.is_year_day)
        self.assertEqual(fixed_date.year, 2024)
        self.assertEqual(fixed_date.month, 13)
        self.assertEqual(fixed_date.day_of_month, 29)

    def test_ordinary_date_after_leap_day(self):
        fixed_date = FixedDate(datetime.date(2024, 10, 13))
        self.assertEqual(fixed_date.month, 11)
        self.assertEqual(fixed_date.day_of_month, 6)


    def test_fixed_date_difference_over_gregorian_leap_day(self):
        # in Gregorian system there are 7 days between,
        # but in IFC the leap day is at the end of June
        # and thus the difference should be just 6 days
        date1 = FixedDate(datetime.date(2024, 2, 25))
        date2 = FixedDate(datetime.date(2024, 3, 3))
        self.assertEqual(date2-date1, datetime.timedelta(6))

    def test_fixed_date_difference_over_fixed_leap_day(self):
        # in Gregorian system there are 7 days between,
        # but in IFC the leap day is also in between
        # and therefore the difference should be 8 days
        date1 = FixedDate(datetime.date(2024, 6, 27))
        date2 = FixedDate(datetime.date(2024, 7, 4))
        self.assertEqual(date2-date1, datetime.timedelta(8))

    def test_fixed_date_difference_with_itself_gregorian_leap_day(self):
        date = FixedDate(datetime.date(2024, 2, 29))
        self.assertEqual(date-date, datetime.timedelta(0))

    def test_fixed_date_difference_with_itself_fixed_leap_day(self):
        date = FixedDate(datetime.date(2024, 6, 27))
        self.assertEqual(date-date, datetime.timedelta(0))

    def test_fixed_date_difference_over_both_leap_days(self):
        # day count should be the same in both systems
        date1 = FixedDate(datetime.date(2024, 2, 15))
        date2 = FixedDate(datetime.date(2024, 8, 3))
        self.assertEqual(date2-date1, datetime.timedelta(170))

    def test_fixed_date_difference_over_multiple_leap_days(self):
        # there are 3 Gregorian and 2 fixed leap days between
        # difference is 2987 days in Gregorian including Greg leap days
        date1 = FixedDate(datetime.date(2020, 2, 15))
        date2 = FixedDate(datetime.date(2028, 4, 20))
        self.assertEqual(date2-date1, datetime.timedelta(2986))
