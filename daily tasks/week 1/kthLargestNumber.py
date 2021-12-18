"""
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading
zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest
integer, "2" is the second-largest integer, and "1" is the third-largest integer.

Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".
"""
import unittest
from typing import List


def kthLargestNumber(nums: List[str], k: int) -> str:
    nums = [int(num) for num in nums]
    nums.sort()
    return str(nums[-k])


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums, k = ["3", "6", "7", "10"], 4
        expected = "3"
        actual = kthLargestNumber(nums, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums, k = ["0", "0"], 2
        expected = "0"
        actual = kthLargestNumber(nums, k)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums, k = ["2", "21", "12", "1"], 3
        expected = "2"
        actual = kthLargestNumber(nums, k)
        self.assertEqual(expected, actual)
