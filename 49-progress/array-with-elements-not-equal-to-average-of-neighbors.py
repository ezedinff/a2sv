from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        i, j = 0, len(nums) - 1
        while i <= j:
            result.append(nums[i])
            i += 1
            if i <= j:
                result.append(nums[j])
                j -= 1
        return result
