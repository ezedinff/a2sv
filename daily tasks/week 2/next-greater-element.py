import unittest
from typing import List

"""
https://leetcode.com/problems/next-greater-element-i/

The next greater element of some element x in an array is the first greater element that is to the right of x in 
the same array. 

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater 
element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1. 

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""


# without stack
# def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
#     res = [-1] * len(nums1)
#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
#             if nums1[i] == nums2[j]:
#                 if j + 1 != len(nums2) and nums1[i] < nums2[j + 1]:
#                     res[i] = nums2[j + 1]
#     return res


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    # stack to contain greater elements in decreasing order.
    # the top of stack is smaller than the elements in the stack
    stack = []

    # hash map for storing next greater element of each
    next_greater_mp = {}

    # start from the right
    i = len(nums2) - 1

    while i >= 0:
        # pop until you get a greater value
        while stack and nums2[i] >= nums2[stack[-1]]:
            stack.pop()
        # if the stack is not empty next greater element of the current element is the element on top of stack
        if stack:
            next_greater_mp[nums2[i]] = nums2[stack[-1]]
        # else does not have greater element
        else:
            next_greater_mp[nums2[i]] = -1
        stack.append(i)
        i -= 1

    for i, j in enumerate(nums1):
        nums1[i] = next_greater_mp[j]
    return nums1


class TestSolutions(unittest.TestCase):
    def test_1(self):
        nums1, nums2 = [4, 1, 2], [1, 3, 4, 2]
        expected = [-1, 3, -1]
        actual = nextGreaterElement(nums1, nums2)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums1, nums2 = [2, 4], [1, 2, 3, 4]
        expected = [3, -1]
        actual = nextGreaterElement(nums1, nums2)
        self.assertEqual(expected, actual)

