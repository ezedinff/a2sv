'''
A bracket sequence is called regular if it is possible to obtain correct
arithmetic expression by inserting characters «+» and «1» into this sequence.
For example, sequences «(())()», «()» and «(()(()))» are regular, while «)(», «(()» and «(()))(» are not.

One day Johnny got bracket sequence. He decided to remove some of the brackets
from it in order to obtain a regular bracket sequence.
What is the maximum length of a regular bracket sequence which can be obtained?

Input
Input consists of a single line with non-empty string of «(» and «)» characters. Its length does not exceed 106.

Output
Output the maximum possible length of a regular bracket sequence.

Examples
inputCopy
(()))(
outputCopy
4
inputCopy
((()())
outputCopy
6
'''

def main():
    # Read input string
    s = input()

    # Initialize stack
    stack = []

    # Iterate over the characters of the string
    for c in s:
        if stack and stack[-1] == '(' and c == ')':
            # If the current character is ')' and the top of the stack is '(',
            # pop the top of the stack
            stack.pop()
        else:
            # Otherwise, push the current character onto the stack
            stack.append(c)

    # The length of the maximum regular bracket sequence is the difference between
    # the length of the input string and the length of the stack
    print(len(s) - len(stack))

main()
