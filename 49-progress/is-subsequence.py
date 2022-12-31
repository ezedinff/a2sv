import unittest

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

class Test(unittest.TestCase):
    def test1(self):
        s = "abc"
        t = "ahbgdc"
        self.assertEqual(Solution().isSubsequence(s, t), True)
    def test2(self):
        s = "axc"
        t = "ahbgdc"
        self.assertEqual(Solution().isSubsequence(s, t), False)

if __name__ == '__main__':
    unittest.main()