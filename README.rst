=====================================================
Python decorator for dbus interface client definition
=====================================================

Python decorators to define dbus
interface, then use it as lib.

For examples see mpris2
( https://github.com/hugosenari/mpris2 )

See also:
=========
dbus2any: Convert dbus instrospection into code
( https://github.com/hugosenari/dbus2any )


Require:
========

Python dbus


Example:
========

Import decorators
-----------------

>>> from dbusdecorator import DbusAttr, DbusInterface, DbusMethod


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


See also:
---------

dbus2any is a subproject now I created a project only for this
(https://github.com/hugosenari/dbus2any)