# Setup

## Default installation

Setting up and getting started with this toolbox is very simple. At first make sure you are installing the latest
version of `ai-django-core`:

* Installation via pip:

  `pip install -U ai-django-core`

* Installation via pipenv:

  `pipenv install ai-django-core`

Afterwards, include the package in your ``INSTALLED_APPS`` within your main
[django settings file](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-INSTALLED_APPS):

````
INSTALLED_APPS = (
    ...
    'ai_django_core',
)
 ````

## Installing the djangorestframework extension

If you wish to use the extensions for [djangorestframework](https://www.django-rest-framework.org/), simply install the
toolbox with the desired extension:

* Installation via pip:

  `pip install -U ai-django-core[drf]`

* Installation via pipenv:

  `pipenv install ai-django-core[drf]`

## Installing the GraphQL extension

If you wish to use the extensions for [django-graphene](https://pypi.org/project/graphene-django/), simply install the
toolbox with the desired extension:

* Installation via pip:

  `pip install -U ai-django-core[graphql]`

* Installation via pipenv:

  `pipenv install ai-django-core[graphql]`

# Installing multiple extensions

In the case that you want to install more than one extension, just chain the extension with a comma:

* Installation via pip:

  `pip install -U ai-django-core[drf,graphql]`

* Installation via pipenv:

  `pipenv install ai-django-core[drf,graphql]`
