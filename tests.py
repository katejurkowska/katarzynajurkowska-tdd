import unittest

from main import is_even, fib_numbers


class IsEvenTests(unittest.TestCase):

    def test_when_positive_odd(self):
        self.assertFalse(is_even(13))

    def test_when_negative_odd(self):
        self.assertFalse(is_even(-5))

    def test_when_positive_even(self):
        self.assertTrue(is_even(20))

    def test_when_negative_even(self):
        self.assertTrue(is_even(-10))


class FibNumbersTests(unittest.TestCase):

    def test_1_number(self):
        number_gen = fib_numbers()
        self.assertEqual(1, next(number_gen))

    def test_2_numbers(self):
        number_gen = fib_numbers()
        self.assertEqual(1, next(number_gen))
        self.assertEqual(2, next(number_gen))

    def test_10_numbers(self):
        number_gen = fib_numbers()
        numbers = [next(number_gen) for _ in range(10)]
        expected_numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(expected_numbers, numbers)


if __name__ == '__main__':
    unittest.main()