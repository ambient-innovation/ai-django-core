from typing import Union
from unittest import mock

from django.contrib.auth.models import AnonymousUser, User
from django.utils.translation import gettext_lazy as _

from ai_django_core.tests.errors import TestSetupConfigurationError
from ai_django_core.tests.mixins import RequestProviderMixin
from ai_django_core.view_layer.mixins import DjangoPermissionRequiredMixin


class BaseViewPermissionTestMixin(RequestProviderMixin):
    view_class = None
    permission_list = None
    view_kwargs = {}

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.user = cls.get_test_user()

    @classmethod
    def get_test_user(cls):
        return User.objects.create(username='test_user', email='test.user@ai-django-core.com')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if not self.view_class:
            raise TestSetupConfigurationError(_('BaseViewPermissionTestMixin used without setting a "view_class".'))

    def get_view_instance(self, *, user: Union[User, AnonymousUser], kwargs: dict = None, method: str = 'GET'):
        """
        Creates an instance of the given view class and injects a valid request.
        """
        request = self.get_request(user=user, method=method)
        view = self.view_class()
        view.kwargs = kwargs if kwargs else self.view_kwargs
        view.request = request
        return view

    def test_view_class_inherits_mixin(self):
        self.assertTrue(issubclass(self.view_class, DjangoPermissionRequiredMixin))

    def test_permissions_are_equal(self):
        # Sanity checks
        self.assertIsNotNone(self.permission_list, msg='Missing permission list declaration in test')
        self.assertIsNotNone(self.view_class.permission_list, msg='Missing permission list declaration in view')

        # Proper assertion
        self.assertEqual(self.permission_list, list(self.view_class.permission_list))

    def test_passes_login_barrier_is_called(self):
        with mock.patch.object(self.view_class, 'passes_login_barrier', return_value=False) as mock_method:
            view = self.get_view_instance(user=AnonymousUser())
            response = view.dispatch(request=view.request, **view.kwargs)
            # If a user is not logged in, he'll be forwarded to the login view
            self.assertEqual(response.status_code, 302)

        mock_method.assert_called_once()

    def test_has_permissions_is_called(self):
        with mock.patch.object(self.view_class, 'has_permissions', return_value=False) as mock_method:
            view = self.get_view_instance(user=self.user)
            response = view.dispatch(request=view.request, **view.kwargs)
            self.assertEqual(response.status_code, 403)

        mock_method.assert_called_once()
