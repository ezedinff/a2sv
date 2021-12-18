import unittest
from typing import List
"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element/

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
"""

def max_frequency(nums: List[int], k: int):
    nums.sort()
    maxFre = 1
    l, u = len(nums) - 1, len(nums) - 1
    while u >= maxFre:
        while l and k - (nums[u] - nums[l - 1]) >= 0:
            k -= nums[u] - nums[l - 1]
            l -= 1
        maxFre = max(maxFre, u - l + 1)
        k += (u - l) * (nums[u] - nums[u - 1])
        u -= 1
    return maxFre


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums, k = [1, 2, 4], 5
        expected = 3
        actual = max_frequency(nums, k)
        self.assertEqual(expected, actual)
