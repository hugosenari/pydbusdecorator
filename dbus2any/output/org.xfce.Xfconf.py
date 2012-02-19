'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/xfce/Xfconf
* org.xfce.Xfconf
* 

'''
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/org/xfce/Xfconf", "org.xfce.Xfconf")
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
	@DbusInterface("org.freedesktop.DBus.Properties", "/org/xfce/Xfconf", "org.xfce.Xfconf")
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
  
class Xfconf(object):
	@DbusInterface("org.xfce.Xfconf", "/org/xfce/Xfconf", "org.xfce.Xfconf")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def IsPropertyLocked(self, arg_channel, arg_property, *arg, **kw):
		"""
		IsPropertyLocked method:
		
		Parameters
		----------
		channel: s, direction: in,
		property: s, direction: in,
		locked: b, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def ListChannels(self, *arg, **kw):
		"""
		ListChannels method:
		
		Parameters
		----------
		channels: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def ResetProperty(self, arg_channel, arg_property, arg_recursive, *arg, **kw):
		"""
		ResetProperty method:
		
		Parameters
		----------
		channel: s, direction: in,
		property: s, direction: in,
		recursive: b, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PropertyExists(self, arg_channel, arg_property, *arg, **kw):
		"""
		PropertyExists method:
		
		Parameters
		----------
		channel: s, direction: in,
		property: s, direction: in,
		exists: b, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetAllProperties(self, arg_channel, arg_property_base, *arg, **kw):
		"""
		GetAllProperties method:
		
		Parameters
		----------
		channel: s, direction: in,
		property_base: s, direction: in,
		properties: a{sv}, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetProperty(self, arg_channel, arg_property, *arg, **kw):
		"""
		GetProperty method:
		
		Parameters
		----------
		channel: s, direction: in,
		property: s, direction: in,
		value: v, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def SetProperty(self, arg_channel, arg_property, arg_value, *arg, **kw):
		"""
		SetProperty method:
		
		Parameters
		----------
		channel: s, direction: in,
		property: s, direction: in,
		value: v, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def PropertyRemoved(self, *arg, **kw):
		"""
		PropertyRemoved signal:
		
		Parameters
		----------
		
		    arg1: s, direction: in,
		
		    arg2: s, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def PropertyChanged(self, *arg, **kw):
		"""
		PropertyChanged signal:
		
		Parameters
		----------
		
		    arg1: s, direction: in,
		
		    arg2: s, direction: in,
		
		    arg3: v, direction: in,
		
		"""
		pass
  
