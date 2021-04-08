# Tests

## Unit-testing for mails

// todo tbr

[Link to blog entry](https://medium.com/ambient-innovation/thorough-and-reliable-unit-testing-of-emails-in-django-5f34901b1b16)

## Mixins

### ClassBasedViewTestMixin

// todo tbr

### RequestProviderMixin

In many cases you will find yourself in the position that you need a request in your unittests. A wise programmer will
of course try to avoid looping the request object through all services - but from time to time you just end up with a
well written method which takes the request as a parameter.

For these cases the toolbox provides a handy mixin, from which you can easily derive your test class. Then you will be
able to use a method called `get_request(user=None)`. If you specify a user, he/she will be the request user.

````
from django.test import TestCase
from ai_django_core.tests.mixins import RequestProviderMixin


class MyAwesomeTest(RequestProviderMixin, TestCase):

    def test_something_with_a_request_without_a_user(self):
        request = self.get_request(None)
        ...

    def test_something_with_a_request_having_a_user(self):
        ...
        request = self.get_request(user=my_user)
        ...

````
