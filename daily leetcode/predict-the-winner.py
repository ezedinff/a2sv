from typing import List


class Solution:
    cache = {}

    def PredictTheWinner(self, nums: List[int]) -> bool:
        return 0 <= self.min_max(nums, 0, len(nums) - 1, 1)

    def min_max(self, nums: List[int], i: int, j: int, turn: int):
        if i == j:
            return turn * nums[i]
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        a = turn * nums[i] + self.min_max(nums, i + 1, j, -turn)
        b = turn * nums[j] + self.min_max(nums, i, j - 1, -turn)
        self.cache[(i, j)] = turn * max(turn * a, turn * b)
        return self.cache[(i, j)]


s = Solution()
print(s.PredictTheWinner([1, 2]))
