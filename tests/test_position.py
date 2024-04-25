"""Test for nutrient"""

import unittest

from src.bacsim.position import Position

class TestPosition(unittest.TestCase):

    """Class to test the functions in src.bacsim.position"""

    def test_Position(self):
        self.assertIsNotNone(Position.__doc__)