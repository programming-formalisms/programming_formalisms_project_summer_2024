import unittest

def is_probability(x):
    return True

class Test(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(is_probability(0))

    def test_is_false(self):
        self.assertFalse(is_probability(0))