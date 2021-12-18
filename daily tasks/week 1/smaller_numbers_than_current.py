import unittest
from typing import List

"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
that is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.


Example
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""


def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    counts = [0 for i in range(len(nums))]

    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i and nums[j] < nums[i]:
                counts[i] += 1

    return counts


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [8, 1, 2, 2, 3]
        expected = [4, 0, 1, 1, 3]
        result = smaller_numbers_than_current(nums)
        self.assertEqual(expected, result)
