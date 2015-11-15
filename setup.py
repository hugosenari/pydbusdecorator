#!/usr/bin/env python
'''
Created on Nov 6, 2011

@author: hugosenari
'''

from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(name='pydbusdecorator',
      version='1.0',
      description='Python decorator for dbus interface client definition',
      author='hugosenari',
      author_email='hugosenari@gmail.com',
      url='https://github.com/hugosenari/pydbusdecorator',
      keywords = ["dbus"],
      packages=('pydbusdecorator', 'dbusdecorator'),
      requires=(),
      license = "GPL",
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.4"
      ],
      long_description = readme
)