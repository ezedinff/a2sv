from typing import List 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k % len(nums)):
            nums.insert(0, nums.pop())
        return nums
    
    # explanation
    # the idea is to use the built-in insert and pop methods
    # to rotate the array k times
    # the modulo operator is used to handle the case where k > len(nums)
    # the time complexity is O(k * n) and the space complexity is O(1)