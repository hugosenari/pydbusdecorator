===========
Dbus To Any 
===========

This use dbus introspection to convert
running dbus interface into any code
defined by xslt

Xml definition file:
http://standards.freedesktop.org/dbus/1.0/introspect.dtd


Require:
========

libxslt


Usage:
======

python dbus2any.py "xslt" "bus name" "object path"


Command line example:
----------------------
>>> #this exemple require gmusicbrowser to be running
>>> python dbus2any/dbustoany.py "xslt/pydbusdecorator.xsl" "org.mpris.MediaPlayer2.gmusicbrowser" "/org/mpris/MediaPlayer2"
>>> python dbus2any/dbustoany.py "xslt/pydbusdecorator.xsl" "im.pidgin.purple.PurpleService" "/im/pidgin/purple/PurpleObject"

Code examples:
--------------
>>> from dbus2any import Dbus2Xml, Xml2Any

>>> dbus2xml = Dbus2Xml("org.mpris.MediaPlayer2.gmusicbrowser", "/org/mpris/MediaPlayer2")

>>> xml2any = Xml2Any(dbus2xml, "xslt/pydbusdecorator.xsl")

>>> print "All class: ", xml2any

