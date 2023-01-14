class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k % len(nums)):
            nums.insert(0, nums.pop())
        return nums