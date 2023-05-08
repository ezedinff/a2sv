class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        win_sum = 0
        left, right = 0, 0
        while left < len(nums) and right < len(nums):
            win_sum += nums[right]
            if win_sum == target:
                min_len = min((right - left) + 1, min_len)
                win_sum -= nums[left]
                left += 1
                right += 1
            elif win_sum > target:
                win_sum -= nums[left]
                win_sum -= nums[right]
                left += 1
            else:
                right += 1
        
        return 0 if min_len == float('inf') else min_len
    
    # fix the above code and rewrite it
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        win_sum = 0
        left, right = 0, 0
        while right < len(nums):
            win_sum += nums[right]
            while win_sum >= target:
                min_len = min((right - left) + 1, min_len)
                win_sum -= nums[left]
                left += 1
            right += 1
        
        return 0 if min_len == float('inf') else min_len