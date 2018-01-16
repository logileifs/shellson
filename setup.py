#!/usr/bin/env python
from setuptools import setup

setup(
    name='shellson',
    version='0.1.0',
    description='JSON command line parser',
    author='Logi og Fjalar',
    author_email='logileifs@gmail.com',
    url='https://github.com/logileifs/shellson',
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    #package_data={'nextcode': ['VERSION']},
    install_requires=[],
    #scripts=['scripts/shellson'],
    entry_points={
        "console_scripts": [
            'shellson = shellson.shellson:main'
        ]
    }
)
