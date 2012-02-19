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
from pydbusdecorator import DbusInterface, DbusMethod, DbusSignal, DbusAttr

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
    @DbusInterface("org.freedesktop.DBus.Properties", "/org/gnome/SettingsDaemon", "org.gnome.SettingsDaemon")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def Get(self, arg_interface_name, arg_property_name, *arg, **kw):
        """
        Get method:

        Parameters
        ----------

        interface_name:
            type: s,
            direction: in;
        property_name:
            type: s,
            direction: in;
        value:
            type: v,
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetAll(self, arg_interface_name, *arg, **kw):
        """
        GetAll method:

        Parameters
        ----------

        interface_name:
            type: s,
            direction: in;
        properties:
            type: a{sv},
            direction: out;
        
        """
        pass
    @DbusMethod
    def Set(self, arg_interface_name, arg_property_name, arg_value, *arg, **kw):
        """
        Set method:

        Parameters
        ----------

        interface_name:
            type: s,
            direction: in;
        property_name:
            type: s,
            direction: in;
        value:
            type: v,
            direction: in;
        
        """
        pass
    @DbusSignal
    def PropertiesChanged(self, *arg, **kw):
        """

        PropertiesChanged signal:

        Parameters
        ----------

        interface_name:
            type: s,
            direction: in;
        changed_properties:
            type: a{sv},
            direction: in;
        invalidated_properties:
            type: as,
            direction: in;
        
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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/org/gnome/SettingsDaemon", "org.gnome.SettingsDaemon")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def Introspect(self, *arg, **kw):
        """
        Introspect method:

        Parameters
        ----------

        xml_data:
            type: s,
            direction: out;
        
        """
        pass
  
class Peer(object):
    '''
    Peer
    
    Usage:
    ------
    
    >> myPeer = Peer()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myPeer.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myPeer.bar
    >>> myPeer.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myPeer.spam = lambda eggs: do_something(eggs)
    every time that Peer
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.freedesktop.DBus.Peer", "/org/gnome/SettingsDaemon", "org.gnome.SettingsDaemon")
    def __init__(self, *arg, **kw):
        '''Constructor'''
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

        machine_uuid:
            type: s,
            direction: out;
        
        """
        pass
  
class SettingsDaemon(object):
    '''
    SettingsDaemon
    
    Usage:
    ------
    
    >> mySettingsDaemon = SettingsDaemon()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> mySettingsDaemon.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = mySettingsDaemon.bar
    >>> mySettingsDaemon.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> mySettingsDaemon.spam = lambda eggs: do_something(eggs)
    every time that SettingsDaemon
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.gnome.SettingsDaemon", "/org/gnome/SettingsDaemon", "org.gnome.SettingsDaemon")
    def __init__(self, *arg, **kw):
        '''Constructor'''
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

        name:
            type: s,
            direction: in;
        
        """
        pass
    @DbusSignal
    def PluginDeactivated(self, *arg, **kw):
        """

        PluginDeactivated signal:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
        
        """
        pass
  
