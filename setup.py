# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='aptronics',
    version=version,
    description='Aptronics Custom Application',
    author='Hemant',
    author_email='hemant@aptronics.co.za',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
