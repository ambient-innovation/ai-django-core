# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='ai-django-core',
    version='1.0',
    author=u'Ambient Innovation GmbH',
    author_email='info@ambient-innovation.com',
    packages=find_packages(),
    url='ssh://git@gitlab.ambient-innovation.com:20141/ai/ai-django-core',
    license='BSD License',
    description='Lots of helper functions and useful widgets.',
    long_description=open('README.rst').read(),
    zip_safe=False,
)