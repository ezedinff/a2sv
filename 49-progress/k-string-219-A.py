import unittest
from collections import Counter


def kString(k, s):
    d = Counter(s)
    result = "".join([c * (d[c] // k) for c in d])
    if len(result) * k != len(s):
        return -1
    return result * k


class Test(unittest.TestCase):
    def test1(self):
        k = 2
        s = "aazz"
        self.assertEqual(kString(k, s), "azaz")

    def test2(self):
        k = 3
        s = "abcabcabz"
        self.assertEqual(kString(k, s), -1)


if __name__ == '__main__':
    unittest.main()