'''P
Created on Dec 27, 2011

@author: hugosenari
'''
import unittest
from fixtures.attributes import BasicInterfaceWithAttributes
from fixtures.methods import SomeReturnType, AnotherReturnType
from fixtures.dbus import RESPONSE, ANOTHER_RESPONSE

class DbusAttrTest(unittest.TestCase):
    """
    Tests for DbusAttr
    """

    def testGetAttr(self):
        """
        Test get simple attr
        """
        bifacewattr = BasicInterfaceWithAttributes()
        self.assertEqual(bifacewattr.my_attr, RESPONSE)

    def testSetAttr(self):
        """
        Test set simple attr
        """
        bifacewattr = BasicInterfaceWithAttributes()
        bifacewattr.my_attr = ANOTHER_RESPONSE
        self.assertEquals(bifacewattr.my_attr, ANOTHER_RESPONSE)
    
    def testDeleteAttr(self):
        """
        Test delete simple attr (implementation raise AttributeError)
        """
        bifacewattr = BasicInterfaceWithAttributes()
        def callme(): del bifacewattr.my_attr
        self.assertRaises(AttributeError, callme)
        self.assertEqual(bifacewattr.my_attr, RESPONSE)
    
    def testGetAttrProduces(self):
        """
        Test get attr created with produces param, procuces class
        """
        bifacewattr = BasicInterfaceWithAttributes()
        self.assertTrue(isinstance(bifacewattr.my_attr_produces, SomeReturnType), "attr must return class passed to produces")
    
    def testSetAttrProduces(self):
        """
        Test set attr created with produces param, produces class
        """
        bifacewattr = BasicInterfaceWithAttributes() 
        bifacewattr.my_attr_produces = ANOTHER_RESPONSE
        self.assertEquals(bifacewattr.my_attr, ANOTHER_RESPONSE)
    
    def testGetAttrProducesMethod(self):
        """
        Test get attr created with produces param, but calling method
        """
        bifacewattr = BasicInterfaceWithAttributes()
        self.assertTrue(isinstance(bifacewattr.my_attr_produces_method, SomeReturnType), "attr must return class passed to produces")
    
    def testSetAttrProducesMethod(self):
        """
        Test set attr created with produces param, but calling method
        """
        bifacewattr = BasicInterfaceWithAttributes() 
        bifacewattr.my_attr_produces_method = ANOTHER_RESPONSE
    
    def testGetAttrToPrimitive(self):
        """
        Test get attr created with to_primitive param
        """
        bifacewattr = BasicInterfaceWithAttributes()
        self.assertEqual(bifacewattr.my_attr, RESPONSE)
    
    def testSetAttrToPrimitive(self):
        """
        Test set attr created with to_primitive param
        """
        bifacewattr = BasicInterfaceWithAttributes() 
        bifacewattr.my_attr_to_primitive = ANOTHER_RESPONSE
        self.assertTrue(isinstance(bifacewattr.my_attr_produces_method, AnotherReturnType), "attr must return class passed to to_primitive")
    
    def testGetAttrToPrimitiveMethod(self):
        """
        Test get attr created with to_primitive param, but calling one method
        """
        bifacewattr = BasicInterfaceWithAttributes()
        self.assertEqual(bifacewattr.my_attr, RESPONSE)
    
    def testSetAttrToPrimitiveMethod(self):
        """
        Test set attr created with to_primitive param, but calling one method
        """
        bifacewattr = BasicInterfaceWithAttributes() 
        bifacewattr.my_attr_to_primitive_method = ANOTHER_RESPONSE
        self.assertTrue(isinstance(bifacewattr.my_attr_produces_method, AnotherReturnType), "attr must return class passed to to_primitive")
    
    def testGetAttrIface(self):
        """
        Test get attr created with ifcae param
        """
        bifacewattr = BasicInterfaceWithAttributes()
        self.assertEquals(bifacewattr.my_attr_iface, RESPONSE)
    
    def testSetAttrIface(self):
        """
        Test set attr created with to_primitive param
        """
        bifacewattr = BasicInterfaceWithAttributes()
        bifacewattr.my_attr_iface = ANOTHER_RESPONSE


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()