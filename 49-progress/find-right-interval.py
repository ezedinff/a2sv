from typing import List

'''
Example 1:

Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
'''

class Solution:
    # using binary search
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((interval[0], index) for index, interval in enumerate(intervals))
        res = []
        for _, end in intervals:
            left, right = 0, len(starts) - 1
            while left < right:
                mid = left + (right - left) // 2
                if starts[mid][0] < end:
                    left = mid + 1
                else:
                    right = mid
            r = starts[left][1] if starts[left][0] >= end else -1
            res.append(r)
        return res
