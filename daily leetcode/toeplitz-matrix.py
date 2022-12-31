# Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
            # check if the matrix is empty
        if not matrix:
            return True
            # check if the matrix is a square matrix
        for row in matrix:
            if len(row) != len(matrix[0]):
                return False
            # check if the matrix is a Toeplitz matrix
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True