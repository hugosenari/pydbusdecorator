'''
Created on Dec 29, 2011

@author: hugosenari
'''
import unittest
from fixtures.methods import BasicInterfaceWithMethods, SomeReturnType, AnotherReturnType
from fixtures.dbus import RESPONSE, ANOTHER_RESPONSE


class DbusMethodTest(unittest.TestCase):
    """
    Tests for DbusMethod
    """
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.bifacewmethods = BasicInterfaceWithMethods()
    
    def tearDown(self):
        self.bifacewmethods = None
        unittest.TestCase.tearDown(self)

    def testCallMethod(self):
        self.bifacewmethods.my_method()
        
    def testCallMethodWithResponse(self):
        self.assertEqual(
            self.bifacewmethods.my_method_response(),
            RESPONSE)
        
    def testCallMethodWithDbusResponse(self):
        self.assertEqual(
            self.bifacewmethods.my_method_dbus_response(
                fake_dbus_method_answer=ANOTHER_RESPONSE
            ), ANOTHER_RESPONSE)
        
    def testCallMethodWithBothResponses(self):
        self.assertEqual(
            self.bifacewmethods.my_method_both_responses(
                fake_dbus_method_answer=ANOTHER_RESPONSE
            ), RESPONSE)

    def testCallMethodWithIfaceKw(self):
        self.bifacewmethods.my_method_iface(RESPONSE)
        
    def testCallMethodWithProducesKw(self):
        result = self.bifacewmethods.my_method_produces()
        self.assertEquals(type(result), SomeReturnType)
        
    def testCallMethodWithProducesCallingMethodKw(self):
        result = self.bifacewmethods.my_method_produces_method()
        self.assertEquals(type(result), AnotherReturnType)
        
    def testCallMethodWithArgsToDbus(self):
        self.bifacewmethods.my_method_args_to_dbus_callable()
        
    def testCallMethodWithArgsToDbusIter(self):
        self.bifacewmethods.my_method_args_to_dbus_iter(1)
        
    def testCallMethodWithArgsToDbusIterEmpty(self):
        self.bifacewmethods.my_method_args_to_dbus_iter_empty(1)
        
    def testCallMethodWithArgsToDbusIterLessThanArgs(self):
        self.bifacewmethods.my_method_args_to_dbus_iter_less_than_args(1, 2)
        
    def testCallMethodWithArgsToDbusIterMoreThanArgs(self):
        self.bifacewmethods.my_method_args_to_dbus_iter_more_than_args(1)
        
    def testCallMethodWithKwToDbus(self):
        self.bifacewmethods.my_method_kw_to_dbus_callable(my_arg=1)
        
    def testCallMethodWithKwToDbusDict(self):
        self.bifacewmethods.my_method_kw_to_dbus_dict(my_arg=1)
        
    def testCallMethodWithKwToDbusDictEmpty(self):
        self.bifacewmethods.my_method_kw_to_dbus_dict_empty(my_arg=1)
        
    def testCallMethodWithKwToDbusDictLessThenKw(self):
        self.bifacewmethods.my_method_kw_to_dbus_dict_less_than_kw(my_arg=1, your_arg=2)
        
    def testCallMethodWithKwToDbusDictMoreThenKw(self):
        self.bifacewmethods.my_method_kw_to_dbus_dict_more_than_kw(my_arg=1, your_arg=2)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
