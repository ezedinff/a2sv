# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.
# Example 1:
# Input: n = 27
# Output: true
# Example 2:
# Input: n = 0
# Output: false
# Example 3:
# Input: n = 9
# Output: true
import unittest


def isPowerOfThree(n: int) -> bool:
    if n == 1:
        return True
    if n <= 0 or n % 3 != 0:
        return False
    return isPowerOfThree(n // 3)


class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(isPowerOfThree(27), True)
    def test_two(self):
        self.assertEqual(isPowerOfThree(0), False)
    def test_three(self):
        self.assertEqual(isPowerOfThree(9), True)


if __name__ == '__main__':
    unittest.main()
    