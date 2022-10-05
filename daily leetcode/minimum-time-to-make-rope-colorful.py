# Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
'''
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
'''
# We have a rope of length n, where n is an even integer. We split the rope into n / 2 even-length pieces, and we color each piece red or blue.
# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3

# Input: colors: "dbacd", neededTime = [10,5,2,2,2]
# Output: 0

class Solution:
    # using two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    # steps:
    # 1. use two pointers to find the longest subarray with at most two different colors
    # 2. return the minimum time needed to remove the rest of the balloons
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time, i,  j = 0, 0, 0
        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0

            # find all the same color balloons
            # balloon i, record the total removal time and the max removal time
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1
            

            total_time += curr_total - curr_max
            i = j
        return total_time
    
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        runMax = neededTime[0]
        runTotal = neededTime[0]
        res = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                runMax = max(runMax, neededTime[i])
                runTotal += neededTime[i]
            else:
                res += runTotal - runMax
                runMax = neededTime[i]
                runTotal = neededTime[i]
        return res + runTotal - runMax