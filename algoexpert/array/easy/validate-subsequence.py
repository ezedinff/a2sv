# Validate Subsequence
# https://www.algoexpert.io/questions/Validate%20Subsequence
# Given two non-empty arrays of integers, write a function that determines whether
# the second array is a subsequence of the first one.
# A subsequence of an array is a set of numbers that aren't necessarily adjacent
# in the array but that are in the same order as they appear in the array. For
# instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and
# so do the numbers [2, 4]. Note that a single number in an array and the array
# itself are both valid subsequences of the array.
# You can assume that there will only be one subsequence match for the given
# test cases.
# Sample Input
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# Sample Output
# true
# Hints
# Hint 1
# Try using two pointers to solve this problem. One pointer will iterate through
# the first array, and the other pointer will iterate through the second array.
# Hint 2
# As you iterate through the first array, check if the current number matches the
# number at the current index of the second array. If it does, increment the
# second array's pointer. If it doesn't, don't increment the second array's
# pointer. If the second array's pointer reaches the end of the second array,
# return true.
# Optimal Space & Time Complexity
# O(n) time | O(1) space - where n is the length of the first array
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)