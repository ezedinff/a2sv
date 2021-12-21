"""
https://leetcode.com/problems/arithmetic-subarrays/
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between
every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] ==
s[1] - s[0] for all valid i

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic:

1, 1, 2, 5, 7


You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range
queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed. """
import unittest
from typing import List


def checkArithmeticSubArrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    result = []
    for left, right in zip(l, r):
        max_num, min_num, lookup = max(nums[left:right + 1]), min(nums[left:right + 1]), set(nums[left:right + 1])
        if max_num == min_num:
            result.append(True)

        dividend, remainder = divmod(max_num - min_num, len(nums[left:right + 1]) - 1)
        if remainder:
            result.append(False)
        else:
            if dividend:
                result.append(all(i in lookup for i in range(min_num, max_num, dividend)))
    return result


class TestSolutions(unittest.TestCase):
    def test_1(self):
        nums, l, r = [-3, -6, -8, -4, -2, -8, -6, 0, 0, 0, 0], [5, 4, 3, 2, 4, 7, 6, 1, 7], [6, 5, 6, 3, 7, 10, 7, 4, 10]
        expected = [True, True, True, True, False, True, True, True, True]
        actual = checkArithmeticSubArrays(nums, l, r)
        self.assertEqual(expected, actual)
