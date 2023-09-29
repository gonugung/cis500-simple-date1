#######################################################
# my_date
#
# Name: Gayatri Gonuguntla
# Section: 04
#
# Fall 2023
#########################################################
import datetime as dt
def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    isDivideBy4=year % 4 == 0
    isDivideBy100=year % 100 != 0
    isDivideBy400=year % 400 == 0
    if (isDivideBy4 and isDivideBy100) or (isDivideBy400):
        return True
    else:
        return False
 
def ordinal_date(year:int , month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        daysInMonth[1] = 29
    ordinalDate = sum(daysInMonth[:month - 1]) + day
    return ordinalDate

def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    return (dt.date(year2, month2, day2) - dt.date(year1, month1, day1)).days

# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    weekDay = dt.date(year, month, day).weekday()
    global DAYS_OF_WEEK
    return DAYS_OF_WEEK[weekDay]
    
def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    str = dt.date(year, month, day).strftime("%A, %d %B %Y")
    return str
