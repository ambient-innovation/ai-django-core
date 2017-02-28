# -*- coding: UTF-8 -*-
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
from django.utils.timezone import utc
import time

def add_months(sourcedate, months):
    return sourcedate + relativedelta(months=months)


def add_days(sourcedate, days):
    return sourcedate + relativedelta(days=days)

def add_minutes(sourcedate, minutes):
    return sourcedate + relativedelta(minutes=minutes)

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


def get_seconds(string_time):
    duration = time.strptime(string_time, "%H:%M:%S")

    hour = duration.tm_hour
    min = duration.tm_min
    sec = duration.tm_sec
    ##### CONVERT TO SECONDS
    total_seconds = ((hour*60) + min)*60 + sec

    return total_seconds


def get_time_from_seconds(seconds):
    ### CONVERT TO TIME
    new_hor = int(seconds/3600)
    new_minu = int((seconds-(new_hor*3600))/60)
    new_seg = seconds-((new_hor*3600)+(new_minu*60))
    result = "%02d:%02d:%02d" % (new_hor, new_minu,new_seg)
    return result
