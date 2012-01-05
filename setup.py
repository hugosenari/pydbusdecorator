#!/usr/bin/env python
'''
Created on Nov 6, 2011

@author: hugosenari
'''
from distutils.core import setup


setup(name='pydbusdecorator',
      version='1.0',
      description='Python decorator for dbus interface definition',
      author='hugosenari',
      author_email='hugosenari@gmail.com',
      url='https://github.com/hugosenari/pydbusdecorator',
      packages=('pydbusdecorator',),
      requires=('dbus',),
     )