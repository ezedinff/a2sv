from typing import List
import unittest

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
# the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

def maxArea(height: List[int]) -> int:
    # Write your code here
    n = len(height)
    left = 0
    right = n - 1
    max_area = 0
    while left < right:
        # print(left, right)
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            # print(height[left], height[right])
            left += 1
        else:
            right -= 1
    return max_area




class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(maxArea([1,8,6,2,5,4,8,3,7]), 49)