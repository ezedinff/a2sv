import unittest

class Solution:
    def appendCharacters(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1; j += 1
                continue
            i += 1
        return len(t) - j

class Test(unittest.TestCase):
    def test1(self):
        s = "coaching"; t = "coding"
        self.assertEqual(Solution().appendCharacters(s, t), 4)

    def test2(self):
        s = "abcde"; t = "a"
        self.assertEqual(Solution().appendCharacters(s, t), 0)


if __name__ == '__main__':
    unittest.main()