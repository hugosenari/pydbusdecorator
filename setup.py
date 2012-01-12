#!/usr/bin/env python
'''
Created on Nov 6, 2011

@author: hugosenari
'''

from distutils.core import setup

setup(name='pydbusdecorator',
      version='1.0',
      description='Python decorator for dbus interface client definition',
      author='hugosenari',
      author_email='hugosenari@gmail.com',
      url='https://github.com/hugosenari/pydbusdecorator',
      keywords = ["dbus"],
      packages=('pydbusdecorator',),
      requires=('dbus',),
      license = "GPL",
      classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: X11 Applications",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Programming Language :: Python :: 2.7",
            "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      long_description = """\
=====================================================
Python decorator for dbus interface client definition
=====================================================

Python decorators to define dbus
interface, then use it as lib.

For examples see tests or mpris2
(https://github.com/hugosenari/mpris2)


Require:
========

Python dbus


Example:
========

Import decorators
-----------------
>>> from pydbusdecorator import DbusAttr, DbusInterface, DbusMethod

Define dbus interface
---------------------

>>> @DbusInterface('org.mpris.MediaPlayer2', '/org/mpris/MediaPlayer2')
>>> class Player(object):
>>>    @DbusMethod
>>>    def Next(self):
>>>       pass
>>>    @DbusAttr
>>>    def Volume(self): 
>>>       pass
    
Use your definition
-------------------
>>> mediaplayer2 = Player(
>>>    dbus_interface_info={
>>>       'dbus_uri': 'org.mpris.MediaPlayer2.gmusicbrowser'})
>>> mediaplayer2.Next()
>>> print mediaplayer2.Volume
>>> mediaplayer2.Volume = 1
>>> print mediaplayer2.Volume # integer = 1 :P

"""
)