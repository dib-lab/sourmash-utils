#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'sourmash>=2.0.0a1',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='sourmash_utils',
    version='0.1.0',
    description="Assorted sourmash scripts",
    long_description=readme + '\n\n' + history,
    author="C. Titus Brown",
    author_email='titus@idyll.org',
    url='https://github.com/dib-lab/sourmash_utils',
    packages=[
        'sourmash_utils',
    ],
    package_dir={
        'sourmash_utils': 'sourmash_utils'
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='sourmash_utils',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={"console_scripts": [
        'sourmash-utils = sourmash_utils.__main__:main'
        ]
    },
    test_suite='tests',
    tests_require=test_requirements
)
