"""
https://leetcode.com/problems/find-original-array-from-doubled-array/
An integer array original is transformed into a doubled array changed by appending twice the value of every
element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array,
return an empty array. The elements in original may be returned in any order.

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]

Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
"""
import unittest
from typing import List
from collections import Counter


def findOriginalArray(changed: List[int]) -> List[int]:
    if not changed or len(changed) % 2 == 1:
        return []
    num2cnt = Counter(changed)

    # NlogN
    sorted_nums = sorted(changed)
    small_nums = []
    for num in sorted_nums:
        if num not in num2cnt:
            continue
        doubled_num = num * 2
        if doubled_num not in num2cnt:
            return []

        small_nums.append(num)
        num2cnt[num] -= 1
        if num2cnt[num] == 0:
            del num2cnt[num]
        num2cnt[doubled_num] -= 1
        if num2cnt[doubled_num] == 0:
            del num2cnt[doubled_num]

    return small_nums


class TestSolution(unittest.TestCase):
    def test_1(self):
        changed = [1, 3, 4, 2, 6, 8]
        expected = [1, 3, 4]
        actual = findOriginalArray(changed)
        self.assertEqual(expected, actual)
