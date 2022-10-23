# subarray range with given sum
# given an unsorted array of integers and a sum, the task is to count the number of subarrays which adds to a given number

# input: arr[] = {10, 2, -2, -20, 10}, sum = -10
# output: 3
# Explanation:
# Subarrays: arr[0...3], arr[1...4], arr[3..4] have sum exactly equal to -10.

class Solution:
    def subArraySum(self,arr, n, sum):
        d = {}
        d[0], total, count = 1, 0, 0
        for i in range(n):
            total += arr[i]
            if total - sum in d:
                count += d[total - sum]
            if total in d:
                d[total] += 1
            else:
                d[total] = 1
        return count