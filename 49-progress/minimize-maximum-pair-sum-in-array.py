from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        sums = []
        for i in range(size // 2 + 1):
            sums.append(nums[i] + nums[size - i - 1])

        return max(sums)