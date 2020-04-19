# -*- coding: utf-8 -*-

import setuptools


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='pdfmole',
    version='0.0.1',
    description='Refine data from pdfminer',
    long_description=readme,
    author='Florian Schwendinger',
    author_email='FlorianSchwendinger@mx.at',
    license=license,
    packages=setuptools.find_packages(exclude=('docs', 'tests', 'vignettes', 'work')),
    install_requires=['matplotlib', 'pandas', 'pdfminer.six'],
    python_requires='>=3.6'
)

