#  Maximum Length of a Concatenated String with Unique Characters
#  https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
Input: ["aa","bb"]
Expected: 0
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def check(s):
            return len(s) == len(set(s))
        def dfs(i, s):
            if not check(s):
                return
            self.ans = max(self.ans, len(s))
            for j in range(i, len(arr)):
                dfs(j + 1, s + arr[j])
        self.ans = 0
        dfs(0, '')
        return self.ans