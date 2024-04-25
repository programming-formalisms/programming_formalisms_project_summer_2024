import unittest

class DNA:
    """
    this class will randomly select A-T and G-C nucleotide pairs.
    """
    def DNA_string(x):
        return x

class DNATest(unittest.TestCase):
    def test_is_DNA_string(self):
        self.assertIsInstance(DNA.DNA_string("t"), str)

    def test_is_DNA_notNone(self): 
        self.assertIn("t",DNA.DNA_string(3))

    def test_is_DNA_base():
        self.assertEqual(DNA.DNA_string(3),("A-T" or "G-C"))
