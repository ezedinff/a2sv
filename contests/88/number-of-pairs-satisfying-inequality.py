# Number of Pairs Satisfying Inequality
# https://leetcode.com/contest/biweekly-contest-88/problems/number-of-pairs-satisfying-inequality/

from sortedcontainers import SortedList
class Solution:
    # using binary search
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        l = SortedList()
        ans = 0
        for i in range(len(nums1)):
            curr = nums1[i] - nums2[i]
            ans += l.bisect_left(curr + diff + 1)
            l.add(curr)
        return ans