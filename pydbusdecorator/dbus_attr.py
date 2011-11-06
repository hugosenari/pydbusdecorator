'''
Created on Nov 5, 2011

@author: hugosenari
'''

from pydbusdecorator.dbus_decorator import DbusDecorator
from pydbusdecorator.undefined_param import UndefinedParam
from pydbusdecorator.dbus_interface import DbusInterface

from functools import wraps

class DbusAttr(DbusDecorator):
    '''
    Wrap some method as attribute
    '''


    def __init__(self, meth=None, iface=None, override_none_val=UndefinedParam,
                  override_none_return=True, *args, **kw):
        '''
            Instantiate one new DbusAttr decoreator
            By default pass received val to method
            @param meth: function overrided
            @param iface: str dbus intercafe string with this property
            @param override_none_val: anything different than UndefinedParam is True
            @param override_none_return: anything else than UndefinedParam is True
        '''
        super(DbusAttr, self).__init__(*args, **kw)
        self.meth = meth
        self.iface = iface
        self.override_val = override_none_val
        self.override_return = override_none_return

    def __call__(self, meth, *args, **kw):
        self.meth=meth
        @wraps(meth)
        def dbusWrapedAttr(obj, val=UndefinedParam, *args, **kw):
            return self._get_set_dbus(obj, val, *args, **kw)
        return dbusWrapedAttr

    def _get_set_dbus(self, obj, val=UndefinedParam, *args, **kw):
        properties = DbusInterface.get_bus_properties(obj)
        iface = self.iface or DbusInterface.get_bus_iface(obj)
        #vals is UndefinedParam, try to get val from object
        if val is UndefinedParam:
            mval = properties.Get(iface, self.meth.__name__)
            DbusInterface.store_result(obj, mval)
            if self.override_val is not UndefinedParam:
                val = mval
        else:
            properties.Set(iface, self.meth.__name__, val)
            DbusInterface.store_result(self, val)
        yval = self.meth(val, *args, **kw)
        if yval is None and self.override_return is not UndefinedParam:
            return properties.Get(iface, self.meth.__name__)
        return yval

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self._get_set_dbus(obj)

    def __set__(self, obj, value):
        return self._get_set_dbus(obj, value)

    def __delete__(self, obj):
        raise AttributeError, "can't delete attribute"
        