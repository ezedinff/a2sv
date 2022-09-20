# Palindrome Pairs
'''
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

https://leetcode.com/problems/palindrome-pairs/
'''

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        words_map = {word: i for i, word in enumerate(words)}
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                if self.isPalindrome(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix in words_map and words_map[rev_suffix] != i:
                        ans.append([words_map[rev_suffix], i])
                if j != len(word) and self.isPalindrome(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in words_map and words_map[rev_prefix] != i:
                        ans.append([i, words_map[rev_prefix]])
        return ans
    
    def isPalindrome(self, word):
        return word == word[::-1]


if __name__ == "__main__":
    words = ["abcd","dcba","lls","s","sssll"]
    print(Solution().palindromePairs(words))