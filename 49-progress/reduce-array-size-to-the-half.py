from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequencies = Counter(arr)
        pairs = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        total = 0
        ans = 0
        for pair in pairs:
            total += pair[1]
            ans += 1
            if total >= len(arr) // 2:
                break

        return ans