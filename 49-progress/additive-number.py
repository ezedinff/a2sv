class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(s, i, a, b, n):
            if i == len(s):
                return n > 2
            num = 0
            for x in range(i, len(s)):
                num = num * 10 + int(s[x])
                if n < 2:
                    if backtrack(s, x + 1, b, num, n + 1):
                        return True
                elif a + b == num:
                    if backtrack(s, x + 1, b, num, n + 1):
                        return True
                if num == 0:
                    break
            return False
        return backtrack(num, 0, 0, 0, 0)