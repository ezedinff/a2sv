class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # using bit manipulation
      
        bits = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            a_bit = int(a[i]) if i >= 0 else 0
            b_bit = int(b[j]) if j >= 0 else 0
            sum = a_bit + b_bit + carry
            bits.append(sum % 2)
            carry = sum // 2
            i -= 1
            j -= 1
        if carry > 0:
            bits.append(carry)
        return ''.join(str(bit) for bit in bits[::-1])
