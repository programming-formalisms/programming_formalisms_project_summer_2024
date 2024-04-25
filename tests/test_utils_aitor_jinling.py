import unittest

def is_probability(x):
    return(x >= 0 and x <= 1)

class Test(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(is_probability(0))

    def test_is_false(self):
        self.assertFalse(is_probability(2))
    
    def test_is_not_number(self):
        self.assertRaises(TypeError, is_probability("TestString"))

