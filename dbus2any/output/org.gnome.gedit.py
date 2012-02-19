'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/gnome/gedit
* org.gnome.gedit
* 

'''
from pydbusdecorator import DbusInterface
        
class Properties(object):
	@DbusInterface("org.freedesktop.DBus.Properties", "/org/gnome/gedit", "org.gnome.gedit")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Get(self, arg_interface_name, arg_property_name, *arg, **kw):
		"""
		Get method:
		
		Parameters
		----------
		interface_name: s, direction: in,
		property_name: s, direction: in,
		value: v, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetAll(self, arg_interface_name, *arg, **kw):
		"""
		GetAll method:
		
		Parameters
		----------
		interface_name: s, direction: in,
		properties: a{sv}, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def Set(self, arg_interface_name, arg_property_name, arg_value, *arg, **kw):
		"""
		Set method:
		
		Parameters
		----------
		interface_name: s, direction: in,
		property_name: s, direction: in,
		value: v, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def PropertiesChanged(self, *arg, **kw):
		"""
		PropertiesChanged signal:
		
		Parameters
		----------
		interface_name: s, direction: in,
		changed_properties: a{sv}, direction: in,
		invalidated_properties: as, direction: in,
		
		"""
		pass
  
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/org/gnome/gedit", "org.gnome.gedit")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Introspect(self, *arg, **kw):
		"""
		Introspect method:
		
		Parameters
		----------
		xml_data: s, direction: out,
		
		"""
		pass
  
class Peer(object):
	@DbusInterface("org.freedesktop.DBus.Peer", "/org/gnome/gedit", "org.gnome.gedit")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Ping(self, *arg, **kw):
		"""
		Ping method:
		"""
		pass
    
        @DbusMethod
	def GetMachineId(self, *arg, **kw):
		"""
		GetMachineId method:
		
		Parameters
		----------
		machine_uuid: s, direction: out,
		
		"""
		pass
  
class CommandLine(object):
	@DbusInterface("org.gnome.gedit.CommandLine", "/org/gnome/gedit", "org.gnome.gedit")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Open(self, arg_files, arg_options, *arg, **kw):
		"""
		Open method:
		
		Parameters
		----------
		files: as, direction: in,
		options: a{sv}, direction: in,
		wait_id: u, direction: out,
		
		"""
		pass
    
        @DbusSignal
	def WaitDone(self, *arg, **kw):
		"""
		WaitDone signal:
		
		Parameters
		----------
		wait_id: u, direction: in,
		
		"""
		pass
  
