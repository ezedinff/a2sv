class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def solve(n, k):
            if n == 1:
                return 0
            else:
                return (solve(n - 1, k) + k) % n
        return solve(n, k) + 1

    # using loop
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            ans = (ans + k) % i
        return ans + 1