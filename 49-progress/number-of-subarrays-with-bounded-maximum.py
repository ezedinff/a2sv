'''
795. Number of Subarrays with Bounded Maximum
Medium
2K
105
Companies
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7

'''
from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countSubarrays(nums, bound):
            count = 0
            start = 0
            for i in range(len(nums)):
                if nums[i] <= bound:
                    count += i - start + 1
                else:
                    start = i + 1
            return count
        return countSubarrays(nums, right) - countSubarrays(nums, left - 1)
    
s = Solution()
print(s.numSubarrayBoundedMax([2,1,4,3], 2, 3))
print(s.numSubarrayBoundedMax([2,9,2,5,6], 2, 8))
print(s.numSubarrayBoundedMax([73,55,36,5,55,14,9,7,72,52], 32, 69))

'''
The solution uses a sliding window approach to count the number of subarrays that meet 
the requirements. The count variable is used to keep track of the number of subarrays that
meet the requirements, and start is the starting index of the current subarray. The loop iterates
through the array nums, and if the current element is less than left, it means the current element cannot be the maximum value of any subarray that includes it, so the number of subarrays that can be formed by including this element is equal to the number of subarrays that can be formed using the elements from the start index up to the current index i, which is i - start. If the current element is greater than right, it means the current subarray cannot be included in the count, so the start index is updated to i + 1 to start a new subarray. Finally, if the current element is between left and right, it means the current element can be the maximum value of a subarray, and the number of subarrays that can be formed by including this element is equal to the number of subarrays that can be formed using the elements from the start index up to the current index i, plus the current element itself, which is i - start + 1.

At the end of the loop, the count variable contains the number of subarrays that meet the requirements, which is returned as the final answer.

'''