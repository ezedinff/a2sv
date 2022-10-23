# Equilibrium Point
# Given an array of n positive number. The task is to find the first equilibium point in the array
# Equilibrium point in an array is a position such that the sum of elements before it is equal to the sum
# of elements after it

# input n = 5, A[] = {1, 3, 5, 2, 2}
# output 3
# Explanation:
# 3 is an equilibrium point in this array because:
# A[0] + A[1] = A[3] + A[4]

class Solution:
    def equilibriumPoint(self, A, n):
        # code here
        if n == 1:
            return 1
        left = 0
        right = sum(A)
        for i in range(n):
            right -= A[i]
            if left == right:
                return i + 1
            left += A[i]
        return -1