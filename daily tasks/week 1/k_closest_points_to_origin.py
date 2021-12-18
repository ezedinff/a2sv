"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].


Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""
import math
import unittest
from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    distances = []
    m = {}
    for point in points:
        x1, x2, y1, y2 = point[0], 0, point[1], 0
        d = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
        distances.append(d)
        m[d] = point

    distances.sort()

    return [m[distance] for distance in distances[:k]]


class TestSolution(unittest.TestCase):
    def test_1(self):
        points, k = [[1, 3], [-2, 2]], 1
        expected = [[-2, 2]]
        actual = k_closest(points, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        points, k = [[3, 3], [5, -1], [-2, 4]], 2
        expected = [[3, 3], [-2, 4]]
        actual = k_closest(points, k)
        self.assertEqual(expected, actual)
