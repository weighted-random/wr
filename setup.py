#!/usr/bin/env python
from setuptools import setup


with open('README.rst') as file:
    long_description = file.read()

setup(
    name='wr',
    version='0.1.1',
    url='https://github.com/waawal/wr/',
    license='LGPL',
    author='Waawal',
    author_email='waawal@boom.ws',
    description='wr is a simple, lightweight module that provides '
                'random choice based on weight',
    long_description=long_description,
    py_modules=['wr'],
    zip_safe=True,
    platforms='any',
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',

    ]
)
