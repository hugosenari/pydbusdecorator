'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/xfce/SessionManager
* org.xfce.SessionManager
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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/org/xfce/SessionManager", "org.xfce.SessionManager")
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
    @DbusInterface("org.freedesktop.DBus.Properties", "/org/xfce/SessionManager", "org.xfce.SessionManager")
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
    @DbusInterface("org.xfce.Session.Manager", "/org/xfce/SessionManager", "org.xfce.SessionManager")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def Shutdown(self, arg_type, arg_allow_save, *arg, **kw):
        """
        Shutdown method:

        Parameters
        ----------

        type:
            type: u,
            direction: in;
        allow_save:
            type: b,
            direction: in;
        
        """
        pass
    @DbusMethod
    def Checkpoint(self, arg_session_name, *arg, **kw):
        """
        Checkpoint method:

        Parameters
        ----------

        session_name:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def GetState(self, *arg, **kw):
        """
        GetState method:

        Parameters
        ----------

        state:
            type: u,
            direction: out;
        
        """
        pass
    @DbusMethod
    def ListClients(self, *arg, **kw):
        """
        ListClients method:

        Parameters
        ----------

        clients:
            type: ao,
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetInfo(self, *arg, **kw):
        """
        GetInfo method:

        Parameters
        ----------

        name:
            type: s,
            direction: out;
        version:
            type: s,
            direction: out;
        vendor:
            type: s,
            direction: out;
        
        """
        pass
    @DbusSignal
    def ShutdownCancelled(self, *arg, **kw):
        """

        ShutdownCancelled signal:
        """
        pass
    @DbusSignal
    def ClientRegistered(self, *arg, **kw):
        """

        ClientRegistered signal:

        Parameters
        ----------

        arg1:
            type: s,
            direction: in;
        
        """
        pass
    @DbusSignal
    def StateChanged(self, *arg, **kw):
        """

        StateChanged signal:

        Parameters
        ----------

        arg1:
            type: u,
            direction: in;
        arg2:
            type: u,
            direction: in;
        
        """
        pass
  
