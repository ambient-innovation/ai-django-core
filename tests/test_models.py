import datetime
from unittest.mock import PropertyMock, patch

from django.test import TestCase
from freezegun import freeze_time

from testapp.models import CommonInfoBasedModel


class CommonInfoTest(TestCase):
    @freeze_time('2022-06-26 10:00')
    def test_save_update_fields_common_fields_set(self):
        with freeze_time('2020-09-19'):
            obj = CommonInfoBasedModel.objects.create(value=1)
        obj.value = 2
        obj.save(update_fields=('value',))

        obj.refresh_from_db()
        self.assertEqual(obj.value, 2)
        self.assertEqual(obj.lastmodified_at, datetime.datetime(2022, 6, 26, 10))

    @patch('testapp.models.CommonInfoBasedModel.ALWAYS_UPDATE_FIELDS', new_callable=PropertyMock)
    @freeze_time('2022-06-26 10:00')
    def test_save_update_fields_common_fields_set_without_always_update(self, always_update_mock):
        always_update_mock.return_value = False
        with freeze_time('2020-09-19'):
            obj = CommonInfoBasedModel.objects.create(value=1)
        obj.value = 2
        obj.save(update_fields=('value',))

        obj.refresh_from_db()
        self.assertEqual(obj.value, 2)
        self.assertEqual(obj.lastmodified_at, datetime.datetime(2020, 9, 19))

    @freeze_time('2022-06-26 10:00')
    def test_save_common_fields_set_without_update_fields(self):
        with freeze_time('2020-09-19'):
            obj = CommonInfoBasedModel.objects.create(value=1)
        obj.value = 2
        obj.save()

        obj.refresh_from_db()
        self.assertEqual(obj.value, 2)
        self.assertEqual(obj.lastmodified_at, datetime.datetime(2022, 6, 26, 10))
