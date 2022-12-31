# question link
# https://leetcode.com/problems/3sum

# question intution
# - sort the array
# - iterate through the array
# - for each element, find the pair that sums to -element
# - if the pair is found, add it to the result
# - if the pair is not found, continue

# question solution
# - sort the array
# - iterate through the array
# - for each element, find the pair that sums to -element
# - if the pair is found, add it to the result
# - if the pair is not found, continue

# question complexity
# - time: O(n^2)
# - space: O(n)

# question code
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 s = nums[i] + nums[l] + nums[r]
#                 if s == 0:
#                     res.append([nums[i], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while l < r and nums[l] == nums[l - 1]:
#                         l += 1
#                     while l < r and nums[r] == nums[r + 1]:
#                         r -= 1
#                 elif s < 0:
#                     l += 1
#                 else:
#                     r -= 1
#         return res

# better solution using two pointers and a set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res