# Convert array into Zig-Zag fashion
# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/

# Given an array of DISTINCT elements, rearrange the elements of array in zig-zag fashion in O(n) time.

# The converted array should be in form a < b > c < d > e < f.

# Example:
# input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
# output: arr[] = {3, 7, 4, 8, 2, 6, 1}

class Solution:
    def zigZag(self, arr, n):
        # code here
        for i in range(1, n):
            if i % 2 == 1:
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
            else:
                if arr[i] > arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
        return arr