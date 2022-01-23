# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4^x.
# Example 1:
# Input: n = 16
# Output: true

import unittest


def isPowerOfFour(n: int) -> bool:
    if n == 1:
        return True
    if n <= 0 or n % 4 != 0:
        return False
    return isPowerOfFour(n // 4)

class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(isPowerOfFour(16), True)
    def test_two(self):
        self.assertEqual(isPowerOfFour(5), False)
    def test_three(self):
        self.assertEqual(isPowerOfFour(1), True)


if __name__ == '__main__':
    unittest.main()