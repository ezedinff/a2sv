from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        while start < end:
            mid = (start + end) // 2
            if self.canShip(weights, days, mid):
                end = mid
            else:
                start = mid + 1
        return start

    def canShip(self, weights: List[int], days: int, capacity: int) -> bool:
        d = 1
        total = 0
        for w in weights:
            total += w
            if total > capacity:
                d += 1
                total = w
        return d <= days