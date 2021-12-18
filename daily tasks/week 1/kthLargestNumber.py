"""
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading
zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest
integer, "2" is the second-largest integer, and "1" is the third-largest integer.

Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".
"""
from typing import List


def kthLargestNumber(nums: List[str], k: int) -> str:
    nums = [int(num) for num in nums]
    nums.sort()
    return str(nums[-k])


print(kthLargestNumber(["3", "6", "7", "10"], 4))
print(kthLargestNumber(["0", "0"], 2))
print(kthLargestNumber(["2", "21", "12", "1"], 3))
