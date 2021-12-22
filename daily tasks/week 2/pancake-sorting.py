"""
https://leetcode.com/problems/pancake-sorting/
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length. Reverse the sub-array arr[0...k-1] (0-indexed). For example,
if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,
4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that
sorts the array within 10 * arr.length flips will be judged as correct.

"""
import unittest
from typing import List


def pancake_flips(arr: List[int]) -> List[int]:
    length = len(arr)
    answer = []
    i = length
    while i > 0:
        max_local = max(arr[:i])
        if arr[i - 1] != max_local:
            k = arr.index(max_local)
            arr_left = arr[:k + 1]
            arr_right = arr[k + 1:]
            arr_left.reverse()
            arr = arr_left + arr_right
            answer.append(k + 1)

            arr_left = arr[:i]
            arr_right = arr[i:]
            arr_left.reverse()
            arr = arr_left + arr_right
            answer.append(i)
        i -= 1
    return answer


class TestSolution(unittest.TestCase):
    def test_1(self):
        arr = [3, 2, 4, 1]
        expected = [3, 4, 2, 3, 1, 2]
        actual = pancake_flips(arr)
        self.assertEqual(expected, actual)
