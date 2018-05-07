#!/usr/bin/python3
"""
Module to find the max integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function
    """

    def test_max_integer(self):
        '''
        Test if integer is max integer
        '''
        result = max_integer([1, 4, 3, 2])
        self.assertEqual(result, 4)
        result = max_integer([12, 9, 7, 2])
        self.assertEqual(result, 12)

    def test_isint(self):
        '''
        Test to check variable against integer
        '''
        var = 1
        self.assertTrue(max_integer([var, 2]) == 2)
        x = 5
        self.assertTrue(max_integer([1, x]) == x)

    def test_same_entry(self):
        '''
        Test to check max int if same
        '''
        a = 50
        self.assertEqual(max_integer([a, a, a, a]), a)

    def test_float_integer(self):
        '''
        Test to see if float is max integer
        '''
        self.assertEqual(max_integer([4.0, 3, 2]), 4.0)

    def test_one_entry(self):
        '''
        Test to check if only one entry
        '''
        self.assertEqual(max_integer([10]), 10)

    def test_negative_integer(self):
        '''
        Test only negative integers
        '''
        self.assertEqual(max_integer([-1, -2, -5]), -1)
    def test_no_argument(self):
        '''
        Test that None is returned if no argument
        '''
        self.assertEqual(max_integer(), None)
    def test_empty_list(self):
        '''
        Test if list is empty
        '''
        self.assertEqual(max_integer([]), None)

    if __name__ == '__main__':
        unittest.main()
