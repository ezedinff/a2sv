class Solution:
    def getSum(self, a: int, b: int) -> int:
        # using bit manipulation
        # O(1) time and O(1) space
        # XOR the two numbers to get the sum without the carry
        # AND the two numbers to get the carry
        # shift the carry to the left by 1
        # repeat until there is no carry
        # e.g. 2 + 3
        # 2 = 10, 3 = 11
        # 10 ^ 11 = 01, (10 & 11) => 10 << 1 = 100
        # 01 ^ 100 = 101, (01 & 100) => 0 << 1 = 0
        # 101 ^ 0 = 101

        ans = a ^ b
        carry = (a & b) << 1
        mask = (1 << 32) - 1
        while carry & mask != 0:
            ans, carry = ans ^ carry, (ans & carry) << 1
        return ans & mask if carry > 0 else ans

