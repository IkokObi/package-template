# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='package-template',
    version='0.0.1',
    description='Template of Python package',
    long_description=readme,
    author='Koki Obinata',
    author_email='koki.obi.321@gmail.com',
    url='https://github.com/IkokObi/package_template',
    install_requires=['numpy>=1.14'],
    packages=find_packages(exclude=('tests')),
    test_suite='tests'
)
