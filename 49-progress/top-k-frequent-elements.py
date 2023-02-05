from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            frequencies = Counter(nums)
            return [items[0] for items in frequencies.most_common()[:k]]