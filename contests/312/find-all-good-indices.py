# Find All Good Indices

'''
You are given a 0-indexed integer array nums of size n and a positive integer k.

We call an index i in the range k <= i < n - k good if the following conditions are satisfied:

The k elements that are just before the index i are in non-increasing order.
The k elements that are just after the index i are in non-decreasing order.
Return an array of all good indices sorted in increasing order.

Input: nums = [2,1,1,1,3,4,1], k = 2
Output: [2,3]
Explanation: There are two good indices in the array:
- Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
- Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
Note that the index 4 is not good because [4,1] is not non-decreasing.

Input: nums = 
'''

from typing import List
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l, r = [0] * n, [0] * n
        l[0] = r[-1] = 1
        
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                l[i] = l[i-1] + 1
            else:
                l[i] = 1
        
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                r[i] = r[i+1] + 1
            else:
                r[i] = 1
                
        ret = []
        for i in range(k, n-k):
            if l[i-1] >= k and r[i+1] >= k:
                ret.append(i)
        return ret
                        