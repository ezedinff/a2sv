from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                ans[j][i] = matrix[i][j]
        return ans
