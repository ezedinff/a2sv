# Maximum Score from Performing Multiplication Operations

'''
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

Example 1:
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14

https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
'''

from typing import List

class Solution:
        # iterative dp solution
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # number of operations
        m = len(multipliers)
        # for highet pointer
        n = len(nums)
        memo = {}

        def dp(op, left):
            if op == m:
                return 0

            # If already computed, return
            if (op, left) in memo:
                return memo[(op, left)]

            l = nums[left] * multipliers[op] + dp(op+1, left+1)
            r = nums[(n-1)-(op-left)] * multipliers[op] + dp(op+1, left)

            memo[(op, left)] = max(l, r)

            return memo[(op, left)]

        # Zero operation done in the beginning
        return dp(0, 0)

        


if __name__ == "__main__":
    nums = [1,2,3]
    multipliers = [3,2,1]
    assert Solution().maximumScore(nums, multipliers) == 14