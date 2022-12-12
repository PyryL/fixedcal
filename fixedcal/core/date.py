"""Module containing class for IFC date"""

import datetime
from fixedcal.services.leap_days import is_leap_year,\
    gregorian_leap_days_between, fixed_leap_days_between

class FixedDate:
    """IFC date

    Construct the date by passing either date argument or
    both day_of_year and year arguments.

    Args:
        date (Optional[datetime.date]): Gregorian date that will be represented
        day_of_year (Optional[int]): The ordinal of the date in year. In range 1...366.
        year (Optional[int]): The year in range 1...9999.
    """

    def __init__(self,
                date: datetime.date = None,
                day_of_year: int = None,
                year: int = None) -> None:
        if isinstance(date, datetime.date):
            init_tuple = self._from_datetime(date)
        elif isinstance(day_of_year, int) and isinstance(year, int):
            init_tuple = self._from_day_of_year(day_of_year, year)
        else:
            raise ValueError("Invalid FixedDate initialization")

        self._day_of_year, self._year = init_tuple

    def _from_datetime(self, date: datetime.date) -> tuple:
        """Initialize this class with native datetime object.

        Args:
            date (datetime.date): _description_

        Returns:
            tuple: day of year (1...366) and year (1...9999) in a tuple
        """
        day_of_year = date.timetuple().tm_yday
        return self._from_day_of_year(day_of_year, date.year)

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
    def today(cls) -> "FixedDate":
        """Initialize fixed date representing today.

        Returns:
            FixedDate: Today as fixed date.
        """
        return FixedDate(date=datetime.date.today())

    @property
    def is_leap_year(self) -> bool:
        """Whether the year of this date is leap year.

        Returns:
            bool: Is this leap year
        """
        return is_leap_year(self._year)

    @property
    def is_leap_day(self) -> bool:
        """Whether this fixed date is a leap day (June 29th in fixed) of IFC system.

        Returns:
            bool: Whether this is a leap day
        """
        return self.is_leap_year and self._day_of_year == 169

    @property
    def date(self) -> datetime.date:
        """Construct a native date object from fixed date.

        Returns:
            datetime.date: Native date equal to the fixed date.
        """
        return datetime.date(self.year, 1, 1) + datetime.timedelta(self._day_of_year-1)

    @property
    def day_of_year(self) -> int:
        """Ordinal of the day in year. In range 1...366.

        Returns:
            int: Ordinal in year.
        """
        return self._day_of_year

    @property
    def day_of_month(self):
        """In range 1...29"""
        if self.is_leap_day or self.is_year_day:
            return 29
        if self.is_leap_year and self.day_of_year > 169: # leap day past this year
            return ((self._day_of_year-2) % 28) + 1
        return ((self._day_of_year-1) % 28) + 1

    @property
    def month(self):
        """In range 1...13"""
        if self.is_leap_day:
            return 6
        if self.is_year_day:
            return 13
        return ((self._day_of_year-1) // 28) + 1

    @property
    def year(self):
        """In range 1...9999"""
        return self._year

    @property
    def is_year_day(self) -> bool:
        """Whether the day is year day.

        Returns:
            bool: Is the day year day
        """
        if self.is_leap_year:
            return self._day_of_year == 366
        return self._day_of_year == 365

    @property
    def week_of_month(self) -> int:
        """The ordinal of the week in month.

        Returns:
            int: In range 1...4
        """
        if self.is_leap_day or self.is_year_day:
            return 4
        return ((self.day_of_month-1) // 7) + 1

    @property
    def weekday(self) -> int:
        """Ordinal of the day in week. Value 1 for year day.

        Returns:
            Optional[int]: 1 for Sunday, 2 for Monday, 7 for Saturday
            None for leap day and year day.
        """
        if self.is_leap_day or self.is_year_day:
            return None
        return ((self.day_of_month-1) % 7) + 1

    @property
    def week_of_year(self) -> int:
        """The ordinal of the week in year.

        Returns:
            int: In range 1...52
        """
        if self.is_leap_day:
            return 24
        if self.is_year_day:
            return 52
        return ((self._day_of_year-1) // 7) + 1

    @property
    def year_quarter(self) -> int:
        """Quarter of the year.

        Returns:
            int: In range 1...4
        """
        if self.is_year_day:
            return 4
        return ((self.day_of_year-1) // 91) + 1

    def __eq__(self, other: "FixedDate") -> bool:
        return self._day_of_year == other.day_of_year and self._year == other.year

    def __gt__(self, other: "FixedDate") -> bool:
        if self._year == other.year:
            return self._day_of_year > other.day_of_year
        return self._year > other.year

    def __add__(self, other: datetime.timedelta) -> "FixedDate":
        """Addition of FixedDate and timedelta.
        Does not modify this instance, but creates new one.

        Args:
            o (datetime.timedelta): The time delta that will be added.

        Returns:
            FixedDate: New FixedDate instance that will hold the new date.
        """
        new_date = self.date + other
        return FixedDate(date=new_date)

    def __sub__(self, other):
        """Subtraction of FixedDate and some other value.
        Does not modify either one of the values.

        Args:
            o (Union[FixedDate, datetime.timedelta]): The value that will be added.

        Raises:
            ValueError: Given argument was not FixedDate nor timedelta.

        Returns:
            Union[FixedDate, datetime.timedelta]: With FixedDate as argument,
            timedelta will be returned representing the difference of given fixed dates.
            With timedelta as argument, new FixedDate will be returned.
        """
        if isinstance(other, FixedDate):
            difference = self.date - other.date
            greg_leap_days = gregorian_leap_days_between(self.date, other.date)
            fixed_leap_days = fixed_leap_days_between(self.date, other.date)
            return difference + datetime.timedelta(fixed_leap_days - greg_leap_days)
        if isinstance(other, datetime.timedelta):
            new_date = self.date - other
            return FixedDate(date=new_date)
        raise ValueError("Invalid subtractor type, expected FixedDate or timedelta")

    def __str__(self) -> str:
        """String representation of fixed date.
        For year day, month is 14 and date 1.

        Returns:
            str: Date as YYYY-MM-DD
        """
        return f"{self._year:04.0f}-{self.month:02.0f}-{self.day_of_month:02.0f}"
