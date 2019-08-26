#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# TODO: This doesn't work, circular imports
# from howmanywinsdoesbrucebochyhave.__version__ import __version__

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name="howmanywinsdoesbrucebochyhave",
    version="0.1.0",
    description="Source code for the website 'howmanywinsdoesbrucebochyhave.com'",
    author="Mike Dougherty",
    author_email="mike.dougherty@gmail.com",
    url="https://github.com/mikedougherty/howmanywinsdoesbrucebochyhave",
    packages=["howmanywinsdoesbrucebochyhave"],
    package_dir={"howmanywinsdoesbrucebochyhave": "howmanywinsdoesbrucebochyhave"},
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    keywords="howmanywinsdoesbrucebochyhave",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
