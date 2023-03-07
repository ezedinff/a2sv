'''
Intuition and Algorithm
Given that every element in the sorted array appears exactly twice except for one element,
we can utilize this property to find the single element efficiently.
Specifically, if we take any element at an even index (0-indexed),
the next element should be the same, and if we take any element at an odd index,
the previous element should be the same.

By leveraging this fact, we can employ binary search to compare the middle element
with its adjacent elements, which allows us to determine which side of the array
the single element is on. If the middle element is at an even index, we can deduce
that the single element must be on the right side of the array, as all the elements
on the left side should come in pairs. Conversely, if the middle element is at an odd index,
then the single element must be on the left side of the array.

We can repeat this process by dividing the search range in half each time,
until we ultimately locate the single element.
'''
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                start = mid + 2
            else:
                end = mid
        return nums[start]