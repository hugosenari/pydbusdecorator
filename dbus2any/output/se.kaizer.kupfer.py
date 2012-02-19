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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/interface", "se.kaizer.kupfer")
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
  
class Listener(object):
    '''
    Listener
    
    Usage:
    ------
    
    >> myListener = Listener()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myListener.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myListener.bar
    >>> myListener.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myListener.spam = lambda eggs: do_something(eggs)
    every time that Listener
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("se.kaizer.kupfer.Listener", "/interface", "se.kaizer.kupfer")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def ExecuteFile(self, arg_filepath, *arg, **kw):
        """
        ExecuteFile method:

        Parameters
        ----------

        filepath:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def PutText(self, arg_text, *arg, **kw):
        """
        PutText method:

        Parameters
        ----------

        text:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def PutFiles(self, arg_fileuris, *arg, **kw):
        """
        PutFiles method:

        Parameters
        ----------

        fileuris:
            type: as,
            direction: in;
        
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

        arg1:
            type: as,
            direction: out;
        
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

        text:
            type: s,
            direction: in;
        display:
            type: ay,
            direction: in;
        notify_id:
            type: ay,
            direction: in;
        
        """
        pass
    @DbusMethod
    def RelayKeysFromDisplay(self, arg_keystring, arg_display, arg_notify_id, *arg, **kw):
        """
        RelayKeysFromDisplay method:

        Parameters
        ----------

        keystring:
            type: s,
            direction: in;
        display:
            type: ay,
            direction: in;
        notify_id:
            type: ay,
            direction: in;
        
        """
        pass
    @DbusMethod
    def PresentOnDisplay(self, arg_display, arg_notify_id, *arg, **kw):
        """
        PresentOnDisplay method:

        Parameters
        ----------

        display:
            type: ay,
            direction: in;
        notify_id:
            type: ay,
            direction: in;
        
        """
        pass
    @DbusMethod
    def ExecuteFileOnDisplay(self, arg_filepath, arg_display, arg_notify_id, *arg, **kw):
        """
        ExecuteFileOnDisplay method:

        Parameters
        ----------

        filepath:
            type: s,
            direction: in;
        display:
            type: ay,
            direction: in;
        notify_id:
            type: ay,
            direction: in;
        
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

        fileuris:
            type: as,
            direction: in;
        display:
            type: ay,
            direction: in;
        notify_id:
            type: ay,
            direction: in;
        
        """
        pass
    @DbusSignal
    def BoundKeyChanged(self, *arg, **kw):
        """

        BoundKeyChanged signal:

        Parameters
        ----------

        keystr:
            type: s,
            direction: in;
        is_bound:
            type: b,
            direction: in;
        
        """
        pass
    @DbusMethod
    def PresentWithStartup(self, arg_notify_id, *arg, **kw):
        """
        PresentWithStartup method:

        Parameters
        ----------

        notify_id:
            type: ay,
            direction: in;
        
        """
        pass
  
