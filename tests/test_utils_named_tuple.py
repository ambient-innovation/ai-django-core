from django.test import TestCase

from ai_django_core.utils import get_value_from_tuple_by_key, get_key_from_tuple_by_value


class UtilsNamedTupleTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.MY_CHOICE_ONE = 1
        cls.MY_CHOICE_TWO = 2
        cls.MY_CHOICE_THREE = 3

        cls.MY_CHOICE_LIST = (
            (cls.MY_CHOICE_ONE, "Choice 1"),
            (cls.MY_CHOICE_TWO, "Choice 2"),
            (cls.MY_CHOICE_THREE, "Choice 3"),
        )

    def test_get_value_from_tuple_by_key_found(self):
        self.assertEqual(get_value_from_tuple_by_key(self.MY_CHOICE_LIST, self.MY_CHOICE_TWO), 'Choice 2')

    def test_get_value_from_tuple_by_key_not_found(self):
        self.assertEqual(get_value_from_tuple_by_key(self.MY_CHOICE_LIST, 99), '-')

    def test_get_key_from_tuple_by_value_found(self):
        self.assertEqual(get_key_from_tuple_by_value(self.MY_CHOICE_LIST, 'Choice 2'), self.MY_CHOICE_TWO)

    def test_get_key_from_tuple_by_value_not_found(self):
        self.assertEqual(get_key_from_tuple_by_value(self.MY_CHOICE_LIST, 'Something odd'), '-')
