# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
from typing import List
import unittest


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Write your code here
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        res = []
        while left <= right and top <= bottom:
            # print(left, right, top, bottom)
            for i in range(left, right + 1):
                # print(i)
                res.append(matrix[top][i])
            for i in range(top + 1, bottom):
                # print(i)
                res.append(matrix[i][right])
            for i in reversed(range(left, right + 1)):
                # print(i)
                if top < bottom:
                    res.append(matrix[bottom][i])
            for i in reversed(range(top + 1, bottom)):
                # print(i)
                if left < right:
                    res.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res


class TestSolution(unittest.TestCase):
    def test_one(self):
        s = Solution()
        self.assertEqual(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])


if __name__ == '__main__':
    unittest.main()
