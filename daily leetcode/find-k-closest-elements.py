# Find k closest elements
# https://leetcode.com/problems/find-k-closest-elements/

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the index of the closest element
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        # find the k closest elements
        left, right = left - 1, left
        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]
    # technique is to use binary search to find the index of the closest elements
    # then we can use two pointers to find the k closest elements
    # we can use a left pointer and a right pointer
    # we can then move the left pointer to the left and the right pointer to the right
    # until the right pointer is k elements away from the left pointer
    # we can then return the elements between the left pointer and the right pointer
    
    # using bisect
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import bisect
        left = bisect.bisect_left(arr, x)
        right = left
        while right - left < k:
            if left == 0:
                right += 1
            elif right == len(arr):
                left -= 1
            elif x - arr[left - 1] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left:right]
    
    # technique is to use a heap to keep track of the k closest elements
    # we can then push the absolute difference between the element and x and the element
    # onto the heap
    # we can then pop the k elements off the heap and return the elements
    
    # using heapq
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq
        heap = []
        for i in arr:
            heapq.heappush(heap, (abs(i-x), i))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return sorted(res)