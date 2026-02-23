import unittest
from src.lab1.calculator import calc

class CalculatorTestCase(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calc(1, 3, "+"), 4)

    def test_minus(self):
        self.assertEqual(calc(7, 2, "-"), 5)

    def test_um(self):
        self.assertEqual(calc(3, 6, "*"), 18)

    def test_del(self):
        self.assertEqual(calc(12, 4, "/"), 3.0)

    def test_div_by_0(self):
        with self.assertRaises(ZeroDivisionError):
            calc(23, 0, "/")