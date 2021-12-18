"""
bubble sort
for (int i = 0; i < n; i++) {

    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }

}

Example
a = [6,4,1]

1       [4,6,1]
2       [4,1,6]
3       [1,4,6]

output:
Array is sorted in 3 swaps.
First Element: 1
Last Element: 6
"""
import string
import unittest


def bubble_sort(nums: list) -> string:
    swaps = 0
    template = "Array is sorted in {swaps} swaps.\nFirst Element: {firstElement}\nLast Element: {lastElement}"
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swaps += 1

    return template.format(swaps=swaps, firstElement=nums[0], lastElement=nums[-1])


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [6, 4, 1]
        expected = "Array is sorted in 3 swaps.\nFirst Element: 1\nLast Element: 6"
        result = bubble_sort(nums)
        self.assertEqual(expected, result)
