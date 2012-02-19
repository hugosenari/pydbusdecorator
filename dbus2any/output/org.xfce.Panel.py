'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/xfce/Panel
* org.xfce.Panel
* 

'''
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/org/xfce/Panel", "org.xfce.Panel")
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
	@DbusInterface("org.freedesktop.DBus.Properties", "/org/xfce/Panel", "org.xfce.Panel")
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
  
class Panel(object):
	@DbusInterface("org.xfce.Panel", "/org/xfce/Panel", "org.xfce.Panel")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Terminate(self, arg_restart, *arg, **kw):
		"""
		Terminate method:
		
		Parameters
		----------
		restart: b, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PluginEvent(self, arg_plugin_name, arg_name, arg_value, *arg, **kw):
		"""
		PluginEvent method:
		
		Parameters
		----------
		plugin_name: s, direction: in,
		name: s, direction: in,
		value: v, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def AddNewItem(self, arg_plugin_name, arg_arguments, *arg, **kw):
		"""
		AddNewItem method:
		
		Parameters
		----------
		plugin_name: s, direction: in,
		arguments: as, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def Save(self, *arg, **kw):
		"""
		Save method:
		"""
		pass
    
        @DbusMethod
	def DisplayItemsDialog(self, arg_active, *arg, **kw):
		"""
		DisplayItemsDialog method:
		
		Parameters
		----------
		active: u, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def DisplayPreferencesDialog(self, arg_active, *arg, **kw):
		"""
		DisplayPreferencesDialog method:
		
		Parameters
		----------
		active: u, direction: in,
		
		"""
		pass
  
