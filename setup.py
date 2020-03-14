#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'requests']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="simonholmes001",
    author_email='simonholmesabc@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A simple API call to the pubchem database",
    entry_points={
        'console_scripts': [
            'pubchem_api=pubchem_api.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pubchem_api',
    name='pubchem_api',
    packages=find_packages(include=['pubchem_api', 'pubchem_api.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/simonholmes001/pubchem_api',
    version='1.0.1',
    zip_safe=False,
    extensions = ['sphinx.ext.autosectionlabel'],
)
