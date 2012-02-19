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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/org/gnome/network_manager_applet", "org.gnome.network_manager_applet")
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
    @DbusInterface("org.freedesktop.DBus.Properties", "/org/gnome/network_manager_applet", "org.gnome.network_manager_applet")
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
  
class network_manager_applet(object):
    '''
    network_manager_applet
    
    Usage:
    ------
    
    >> mynetwork_manager_applet = network_manager_applet()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> mynetwork_manager_applet.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = mynetwork_manager_applet.bar
    >>> mynetwork_manager_applet.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> mynetwork_manager_applet.spam = lambda eggs: do_something(eggs)
    every time that network_manager_applet
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.gnome.network_manager_applet", "/org/gnome/network_manager_applet", "org.gnome.network_manager_applet")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def ConnectTo3gNetwork(self, arg_device, *arg, **kw):
        """
        ConnectTo3gNetwork method:

        Parameters
        ----------

        device:
            type: o,
            direction: in;
        
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

        device:
            type: o,
            direction: in;
        ap:
            type: o,
            direction: in;
        
        """
        pass
    @DbusMethod
    def ConnectToHiddenNetwork(self, *arg, **kw):
        """
        ConnectToHiddenNetwork method:
        """
        pass
  
