'''
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
        return final
