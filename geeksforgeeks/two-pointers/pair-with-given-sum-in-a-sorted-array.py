# Pair with given sum in a sorted array

# Example
# input: arr[] = {1, 2, 3, 4, 5, 6, 7}
# k = 8
# output: 3


class Solution:
    def counPair(self, arr, n, k):
        i, j, count = 0, n - 1, 0
        while i < j:
            if arr[i] + arr[j] == k:
                count += 1
                i+=1
                j-=1
            elif arr[i] + arr[j] < k:
                i += 1
            else:
                j -= 1
        
        return count if count else -1
