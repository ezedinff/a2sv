"""
STACK
https://leetcode.com/problems/evaluate-reverse-polish-notation/
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a
result, and there will not be any division by zero operation.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""
import math
import unittest
from typing import List


def evalRPN(tokens: List[str]) -> int:
    if not len(tokens):
        return 0

    stack = []
    operations = "+-/*"

    for token in tokens:
        if token in operations:
            firstNumber = stack.pop()
            secondNumber = stack.pop()
            if token == "+":
                stack.append(firstNumber + secondNumber)
            elif token == "-":
                stack.append(secondNumber - firstNumber)
            elif token == "*":
                stack.append(firstNumber * secondNumber)
            elif token == "/":
                if secondNumber / firstNumber < 0:
                    stack.append(math.ceil(secondNumber / firstNumber))
                else:
                    stack.append(math.floor(secondNumber / firstNumber))
        else:
            stack.append(int(token))
    return stack[0]


class TestSolution(unittest.TestCase):
    def test_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9
        actual = evalRPN(tokens)
        self.assertEqual(expected, actual)

    def token_2(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        expected = 22
        actual = evalRPN(tokens)
        self.assertEqual(expected, actual)