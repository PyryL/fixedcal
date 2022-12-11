from datetime import datetime, timedelta
from fixedcal.services.leap_days import is_leap_year, gregorian_leap_days_between, fixed_leap_days_between

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

    @classmethod
    def today(self) -> "FixedDate":
        return FixedDate(date=datetime.today())

    @property
    def is_leap_year(self) -> bool:
        """Whether the year of this date is leap year.

        Returns:
            bool: Is this leap year
        """
        # if self._year % 100 == 0:
        #     return self._year % 4 == 0 and self._year % 400 == 0
        # return self._year % 4 == 0
        return is_leap_year(self._year)

    @property
    def is_leap_day(self) -> bool:
        """Whether this fixed date is a leap day (June 29th in fixed) of IFC system.

        Returns:
            bool: Whether this is a leap day
        """
        return self.is_leap_year and self._day_of_year == 169

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
        if self.is_leap_day:
            return 29
        return ((self._day_of_year-1) % 28) + 1

    @property
    def month(self):
        """In range 1...13"""
        if self.is_leap_day:
            return 6
        return ((self._day_of_year-1) // 28) + 1

    @property
    def year(self):
        """In range 1...9999"""
        return self._year

    @property
    def is_year_day(self) -> bool:
        if self.is_leap_year:
            return self.day_of_year == 366
        return self.day_of_year == 365

    @property
    def week_of_month(self) -> int:
        """The ordinal of the week in month. Value 1 for year day.

        Returns:
            int: In range 1...4
        """
        if self.is_year_day:
            return 1
        if self.is_leap_day:
            return 4
        return ((self.day_of_month-1) // 7) + 1

    @property
    def weekday(self) -> int:
        """Ordinal of the day in week. Value 1 for year day.

        Returns:
            int: 1 for Sunday, 2 for Monday, 7 for Saturday
        """
        if self.is_leap_day:
            return None
        return ((self.day_of_month-1) % 7) + 1

    @property
    def week_of_year(self) -> int:
        """The ordinal of the week in year. Value 53 for year day.

        Returns:
            int: In range 1...53
        """
        if self.is_leap_day:
            return 24
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

    def __eq__(self, o: "FixedDate") -> bool:
        return self._day_of_year == o.day_of_year and self._year == o.year

    def __gt__(self, o: "FixedDate") -> bool:
        if self._year == o.year:
            return self._day_of_year > o.day_of_year
        return self._year > o.year

    def __add__(self, o: timedelta) -> "FixedDate":
        """Addition of FixedDate and timedelta.
        Does not modify this instance, but creates new one.

        Args:
            o (timedelta): The time delta that will be added.

        Returns:
            FixedDate: New FixedDate instance that will hold the new date.
        """
        new_date = self.datetime + o
        return FixedDate(date=new_date)

    def __sub__(self, o):
        """Subtraction of FixedDate and some other value.
        Does not modify either one of the values.

        Args:
            o (Union[FixedDate, timedelta]): The value that will be added.

        Raises:
            ValueError: Given argument was not FixedDate nor timedelta.

        Returns:
            Union[FixedDate, timedelta]: With FixedDate as argument,
            timedelta will be returned representing the difference of given fixed dates.
            With timedelta as argument, new FixedDate will be returned.
        """
        if isinstance(o, FixedDate):
            difference = self.datetime - o.datetime
            greg_leap_days = gregorian_leap_days_between(self.datetime, o.datetime)
            fixed_leap_days = fixed_leap_days_between(self.datetime, o.datetime)
            return difference - timedelta(greg_leap_days) + timedelta(fixed_leap_days)
        elif isinstance(o, timedelta):
            new_date = self.datetime - o
            return FixedDate(date=new_date)
        raise ValueError("Invalid subtractor type, expected FixedDate or timedelta")

    def __str__(self) -> str:
        """String representation of fixed date.
        For year day, month is 14 and date 1.

        Returns:
            str: Date as YYYY-MM-DD
        """
        return f"{self._year:04.0f}-{self.month:02.0f}-{self.day_of_month:02.0f}"
