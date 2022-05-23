class Solution:
    cache = {}

    def fib(self, n: int) -> int:
        if n in Solution.cache:
            return Solution.cache[n]
        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1
        f = self.fib(n - 1) + self.fib(n - 2)
        Solution.cache[n] = f
        return f
