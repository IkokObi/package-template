# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='template',
    version='0.0.1',
    description='Template package for Obinata',
    long_description=readme,
    author='Koki Obinata',
    author_email='koki.obi.321@gmail.com',
    url='https://github.com/IkokObi/package_template',
    install_requires=['numpy>=1.14'],
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)

