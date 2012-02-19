'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /org/xfce/FileManager
* org.xfce.FileManager
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
    @DbusInterface("org.freedesktop.DBus.Introspectable", "/org/xfce/FileManager", "org.xfce.FileManager")
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
    @DbusInterface("org.freedesktop.DBus.Properties", "/org/xfce/FileManager", "org.xfce.FileManager")
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
  
class FileManager(object):
    '''
    FileManager
    
    Usage:
    ------
    
    >> myFileManager = FileManager()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myFileManager.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myFileManager.bar
    >>> myFileManager.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myFileManager.spam = lambda eggs: do_something(eggs)
    every time that FileManager
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.xfce.FileManager", "/org/xfce/FileManager", "org.xfce.FileManager")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def CreateFileFromTemplate(self, arg_parent_directory, arg_template_uri, arg_display, arg_startup_id, *arg, **kw):
        """
        CreateFileFromTemplate method:

        Parameters
        ----------

        parent_directory:
            type: s,
            direction: in;
        template_uri:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def CreateFile(self, arg_parent_directory, arg_content_type, arg_display, arg_startup_id, *arg, **kw):
        """
        CreateFile method:

        Parameters
        ----------

        parent_directory:
            type: s,
            direction: in;
        content_type:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def RenameFile(self, arg_filename, arg_display, arg_startup_id, *arg, **kw):
        """
        RenameFile method:

        Parameters
        ----------

        filename:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def LaunchFiles(self, arg_working_directory, arg_filenames, arg_display, arg_startup_id, *arg, **kw):
        """
        LaunchFiles method:

        Parameters
        ----------

        working_directory:
            type: s,
            direction: in;
        filenames:
            type: as,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def UnlinkFiles(self, arg_working_directory, arg_filenames, arg_display, arg_startup_id, *arg, **kw):
        """
        UnlinkFiles method:

        Parameters
        ----------

        working_directory:
            type: s,
            direction: in;
        filenames:
            type: as,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def LinkInto(self, arg_working_directory, arg_source_filenames, arg_target_filename, arg_display, arg_startup_id, *arg, **kw):
        """
        LinkInto method:

        Parameters
        ----------

        working_directory:
            type: s,
            direction: in;
        source_filenames:
            type: as,
            direction: in;
        target_filename:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def MoveInto(self, arg_working_directory, arg_source_filenames, arg_target_filename, arg_display, arg_startup_id, *arg, **kw):
        """
        MoveInto method:

        Parameters
        ----------

        working_directory:
            type: s,
            direction: in;
        source_filenames:
            type: as,
            direction: in;
        target_filename:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def CopyInto(self, arg_working_directory, arg_source_filenames, arg_target_filename, arg_display, arg_startup_id, *arg, **kw):
        """
        CopyInto method:

        Parameters
        ----------

        working_directory:
            type: s,
            direction: in;
        source_filenames:
            type: as,
            direction: in;
        target_filename:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def CopyTo(self, arg_working_directory, arg_source_filenames, arg_target_filenames, arg_display, arg_startup_id, *arg, **kw):
        """
        CopyTo method:

        Parameters
        ----------

        working_directory:
            type: s,
            direction: in;
        source_filenames:
            type: as,
            direction: in;
        target_filenames:
            type: as,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def DisplayPreferencesDialog(self, arg_display, arg_startup_id, *arg, **kw):
        """
        DisplayPreferencesDialog method:

        Parameters
        ----------

        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def Execute(self, arg_working_directory, arg_uri, arg_files, arg_display, arg_startup_id, *arg, **kw):
        """
        Execute method:

        Parameters
        ----------

        working_directory:
            type: s,
            direction: in;
        uri:
            type: s,
            direction: in;
        files:
            type: as,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def Launch(self, arg_uri, arg_display, arg_startup_id, *arg, **kw):
        """
        Launch method:

        Parameters
        ----------

        uri:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def DisplayFileProperties(self, arg_uri, arg_display, arg_startup_id, *arg, **kw):
        """
        DisplayFileProperties method:

        Parameters
        ----------

        uri:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def DisplayFolderAndSelect(self, arg_uri, arg_filename, arg_display, arg_startup_id, *arg, **kw):
        """
        DisplayFolderAndSelect method:

        Parameters
        ----------

        uri:
            type: s,
            direction: in;
        filename:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def DisplayFolder(self, arg_uri, arg_display, arg_startup_id, *arg, **kw):
        """
        DisplayFolder method:

        Parameters
        ----------

        uri:
            type: s,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def DisplayChooserDialog(self, arg_uri, arg_open, arg_display, arg_startup_id, *arg, **kw):
        """
        DisplayChooserDialog method:

        Parameters
        ----------

        uri:
            type: s,
            direction: in;
        open:
            type: b,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
  
class Thunar(object):
    '''
    Thunar
    
    Usage:
    ------
    
    >> myThunar = Thunar()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myThunar.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myThunar.bar
    >>> myThunar.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myThunar.spam = lambda eggs: do_something(eggs)
    every time that Thunar
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.xfce.Thunar", "/org/xfce/FileManager", "org.xfce.FileManager")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def Terminate(self, *arg, **kw):
        """
        Terminate method:
        """
        pass
    @DbusMethod
    def BulkRename(self, arg_working_directory, arg_filenames, arg_standalone, arg_display, arg_startup_id, *arg, **kw):
        """
        BulkRename method:

        Parameters
        ----------

        working_directory:
            type: s,
            direction: in;
        filenames:
            type: as,
            direction: in;
        standalone:
            type: b,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
  
class Trash(object):
    '''
    Trash
    
    Usage:
    ------
    
    >> myTrash = Trash()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myTrash.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myTrash.bar
    >>> myTrash.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myTrash.spam = lambda eggs: do_something(eggs)
    every time that Trash
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("org.xfce.Trash", "/org/xfce/FileManager", "org.xfce.FileManager")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    
    @DbusMethod
    def QueryTrash(self, *arg, **kw):
        """
        QueryTrash method:

        Parameters
        ----------

        full:
            type: b,
            direction: out;
        
        """
        pass
    @DbusMethod
    def MoveToTrash(self, arg_filenames, arg_display, arg_startup_id, *arg, **kw):
        """
        MoveToTrash method:

        Parameters
        ----------

        filenames:
            type: as,
            direction: in;
        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def EmptyTrash(self, arg_display, arg_startup_id, *arg, **kw):
        """
        EmptyTrash method:

        Parameters
        ----------

        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusMethod
    def DisplayTrash(self, arg_display, arg_startup_id, *arg, **kw):
        """
        DisplayTrash method:

        Parameters
        ----------

        display:
            type: s,
            direction: in;
        startup_id:
            type: s,
            direction: in;
        
        """
        pass
    @DbusSignal
    def TrashChanged(self, *arg, **kw):
        """

        TrashChanged signal:

        Parameters
        ----------

        arg1:
            type: b,
            direction: in;
        
        """
        pass
  
