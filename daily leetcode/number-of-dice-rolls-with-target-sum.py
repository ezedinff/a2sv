# Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


# Example 1:
# Input: d = 1, f = 6, target = 3
# Output: 1

# Example 2:
# Input: d = 2, f = 6, target = 7
# Output: 6


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]
        return dp[-1][-1] % (10 ** 9 + 7)