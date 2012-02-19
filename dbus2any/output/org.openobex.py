'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/openobex
* org.openobex
* 

'''
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/org/openobex", "org.openobex")
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
	@DbusInterface("org.freedesktop.DBus.Properties", "/org/openobex", "org.openobex")
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
	@DbusInterface("org.openobex.Manager", "/org/openobex", "org.openobex")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def GetVersion(self, *arg, **kw):
		"""
		GetVersion method:
		
		Parameters
		----------
		arg0: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetServerList(self, *arg, **kw):
		"""
		GetServerList method:
		
		Parameters
		----------
		arg0: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetSessionList(self, *arg, **kw):
		"""
		GetSessionList method:
		
		Parameters
		----------
		arg0: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetServerInfo(self, arg_server_object, *arg, **kw):
		"""
		GetServerInfo method:
		
		Parameters
		----------
		server_object: o, direction: in,
		arg1: a{ss}, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetSessionInfo(self, arg_session_object, *arg, **kw):
		"""
		GetSessionInfo method:
		
		Parameters
		----------
		session_object: o, direction: in,
		arg1: a{ss}, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def CreateTtyServer(self, arg_tty_dev, arg_pattern, *arg, **kw):
		"""
		CreateTtyServer method:
		
		Parameters
		----------
		tty_dev: s, direction: in,
		pattern: s, direction: in,
		server_object: o, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def CreateBluetoothServer(self, arg_source_address, arg_pattern, arg_require_pairing, *arg, **kw):
		"""
		CreateBluetoothServer method:
		
		Parameters
		----------
		source_address: s, direction: in,
		pattern: s, direction: in,
		require_pairing: b, direction: in,
		server_object: o, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def CancelSessionConnect(self, arg_session_object, *arg, **kw):
		"""
		CancelSessionConnect method:
		
		Parameters
		----------
		session_object: s, direction: in,
		arg1: b, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetUsbInterfaceInfo(self, arg_interface_number, *arg, **kw):
		"""
		GetUsbInterfaceInfo method:
		
		Parameters
		----------
		interface_number: u, direction: in,
		usb_interface: a{ss}, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def GetUsbInterfacesNum(self, *arg, **kw):
		"""
		GetUsbInterfacesNum method:
		
		Parameters
		----------
		interfaces_number: u, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def CreateTtySession(self, arg_tty_dev, arg_pattern, *arg, **kw):
		"""
		CreateTtySession method:
		
		Parameters
		----------
		tty_dev: s, direction: in,
		pattern: s, direction: in,
		session_object: o, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def CreateUsbSession(self, arg_interface_number, arg_pattern, *arg, **kw):
		"""
		CreateUsbSession method:
		
		Parameters
		----------
		interface_number: u, direction: in,
		pattern: s, direction: in,
		session_object: o, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def CreateBluetoothImagingSession(self, arg_target_address, arg_source_address, arg_bip_feature, *arg, **kw):
		"""
		CreateBluetoothImagingSession method:
		
		Parameters
		----------
		target_address: s, direction: in,
		source_address: s, direction: in,
		bip_feature: s, direction: in,
		session_object: o, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def CreateBluetoothSession(self, arg_target_address, arg_source_address, arg_pattern, *arg, **kw):
		"""
		CreateBluetoothSession method:
		
		Parameters
		----------
		target_address: s, direction: in,
		source_address: s, direction: in,
		pattern: s, direction: in,
		session_object: o, direction: out,
		
		"""
		pass
    
        @DbusSignal
	def SessionConnectError(self, *arg, **kw):
		"""
		SessionConnectError signal:
		
		Parameters
		----------
		
		    arg1: o, direction: in,
		
		    arg2: s, direction: in,
		
		    arg3: s, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SessionClosed(self, *arg, **kw):
		"""
		SessionClosed signal:
		
		Parameters
		----------
		
		    arg1: o, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SessionConnected(self, *arg, **kw):
		"""
		SessionConnected signal:
		
		Parameters
		----------
		
		    arg1: o, direction: in,
		
		"""
		pass
  
