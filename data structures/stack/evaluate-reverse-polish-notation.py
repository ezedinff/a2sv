# Evaluate reverse polish notation

'''
Evaluate the value of an arithmetic expression in reverse polish notation
valid operators are +, -, *, and /

Example 1:
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
'''

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                stack.append(self.evaluate(token, stack.pop(), stack.pop()))
        return stack.pop()
    def evaluate(self, op, b, a):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return int(a / b)
        else:
            raise ValueError(f"illegal operand was found: {op}")

if __name__ == "__main__":
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    solution = Solution()
    print(solution.evalRPN(tokens))