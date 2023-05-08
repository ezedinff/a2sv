
'''
s => only digits
check if we can split s
    -> into 2 or more substrings
    -> (DESC order)
    -> difference b/n 2 adjacent substrings is 1

0090089
   -> ['0090', '089'] => 90 - 89 = 1, values are in DESC order
'''

class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(s, prev):
            if not s:
                return True
            for i in range(1, len(s) + 1):
                curr = int(s[:i])
                if curr == prev - 1:
                    if dfs(s[i:], curr):
                        return True
            return False
        
        for i in range(1, len(s)):
            if dfs(s[i:], int(s[:i])):
                return True
        return False
