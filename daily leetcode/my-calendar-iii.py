# My Calandar III
# https://leetcode.com/problems/my-calendar-iii/

# using sweep line algorithm
from sortedcontainers import SortedDict
class MyCalendarThree:
    
    def __init__(self):
        self.calendar = SortedDict()
        
    def book(self, start: int, end: int) -> int:
        self.calendar[start] = self.calendar.get(start, 0) + 1
        self.calendar[end] = self.calendar.get(end, 0) - 1
        active = ans = 0
        for x in self.calendar.values():
            active += x
            ans = max(ans, active)
        return ans


# using segment tree
class MyCalendarThree:
        
        def __init__(self):
            self.vals = Counter()
            self.lazy = Counter()
            
        def update(self, start: int, end: int, left: int = 0, right: int = 10**9, idx: int = 1) -> None:
            if start > right or end < left:
                return
            
            if start <= left <= right <= end:
                self.vals[idx] += 1
                self.lazy[idx] += 1
            else:
                mid = (left + right) // 2
                self.update(start, end, left, mid, idx * 2)
                self.update(start, end, mid + 1, right, idx * 2 + 1)
                self.vals[idx] = max(self.vals[idx * 2], self.vals[idx * 2 + 1]) + self.lazy[idx]
        
        def book(self, start: int, end: int) -> int:
            self.update(start, end - 1)
            return self.vals[1]