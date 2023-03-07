from typing import List
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # [1,1,1,1,2,2,3,3]
        # { 1: 4, 3: 2, 2: 2 } -> most freq to less freq (sort), number + freq
        # [0, 0, 0, 0, 0, 0, 0, 0]
        # [1, 0, 1, 0, 1, 0, 1, 0] -> 1 
        # [1, 3, 1, 3, 1, 0, 1, 0] -> 3
        # [1, 3, 1, 3, 1, 2, 1, 2] -> 2
        n = len(barcodes)
        freq = Counter(barcodes)
        freq = sorted([(count, num) for num, count in freq.items()], reverse = True)

        result = [0] * n
        i = 0

        for count, num in freq:
            for _ in range(count):
                result[i] = num
                i += 2
                if i >= n:
                    i = 1

        return result