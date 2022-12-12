# FixedCal

[![CI](https://github.com/PyryL/fixedcal/actions/workflows/main.yml/badge.svg)](https://github.com/PyryL/fixedcal/actions)
[![codecov](https://codecov.io/gh/PyryL/fixedcal/branch/main/graph/badge.svg?token=ZMYYLBUPNA)](https://codecov.io/gh/PyryL/fixedcal)

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
import datetime
february_seventh = datetime.date(2022, 2, 7)
fixed_date = FixedDate(february_seventh)

# From day's ordinal in year
fixed_date = FixedDate(day_of_year=107, year=2022)
```

### Date's properties

```python3
from fixedcal import FixedDate
import datetime
fixed_date = FixedDate(datetime.date(2022, 8, 12))

fixed_date.date           # datetime.date(2022, 8, 12)
fixed_date.day_of_year    # 224
fixed_date.day_of_month   # 28
fixed_date.month          # 8
fixed_date.year           # 2022
fixed_date.is_year_day    # False
fixed_date.is_leap_day    # False
fixed_date.is_leap_year   # False
fixed_date.week_of_month  # 4
fixed_date.weekday        # 7
fixed_date.week_of_year   # 32
fixed_date.year_quarter   # 3
```

### Date's operations

```python3
from fixedcal import FixedDate
from datetime import date, timedelta

fixed_date = FixedDate(date(2022, 12, 6))
jan_first = FixedDate(date(2023, 1, 1))

str(fixed_date)                       # 2022-13-04

new_fixed = fixed_date + timedelta(3) # FixedDate 3 days ahead
new_fixed = fixed_date - timedelta(2) # FixedDate 2 days before
new_fixed = jan_first - fixed_date    # timedelta between dates

fixed_date == fixed_date              # True
fixed_date != jan_first	              # True
jan_first < fixed_date                # False
```

### Year day

Year day is the day after the last of December and before the first of January.
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
