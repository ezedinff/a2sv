# Numbers With Same Consecutive Differences
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# algorithms
# Medium (41.5%)

from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        
        res = []
        def dfs(n, num):
            if n == 0:
                res.append(num)
                return
            
            last_digit = num % 10
            if last_digit + k < 10:
                dfs(n - 1, num * 10 + last_digit + k)
            if last_digit - k >= 0:
                dfs(n - 1, num * 10 + last_digit - k)
        
        for i in range(1, 10):
            dfs(n - 1, i)
        
        return res