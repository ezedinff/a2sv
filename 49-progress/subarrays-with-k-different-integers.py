'''
992. Subarrays with K Different Integers
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
'''
from typing import List
from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            res = 0
            i = 0
            count = Counter()
            for j in range(len(nums)):
                count[nums[j]] += 1
                while len(count) > k:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        del count[nums[i]]
                    i += 1
                res += j - i + 1

            return res
        
        return atMostK(k) - atMostK(k - 1)
