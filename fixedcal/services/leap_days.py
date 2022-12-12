import datetime

def is_leap_year(year: int) -> bool:
    if year % 100 == 0:
        return year % 4 == 0 and year % 400 == 0
    return year % 4 == 0

def gregorian_leap_days_between(date1: datetime.date, date2: datetime.date) -> int:
    """Counts the gregorian leap days (29th Feb) between given dates.
    Count includes both ends (date1 and date2 themselves).

    Args:
        date1 (datetime.date): The beginning of the count
        date2 (datetime.date): The end of the count

    Returns:
        int: Count of the leap days.
    """
    count = 0
    if date1 > date2:
        date1, date2 = date2, date1
    days_between = (date2 - date1).days
    for plusday in range(0, days_between):
        date = date1 + datetime.timedelta(plusday)
        if is_leap_year(date.year) and date.month == 2 and date.day == 29:
            count += 1
    return count

def fixed_leap_days_between(date1: datetime.date, date2: datetime.date) -> int:
    count = 0
    if date1 > date2:
        date1, date2 = date2, date1
    days_between = (date2 - date1).days
    for plusday in range(0, days_between):
        date = date1 + datetime.timedelta(plusday)
        if is_leap_year(date.year) and date.month == 6 and date.day == 27:
            count += 1
    return count
