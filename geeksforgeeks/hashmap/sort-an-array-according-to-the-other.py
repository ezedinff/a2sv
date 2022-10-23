# Sort an array according to the other
# Given two arrays A1[] and A2[], 
# sort A1 in such a way that the relative order among the elements will be same as those are in A2.
# For the elements not present in A2, append them at last in sorted order.

# Example:
# Input:
# A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
# A2[] = {2, 1, 8, 3}
# Output:
# 2 2 1 1 8 8 3 5 6 7 9

class Solution:
    def relativeSort(self, A1, N, A2, M):
        # code here
        # create a hashmap
        hashmap = {}
        for i in A1:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        # create a new array
        new_array = []
        for i in A2:
            if i in hashmap:
                new_array.extend([i] * hashmap[i])
                del hashmap[i]
        # add the remaining elements
        for i in sorted(hashmap):
            new_array.extend([i] * hashmap[i])
        return new_array