import unittest
from typing import List

"""
https://leetcode.com/problems/sort-colors/submissions/

sort nums inplace
"""


def sort_colors(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        expected = [0, 0, 1, 1, 2, 2]
        actual = sort_colors(nums)
        self.assertEqual(expected, actual)
