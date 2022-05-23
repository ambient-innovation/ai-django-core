from unittest import mock

from django.test import TestCase

from testapp.models import ModelWithCleanMixin


class CleanOnSaveMixinTest(TestCase):
    def test_clean_is_called(self):
        obj = ModelWithCleanMixin()
        with mock.patch.object(obj, 'clean') as mocked_method:
            obj.save()

        mocked_method.assert_called_once()
