import unittest
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        for L in range(len(nums)):
            if nums[L] == 0:
                break
        for R in range(L+1, len(nums)):
            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L = L + 1
                R = R + 1

        return nums


class Test(unittest.TestCase):
    def test_applyOperations(self):
        self.assertEqual(Solution().applyOperations(
            [1, 2, 2, 1, 1, 0]), [1, 4, 2, 0, 0, 0])
        self.assertEqual(
            Solution().applyOperations([847, 847, 0, 0, 0, 399, 416, 416, 879, 879, 206, 206, 206, 272]), [1694, 399, 832, 1758, 412, 206, 272, 0, 0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
