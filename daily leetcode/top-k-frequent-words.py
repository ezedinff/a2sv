# Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # using heap
        freq = []

        # count frequency
        for word in set(words):
            heapq.heappush(freq, (-words.count(word), word))

        # get top k
        return [heapq.heappop(freq)[1] for _ in range(k)]
    