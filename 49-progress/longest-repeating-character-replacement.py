# 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if k >= len(s) - 1:
            return len(s)
        max_len = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] != s[j]:
                    if k > 0:
                        k -= 1
                        continue
                    else:
                        break
                else:
                    continue
            max_len = max(max_len, j - i)
        return max_len

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AABABBA
        #   |    |
        left, right = 0, 0
        freq = {}
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            if right - left + 1 - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            right += 1
        return right - left
