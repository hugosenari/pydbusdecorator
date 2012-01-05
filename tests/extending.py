'''
Tests for extended classes

Created on Jan 4, 2012

@author: hugosenari
'''
import unittest
from fixtures.extended import BasicInterface, ExtendingInterface, SomeReturnType
from fixtures.dbus import RESPONSE, ANOTHER_RESPONSE
    
    
class ExtendedInterfaceTest(unittest.TestCase):
    ''' Tests for extended classes '''
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.iface = ExtendingInterface()
        self.parentIface = BasicInterface()
    
    def testIsInstance(self):
        self.assertIsInstance(self.iface, BasicInterface)
        self.assertIsInstance(self.iface, ExtendingInterface)
    
    def testMethodCall(self):
        self.assertEqual(
            self.iface.parentMethod(
                fake_dbus_method_answer=ANOTHER_RESPONSE
            ), ANOTHER_RESPONSE)
    
    def testExtendedClassMethodCall(self):
        result = self.iface.childMethod()
        self.assertEquals(type(result), SomeReturnType)
    
    def testOverrideMethodCall(self):
        result = self.iface.bothMethod()
        self.assertEquals(type(result), SomeReturnType)
    
    def testGetAndSetAttr(self):
        val = self.iface.parentAttr
        self.assertEqual(val, RESPONSE)
    
    def testExtendedClassGetAndSetAttr(self):
        val =  self.iface.childAttr
        self.assertIsInstance(val, SomeReturnType)
    
    def testOverrideGetAndSetAttr(self):
        val =  self.iface.childAttr
        self.assertIsInstance(val, SomeReturnType)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()