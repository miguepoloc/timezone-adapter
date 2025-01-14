"""
This module provides a class for converting and manipulating datetime objects based on a given timezone offset or name.
"""
from datetime import datetime, timedelta
from typing import Union

import pytz


class TimeZoneAdapter:
    """
    Provides methods for converting and manipulating datetime objects based on a given timezone offset or name.
    """

    def __init__(self, timezone_offset: Union[int, str]) -> None:
        """
        Initialize the TimeZoneAdapter with a timezone offset or name.

        Parameters:
            timezone_offset (Union[int, str]): The timezone offset or name.
        """
        self.timezone_offset: int
        if isinstance(timezone_offset, int):
            self.timezone_offset = timezone_offset
            self.timezone = pytz.FixedOffset(timezone_offset * 60)  # Convert hours to minutes
            self.today_with_timezone = datetime.now(self.timezone)
        elif isinstance(timezone_offset, str):
            self.timezone = pytz.timezone(timezone_offset)
            self.timezone_offset = self.timezone.utcoffset(datetime.now()).total_seconds() / 3600
            self.today_with_timezone = datetime.now(self.timezone)
        else:
            raise ValueError("timezone must be an int or a str")

    def is_utc(self, date_time: datetime) -> bool:
        """
        Check if a datetime object is in UTC timezone.

        Parameters:
            date_time (datetime): The datetime object to be checked.

        Returns:
            bool: True if the datetime object is in UTC timezone, False otherwise.
        """
        return date_time.tzinfo == pytz.UTC

    def to_utc(self, date_time: datetime) -> datetime:
        """
        Converts a datetime object to UTC timezone.

        Parameters:
            date_time (datetime): The datetime object to be converted.

        Returns:
            datetime: The converted datetime object in UTC timezone.

        Note:
            If the datetime object is already in UTC timezone, it is returned as is.
        """
        return date_time.astimezone(pytz.UTC)

    def from_utc(self, date_time: datetime) -> datetime:
        """
        Converts a datetime object from UTC timezone to the specified timezone.

        Parameters:
            date_time (datetime): The datetime object to be converted.

        Returns:
            datetime: The converted datetime object in the specified timezone.

        Note:
            If the datetime object is already in the specified timezone, it is returned as is.
        """
        return date_time.astimezone(self.timezone)

    def get_min_date(self, date_time: datetime) -> datetime:
        """
        Returns the minimum datetime value for the specified date in the specified timezone.

        Parameters:
            date_time (datetime): The datetime object for which the minimum datetime value needs to be calculated.

        Returns:
            datetime: The minimum datetime value for the specified date in the specified timezone.
        """
        naive_dt: datetime = datetime.combine(self.from_utc(date_time).date(), datetime.min.time()) - timedelta(
            hours=self.timezone_offset
        )
        return naive_dt.replace(tzinfo=pytz.UTC)

    def get_max_date(self, date_time: datetime) -> datetime:
        """
        Returns the maximum datetime value for the specified date in the specified timezone.

        Parameters:
            date_time (datetime): The datetime object for which the maximum datetime value needs to be calculated.

        Returns:
            datetime: The maximum datetime value for the specified date in the specified timezone.
        """
        naive_dt: datetime = datetime.combine(self.from_utc(date_time).date(), datetime.max.time()) - timedelta(
            hours=self.timezone_offset
        )
        return naive_dt.replace(tzinfo=pytz.UTC)

    def get_min_max_datetime_today(self) -> tuple[datetime, datetime]:
        """
        Returns the minimum and maximum datetime values for the current day in the specified timezone.

        Returns:
            tuple[datetime, datetime]: A tuple containing the minimum and maximum datetime values for the current day
                in the specified timezone.
        """

        today: datetime = self.today_with_timezone
        min_date: datetime = self.get_min_date(date_time=today)
        max_date: datetime = self.get_max_date(date_time=today)
        return min_date, max_date

    def get_min_max_datetime_by_date(self, date_time: datetime) -> tuple[datetime, datetime]:
        """
        Returns the minimum and maximum datetime values for the specified date in the specified timezone.

        Parameters:
            date_time (datetime): The datetime object for which the minimum and maximum datetime values need to be
                calculated.

        Returns:
            tuple[datetime, datetime]: A tuple containing the minimum and maximum datetime values for the specified date
                in the specified timezone.
        """
        min_date: datetime = self.get_min_date(date_time=date_time)
        max_date: datetime = self.get_max_date(date_time=date_time)
        return min_date, max_date
