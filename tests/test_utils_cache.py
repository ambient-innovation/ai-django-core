from django.test import TestCase

from ai_django_core.utils import clear_cache


class CacheUtilTest(TestCase):

    def test_clear_cache_pseudo(self):
        # This test just executes the method to ensure the api from django is still as we expect it to be
        clear_cache()
