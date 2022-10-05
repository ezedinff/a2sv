# Bitwise XOR of All Pairings

'''
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.


Example 1:

Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.


Input:
[1,2]
[3,4]
Output: 0


Constraints:

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[j] <= 109
'''
from typing import List
class Solution:
    # save memory
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a = 0
        if len(nums2) % 2:
            for i in nums1:
                a ^= i
        if len(nums1) % 2:
            for i in nums2:
                a ^= i
        return a


        

        

    


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.xorAllNums([2,1,3], [10,2,5,0]) == 13
    

