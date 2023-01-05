class Solution:
    def isPalindrome(self, s: int) -> bool:
        if s < 0 or (s % 10 == 0 and s != 0):
            return False
        if s < 10:
            return True
        rev = 0
        while s > rev:
            rev = rev * 10 + s % 10
            s = s // 10
        return s == rev or s == rev // 10