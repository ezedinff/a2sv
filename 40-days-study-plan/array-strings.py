
# is unique, check if a string has all unique characters without using additional data structures

class Solution:
    def isUnique(self, s):
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    return False
        return True
    # this is O(n^2) time complexity and O(1) space complexity
    # technique: nested for loops
    # step 1: iterate through the string
    # step 2: iterate through the string again
    # step 3: check if the characters are the same
    # step 4: if they are, return false
    # step 5: if they are not, return true

# check permutation, check if one string is a permutation of another

class Solution:
    def checkPermutation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        s1 = sorted(s1)
        s2 = sorted(s2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True


# URLify, replace all spaces in a string with %20

class Solution:
    def URLify(self, s):
        s = s.strip()
        s = s.replace(" ", "%20")
        return s


# palindrome permutation, check if a string is a permutation of a palindrome

class Solution:
    def palindromePermutation(self, s):
        s = s.replace(" ", "")
        s = s.lower()
        s = sorted(s)
        count = 0
        for i in range(len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            if count > 1:
                return False
        return True
    # this is O(n log n) time complexity and O(1) space complexity
    # technique: sort the string, then iterate through the string and check if the characters are the same
    # step 1: remove spaces and lowercase the string
    # step 2: sort the string
    # step 3: iterate through the string
    # step 4: check if the characters are the same
    # step 5: if they are, increment the count
    # step 6: if they are not, reset the count
    # step 7: if the count is greater than 1, return false
    # step 8: if the count is not greater than 1, return true
    