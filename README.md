[![pypi](https://img.shields.io/pypi/v/ai-django-core.svg)](https://pypi.python.org/pypi/ai-django-core/)
[![Downloads](https://pepy.tech/badge/ai-django-core)](https://pepy.tech/project/ai-django-core)
[![Documentation Status](https://readthedocs.org/projects/ai-django-core/badge/?version=latest)](https://ai-django-core.readthedocs.io/en/latest/?badge=latest)

# Disclaimer: Package was superseded by ambient-toolbox!

This package was renamed, moved and deprecated under the old name. The successor is the "**Ambient Toolbox**".
* [PyPI](https://pypi.org/project/ambient-toolbox/)
* [Migration docs](https://github.com/ambient-innovation/ambient-toolbox#migration-from-ai_django_core)

---

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

## Setup package for development

- Create a Python 3.11 virtualenv
- Activate the virtualenv (take care that you need `Scripts/activate.ps1` for Windows users instead of
  `Scripts/activate`)
- Install dependencies with `pip install .[dev,docs,view-layer,drf,graphql]`

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

## Git hooks (via pre-commit)

We use pre-push hooks to ensure that only linted code reaches our remote repository and pipelines aren't triggered in
vain.

To enable the configured pre-push hooks, you need to [install](https://pre-commit.com/) pre-commit and run once:

    pre-commit install -t pre-push -t pre-commit --install-hooks

This will permanently install the git hooks for both, frontend and backend, in your local
[`.git/hooks`](./.git/hooks) folder.
The hooks are configured in the [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

You can check whether hooks work as intended using the [run](https://pre-commit.com/#pre-commit-run) command:

    pre-commit run [hook-id] [options]

Example: run single hook

    pre-commit run ruff --all-files --hook-stage push

Example: run all hooks of pre-push stage

    pre-commit run --all-files --hook-stage push

## Update documentation

- To generate new auto-docs for new modules run: `sphinx-apidoc -o ./docs/modules/ ./ai_django_core/` (in the current
  set up an auto doc for the antivirus module is not supported due to installation and import problems. Since it might
  be removed in the future, that should be fine for now).
- To build the documentation run: `sphinx-build docs/ docs/_build/html/` or go into the **docs** folder and
  run: `make html`. Open `docs/_build/html/index.html` to see the documentation.

## Translation files

If you have added custom text, make sure to wrap it in `_()` where `_` is
gettext_lazy (`from django.utils.translation import gettext_lazy as _`).

How to create translation file:

* Navigate to `ai_django_core/ai_django_core` (the inner directory!)
* `python manage.py makemessages -l de`
* Have a look at the new/changed files within `ai_django_core/ai_django_core/locale`

How to compile translation files:

* Navigate to `ai_django_core/ai_django_core` (the inner directory!)
* `python manage.py compilemessages`
* Have a look at the new/changed files within `ai_django_core/ai_django_core/locale`

## Publish to ReadTheDocs.io

- Fetch the latest changes in GitHub mirror and push them
- Trigger new build at ReadTheDocs.io (follow instructions in admin panel at RTD) if the GitHub webhook is not yet set
  up.

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
