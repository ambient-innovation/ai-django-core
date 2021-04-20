# Changelog

* **5.1.0** (2021-04-20)
    * *Breaking change:* Fixed typo in `WhitelistEmailBackend.whitify_mail_adresses` method name. Method is now
      called `whitify_mail_addresses`
    * Moved assignment of `WhitelistEmailBackend` settings var to static methods to be able to overwrite them if needed
    * Added documentation about `WhitelistEmailBackend`
    * Added some type hinting to `WhitelistEmailBackend`
    * Added formset mixin `CountChildrenFormsetMixin`
    * Added djangorestframework field `RecursiveField`
    * Added `get_attachments()` method to `BaseEmailService` and extended constructor to accept a
      variable `attachment_list`

* **5.0.0** (2021-03-26)
    * *Breaking change:* Moved `ReadOnlyAdmin` and `EditableOnlyAdmin` to package `model_admins.classes`
      and `ReadOnlyTabularInline` to package `model_admins.inlines` to enable better structuring of new admin components
    * Fixed some inconsistencies within `ReadOnlyAdmin`, `EditableOnlyAdmin` and `ReadOnlyTabularInline` classes
    * Added `admin.views` package containing a base crispy form, and a mixin to turn any regular django view into a nice
      and cozy django admin view
    * Added an abundance of `model_admins.mixins`: `AdminCreateFormMixin`, `AdminNoInlinesForCreateMixin`
      ,`AdminRequestInFormMixin`, `FetchParentObjectInlineMixin`, `FetchObjectMixin`, `CommonInfoAdminMixin`
    * Added `RequestProviderMixin` to easily create a dummy request in unittests
    * Added support for django 3.2 and dropped support for 2.0, 2.1 and 3.0
    * Added support for Python 3.9 and dropped support for 3.5
    * Updated test python version to 3.9

* **4.2.1** (2021-03-17)
    * Added some links to setup.py for pypi
    * Added some documentation for setting up the toolbox

* **4.2.0** (2021-03-12)
    * Added ``GloballyVisibleQuerySet`` including tests and documentation
    * Added ``BaseViewSetTestMixin`` for the djangorestframework plugin
    * Fixed some typos in the documentation

* **4.1.2** (2021-03-05)
    * Added kwargs parameter to init-method of `BaseEmailServiceFactory`

* **4.1.1** (2021-03-04)
    * Fixed a bug in the documentation

* **4.1.0** (2021-02-25)
    * Added class `BaseEmailService` for easier email creation and factory `BaseEmailServiceFactory`
      for multiple (mostly personalised) emails
    * Added `html2text` as a dependency to be able to automatically process the text part of an email from the html
      template

* **4.0.2** (2021-02-24)
    * Fixed a bug in ``EmailTestService.assert_body_contains()`` method to make it work for emails NOT having an HTML
      part

* **4.0.1** (2021-01-29)
    * Optimised code of function `test_get_value_from_tuple_by_key_found()`
    * Added unittests for named tuple functions

* **4.0.0** (2020-11-10)
    * *Breaking change:* Moved view mixin ``RequestInFormKwargsMixin`` from ``mixin.forms`` to proper place
      ``mixin.views``
    * *Breaking change:* Removed string helper function ``restore_windows1252controls()``, ``number_to_text()`` and
      ``replace_link_pattern()``
    * *Breaking change:* Removed choice converter function ``get_name_by_value()`` in favour
      of ``get_value_from_tuple_by_key()``
    * *Breaking change:* Removed date converter function ``get_seconds()`` because Python 3.6 already provides
      a `total_seconds()` method
    * *Breaking change:* Removed date converter function ``get_current_datetime()`` because django already provides
      the `timezone.now()` method
    * *Breaking change:* Removed date converter function ``diff_month()`` in favour of ``date_month_delta()``
    * *Breaking change:* Merged ``converter`` package in ``utils`` package
    * *Breaking change:* Moved view-layer-based helpers to extra requirement ``view-layer``: `_FormsetMixin`,
      `FormsetUpdateViewMixin`, `FormsetCreateViewMixin`, `CrispyLayoutFormMixin`, `CustomPermissionMixin`
      , `RequestInFormKwargsMixin`
    * Simplified code of function ``float_to_string()``
    * Added type hinting to lots of helper functions
    * Updated and restructured documentation
    * Added security check for dependencies in local pipeline
    * Removed some old python 2.7 syntax

* **3.5.2** (2021-01-07)
    * Bugfix with args and kwargs in ``ReadOnlyTabularInline``

* **3.5.1** (2020-11-19)
    * Bugfix with args and kwargs in ``ClassBasedViewTestMixin``

* **3.5.0** (2020-11-10)
    * Merged package ``graphene-django-ai`` into this package and enabled graphql-specific installation
      with `pip install ai_django_core[graphql]`
    * Added some files for readthedocs.io and updated Readme

* **3.4.0** (2020-10-30)
    * Moved tests out of package scope
    * Updated test python version to 3.8
    * Added tests for context manager ``TempDisconnectSignal`` with test setup

* **3.3.0** (2020-10-30)
    * Merged package ``ai-drf-core`` into this package and enabled djangorestframework-specific installation
      with `pip install ai_django_core[drf]`
    * Added ``BaseModelSerializer`` and ``CommonInfoSerializer``
    * Incremented dependencies django and bleach to previous versions latest bugfix release

* **3.2.0** (2020-10-16)
    * Added ``AbstractPermissionMixin``, ``AbstractUserSpecificQuerySet`` and ``AbstractUserSpecificManager`` abstract
      managers
    * Removed deprecated antivir package
    * Added Sphinx documentation setup to package

* **3.1.0** (2020-10-14)
    * Added context manager ``TempDisconnectSignal`` to nicely disable model signals temporarily
    * Moved dev dependencies to ``extras_require`` in the setup file

* **3.0.2** (2020-10-15)
    * Imports all utils into the modules scope
    * Retranslated some docstrings into English
    * Adds tests for the log_whodid util function

* **3.0.1** (2020-10-12)
    * Added missing ``__init__.py`` file to package mail.services

* **3.0.0** (2020-09-09)
    * *Breaking change:*  Renamed package from `ai` to `ai_django_core` to clarify dependencies for usages
    * Finished code linting
    * Removed unused imports in antivirus util package

* **2.3.0** (2020-08-07)
    * Changed `ugettext_lazy` to `gettext_lazy` to tackle django 4.0 deprecation warnings

* **2.2.1** (2020-07-01)
    * Removed misleading inheritance of mixin `ClassBasedViewTestMixin` from `TestCase`

* **2.2.0** (2020-07-01)
    * Added response class `CustomPermissionMixin`

* **2.1.2** (2020-04-30)
    * Extended pypi documentation with classifiers

* **2.1.1** (2020-04-24)
    * Refactors open calls to use context managers
    * Refactors the test setup
    * Configures coverage
    * Adds a coverage report to the CI

* **2.1.0** (2020-04-20)
    * Removed password generator method `generate_password`
    * Renamed math method `round_up_to_decimal` to `round_up_decimal`
    * Added math method `round_to_decimal`
    * Updated metadata in setup.cfg

* **2.0.0** (2020-04-09)
    * Dropped Python 2.x support
    * Removed explicit dependency to package `mock` and using implicit one via unittest
    * Improved linting

* **1.2.14** (2020-04-06)
    * Fixed a bug with session setup in `ClassBasedViewTestMixin`

* **1.2.13** (2020-04-02)
    * Added ``DELETE`` method for testing mixing `ClassBasedViewTestMixin`

* **1.2.12** (2020-02-14)
    * Added CBV testing mixing `ClassBasedViewTestMixin`

* **1.2.11** (2020-01-28)
    * Bugfix in documentation

* **1.2.10** (2020-01-28)
    * Improved documentation

* **1.2.9** (2020-01-02)
    * Extended and improved class `AbstractScrubbingService`

* **1.2.8** (2019-12-13)
    * Added custom scrubber class `AbstractScrubbingService` to provide a helper for adding custom scrubbing logic for
      data anonymisation

* **1.2.7** (2019-07-11)
    * Added email testing class `EmailTestService` to provide a wrapper for better email unittests

* **1.2.6** (2019-07-02)
    * Added helper class `tz_today()` to provide an easy getter for a timezone-aware today

* **1.2.5** (2019-06-25)
    * Added helper class `DateHelper` to provide constants to use in djangos ORM lookup `__week_day`

* **1.2.4** (2019-05-20)
    * More refactoring on `CurrentUserMiddleware` to make it more easy to override internal functions

* **1.2.3** (2019-05-20)
    * Moved `get_current_user` function inside `CurrentUserMiddleware` as a static method to enable devs to override it

* **1.2.2** (2019-04-05)
    * Updated deployment documentation
    * Added markdown support to Readme file

* **1.2.1** (2019-03-25)
    * Fixed bug causing `CommonInfo` middleware to not set `lastmodified_by` on object creation

* **1.2.0** (2019-03-19)
    * Added `CommonInfo` middleware

* **> 1.2.0**
    * Ancient history ;)

* **1.1.8**
    * Readonly admin classes
    * Date util functions
    * Clear cache helper

* **1.1.7**
    * Settings for whitelist email services added
    * Formset mixins added

* **1.1.6**
    * Modifications to anti-virus field

* **1.1.5**
    * Updated setup.py with newer information

* **1.1.4**
    * Bleacher mixin bugfix

* **1.1.3**
    * Bleacher mixin added

* **< 1.1.3**
    * Ancient history :)
