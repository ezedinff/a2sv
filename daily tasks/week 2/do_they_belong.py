# a triangle formed by three points a(x1,y1), b(x2,y2) and c(x3,y3) is a non-degenerate triangle if the following rules are respected(|ab| is the length of the line between points a and b):
# |ab| + |bc| > |ac|
# |bc| + |ac| > |ab|
# |ac| + |ab| > |bc|
# A point belongs to a triangle if it lies somewhere on or inside the triangle. Given two points p = (xp,yp) and q = (xq,yq), return the correct scenario number:
# 0: if the triangle abc does not form a valid non-degenerate triangle
# 1: if point p belongs to the triangle abc but point q does not
# 2: if point q belongs to the triangle abc but point p does not
# 3: if both point p and q belong to the triangle abc
# 4: if neither point p nor q belong to the triangle abc

# Example:
# x1, y1, x2, y2, x3, y3, xp, yp, xq, yq = 2, 2, 7, 2, 5, 4, 4, 3, 7, 4
# First, the triangle abc forms a valid non-degenerate triangle.
# |ab| = 7 - 2 = 5. |bc| = sqrt(7 - 5)^2 + (4 - 2)^2) = sqrt(2^2 + 2^2) = sqrt(8) = 2.828. |ac| = sqrt(5 - 2)^2 + (4 - 2)^2 = (3^2 + 2^2) = sqrt(13) = 3.464.
# |ab| + |bc| > |ac| => 5 + 2.828 > 3.464 => True.
# |bc| + |ac| > |ab| => 2.828 + 3.464 > 5 => True.
# |ac| + |ab| > |bc| => 3.464 + 5 > 2.828 => True.

# second, the point p(5, 4) belongs to the triangle abc and the point q(7, 4) does not as shown in the image.

# function description:
# pointsBelong has the following parameters:
# int x1, y1, x2, y2, x3, y3: integer coordinates of the three points of the triangle
# int xp, yp, xq, yq: integer coordinates of the two points to be p and q
# return:
# int: an integer that represents the correct scenario number

# Constraints:
# 0 <= x1, y1, x2, y2, x3, y3, xp, yp, xq, yq <= 2000

# Test Cases
# x1, y1, x2, y2, x3, y3, xp, yp, xq, yq = 3, 1, 7, 1, 5, 5, 3, 1, 0, 0
# Expected Output: 1

# Test Cases
# x1, y1, x2, y2, x3, y3, xp, yp, xq, yq = 3, 1, 7, 1, 5, 5, 1, 1, 2, 2
# Expected Output: 4

import math


def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq) -> int:
    # check if the triangle is valid
    if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3):
        return 0
    # calculate the length of the line between points a and b
    ab = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    # calculate the length of the line between points b and c
    bc = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    # calculate the length of the line between points a and c
    ac = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    # check if the triangle is valid
    if ab + bc <= ac or bc + ac <= ab or ac + ab <= bc:
        return 0
    # check if point p belongs to the triangle
    if (xp - x1)**2 + (yp - y1)**2 <= ab**2 and (xp - x2)**2 + (yp - y2)**2 <= bc**2 and (xp - x3)**2 + (yp - y3)**2 <= ac**2:
        # check if point q belongs to the triangle
        if (xq - x1)**2 + (yq - y1)**2 <= ab**2 and (xq - x2)**2 + (yq - y2)**2 <= bc**2 and (xq - x3)**2 + (yq - y3)**2 <= ac**2:
            return 3
        else:
            return 1
    else:
        # check if point q belongs to the triangle
        if (xq - x1)**2 + (yq - y1)**2 <= ab**2 and (xq - x2)**2 + (yq - y2)**2 <= bc**2 and (xq - x3)**2 + (yq - y3)**2 <= ac**2:
            return 2
        else:
            return 4
    

print(pointsBelong(3, 1, 7, 1, 5, 5, 3, 1, 0, 0))