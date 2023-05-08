# 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(piles, h, k):
            return sum((pile - 1) // k + 1 for pile in piles) <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not canEatAllBananas(piles, h, mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
    
    '''
    canEatAllBananas works in the following way:
    1. We have a list of piles of bananas, and a number of hours we have to eat
      them all.
    2. We have a speed k, which is the number of bananas we can eat per hour.
    3. We want to know if we can eat all the bananas in h hours or less.
    4. We can eat all the bananas in h hours or less if the sum of the
      number of hours it takes to eat each pile is less than or equal to h.

      why (pile - 1) // k + 1?
        - If we have 10 bananas and a speed of 4, we can eat 2 bananas in 1 hour.
        - If we have 10 bananas and a speed of 3, we can eat 3 bananas in 1 hour.
        - If we have 10 bananas and a speed of 2, we can eat 5 bananas in 1 hour.
        - If we have 10 bananas and a speed of 1, we can eat 10 bananas in 1 hour.
    '''