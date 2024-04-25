import unittest

from src.bacsim.phuong_utils import is_zero

class TestPhuonglUtils(unittest.TestCase):

        def test_is_zero(self):
                """Test 'is_zero'."""
                self.assertIsNotNone(is_zero.__doc__)
                self.assertTrue(is_zero(0))
                self.assertTrue(is_zero(0.0))
                self.assertFalse(is_zero(1))
                self.assertRaises(TypeError, is_zero, {1, 2})
                self.assertRaises(TypeError, is_zero, "I am a string"):while

