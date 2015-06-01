import unittest

from main import is_even


class IsEvenTests(unittest.TestCase):

    def test_when_positive_odd(self):
        self.assertFalse(is_even(13))

    def test_when_negative_odd(self):
        self.assertFalse(is_even(-5))

    def test_when_positive_even(self):
        self.assertTrue(is_even(20))

    def test_when_negative_even(self):
        self.assertTrue(is_even(-10))


if __name__ == '__main__':
    unittest.main()