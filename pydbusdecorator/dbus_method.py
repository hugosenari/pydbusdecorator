'''
Created on Nov 5, 2011

@author: hugosenari
'''

from pydbusdecorator.dbus_decorator import DbusDecorator
from pydbusdecorator.dbus_interface import DbusInterface

from functools import wraps

class DbusMethod(DbusDecorator):
    '''
    Wrapps some method calling dbus method
    '''

    def __init__(self, meth=None,
                 iface=None,
                 produces=None, 
                 args_to_dbus=lambda args: args,
                 kw_to_dbus=lambda kw: kw, 
                 *args, **kw):
        '''
        Wrapps some method calling dbus method
        @param meth:
            method to be wrapped
        @param produces:
            callable to convert dbus response into other type: produces(dbus_returned)
            if is not callable but iterable try convert params calling list item in same order  
        @param args_to_dbus:
            callable to convert function params into dbus typee: args_to_dbus([array of args])
            if is not callable but dict try convert params calling dicts item whith the same keyword
        @param kw_to_dbus:
            callable to convert function params (received as keywords dict) into dbus types: kw_to_dbus({dict of keywords})
        '''
        super(DbusMethod, self).__init__(*args, **kw)
        self.meth = meth
        self.iface = iface
        self.obj = None
        self.produces = produces
        self.args_to_dbus = args_to_dbus
        self.kw_to_dbus = kw_to_dbus
        
    def _call_dbus(self, obj, *args, **kw):
        bus_obj = DbusInterface.get_bus_obj(obj)
        bus_interface = self.iface if self.iface else\
            DbusInterface.get_bus_iface(obj)
        bus_meth = bus_obj.get_dbus_method(self.meth.__name__, bus_interface)
        args = self.convert_args_to_dbus_args(args)
        kw = self.convert_kw_to_dbus_kw(kw)
        result = bus_meth(*args, **kw)
        DbusInterface.store_result(obj, result)
        if self.produces:
            return self.produces(result)
        return self.meth(obj, *args, **kw)
     
    def __call__(self, __call__meth=None, *args, **kw):
        if self.meth and self.obj:
            if __call__meth:
                largs = list(args)
                largs.insert(0, __call__meth)
                args = tuple(largs)
            return self._call_dbus(self.obj, *args, **kw)
        else:
            self.meth = __call__meth
            @wraps(self.meth)
            def dbusWrapedMethod(obj, *args, **kw):
                return self._call_dbus(obj, *args, **kw)
            return dbusWrapedMethod

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        self.obj = obj
        return self.__call__
    
    def convert_args_to_dbus_args(self, args):
        if callable(self.args_to_dbus):
            return self.args_to_dbus(args)
        
        result = []
        for i in range(len(args)):
            arg = args[i]
            if len(self.args_to_dbus) > i:
                make = self.args_to_dbus[i]
                result.append(make(arg))
            else:
                result.append(arg)
        return tuple(result)
    
    def convert_kw_to_dbus_kw(self, kw):
        if callable(self.kw_to_dbus):
            return self.kw_to_dbus(kw)
        
        if hasattr(self.kw_to_dbus, 'keys'):
            to_dbus_keys = self.kw_to_dbus.keys()
            for key in kw.keys():
                if key in to_dbus_keys:
                    kw[key] = self.kw_to_dbus[key](kw[key])
        return kw