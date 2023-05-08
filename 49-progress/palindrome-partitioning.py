'''
131. Palindrome Partitioning

Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
'''
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start = 0, path = []):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    backtrack(i + 1, path + [s[start:i+1]])
        
        backtrack()
        return res