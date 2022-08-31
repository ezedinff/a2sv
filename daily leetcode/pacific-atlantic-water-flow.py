import unittest

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        for i in range(m):
            self.dfs(heights, i, 0, pacific)
            self.dfs(heights, i, n-1, atlantic)
        for j in range(n):
            self.dfs(heights, 0, j, pacific)
            self.dfs(heights, m-1, j, atlantic)
        return pacific & atlantic

    def dfs(self, heights, i, j, visited):
        m, n = len(heights), len(heights[0])
        if (i, j) in visited:
            return
        visited.add((i, j))
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                self.dfs(heights, x, y, visited)

class TestSolution(unittest.TestCase):
    def test_pacificAtlantic(self):
        heights = [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ]
        self.assertEqual(Solution().pacificAtlantic(heights), [
            [0,4],
            [1,3],
            [1,4],
            [2,2],
            [3,0],
            [3,1],
            [4,0]
        ])