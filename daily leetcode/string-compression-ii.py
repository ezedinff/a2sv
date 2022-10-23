# String Compression II
# https://leetcode.com/problems/string-compression-ii/
# Hard
#
# Example 1:
# Input: s = "aaabcccd", k = 2
# Output: 4
# Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6.
# Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5,
# for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d.
# Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
#


class Solution:
    # technique: dynamic programming 

    from functools import lru_cache
    from math import inf
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def counts(k, i, j, c):

            if k < 0:
                return inf

            if i >= n:
                return 0

            if 0 <= j < n and s[i] == s[j]:

                return int(c == 1 or c == 9 or c == 99) + counts(k, i + 1, i, c + 1)

            return min(1 + counts(k, i + 1, i, 1), counts(k - 1, i + 1, j, c))

        return counts(k, 0, -1, 0)
    
    # time complexity: O(n^2)
    # space complexity: O(n^2)

    
