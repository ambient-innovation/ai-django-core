import datetime


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
