import unittest
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        result = []
        for num in nums:
            if num in d:
                result.append(num)
            else:
                d[num] = 1
        
        for i in range(1, len(nums) + 1):
            if i not in d:
                result.append(i)
        return result

class Test(unittest.TestCase):
    def test1(self):
        nums = [1,2,2,4]
        self.assertEqual(Solution().findErrorNums(nums), [2,3])
    def test2(self):
        nums = [1,1]
        self.assertEqual(Solution().findErrorNums(nums), [1,2])

if __name__ == '__main__':
    unittest.main()