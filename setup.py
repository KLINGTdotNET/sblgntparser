#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

def load_readme():
    with open('README.rst') as f:
        return f.read()

# http://pythonhosted.org/setuptools/setuptools.html#developer-s-guide
setup(
    name = "sblgntparser",
    version = "0.3.3",
    packages = ["sblgntparser"],

    install_requires = [],
    package_data = {
        'sblgntparser': ['*.json']
    },

    tests_require = ['pytest'],
    cmdclass = {
        'test': PyTest,
    },

    # metadata
    author = "Andreas Linz",
    author_email = "klingt.net@gmail.com",
    description = "This packages provides a python 3 parser and tools for the SBL Greek New Testament format.",
    long_description = load_readme(),
    license = "MIT",
    keywords = "sblgnt parser",
    url = "https://github.com/KLINGTdotNET/sblgntparser",
    download_url = "https://github.com/KLINGTdotNET/sblgntparser/archive/0.1.tar.gz",
)