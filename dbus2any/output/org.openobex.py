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
from pydbusdecorator import DbusInterface, DbusMethod, DbusSignal, DbusAttr

class Introspectable(object):
    '''
    Introspectable
    
    Usage:
    ------
    
    >> myIntrospectable = Introspectable()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myIntrospectable.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myIntrospectable.bar
    >>> myIntrospectable.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myIntrospectable.spam = lambda eggs: do_something(eggs)
    every time that Introspectable
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/org/openobex", "org.openobex")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def Introspect(self, *arg, **kw):
        """
        Introspect method:

        Parameters
        ----------

        data:
            type: s,
            direction: out;
        
        """
        pass
  
class Properties(object):
    '''
    Properties
    
    Usage:
    ------
    
    >> myProperties = Properties()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myProperties.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myProperties.bar
    >>> myProperties.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myProperties.spam = lambda eggs: do_something(eggs)
    every time that Properties
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.freedesktop.DBus.Properties", "/org/openobex", "org.openobex")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def Get(self, arg_interface, arg_propname, *arg, **kw):
        """
        Get method:

        Parameters
        ----------

        interface:
            type: s,
            direction: in;
        propname:
            type: s,
            direction: in;
        value:
            type: v,
            direction: out;
        
        """
        pass
    @DbusMethod
    def Set(self, arg_interface, arg_propname, arg_value, *arg, **kw):
        """
        Set method:

        Parameters
        ----------

        interface:
            type: s,
            direction: in;
        propname:
            type: s,
            direction: in;
        value:
            type: v,
            direction: in;
        
        """
        pass
    @DbusMethod
    def GetAll(self, arg_interface, *arg, **kw):
        """
        GetAll method:

        Parameters
        ----------

        interface:
            type: s,
            direction: in;
        props:
            type: a{sv},
            direction: out;
        
        """
        pass
  
class Manager(object):
    '''
    Manager
    
    Usage:
    ------
    
    >> myManager = Manager()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myManager.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myManager.bar
    >>> myManager.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myManager.spam = lambda eggs: do_something(eggs)
    every time that Manager
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.openobex.Manager", "/org/openobex", "org.openobex")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def GetVersion(self, *arg, **kw):
        """
        GetVersion method:

        Parameters
        ----------

        arg0:
            type: s,
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetServerList(self, *arg, **kw):
        """
        GetServerList method:

        Parameters
        ----------

        arg0:
            type: as,
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetSessionList(self, *arg, **kw):
        """
        GetSessionList method:

        Parameters
        ----------

        arg0:
            type: as,
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetServerInfo(self, arg_server_object, *arg, **kw):
        """
        GetServerInfo method:

        Parameters
        ----------

        server_object:
            type: o,
            direction: in;
        arg1:
            type: a{ss},
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetSessionInfo(self, arg_session_object, *arg, **kw):
        """
        GetSessionInfo method:

        Parameters
        ----------

        session_object:
            type: o,
            direction: in;
        arg1:
            type: a{ss},
            direction: out;
        
        """
        pass
    @DbusMethod
    def CreateTtyServer(self, arg_tty_dev, arg_pattern, *arg, **kw):
        """
        CreateTtyServer method:

        Parameters
        ----------

        tty_dev:
            type: s,
            direction: in;
        pattern:
            type: s,
            direction: in;
        server_object:
            type: o,
            direction: out;
        
        """
        pass
    @DbusMethod
    def CreateBluetoothServer(self, arg_source_address, arg_pattern, arg_require_pairing, *arg, **kw):
        """
        CreateBluetoothServer method:

        Parameters
        ----------

        source_address:
            type: s,
            direction: in;
        pattern:
            type: s,
            direction: in;
        require_pairing:
            type: b,
            direction: in;
        server_object:
            type: o,
            direction: out;
        
        """
        pass
    @DbusMethod
    def CancelSessionConnect(self, arg_session_object, *arg, **kw):
        """
        CancelSessionConnect method:

        Parameters
        ----------

        session_object:
            type: s,
            direction: in;
        arg1:
            type: b,
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetUsbInterfaceInfo(self, arg_interface_number, *arg, **kw):
        """
        GetUsbInterfaceInfo method:

        Parameters
        ----------

        interface_number:
            type: u,
            direction: in;
        usb_interface:
            type: a{ss},
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetUsbInterfacesNum(self, *arg, **kw):
        """
        GetUsbInterfacesNum method:

        Parameters
        ----------

        interfaces_number:
            type: u,
            direction: out;
        
        """
        pass
    @DbusMethod
    def CreateTtySession(self, arg_tty_dev, arg_pattern, *arg, **kw):
        """
        CreateTtySession method:

        Parameters
        ----------

        tty_dev:
            type: s,
            direction: in;
        pattern:
            type: s,
            direction: in;
        session_object:
            type: o,
            direction: out;
        
        """
        pass
    @DbusMethod
    def CreateUsbSession(self, arg_interface_number, arg_pattern, *arg, **kw):
        """
        CreateUsbSession method:

        Parameters
        ----------

        interface_number:
            type: u,
            direction: in;
        pattern:
            type: s,
            direction: in;
        session_object:
            type: o,
            direction: out;
        
        """
        pass
    @DbusMethod
    def CreateBluetoothImagingSession(self, arg_target_address, arg_source_address, arg_bip_feature, *arg, **kw):
        """
        CreateBluetoothImagingSession method:

        Parameters
        ----------

        target_address:
            type: s,
            direction: in;
        source_address:
            type: s,
            direction: in;
        bip_feature:
            type: s,
            direction: in;
        session_object:
            type: o,
            direction: out;
        
        """
        pass
    @DbusMethod
    def CreateBluetoothSession(self, arg_target_address, arg_source_address, arg_pattern, *arg, **kw):
        """
        CreateBluetoothSession method:

        Parameters
        ----------

        target_address:
            type: s,
            direction: in;
        source_address:
            type: s,
            direction: in;
        pattern:
            type: s,
            direction: in;
        session_object:
            type: o,
            direction: out;
        
        """
        pass
    @DbusSignal
    def SessionConnectError(self, *arg, **kw):
        """

        SessionConnectError signal:

        Parameters
        ----------

        arg1:
            type: o,
            direction: in;
        arg2:
            type: s,
            direction: in;
        arg3:
            type: s,
            direction: in;
        
        """
        pass
    @DbusSignal
    def SessionClosed(self, *arg, **kw):
        """

        SessionClosed signal:

        Parameters
        ----------

        arg1:
            type: o,
            direction: in;
        
        """
        pass
    @DbusSignal
    def SessionConnected(self, *arg, **kw):
        """

        SessionConnected signal:

        Parameters
        ----------

        arg1:
            type: o,
            direction: in;
        
        """
        pass
  
