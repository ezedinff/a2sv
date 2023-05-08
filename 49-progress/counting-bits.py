class Solution:
    def countBits(self, n: int) -> List[int]:
        # using bit manipulation
        # O(n) time and O(1) space
        # the number of bits in a number is the same as the number of bits in the number without the last bit
        # plus 1 if the last bit is 1
        # e.g. 5 = 101, 5 >> 1 = 10 = 2, 5 & 1 = 1, 2 + 1 = 3
        # e.g. 4 = 100, 4 >> 1 = 10 = 2, 4 & 1 = 0, 2 + 0 = 2

        # initialize the array with 0s
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)

        return bits

    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)

        for i in range(1, n + 1):
            # if the number is even, the number of bits is the same as the number of bits in the number without the last bit
            # if the number is odd, the number of bits is the same as the number of bits in the number without the last bit
            # plus 1
            num = i
            while num > 0:
                if num % 2 != 0: # if the number is odd
                    bits[i] += 1
                num >>= 1

        return bits



# Set the Kth bit from the right, 1 indexed
def kthBitSet(num : int, k : int) -> int:
    return num | (1 << (k - 1))


import sys
# turn off the kth bit from the right, 1 indexed
def turnOffKthBit(num : int, k : int) -> int:
    return num & ~(1 << (k - 1))