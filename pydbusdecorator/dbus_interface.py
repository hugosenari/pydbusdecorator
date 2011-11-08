'''
Created on Nov 5, 2011

@author: hugosenari
'''

from pydbusdecorator.dbus_decorator import DbusDecorator
from functools import wraps
import dbus

class DbusInterface(DbusDecorator):
    '''
    Wraps some class that define dbus interface
    '''
    def __init__(self,
                   #default values
                   iface=None,
                   path=None,
                   uri=None,
                   obj=None,
                   session=None,
                   retur=None,
                   on_change=None,
                   prop_iface='org.freedesktop.DBus.Properties',
                   #defalt var names in object 
                   iface_at='dbus_iface',
                   path_at='dbus_path',
                   uri_at='dbus_uri',
                   obj_at='dbus_object',
                   session_at='dbus_session',
                   return_at='last_fn_return',
                   on_change_at='on_change',
                   prop_iface_at='dbus_prop_iface',
                *args, **kw):
        '''
        Init this decorator
        @param iface: str dbus object interface
        @param path: str dbus object path
        @param path: str dbus object uri (org.mpris.MediaPlayer2.banshee)
        @param obj: dbus.proxies.ProxyObject
        @param session: dbus dbus.SessionBus.get_session()
        @param prop_iface: str dbus object default interface for properties
        @param iface_at: str where store iface in this obj
        @param path_at: str where store dbus_path in this obj
        @param uri_at: str where store dbus_uri in this obj
        @param obj_at: str where store dbus_object in this obj
        @param session_at: str where store dbus_session in this obj
        @param return_at: str where store last call return in this obj
        @param on_change_at: str where store on change callbacks in this obj
        @param prop_iface_at: str where store properties iface in this obj
        
        @see: mpris2.mediaplayer2 to see some examples
        '''
        super(DbusInterface, self).__init__(*args, **kw)
        self._attr_keys = (
                           iface_at,
                           path_at,
                           uri_at,
                           obj_at,
                           session_at,
                           return_at,
                           on_change_at,
                           prop_iface_at)
        self._dbus_default_attrs = {
                                        'dbus_iface':iface,
                                        'dbus_path':path,
                                        'dbus_uri':uri,
                                        'dbus_object':obj,
                                        'dbus_session':session,
                                        'last_fn_return':retur,
                                        'on_change':on_change,
                                        'dbus_prop_iface':prop_iface
        }
        self._dbus_injected_attr_dict = {
                                        'iface_at':iface_at,
                                        'path_at':path_at,
                                        'uri_at':uri_at,
                                        'obj_at':obj_at,
                                        'session_at':session_at,
                                        'return_at':return_at,
                                        'on_change_at':on_change_at,
                                        'prop_iface_at':prop_iface_at
        }
        
    def __call__(self, meth, *args, **kw):
        '''
            Called when any decorated class is loaded
        '''
        @wraps(meth)
        def dbusWrapedInterface(*args, **kw):
            '''
                Called when some decoreted class was called
                @param *args: list of args to call constructor
                @param **kw: dict of keywords, can redefine class default parameters
                @return: instance of decoreted class, with new attributes
                @see: mpris2.mediaplayer2 to see some examples
            '''
            new_obj = meth(*args)
            for key in self._attr_keys:
                if key in kw:
                    setattr(new_obj, key, kw[key])
                elif key in self._dbus_default_attrs:
                    setattr(new_obj, key, self._dbus_default_attrs[key])
            setattr(new_obj, '_dbus_injected_attr_dict',
                    self._dbus_injected_attr_dict)
            setattr(new_obj, '_dbus_default_attrs',
                    self._dbus_default_attrs)
            return new_obj
        return dbusWrapedInterface
    
    @staticmethod
    def attr_name_at(at, attr, val=None):
        '''
            gets/sets objs attributes
            @param at: object where get/set
            @param attr: str name o attribute
            @param val: object with new value
            @return:  attribute value
        '''
        if val:
            setattr(at, at._dbus_injected_attr_dict[attr], val)
        return getattr(at, at._dbus_injected_attr_dict[attr])
    
    @staticmethod
    def store_result(at, val):
        '''
            use to set last call result
            @param at: object where set
            @param val: object to set
            @return:  val
        '''
        return DbusInterface.attr_name_at(at, 'return_at', val)
    
    @staticmethod
    def get_session(at):
        '''
            use to get dbus_session in object
            @param at: object where get session previously criated
            @return session object
         '''
        bus_session = DbusInterface.attr_name_at(at, 'session_at')
        if bus_session == None:
            bus_session = dbus.SessionBus.get_session()
            DbusInterface.attr_name_at(at, 'session_at', bus_session)
        return bus_session
    
    @staticmethod
    def get_path(at):
        '''
            Return dbus object path attribute
            @param at: object where get this path
            @return: str object dbus path
        '''
        return DbusInterface.attr_name_at(at, 'path_at')
    
    @staticmethod
    def get_uri(at):
        '''
            Return dbus object uri attribute
            @param at: object where get this uri
            @return: str object dbus uri
        '''
        return DbusInterface.attr_name_at(at, 'uri_at')
    
    @staticmethod
    def get_bus_obj(at):
        '''
            Return dbus object
            @param at: object where get this dbus object
            @return: dbus proxi object
        '''
        obj = DbusInterface.attr_name_at(at, 'obj_at')
        if obj == None:
            uri = DbusInterface.get_uri(at)
            if uri:
                path = DbusInterface.get_path(at)
                if path:
                    session = DbusInterface.get_session(at)
                    obj = session.get_object(uri, path)
                    DbusInterface.attr_name_at(at, 'obj_at', obj)
        return obj
    
    @staticmethod
    def get_bus_iface(at):
        '''
        return bus_iface of 'at'
        '''
        return DbusInterface.attr_name_at(at, 'iface_at')
    
    @staticmethod
    def get_bus_prop_iface(at):
        '''
        return bus_prop_iface of 'at'
        '''
        return DbusInterface.attr_name_at(at, 'prop_iface_at')\
             or DbusInterface.get_bus_iface(at)  
    
    @staticmethod
    def get_bus_properties(at, iface=None):
        '''
        return bus propeterty calls
        '''
        obj = DbusInterface.get_bus_obj(at)
        iface = iface or DbusInterface.get_bus_prop_iface(at)
        return dbus.Interface(obj, dbus_interface=iface)
    
    @staticmethod
    def iface(at, iface):
        return dbus.Interface(DbusInterface.get_bus_obj(at), iface)