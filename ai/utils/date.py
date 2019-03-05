import datetime
from calendar import monthrange

from dateutil.relativedelta import relativedelta


def get_start_and_end_date_from_calendar_week(year, calendar_week):
    """
    Returns the first and last day of a given calendar week
    :param year: int
    :param calendar_week: int
    :return:
    """
    monday = datetime.datetime.strptime('{%s}-{%s}-1' % (year, calendar_week), "%Y-%W-%w").date()
    return monday, monday + datetime.timedelta(days=6.9)


def get_next_calendar_week(compare_date):
    """
    Returns the next calendar week as an integer
    :param compare_date: date
    :return:
    """
    day_in_one_week = compare_date + datetime.timedelta(days=(7 - compare_date.weekday()))
    return day_in_one_week.isocalendar()[1]


def next_weekday(d, weekday):
    """
    Returns the next date of the given weekday
    For example: next_weekday(d, calendar.MONDAY) would return the next monday starting at date "d"
    :param d: date
    :param weekday: int
    :return:
    """
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def date_month_delta(start_date: datetime.date, end_date: datetime.date):
    """
    Calculates the number of months lying between two dates.
    So from April 15th to May 1st it's 0.5 months.
    Attention: `end_date` will be excluded in the result (outer border)
    :return: float or False (if `start_date` > `end_date`)
    """

    # If `start_date` is greater, this logic doesn't make any sense
    if start_date > end_date:
        return False

    # Calculate date difference between dates
    date_diff = (end_date - start_date).days

    # Iteration variable
    delta = 0
    iter_date = start_date
    # Loop until all days are processed
    while date_diff > 0:
        # Get days of month we are currently looking at
        iter_month, iter_month_days = monthrange(iter_date.year, iter_date.month)
        # Calculate how many days are left to end of this month
        days_to_month_end = min((iter_month_days - (iter_date.day - 1)), date_diff)
        # Add percentage of the month these days cover to return variable
        delta += days_to_month_end / iter_month_days
        # Reduce leftover days by the amout we already processed
        date_diff -= days_to_month_end

        # Set iteration date to first of next month
        iter_date += relativedelta(months=1, day=1)

    # Return data
    return delta
