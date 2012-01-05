'''
Class for test extending class

Created on Jan 4, 2012

@author: hugosenari
'''

from pydbusdecorator import DbusInterface, DbusMethod, DbusAttr
from dbus import My_Dbus, OBJECT_PATH, OBJECT_URI, INTERFACE

DbusInterface.dbus_lib = My_Dbus()
class SomeReturnType(object):
    """
    My return type
    """
    
    def __init__(self, value):
        self.valeu = value

class AnotherReturnType(SomeReturnType):
    """
    My anther return type
    """
    pass

class BasicInterface(object):
    '''
    Basic interface to test DbusInterface decorator
    Now using __init__ that is extensible
    '''
    @DbusInterface(INTERFACE, OBJECT_PATH, OBJECT_URI)
    def __init__(self):
        pass
    
    @DbusMethod
    def parentMethod(self, *args, **kw):
        pass
    
    @DbusMethod
    def bothMethod(self, *args, **kw):
        pass
    
    @DbusAttr
    def parentAttr(self, *args, **kw):
        pass
    
    @DbusAttr
    def bothAttr(self, *args, **kw):
        pass
    
class ExtendingInterface(BasicInterface):
    ''' Extending BasicInterfaceInit '''
    
    @DbusMethod(produces=SomeReturnType)
    def childMethod(self, *args, **kw):
        pass
    
    @DbusMethod(produces=SomeReturnType)
    def bothMethod(self, *args, **kw):
        pass
    
    @DbusAttr(produces=SomeReturnType)
    def childAttr(self, *args, **kw):
        pass
    
    @DbusAttr(produces=SomeReturnType)
    def bothAttr(self, *args, **kw):
        pass