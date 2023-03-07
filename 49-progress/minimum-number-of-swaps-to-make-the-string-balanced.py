# 1963. Minimum Number of Swaps to Make the String Balanced
'''
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.


'''
class Solution:
    def minSwaps(self, s: str) -> int:
        open_brackets = 0
        min_swaps = 0
        for char in s:
            if char == '[':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_swaps += 1
                    open_brackets += 1
        return min_swaps
    
'''
The problem asks us to find the minimum number of swaps required to make a given string balanced.

The input string s is guaranteed to have an even length n and consists of exactly n / 2 opening
 brackets '[' and n / 2 closing brackets ']'.

The solution approach is to iterate through the string s character by character, keeping track of
the number of opening brackets encountered so far in a variable called open_brackets. If an opening
bracket '[' is encountered, we simply increment the open_brackets count. If a closing
bracket ']' is encountered, we check if there is an opening bracket available to match it by
checking if open_brackets > 0. If an opening bracket is available, we decrement open_brackets
to indicate that it has been used to match the current closing bracket. If an opening bracket is not
available, we must swap the current closing bracket with an opening bracket from a future position
in the string. This is because any opening bracket we have encountered so far has already been used
to match a previous closing bracket. Thus, we increment the min_swaps count and increment open_brackets
to indicate that we have "used" an opening bracket from a future position in the string.

After iterating through the entire string, the min_swaps count represents the minimum number of swaps
required to make the string balanced, and we return it.
'''