import unittest

def is_probability(x):
    return True

class Test(unittest.TestCase):
    def test_is_true(self):
        self.assertIsTrue(is_probability(0))

    def test_is_false(self):
        self.assertIsTrue(not is_probability(2))