from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j, score, max_score = 0, len(tokens) - 1, 0, 0
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return max_score

if __name__ == "__main__":
    tokens = [100,200]
    power = 150
    assert Solution().bagOfTokensScore(tokens, power) == 1
