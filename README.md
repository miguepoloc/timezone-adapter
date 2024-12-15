# TimeZoneAdapter

A Python library that provides an easy-to-use interface for converting and manipulating datetime objects across different time zones.

[![PyPI version](https://badge.fury.io/py/timezone-adapter.svg)](https://badge.fury.io/py/timezone-adapter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/timezone-adapter.svg)](https://pypi.org/project/timezone-adapter/)

## Features

- Convert between time zones using numeric offset or timezone name
- Convert to and from UTC
- Calculate minimum and maximum dates for a specific day
- Support for both timezone offsets and timezone names (e.g., 'America/Bogota')
- Type hints support
- Zero dependencies (except pytz)

## Installation
```bash
pip install timezone-adapter
```

## Quick Start

```python
from datetime import datetime
from timezone_adapter import TimeZoneAdapter

# Using numeric offset (hours)
tz_adapter = TimeZoneAdapter(-5)  # UTC-5

# Using timezone name
tz_adapter = TimeZoneAdapter('America/Bogota')

# Convert to UTC
local_time = datetime.now()
utc_time = tz_adapter.to_utc(local_time)

# Get range of dates for today
min_date, max_date = tz_adapter.get_min_max_datetime_today()
```

## API Reference

### TimeZoneAdapter

#### `__init__(timezone: Union[int, str])`
Initialize with either a numeric offset (hours from UTC) or timezone name.

#### `to_utc(date_time: datetime) -> datetime`
Convert a local datetime to UTC.

#### `from_utc(date_time: datetime) -> datetime`
Convert a UTC datetime to local time.

#### `get_min_max_datetime_today() -> Tuple[datetime, datetime]`
Get the minimum and maximum datetime for the current day.

#### `get_min_max_datetime_by_date(date_time: datetime) -> Tuple[datetime, datetime]`
Get the minimum and maximum datetime for a specific date.

## Development

### Setup Development Environment

Clone the repository

```bash
git clone https://github.com/miguepoloc/timezone-adapter.git
cd timezone-adapter
```

Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

Install development dependencies

```bash
pip install -e ".[dev]"
```

Run tests

```bash
pytest
```


### Code Quality

We use several tools to ensure code quality:

- `black` for code formatting
- `isort` for import sorting
- `mypy` for type checking
- `flake8` for style guide enforcement

Run all checks with:

```bash
pre-commit run --all-files
```


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Miguel Angel Polo Castañeda - [@miguepoloc](https://github.com/miguepoloc)

## Acknowledgments

- Thanks to the `pytz` library for timezone support
- Inspired by the need for simpler timezone handling in Python
