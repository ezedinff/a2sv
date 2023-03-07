# Return the lexicographically largest merge you can construct.
# word1 and word2 are strings of lowercase English letters.
# Example 1:
# Input: word1 = "cabaa", word2 = "bcaaa"
# Output: "cbcabaaaaa"

# lexicographical means that the order of the characters 
# is determined by the order of the characters in the alphabet.
# example of lexicographical order:
# a < b < c < d < e < f < g < h < i < j < k < l < m < n < o < p < q < r < s < t < u < v < w < x < y < z


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        if word1[0] > word2[0]:
            return word1[0] + self.largestMerge(word1[1:], word2)
        elif word1[0] < word2[0]:
            return word2[0] + self.largestMerge(word1, word2[1:])
        else:
            if word1 > word2:
                return word1[0] + self.largestMerge(word1[1:], word2)
            else:
                return word2[0] + self.largestMerge(word1, word2[1:])
    
    # using two pointers
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0
        res = ""
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
        return res + word1[i:] + word2[j:]