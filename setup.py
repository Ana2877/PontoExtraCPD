# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import unittest

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

with open('README.md') as f:
    readme = f.read()

setup(
    name='convert',
    version='0.1.0',
    description='Trabalho de CPD 2018/2 - Ponto Extra',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Ana Carolina Pagnoncelli',
    author_email='acpagnoncelli@inf.ufrgs.br',
    url='https://github.com/Ana2877/PontoExtraCPD',
    license=license,
    test_suite='setup.test_suite',
    packages=find_packages(exclude=('docs','examples')),
)
