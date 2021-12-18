"""
https://leetcode.com/problems/sorting-the-sentence/

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
"""
import unittest


def sort_sentence(s: str) -> str:
    m = {}
    words = s.split(" ")
    for word in words:
        m[int(word[-1])] = word[:len(word) - 1]

    keys = [k for k in m.keys()]
    keys.sort()

    return " ".join([m[key] for key in keys])


class TestSolution(unittest.TestCase):
    def test_1(self):
        expected = "This is a sentence"
        s = 'is2 sentence4 This1 a3'
        result = sort_sentence(s)
        self.assertEqual(expected, result)
