from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        frequencies = Counter(nums)
        ans = []
        for _, key in enumerate(frequencies):
            if frequencies.get(key) > target:
                ans.append(key)
        return ans

