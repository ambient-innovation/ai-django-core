from django.test import TestCase
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

from ai_django_core.tests.mixins import RequestProviderMixin
from ai_django_core.view_layer.views import ToggleView


class ToggleViewTest(RequestProviderMixin, TestCase):

    def test_http_method_set_correctly(self):
        self.assertEqual(ToggleView.http_method_names, ('post',))

    def test_post_raises_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            view = ToggleView()
            view.post(request=self.get_request())

    def test_class_inherits_from_single_object_mixin(self):
        self.assertTrue(issubclass(ToggleView, SingleObjectMixin))

    def test_class_inherits_from_generic_view(self):
        self.assertTrue(issubclass(ToggleView, View))
