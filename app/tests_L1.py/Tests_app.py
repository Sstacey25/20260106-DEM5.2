import unittest
from Guidance.test_demo.calc import Calculator

class TestOperations:

    def setup(self):
        self.calculator = Calculator (8,2)

    def test_sum(self):
        self.assertEqual(self.calculator.get_sum(), 10, "The answer is not 10.")
                         
    def tear_down(self):
        pass