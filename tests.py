import unittest

from main import is_even, fib_numbers, sum_limit, sum_even_fib_numbers


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


class SumLimitTests(unittest.TestCase):

    def test_empty_sequence(self):
        self.assertEqual(0, sum_limit([], 40))

    def test_when_limit_is_greater_then_sum_of_numbers(self):
        self.assertEqual(15, sum_limit([1, 2, 3, 4, 5], 40))

    def test_when_limit_is_less_then_sum_of_numbers(self):
        self.assertEqual(10, sum_limit([1, 2, 3, 4, 5], 11))

    def test_when_first_number_is_greater_then_limit(self):
        self.assertEqual(0, sum_limit([100], 10))


class SumEvenFibNumbersTests(unittest.TestCase):

    def test_when_limit_is_zero(self):
        self.assertEqual(0, sum_even_fib_numbers(limit=0))

    def test_when_limit_is_10(self):
        self.assertEqual(10, sum_even_fib_numbers(limit=10))

    def test_when_limit_is_100(self):
        self.assertEqual(44, sum_even_fib_numbers(limit=100))

    def test_when_limit_is_2000(self):
        self.assertEqual(798, sum_even_fib_numbers(limit=2000))

    def test_when_limit_is_4000000(self):
        self.assertEqual(1089154, sum_even_fib_numbers(limit=4000000))


if __name__ == '__main__':
    unittest.main()