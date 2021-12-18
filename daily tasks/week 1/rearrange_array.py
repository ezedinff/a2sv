import unittest
from typing import List

"""
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such 
that every element in the rearranged array is not equal to the average of its neighbors. 

More formally, the rearranged array should have the property such that for every i in the range 
1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i]. 

Return any rearrangement of nums that meets the requirements.

Input: nums = [1,2,3,4,5]
Output: [1,5,2,4,3]
Explanation:
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.

"""


def rearrange_array(nums: List[int]) -> List[int]:
    nums.sort()
    res = []
    ls = len(nums)
    l, r = 0, ls - 1
    while len(res) != ls:
        res.append(nums[l])
        l += 1
        if l <= r:
            res.append(nums[r])
            r -= 1
    return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 5, 2, 4, 3]
        actual = rearrange_array(nums)
        self.assertEqual(expected, actual)
