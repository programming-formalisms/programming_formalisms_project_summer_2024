import unittest
import src.bacsim.model as model


class ModelTest(unittest.TestCase):
    def test_doc(self):
        self.assertIsNotNone(model.__doc__)
