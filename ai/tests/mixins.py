from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory


class ClassBasedViewTestMixin(TestCase):
    """Test mixin for Django views"""
    factory_class = RequestFactory
    view_class = None

    @staticmethod
    def _authentication(request, user):
        request.user = user if user else AnonymousUser()

    def _get_response(self, method, user, data, url_params=None, *args):
        """Returns response."""

        # Catch case that URL does not get any params passed to
        if not url_params:
            url_params = {}

        # Create request
        factory = self.factory_class()
        req_kwargs = {}
        if data:
            req_kwargs.update({'data': data})
        req = getattr(factory, method)('/', **req_kwargs)

        # Annotate a request object with a session
        middleware = SessionMiddleware()
        middleware.process_request(req)
        req.session.save()

        # Authenticate user
        self._authentication(req, user)

        # Setup messages
        messages = FallbackStorage(req)
        setattr(req, '_messages', messages)

        # Call view
        return self.view_class.as_view()(req, *args, **url_params)

    def get(self, user=None, data=None, url_params=None, *args, **kwargs):
        """Returns response for a GET request."""
        return self._get_response('get', user, data, url_params, args, kwargs)

    def post(self, user=None, data=None, url_params=None, *args, **kwargs):
        """Returns response for a POST request."""
        return self._get_response('post', user, data, url_params, args, kwargs)

    def delete(self, user=None, data=None, url_params=None, *args, **kwargs):
        """Returns response for a DELETE request."""
        return self._get_response('delete', user, data, url_params, args, kwargs)
