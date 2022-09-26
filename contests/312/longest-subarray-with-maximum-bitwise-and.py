# Longest Subarray with Maximum Bitwise AND

'''
you are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.

Example 2:
Input: nums = [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]
Output: 8

Example 3:
Input: nums = [100,5,5]
Output: 1
'''

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 1
        cur = None
        ln = 0
        mv = 0
        for n in nums:
            if n != cur:
                ln = 1
            else:
                ln += 1
            cur = n
            
            if n > mv:
                mx = 1
            elif n == mv:
                mx = max(mx, ln)
            mv = max(mv, n)
            
        return mx
        