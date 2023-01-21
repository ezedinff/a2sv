# https://leetcode.com/problems/find-common-characters/
'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
'''
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            words[i] = list(words[i])
        for i in range(len(words[0])):
            for j in range(1, len(words)):
                if words[0][i] in words[j]:
                    words[j].remove(words[0][i])
                else:
                    break
            else:
                ans.append(words[0][i])
        return ans
