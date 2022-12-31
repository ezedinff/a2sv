import unittest
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {c: i for i, c in enumerate(s)}
        partitions = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_idx[c])
            if i == end:
                partitions.append(end - start + 1)
                start, end = i + 1, i + 1
        return partitions


class Test(unittest.TestCase):
    def test1(self):
        s = "ababcbacadefegdehijhklij"
        self.assertEqual(Solution().partitionLabels(s), [9, 7, 8])

    def test2(self):
        s = "eccbbbbdec"
        self.assertEqual(Solution().partitionLabels(s), [10])


if __name__ == '__main__':
    unittest.main()