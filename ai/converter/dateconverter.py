# coding=utf-8
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from django.utils.timezone import utc


def add_months(sourcedate, months):
    return sourcedate + relativedelta(months=months)


def add_days(sourcedate, days):
    return sourcedate + relativedelta(days=days)


def get_next_month():
    dt = date.today()
    return add_months(dt, 1)


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def first_day_of_month(d):
    return date(d.year, d.month, 1)


def get_current_datetime():
    return datetime.datetime.utcnow().replace(tzinfo=utc)


def get_formatted_date_str(dt):
    return dt.strftime('%d.%m.%Y')
