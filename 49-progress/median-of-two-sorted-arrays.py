'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
from typing import List
class Solution:
    # using binary search
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # make sure nums1 is the shorter one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        # binary
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            # check if i is too small
            if i < m and nums2[j - 1] > nums1[i]:
                left = i + 1
            # check if i is too big
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            # i is perfect
            else:
                # get max of left
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                # if total number is odd
                if (m + n) % 2 == 1:
                    return max_of_left
                # get min of right
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0
            
            
            