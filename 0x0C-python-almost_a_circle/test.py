from test_modules import TestFoo
from test_modules import TestBar
import test_modules
import unittest

def setUpModules():
    print("setUpModule WassCodeur")

def tearDownModules():
    print("tearDownModule Wass")


if __name__ == "__main__":
    test_modules.setUpModule = setUpModules
    test_modules.tearDownModule = tearDownModules
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestBar)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner().run(suite)