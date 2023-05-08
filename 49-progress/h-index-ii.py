from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        left, right = 0, N - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= N - mid:
                right = mid - 1
            else:
                left = mid + 1
        return N - left
    
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        for i in range(N):
            if citations[i] >= N - i:
                return N - i
        return 0