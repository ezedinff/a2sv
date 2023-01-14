from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # find the coordinates of the black queens that can directly
        # attack the king on a 8x8 chessboard.
        
        # list of tuples (x-axis, y-axis) of the 8 directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queens_set = set(tuple(queen) for queen in queens)
        coordinates = []
        for dx, dy in directions:
            kx, ky = king[0] + dx, king[1] + dy
            while 0 <= kx < 8 and 0 <= ky < 8:
                if (kx, ky) in queens_set:
                    coordinates.append([kx, ky])
                    break
                kx += dx
                ky += dy
        return coordinates