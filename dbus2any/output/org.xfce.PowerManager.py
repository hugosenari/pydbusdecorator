'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/xfce/PowerManager
* org.xfce.PowerManager
* 

'''
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/org/xfce/PowerManager", "org.xfce.PowerManager")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Introspect(self, *arg, **kw):
		"""
		Introspect method:
		
		Parameters
		----------
		data: s, direction: out,
		
		"""
		pass
  
class Properties(object):
	@DbusInterface("org.freedesktop.DBus.Properties", "/org/xfce/PowerManager", "org.xfce.PowerManager")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Get(self, arg_interface, arg_propname, *arg, **kw):
		"""
		Get method:
		
		Parameters
		----------
		interface: s, direction: in,
		propname: s, direction: in,
		value: v, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def Set(self, arg_interface, arg_propname, arg_value, *arg, **kw):
		"""
		Set method:
		
		Parameters
		----------
		interface: s, direction: in,
		propname: s, direction: in,
		value: v, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def GetAll(self, arg_interface, *arg, **kw):
		"""
		GetAll method:
		
		Parameters
		----------
		interface: s, direction: in,
		props: a{sv}, direction: out,
		
		"""
		pass
  
class Manager(object):
	@DbusInterface("org.xfce.Power.Manager", "/org/xfce/PowerManager", "org.xfce.PowerManager")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def GetInfo(self, *arg, **kw):
		"""
		GetInfo method:
		
		Parameters
		----------
		name: s, direction: out,
		version: s, direction: out,
		vendor: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetConfig(self, *arg, **kw):
		"""
		GetConfig method:
		
		Parameters
		----------
		config: a{ss}, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def Restart(self, *arg, **kw):
		"""
		Restart method:
		"""
		pass
    
        @DbusMethod
	def Quit(self, *arg, **kw):
		"""
		Quit method:
		"""
		pass
  
