# Increase Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 1. Initialize two variables min1 and min2 to be the maximum value of integer.
        # 2. Iterate through the array, for each element n:
        #   2.1 If n <= min1, update min1 = n
        #   2.2 Else if n <= min2, update min2 = n
        #   2.3 Else if n > min2, return true
        # 3. Return false
        min1, min2 = float('inf'), float('inf')
        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True
        return False