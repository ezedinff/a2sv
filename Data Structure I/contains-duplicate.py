import unittest

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1,2,3,1]
        self.assertEqual(Solution().containsDuplicate(nums), True)
    def test_2(self):
        nums = [1,2,3,4]
        self.assertEqual(Solution().containsDuplicate(nums), False)