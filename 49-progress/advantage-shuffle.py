from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted(nums2)
        assigned = {num: [] for num in nums2}
        remaining = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > sorted_nums2[j]:
                assigned[sorted_nums2[j]].append(nums1[i])
                j += 1
            else:
                remaining.append(nums1[i])
            i += 1
        return [assigned[num].pop() if assigned[num] else remaining.pop() for num in nums2]


