import unittest
from typing import List

"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Constraints:
1 <= n <= 104
"""


def fizzBuzz(n: int) -> List[str]:
    return ["".join(s for d, s in [(3, "Fizz"), (5, "Buzz")] if i % d == 0) or str(i) for i in range(1, n + 1)]


class TestSolution(unittest.TestCase):
    def test_1(self):
        n = 3
        expected = ["1", "2", "Fizz"]
        result = fizzBuzz(n)
        self.assertEqual(expected, result)

    def test_2(self):
        n = 5
        expected = ["1", "2", "Fizz", "4", "Buzz"]
        result = fizzBuzz(n)
        self.assertEqual(expected, result)

    def test_3(self):
        n = 15
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                    "FizzBuzz"]
        result = fizzBuzz(n)
        self.assertEqual(expected, result)
