# two number sum
# https://www.algoexpert.io/questions/Two%20Number%20Sum
# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. If any two numbers in the input array sum
# up to the target sum, the function should return them in an array, in any
# order. If no two numbers sum up to the target sum, the function should return
# an empty array.
# Note that the target sum has to be obtained by summing two different integers
# in the array; you can't add a single integer to itself in order to obtain the
# target sum.
# You can assume that there will be at most one pair of numbers summing up to
# the target sum.
# Sample Input
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10
# Sample Output
# [-1, 11] // the numbers could be in reverse order
# Hints
# Hint 1
# Try using a hash table to store the numbers you've already seen. As you iterate
# through the input array, check if the target sum minus the current number
# exists in the hash table. If it does, return the pair of numbers. If it doesn't,
# add the current number to the hash table.
# Hint 2
# Can you use two pointers to solve this problem?
# Optimal Space & Time Complexity
# O(n) time | O(n) space - where n is the length of the input array
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []