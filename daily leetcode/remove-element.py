import unittest

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        solution = Solution()
        self.assertEqual(solution.removeElement([3, 2, 2, 3], 3), 2)
        self.assertEqual(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)