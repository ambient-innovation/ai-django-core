from django.test import TestCase

from ai_django_core.utils.string import slugify_file_name


class UtilsStringTest(TestCase):

    def test_slugify_file_name_regular(self):
        filename = 'hola and hello.txt'
        slug = slugify_file_name(filename)
        self.assertEqual(slug, 'hola_and_hello.txt')

    def test_slugify_file_name_nothing_to_slugify(self):
        filename = 'hola.txt'
        slug = slugify_file_name(filename)
        self.assertEqual(slug, filename)

    def test_slugify_file_name_max_length(self):
        filename = 'a very long filename.txt'
        slug = slugify_file_name(filename, 6)
        self.assertEqual(slug, 'a_very.txt')
