#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import re
from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


description = 'Version-bump your software with a single command!'

long_description = '%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst')))

setup(
    name='advbumpversion',
    version='1.2.0',
    url='https://github.com/andrivet/advbumpversion',
    packages=find_packages('.'),
    author='Sebastien Andrivet',
    author_email='sebastien@andrivet.com',
    license='MIT',
    description=description,
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'bumpversion = bumpversion:main',
            'bump2version = bumpversion:main',
            'advbumpversion = bumpversion:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ], tests_require=['pytest', 'mock']
)
