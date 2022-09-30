# The Skyline Problem

# https://leetcode.com/problems/the-skyline-problem/

'''
Example 1:
input: [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
'''
from typing import List

class Solution:
    # using heapq
    # technique is to find the left most and right most points
    # we can then create a list of points
    # we can then sort the points
    # we can then create a heap
    # we can then create a list of results
    # we can then iterate through the points
    # if the point is a left point
    # we can then add the point to the heap
    # if the point is a right point
    # we can then remove the point from the heap
    # we can then sort the heap
    # we can then return the results
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq
        heap = []
        results = []
        i = 0
        while i < len(buildings) or heap:
            if not heap or i < len(buildings) and buildings[i][0] <= -heap[0][1]:
                x = buildings[i][0]
                while i < len(buildings) and buildings[i][0] == x:
                    heapq.heappush(heap, [-buildings[i][2], -buildings[i][1]])
                    i += 1
            else:
                x = -heap[0][1]
                while heap and -heap[0][1] <= x:
                    heapq.heappop(heap)
            h = len(heap) and -heap[0][0]
            if not results or results[-1][1] != h:
                results.append([x, h])
        return results

if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) == [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]