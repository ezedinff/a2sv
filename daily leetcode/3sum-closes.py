# 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

# using two pointers
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res=math.inf
        nums.sort()
        ans=0
        for i in range(len(nums)):
            start=i+1
            end=len(nums)-1
            while start<end:
                currsum=nums[start]+nums[end]+nums[i]
                if currsum==target:
                    return target
                elif abs(currsum-target)<(res):
                    res=abs(currsum-target)
                    ans=currsum
                if currsum>target:
                    end-=1
                else:
                    start+=1
        return ans
'''
solution in rust
impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let mut nums = nums;
        nums.sort();
        let mut ans = nums[0] + nums[1] + nums[2];
        for i in 0..nums.len() {
            let mut start = i + 1;
            let mut end = nums.len() - 1;
            while start < end {
                let currsum = nums[start] + nums[end] + nums[i];
                if currsum == target {
                    return target;
                } else if (currsum - target).abs() < (ans - target).abs() {
                    ans = currsum;
                }
                if currsum > target {
                    end -= 1;
                } else {
                    start += 1;
                }
            }
        }
        ans
    }
}
'''

# using binary search
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                l, r = j + 1, len(nums) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] == target - s:
                        return target
                    if abs(s + nums[mid] - target) < abs(ans - target):
                        ans = s + nums[mid]
                    if s + nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
        return ans

# using binary search and two pointers