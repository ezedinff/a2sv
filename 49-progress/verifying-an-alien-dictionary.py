# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        for i, letter in enumerate(order):
            orderDict[letter] = i
        
        def CorrectOrder(word1, word2):
            small = min(len(word1), len(word2))
            
            for i in range(small):
                if orderDict[word1[i]] < orderDict[word2[i]]:
                    return True
                elif orderDict[word1[i]] > orderDict[word2[i]]:
                    return False
            return len(word1) <= len(word2)
        
        
        for i, word1 in enumerate(words[:-1]):
            word2 = words[i+1]
            if not CorrectOrder(word1, word2):
                return False
        return True