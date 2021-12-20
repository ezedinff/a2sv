"""
https://codeforces.com/problemset/problem/1/A
Theatre Square in the capital city of Berland has a rectangular shape with the size n×m meters. On the occasion of
the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of
the size a×a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the
Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones
should be parallel to the sides of the Square.

Input
The input contains three positive integer numbers in the first line: n,m and a (1 ≤ n,m,a ≤ 10^9).

Output
Write the needed number of flagstones.

        n | m | a
input:  6 | 6 | 4
output: 4


"""
import unittest
from typing import List


def theatreSquare(inputs: List[int]) -> int:
    n, m, a = inputs
    width, height = 0, 0

    if n % a == 0:
        width = n // a

    if n % a != 0:
        width = n // a + 1

    if m % a == 0:
        height = m // a

    if m % a != 0:
        height = m // a + 1

    return width * height


class TestSolution(unittest.TestCase):
    def test_1(self):
        inputs = [6, 6, 4]
        expected = 4
        actual = theatreSquare(inputs)
        self.assertEqual(expected, actual)
