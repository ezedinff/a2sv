# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
'''
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
'''

from collections import Counter
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_los = list(zip(*matches)) # [(winners), (losers)]
        lost_0 = set(win_los[0])
        count_lost = Counter(win_los[1]) # { 3: 2, 6: 2 }
        lost_1 = []

        for key, value in count_lost.items():
            if value > 0 and key in lost_0:
                lost_0.remove(key)
            
            if value == 1:
                lost_1.append(key)
        # nlogn 
        return [sorted(lost_0), sorted(lost_1)]


if __name__ == "__main__":
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    assert Solution().findWinners(matches) == [[1,2,10],[4,5,7,8]]
