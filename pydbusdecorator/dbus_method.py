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

    def __init__(self, meth=None, produces=None, *args, **kw):
        '''
        Wrapps some method calling dbus method
        '''
        super(DbusMethod, self).__init__(*args, **kw)
        self.meth = meth
        self.obj = None
        self.produces = produces
    
    def _call_dbus(self, obj, *args, **kw):
        bus_obj = DbusInterface.get_bus_obj(obj)
        bus_meth = bus_obj.get_dbus_method(self.meth.__name__)
        result = bus_meth(*args, **kw)
        DbusInterface.store_result(obj, result)
        return self.meth(obj, *args, **kw) or result
     
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