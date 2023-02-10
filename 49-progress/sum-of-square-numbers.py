class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            if left ** 2 + right ** 2 == c:
                return True
            if left ** 2 + right ** 2 < c:
                left += 1
            else:
                right -= 1
        return False