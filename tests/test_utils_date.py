import calendar
import datetime

import pytz
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.timezone import make_aware
from freezegun import freeze_time

from ai_django_core.utils.date import date_month_delta, get_start_and_end_date_from_calendar_week, tz_today, \
    get_next_calendar_week, next_weekday, add_months, add_days, add_minutes, get_next_month, first_day_of_month, \
    get_formatted_date_str, get_time_from_seconds, datetime_format


class DateUtilTest(TestCase):
    TEST_CURRENT_YEAR = 2017

    def test_get_start_and_end_date_from_calendar_week(self):
        monday, sunday = get_start_and_end_date_from_calendar_week(2016, 52)
        self.assertEqual(monday, datetime.date(year=2016, month=12, day=26))

        monday, sunday = get_start_and_end_date_from_calendar_week(2018, 1)
        self.assertEqual(monday, datetime.date(year=2018, month=1, day=1))

        monday, sunday = get_start_and_end_date_from_calendar_week(2017, 30)
        self.assertEqual(monday, datetime.date(year=2017, month=7, day=24))

    def test_get_next_calendar_week_any_week(self):
        self.assertEqual(get_next_calendar_week(datetime.date(year=2020, month=9, day=19)), 39)

    def test_get_next_calendar_week_first(self):
        self.assertEqual(get_next_calendar_week(datetime.date(year=2020, month=1, day=1)), 2)

    def test_get_next_calendar_week_last(self):
        # We expect calendar week 1 (for 2021)
        self.assertEqual(get_next_calendar_week(datetime.date(year=2020, month=12, day=31)), 1)

    def test_next_weekday_any_weekday(self):
        self.assertEqual(next_weekday(datetime.date(year=2020, month=9, day=19), calendar.FRIDAY),
                         datetime.date(year=2020, month=9, day=25))

    def test_next_weekday_same_weekday(self):
        self.assertEqual(next_weekday(datetime.date(year=2020, month=9, day=19), calendar.SATURDAY),
                         datetime.date(year=2020, month=9, day=26))

    def test_date_month_delta(self):
        start_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=2, day=1)
        end_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=3, day=1)
        self.assertEqual(date_month_delta(start_date, end_date), 1)

    def test_date_month_delta_half_month(self):
        start_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=4, day=15)
        end_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=5, day=1)
        self.assertAlmostEqual(date_month_delta(start_date, end_date), 0.5, 1)

    def test_date_month_delta_one_and_a_half_month(self):
        start_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=4, day=15)
        end_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=6, day=1)
        self.assertAlmostEqual(date_month_delta(start_date, end_date), 1.5, 1)

    def test_date_month_delta_full_year(self):
        start_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=1, day=1)
        end_date = datetime.date(year=self.TEST_CURRENT_YEAR + 1, month=1, day=1)
        self.assertEqual(date_month_delta(start_date, end_date), 12)

    def test_date_month_delta_two_years(self):
        start_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=1, day=1)
        end_date = datetime.date(year=self.TEST_CURRENT_YEAR + 2, month=7, day=1)
        self.assertEqual(date_month_delta(start_date, end_date), 30)

    def test_date_month_delta_no_difference(self):
        start_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=4, day=15)
        end_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=4, day=15)
        self.assertEqual(date_month_delta(start_date, end_date), 0)

    def test_date_month_delta_one_day(self):
        start_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=4, day=15)
        end_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=4, day=16)
        self.assertEqual(date_month_delta(start_date, end_date), 1 / 30)

    def test_date_month_delta_start_greater_then_end_date(self):
        start_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=4, day=15)
        end_date = datetime.date(year=self.TEST_CURRENT_YEAR, month=4, day=14)
        with self.assertRaises(NotImplementedError):
            date_month_delta(start_date, end_date)

    @override_settings(USE_TZ=True)
    def test_tz_today_as_object_tz_active_is_tz_aware(self):
        frozen_date = make_aware(datetime.datetime(year=2019, month=9, day=19))
        with freeze_time(frozen_date):
            self.assertTrue(isinstance(tz_today(), datetime))
            self.assertEqual(tz_today(), frozen_date)

    def test_tz_today_as_object_tz_not_active(self):
        frozen_date = datetime.datetime(year=2019, month=9, day=19, hour=10)
        with freeze_time(frozen_date):
            self.assertEqual(tz_today(), frozen_date.date())

    @override_settings(USE_TZ=True)
    def test_tz_today_as_str(self):
        frozen_date = datetime.datetime(year=2019, month=9, day=19, hour=10)
        with freeze_time(frozen_date):
            self.assertEqual(tz_today('%d.%m.%Y'), '19.09.2019')

    def test_add_months_one_month(self):
        source_date = datetime.date(year=2020, month=6, day=26)
        self.assertEqual(add_months(source_date, 1), datetime.date(year=2020, month=7, day=26))

    def test_add_months_many_months(self):
        source_date = datetime.date(year=2020, month=6, day=26)
        self.assertEqual(add_months(source_date, 10), datetime.date(year=2021, month=4, day=26))

    def test_add_months_negative_months(self):
        source_date = datetime.date(year=2020, month=6, day=26)
        self.assertEqual(add_months(source_date, -2), datetime.date(year=2020, month=4, day=26))

    def test_add_days_one_day(self):
        source_date = datetime.date(year=2020, month=6, day=26)
        self.assertEqual(add_days(source_date, 1), datetime.date(year=2020, month=6, day=27))

    def test_add_days_many_days(self):
        source_date = datetime.date(year=2020, month=6, day=26)
        self.assertEqual(add_days(source_date, 10), datetime.date(year=2020, month=7, day=6))

    def test_add_days_negative_days(self):
        source_date = datetime.date(year=2020, month=6, day=26)
        self.assertEqual(add_days(source_date, -2), datetime.date(year=2020, month=6, day=24))

    def test_add_minutes_one_minute(self):
        source_datetime = datetime.datetime(year=2020, month=6, day=26, hour=8, minute=0)
        self.assertEqual(add_minutes(source_datetime, 1),
                         datetime.datetime(year=2020, month=6, day=26, hour=8, minute=1))

    def test_add_minutes_many_minutes(self):
        source_datetime = datetime.datetime(year=2020, month=6, day=26, hour=8, minute=0)
        self.assertEqual(add_minutes(source_datetime, 10),
                         datetime.datetime(year=2020, month=6, day=26, hour=8, minute=10))

    def test_add_minutes_negative_minutes(self):
        source_datetime = datetime.datetime(year=2020, month=6, day=26, hour=8, minute=0)
        self.assertEqual(add_minutes(source_datetime, -2),
                         datetime.datetime(year=2020, month=6, day=26, hour=7, minute=58))

    @freeze_time('2020-06-26')
    def test_get_next_month_regular(self):
        self.assertEqual(get_next_month(), datetime.date(year=2020, month=7, day=26))

    def test_first_day_of_month_regular(self):
        source_date = datetime.date(year=2020, month=6, day=26)
        self.assertEqual(first_day_of_month(source_date), datetime.date(year=2020, month=6, day=1))

    def test_get_formatted_date_str_regular(self):
        source_date = datetime.date(year=2020, month=6, day=26)
        self.assertEqual(get_formatted_date_str(source_date), '26.06.2020')

    def test_get_time_from_seconds_one_hour(self):
        self.assertEqual(get_time_from_seconds(3600), '01:00:00')

    def test_get_time_from_seconds_one_minute(self):
        self.assertEqual(get_time_from_seconds(60), '00:01:00')

    def test_get_time_from_seconds_big_hours(self):
        self.assertEqual(get_time_from_seconds(3600 * 99), '99:00:00')

    def test_get_time_from_seconds_huge_hours(self):
        self.assertEqual(get_time_from_seconds(3600 * 1000), '1000:00:00')

    def test_get_time_from_seconds_negative_seconds(self):
        with self.assertRaises(ValueError):
            get_time_from_seconds(-1)

    @override_settings(TIME_ZONE='UTC')
    def test_datetime_format_regular(self):
        source_date = datetime.datetime(year=2020, month=6, day=26, hour=8, tzinfo=pytz.UTC)
        self.assertEqual(datetime_format(source_date, '%d.%m.%Y %H:%M'), '26.06.2020 08:00')

    @override_settings(TIME_ZONE='Europe/Cologne')
    def test_datetime_format_wrong_timezone(self):
        source_date = datetime.datetime(year=2020, month=6, day=26, hour=8)
        self.assertEqual(datetime_format(source_date, '%d.%m.%Y %H:%M'), '26.06.2020 08:00')

    @override_settings(TIME_ZONE='Europe/Berlin')
    def test_datetime_format_different_timezone(self):
        source_date = datetime.datetime(year=2020, month=6, day=26, hour=8, tzinfo=pytz.UTC)
        self.assertEqual(datetime_format(source_date, '%d.%m.%Y %H:%M'), '26.06.2020 10:00')
