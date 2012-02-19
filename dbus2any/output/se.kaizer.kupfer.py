'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /interface
* se.kaizer.kupfer
* 

'''
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/interface", "se.kaizer.kupfer")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Introspect(self, *arg, **kw):
		"""
		Introspect method:
		
		Parameters
		----------
		
		    arg1: s, direction: out,
		
		"""
		pass
  
class Listener(object):
	@DbusInterface("se.kaizer.kupfer.Listener", "/interface", "se.kaizer.kupfer")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def ExecuteFile(self, arg_filepath, *arg, **kw):
		"""
		ExecuteFile method:
		
		Parameters
		----------
		filepath: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PutText(self, arg_text, *arg, **kw):
		"""
		PutText method:
		
		Parameters
		----------
		text: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PutFiles(self, arg_fileuris, *arg, **kw):
		"""
		PutFiles method:
		
		Parameters
		----------
		fileuris: as, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ShowHide(self, *arg, **kw):
		"""
		ShowHide method:
		"""
		pass
    
        @DbusMethod
	def GetBoundKeys(self, *arg, **kw):
		"""
		GetBoundKeys method:
		
		Parameters
		----------
		
		    arg1: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def Quit(self, *arg, **kw):
		"""
		Quit method:
		"""
		pass
    
        @DbusMethod
	def PutTextOnDisplay(self, arg_text, arg_display, arg_notify_id, *arg, **kw):
		"""
		PutTextOnDisplay method:
		
		Parameters
		----------
		text: s, direction: in,
		display: ay, direction: in,
		notify_id: ay, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def RelayKeysFromDisplay(self, arg_keystring, arg_display, arg_notify_id, *arg, **kw):
		"""
		RelayKeysFromDisplay method:
		
		Parameters
		----------
		keystring: s, direction: in,
		display: ay, direction: in,
		notify_id: ay, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PresentOnDisplay(self, arg_display, arg_notify_id, *arg, **kw):
		"""
		PresentOnDisplay method:
		
		Parameters
		----------
		display: ay, direction: in,
		notify_id: ay, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ExecuteFileOnDisplay(self, arg_filepath, arg_display, arg_notify_id, *arg, **kw):
		"""
		ExecuteFileOnDisplay method:
		
		Parameters
		----------
		filepath: s, direction: in,
		display: ay, direction: in,
		notify_id: ay, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def Present(self, *arg, **kw):
		"""
		Present method:
		"""
		pass
    
        @DbusMethod
	def PutFilesOnDisplay(self, arg_fileuris, arg_display, arg_notify_id, *arg, **kw):
		"""
		PutFilesOnDisplay method:
		
		Parameters
		----------
		fileuris: as, direction: in,
		display: ay, direction: in,
		notify_id: ay, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BoundKeyChanged(self, *arg, **kw):
		"""
		BoundKeyChanged signal:
		
		Parameters
		----------
		keystr: s, direction: in,
		is_bound: b, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PresentWithStartup(self, arg_notify_id, *arg, **kw):
		"""
		PresentWithStartup method:
		
		Parameters
		----------
		notify_id: ay, direction: in,
		
		"""
		pass
  
