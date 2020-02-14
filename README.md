[![pypi](https://img.shields.io/pypi/v/ai-django-core.svg)](https://pypi.python.org/pypi/ai-django-core/)
[![Downloads](https://pepy.tech/badge/ai-django-core)](https://pepy.tech/project/ai-django-core)

# Overview:
This package contains various useful helper functions.


# Installation:
- Add a requirement to your requirements.txt:

    `ai-django-core`

- Add module to `INSTALLED_APPS`:

    `ai`

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

    `pytest --cov=ai-django-core`

- Run tests

    `pytest`

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
