#!/usr/bin/env python
from setuptools import setup

setup(
    name='shellson',
    version='0.2.0',
    description='JSON command line parser',
    author='Logi og Fjalar',
    author_email='logileifs@gmail.com',
    url='https://github.com/logileifs/shellson',
    packages=['shellson'],
    entry_points={
        "console_scripts": [
            'shellson = shellson.__main__:main'
        ]
    }
)
