"""
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that
the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
"""
import unittest
from collections import deque
from typing import List


def longestSubarray(nums: List[int], limit: int) -> int:
    hi = deque()
    lo = deque()
    ans = 0
    i = 0
    for j in range(len(nums)):
        while hi and nums[hi[-1]] <= nums[j]:
            hi.pop()
        while lo and nums[lo[-1]] >= nums[j]:
            lo.pop()
        hi.append(j)
        lo.append(j)
        if len(hi) == 1:
            while nums[hi[0]] - nums[lo[0]] > limit:
                ans = max(ans, j - i)
                i = lo.popleft() + 1
        elif len(lo) == 1:
            while nums[hi[0]] - nums[lo[0]] > limit:
                ans = max(ans, j - i)
                i = hi.popleft() + 1
    return max(ans, j - i + 1)


class TestSolution(unittest.TestCase):
    def test_one(self):
        nums, limit = [4, 2, 2, 2, 4, 4, 2, 2], 0
        expected = 3
        output = longestSubarray(nums, limit)
        self.assertEqual(expected, output)

    def test_two(self):
        nums, limit = [10, 1, 2, 4, 7, 2], 5
        expected = 4
        output = longestSubarray(nums, limit)
        self.assertEqual(expected, output)