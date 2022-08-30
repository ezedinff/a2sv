import unittest

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        return matrix

class TestSolution(unittest.TestCase):
    def test_rotate(self):
        matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ])
