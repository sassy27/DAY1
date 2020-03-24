
from SimpleCalc import Simple_Calc
import unittest

class Calctests(unittest.TestCase):

    cal = Simple_Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8, 4), 4)

if __name__ == '__main__':
    unittest.main()