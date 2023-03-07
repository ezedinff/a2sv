'''
1861. Rotating the Box
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.
'''
from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        res = [['.'] * m for _ in range(n)]
        for i in range(m):
            j = n - 1
            while j >= 0:
                if box[i][j] == '#':
                    k = j
                    while k < n - 1 and box[i][k + 1] == '.':
                        box[i][k], box[i][k + 1] = box[i][k + 1], box[i][k]
                        k += 1
                j -= 1
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = box[i][j]
        return res
    
    '''
    Intituion:
    1. Rotate the box 90 degrees clockwise
    2. For each row, move all stones to the right as far as possible
    3. Rotate the box 90 degrees counter-clockwise

    time complexity: O(mn)
    space complexity: O(mn)
    '''

class Solution:
    # idea:
    #   each row in input array is independent and can be processed separately
    # how to process each row:
    #   we need to move stones ("#") to empty spaces (".") from left to right
    #   since it's only move from left to rigth, we can iterate from the end of the row
    #   and keep in memory the last non-obstacle space where we can move stones
    # and at the end we just need to rotate array
    
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            move_position = len(row) - 1             # initialize with the last position in row
            for j in range(len(row) - 1, -1, -1):    # iterate from the end of the row
                if row[j] == "*":                    # we cannot move stones behind obstacles,
                    move_position = j - 1            # so update move position to the first before obstacle
                elif row[j] == "#":                  # if stone, move it to the "move_position"
                    row[move_position], row[j] = row[j], row[move_position]
                    move_position -= 1

        return zip(*box[::-1])