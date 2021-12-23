"""

https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.


Example 1:

Input: s = "(abcd)"
Output: "dcba"



Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
"""
import unittest


def reverseParentheses(s: str) -> str:
    stack = []
    for c in s:
        if c != ")":
            stack.append(c)
        else:
            temp = ""
            while stack != [] and stack[-1] != "(":
                temp += stack.pop()

            stack.pop()
            stack.append(temp[::-1])

    for i in range(len(stack)):
        stack[i] = stack[i][::-1]

    return "".join(stack)


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "(ed(et(oc))el)"
        expected = "leetcode"
        actual = reverseParentheses(s)
        self.assertEqual(expected, actual)
