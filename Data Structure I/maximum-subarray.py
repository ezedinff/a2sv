import unittest

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum

class TestSolution(unittest.TestCase):
    def test_maxSubArray(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(Solution().maxSubArray(nums), 6)