import unittest
from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        def is_same_frequency(d):
            return len(set([c for c in d.values() if c != 0])) == 1

        c = Counter(word)
        for char in word:
            c[char] -= 1
            if is_same_frequency(c):
                return True
            c[char] += 1
        return False

        

class Test(unittest.TestCase):
    def test1(self):
        word = "abcc"
        self.assertEqual(Solution().equalFrequency(word), True)

    def test2(self):
        word = "aazz"
        self.assertEqual(Solution().equalFrequency(word), False)

    def test3(self):
        word = "bac"
        self.assertEqual(Solution().equalFrequency(word), True)


if __name__ == '__main__':
    unittest.main()

