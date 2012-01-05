'''
Created on Dec 26, 2011

@author: hugosenari
'''
import unittest

from fixtures.interfaces import BasicInterface, BasicInterfaceInit, OBJECT_URI_TOO,\
    BasicInterfaceWithParamInConstructor, BasicInterfaceWithKeywordsInConstructor, \
    BasicInterfaceWithParamAndKeywordsInConstructor, InterfaceWithAllParams, \
    ExtendingInterfaceInit
    
from pydbusdecorator.dbus_interface import DbusInterface, DBUS_INJECTED_ATTRS

class BasicInterfaceTest(unittest.TestCase):
    '''
    Test interface creation
    '''

    def testBasicInterface(self):
        '''
        Test simple interface with no parameters and no keywords
        '''
        biface = BasicInterface()
        self.assertTrue(hasattr(biface, DBUS_INJECTED_ATTRS.dbus_interface_info_at))
        dbus_interface_info = getattr(biface, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertTrue(hasattr(dbus_interface_info, "dbus_obj_uri"))
        
    def testBasicInterfaceChangingDefaultVars(self):
        '''
        Test simple interface with no parameters and no keywords
        but now changing default DbusDecorator value
        '''
        biface = BasicInterface(dbus_uri=OBJECT_URI_TOO)
        dbus_interface_info = getattr(biface, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertEqual(dbus_interface_info.dbus_obj_uri, OBJECT_URI_TOO)
        
    def testBasicInterfaceWithParamInConstructor(self):
        '''
        test simple interface that receives a param
        '''
        bifaceWP = BasicInterfaceWithParamInConstructor(None)
        self.assertTrue(hasattr(bifaceWP, DBUS_INJECTED_ATTRS.dbus_interface_info_at))
        dbus_interface_info = getattr(bifaceWP, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertTrue(hasattr(dbus_interface_info, "dbus_obj_uri"))
        
    def testBasicInterfaceWithParamInConstructorChangingDefaultVars(self):
        '''
        test simple interface that receives a param
        but now changing default DbusDecorator value
        '''
        bifaceWP = BasicInterfaceWithParamInConstructor(None, dbus_uri=OBJECT_URI_TOO)
        dbus_interface_info = getattr(bifaceWP, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertEqual(dbus_interface_info.dbus_obj_uri, OBJECT_URI_TOO)
        
    def testBasicInterfaceWithKeywordsInConstructor(self):
        '''
        test simple interface that receives a keyword param
        '''
        bifaceWK = BasicInterfaceWithKeywordsInConstructor(keyword=None)
        self.assertTrue(hasattr(bifaceWK, DBUS_INJECTED_ATTRS.dbus_interface_info_at))
        dbus_interface_info = getattr(bifaceWK, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertTrue(hasattr(dbus_interface_info, "dbus_obj_uri"))
        
    def testBasicInterfaceWithKeywordsInConstructorChangingDefaultVars(self):
        '''
        test simple interface that receives a keyword param
        but now changing default DbusDecorator value
        '''
        bifaceWK = BasicInterfaceWithKeywordsInConstructor(keyword=None, dbus_uri=OBJECT_URI_TOO)
        dbus_interface_info = getattr(bifaceWK, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertEqual(dbus_interface_info.dbus_obj_uri, OBJECT_URI_TOO)
                
    def testBasicInterfaceWithParamAndKeywordsInConstructor(self):
        '''
        test simple interface that receives a param and keyword param 
        '''
        bifaceWPK = BasicInterfaceWithParamAndKeywordsInConstructor(None, keyword=None)
        self.assertTrue(hasattr(bifaceWPK, DBUS_INJECTED_ATTRS.dbus_interface_info_at))
        dbus_interface_info = getattr(bifaceWPK, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertTrue(hasattr(dbus_interface_info, "dbus_obj_uri"))
                
    def testBasicInterfaceWithParamAndKeywordsInConstructorChangingDefaultVars(self):
        '''
        test simple interface that receives a param and keyword param
        but now changing default DbusDecorator value 
        '''
        bifaceWPK = BasicInterfaceWithParamAndKeywordsInConstructor(None, keyword=None, dbus_uri=OBJECT_URI_TOO)
        dbus_interface_info = getattr(bifaceWPK, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertEqual(dbus_interface_info.dbus_obj_uri, OBJECT_URI_TOO)


class AttrNameAtTest(unittest.TestCase):
    '''
    Test set and get attr
    '''

    def testAttrNameAt(self):
        '''
        test attr_name_at
        '''
        IWAPface = InterfaceWithAllParams()
        dbus_uriA = IWAPface.dbus_interface_info.dbus_obj_uri
        dbus_uriB = DbusInterface.get_uri(IWAPface)
        self.assertEquals(dbus_uriA, dbus_uriB)
    
    def testAttrNameAtChangingValues(self):
        '''
        test attr_name_at setting values
        '''
        IWAPface = InterfaceWithAllParams()
        dbus_uriA = IWAPface.dbus_interface_info.dbus_obj_uri
        dbus_uriB = DbusInterface.get_uri(IWAPface)
        self.assertEquals(dbus_uriA, dbus_uriB)
        
    def testAttrNameAtShortcuts(self):
        '''
        Test attr_name_at shortcuts
        '''
        IWAPface = InterfaceWithAllParams()
        dbus_interface_info = IWAPface.dbus_interface_info
        self.assertEquals(
                          DbusInterface.get_bus_iface(IWAPface),
                          dbus_interface_info.dbus_iface
        )
        self.assertEquals(
                          DbusInterface.get_bus_obj(IWAPface),
                          dbus_interface_info.dbus_obj
        )
        self.assertEquals(
                          DbusInterface.get_bus_iface(IWAPface),
                          dbus_interface_info.dbus_iface
        )
        self.assertEquals(
                          DbusInterface.get_bus_prop_iface(IWAPface),
                          dbus_interface_info.dbus_prop_iface
        )
        self.assertEquals(
                          DbusInterface.get_path(IWAPface),
                          dbus_interface_info.dbus_path
        )
        self.assertEquals(
                          DbusInterface.get_session(IWAPface),
                          dbus_interface_info.dbus_session
        )
        self.assertEquals(
                          DbusInterface.get_uri(IWAPface),
                          dbus_interface_info.dbus_obj_uri
        )

    def testBasicInterfaceInit(self):
        '''
        Test simple interface with no parameters and no keywords
        Now using __init__
        '''
        biface = BasicInterfaceInit()
        self.assertTrue(hasattr(biface, DBUS_INJECTED_ATTRS.dbus_interface_info_at))
        dbus_interface_info = getattr(biface, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertTrue(hasattr(dbus_interface_info, "dbus_obj_uri"))

    def testExtendedInterface(self):
        '''
        Test simple interface with no parameters and no keywords
        Now using __init__
        '''
        biface = ExtendingInterfaceInit()
        self.assertTrue(hasattr(biface, DBUS_INJECTED_ATTRS.dbus_interface_info_at))
        dbus_interface_info = getattr(biface, DBUS_INJECTED_ATTRS.dbus_interface_info_at)
        self.assertTrue(hasattr(dbus_interface_info, "dbus_obj_uri"))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()