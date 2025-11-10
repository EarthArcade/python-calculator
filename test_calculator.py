import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(1, -2), -1)
        

    # Add the following test methods to the TestCalculator class:
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(4, -2), 6)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(4, 20), 80)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(20, 10), 2)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(20, 6), 2)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(16, 3), 1)
    
if __name__ == '__main__':
    unittest.main()