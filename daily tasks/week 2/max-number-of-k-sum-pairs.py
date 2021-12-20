import unittest
from typing import List

"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.


Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
"""

"""
MyFirst Attempt, got time limit exceeded with big input
def maxOperations(nums: List[int], k: int) -> int:
        operations = 0
        removedItems = list()
        leftPointer, rightPointer = 0, len(nums) - 1
        while leftPointer < rightPointer:

            if nums[leftPointer] + nums[rightPointer] == k \
                    and leftPointer not in removedItems \
                    and rightPointer not in removedItems:
                removedItems.append(leftPointer)
                removedItems.append(rightPointer)
                operations += 1

            rightPointer -= 1

            if leftPointer == rightPointer:
                leftPointer += 1
                rightPointer = len(nums) - 1

        return operations
"""


def maxOperations(nums: List[int], k: int) -> int:
    operations = 0
    d = {}

    for num in nums:
        if num in d and d[num] > 0:
            operations += 1
            d[num] -= 1

        elif num < k:
            if k - num not in d:
                d[k - num] = 1
            else:
                d[k - num] += 1

    return operations


class TestSolutions(unittest.TestCase):
    def test_1(self):
        nums, k = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2
        expected = 2
        actual = maxOperations(nums, k)
        self.assertEqual(expected, actual)