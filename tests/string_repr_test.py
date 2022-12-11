import unittest
from datetime import datetime
from fixedcal import FixedDate

class TestStringRepresentation(unittest.TestCase):
    def test_string_of_ordinary_date(self):
        fixed_date = FixedDate(date=datetime(2022, 4, 15))
        self.assertEqual(str(fixed_date), "2022-04-21")

    def test_string_of_date_in_november(self):
        fixed_date = FixedDate(date=datetime(2022, 11, 11))
        self.assertEqual(str(fixed_date), "2022-12-07")

    def test_string_of_year_day(self):
        fixed_date = FixedDate(day_of_year=365, year=2022)
        self.assertEqual(str(fixed_date), "2022-13-29")
