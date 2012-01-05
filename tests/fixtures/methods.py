'''
Created on Dec 29, 2011

@author: hugosenari
'''

from pydbusdecorator import DbusInterface, DbusMethod
from dbus import My_Dbus, OBJECT_PATH, OBJECT_URI, INTERFACE, RESPONSE

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

def some_return_function(value):
    return AnotherReturnType(value)

def args_to_dbus(*args): return args
args_to_dbus_iter = [some_return_function]
args_to_dbus_iter_empty = []
args_to_dbus_iter_less_than_args = [some_return_function]
args_to_dbus_iter_more_than_args = [some_return_function, some_return_function, some_return_function]

def kw_to_dbus(**kw): return kw
kw_to_dbus_dict = {'my_arg':some_return_function}
kw_to_dbus_dict_empty = {}
kw_to_dbus_dict_more_than_kw = {'my_arg':some_return_function}
kw_to_dbus_dict_less_than_kw = {'my_arg':some_return_function, 'your_arg':some_return_function, 'their_arg':some_return_function}

@DbusInterface(INTERFACE, OBJECT_PATH, OBJECT_URI)
class BasicInterfaceWithMethods(object):
    """
    Basic interface to test DbusMethod
    """

    @DbusMethod
    def my_method(self):
        """
        My dumb method
        """
    
    @DbusMethod
    def my_method_response(self):
        """
        My dumb method with return
        """
        return RESPONSE
    
    @DbusMethod
    def my_method_dbus_response(self, **kw):
        """
        My dumb method with dbus return
        """
        pass
    
    @DbusMethod
    def my_method_both_responses(self, **kw):
        """
        My dumb method with both (method and dbus) return
        """
        return RESPONSE
    
    @DbusMethod(iface=OBJECT_URI)
    def my_method_iface(self, arg):
        """
        My dumb method with iface keyword
        """

    @DbusMethod(produces=SomeReturnType)
    def my_method_produces(self, **kw):
        """
        My dumb method with produces keyword as Class
        """
        pass

    @DbusMethod(produces=some_return_function)
    def my_method_produces_method(self, arg):
        """
        My dumb method with produces keyword as method
        """
        pass

    @DbusMethod(args_to_dbus=args_to_dbus)
    def my_method_args_to_dbus_callable(self, *args):
        """
        My dumb method with args_to_dbus keyword callable
        """
        pass

    @DbusMethod(args_to_dbus=args_to_dbus_iter)
    def my_method_args_to_dbus_iter(self, *args):
        """
        My dumb method with args_to_dbus keyword iterable
        """
        pass

    @DbusMethod(args_to_dbus=args_to_dbus_iter_empty)
    def my_method_args_to_dbus_iter_empty(self, *args):
        """
        My dumb method with args_to_dbus keyword iterable, but empty iter
        """
        pass

    @DbusMethod(args_to_dbus=args_to_dbus_iter_less_than_args)
    def my_method_args_to_dbus_iter_less_than_args(self, *args):
        """
        My dumb method with args_to_dbus keyword iterable, but with less in iter that in args 
        """
        pass

    @DbusMethod(args_to_dbus=args_to_dbus_iter_more_than_args)
    def my_method_args_to_dbus_iter_more_than_args(self, *args):
        """
        My dumb method with args_to_dbus keyword iterable, but with more in iter that in args 
        """
        pass
    
    @DbusMethod(kw_to_dbus=kw_to_dbus)
    def my_method_kw_to_dbus_callable(self, **kw):
        """
        My dumb method with kw_to_dbus keyword iterable
        """
        pass
    
    @DbusMethod(kw_to_dbus=kw_to_dbus_dict)
    def my_method_kw_to_dbus_dict(self, **kw):
        """
        My dumb method with kw_to_dbus keyword dict
        """
        pass
    
    @DbusMethod(kw_to_dbus=kw_to_dbus_dict_empty)
    def my_method_kw_to_dbus_dict_empty(self, **kw):
        """
        My dumb method with kw_to_dbus keyword dict, but empty dict
        """
        pass
    
    @DbusMethod(kw_to_dbus=kw_to_dbus_dict_less_than_kw)
    def my_method_kw_to_dbus_dict_less_than_kw(self, **kw):
        """
        My dumb method with kw_to_dbus keyword dict, but dict with less then passed keywords
        """
        pass
    
    @DbusMethod(kw_to_dbus=kw_to_dbus_dict_more_than_kw)
    def my_method_kw_to_dbus_dict_more_than_kw(self, **kw):
        """
        My dumb method with kw_to_dbus keyword dict, but dict with more that passed keywords
        """
        pass