"""
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length. Reverse the sub-array arr[0...k-1] (0-indexed). For example,
if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,
4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that
sorts the array within 10 * arr.length flips will be judged as correct.


Example 1:

Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state:         arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [1, 4, 2, 3]
After 2nd flip (k = 2): arr = [4, 1, 2, 3]
After 3rd flip (k = 4): arr = [3, 2, 1, 4]
After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.


start from the last element index = len(arr)
- if the last element is in its place decrease value of index and check for the next element.
- if the last element is not in its place** find** the index of the element which must be in
this place. Then flip twice. The first flip is from zero to the index of the element. The second
- flip is from zero to the value of the element.
- If we flip twice we must append or push the number of flips into flips array. The first number of
- flips is the index of the element. The second number of flips is the value of the element.
After twice flipping go to the next elements
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
