# You are given a positive integer p. Consider an array nums (1-indexed) that consists of the integers in the inclusive range [1, 2p - 1] in their binary representations. You are allowed to do the following operation any number of times:
# choose two elements x and y from nums
# choose a bit in x and swap it with bit in y, corresponding bits refers to the bit that is in the same position in other integers.

# For example, if x = 1101 and y = 0011, after swapping the 2nd bit from the right, we have x = 1111 and y = 0001.
# Find the minimum non-zero product of nums after performing the above operation any number of times. Return this product modulo 109 + 7.

# Note: The answer should be the minimum product before the modulo operation is done.

# Example 1:
# Input: p = 1
# Output: 1
# Explanation: nums = [1].
# There is only one element, so the product equals that element.

# Example 2:
# Input: p = 2
# Output: 6
# Explanation: nums = [01, 10, 11].
# Any swap would either make the product 0 or stay the same.
# Thus, the array product of 1 * 2 * 3 = 6 is already minimized.

import unittest


def minNonZeroProduct(p: int) -> int:
    
    m = (10**9+7)

    def myPow( x, n):
        if n < 0:
            x = 1/x
        n = abs(n)
        if n == 0:
            return 1
        temp = myPow(x,n//2)
        if n%2 == 0:
            return temp* temp % m
        else:
            return x * temp * temp %m

    num = (2**p)-1
    res = myPow(num-1,num//2)
    return res * num % m


class TestSolution(unittest.TestCase):
    def test_case(self):
        self.assertEqual(minNonZeroProduct(1), 1)
        self.assertEqual(minNonZeroProduct(2), 6)


if __name__ == '__main__':
    unittest.main()