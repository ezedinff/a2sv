# Print Non-Repeated Elements in the Same Order as They Appear in the Input Array

class Solution:
    def printNonRepeated(self, arr, n):
        # code here
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in arr:
            if d[i] == 1:
                print(i, end=" ")
    
    # using counter
    def printNonRepeated2(self, arr, n):
        # code here
        from collections import Counter
        d = Counter(arr)
        for i in arr:
            if d[i] == 1:
                print(i, end=" ")