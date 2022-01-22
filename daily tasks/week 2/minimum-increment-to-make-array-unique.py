# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
# Example 1:
# Input: nums = [1,2,2]
# Output: 2
# Explanation: You cannot simply select index 1 twice without losing any of the numbers. The optimal way is to move the two elements at index 0 and 2 to index 1.
# Example 2:
# Input: nums = [3,2,1,2,1,7]
# Output: 6
# Explanation: You can select index 1 or index 5.

from typing import List
import unittest


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return res

class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        self.assertEqual(s.minIncrementForUnique([1,2,2]), 2)
    def test_two(self):
        s = Solution()
        self.assertEqual(s.minIncrementForUnique([3,2,1,2,1,7]), 6)


if __name__ == '__main__':
    unittest.main()