from unittest import mock

from django.contrib.auth.models import User

from ai_django_core.admin.model_admins.mixins import DeactivatableChangeViewAdminMixin
from ai_django_core.tests.mixins import RequestProviderMixin
from django.contrib import admin
from django.http import HttpResponseRedirect

from django.test import TestCase


class TestAdmin(DeactivatableChangeViewAdminMixin, admin.ModelAdmin):
    pass


class DeactivatableChangeViewAdminMixinTest(RequestProviderMixin, TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        # Use random model for this meta test
        cls.admin = TestAdmin(admin_site=None, model=User)
        cls.user = User.objects.create(username="test_user", is_superuser=False)
        cls.super_user = User.objects.create(username="super_user", is_superuser=True)

    def setUp(self) -> None:
        super().setUp()
        self.admin.enable_change_view = True

    def test_can_see_change_view_positive_flag(self):
        self.assertTrue(self.admin.can_see_change_view(request=self.get_request()))

    def test_can_see_change_view_negative_flag(self):
        self.admin.enable_change_view = False
        self.assertFalse(self.admin.can_see_change_view(request=self.get_request()))

    def test_get_list_display_links_can_see_method_called(self):
        with mock.patch.object(self.admin, 'can_see_change_view', return_value=True) as mock_method:
            self.admin.get_list_display_links(request=self.get_request(user=self.user), list_display=('first_name',))

        mock_method.assert_called_once()

    def test_get_list_display_links_can_see_method_positive_flag(self):
        field_tuple = ('first_name',)
        self.assertEqual(list(field_tuple),
                         self.admin.get_list_display_links(request=self.get_request(user=self.user),
                                                           list_display=field_tuple))

    def test_get_list_display_links_can_see_method_negative_flag(self):
        self.admin.enable_change_view = False
        self.assertIsNone(self.admin.get_list_display_links(request=self.get_request(user=self.user),
                                                            list_display=('first_name',)))

    def test_change_view_can_see_method_called_because_of_positive_flag(self):
        with mock.patch.object(self.admin, 'can_see_change_view', return_value=True) as mocked_can_see_method:
            with mock.patch('django.contrib.admin.ModelAdmin.change_view') as mocked_base_change_view:
                self.admin.change_view(request=self.get_request(user=self.super_user), object_id=str(self.user.id))

        mocked_can_see_method.assert_called_once()
        mocked_base_change_view.assert_called_once()

    def test_change_view_can_see_method_not_called_because_of_negative_flag(self):
        with mock.patch.object(self.admin, 'can_see_change_view', return_value=False) as mocked_can_see_method:
            with mock.patch('django.contrib.admin.ModelAdmin.change_view') as mocked_base_change_view:
                self.admin.change_view(request=self.get_request(user=self.super_user), object_id=str(self.user.id))

        mocked_can_see_method.assert_called_once()
        mocked_base_change_view.assert_not_called()

    def test_change_view_can_see_method_not_called_but_redirect(self):
        self.admin.enable_change_view = False
        result = self.admin.change_view(request=self.get_request(user=self.super_user), object_id=str(self.user.id))

        self.assertIsInstance(result, HttpResponseRedirect)
