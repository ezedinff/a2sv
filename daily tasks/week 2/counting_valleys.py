"""
https://www.hackerrank.com/challenges/counting-valleys/problem
- A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending
with a step down to sea level.

- A valley is a sequence of consecutive steps below sea level, starting with a step down
from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

sample input:
8
UDDDUDUU

Sample Output
1

Explanation
If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

_/\      _
   \    /
    \/\/
"""
import unittest


def countingValleys(steps, path):
    sea_level = 0
    num_of_valley = 0
    for step in path:
        if step == 'D':
            sea_level -= 1

        if step == 'U':
            sea_level += 1

        if sea_level == 0 and step == 'U':
            num_of_valley += 1

    return num_of_valley


class TestSolution(unittest.TestCase):
    def test_1(self):
        steps, path = 8, 'UDDDUDUU'
        expected = 1
        actual = countingValleys(steps, path)
        self.assertEqual(expected, actual)
