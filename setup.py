#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io

from setuptools import setup, find_packages

description = "A Python library for working with a Data Package Registry."
with io.open('README.md') as readme:
    long_description = ''.join(
        filter(lambda x: 'https://travis-ci.org/' not in x,
               readme.readlines()))

dependencies = [
    'requests>=2.8.0',
]

setup(
    name='datapackage-registry',
    version='0.0.2',
    url='https://github.com/okfn/datapackage-registry-py',
    license='MIT',
    description=description,
    long_description=long_description,
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_dir={'datapackage_registry': 'datapackage_registry'},
    install_requires=dependencies,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
