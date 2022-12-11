from datetime import datetime

class FixedDate:
    def __init__(self, date = None):
        if date is not None:
            self._from_datetime(date)
        else:
            raise ValueError("Invalid FixedDate initialization")

    def _from_datetime(self, _datetime):
        day_of_year = _datetime.timetuple().tm_yday       # 1...
        self._from_day_of_year(day_of_year, _datetime.year)

    def _from_day_of_year(self, day_of_year: int, year: int) -> None:
        """Initialize this class with day of year and year.

        Args:
            day_of_year (int): In range 1...366
            year (int): In range 1...9999
        """
        self._month, self._day_of_month = divmod(day_of_year-1, 28)
        self._month += 1
        self._day_of_month += 1
        self._year = year

    @property
    def day_of_month(self):
        """In range 1...29"""
        return self._day_of_month

    @property
    def month(self):
        """In range 1...13"""
        return self._month

    @property
    def year(self):
        """In range 1...9999"""
        return self._year

    @property
    def is_year_day(self) -> bool:
        return self._month == 14 and self._day_of_month == 1

    # TODO: week of month
    # TODO: week of year
    # TODO: weekday
    # TODO: year quarter
