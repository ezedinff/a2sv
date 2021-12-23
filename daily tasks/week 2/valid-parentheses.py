import unittest

"""
@author Ezedin Fedlu

STACK

https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def isValid(s: str) -> bool:
    stack = []
    openings = "({["
    for c in s:
        if c in openings:
            stack.append(c)
        elif len(stack) == 0:
            return False
        elif c == ")" and stack.pop() != "(":
            return False
        elif c == "]" and stack.pop() != "[":
            return False
        elif c == "}" and stack.pop() != "{":
            return False

    return len(stack) == 0


class TestSolutions(unittest.TestCase):
    def test_1(self):
        expected = False
        actual = isValid("(]")
        self.assertEqual(expected, actual)

    def test_2(self):
        expected = True
        actual = isValid("()[]{}")
        self.assertEqual(expected, actual)
