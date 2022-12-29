#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_beginning(self):
        """Test a list when the max value is on the beginning"""
        max_at_begin = [100, 3, 98, 0]
        self.assertEqual(max_integer(max_at_begin), 100)

    def test_max_at_end(self):
        """Test a list when the max value is on the end"""
        max_at_end = [0, 9, 2, 14]
        self.assertEqual(max_integer(max_at_end), 14)

    def test_empty_list(self):
        """Test a list when it's empty"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

if __name__ == "__main__":
    unittest.main()
