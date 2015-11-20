#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from distutils.core import setup, Extension
import numpy


setup(name = "awchecker",
      version = '0.1',
      description = "academic writing checker",
      author = "Ulrich Eck",
      author_email = "ulrich.eck@magicvisionlab.com",
      url = "http://www.magicvisionlab.com",
      packages = find_packages('.'),
      package_data = {'awchecker' : ['rules/*']},
      license = "BSD License",
      requires=[
      ],
      #ext_modules=[Extension('awchecker.external._transformations',
      #                       ['awchecker/external/transformations.c'],
      #                       include_dirs=[numpy.get_include()])],
      zip_safe=False,
      long_description = """\
Use regular expressions to identify problems with academic writing .. based on multiple projects found on the net..""",
      classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      )
