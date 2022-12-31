# question link
# minimum amount of time to collect garbage
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/


'''
You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.
'''
# input garbage = ["G", "P", "GP", "GG"], travel = [2, 4, 3]
# output: 21

# input garbage = ["MMM","PGM","GP"], travel = [3, 10]
# output: 37



# question intution
# we need to count the number of different types of garbage at each house and travel time to reach the next house
# also, a garbage truck of some type will only stop at a house if it has garbage of that type else it will continue to the next house
# if a truck stops at a house, we can use a prefix sum of travel time to get time to reach current house from previous stop.
#   - use 3 variable to keep track of previous stop for each type of garbage
# so, time require by truck of a particular type to pick garbase from current house is:
#  - time to reach current house from previous stop + time to pick garbage from current house
#  - and number of garbage of that type at current house
# sum up the travel time of each type of trucks and return total time required to pick up all garbage

from typing import List
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        p, g, m = 0, 0, 0
        p_idx, g_idx, m_idx = -1, -1, -1
        for i in range(len(garbage)):
            if 'P' in garbage[i]:
                p_idx = i
                p += garbage[i].count('P')
            if 'G' in garbage[i]:
                g_idx = i
                g += garbage[i].count('G')
            if 'M' in garbage[i]:
                m_idx = i
                m += garbage[i].count('M')

        # calculate cumulative time
        time = [0]
        for i in range(len(travel)):
            time.append(time[-1] + travel[i])
        
        res = 0
        if p_idx != -1:
            res += time[p_idx]

        if g_idx != -1:
            res += time[g_idx]
        
        if m_idx != -1:
            res += time[m_idx]
        
        res += p + g + m
        return res



i = ["G", "P", "GP", "GG"]
t = [2, 4, 3]
s = Solution()
print(s.garbageCollection(i, t))
  
i = ["MMM","PGM","GP"]
t = [3, 10]
s = Solution()
print(s.garbageCollection(i, t))
