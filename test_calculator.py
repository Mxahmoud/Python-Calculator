import unittest

from calculator import calculate


class TestCalculator(unittest.TestCase):
    
    def test_addition_positive_numbers(self):
        self.assertEqual(calculate(5, 3, "+"), 8)

    def test_addition_with_zero(self):
        self.assertEqual(calculate(5, 0, "+"), 5)

if __name__ == "__main__":
    unittest.main()
