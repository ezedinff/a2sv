class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        longest = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(s[i:j])) == len(s[i:j]):
                    longest = max(longest, j - i)
        return longest


if __name__ == "__main__":
    s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(s)
    expected = 3
    assert result == expected, (result, expected)

    s = "bbbbb"
    result = Solution().lengthOfLongestSubstring(s)
    expected = 1
    assert result == expected, (result, expected)

    s = "pwwkew"
    result = Solution().lengthOfLongestSubstring(s)
    expected = 3
    assert result == expected, (result, expected)
