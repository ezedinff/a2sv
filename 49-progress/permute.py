from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(first = 0):
            if first >= len(nums):
                output.append(nums[:])

            for i in range(first, len(nums)):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

                
                
        backtrack()
        return output.sort(key=lambda x: x[0])
    
    # using bit manipulation
    '''
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        # using bit manipulation
        output = []
        def 

