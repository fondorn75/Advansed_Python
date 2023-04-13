import unittest
from hexametric import hexCreation


class TestCaseHex(unittest.TestCase):
    def testHexTrue(self):
        self.assertTrue(hexCreation(42))
        self.assertTrue(hexCreation(184))
        self.assertTrue(hexCreation(20154))

    def test_type(self):
        self.assertRaises(TypeError, hexCreation, 'Двадцать')


if __name__ == '__main__':
    unittest.main()
