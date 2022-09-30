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


if __name__ == "__main__":
    s = "()"
    solution = Solution()
    print(solution.isValid(s))