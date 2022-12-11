import unittest
from datetime import datetime, timedelta
from fixedcal import FixedDate

class TestLeapYear(unittest.TestCase):
    def test_leap_year_detection_with_simple_noleap(self):
        # 2022 is not divisible of four -> not a leap year
        fixed_date = FixedDate(datetime(2022, 5, 4))
        self.assertFalse(fixed_date.is_leap_year)

    def test_leap_year_detection_with_complex_noleap(self):
        # 1900 is divisible of four but also by 100 and not by 400 -> not a leap year
        fixed_date = FixedDate(datetime(1900, 5, 4))
        self.assertFalse(fixed_date.is_leap_year)

    def test_leap_year_detection_with_common_leap_year(self):
        # 2024 is divisible of four but not by 100 -> leap year
        fixed_date = FixedDate(datetime(2024, 5, 4))
        self.assertTrue(fixed_date.is_leap_year)

    def test_leap_year_detection_with_centurial_leap_year(self):
        # 2000 is divisible of all four, 100 and 400 -> leap year
        fixed_date = FixedDate(datetime(2000, 5, 4))
        self.assertTrue(fixed_date.is_leap_year)

    def test_fixed_date_difference_over_gregorian_leap_day(self):
        # in Gregorian system there are 7 days between,
        # but in IFC the leap day is at the end of June
        # and thus the difference should be just 6 days
        date1 = FixedDate(datetime(2024, 2, 25))
        date2 = FixedDate(datetime(2024, 3, 3))
        self.assertEqual(date2-date1, timedelta(6))

    def test_fixed_date_difference_over_fixed_leap_day(self):
        # in Gregorian system there are 7 days between,
        # but in IFC the leap day is also in between
        # and therefore the difference should be 8 days
        date1 = FixedDate(datetime(2024, 6, 27))
        date2 = FixedDate(datetime(2024, 7, 4))
        self.assertEqual(date2-date1, timedelta(8))

    def test_fixed_date_difference_with_itself_gregorian_leap_day(self):
        date = FixedDate(datetime(2024, 2, 29))
        self.assertEqual(date-date, timedelta(0))

    def test_fixed_date_difference_with_itself_fixed_leap_day(self):
        date = FixedDate(datetime(2024, 6, 27))
        self.assertEqual(date-date, timedelta(0))

    def test_fixed_date_difference_over_both_leap_days(self):
        # day count should be the same in both systems
        date1 = FixedDate(datetime(2024, 2, 15))
        date2 = FixedDate(datetime(2024, 8, 3))
        self.assertEqual(date2-date1, timedelta(170))

    def test_fixed_date_difference_over_multiple_leap_days(self):
        # there are 3 Gregorian and 2 fixed leap days between
        # difference is 2987 days in Gregorian including Greg leap days
        date1 = FixedDate(datetime(2020, 2, 15))
        date2 = FixedDate(datetime(2028, 4, 20))
        self.assertEqual(date2-date1, timedelta(2986))
