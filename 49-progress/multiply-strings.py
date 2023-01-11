class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = self.strToInt(num1)
        n2 = self.strToInt(num2)
        return str(n1 * n2)
    
    def strToInt(self, num: str) -> int:
        ZERO = 48
        ret = 0
        for n in num:
            ret *= 10
            ret += ord(n) - ZERO
        return ret