"""
https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
"""
import unittest
from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    count = 0
    leftPointer, rightPointer = 0, len(nums) - 1
    while leftPointer < rightPointer:
        if nums[leftPointer] == nums[rightPointer]:
            count += 1
        rightPointer -= 1

        if leftPointer == rightPointer:
            leftPointer += 1
            rightPointer = len(nums) - 1

    return count


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 1, 1, 3]
        expected = 4
        actual = numIdenticalPairs(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1, 1, 1, 1]
        expected = 6
        actual = numIdenticalPairs(nums)
        self.assertEqual(expected, actual)