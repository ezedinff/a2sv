# 179. Largest Number
'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.


Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        nums.sort(key = lambda x: x * 20, reverse = True)
        return str(int("".join(nums)))

# explaination:
# we sort the list by the string of each element multiplied by 20
# this is because the largest number can be formed by the largest digit
# in each position
# so we need to make sure that the largest digit is in the front
# Time: O(nlogn)
# why x * 20?
# because the largest number can have at most 20 digits