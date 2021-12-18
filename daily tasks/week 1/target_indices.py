import unittest
from typing import List

"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/

You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target 
indices, return an empty list. The returned list must be sorted in increasing order.
 
 
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
"""


def target_indices(nums: List[int], target: int) -> List[int]:
    if target not in nums:
        return []

    nums.sort()
    m = {}
    for num in nums:
        m[num] = []

    for i in range(len(nums)):
        m[nums[i]].append(i)

    return m[target]


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums, target = [1, 2, 5, 2, 3], 2
        expected = [1, 2]
        actual = target_indices(nums, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums, target = [1, 2, 5, 2, 3], 4
        expected = []
        actual = target_indices(nums, target)
        self.assertEqual(expected, actual)
