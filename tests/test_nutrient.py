"""Test for nutrient"""

import unittest

from src.bacsim.nutrient import Nutrient

class TestNutrients(unittest.TestCase):

    """Class to test the functions in src.bacsim.nutrient"""

    def test_Nutrient(self):
        self.assertIsNotNone(Nutrient.__doc__)
    
