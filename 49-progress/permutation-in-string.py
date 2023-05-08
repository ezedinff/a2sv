from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s2_freq = Counter(s2[:len(s1)])
        if s1_freq == s2_freq:
            return True
        for i in range(len(s1), len(s2)):
            s2_freq[s2[i]] += 1
            s2_freq[s2[i - len(s1)]] -= 1
            if s2_freq[s2[i - len(s1)]] == 0:
                del s2_freq[s2[i - len(s1)]]
            if s1_freq == s2_freq:
                return True
        return False