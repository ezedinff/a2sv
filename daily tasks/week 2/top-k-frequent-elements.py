"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
import unittest
from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    frequencies = Counter(nums)
    return [items[0] for items in frequencies.most_common()[:k]]


class TestSolutions(unittest.TestCase):
    def test_1(self):
        nums, k = [1, 1, 1, 2, 2, 3], 2
        expected = [1, 2]
        actual = topKFrequent(nums, k)
        self.assertEqual(expected, actual)
