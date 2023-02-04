from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []

        nums.sort()
        m = {}
        for num in nums:
            m[num] = []

        for i in range(len(nums)):
            m[nums[i]].append(i)

        return m[target]