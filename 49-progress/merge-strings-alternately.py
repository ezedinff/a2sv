# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        i = 0
        while i < len(word1) and i < len(word2):
            answer += word1[i]
            answer += word2[i]
            i += 1
        if i < len(word1):
            answer += word1[i:]
        if i < len(word2):
            answer += word2[i:]
        return answer