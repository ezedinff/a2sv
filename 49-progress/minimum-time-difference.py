'''
539. Minimum Time Difference
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between
any two time-points in the list.
 

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
'''


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = 24 * 60
        for i in range(len(timePoints) - 1):
            ans = min(ans, self.timeDiff(timePoints[i], timePoints[i + 1]))
        ans = min(ans, self.timeDiff(timePoints[-1], timePoints[0]) + 24 * 60)
        return ans

    def timeDiff(self, time1, time2):
        h1, m1 = time1.split(":")
        h2, m2 = time2.split(":")
        return (int(h2) - int(h1)) * 60 + (int(m2) - int(m1))

# explaination:
# we sort the list of time points
# then we compare the difference between each time point and the next time point
# we also compare the difference between the last time point and the first time point
# Time: O(nlogn)
# why we sort the list of time points?
# because we need to compare the difference between each time point and the next time point

# why 24 * 60?
# because the largest difference between two time points is 24 hours

# why (int(h2) - int(h1)) * 60 + (int(m2) - int(m1))?
# because we need to convert the time to minutes

# better solution:
# using counting sort

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = [0] * 24 * 60
        for timePoint in timePoints:
            h, m = timePoint.split(":")
            if time[int(h) * 60 + int(m)] == 1:
                return 0
            time[int(h) * 60 + int(m)] = 1
        prev = 0
        first = 24 * 60
        last = 0
        ans = 24 * 60
        for i in range(24 * 60):
            if time[i] == 1:
                if first != 24 * 60:
                    ans = min(ans, i - prev)
                first = min(first, i)
                last = max(last, i)
                prev = i
        ans = min(ans, first + 24 * 60 - last)
        return ans