'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /
* org.blueman.Applet
* 

'''
from pydbusdecorator import DbusInterface, DbusMethod, DbusSignal, DbusAttr

class Applet(object):
    '''
    Applet
    
    Usage:
    ------
    
    >> myApplet = Applet()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myApplet.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myApplet.bar
    >>> myApplet.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myApplet.spam = lambda eggs: do_something(eggs)
    every time that Applet
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.blueman.Applet", "/", "org.blueman.Applet")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def RefreshServices(self, arg_path, *arg, **kw):
        """
        RefreshServices method:

        Parameters
        ----------

        path:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def CancelDeviceCreation(self, arg_adapter_path, arg_address, *arg, **kw):
        """
        CancelDeviceCreation method:

        Parameters
        ----------

        adapter_path:
            type: s,
            direction: in;
        address:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def SetPluginConfig(self, arg_plugin, arg_value, *arg, **kw):
        """
        SetPluginConfig method:

        Parameters
        ----------

        plugin:
            type: s,
            direction: in;
        value:
            type: b,
            direction: in;
        
        """
        pass
    @DbusMethod
    def CreateDevice(self, arg_adapter_path, arg_address, arg_pair, arg_time, *arg, **kw):
        """
        CreateDevice method:

        Parameters
        ----------

        adapter_path:
            type: s,
            direction: in;
        address:
            type: s,
            direction: in;
        pair:
            type: b,
            direction: in;
        time:
            type: u,
            direction: in;
        
        """
        pass
    @DbusMethod
    def QueryAvailablePlugins(self, *arg, **kw):
        """
        QueryAvailablePlugins method:

        Parameters
        ----------

        arg1:
            type: as,
            direction: out;
        
        """
        pass
    @DbusMethod
    def TransferControl(self, arg_pattern, arg_action, *arg, **kw):
        """
        TransferControl method:

        Parameters
        ----------

        pattern:
            type: s,
            direction: in;
        action:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def GetBluetoothStatus(self, *arg, **kw):
        """
        GetBluetoothStatus method:

        Parameters
        ----------

        arg1:
            type: b,
            direction: out;
        
        """
        pass
    @DbusMethod
    def ServiceProxy(self, arg_interface, arg_object_path, arg__method, arg_args, *arg, **kw):
        """
        ServiceProxy method:

        Parameters
        ----------

        interface:
            type: s,
            direction: in;
        object_path:
            type: o,
            direction: in;
        _method:
            type: s,
            direction: in;
        args:
            type: as,
            direction: in;
        
        """
        pass
    @DbusMethod
    def DisconnectDevice(self, arg_obj_path, *arg, **kw):
        """
        DisconnectDevice method:

        Parameters
        ----------

        obj_path:
            type: o,
            direction: in;
        
        """
        pass
    @DbusSignal
    def BluetoothStatusChanged(self, *arg, **kw):
        """

        BluetoothStatusChanged signal:

        Parameters
        ----------

        arg0:
            type: b,
            direction: in;
        
        """
        pass
    @DbusMethod
    def SetBluetoothStatus(self, arg_status, *arg, **kw):
        """
        SetBluetoothStatus method:

        Parameters
        ----------

        status:
            type: b,
            direction: in;
        
        """
        pass
    @DbusMethod
    def QueryPlugins(self, *arg, **kw):
        """
        QueryPlugins method:

        Parameters
        ----------

        arg1:
            type: as,
            direction: out;
        
        """
        pass
    @DbusMethod
    def TransferStatus(self, arg_pattern, *arg, **kw):
        """
        TransferStatus method:

        Parameters
        ----------

        pattern:
            type: s,
            direction: in;
        arg2:
            type: i,
            direction: out;
        
        """
        pass
    @DbusMethod
    def SetTimeHint(self, arg_time, *arg, **kw):
        """
        SetTimeHint method:

        Parameters
        ----------

        time:
            type: u,
            direction: in;
        
        """
        pass
    @DbusMethod
    def RfcommDisconnect(self, arg_device, arg_rfdevice, *arg, **kw):
        """
        RfcommDisconnect method:

        Parameters
        ----------

        device:
            type: s,
            direction: in;
        rfdevice:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def RfcommConnect(self, arg_device, arg_uuid, *arg, **kw):
        """
        RfcommConnect method:

        Parameters
        ----------

        device:
            type: s,
            direction: in;
        uuid:
            type: s,
            direction: in;
        arg3:
            type: s,
            direction: out;
        
        """
        pass
  
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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/", "org.blueman.Applet")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def Introspect(self, *arg, **kw):
        """
        Introspect method:

        Parameters
        ----------

        arg1:
            type: s,
            direction: out;
        
        """
        pass
  
