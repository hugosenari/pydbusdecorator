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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/", "org.gnome.ScreenSaver")
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
  
class ScreenSaver(object):
    '''
    ScreenSaver
    
    Usage:
    ------
    
    >> myScreenSaver = ScreenSaver()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myScreenSaver.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myScreenSaver.bar
    >>> myScreenSaver.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myScreenSaver.spam = lambda eggs: do_something(eggs)
    every time that ScreenSaver
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.gnome.ScreenSaver", "/", "org.gnome.ScreenSaver")
    def __init__(self, *arg, **kw):
        '''Constructor'''
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

        value:
            type: b,
            direction: out;
        
        """
        pass
    @DbusMethod
    def GetActiveTime(self, *arg, **kw):
        """
        GetActiveTime method:

        Parameters
        ----------

        seconds:
            type: u,
            direction: out;
        
        """
        pass
    @DbusMethod
    def SetActive(self, arg_value, *arg, **kw):
        """
        SetActive method:

        Parameters
        ----------

        value:
            type: b,
            direction: in;
        
        """
        pass
    @DbusMethod
    def ShowMessage(self, arg_summary, arg_body, arg_icon, *arg, **kw):
        """
        ShowMessage method:

        Parameters
        ----------

        summary:
            type: s,
            direction: in;
        body:
            type: s,
            direction: in;
        icon:
            type: s,
            direction: in;
        
        """
        pass
    @DbusSignal
    def ActiveChanged(self, *arg, **kw):
        """

        ActiveChanged signal:

        Parameters
        ----------

        new_value:
            type: b,
            direction: in;
        
        """
        pass
  
