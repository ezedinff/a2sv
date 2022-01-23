# decode string
# Given an encoded string, return it's decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# you may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits  and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

import unittest


def decodeString(s) -> str:
    stack = []
    for c in s:
        if c != ']':
            stack.append(c)
        else:
            temp = []
            while stack[-1] != '[':
                char = stack.pop()
                temp.append(char)
            stack.pop()
            recurrence = []
            while len(stack) > 0 and stack[-1].isdigit():
                recurrence.append(int(stack.pop()))
            
            value = 0
            for i in range(len(recurrence)-1,-1,-1):
                value*=10
                value+=recurrence[i]
            temp.reverse()
            stack.append(''.join(temp)*value)
            
    return ''.join(stack)



class TestSolution(unittest.TestCase):
    def test_case(self):
        self.assertEqual(decodeString("3[a]2[bc]"), "aaabcbc")


if __name__ == '__main__':
    unittest.main()
    