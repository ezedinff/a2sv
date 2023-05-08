from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(first = 0, curr = []):
            output.append(curr[:])
            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        backtrack()
        return output