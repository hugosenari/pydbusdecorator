'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/xfce/Xfconf
* org.xfce.Xfconf
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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/org/xfce/Xfconf", "org.xfce.Xfconf")
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
    @DbusInterface("org.freedesktop.DBus.Properties", "/org/xfce/Xfconf", "org.xfce.Xfconf")
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
  
class Xfconf(object):
    '''
    Xfconf
    
    Usage:
    ------
    
    >> myXfconf = Xfconf()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myXfconf.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myXfconf.bar
    >>> myXfconf.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myXfconf.spam = lambda eggs: do_something(eggs)
    every time that Xfconf
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.xfce.Xfconf", "/org/xfce/Xfconf", "org.xfce.Xfconf")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def IsPropertyLocked(self, arg_channel, arg_property, *arg, **kw):
        """
        IsPropertyLocked method:

        Parameters
        ----------

        channel:
            type: s,
            direction: in;
        property:
            type: s,
            direction: in;
        locked:
            type: b,
            direction: out;
        
        """
        pass
    @DbusMethod
    def ListChannels(self, *arg, **kw):
        """
        ListChannels method:

        Parameters
        ----------

        channels:
            type: as,
            direction: out;
        
        """
        pass
    @DbusMethod
    def ResetProperty(self, arg_channel, arg_property, arg_recursive, *arg, **kw):
        """
        ResetProperty method:

        Parameters
        ----------

        channel:
            type: s,
            direction: in;
        property:
            type: s,
            direction: in;
        recursive:
            type: b,
            direction: in;
        
        """
        pass
    @DbusMethod
    def PropertyExists(self, arg_channel, arg_property, *arg, **kw):
        """
        PropertyExists method:

        Parameters
        ----------

        channel:
            type: s,
            direction: in;
        property:
            type: s,
            direction: in;
        exists:
            type: b,
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetAllProperties(self, arg_channel, arg_property_base, *arg, **kw):
        """
        GetAllProperties method:

        Parameters
        ----------

        channel:
            type: s,
            direction: in;
        property_base:
            type: s,
            direction: in;
        properties:
            type: a{sv},
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetProperty(self, arg_channel, arg_property, *arg, **kw):
        """
        GetProperty method:

        Parameters
        ----------

        channel:
            type: s,
            direction: in;
        property:
            type: s,
            direction: in;
        value:
            type: v,
            direction: out;
        
        """
        pass
    @DbusMethod
    def SetProperty(self, arg_channel, arg_property, arg_value, *arg, **kw):
        """
        SetProperty method:

        Parameters
        ----------

        channel:
            type: s,
            direction: in;
        property:
            type: s,
            direction: in;
        value:
            type: v,
            direction: in;
        
        """
        pass
    @DbusSignal
    def PropertyRemoved(self, *arg, **kw):
        """

        PropertyRemoved signal:

        Parameters
        ----------

        arg1:
            type: s,
            direction: in;
        arg2:
            type: s,
            direction: in;
        
        """
        pass
    @DbusSignal
    def PropertyChanged(self, *arg, **kw):
        """

        PropertyChanged signal:

        Parameters
        ----------

        arg1:
            type: s,
            direction: in;
        arg2:
            type: s,
            direction: in;
        arg3:
            type: v,
            direction: in;
        
        """
        pass
  
