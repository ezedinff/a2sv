# Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

'''
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 1. Brute force
        # Time: O(n^2)
        # Space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (sum(nums[i:j+1]) % k == 0):
        #             return True
        # return False

        # 2. Prefix sum
        # Time: O(n^2)
        # Space: O(n)
        # prefix_sum = [0]
        # for num in nums:
        #     prefix_sum.append(prefix_sum[-1] + num)
        # for i in range(len(prefix_sum)):
        #     for j in range(i+2, len(prefix_sum)):
        #         if (prefix_sum[j] - prefix_sum[i]) % k == 0:
        #             return True
        # return False

        # 3. Prefix sum + Hashmap
        # Time: O(n)
        # Space: O(n)
        prefix_sum = 0
        seen = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
            if prefix_sum in seen:
                if i - seen[prefix_sum] > 1:
                    return True
            else:
                seen[prefix_sum] = i
        return False