import unittest
from src.bacsim.visualization import Visualization

class TestVisualization(unittest.TestCase):

    """Class to test the code in src.bacsim.visualization"""

    def test_can_create_visual_object(self):
        """Test if we can create a visualization object"""
        Visualization()