import unittest

from src.test_is_even_jenny_monika import is_even

class TestIsEven(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(is_even(2), True)