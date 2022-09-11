# Maximum Performance of a Team

# You are given two integers n and k and two integer arrays speed and efficiency both of length n.
#  There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and
#  efficiency of the ith engineer respectively.

# Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

# The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency
#  among their engineers.

# Return the maximum performance of this team. Since the answer can be a huge number, return it
#  modulo 109 + 7.

# Example 1:
# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2

# Output: 60

from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        # sort the engineers by their efficiency
        engineers = sorted(zip(efficiency, speed), reverse=True)
        # print(engineers)

        # use a min heap to keep track of the speed of the k fastest engineers
        # we can use a min heap because we want to remove the slowest engineer
        # if we have more than k engineers in the team
        from heapq import heappush, heappop
        team = []
        team_speed = 0
        max_performance = 0
        for e, s in engineers:
            # add the current engineer to the team
            heappush(team, s)
            team_speed += s
            # if the team has more than k engineers, remove the slowest engineer
            if len(team) > k:
                team_speed -= heappop(team)
            # update the max_performance with the current team performance
            max_performance = max(max_performance, team_speed * e)

        return max_performance % (10 ** 9 + 7)
