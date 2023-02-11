from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    counts[i] += 1

        return counts

    # explanation
    # the approach is to iterate through the array and for each element
    # iterate through the array again and count how many elements are
    # smaller than the current element
    # the time complexity is O(n^2) and the space complexity is O(n)
    