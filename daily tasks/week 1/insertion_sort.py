"""
Insertion Sort
https://www.hackerrank.com/challenges/insertionsort1/problem

Assume you are given the array arr = [1, 2, 4, 5, 3]  indexed 0...4 Store the value of arr[4] Now test lower index
values successively from 3 to 0 until you reach a value that is lower than arr[4], at arr[1]  in this case. Each time
your test fails, copy the value at the lower index to the current index and print your array. When the next lower
indexed value is smaller than , insert the stored value at the current index and print the entire array.


Example
input: n = 5 arr = [1, 2, 4, 5, 3]
Start at the rightmost index. Store the value of arr[4] = 3. Compare this to each
element to the left until a smaller value is reached. Here are the results as described:
1 2 4 5 5
1 2 4 4 5
1 2 3 4 5


sample Input
5
2 4 6 8 3

sample Output
2 4 6 8 8
2 4 6 6 8
2 4 4 6 8
2 3 4 6 8
"""
import string
import unittest


def insertion_sort(n: int, nums: list) -> string:
    steps = ""
    # Traverse through 1 to len(nums)
    for i in range(1, n):

        key = nums[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
            steps += " ".join([str(d) for d in nums]) + "\n"
        nums[j + 1] = key
    steps += " ".join([str(d) for d in nums])

    return steps


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [2, 4, 6, 8, 3]
        expected = "2 4 6 8 8\n2 4 6 6 8\n2 4 4 6 8\n2 3 4 6 8"
        result = insertion_sort(len(nums), nums)
        self.assertEqual(expected, result)