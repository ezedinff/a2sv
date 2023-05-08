class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def fastPow(x, n):
            res = 1
            while n:
                if n & 1:
                    res = res * x % 1000000007
                x = x * x % 1000000007
                n >>= 1
            return res
        return fastPow(5, (n + 1) // 2) * fastPow(4, n // 2) % 1000000007