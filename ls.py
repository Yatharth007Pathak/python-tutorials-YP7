"""
The datetime module in Python provides classes for manipulating dates and times. 

It includes several key classes:
datetime.date: Represents a date (year, month, and day).
datetime.time: Represents a time (hour, minute, second, and microsecond).
datetime.datetime: Represents a combination of date and time.
datetime.timedelta: Represents the difference between two dates or times.
datetime.tzinfo: Base class for dealing with time zones. (Note: It's not usually used directly but is subclassed to handle time zones.)

Common Functions and Methods
datetime.date Class
datetime.date.today(): Returns the current local date.
datetime.date.fromisoformat(date_string): Creates a date object from an ISO format string.

datetime.time Class
datetime.time(hour, minute, second, microsecond): Creates a time object.

datetime.datetime Class
datetime.datetime.now(): Returns the current local date and time.
datetime.datetime.utcnow(): Returns the current UTC date and time.
datetime.datetime.fromtimestamp(timestamp): Converts a timestamp (seconds since the epoch) to a datetime object.
datetime.datetime.strptime(date_string, format): Parses a string into a datetime object based on the given format.
datetime.datetime.strftime(format): Formats a datetime object as a string based on the given format.

datetime.timedelta Class
datetime.timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks): Represents a duration.
"""

import datetime

# Working with datetime.date
today = datetime.date.today()
print(f"Today's date: {today}")

# Create a specific date
specific_date = datetime.date(2024, 8, 27)
print(f"Specific date: {specific_date}")

# Working with datetime.time
current_time = datetime.datetime.now().time()
print(f"Current time: {current_time}")

# Create a specific time
specific_time = datetime.time(14, 30, 45)
print(f"Specific time: {specific_time}")

# Working with datetime.datetime
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Convert timestamp to datetime
timestamp = datetime.datetime.now().timestamp()
print(f"Current timestamp: {timestamp}")
converted_datetime = datetime.datetime.fromtimestamp(timestamp)
print(f"Converted datetime from timestamp: {converted_datetime}")

# Parse a string into a datetime object
date_string = "2024-08-27 14:30:00"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed datetime: {parsed_datetime}")

# Format datetime object as a string
formatted_date = now.strftime("%A, %d %B %Y %I:%M%p")
print(f"Formatted date: {formatted_date}")

# Working with datetime.timedelta
delta = datetime.timedelta(days=5, hours=3)
future_date = now + delta
print(f"Future date and time: {future_date}")

# Subtract two dates
past_date = datetime.date(2024, 8, 20)
difference = today - past_date
print(f"Difference between today and past_date: {difference.days} days")

'''
datetime.date.today(): Gets the current date.
datetime.date(year, month, day): Creates a specific date.
datetime.time(hour, minute, second): Creates a specific time.
datetime.datetime.now(): Gets the current date and time.
datetime.datetime.fromtimestamp(timestamp): Converts a timestamp to a datetime object.
datetime.datetime.strptime(date_string, format): Parses a string to create a datetime object.
datetime.datetime.strftime(format): Formats a datetime object as a string.
datetime.timedelta(days, hours): Represents a time difference.
datetime.date subtraction returns a timedelta object, which can be used to determine the difference in days between two dates.
'''