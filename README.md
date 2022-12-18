# FixedCal

[![CI](https://github.com/PyryL/fixedcal/actions/workflows/main.yml/badge.svg)](https://github.com/PyryL/fixedcal/actions)
[![codecov](https://codecov.io/gh/PyryL/fixedcal/branch/main/graph/badge.svg?token=ZMYYLBUPNA)](https://codecov.io/gh/PyryL/fixedcal)
[![GitHub](https://img.shields.io/github/license/PyryL/fixedcal)](LICENSE)

Python package for international fixed calendar dates.

## What is that?

International fixed calendar is an alternative calendar system.
It divides year into 13 even months by adding a month called Sol between June and July.
Each month starts with Sunday and has exactly 28 days or 4 weeks.
An additional _year day_ is added to the end of the year and it does not belong to any of the months and has no weekday.
You can read more about IFC on [Wikipedia](https://en.wikipedia.org/wiki/International_Fixed_Calendar).

## Installation

This package is available via PyPI:

```
pip install fixedcal
```

You can also download the package directly from [releases](https://github.com/PyryL/fixedcal/releases).

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

# From fixed day of month, month and year
fixed_date = FixedDate(day=24, month=4, year=2022)

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

### Leap day

Leap day occurres on the same years as in Gregorian calendar. However, the placement of that day is different: after the last day of June and before the first day of Sol (17th June in Gregorian). The following properties are given by `FixedDate` for leap day:

* `day_of_year` = 169
* `day_of_month` = 29
* `month` = 6
* `is_leap_day` = True
* `is_leap_year` = True
* `week_of_month` = 4
* `weekday` = None
* `week_of_year` = 24
* `year_quarter` = 2

## Contributing

Yes, you can contribute in the development of this package. If you find a bug or have a feature request, please file an [issue](https://github.com/PyryL/fixedcal/issues/new). You can also modify the code yourself and create a pull request.

You need [Poetry](https://python-poetry.org/) to manage the development environment. After downloading the source code of this package, run `poetry install` to install development dependencies and to set up a compatible Python environment.

Please check the following topics before creating a pull request:

* Your changes should not create new Pylint errors.
* There should be proper unit tests included in the pull request. This consists of high branch coverage (>90%) and quality of the tests. Working with dates has a lot of corner cases and tests are the best way to avoid bugs.
* The structure of the project should remain healthy: split the code between modules and packages.
