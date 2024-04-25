import unittest

class TestIsEven(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(is_even(2), True)