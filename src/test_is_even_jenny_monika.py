import unittest

from is_even_jenny_monika import is_even

class TestIsEven(unittest.TestCase):

    def test_is_even_true(self):
        self.assertEqual(is_even(2), True)

    def test_is_even_false(self):
        self.assertEqual(is_even(3), False)

    def test_is_even_not_number(self):
        self.assertEqual(is_even(""), "Warning! The input must be an integer")
