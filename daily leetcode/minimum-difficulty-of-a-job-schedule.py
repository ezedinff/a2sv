# Minimum Difficulty of a Job Schedule

# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

# Hard

# Example 1:

# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7


class Solution:
    # technique: dynamic programming 

    from functools import lru_cache
    from math import inf
    # top-down approach with memoization
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        @lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        
        return dfs(0, d) if n >= d else -1
            

    
    # time complexity: O(n^2)
    # space complexity: O(n^2)

    # step 1: check if the number of days is greater than the number of jobs
    # step 2: initialize a current pointer
    # step 3: initialize a length variable
    # step 4: iterate through the string
    # step 5: check if the next character is the same as the current character
    # step 6: if it is, increment the length variable
    # step 7: if it is not, increment the length variable
    # step 8: return the length variable

   # another solution
   # time complexity O(n)
   # 

   def 