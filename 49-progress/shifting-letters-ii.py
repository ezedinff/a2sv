# 2381. Shifting Letters II

'''
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
 
'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        for start, end, direction in shifts:
            if direction == 0:
                for i in range(start, end):
                    s[i] = chr(ord(s[i]) - 1 if ord(s[i]) > 97 else 122)
            else:
                for i in range(start, end):
                    s[i] = chr(ord(s[i]) + 1 if ord(s[i]) < 122 else 97)
        return ''.join(s)
    
    # optimized solution using prefix sum
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0] * len(s)
        for start, end, direction in shifts:
            if direction == 0:
                cum_shifts[start] -= 1
                cum_shifts[end] += 1
            else:
                cum_shifts[start] += 1
                cum_shifts[end] -= 1
        
        cum_sum = 0
        for i in range(len(s)):
            cum_sum += cum_shifts[i]
            
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
            
            
