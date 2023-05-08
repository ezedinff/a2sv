'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using bit manipulation
        # XOR all the numbers in the array with the numbers from 0 to n
        # the result will be the missing number
        # O(n) time and O(1) space
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num # XOR the index and the number, 
            # XOR the index required because the array is missing a number
        
        return missing

        # why XOR for this problem?
        # XOR is commutative and associative
        # XOR of a number with itself is 0
        # XOR of a number with 0 is the number itself
        # XOR of a number with another number is the same as XORing the two numbers together
        # XOR of a number with a number that is not in the array will result in the number itself