# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = "3/2"
# Output: 1

import unittest


def calculate(s) -> int:
    # Write your code here
    if not s:
        # print(s)
        return 0
    stack = []
    num = 0
    sign = '+'
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if s[i] in ['+', '-', '*', '/'] or i == len(s) - 1:
            # print(s[i])
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            sign = s[i]
            num = 0
    return sum(stack)



class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calculate("3+2*2"), 7)
    def test_2(self):
        self.assertEqual(calculate("3/2"), 1)


if __name__ == '__main__':
    unittest.main()
