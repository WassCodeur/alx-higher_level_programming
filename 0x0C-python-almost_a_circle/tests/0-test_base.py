import unittest
import inspect
import json
from models import base
Base = base.Base
"""TestBase class"""
class TestBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base()
        self.assertFalse(b6.id == 6)