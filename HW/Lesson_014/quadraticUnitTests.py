import unittest
from quadratic import quadraticEquation


class NewQuadraticCase(unittest.TestCase):
    def testCheckQuadratic(self):
        self.assertEqual(quadraticEquation(2, -5, -4), 'У уравнения два разных корня: 3.14, -0.64')
        self.assertEqual(quadraticEquation(4, -2, -8), 'У уравнения два разных корня: 1.69, -1.19')

    def testCheckTypeError(self):
        self.assertRaises(TypeError, quadraticEquation, 2, -5, "3")


if __name__ == '__main__':
    unittest.main()

