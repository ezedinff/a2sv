'''
Given a string s containing just the characters
'{', '}', '{', '}', '[' and ']' determine if the input string is valid
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ['(', '{', '[']
        closings = [')', '}', ']']
        for char in s:
            if char in openings:
                stack.append(char)
            elif char in closings:
                if not stack:
                    return False
                if openings.index(stack.pop()) != closings.index(char):
                    return False
        return not stack


    # technique is to use a stack to keep track of the opening brackets
    # using mappings to keep track of the opening and closing brackets
    # if the current character is an opening bracket, then we can push it onto the stack
    
    def isValid(self, s: str) -> bool:
        m = {"{": -1, "}": 1, "(": -2, ")": 2, "[": -3, "]": 3}
        stack = []
        for c in s:
            if m[c] < 0:
                stack.append(c)
            elif not stack or m[c] + m[stack.pop()] != 0:
                return False
        return not stack


if __name__ == "__main__":
    s = "()"
    solution = Solution()
    print(solution.isValid(s))