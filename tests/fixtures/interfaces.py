'''
Interfaces to test dbus_interface
Created on Dec 26, 2011

@author: hugosenari
'''
from pydbusdecorator import DbusInterface
from dbus import My_Dbus, OBJECT_PATH, OBJECT_URI, OBJECT_URI_TOO, INTERFACE

DbusInterface.dbus_lib = My_Dbus()
OBJECT_URI_OTHER = "org.test.interface.InterfaceWithAllParams"

@DbusInterface(INTERFACE, OBJECT_PATH, OBJECT_URI)
class BasicInterface(object):
    '''
    Basic interface to test DbusInterface decorator
    This class isn't extensible
    '''

@DbusInterface(INTERFACE, OBJECT_PATH, OBJECT_URI)
class BasicInterfaceWithParamInConstructor(object):
    '''
    Basic interface to test DbusInterface decorator
    '''

    def __init__(self, param):
        '''
        Constructor
        '''
        pass
    

@DbusInterface(INTERFACE, OBJECT_PATH, OBJECT_URI)
class BasicInterfaceWithKeywordsInConstructor(object):
    '''
    Basic interface to test DbusInterface decorator
    '''

    def __init__(self, keyword):
        '''
        Constructor
        '''
        pass

    

@DbusInterface(INTERFACE, OBJECT_PATH, OBJECT_URI)
class BasicInterfaceWithParamAndKeywordsInConstructor(object):
    '''
    Basic interface to test DbusInterface decorator
    '''

    def __init__(self, param, keyword):
        '''
        Constructor
        '''
        pass


@DbusInterface(iface=INTERFACE,
               path=OBJECT_PATH,
               uri=OBJECT_URI_OTHER,
               obj={"obj":"dbus_obj"},
               session={"session":"dbus_session"},
               retur={"return":"return"},
               prop_iface=OBJECT_URI_TOO,
               on_change=lambda x: x)
class InterfaceWithAllParams(object):
    '''
    Interface with all param setted
    '''
    pass


class BasicInterfaceInit(object):
    '''
    Basic interface to test DbusInterface decorator
    Now using __init__ that is extensible
    '''
    @DbusInterface(INTERFACE, OBJECT_PATH, OBJECT_URI)
    def __init__(self):
        pass
    
class ExtendingInterfaceInit(BasicInterfaceInit):
    ''' Extending BasicInterfaceInit '''
    