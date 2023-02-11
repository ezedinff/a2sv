# https://leetcode.com/problems/string-compression/
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        i = 0
        j = 0
        while i < n and j < n:
            count = 1
            while j < n - 1 and chars[j] == chars[j + 1]:
                count += 1
                j += 1
            chars[i] = chars[j]
            i += 1
            if count > 1:
                for c in str(count):
                    chars[i] = c
                    i += 1
            j += 1
        return i


