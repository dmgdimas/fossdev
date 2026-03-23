import unittest
from tax.income import Income
class TestIncome(unittest.TestCase):
    def test_calculator_tax(self):
        income = Income(1000)
        self.assertEqual(income.calculator_tax(), 150.0)
        income = Income(1234)
        self.assertEqual(income.calculator_tax(), 185.1)
        income = Income(0)
        self.assertEqual(income.calculator_tax(), 0.0)
        print("test tax passed")