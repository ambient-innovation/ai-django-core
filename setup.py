#!/usr/bin/env python
import ast
import re

from setuptools import find_packages, setup

# Dependencies
requirements = [
    'django-crispy-forms>=1.4.0',
    'Django>=2.0.0',
    'bleach>=1.4.2',
    'python-dateutil>=2.5.3',
]

# Parse version
_version_re = re.compile(r"__version__\s+=\s+(.*)")
with open("ai_django_core/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

setup(
    name='ai-django-core',
    version=version,
    author='Ambient Innovation: GmbH',
    author_email='hello@ambient-innovation.com',
    packages=find_packages(),
    include_package_data=True,
    license="The MIT License (MIT)",
    description='Lots of helper functions and useful widgets.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    zip_safe=False,
    install_requires=requirements,
    extras_require={
        'dev': [
            'freezegun',
            'pytest-cov',
            'pytest-django',
            'pytest-mock',
            'sphinx',
            'recommonmark',
            'sphinx-rtd-theme',
        ],
    },
)
