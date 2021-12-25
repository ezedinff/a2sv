"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum
of at least k. If there is no such subarray, return -1.

A subArray is a contiguous part of an array.


Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3
"""
import unittest
from collections import deque
from typing import List


def shortestSubArray(nums: List[int], k: int) -> int:
    queue = deque()
    curr = 0
    minCount = 0
    out = -1
    for num in nums:
        # if queue is empty, append num if positive

        if len(queue) == 0:
            if num > 0:
                queue.append((num, 1))
                curr = num
                minCount = 1
                # if one number is already enough, just return 1
                # small optimization, not a big deal
                if curr >= k:
                    return 1

        else:
            # if queue is not empty

            # if num is positive, increment current array sum and counter
            if num > 0:
                queue.append((num, 1))
                curr += num
                minCount += 1

            # if num is not positive, we need to determine
            # whether it is meaningful to append,
            # or just empty the queue and start fresh
            else:
                # if current sum adding the number is still positive,
                # it will be meaningful to proceed, consider case:
                # [1,1,1,1,5,-1,5], k = 9
                if curr + num > 0:
                    curr += num
                    temp = 1
                    # merge the value and count to the elements in queue
                    # [(10,1), (20,1), (-25,1)] -> [(5,3)]
                    while queue:
                        val, count = queue.pop()
                        if val + num > 0:
                            queue.append((val + num, count + temp))
                            break
                        else:
                            num += val
                            temp += count

                    minCount += 1
                # if current sum adding the number is not positive,
                # then it's meaningless to continue with present queue,
                # just start fresh, consider case
                # [1,-2,3], k = 3
                else:
                    curr = 0
                    queue = deque()
        # after processing the number, we recursively popleft
        # till current sum is smaller than k, update output when necessary
        while curr >= k:
            if out == -1 or out > minCount:
                out = minCount
            val, count = queue.popleft()
            curr -= val
            minCount -= count

    return out


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums, k = [2, -1, 2], 3
        expected = 3
        actual = shortestSubArray(nums, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums, k = [1, 2], 4
        expected = 3
        actual = shortestSubArray(nums, k)
        self.assertEqual(expected, actual)