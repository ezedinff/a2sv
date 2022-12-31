# Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# hard
'''
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
'''
class Solution:
     def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # BFS
        # 1. create a queue
        queue = []
        # 2. add the starting point to the queue
        queue.append((0, 0, k))
        # 3. while the queue is not empty
        visited = set()
        visited.add((0, 0, k))
        distance = 0
        while queue:
            # 4. pop the first element from the queue
            size = len(queue)
            for i in range(size):
                point = queue.pop(0)
                x, y, k = point
                # 5. if the popped element is the destination, return the distance
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return distance
                # 6. for each of the 4 directions, check if the new point is valid
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newX = x + dx
                    newY = y + dy
                    if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]):
                        if grid[newX][newY] == 0:
                            if (newX, newY, k) not in visited:
                                queue.append((newX, newY, k))
                                visited.add((newX, newY, k))
                        elif grid[newX][newY] == 1 and k > 0:
                            if (newX, newY, k - 1) not in visited:
                                queue.append((newX, newY, k - 1))
                                visited.add((newX, newY, k - 1))
            distance += 1
        return -1
