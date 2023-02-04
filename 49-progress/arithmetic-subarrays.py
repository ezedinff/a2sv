from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for left, right in zip(l, r):
            max_num, min_num, lookup = max(nums[left:right + 1]), min(nums[left:right + 1]), set(nums[left:right + 1])
            if max_num == min_num:
                result.append(True)

            dividend, remainder = divmod(max_num - min_num, len(nums[left:right + 1]) - 1)
            if remainder:
                result.append(False)
            else:
                if dividend:
                    result.append(all(i in lookup for i in range(min_num, max_num, dividend)))
        return result