# https://leetcode.com/problems/minimum-window-substring

# # Minimum Window Substring
'''
Input: s = "a", t = "aa"
Output: ""
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # using dictionary
        # time complexity: O(n)
        # space complexity: O(n)
        # create dictionary
        d = {}
        for char in t:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        # create result
        result = ''
        # create left and right pointers
        left = 0
        right = 0
        # create count
        count = len(t)
        # create min length
        min_length = len(s) + 1
        # create min left
        min_left = 0
        # create min right
        min_right = 0
        # loop through s
        while right < len(s):
            # if char is in d
            if s[right] in d:
                # decrement d[char]
                d[s[right]] -= 1
                # if d[char] >= 0
                if d[s[right]] >= 0:
                    # decrement count
                    count -= 1
            # increment right
            right += 1
            # while count == 0
            while count == 0:
                # if right - left < min_length
                if right - left < min_length:
                    # update min length
                    min_length = right - left
                    # update min left
                    min_left = left
                    # update min right
                    min_right = right
                # if char is in d
                if s[left] in d:
                    # increment d[char]
                    d[s[left]] += 1
                    # if d[char] > 0
                    if d[s[left]] > 0:
                        # increment count
                        count += 1
                # increment left
                left += 1
        # return result
        return s[min_left:min_right]