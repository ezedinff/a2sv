"""
https://leetcode.com/problems/reduce-array-size-to-the-half/
You are given an integer array arr. You can choose a set of integers and remove
all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2]
which has size 5 (i.e equal to half of the size of the old array). Possible sets of size 2 are
{3,5},{3,2},{5,2}. Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5]
which has a size greater than half of the size of the old array. """
import unittest
from typing import List


def minSetSize(arr: List[int]) -> int:
    d = {}
    for num in arr:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 0

    n = [v for v in d.values()]
    n.sort()

    total, ans = 0, 0
    for i in range(len(n) - 1, 0, -1):
        if total >= len(arr) // 2:
            break
        total += n[i]
        ans += 1

    return ans


class TestSolutions(unittest.TestCase):
    def test_1(self):
        arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
        expected = 2
        actual = minSetSize(arr)
        self.assertEqual(expected, actual)
