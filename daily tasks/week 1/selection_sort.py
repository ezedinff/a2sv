"""
https://practice.geeksforgeeks.org/problems/selection-sort/1
Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

Input:
N = 5
arr[] = {4, 1, 3, 9, 7}

Output:
1 3 4 7 9

Explanation:
Maintain sorted (in bold) and unsorted subarrays.
Select 1. Array becomes 1 4 3 9 7.
Select 3. Array becomes 1 3 4 9 7.
Select 4. Array becomes 1 3 4 9 7.
Select 7. Array becomes 1 3 4 7 9.
Select 9. Array becomes 1 3 4 7 9.
"""
import unittest


def select(nums: list, i: int):
    return nums[i]


def selectionSort(nums: list, n: int) -> list:
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[j] < select(nums, i):
                nums[i], nums[j] = nums[j], nums[i]
    return nums


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [4, 1, 3, 9, 7]
        expected = [1, 3, 4, 7, 9]
        result = selectionSort(nums, len(nums))
        self.assertEqual(expected, result)
