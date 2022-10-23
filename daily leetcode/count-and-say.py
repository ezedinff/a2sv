# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.countAndSayHelper(self.countAndSay(n-1))
    
    def countAndSayHelper(self, s: str) -> str:
        res = ""
        count = 1
        for i in range(len(s)):
            if i == len(s) - 1:
                res += str(count) + s[i]
            elif s[i] == s[i+1]:
                count += 1
            else:
                res += str(count) + s[i]
                count = 1
        return res
        