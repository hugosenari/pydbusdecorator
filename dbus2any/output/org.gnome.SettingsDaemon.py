'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/gnome/SettingsDaemon
* org.gnome.SettingsDaemon
* 

'''
from pydbusdecorator import DbusInterface
        
class Properties(object):
	@DbusInterface("org.freedesktop.DBus.Properties", "/org/gnome/SettingsDaemon", "org.gnome.SettingsDaemon")
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
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/org/gnome/SettingsDaemon", "org.gnome.SettingsDaemon")
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
	@DbusInterface("org.freedesktop.DBus.Peer", "/org/gnome/SettingsDaemon", "org.gnome.SettingsDaemon")
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
  
class SettingsDaemon(object):
	@DbusInterface("org.gnome.SettingsDaemon", "/org/gnome/SettingsDaemon", "org.gnome.SettingsDaemon")
	def __init__(self, *arg, **kw):
		pass
    
    
    
        @DbusMethod
	def Awake(self, *arg, **kw):
		"""
		Awake method:
		"""
		pass
    
        @DbusMethod
	def Start(self, *arg, **kw):
		"""
		Start method:
		"""
		pass
    
        @DbusSignal
	def PluginActivated(self, *arg, **kw):
		"""
		PluginActivated signal:
		
		Parameters
		----------
		name: s, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def PluginDeactivated(self, *arg, **kw):
		"""
		PluginDeactivated signal:
		
		Parameters
		----------
		name: s, direction: in,
		
		"""
		pass
  
