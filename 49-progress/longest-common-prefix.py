from os import path
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return path.commonprefix(strs)