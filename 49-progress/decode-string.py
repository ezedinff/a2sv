class Solution:
    def decodeString(self, s: str) -> str:
        # using recursion
        def decode(s, i):
            res, mul = '', 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    mul = mul * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = decode(s, i + 1)
                    res += mul * tmp
                    mul = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return decode(s, 0)