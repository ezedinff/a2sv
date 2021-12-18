"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Input: nums = [3,30,34,5,9]
Output: "9534330"
"""
import functools
import unittest
from typing import List


def sort_rule(x, y):
    return 1 if x + y > y + x else -1


def largest_number(nums: List[int]) -> str:
    str_nums = map(str, nums)
    sorted_nums = sorted(str_nums, key=functools.cmp_to_key(sort_rule), reverse=True)
    if sorted_nums[0] == '0':
        return '0'
    return ''.join(sorted_nums)


class TestSolutions(unittest.TestCase):
    def test_1(self):
        nums = [3, 30, 34, 5, 9]
        expected = "9534330"
        actual = largest_number(nums)
        self.assertEqual(expected, actual)
