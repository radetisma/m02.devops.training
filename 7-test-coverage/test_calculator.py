import unittest
import calculator


class TestCalculator(unittest.TestCase):

    # -------- BASIC OPERATIONS --------
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertAlmostEqual(calculator.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    # -------- POWER --------
    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(calculator.power(2, -1), 0.5)

    # -------- SQUARE ROOT --------
    def test_square_root(self):
        self.assertEqual(calculator.square_root(16), 4)

    def test_square_root_zero(self):
        self.assertEqual(calculator.square_root(0), 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

    # -------- MODULO --------
    def test_modulo(self):
        self.assertEqual(calculator.modulo(10, 3), 1)

    def test_modulo_zero(self):
        with self.assertRaises(ValueError):
            calculator.modulo(10, 0)

    # -------- EVEN --------
    def test_is_even(self):
        self.assertTrue(calculator.is_even(4))
        self.assertFalse(calculator.is_even(5))

    # -------- POSITIVE --------
    def test_is_positive(self):
        self.assertTrue(calculator.is_positive(10))
        self.assertFalse(calculator.is_positive(-1))
        self.assertFalse(calculator.is_positive(0))

    # -------- FACTORIAL --------
    def test_factorial(self):
        self.assertEqual(calculator.factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(calculator.factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(calculator.factorial(1), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculator.factorial(-1)

    def test_factorial_type(self):
        with self.assertRaises(TypeError):
            calculator.factorial(3.5)

    # -------- LARGE NUMBERS --------
    def test_large_numbers(self):
        self.assertEqual(calculator.power(2, 10), 1024)
        self.assertEqual(calculator.multiply(1000, 1000), 1000000)


if __name__ == "__main__":
    unittest.main()
