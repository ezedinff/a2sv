from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
    # explanation
    # the idea is to use two pointers,
    # one to iterate through the array and
    # the other to keep track of the unique elements