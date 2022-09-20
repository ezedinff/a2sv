# Find original array from doubled array
# https://leetcode.com/contest/weekly-contest-252/problems/find-original-array-from-doubled-array/

from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        counter = Counter(changed)
        original = []
        for num in changed:
            if counter[num] == 0:
                continue
            if counter[num * 2] == 0:
                return []
            counter[num] -= 1
            counter[num * 2] -= 1
            original.append(num)
        return original


if __name__ == "__main__":
    changed = [1,3,4,2,6,8]
    print(Solution().findOriginalArray(changed))