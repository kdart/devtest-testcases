# python3

from setuptools import setup

NAME = "devtest-testcases"
VERSION = "1.0"

with open('README.md') as fo:
    LONG_DESCRIPTION = fo.read()


setup(name=NAME, version=VERSION,
  namespace_packages=["testcases"],
  packages=["testcases.examples"],
  install_requires=[
    "devtest",
  ],
  description="Base namespace package for all test cases.",
  long_description_content_type="text/markdown",
  long_description=LONG_DESCRIPTION,
  license="Apache-2.0",
  author="Keith Dart",
  author_email="keith.dart@gmail.com",
  keywords="automated tests",
  classifiers=[
    "Operating System :: POSIX",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Intended Audience :: Developers",
    "Environment :: Console",
    "Programming Language :: Python :: 3 :: Only",
  ],
)

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
