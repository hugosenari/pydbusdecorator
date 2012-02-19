'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/gnome/network_manager_applet
* org.gnome.network_manager_applet
* 

'''
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/org/gnome/network_manager_applet", "org.gnome.network_manager_applet")
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
	@DbusInterface("org.freedesktop.DBus.Properties", "/org/gnome/network_manager_applet", "org.gnome.network_manager_applet")
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
  
class network_manager_applet(object):
	@DbusInterface("org.gnome.network_manager_applet", "/org/gnome/network_manager_applet", "org.gnome.network_manager_applet")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def ConnectTo3gNetwork(self, arg_device, *arg, **kw):
		"""
		ConnectTo3gNetwork method:
		
		Parameters
		----------
		device: o, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def CreateWifiNetwork(self, *arg, **kw):
		"""
		CreateWifiNetwork method:
		"""
		pass
    
        @DbusMethod
	def ConnectTo8021xNetwork(self, arg_device, arg_ap, *arg, **kw):
		"""
		ConnectTo8021xNetwork method:
		
		Parameters
		----------
		device: o, direction: in,
		ap: o, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ConnectToHiddenNetwork(self, *arg, **kw):
		"""
		ConnectToHiddenNetwork method:
		"""
		pass
  
