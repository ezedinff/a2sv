"""

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""
import unittest
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) <= 1:
        return intervals

    intervals.sort()
    result = []
    low, high = None, None
    for i in range(len(intervals)):
        interval = intervals[i]
        if low == high is None:
            low, high = interval[0], interval[1]

        elif high >= interval[0] and interval[1] >= low:
            low = min(interval[0], low)
            high = max(interval[1], high)

        else:
            result.append([low, high])
            low, high = interval[0], interval[1]

    if low is not None and high is not None:
        result.append([low, high])

    return result


class TestSolution(unittest.TestCase):
    def test_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        actual = merge(intervals)
        self.assertEqual(expected, actual)

    def test_2(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        actual = merge(intervals)
        self.assertEqual(expected, actual)

    def test_3(self):
        intervals = [[1, 4], [1, 4]]
        expected = [[1, 4]]
        actual = merge(intervals)
        self.assertEqual(expected, actual)
