def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" %(key,value))
    elif kwargs == {}:
        print("No arguments passed")
greet_me(name="yasoob")

def test_args_kwargs(arg1, arg2, arg3,arg4):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    print("arg4:", arg4)
argv = ["one", "two", "three", "sun"]
arg = {"arg1": "one", "arg2": "two", "arg3": "three", "arg4": "sun"}
test_args_kwargs(*argv)
test_args_kwargs(**arg)


import unittest

def fib(n):
    return 1 if n<=2 else fib(n-1)+fib(n-2)

def setUpModule():
        print("setup module")
def tearDownModule():
        print("teardown module")

class TestFib(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.n = 10
    def tearDown(self):
        print("tearDown")
        del self.n
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def test_fib_assert_equal(self):
        self.assertEqual(fib(self.n), 55)
    def test_fib_assert_true(self):
        self.assertTrue(fib(self.n) == 55)

if __name__ == "__main__":
    unittest.main()