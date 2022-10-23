# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # using dictionary
        # time complexity: O(n)
        # space complexity: O(n)
        # create dictionary
        d = {}
        # create result
        result = []
        # loop through nums
        for num in nums:
            # if num in d
            if num in d:
                # append num to result
                result.append(num)
            # else
            else:
                # add num to d
                d[num] = 1
        # loop through range(1, len(nums) + 1)
        for i in range(1, len(nums) + 1):
            # if i not in d
            if i not in d:
                # append i to result
                result.append(i)
        # return result
        return result