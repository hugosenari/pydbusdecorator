'''
Created on Dec 28, 2011

@author: hugosenari
'''
from mockito import mock, when
from pydbusdecorator import DbusInterface

RESPONSE = {'sausage' : 'spam',
        'eggs' : 'spam spam',
        'spam' : 'spam spam spam'}

ANOTHER_RESPONSE = {'spam' : 'sausage',
                'spamspam' : 'eggs',
                'spamspamsapm' : 'spam'}

INTERFACE = "org.test.interface"
OBJECT_PATH = "/org/test/interface"
OBJECT_URI = "org.test.interface.Basic"
OBJECT_URI_TOO = "org.test.interface.BasicToo"


class My_Interface(mock):
    def __init__(self, *args, **kw):
        super(My_Interface, self).__init__()
        self.response = RESPONSE

    def Get(self, *args, **kw):
        return self.response 
    
    def Set(self, iface, attr, val, *args, **kw):
        self.response = val

class My_Dbus_Object(mock):
    def __init__(self, *args, **kw):
        super(My_Dbus_Object, self).__init__()
        
    def get_dbus_method(self, member, dbus_interface=None):
        def fake_dbus_method(*args, **kw):
            return kw.get('fake_dbus_method_answer', None) or\
                DbusInterface.store_result(self)
        return fake_dbus_method

class My_Dbus(object):
    '''
    My dbus mock
    '''
    def __init__(self, *args, **kw):
        self.SessionBus = mock()
        session = mock()
        obj = My_Dbus_Object()
        
        when(session).get_object(OBJECT_URI, OBJECT_PATH).thenReturn(obj)
        when(session).get_object(OBJECT_URI_TOO, OBJECT_PATH).thenReturn(obj)
        when(self.SessionBus).get_session().thenReturn(session)

        self.Interface = My_Interface
        
