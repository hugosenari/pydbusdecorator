"""
Created on Dec 27, 2011

@author: hugosenari
"""
from pydbusdecorator import DbusInterface, DbusAttr
from dbus import My_Dbus, OBJECT_PATH, OBJECT_URI, INTERFACE
from methods import SomeReturnType, some_return_function


DbusInterface.dbus_lib = My_Dbus()

@DbusInterface(INTERFACE, OBJECT_PATH, OBJECT_URI)
class BasicInterfaceWithAttributes(object):
    """
    Basic interface to test DbusAttr
    """
    
    @DbusAttr
    def my_attr(self):
        """
        My dumb attr
        """
        
    @DbusAttr(produces=SomeReturnType)
    def my_attr_produces(self):
        """
        My dumb attr with produces Object param
        """
        
    @DbusAttr(produces=some_return_function)
    def my_attr_produces_method(self):
        """
        My dumb attr with produces method param
        """
        
    @DbusAttr(to_primitive=SomeReturnType)
    def my_attr_to_primitive(self):
        """
        My dumb attr with to_primitive Object param
        """
        
    @DbusAttr(to_primitive=some_return_function)
    def my_attr_to_primitive_method(self):
        """
        My dumb attr with to_primitive Method param
        """
    
    @DbusAttr(iface="org.test.zooom")
    def my_attr_iface(self):
        """
        my dumb attr with iface param
        """