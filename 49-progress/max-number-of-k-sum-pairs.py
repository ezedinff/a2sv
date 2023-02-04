from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        d = {}

        for num in nums:
            if num in d and d[num] > 0:
                operations += 1
                d[num] -= 1

            elif num < k:
                if k - num not in d:
                    d[k - num] = 1
                else:
                    d[k - num] += 1

        return operations