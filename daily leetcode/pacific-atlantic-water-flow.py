'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring
cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''

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