'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/xfce/Panel
* org.xfce.Panel
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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/org/xfce/Panel", "org.xfce.Panel")
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
    @DbusInterface("org.freedesktop.DBus.Properties", "/org/xfce/Panel", "org.xfce.Panel")
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
  
class Panel(object):
    '''
    Panel
    
    Usage:
    ------
    
    >> myPanel = Panel()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myPanel.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myPanel.bar
    >>> myPanel.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myPanel.spam = lambda eggs: do_something(eggs)
    every time that Panel
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.xfce.Panel", "/org/xfce/Panel", "org.xfce.Panel")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def Terminate(self, arg_restart, *arg, **kw):
        """
        Terminate method:

        Parameters
        ----------

        restart:
            type: b,
            direction: in;
        
        """
        pass
    @DbusMethod
    def PluginEvent(self, arg_plugin_name, arg_name, arg_value, *arg, **kw):
        """
        PluginEvent method:

        Parameters
        ----------

        plugin_name:
            type: s,
            direction: in;
        name:
            type: s,
            direction: in;
        value:
            type: v,
            direction: in;
        
        """
        pass
    @DbusMethod
    def AddNewItem(self, arg_plugin_name, arg_arguments, *arg, **kw):
        """
        AddNewItem method:

        Parameters
        ----------

        plugin_name:
            type: s,
            direction: in;
        arguments:
            type: as,
            direction: in;
        
        """
        pass
    @DbusMethod
    def Save(self, *arg, **kw):
        """
        Save method:
        """
        pass
    @DbusMethod
    def DisplayItemsDialog(self, arg_active, *arg, **kw):
        """
        DisplayItemsDialog method:

        Parameters
        ----------

        active:
            type: u,
            direction: in;
        
        """
        pass
    @DbusMethod
    def DisplayPreferencesDialog(self, arg_active, *arg, **kw):
        """
        DisplayPreferencesDialog method:

        Parameters
        ----------

        active:
            type: u,
            direction: in;
        
        """
        pass
  
