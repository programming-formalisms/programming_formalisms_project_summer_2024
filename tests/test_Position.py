"""Tests Position class"""

import unittest

from src.bacsim.Position import Position

class TestPosition(unittest.TestCase):

    """Class to test Position class"""

    def test_Position(self):
        self.assertIsNotNone(Position)
        self.assertIsNotNone(Position.x)
