"""
https://codeforces.com/problemset/problem/50/A

You are given a rectangular board of M×N squares. Also you are given an unlimited number of standard domino pieces of
2×1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board
so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.


example
input: m = 2 and n = 4
output: 4 the maximal number of dominoes, which can be placed.
"""
import unittest


def domino_piling(m: int, n: int) -> int:
    area = m * n  # area of the container
    area_of_piece = 2 * 1
    return area // area_of_piece


class TestSolution(unittest.TestCase):
    def test_1(self):
        m, n = 2, 4
        expected = 4
        result = domino_piling(m, n)
        self.assertEqual(expected, result)

    def test_2(self):
        m, n = 3, 3
        expected = 4
        result = domino_piling(m, n)
        self.assertEqual(expected, result)
