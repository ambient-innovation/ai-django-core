[![pypi](https://img.shields.io/pypi/v/ai-django-core.svg)](https://pypi.python.org/pypi/ai-django-core/)
[![Downloads](https://pepy.tech/badge/ai-django-core)](https://pepy.tech/project/ai-django-core)
[![Documentation Status](https://readthedocs.org/projects/ai-django-core/badge/?version=latest)](https://ai-django-core.readthedocs.io/en/latest/?badge=latest)

# Overview

This package contains various useful helper functions. You can read up on all the fancy things at
[readthedocs.io](https://ai-django-core.readthedocs.io/en/latest/index.html).

# Installation

- Install the package via pip:

  `pip install ai-django-core`

  or via pipenv:

  `pipenv install ai-django-core`

- Add module to `INSTALLED_APPS` within the main django `settings.py`:

    ````
    INSTALLED_APPS = (
        ...
        'ai_django_core',
    )
     ````

# Contribute

## Add functionality

- Clone the project locally
- Create a new branch for your feature
- Change the dependency in your requirements.txt to a local (editable) one that points to your local file system:
  `-e /Users/workspace/ai-django-core` or via pip  `pip install -e /Users/workspace/ai-django-core`
- Ensure the code passes the tests
- Create a pull request

## Run tests

- Check coverage
  ````
  pytest --cov=.
  ````

- Run tests
  ````
  pytest
  ````

## Update documentation

- To generate new auto-docs for new modules run: `sphinx-apidoc -o ./docs/modules/ ./ai_django_core/` (in the current
  set up an auto doc for the antivirus module is not supported due to installation and import problems. Since it might
  be removed in the future, that should be fine for now).
- To build the documentation run: `sphinx-build docs/ docs/_build/html/` or go into the **docs** folder and
  run: `make html`. Open `docs/_build/html/index.html` to see the documentation.

## Translation files

How to create translation file:

* Navigate to `ai_django_core/ai_django_core` (the inner directory!)
* `django-admin makemessages -l de`
* Have a look at the new/changed files within `ai_django_core/ai_django_core/locale`

How to compile translation files:

* Navigate to `ai_django_core/ai_django_core` (the inner directory!)
* `django-admin compilemessages`
* Have a look at the new/changed files within `ai_django_core/ai_django_core/locale`

## Publish to ReadTheDocs.io

- Fetch the latest changes in GitHub mirror and push them
- Trigger new build at ReadTheDocs.io (follow instructions in admin panel at RTD)

## Publish to PyPi

- Update documentation about new/changed functionality

- Update the `Changelog`

- Increment version in main `__init__.py`

- Create pull request / merge to master

- This project uses the flit package to publish to PyPI. Thus publishing should be as easy as running:
  ```
  flit publish
  ```

  To publish to TestPyPI use the following ensure that you have set up your .pypirc as
  shown [here](https://flit.readthedocs.io/en/latest/upload.html#using-pypirc) and use the following command:

  ```
  flit publish --repository testpypi
  ```
