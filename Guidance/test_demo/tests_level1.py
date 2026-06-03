import unittest
from calc import Calculator

## This is the ineffecient run

"""class TestOperations(unittest.TestCase):


        def test_sum(self):
                calculator = Calculator(8,2)
                self.assertEqual(calculator.get_sum(), 10, "The answer was not 10.")

        def test_product(self):
                calculator = Calculator(2,2)
                self.assertEqual(calculator.get_product(), 4, "The answer was not 4.")

        def test_diff(self):
                calculator = Calculator(10,6)
                self.assertEqual(calculator.get_diff(), 4, "The answer was not 4.")
        
        def test_quotient(self):
                calculator = Calculator(10,2)
                self.assertEqual(calculator.get_quotient(), 5.0, "The answer was not 5.")

if __name__== "__main__":
        unittest.main()
"""

#More efficient BUT limited on Calculator

"""class TestOperations(unittest.TestCase):
        
        def setUp(self):
                self.calculator = Calculator(8,2)
        
        def test_sum(self):
                self.assertEqual(self.calculator.get_sum(), 10, "The answer was not 10.")

        def test_product(self):
                self.assertEqual(self.calculator.get_product(), 16, "The answer was not 16.")

        def test_diff(self):
                self.assertEqual(self.calculator.get_diff(), 6, "The answer was not 6.")
        
        def test_quotient(self):
                self.assertEqual(self.calculator.get_quotient(), 4.0, "The answer was not 4.")

if __name__== "__main__":
        unittest.main()

"""

import unittest
from Guidance.test_demo.calc import Calculator

class TestOperations:

    def setup(self):
        self.calculator = Calculator (8,2)

    def test_sum(self):
        self.assertEqual(self.calculator.get_sum(), 10, "The answer is not 10.")
                         
    def tear_down(self):
        pass