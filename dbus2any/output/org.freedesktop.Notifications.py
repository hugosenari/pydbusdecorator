'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/freedesktop/Notifications
* org.freedesktop.Notifications
* 

'''
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/org/freedesktop/Notifications", "org.freedesktop.Notifications")
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
	@DbusInterface("org.freedesktop.DBus.Properties", "/org/freedesktop/Notifications", "org.freedesktop.Notifications")
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
  
class Notifications(object):
	@DbusInterface("org.freedesktop.Notifications", "/org/freedesktop/Notifications", "org.freedesktop.Notifications")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def GetServerInformation(self, *arg, **kw):
		"""
		GetServerInformation method:
		
		Parameters
		----------
		return_name: s, direction: out,
		return_vendor: s, direction: out,
		return_version: s, direction: out,
		return_spec_version: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetCapabilities(self, *arg, **kw):
		"""
		GetCapabilities method:
		
		Parameters
		----------
		return_caps: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def CloseNotification(self, arg_id, *arg, **kw):
		"""
		CloseNotification method:
		
		Parameters
		----------
		id: u, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def Notify(self, arg_app_name, arg_id, arg_icon, arg_summary, arg_body, arg_actions, arg_hints, arg_timeout, *arg, **kw):
		"""
		Notify method:
		
		Parameters
		----------
		app_name: s, direction: in,
		id: u, direction: in,
		icon: s, direction: in,
		summary: s, direction: in,
		body: s, direction: in,
		actions: as, direction: in,
		hints: a{sv}, direction: in,
		timeout: i, direction: in,
		return_id: u, direction: out,
		
		"""
		pass
  
