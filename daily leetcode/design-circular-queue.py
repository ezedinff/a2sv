# Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    def __init__(self, k: int):
            self.q = [None] * k
            self.k = k
            self.l = 0
            self.r = 0
    
    def enQueue(self, value: int) -> bool:
        if self.q[self.r] is None:
            self.q[self.r] = value
            self.r = (self.r + 1) % self.k
            return True
        return False
    
    def deQueue(self) -> bool:
        if self.q[self.l] is not None:
            self.q[self.l] = None
            self.l = (self.l + 1) % self.k
            return True
        return False
    
    def Front(self) -> int:
        return self.q[self.l] if self.q[self.l] is not None else -1
    
    def Rear(self) -> int:
        return self.q[self.r - 1] if self.q[self.r - 1] is not None else -1
    
    def isEmpty(self) -> bool:
        return self.q[self.l] is None
    
    def isFull(self) -> bool:
        return self.q[self.r] is not None