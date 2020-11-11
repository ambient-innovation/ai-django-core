[![pypi](https://img.shields.io/pypi/v/ai-django-core.svg)](https://pypi.python.org/pypi/ai-django-core/)
[![Downloads](https://pepy.tech/badge/ai-django-core)](https://pepy.tech/project/ai-django-core)

# Overview:
This package contains various useful helper functions.


# Installation:
- Add a requirement to your requirements.txt:

    `ai-django-core`

- Add module to `INSTALLED_APPS`:

    `ai_django_core`

- Run migrations


# Contribute

- Clone the project locally
- Create a new branch for your feature
- Change the dependency in your requirements.txt to a local (editable) one that points to your local file system:
    ```
    -e /Users/felix/Documents/workspace/ai-django-core
    ```
- Ensure the code passes the tests
- Run:

    `python setup.py develop`

- Create a pull request

# Tests

- Check coverage

    `pytest --cov=.`

- Run tests

    `pytest`

# Documentation

## Generate HTML locally
- To generate new auto-docs for new modules run: `sphinx-apidoc -o ./docs/modules/ ./ai_django_core/ ./ai_django_core/utils/antivirus/` (in the current setup an auto doc for the anti virus module is not supported due to installation and import problems. Since it might be removed in the future, that should be fine for now).
- To build the documentation run: `sphinx-build docs/ docs/_build/html/` or go into the **docs** folder and run: `make html`.
  Open `docs/_build/html/index.html` to see the documentation.

## Publish to ReadTheDocs.io

- Fetch latest changes in github mirror and push them
- Trigger new build at ReadTheDocs.io (follow instructions in admin panel at RTD)

## Publish to PyPi

- Increment version in main `__init__.py`

- Update `Changelog` in `Readme.md`

- Create pull request / merge to master

- Run:

    * Make sure you have all the required packages installed
    `pip install twine wheel`
    * Create a file in your home directory: `~/.pypirc`
    ```
    [distutils]
    index-servers=
        pypi
        testpypi

    [pypi]
    repository: https://upload.pypi.org/legacy/
    username: ambient-innovation

    [testpypi]
    repository: https://test.pypi.org/legacy/
    username: ambient-innovation
    ```
    * Empty `dist` directory
    * Create distribution
    `python setup.py sdist bdist_wheel`
    * Upload to Test-PyPi
    `twine upload --repository testpypi dist/*`
    * Check at Test-PyPi if it looks nice
    * Upload to real PyPi
    `twine upload dist/*`

# Changelog

* **3.5.0** (2020-11-10)
    * Merged package ``graphene-django-ai`` into this package and enabled graphql-specific installation with `pip install ai_django_core[graphql]`
    * Added some files for readthedocs.io and updated Readme

* **3.4.0** (2020-10-30)
    * Moved tests out of package scope
    * Updated test python version to 3.8
    * Added tests for context manager ``TempDisconnectSignal`` with test setup

* **3.3.0** (2020-10-30)
    * Merged package ``ai-drf-core`` into this package and enabled djangorestframework-specific installation with `pip install ai_django_core[drf]`
    * Added ``BaseModelSerializer`` and ``CommonInfoSerializer``
    * Incremented dependencies django and bleach to previous versions latest bugfix release

* **3.2.0** (2020-10-16)
    * Added ``AbstractPermissionMixin``, ``AbstractUserSpecificQuerySet`` and ``AbstractUserSpecificManager`` abstract managers
    * Removed deprecated antivir package
    * Added Sphinx documentation setup to package

* **3.1.0** (2020-10-14)
    * Added context manager ``TempDisconnectSignal`` to nicely disable model signals temporarily
    * Moved dev dependencies to ``extras_require`` in the setup file

* **3.0.2** (2020-10-15)
    * Imports all utils into the modules scope
    * Retranslates some docstrings into English
    * Adds tests for the log_whodid util function

* **3.0.1** (2020-10-12)
    * Added missing ``__init__.py`` file to package mail.services

* **3.0.0** (2020-09-09)
    * Breaking change: Renamed package from `ai` to `ai_django_core` to clarify dependencies for usages
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
