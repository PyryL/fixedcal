# FixedCal

[![CI](https://github.com/PyryL/fixedcal/actions/workflows/main.yml/badge.svg)](https://github.com/PyryL/fixedcal/actions)

Python package for international fixed calendar dates.

## What is that?

International fixed calendar is an alternative calendar system.
It divides year into 13 even months by adding a month called Sol between June and July.
Each month starts with Sunday and has exactly 28 days or 4 weeks.
An additional _year day_ is added to the end of the year and it does not belong to any of the months and has no weekday.
You can read more about IFC on [Wikipedia](https://en.wikipedia.org/wiki/International_Fixed_Calendar).

## Usage

### Date initialization

```python3
from fixedcal import FixedDate

# Date of today
fixed_date = FixedDate.today()

# From native datetime
from datetime import datetime
february_seventh = datetime(2022, 2, 7)
fixed_date = FixedDate(february_seventh)

# From day's ordinal in year
fixed_date = FixedDate(day_of_year=107, year=2022)
```

### Date's properties

```python3
from fixedcal import FixedDate
from datetime import datetime
fixed_date = FixedDate(datetime(2022, 8, 12))

fixed_date.datetime       # datetime(2022, 8, 12, 0, 0, 0)
fixed_date.day_of_year    # 224
fixed_date.day_of_month   # 28
fixed_date.month          # 8
fixed_date.year           # 2022
fixed_date.is_year_day    # False
fixed_date.week_of_month  # 4
fixed_date.weekday        # 7
fixed_date.week_of_year   # 32
fixed_date.year_quarter   # 3
```

### Date's operations

```python3
from fixedcal import FixedDate
from datetime import datetime, timedelta
fixed_date = FixedDate(datetime(2022, 12, 6))
jan_first = FixedDate(datetime(2023, 1, 1))

new_fixed = fixed_date + timedelta(3) # FixedDate 3 days ahead
new_fixed = fixed_date - timedelta(2) # FixedDate 2 days before
new_fixed = jan_first - fixed_date    # timedelta between dates

fixed_date == fixed_date              # True
fixed_date != jan_first	              # True
jan_first < fixed_date                # False
```

### Year day

Year day is the day after the last of December and before the first of January (December 31st Gregorian).
For that date, `FixedDate` gives the following property values.

* `day_of_year` = 365 (366 on leap years)
* `day_of_month` = 29
* `month` = 13
* `year` is obviously the ending year
* `is_year_day` = True
* `week_of_month` = 4
* `weekday` = None
* `week_of_year` = 52
* `year_quarter` = 4

### Leap day

In IFC the leap year is defined in the same way as in the Gregorian system.
The leap day is, however, placed after the last of June and before the first of Sol (June 17th Gregorian).
`FixedDate` gives the following property values for leap day.

* `day_of_year` = 169
* `day_of_month` = 29
* `month` = 6
* `year` the year
* `is_leap_day` = True
* `week_of_month` = 4
* `weekday` = None
* `week_of_year` = 24
* `year_quarter` = 2
