#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        lst = [1, 2, 3, 4, 5]
        result = max_integer(lst)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        lst = [-5, -4, -3, -2, -1]
        result = max_integer(lst)
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        lst = [-5, 2, 0, 10, -1]
        result = max_integer(lst)
        self.assertEqual(result, 10)

    def test_duplicate_max(self):
        lst = [1, 2, 3, 3, 2, 1]
        result = max_integer(lst)
        self.assertEqual(result, 3)

    def test_empty_list(self):
        lst = []
        result = max_integer(lst)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
