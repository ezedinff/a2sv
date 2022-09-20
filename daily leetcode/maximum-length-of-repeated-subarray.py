# Maximum length of repeated subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

# algorithm: dynamic programming
# topics: array

from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        max_len = 0
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len