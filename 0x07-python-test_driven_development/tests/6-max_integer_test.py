import unittest
"""Unittest for max_integer([..])
"""
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer([..])
    args:
        unittest (class): Class to test max_integer([..])   
    returns:
        None
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 11)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 12)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 13)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 14)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 15)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 16)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 17)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), 18)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), 19)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 20)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), 21)
