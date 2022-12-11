from datetime import datetime, timedelta
from math import floor

class FixedDate:
    def __init__(self, date = None, day_of_year = None, year = None):
        if date is not None:
            init_tuple = self._from_datetime(date)
        elif day_of_year is not None and year is not None:
            init_tuple = self._from_day_of_year(day_of_year, year)
        else:
            raise ValueError("Invalid FixedDate initialization")
        
        self._day_of_year, self._year = init_tuple

    def _from_datetime(self, _datetime: datetime) -> tuple:
        """Initialize this class with native datetime object.

        Args:
            _datetime (datetime): _description_

        Returns:
            tuple: day of year (1...366) and year (1...9999) in a tuple
        """
        day_of_year = _datetime.timetuple().tm_yday
        return self._from_day_of_year(day_of_year, _datetime.year)

    def _from_day_of_year(self, day_of_year: int, year: int) -> tuple:
        """Initialize this class with day of year and year.

        Args:
            day_of_year (int): In range 1...366
            year (int): In range 1...9999

        Returns:
            tuple: day of year (1...366) and year (1...9999) in a tuple
        """
        return (day_of_year, year)

    @property
    def datetime(self) -> datetime:
        """Construct a native datetime object from fixed date.

        Returns:
            datetime: Datetime equal to the fixed date.
        """
        return datetime(self.year, 1, 1) + timedelta(self._day_of_year-1)

    @property
    def day_of_year(self):
        return self._day_of_year

    @property
    def day_of_month(self):
        """In range 1...29"""
        return ((self._day_of_year-1) % 28) + 1

    @property
    def month(self):
        """In range 1...13"""
        return ((self._day_of_year-1) // 28) + 1

    @property
    def year(self):
        """In range 1...9999"""
        return self._year

    @property
    def is_year_day(self) -> bool:
        return self.month == 14 and self.day_of_month == 1

    @property
    def week_of_month(self) -> int:
        """The ordinal of the week in month. Value 1 for year day.

        Returns:
            int: In range 1...4
        """
        if self.is_year_day:
            return 1
        return ((self.day_of_month-1) // 7) + 1

    @property
    def weekday(self) -> int:
        """Ordinal of the day in week. Value 1 for year day.

        Returns:
            int: 1 for Sunday, 2 for Monday, 7 for Saturday
        """
        return ((self.day_of_month-1) % 7) + 1

    @property
    def week_of_year(self) -> int:
        """The ordinal of the week in year. Value 53 for year day.

        Returns:
            int: In range 1...53
        """
        return ((self._day_of_year-1) // 7) + 1

    @property
    def year_quarter(self) -> int:
        """Quarter of the year. Value 4 for year day.

        Returns:
            int: In range 1...4
        """
        if self.is_year_day:
            return 4
        return ((self.day_of_year-1) // 91) + 1

    # TODO: plus and minus operations
    # TODO: equatable
