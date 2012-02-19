'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /
* org.gnome.ScreenSaver
* 

'''
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/", "org.gnome.ScreenSaver")
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
  
class ScreenSaver(object):
	@DbusInterface("org.gnome.ScreenSaver", "/", "org.gnome.ScreenSaver")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Lock(self, *arg, **kw):
		"""
		Lock method:
		"""
		pass
    
        @DbusMethod
	def SimulateUserActivity(self, *arg, **kw):
		"""
		SimulateUserActivity method:
		"""
		pass
    
        @DbusMethod
	def GetActive(self, *arg, **kw):
		"""
		GetActive method:
		
		Parameters
		----------
		value: b, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetActiveTime(self, *arg, **kw):
		"""
		GetActiveTime method:
		
		Parameters
		----------
		seconds: u, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def SetActive(self, arg_value, *arg, **kw):
		"""
		SetActive method:
		
		Parameters
		----------
		value: b, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ShowMessage(self, arg_summary, arg_body, arg_icon, *arg, **kw):
		"""
		ShowMessage method:
		
		Parameters
		----------
		summary: s, direction: in,
		body: s, direction: in,
		icon: s, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ActiveChanged(self, *arg, **kw):
		"""
		ActiveChanged signal:
		
		Parameters
		----------
		new_value: b, direction: in,
		
		"""
		pass
  
