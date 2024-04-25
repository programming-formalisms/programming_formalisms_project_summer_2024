import unittest

class DNA:
    """
    this class will randomly select A-T and G-C nucleotide pairs.
    """
    def DNA_string():
        return "catgc"

class DNATest(unittest.TestCase):
    def test_is_DNA_string(self):
        self.assertIsInstance(DNA.DNA_string(), str)

    def test_is_DNA_notNone(self): 
        self.assertIn("t",DNA.DNA_string(3))

