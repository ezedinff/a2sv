'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # create a 2d array
        # fill the first row with 0, 1, 2, 3, 4, 5
        # fill the first column with 0, 1, 2, 3, 4, 5
        # traverse the array
        
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        # fill the first row
        for i in range(len(word2) + 1):
            dp[0][i] = i

        # fill the first column
        for i in range(len(word1) + 1):
            dp[i][0] = i

        for i in range(1, len(word1) + 1):
            # traverse the array
            for j in range(1, len(word2) + 1):
                # if the characters are the same, copy the value from the diagonal
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # otherwise, take the min of the three values
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]